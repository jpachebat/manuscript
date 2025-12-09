"""
Generate neural network architecture illustration for PhD manuscript introduction.

Shows a feedforward neural network with multiple hidden layers:
h_0 = x (input) -> h_1 -> h_2 -> ... -> h_{L-1} -> h_L -> g(x) (output)

Output: figures/intro/neural_network.pdf
"""

import matplotlib
matplotlib.use('Agg')  # Non-interactive backend

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import matplotlib.patches as mpatches

# Network architecture
n_input = 3       # Input neurons (showing h_0 = x)
n_hidden = 4      # Neurons per hidden layer
n_output = 1      # Output neuron g(x)

# Layer positions (x-coordinates):
# h_0, h_1, h_2, dots, h_{L-1}, h_L, output
layer_x = [0, 1.6, 3.0, 4.3, 5.6, 7.0, 8.6]

# Vertical spacing
def get_y_positions(n_neurons, max_neurons=4):
    """Get y positions for neurons, centered around 0."""
    if n_neurons == 1:
        return [0]
    spacing = 0.9
    total_height = (n_neurons - 1) * spacing
    return [total_height/2 - i * spacing for i in range(n_neurons)]

# Create figure - BIGGER
fig, ax = plt.subplots(figsize=(14, 7))

# Colors
input_color = '#4A90D9'      # Blue
hidden_color = '#F5A623'     # Orange
output_color = '#7ED321'     # Green
edge_color = '#666666'

# Neuron radius - MUCH BIGGER
radius = 0.32

# Store neuron positions for drawing connections
layers = []

# Input layer (h_0 = x)
input_y = get_y_positions(n_input)
input_neurons = [(layer_x[0], y) for y in input_y]
layers.append(input_neurons)

# Hidden layer 1 (h_1)
hidden1_y = get_y_positions(n_hidden)
hidden1_neurons = [(layer_x[1], y) for y in hidden1_y]
layers.append(hidden1_neurons)

# Hidden layer 2 (h_2)
hidden2_y = get_y_positions(n_hidden)
hidden2_neurons = [(layer_x[2], y) for y in hidden2_y]
layers.append(hidden2_neurons)

# (dots at position 3)

# Hidden layer L-1 (h_{L-1})
hiddenLm1_y = get_y_positions(n_hidden)
hiddenLm1_neurons = [(layer_x[4], y) for y in hiddenLm1_y]
layers.append(hiddenLm1_neurons)

# Hidden layer L (h_L)
hiddenL_y = get_y_positions(n_hidden)
hiddenL_neurons = [(layer_x[5], y) for y in hiddenL_y]
layers.append(hiddenL_neurons)

# Output layer g(x)
output_y = get_y_positions(n_output)
output_neurons = [(layer_x[6], y) for y in output_y]
layers.append(output_neurons)

# Draw connections - THICKER
linewidth = 0.9
alpha = 0.3

# Draw connections: input to h1
for (x1, y1) in layers[0]:
    for (x2, y2) in layers[1]:
        ax.plot([x1 + radius, x2 - radius], [y1, y2],
               color=edge_color, alpha=alpha, linewidth=linewidth, zorder=1)

# Draw connections: h1 to h2
for (x1, y1) in layers[1]:
    for (x2, y2) in layers[2]:
        ax.plot([x1 + radius, x2 - radius], [y1, y2],
               color=edge_color, alpha=alpha, linewidth=linewidth, zorder=1)

# Draw connections: h_{L-1} to h_L
for (x1, y1) in layers[3]:
    for (x2, y2) in layers[4]:
        ax.plot([x1 + radius, x2 - radius], [y1, y2],
               color=edge_color, alpha=alpha, linewidth=linewidth, zorder=1)

# Draw connections: hL to output
for (x1, y1) in layers[4]:
    for (x2, y2) in layers[5]:
        ax.plot([x1 + radius, x2 - radius], [y1, y2],
               color=edge_color, alpha=alpha, linewidth=linewidth, zorder=1)

# Draw neurons - THICKER EDGE
def draw_neuron(ax, x, y, color, label=None, fontsize=14):
    circle = Circle((x, y), radius, facecolor=color, edgecolor='black',
                   linewidth=2.5, zorder=2, alpha=0.9)
    ax.add_patch(circle)
    if label:
        ax.text(x, y, label, ha='center', va='center', fontsize=fontsize,
               fontweight='bold', zorder=3)

