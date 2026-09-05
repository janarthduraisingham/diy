import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt

import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# --- Shape 1: Cuboid ---
def cuboid(x, y, z, dx, dy, dz):
    v = np.array([
        [x,     y,     z],
        [x+dx,  y,     z],
        [x+dx,  y+dy,  z],
        [x,     y+dy,  z],
        [x,     y,     z+dz],
        [x+dx,  y,     z+dz],
        [x+dx,  y+dy,  z+dz],
        [x,     y+dy,  z+dz]
    ])
    faces = [
        [v[0], v[1], v[2], v[3]],
        [v[4], v[5], v[6], v[7]],
        [v[0], v[1], v[5], v[4]],
        [v[2], v[3], v[7], v[6]],
        [v[1], v[2], v[6], v[5]],
        [v[0], v[3], v[7], v[4]]
    ]
    return faces

opacity=1

# 2x4 dimensions
d1 = 2 * 0.0254
d2 = 4 * 0.0254

# Rack parameters
rack_height = 1
rack_width = 0.75
spacing = 0.05

# Legs
back_left_leg = cuboid(0, 0, 0, d2, -d1, rack_height)
back_right_leg = cuboid(rack_width-d2, 0, 0, d2, -d1, rack_height)

middle_left_leg = cuboid(0, -0.5, 0, d2, -d1, rack_height)
middle_right_leg = cuboid(rack_width-d2, -0.5, 0, d2, -d1, rack_height)

front_left_leg = cuboid(0, -1, 0, d2, -d1, rack_height/2)
front_right_leg = cuboid(rack_width-d2, -1, 0, d2, -d1, rack_height/2)

# Crossbars
front_crossbar_1 = cuboid(0, -1-d1, rack_height/2,
                        rack_width, d2, d1)
front_crossbar_2 = cuboid(0, -1-d1 + (d2+spacing), rack_height/2,
                        rack_width, d2, d1)
front_crossbar_3 = cuboid(0, -1-d1 + 2*(d2+spacing), rack_height/2,
                        rack_width, d2, d1)
back_crossbar_1 = cuboid(0, -0.5-d1, rack_height,
                        rack_width, d2, d1)
back_crossbar_2 = cuboid(0, -0.5-d1 + 1*(spacing+d2), rack_height,
                        rack_width, d2, d1)
back_crossbar_3 = cuboid(0, -0.5-d1 + 2*(spacing+d2), rack_height,
                        rack_width, d2, d1)

# Longitudinal bars
lower_left_long_bar = cuboid(d2, 0, rack_height/2 - d2,
                             d1, -1-d1, d2)
lower_right_long_bar = cuboid(rack_width - d2 - d1, 0, rack_height/2 - d2,
                             d1, -1-d1, d2)

upper_left_long_bar = cuboid(d2, 0, rack_height - d2,
                             d1, -0.5-d1, d2)
upper_right_long_bar = cuboid(rack_width - d2 - d1, 0, rack_height - d2,
                             d1, -0.5-d1, d2)

# Walls

back_wall = cuboid(0, 0, 0, rack_width, 0.01, rack_height)
left_wall = cuboid(0-0.01, 0, 0, 0.01, -0.5, rack_height)
right_wall = cuboid(rack_width, 0, 0, 0.01, -0.5, rack_height)

# Legs
ax.add_collection3d(Poly3DCollection(back_left_leg, facecolors='lightblue', edgecolors='black', alpha=opacity))
ax.add_collection3d(Poly3DCollection(back_right_leg, facecolors='lightblue', edgecolors='black', alpha=opacity))
ax.add_collection3d(Poly3DCollection(middle_left_leg, facecolors='lightblue', edgecolors='black', alpha=opacity))
ax.add_collection3d(Poly3DCollection(middle_right_leg, facecolors='lightblue', edgecolors='black', alpha=opacity))
ax.add_collection3d(Poly3DCollection(front_left_leg, facecolors='lightblue', edgecolors='black', alpha=opacity))
ax.add_collection3d(Poly3DCollection(front_right_leg, facecolors='lightblue', edgecolors='black', alpha=opacity))

# Crossbars
ax.add_collection3d(Poly3DCollection(front_crossbar_1, facecolors='lightgreen', edgecolors='black', alpha=opacity))
ax.add_collection3d(Poly3DCollection(front_crossbar_2, facecolors='lightgreen', edgecolors='black', alpha=opacity))
ax.add_collection3d(Poly3DCollection(front_crossbar_3, facecolors='lightgreen', edgecolors='black', alpha=opacity))
ax.add_collection3d(Poly3DCollection(back_crossbar_1, facecolors='lightgreen', edgecolors='black', alpha=opacity))
ax.add_collection3d(Poly3DCollection(back_crossbar_2, facecolors='lightgreen', edgecolors='black', alpha=opacity))
ax.add_collection3d(Poly3DCollection(back_crossbar_3, facecolors='lightgreen', edgecolors='black', alpha=opacity))

# Longitudinal bars
ax.add_collection3d(Poly3DCollection(lower_left_long_bar, facecolors='lightgreen', edgecolors='black', alpha=opacity))
ax.add_collection3d(Poly3DCollection(lower_right_long_bar, facecolors='lightgreen', edgecolors='black', alpha=opacity))

ax.add_collection3d(Poly3DCollection(upper_left_long_bar, facecolors='lightgreen', edgecolors='black', alpha=opacity))
ax.add_collection3d(Poly3DCollection(upper_right_long_bar, facecolors='lightgreen', edgecolors='black', alpha=opacity))


# Walls
ax.add_collection3d(Poly3DCollection(back_wall, facecolors='yellow', edgecolors='yellow', alpha=0.1))
ax.add_collection3d(Poly3DCollection(left_wall, facecolors='yellow', edgecolors='yellow', alpha=0.1))
ax.add_collection3d(Poly3DCollection(right_wall, facecolors='yellow', edgecolors='yellow', alpha=0.1))


# --- Axes limits ---
ax.set_aspect('equal')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()
