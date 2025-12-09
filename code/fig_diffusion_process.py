"""
Generate diffusion process illustration figure for PhD manuscript introduction.

Shows forward (noising) and reverse (denoising) processes on a 2D Gaussian mixture.

Forward: x_0 ~ p_data → x_t → x_T ~ N(0, I)
Reverse: x_T ~ N(0, I) → x_t → x_0 ~ p_data

Output: figures/intro/diffusion_process.pdf
"""

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from scipy.stats import multivariate_normal

# Set seed for reproducibility
np.random.seed(123)

# Parameters
n_samples = 400
n_timesteps = 5  # Number of snapshots to show (including t=0 and t=T)
T = 1.0  # Final time

# Gaussian mixture parameters (two clusters)
means = [np.array([-2, 0]), np.array([2, 0])]
cov = np.array([[0.3, 0], [0, 0.3]])
weights = [0.5, 0.5]


def sample_gaussian_mixture(n):
    """Sample from a 2-component Gaussian mixture."""
    samples = []
    for _ in range(n):
        # Choose component
        k = np.random.choice(len(weights), p=weights)
        # Sample from that component
        samples.append(np.random.multivariate_normal(means[k], cov))
    return np.array(samples)


def forward_process(x_0, t, T=1.0):
    """
    Forward diffusion: x_t = sqrt(alpha_t) * x_0 + sqrt(1 - alpha_t) * noise

    Using variance-preserving SDE with alpha_t = exp(-t)
    At t=0: x_0 (data)
    At t=T: approximately N(0, I)
    """
    alpha_t = np.exp(-2 * t / T)  # Decay schedule
    noise = np.random.randn(*x_0.shape)
    x_t = np.sqrt(alpha_t) * x_0 + np.sqrt(1 - alpha_t) * noise
    return x_t


def get_timesteps(n_steps, T=1.0):
    """Get evenly spaced timesteps including 0 and T."""
    return np.linspace(0, T, n_steps)


def compute_marginal_density(x_grid, y_grid, t, T=1.0):
    """
    Compute the theoretical marginal density p_t(x) at time t.

    For the forward process with x_t = sqrt(alpha_t) * x_0 + sqrt(1 - alpha_t) * noise,
    if x_0 ~ mixture of Gaussians, then x_t is also a mixture of Gaussians with:
    - means scaled by sqrt(alpha_t)
    - covariances: alpha_t * cov_0 + (1 - alpha_t) * I
    """
    alpha_t = np.exp(-2 * t / T)

    # Covariance at time t
    cov_t = alpha_t * cov + (1 - alpha_t) * np.eye(2)

    # Evaluate density on grid
    pos = np.dstack((x_grid, y_grid))
    density = np.zeros_like(x_grid)

    for k, (mean, weight) in enumerate(zip(means, weights)):
        # Mean at time t
        mean_t = np.sqrt(alpha_t) * mean
        rv = multivariate_normal(mean_t, cov_t)
        density += weight * rv.pdf(pos)

    return density


# Generate data
x_0 = sample_gaussian_mixture(n_samples)

# Get timesteps
timesteps = get_timesteps(n_timesteps, T)

# Generate forward process snapshots
forward_snapshots = []
for t in timesteps:
    x_t = forward_process(x_0, t, T)
    forward_snapshots.append(x_t)

# For reverse process, we simulate by going backwards through similar states
# (In practice this would use the learned score, but for illustration we just show
# the same marginal distributions in reverse order)
reverse_snapshots = forward_snapshots[::-1]

# Create grid for density evaluation
grid_points = 100
x_range = np.linspace(-4.5, 4.5, grid_points)
y_range = np.linspace(-4.5, 4.5, grid_points)
x_grid, y_grid = np.meshgrid(x_range, y_range)

# Plotting - increase height to make room for SDE annotations
fig, axes = plt.subplots(2, n_timesteps, figsize=(12, 6.5))

# Style settings
scatter_kwargs = dict(s=6, alpha=0.7, edgecolors='none')
xlim, ylim = (-4.5, 4.5), (-4.5, 4.5)

# Colors: blue for data, gray for noise, gradient in between
colors_forward = plt.cm.Blues(np.linspace(0.7, 0.3, n_timesteps))
colors_reverse = plt.cm.Reds(np.linspace(0.3, 0.7, n_timesteps))

# Top row: Forward process
for i, (t, x_t) in enumerate(zip(timesteps, forward_snapshots)):
    ax = axes[0, i]

    # Compute and plot theoretical density as background
    density = compute_marginal_density(x_grid, y_grid, t, T)
    ax.contourf(x_grid, y_grid, density, levels=20, cmap='Blues', alpha=0.4)
    ax.contour(x_grid, y_grid, density, levels=5, colors='steelblue', alpha=0.5, linewidths=0.5)

    # Plot samples on top
    ax.scatter(x_t[:, 0], x_t[:, 1], c='black', **scatter_kwargs)

    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])

    # Time label - use fractions of T for consistency
    if i == 0:
        ax.set_title(r'$t = 0$' + '\n(data)', fontsize=10)
    elif i == n_timesteps - 1:
        ax.set_title(r'$t = T$' + '\n(noise)', fontsize=10)
    else:
        # Express as fraction of T
        frac = t / T
        if frac == 0.25:
            ax.set_title(r'$t = T/4$', fontsize=10)
        elif frac == 0.5:
            ax.set_title(r'$t = T/2$', fontsize=10)
        elif frac == 0.75:
            ax.set_title(r'$t = 3T/4$', fontsize=10)
        else:
            ax.set_title(f'$t = {frac:.2f}T$', fontsize=10)

