import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import numpy as np
def edges(delaunay):
    edges=set()
    for triangle in delaunay.simplices:
        for i in range(3):
            edge=tuple(sorted([triangle[i], triangle[(i + 1) % 3]]))
            edges.add(edge)
    return len(edges)

points=[
    [1,1],
    [1,-1],
    [-1,-1],
    [-1,1],
    [0,-2],
]
#case 1
case1=np.array(points+[[0,2]])
del_tri_case1 = Delaunay(case1)
print("1.Number of triangles:",len(del_tri_case1.simplices),"1.Number of edges:",edges(del_tri_case1))
fig, ax = plt.subplots(1, 4, figsize=(16, 8))
ax[0].triplot(case1[:, 0], case1[:, 1], del_tri_case1.simplices, color='green')
ax[0].scatter(case1[:, 0], case1[:, 1], color='red', label='Points')
ax[0].set_title("Case 1: a>1")

ax[0].legend()
ax[0].set_aspect('equal', adjustable='box')
#case 2
case2=np.array(points+[[0,0]])
del_tri_case2 = Delaunay(case2)
print("2.Number of triangles:",len(del_tri_case2.simplices),"2.Number of edges:",edges(del_tri_case2))
ax[1].triplot(case2[:, 0], case2[:, 1], del_tri_case2.simplices, color='green')
ax[1].scatter(case2[:, 0], case2[:, 1], color='red', label='Points')
ax[1].set_title("Case 2: -2<a<1")
ax[1].legend()
ax[1].set_aspect('equal', adjustable='box')
#case 3
case3=np.array(points+[[0,-2]])
del_tri_case3 = Delaunay(case3)
print("3.Number of triangles:",len(del_tri_case3.simplices),"3.Number of edges:",edges(del_tri_case3))
ax[2].triplot(case3[:, 0], case3[:, 1], del_tri_case3.simplices, color='green')
ax[2].scatter(case3[:, 0], case3[:, 1], color='red', label='Points')
ax[2].set_title("Case 3: a=-2")
ax[2].legend()
ax[2].set_aspect('equal', adjustable='box')
#case 4
case4=np.array(points+[[0,-3]])
del_tri_case4 = Delaunay(case4)
print("4.Number of triangles:",len(del_tri_case4.simplices),"4.Number of edges:",edges(del_tri_case4))
ax[3].triplot(case4[:, 0], case4[:, 1], del_tri_case4.simplices, color='green')
ax[3].scatter(case4[:, 0], case4[:, 1], color='red', label='Points')
ax[3].set_title("Case 4: a<-2")
ax[3].legend()
ax[3].set_aspect('equal', adjustable='box')
plt.tight_layout()
plt.show()