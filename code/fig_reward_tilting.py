"""
Generate reward tilting illustration figure for PhD manuscript introduction.

Shows how exponential tilting shifts a Gaussian distribution toward high-reward regions.

p_0 = N(2, 1)  (base distribution)
r(x) = x       (linear reward)
lambda = 1.5   (tilting strength)
p(x) propto p_0(x) * exp(lambda * r(x)) = N(2 + lambda*sigma^2, sigma^2) = N(3.5, 1)

Output: figures/intro/reward_tilting.pdf
"""

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mu_0 = 2.0        # Mean of base distribution
sigma = 1.0       # Standard deviation (same for both)
lam = 1.5         # Tilting strength (lambda)
mu_tilted = mu_0 + lam * sigma**2  # = 3.5

# Create figure
fig, ax = plt.subplots(figsize=(8, 5))

# x range
x = np.linspace(-1, 7, 500)

# Base distribution p_0
p0 = norm.pdf(x, mu_0, sigma)
ax.plot(x, p0, 'b-', linewidth=2.5, label=r'$p_0(x) = \mathcal{N}(2, 1)$')
ax.fill_between(x, p0, alpha=0.15, color='blue')

# Tilted distribution p
p_tilted = norm.pdf(x, mu_tilted, sigma)
ax.plot(x, p_tilted, 'r-', linewidth=2.5, label=r'$p(x) = \mathcal{N}(3.5, 1)$')
ax.fill_between(x, p_tilted, alpha=0.15, color='red')

# Reward function r(x) = x (scaled for display)
r_scale = 0.12  # Scale factor to fit on plot
r_line = r_scale * x
ax.plot(x, r_line, 'g--', linewidth=2, label=r'$r(x) = x$', alpha=0.8)

# Arrow showing the shift
arrow_y = 0.22
ax.annotate('', xy=(mu_tilted, arrow_y), xytext=(mu_0, arrow_y),
            arrowprops=dict(arrowstyle='->', color='gray', lw=2))
ax.text((mu_0 + mu_tilted)/2, arrow_y - 0.04, r'$+\lambda\sigma^2$',
        ha='center', va='top', fontsize=11, color='gray')

# Vertical lines at means
ax.axvline(mu_0, color='blue', linestyle=':', alpha=0.5, linewidth=1)
ax.axvline(mu_tilted, color='red', linestyle=':', alpha=0.5, linewidth=1)

# Lambda annotation
ax.text(6.2, 0.35, r'$\lambda = 1.5$', fontsize=11, color='gray')

# Formatting
ax.set_xlim(-0.5, 7)
ax.set_ylim(0, 0.5)
ax.set_xlabel(r'$x$', fontsize=12)
ax.set_ylabel('Density', fontsize=12)
ax.legend(loc='upper right', fontsize=11, framealpha=0.9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Grid
ax.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)

plt.tight_layout()

# Save figure
output_path = '../figures/intro/reward_tilting.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Figure saved to {output_path}")

# Also save as PNG for quick preview
plt.savefig(output_path.replace('.pdf', '.png'), bbox_inches='tight', dpi=150)
print(f"Preview saved to {output_path.replace('.pdf', '.png')}")