# Bottom row: Reverse process
for i, (t, x_t) in enumerate(zip(timesteps[::-1], reverse_snapshots)):
    ax = axes[1, i]

    # Compute and plot theoretical density as background
    density = compute_marginal_density(x_grid, y_grid, t, T)
    ax.contourf(x_grid, y_grid, density, levels=20, cmap='Reds', alpha=0.4)
    ax.contour(x_grid, y_grid, density, levels=5, colors='firebrick', alpha=0.5, linewidths=0.5)

    # Plot samples on top
    ax.scatter(x_t[:, 0], x_t[:, 1], c='black', **scatter_kwargs)

    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])

    # Time label - use fractions of T for consistency
    if i == 0:
        ax.set_title(r'$t = T$' + '\n(noise)', fontsize=10)
    elif i == n_timesteps - 1:
        ax.set_title(r'$t = 0$' + '\n(generated)', fontsize=10)
    else:
        # Express as fraction of T
        frac = t / T
        if frac == 0.25:
            ax.set_title(r'$t = T/4$', fontsize=10)
        elif frac == 0.5:
            ax.set_title(r'$t = T/2$', fontsize=10)
        elif frac == 0.75:
            ax.set_title(r'$t = 3T/4$', fontsize=10)
        else:
            ax.set_title(f'$t = {frac:.2f}T$', fontsize=10)

# Row labels
axes[0, 0].set_ylabel('Forward', fontsize=11, labelpad=10)
axes[1, 0].set_ylabel('Reverse', fontsize=11, labelpad=10)

# Add SDE arrows and equations between title and panels
from matplotlib.patches import FancyArrowPatch

plt.subplots_adjust(top=0.85, bottom=0.08, hspace=0.45)

# Forward SDE: arrow and equation above the top row panels
# VP-SDE: dX_t = -X_t dt + sqrt(2) dW_t
fig.text(0.5, 0.91, r'$\mathrm{d}X_t = -X_t\,\mathrm{d}t + \sqrt{2}\,\mathrm{d}W_t$',
         ha='center', va='center', fontsize=12, transform=fig.transFigure)

arrow_forward = FancyArrowPatch((0.13, 0.88), (0.87, 0.88),
                                 arrowstyle='->', mutation_scale=15,
                                 color='steelblue', lw=2,
                                 transform=fig.transFigure, figure=fig)
fig.patches.append(arrow_forward)

# Reverse SDE: arrow and equation above the bottom row panels
# Reverse: dX_t = [-X_t - 2*score] dt + sqrt(2) dW_t
fig.text(0.5, 0.46, r'$\mathrm{d}X_t = \left[-X_t + 2\,s_\theta(X_t, t)\right]\mathrm{d}t + \sqrt{2}\,\mathrm{d}\bar{W}_t$',
         ha='center', va='center', fontsize=12, transform=fig.transFigure)

arrow_reverse = FancyArrowPatch((0.13, 0.43), (0.87, 0.43),
                                 arrowstyle='->', mutation_scale=15,
                                 color='firebrick', lw=2,
                                 transform=fig.transFigure, figure=fig)
fig.patches.append(arrow_reverse)

# Add arrows between panels using axes annotate
# Forward arrows (top row)
for i in range(n_timesteps - 1):
    ax_left = axes[0, i]
    ax_right = axes[0, i + 1]

    # Arrow from right edge of left panel to left edge of right panel
    ax_left.annotate('',
                     xy=(0.02, 0.5), xycoords=ax_right.transAxes,
                     xytext=(0.98, 0.5), textcoords=ax_left.transAxes,
                     arrowprops=dict(arrowstyle='->', color='steelblue', lw=1.5))

# Reverse arrows (bottom row)
for i in range(n_timesteps - 1):
    ax_left = axes[1, i]
    ax_right = axes[1, i + 1]

    ax_left.annotate('',
                     xy=(0.02, 0.5), xycoords=ax_right.transAxes,
                     xytext=(0.98, 0.5), textcoords=ax_left.transAxes,
                     arrowprops=dict(arrowstyle='->', color='firebrick', lw=1.5))

# Note: subplots_adjust already called above for SDE annotations
plt.subplots_adjust(top=0.85, bottom=0.08, hspace=0.45, wspace=0.15)

# Save figure
output_path = '../figures/intro/diffusion_process.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Figure saved to {output_path}")

# Also save as PNG for quick preview
plt.savefig(output_path.replace('.pdf', '.png'), bbox_inches='tight', dpi=150)
print(f"Preview saved to {output_path.replace('.pdf', '.png')}")
