"""
Generate tail dependence illustration figure for PhD manuscript introduction.

Compares:
- Left panel: Independent Pareto margins (no tail dependence)
- Right panel: Gumbel copula with Pareto margins (upper tail dependence)

Output: figures/intro/tail_dependence.pdf
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pareto

# Set seed for reproducibility
np.random.seed(42)

# Parameters
n = 500
alpha = 1.5  # Pareto tail index (shape parameter) - consistent with heavy_tails figure
theta = 2.5  # Gumbel copula parameter (theta > 1 for dependence)


def gumbel_copula_sample(n, theta):
    """
    Sample from Gumbel copula using Marshall-Olkin algorithm.

    Parameters
    ----------
    n : int
        Number of samples
    theta : float
        Gumbel parameter (theta >= 1, theta=1 is independence)

    Returns
    -------
    U : ndarray of shape (n, 2)
        Samples with uniform margins and Gumbel dependence
    """
    # Marshall-Olkin: sample from stable distribution
    # For Gumbel, use the algorithm based on stable(1/theta)

    # Sample V from stable distribution with alpha = 1/theta
    # Using the Chambers-Mallows-Stuck algorithm for stable(1/theta, 1, 0, 0)
    alpha_stable = 1.0 / theta

    # Oversample to handle potential NaN values
    n_sample = int(n * 1.5)

    W1 = np.random.uniform(1e-10, np.pi - 1e-10, n_sample)  # Avoid boundary issues
    W2 = np.random.exponential(1, n_sample)

    if alpha_stable == 1:
        V = np.tan(W1)
    else:
        with np.errstate(invalid='ignore', divide='ignore'):
            V = (np.sin(alpha_stable * W1) / (np.cos(W1) ** (1/alpha_stable))) * \
                (np.cos(W1 - alpha_stable * W1) / W2) ** ((1 - alpha_stable) / alpha_stable)

    # Sample independent exponentials
    E1 = np.random.exponential(1, n_sample)
    E2 = np.random.exponential(1, n_sample)

    # Transform to Gumbel copula
    with np.errstate(invalid='ignore', divide='ignore'):
        U1 = np.exp(-(E1 / V) ** (1/theta))
        U2 = np.exp(-(E2 / V) ** (1/theta))

    # Filter out NaN values and take first n valid samples
    valid = np.isfinite(U1) & np.isfinite(U2) & (U1 > 0) & (U1 < 1) & (U2 > 0) & (U2 < 1)
    U1, U2 = U1[valid][:n], U2[valid][:n]

    return np.column_stack([U1, U2])


# Generate samples
# Panel 1: Independent Pareto margins
X1_indep = pareto.rvs(alpha, size=n)
X2_indep = pareto.rvs(alpha, size=n)

# Panel 2: Gumbel copula with Pareto margins (has upper tail dependence)
U = gumbel_copula_sample(n, theta)
X1_dep = pareto.ppf(U[:, 0], alpha)
X2_dep = pareto.ppf(U[:, 1], alpha)

# Plotting
fig, axes = plt.subplots(1, 2, figsize=(10, 4.5))

# Style settings
scatter_kwargs = dict(s=12, alpha=0.6, edgecolors='none')
xlim, ylim = (0, 20), (0, 20)
box_color = 'red'
box_alpha = 0.15
box_edge = 'red'
box_linestyle = '--'
box_linewidth = 1.5

# Threshold for "extreme" region (upper tail)
tail_threshold = 10

# Left panel: Independent
ax = axes[0]
ax.scatter(X1_indep, X2_indep, c='steelblue', **scatter_kwargs)
ax.set_xlabel(r'$X_1$', fontsize=12)
ax.set_ylabel(r'$X_2$', fontsize=12)
ax.set_title('No tail dependence\n(independent Pareto margins)', fontsize=11)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

# Add box highlighting upper tail region (should be sparse)
from matplotlib.patches import Rectangle
rect = Rectangle((tail_threshold, tail_threshold),
                 xlim[1] - tail_threshold, ylim[1] - tail_threshold,
                 linewidth=box_linewidth, linestyle=box_linestyle,
                 edgecolor=box_edge, facecolor=box_color, alpha=box_alpha)
ax.add_patch(rect)

# Count points in tail region
n_tail_indep = np.sum((X1_indep > tail_threshold) & (X2_indep > tail_threshold))
ax.text(xlim[1] - 1, ylim[1] - 1, f'n={n_tail_indep}', ha='right', va='top',
        fontsize=9, color='red')

# Right panel: Gumbel copula (tail dependent)
ax = axes[1]
ax.scatter(X1_dep, X2_dep, c='steelblue', **scatter_kwargs)
ax.set_xlabel(r'$X_1$', fontsize=12)
ax.set_ylabel(r'$X_2$', fontsize=12)
ax.set_title('Upper tail dependence\n(Gumbel copula, Pareto margins)', fontsize=11)
ax.set_xlim(xlim)
ax.set_ylim(ylim)

# Add box highlighting upper tail region (should have clustering)
rect = Rectangle((tail_threshold, tail_threshold),
                 xlim[1] - tail_threshold, ylim[1] - tail_threshold,
                 linewidth=box_linewidth, linestyle=box_linestyle,
                 edgecolor=box_edge, facecolor=box_color, alpha=box_alpha)
ax.add_patch(rect)

# Count points in tail region
n_tail_dep = np.sum((X1_dep > tail_threshold) & (X2_dep > tail_threshold))
ax.text(xlim[1] - 1, ylim[1] - 1, f'n={n_tail_dep}', ha='right', va='top',
        fontsize=9, color='red')

plt.tight_layout()

# Save figure
output_path = '../figures/intro/tail_dependence.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Figure saved to {output_path}")

# Also save as PNG for quick preview
plt.savefig(output_path.replace('.pdf', '.png'), bbox_inches='tight', dpi=150)
print(f"Preview saved to {output_path.replace('.pdf', '.png')}")

plt.show()
