import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

figsize = (10, 10)
iris = load_iris()

feature_names = iris.feature_names # 특징  # type: ignore
n_feature = len(feature_names) # 4
species = iris.target_names # 종 # type: ignore
n_species = len(species) # 3
iris_X, iris_y = iris.data, iris.target # 데이터, 종 # type: ignore
iris_X = np.transpose(iris_X) # transpose
data = iris_X.reshape(n_feature, n_species, -1) # (특징, 종, 데이터)

list_n_species = [i for i in range(n_species)] # xposition, xticks 위한 리스트

fig, axes = \
    plt.subplots(2, 2, figsize = figsize) # 2 * 2 subplots 
for ax_idx, ax in enumerate(axes.flat):
    ax.violinplot([data[ax_idx][i] for i in list_n_species], positions=list_n_species) # type: ignore # 
    ax.set_title(feature_names[ax_idx], fontsize=10) # type: ignore
    ax.set_xticks(list_n_species) # type: ignore
    ax.set_xticklabels(species) # type: ignore
    ax.tick_params(labelsize=10) # type: ignore
    ax.grid() # type: ignore

plt.show()