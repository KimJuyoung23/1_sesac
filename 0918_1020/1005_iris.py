import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()

# for attr in dir(iris):
#     print(attr)
'''
DESCR
data
data_module
feature_names
filename
frame
target
target_names
'''
# print(iris.data)
# print(iris.feature_names)
# print(iris.target)
# print(iris.target_names)

feature_names = iris.feature_names
n_feature = len(feature_names)
species = iris.target_names
n_species = len(species)
# iris_X -> 대문자 X. 백터를 의미. iris_y 는 소문자. 백터.
iris_X, iris_y = iris.data, iris.target

