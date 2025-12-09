"""
Generate heavy-tailed vs light-tailed density comparison.

Shows |Gaussian|, exponential (light-tailed) vs Pareto (heavy-tailed) densities,
illustrating why extreme values are far more likely under heavy tails.

Output: figures/intro/heavy_tails.pdf
"""

import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Create figure with two subplots stacked vertically, full width
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 9), sharex=True)

# Parameters
alpha = 1.5  # Pareto shape (heavier tail than alpha=2)
lam = 1.0    # Exponential rate
sigma = 1.0  # Gaussian std

# x range for both plots
x = np.linspace(0.01, 20, 2000)

# Half-normal (|Gaussian|): f(x) = 2/sqrt(2*pi*sigma^2) * exp(-x^2/(2*sigma^2)) for x >= 0
half_normal_density = 2 * stats.norm.pdf(x, 0, sigma)

# Exponential: f(x) = lambda * exp(-lambda * x)
exp_density = lam * np.exp(-lam * x)

# Pareto (shifted to start at 0): f(x) = alpha / (1+x)^(alpha+1)
pareto_density = alpha / (1 + x)**(alpha + 1)

# Top plot: densities
ax1.plot(x, half_normal_density, 'g-', lw=2.5, label=r'$|$Gaussian$|$ ($\sigma=1$)')
ax1.plot(x, exp_density, 'b-', lw=2.5, label=r'Exponential ($\lambda=1$)')
ax1.plot(x, pareto_density, 'r-', lw=2.5, label=r'Pareto ($\alpha=1.5$)')

ax1.set_ylabel('Density $f(x)$', fontsize=12)
ax1.set_xlim(0, 20)
ax1.set_ylim(0, 0.15)
ax1.legend(fontsize=11, loc='upper right')
ax1.set_title('Density comparison', fontsize=12)
ax1.grid(True, alpha=0.3)

# Bottom plot: log-scale survival functions (tail probabilities)
# Survival functions P(X > x)
half_normal_survival = 2 * (1 - stats.norm.cdf(x, 0, sigma))
exp_survival = np.exp(-lam * x)
pareto_survival = 1 / (1 + x)**alpha

ax2.semilogy(x, half_normal_survival, 'g-', lw=2.5, label=r'$|$Gaussian$|$')
ax2.semilogy(x, exp_survival, 'b-', lw=2.5, label=r'Exponential')
ax2.semilogy(x, pareto_survival, 'r-', lw=2.5, label=r'Pareto')

ax2.set_xlabel('$x$', fontsize=12)
ax2.set_ylabel(r'Tail probability $\mathbb{P}(X > x)$', fontsize=12)
ax2.set_xlim(0, 20)
ax2.set_ylim(1e-15, 1)
ax2.legend(fontsize=11, loc='upper right')
ax2.set_title('Tail probability (log scale)', fontsize=12)
ax2.grid(True, alpha=0.3, which='both')

# Add vertical lines at key thresholds
for t in [5, 10, 15]:
    ax1.axvline(x=t, color='gray', linestyle='--', alpha=0.4, lw=1)
    ax2.axvline(x=t, color='gray', linestyle='--', alpha=0.4, lw=1)

plt.tight_layout()

# Save figure
output_path = '../figures/intro/heavy_tails.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Figure saved to {output_path}")

plt.savefig(output_path.replace('.pdf', '.png'), bbox_inches='tight', dpi=150)
print(f"Preview saved to {output_path.replace('.pdf', '.png')}")

# Print table values
print("\nTable: Probability of exceeding threshold t")
print("-" * 65)
print(f"{'t':>6} | {'|Gaussian|':>15} | {'Exponential':>15} | {'Pareto':>15}")
print("-" * 65)
for t in [3, 5, 8, 10]:
    gauss_p = 2 * (1 - stats.norm.cdf(t, 0, sigma))
    exp_p = np.exp(-lam * t)
    par_p = 1 / (1 + t)**alpha
    print(f"{t:>6} | {gauss_p:>15.2e} | {exp_p:>15.2e} | {par_p:>15.2e}")