# Input neurons (h_0 = x)
for i, (x, y) in enumerate(input_neurons):
    draw_neuron(ax, x, y, input_color)

# Add vdots in input layer
ax.text(layer_x[0], (input_y[1] + input_y[2])/2, r'$\vdots$',
       ha='center', va='center', fontsize=24)

# Hidden layer 1 neurons (h_1)
for i, (x, y) in enumerate(hidden1_neurons):
    draw_neuron(ax, x, y, hidden_color, r'$\sigma$', fontsize=18)

# Hidden layer 2 neurons (h_2)
for i, (x, y) in enumerate(hidden2_neurons):
    draw_neuron(ax, x, y, hidden_color, r'$\sigma$', fontsize=18)

# Horizontal dots between h_2 and h_{L-1}
dots_x = layer_x[3]
ax.text(dots_x, 0, r'$\cdots$', ha='center', va='center', fontsize=36, color='gray')

# Hidden layer L-1 neurons (h_{L-1})
for i, (x, y) in enumerate(hiddenLm1_neurons):
    draw_neuron(ax, x, y, hidden_color, r'$\sigma$', fontsize=18)

# Hidden layer L neurons (h_L)
for i, (x, y) in enumerate(hiddenL_neurons):
    draw_neuron(ax, x, y, hidden_color, r'$\sigma$', fontsize=18)

# Output neuron
draw_neuron(ax, output_neurons[0][0], output_neurons[0][1], output_color, r'$g(x)$', fontsize=16)

# Layer labels at top - MAIN TEXT SIZE
label_y_top = 1.75
ax.text(layer_x[0], label_y_top, r'$h_0 = x$', ha='center', va='bottom', fontsize=20)
ax.text(layer_x[1], label_y_top, r'$h_1$', ha='center', va='bottom', fontsize=20)
ax.text(layer_x[2], label_y_top, r'$h_2$', ha='center', va='bottom', fontsize=20)
ax.text(layer_x[4], label_y_top, r'$h_{L-1}$', ha='center', va='bottom', fontsize=20)
ax.text(layer_x[5], label_y_top, r'$h_L$', ha='center', va='bottom', fontsize=20)
ax.text(layer_x[6], label_y_top, r'$g(x)$', ha='center', va='bottom', fontsize=20)

# Layer labels at bottom - MAIN TEXT SIZE
label_y = -2.0
ax.text(layer_x[0], label_y, 'Input\n' + r'$x \in \mathbb{R}^d$',
       ha='center', va='top', fontsize=18)
ax.text((layer_x[1] + layer_x[5])/2, label_y, 'Hidden layers\n' + r'$h_1, h_2, \ldots, h_{L-1}, h_L$',
       ha='center', va='top', fontsize=18)
ax.text(layer_x[6], label_y, 'Output\n' + r'$g(x) \in \mathbb{R}$',
       ha='center', va='top', fontsize=18)

# Weight annotations - MAIN TEXT SIZE
ax.annotate(r'$W_1, b_1$', xy=(0.75, 1.25), fontsize=18, color='gray')
ax.annotate(r'$W_2, b_2$', xy=(2.2, 1.25), fontsize=18, color='gray')
ax.annotate(r'$W_{L-1}, b_{L-1}$', xy=(4.3, 1.25), fontsize=18, color='gray', ha='center')
ax.annotate(r'$W_L, b_L$', xy=(6.2, 1.25), fontsize=18, color='gray')
ax.annotate(r'$W_{L+1}$', xy=(7.6, 0.5), fontsize=18, color='gray')

# Brace for hidden layers
brace_y = -1.55
ax.plot([layer_x[1], layer_x[5]], [brace_y, brace_y], 'k-', linewidth=1.2)
ax.plot([layer_x[1], layer_x[1]], [brace_y + 0.06, brace_y - 0.06], 'k-', linewidth=1.2)
ax.plot([layer_x[5], layer_x[5]], [brace_y + 0.06, brace_y - 0.06], 'k-', linewidth=1.2)

# Formatting
ax.set_xlim(-0.9, 9.5)
ax.set_ylim(-2.6, 2.2)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()

# Save figure
output_path = '../figures/intro/neural_network.pdf'
plt.savefig(output_path, bbox_inches='tight', dpi=300)
print(f"Figure saved to {output_path}")

# Also save as PNG for quick preview
plt.savefig(output_path.replace('.pdf', '.png'), bbox_inches='tight', dpi=150)
print(f"Preview saved to {output_path.replace('.pdf', '.png')}")
