"""
Generate GAN framework illustration for PhD manuscript introduction.

Shows the adversarial game: Generator (counterfeiter) vs Discriminator (detective).

Output: figures/intro/gan_framework.pdf
"""

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Create figure
fig, ax = plt.subplots(figsize=(12, 5))

# Colors
gen_color = '#4A90D9'      # Blue
disc_color = '#E74C3C'     # Red
data_color = '#27AE60'     # Green
arrow_color = '#555555'

# Box positions and sizes
box_height = 0.8
box_width = 1.8

# Generator box
gen_x, gen_y = 1.5, 2
gen_box = FancyBboxPatch((gen_x - box_width/2, gen_y - box_height/2),
                          box_width, box_height,
                          boxstyle="round,pad=0.05,rounding_size=0.15",
                          facecolor=gen_color, edgecolor='black', linewidth=2, alpha=0.85)
ax.add_patch(gen_box)
ax.text(gen_x, gen_y + 0.1, 'Generator', ha='center', va='center', fontsize=12, fontweight='bold', color='white')
ax.text(gen_x, gen_y - 0.2, '(Counterfeiter)', ha='center', va='center', fontsize=9, color='white', style='italic')

# Noise input
ax.text(0, 2, 'Noise $Z$', ha='center', va='center', fontsize=11)
ax.annotate('', xy=(gen_x - box_width/2 - 0.1, gen_y), xytext=(0.5, gen_y),
            arrowprops=dict(arrowstyle='->', color=arrow_color, lw=2))

# Fake samples
ax.text(4.2, 2, 'Fake\nsamples', ha='center', va='center', fontsize=10)
ax.annotate('', xy=(3.8, gen_y), xytext=(gen_x + box_width/2 + 0.1, gen_y),
            arrowprops=dict(arrowstyle='->', color=arrow_color, lw=2))

# Real data box
data_x, data_y = 5.5, 3.5
data_box = FancyBboxPatch((data_x - box_width/2, data_y - box_height/2),
                           box_width, box_height,
                           boxstyle="round,pad=0.05,rounding_size=0.15",
                           facecolor=data_color, edgecolor='black', linewidth=2, alpha=0.85)
ax.add_patch(data_box)
ax.text(data_x, data_y + 0.1, 'Real Data', ha='center', va='center', fontsize=12, fontweight='bold', color='white')
ax.text(data_x, data_y - 0.2, '(Genuine notes)', ha='center', va='center', fontsize=9, color='white', style='italic')

# Discriminator box
disc_x, disc_y = 7.5, 2
disc_box = FancyBboxPatch((disc_x - box_width/2, disc_y - box_height/2),
                           box_width, box_height,
                           boxstyle="round,pad=0.05,rounding_size=0.15",
                           facecolor=disc_color, edgecolor='black', linewidth=2, alpha=0.85)
ax.add_patch(disc_box)
ax.text(disc_x, disc_y + 0.1, 'Discriminator', ha='center', va='center', fontsize=12, fontweight='bold', color='white')
ax.text(disc_x, disc_y - 0.2, '(Detective)', ha='center', va='center', fontsize=9, color='white', style='italic')

# Arrow from fake to discriminator
ax.annotate('', xy=(disc_x - box_width/2 - 0.1, disc_y), xytext=(4.6, disc_y),
            arrowprops=dict(arrowstyle='->', color=arrow_color, lw=2))

# Arrow from real data to discriminator
ax.annotate('', xy=(disc_x - 0.3, disc_y + box_height/2 + 0.1), xytext=(data_x + 0.3, data_y - box_height/2 - 0.1),
            arrowprops=dict(arrowstyle='->', color=arrow_color, lw=2))

# Output
ax.text(10, 2, 'Real or Fake?\n$D(x) \\in [0,1]$', ha='center', va='center', fontsize=10)
ax.annotate('', xy=(9.3, disc_y), xytext=(disc_x + box_width/2 + 0.1, disc_y),
            arrowprops=dict(arrowstyle='->', color=arrow_color, lw=2))

# Feedback loop: discriminator to generator (curved below)
ax.annotate('', xy=(gen_x, gen_y - box_height/2 - 0.1), xytext=(disc_x, disc_y - box_height/2 - 0.1),
            arrowprops=dict(arrowstyle='->', color=gen_color, lw=1.5, linestyle='dashed',
                           connectionstyle='arc3,rad=-0.3'))
ax.text(4.5, 0.7, 'Improve to fool', ha='center', va='center', fontsize=9, color=gen_color)

# Feedback loop: output to discriminator
ax.annotate('', xy=(disc_x, disc_y + box_height/2 + 0.1), xytext=(9.5, disc_y + 0.8),
            arrowprops=dict(arrowstyle='->', color=disc_color, lw=1.5, linestyle='dashed',
                           connectionstyle='arc3,rad=-0.2'))
ax.text(9.2, 3.2, 'Improve to detect', ha='center', va='center', fontsize=9, color=disc_color)

# Formatting
ax.set_xlim(-0.5, 11)
ax.set_ylim(0.3, 4.3)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()

# Save figure
output_path = '../figures/intro/gan_framework.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Figure saved to {output_path}")

# Also save as PNG for quick preview
plt.savefig(output_path.replace('.pdf', '.png'), bbox_inches='tight', dpi=150)
print(f"Preview saved to {output_path.replace('.pdf', '.png')}")
