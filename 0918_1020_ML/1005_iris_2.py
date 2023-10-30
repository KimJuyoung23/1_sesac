import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

figsize = (10, 10)
iris = load_iris()
iris_X, iris_y = iris.data, iris.target # type: ignore
feature_names = iris.feature_names # type: ignore
n_feature = len(feature_names)

fig, axes = plt.subplots(4, 4, figsize=figsize)

for i, ax in enumerate(axes.flat):
    row_feat, col_feat = i // n_feature, i % n_feature

    ax.spines['top'].set_visible(False) # type: ignore
    ax.spines['right'].set_visible(False) # type: ignore

    if row_feat == 0:
        ax.set_ylabel(feature_names[col_feat], fontsize=13) # type: ignore
    if col_feat == n_feature-1:
        ax.set_xlabel(feature_names[row_feat], fontsize=13) # type: ignore

    if row_feat == col_feat:
        ax.hist(iris_X[:, row_feat], rwidth=0.9) # type: ignore
    else:
        ax.scatter(iris_X[:, row_feat], iris_X[:, col_feat], c=iris_y, alpha=0.5) # type: ignore
        ax.grid() # type: ignore

plt.tight_layout()
plt.show()
