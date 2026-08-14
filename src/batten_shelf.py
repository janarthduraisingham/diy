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

short = 0.0508
fat = short*2
length = 1
depth = 0.75

shelf_thickness = 0.02

screw_radius = 0.005

back_batten_1 = cuboid(0, depth, 0.75, length, -short, fat)
back_batten_2 = cuboid(0, depth, 1.5, length, -short, fat)
back_batten_3 = cuboid(0, depth, 2.25, length, -short, fat)

left_batten_1 = cuboid(0, 0, 0.75, short, depth-short, fat)
left_batten_2 = cuboid(0, 0, 1.5, short, depth-short, fat)
left_batten_3 = cuboid(0, 0, 2.25, short, depth-short, fat)

right_batten_1 = cuboid(length-short, 0, 0.75, short, depth-short, fat)
right_batten_2 = cuboid(length-short, 0, 1.5, short, depth-short, fat)
right_batten_3 = cuboid(length-short, 0, 2.25, short, depth-short, fat)

shelf_1 = cuboid(0, 0, 0.75+fat, length, depth, shelf_thickness)
shelf_2 = cuboid(0, 0, 1.5+fat, length, depth, shelf_thickness)
shelf_3 = cuboid(0, 0, 2.25+fat, length, depth, shelf_thickness)

screw_clearance = 0.25

back_batten_1_screw_1 = cuboid(screw_clearance-screw_radius, depth-short, 0.75+0.5*fat-screw_radius, screw_radius, short+0.1, screw_radius)
back_batten_1_screw_2 = cuboid(length-screw_clearance-screw_radius, depth-short, 0.75+0.5*fat-screw_radius, screw_radius, short+0.1, screw_radius)


back_batten_2_screw_1 = cuboid(screw_clearance-screw_radius, depth-short, 1.5+0.5*fat-screw_radius, screw_radius, short+0.1, screw_radius)
back_batten_2_screw_2 = cuboid(length-screw_clearance-screw_radius, depth-short, 1.5+0.5*fat-screw_radius, screw_radius, short+0.1, screw_radius)

back_batten_3_screw_1 = cuboid(screw_clearance-screw_radius, depth-short, 2.25+0.5*fat-screw_radius, screw_radius, short+0.1, screw_radius)
back_batten_3_screw_2 = cuboid(length-screw_clearance-screw_radius, depth-short, 1.5+0.5*fat-screw_radius, screw_radius, short+0.1, screw_radius)

left_batten_1_screw_1 = cuboid(-0.1, screw_clearance-screw_radius, 0.75+0.5*fat-screw_radius, 0.1+short, screw_radius, screw_radius)
left_batten_1_screw_2 = cuboid(-0.1, depth-screw_clearance-screw_radius, 0.75+0.5*fat-screw_radius, 0.1+short, screw_radius, screw_radius)

left_batten_2_screw_1 = cuboid(-0.1, screw_clearance-screw_radius, 1.5+0.5*fat-screw_radius, 0.1+short, screw_radius, screw_radius)
left_batten_2_screw_2 = cuboid(-0.1, depth-screw_clearance-screw_radius, 1.5+0.5*fat-screw_radius, 0.1+short, screw_radius, screw_radius)

left_batten_3_screw_1 = cuboid(-0.1, screw_clearance-screw_radius, 2.25+0.5*fat-screw_radius, 0.1+short, screw_radius, screw_radius)
left_batten_3_screw_2 = cuboid(-0.1, depth-screw_clearance-screw_radius, 2.25+0.5*fat-screw_radius, 0.1+short, screw_radius, screw_radius)

right_batten_1_screw_1 = cuboid(length-short, screw_clearance-screw_radius, 0.75+0.5*fat-screw_radius, 0.1+short, screw_radius, screw_radius)
right_batten_1_screw_2 = cuboid(length-short, depth-screw_clearance-screw_radius, 0.75+0.5*fat-screw_radius, 0.1+short, screw_radius, screw_radius)

right_batten_2_screw_1 = cuboid(length-short, screw_clearance-screw_radius, 1.5+0.5*fat-screw_radius, 0.1+short, screw_radius, screw_radius)
right_batten_2_screw_2 = cuboid(length-short, depth-screw_clearance-screw_radius, 1.5+0.5*fat-screw_radius, 0.1+short, screw_radius, screw_radius)

right_batten_3_screw_1 = cuboid(length-short, screw_clearance-screw_radius, 2.25+0.5*fat-screw_radius, 0.1+short, screw_radius, screw_radius)
right_batten_3_screw_2 = cuboid(length-short, depth-screw_clearance-screw_radius, 2.25+0.5*fat-screw_radius, 0.1+short, screw_radius, screw_radius)

