import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

# 데이터 불러오기
iris = load_iris()
iris_X, iris_y = iris.data, iris.target
feature_names = iris.feature_names
species = iris.target_names

# 그래프 설정
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

for ax, feature_name in zip(axes.flat, feature_names):
    data = [iris_X[iris_y == species_idx][:, species_idx] for species_idx in range(len(species))]
    ax.violinplot(data)
    ax.set_title(feature_name, fontsize=10)
    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(species)
    ax.tick_params(labelsize=10)
    ax.grid()

plt.show()