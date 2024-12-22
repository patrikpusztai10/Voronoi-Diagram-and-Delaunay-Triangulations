import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay
import numpy as np

points = np.array([
    [3, -5],
    [-6, 6],
    [6, -4],
    [5, -5],
    [9, 10],
])

vor = Voronoi(points)

del_tri = Delaunay(points)

fig, ax = plt.subplots(1, 2, figsize=(16, 8))
voronoi_plot_2d(vor, ax=ax[0], show_vertices=False, line_colors='blue', line_width=2, point_size=8)
ax[0].scatter(points[:, 0], points[:, 1], color='red', label='Points')
ax[0].set_title("Voronoi Diagram")
ax[0].legend()
ax[0].set_aspect('equal', adjustable='box')

ax[1].triplot(points[:, 0], points[:, 1], del_tri.simplices, color='green')
ax[1].scatter(points[:, 0], points[:, 1], color='red', label='Points')
ax[1].set_title("Delaunay Triangulation")
ax[1].legend()
ax[1].set_aspect('equal', adjustable='box')

plt.tight_layout()
plt.show()