back_wall = cuboid(0, depth, 0, length, 0.01, 3)
left_wall = cuboid(0-0.01, 0, 0, 0.01, depth, 3)
right_wall = cuboid(length, 0, 0, 0.01, depth, 3)

ax.add_collection3d(Poly3DCollection(back_batten_1, facecolors='lightblue', edgecolors='black', alpha=0.7))
ax.add_collection3d(Poly3DCollection(back_batten_2, facecolors='lightblue', edgecolors='black', alpha=0.7))
ax.add_collection3d(Poly3DCollection(back_batten_3, facecolors='lightblue', edgecolors='black', alpha=0.7))

ax.add_collection3d(Poly3DCollection(left_batten_1, facecolors='lightblue', edgecolors='black', alpha=0.7))
ax.add_collection3d(Poly3DCollection(left_batten_2, facecolors='lightblue', edgecolors='black', alpha=0.7))
ax.add_collection3d(Poly3DCollection(left_batten_3, facecolors='lightblue', edgecolors='black', alpha=0.7))

ax.add_collection3d(Poly3DCollection(right_batten_1, facecolors='lightblue', edgecolors='black', alpha=0.7))
ax.add_collection3d(Poly3DCollection(right_batten_2, facecolors='lightblue', edgecolors='black', alpha=0.7))
ax.add_collection3d(Poly3DCollection(right_batten_3, facecolors='lightblue', edgecolors='black', alpha=0.7))

ax.add_collection3d(Poly3DCollection(shelf_1, facecolors='brown', edgecolors='black', alpha=0.1))
ax.add_collection3d(Poly3DCollection(shelf_2, facecolors='brown', edgecolors='black', alpha=0.1))
ax.add_collection3d(Poly3DCollection(shelf_3, facecolors='brown', edgecolors='black', alpha=0.1))

ax.add_collection3d(Poly3DCollection(back_batten_1_screw_1, facecolors='black', edgecolors='black', alpha=1))
ax.add_collection3d(Poly3DCollection(back_batten_1_screw_2, facecolors='black', edgecolors='black', alpha=1))
ax.add_collection3d(Poly3DCollection(back_batten_2_screw_1, facecolors='black', edgecolors='black', alpha=1))
ax.add_collection3d(Poly3DCollection(back_batten_2_screw_2, facecolors='black', edgecolors='black', alpha=1))
ax.add_collection3d(Poly3DCollection(back_batten_3_screw_1, facecolors='black', edgecolors='black', alpha=1))
ax.add_collection3d(Poly3DCollection(back_batten_3_screw_2, facecolors='black', edgecolors='black', alpha=1))

ax.add_collection3d(Poly3DCollection(left_batten_1_screw_1, facecolors='black', edgecolors='black', alpha=1))
ax.add_collection3d(Poly3DCollection(left_batten_1_screw_2, facecolors='black', edgecolors='black', alpha=1))
ax.add_collection3d(Poly3DCollection(left_batten_2_screw_1, facecolors='black', edgecolors='black', alpha=1))
ax.add_collection3d(Poly3DCollection(left_batten_2_screw_2, facecolors='black', edgecolors='black', alpha=1))
ax.add_collection3d(Poly3DCollection(left_batten_3_screw_1, facecolors='black', edgecolors='black', alpha=1))
ax.add_collection3d(Poly3DCollection(left_batten_3_screw_2, facecolors='black', edgecolors='black', alpha=1))

ax.add_collection3d(Poly3DCollection(right_batten_1_screw_1, facecolors='black', edgecolors='black', alpha=1))
ax.add_collection3d(Poly3DCollection(right_batten_1_screw_2, facecolors='black', edgecolors='black', alpha=1))
ax.add_collection3d(Poly3DCollection(right_batten_2_screw_1, facecolors='black', edgecolors='black', alpha=1))
ax.add_collection3d(Poly3DCollection(right_batten_2_screw_2, facecolors='black', edgecolors='black', alpha=1))
ax.add_collection3d(Poly3DCollection(right_batten_3_screw_1, facecolors='black', edgecolors='black', alpha=1))
ax.add_collection3d(Poly3DCollection(right_batten_3_screw_2, facecolors='black', edgecolors='black', alpha=1))

ax.add_collection3d(Poly3DCollection(back_wall, facecolors='yellow', edgecolors='yellow', alpha=0.1))
ax.add_collection3d(Poly3DCollection(left_wall, facecolors='yellow', edgecolors='yellow', alpha=0.1))
ax.add_collection3d(Poly3DCollection(right_wall, facecolors='yellow', edgecolors='yellow', alpha=0.1))


# --- Axes limits ---
ax.set_aspect('equal')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()
