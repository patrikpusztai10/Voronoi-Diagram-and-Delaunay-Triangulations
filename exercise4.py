import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np
A = []
B = []
C = []
xc = 0
for i in range(6):
    xa = 1 - i
    ya = i - 1
    xb = i
    yb = -i
    yc = i
    A.append([xa, ya])
    B.append([xb, yb])
    C.append([xc, yc])

points = np.array(A + B + C)

vor = Voronoi(points)

fig, ax = plt.subplots(figsize=(8, 8))
voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='blue', line_width=2, point_size=8)

halfline_count = sum(1 for vertices in vor.ridge_vertices if -1 in vertices) #works because ridges are marked as [start_vertex,-1]
print("Number of halflines:", halfline_count)

ax.set_title("Voronoi Diagram with Halflines")
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 25)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
