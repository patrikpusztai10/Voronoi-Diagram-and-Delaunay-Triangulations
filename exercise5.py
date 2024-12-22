import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay
import numpy as np
def edges(delaunay):
    edges=set()
    for triangle in delaunay.simplices:
        for i in range(3):
            edge=tuple(sorted([triangle[i], triangle[(i + 1) % 3]]))
            edges.add(edge)
    return len(edges)
M1= np.array([
    [-6, 4],
    [-6, 1],
    [2, 1],
    [2, 4],
    [-2, 4],
])
M2_1=np.array(
    [
        [-4.47,-2.2],
        [-6.85,-5.18],
        [-6,-8],
        [-3.76,-5.53],
        [-3.19,-8.36],
        [-3.76,-5.53],
    ]
)
M2_2=np.array([
    [-8.05,-14.31],
    [-3.55,-9.46],
    [0,-16],
    [-3.74,-13.8],
])
del_tri1=Delaunay(M1)
vor1 = Voronoi(M1)
del_tri2=Delaunay(M2_1)
vor2 = Voronoi(M2_1)
del_tri3=Delaunay(M2_2)
vor3 = Voronoi(M2_2)
fig, ax= plt.subplots(1, 3, figsize=(16, 8))
voronoi_plot_2d(vor1, ax=ax[0], show_vertices=False, line_colors='blue', line_width=2, point_size=8)
halfline_count1 = sum(1 for vertices in vor1.ridge_vertices if -1 in vertices)
voronoi_plot_2d(vor2, ax=ax[1], show_vertices=False, line_colors='blue', line_width=2, point_size=8)
halfline_count2 = sum(1 for vertices in vor2.ridge_vertices if -1 in vertices)
voronoi_plot_2d(vor3, ax=ax[2], show_vertices=False, line_colors='blue', line_width=2, point_size=8)
halfline_count3= sum(1 for vertices in vor3.ridge_vertices if -1 in vertices)

#M1
ax[0].triplot(M1[:, 0], M1[:, 1], del_tri1.simplices, color='green')
ax[0].scatter(M1[:, 0], M1[:, 1], color='red', label='Points')
ax[0].set_title("Delaunay Triangulation of M1")
ax[0].legend()
ax[0].set_aspect('equal', adjustable='box')
ax[0].set_xlim(-20, 15)
ax[0].set_ylim(-25, 20)
#M2_1
ax[1].triplot(M2_1[:, 0], M2_1[:, 1], del_tri2.simplices, color='purple')
ax[1].scatter(M2_1[:, 0], M2_1[:, 1], color='green', label='Points')
ax[1].set_title("Delaunay Triangulation of M2_1")
ax[1].legend()
ax[1].set_aspect('equal', adjustable='box')
ax[1].set_xlim(-20, 10)
ax[1].set_ylim(-20, 10)
#M2_2
ax[2].triplot(M2_2[:, 0], M2_2[:, 1], del_tri3.simplices, color='red')
ax[2].scatter(M2_2[:, 0], M2_2[:, 1], color='yellow', label='Points')
ax[2].set_title("Delaunay Triangulation of M2_2")
ax[2].legend()
ax[2].set_aspect('equal', adjustable='box')
ax[2].set_xlim(-20, 10)
ax[2].set_ylim(4, -30)
print("1.",halfline_count1,"halflines and",edges(del_tri1),"edges")
print("2.",halfline_count2,"halflines and",edges(del_tri2),"edges")
print("3.",halfline_count3,"halflines and",edges(del_tri3),"edges")
plt.show()
