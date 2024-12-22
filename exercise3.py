import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
from scipy.sparse.csgraph import minimum_spanning_tree

points = {
    "A": (-1, 6),
    "B": (-1, -1),
    "C": (4, 7),
    "D": (6, 7),
    "E": (1, -1),
    "F": (-5, 3),
    "P": (-2, 3)
}

def mst_length(lambda_value):
    Q = (2 - lambda_value, 3)
    all_points = list(points.values()) + [Q]

    dist_matrix = distance.cdist(all_points, all_points, 'euclidean')

    mst = minimum_spanning_tree(dist_matrix)

    return mst.sum(), all_points, mst

lambda_range = np.linspace(-10, 10, 200)
min_length = float('inf')
best_lambda = None
best_points = None
best_mst = None

for lambda_value in lambda_range:
    length, all_points, mst = mst_length(lambda_value)
    if length < min_length:
        min_length = length
        best_lambda = lambda_value
        best_points = all_points
        best_mst = mst

print(f"Best lambda: {best_lambda}")
print(f"Minimal MST Length: {min_length}")

def plot_mst(points, mst):
    points_array = np.array(points)
    mst = mst.toarray()

    plt.figure(figsize=(10, 8))

    for i, (x, y) in enumerate(points):
        plt.scatter(x, y, label=str(ord('A')+i))
        plt.text(x, y, f" {chr(65 + i) if i < len(points) - 1 else 'Q'}", fontsize=12)

    for i in range(len(points)):
        for j in range(len(points)):
            if mst[i, j] > 0:
                plt.plot(
                    [points_array[i, 0], points_array[j, 0]],
                    [points_array[i, 1], points_array[j, 1]],
                    'k-', lw=1
                )

    plt.title("Minimal Spanning Tree")
    plt.legend()
    plt.show()

plot_mst(best_points, best_mst)
