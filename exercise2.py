import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np

points =[
    [5,-1],
    [7,-1],
    [9,-1],
    [7,-3],
    [11,-1],
    [-9 , 3],

]
#A7=[[-5,-5]]
A7=[[0.4,3.3]]
#A8=[[-4.9,1.7]]
A8=[[-3.4,1.4]]
voronoi_points=np.array(points+A7+A8)
vor = Voronoi(voronoi_points)

fig, ax = plt.subplots(figsize=(8, 8))
voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='blue', line_width=2, point_size=8)

ax.set_title("Voronoi Diagram")
ax.set_xlim(-60, 60)
ax.set_ylim(-70, 120)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
