import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(12, 8))

# Flag dimensions
flag_width = 10
flag_height = 6

# Draw horizontal stripes
# Black stripe (top)
black_stripe = patches.Rectangle((0, 4), flag_width, 2, 
                                  facecolor='black', edgecolor='none')
ax.add_patch(black_stripe)

# Red stripe (middle)
red_stripe = patches.Rectangle((0, 2), flag_width, 2, 
                                facecolor='#BB0000', edgecolor='none')
ax.add_patch(red_stripe)

# Green stripe (bottom)
green_stripe = patches.Rectangle((0, 0), flag_width, 2, 
                                  facecolor='#006600', edgecolor='none')
ax.add_patch(green_stripe)

# White borders around red stripe
white_top = patches.Rectangle((0, 3.8), flag_width, 0.2, 
                               facecolor='white', edgecolor='none')
white_bottom = patches.Rectangle((0, 2), flag_width, 0.2, 
                                  facecolor='white', edgecolor='none')
ax.add_patch(white_top)
ax.add_patch(white_bottom)

# Central Maasai shield (red)
shield_center_x = flag_width / 2
shield_center_y = flag_height / 2
shield_width = 1.5
shield_height = 2.5

shield = patches.Ellipse((shield_center_x, shield_center_y), 
                         shield_width, shield_height,
                         facecolor='#BB0000', edgecolor='white', linewidth=3)
ax.add_patch(shield)

# White inner ellipse on shield
inner_shield = patches.Ellipse((shield_center_x, shield_center_y), 
                               shield_width * 0.6, shield_height * 0.8,
                               facecolor='white', edgecolor='none')
ax.add_patch(inner_shield)

# Black center of shield
center_shield = patches.Ellipse((shield_center_x, shield_center_y), 
                                shield_width * 0.4, shield_height * 0.6,
                                facecolor='black', edgecolor='none')
ax.add_patch(center_shield)

# Draw two crossed spears (white)
spear_length = 3.5
angle1 = np.radians(25)
angle2 = np.radians(-25)

# Left spear
x1_start = shield_center_x - spear_length/2 * np.cos(angle1)
y1_start = shield_center_y - spear_length/2 * np.sin(angle1)
x1_end = shield_center_x + spear_length/2 * np.cos(angle1)
y1_end = shield_center_y + spear_length/2 * np.sin(angle1)
ax.plot([x1_start, x1_end], [y1_start, y1_end], 'white', linewidth=4)

# Right spear
x2_start = shield_center_x - spear_length/2 * np.cos(angle2)
y2_start = shield_center_y - spear_length/2 * np.sin(angle2)
x2_end = shield_center_x + spear_length/2 * np.cos(angle2)
y2_end = shield_center_y + spear_length/2 * np.sin(angle2)
ax.plot([x2_start, x2_end], [y2_start, y2_end], 'white', linewidth=4)

# Set limits and remove axes
ax.set_xlim(0, flag_width)
ax.set_ylim(0, flag_height)
ax.set_aspect('equal')
ax.axis('off')

plt.title('Flag of Kenya', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('kenyan_flag.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()

print("Kenyan flag created successfully!")
print("The flag has been saved as 'kenyan_flag.png'")
