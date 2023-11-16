from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

N_SAMPLES = 100
LR = 0.001
EPOCHS = 30

X, y = make_blobs(n_samples=N_SAMPLES, centers=2, n_features=2,
                  cluster_std=0.5, random_state=0)

''' Instantiation '''


for epoch in range(EPOCHS):

    for X_, y_ in zip(X, y):
        ''' Training '''


        ''' Metric(loss, accuracy) Calculations '''


''' Result Visualization '''