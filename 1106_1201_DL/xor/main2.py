import numpy as np
import matplotlib.pyplot as plt

from modules import Neuron, BCELoss

EPOCHS = 1000
LR = 0.7
DRAW_FREQ = int(EPOCHS / 16)

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

class Model:
    def __init__(self):
        self.neuron1_1 = Neuron(n_x=2)
        self.neuron1_2 = Neuron(n_x=2)
        self.neuron2 = Neuron(n_x=2)

    def __call__(self, x):
        a1_1 = self.neuron1_1(x)
        a1_2 = self.neuron1_2(x)
        a1 = np.array([a1_1, a1_2])

        pred = self.neuron2(a1)
        return pred

    def backward(self, dJ_dpred, lr):
        dJ_da1 = self.neuron2.backward(dJ_dpred, lr)

        self.neuron1_1.backward(dJ_da1[0], lr)
        self.neuron1_2.backward(dJ_da1[1], lr)


x1 = np.linspace(-0.5, 1.5, 100)
x2 = np.linspace(-0.5, 1.5, 100)
X1, X2 = np.meshgrid(x1, x2)
X2 = X2[::-1]
X_db = np.hstack([X1.reshape(-1, 1), X2.reshape(-1, 1)])

model = Model()
loss_function = BCELoss()
fig, axes = plt.subplots(4, 4, figsize=(10, 10))
axes = axes.flatten()
for epoch in range(EPOCHS):
    for x_, y_ in zip(X, y):
        pred = model(x_)
        J = loss_function(pred, y_)

        dJ_dpred = loss_function.backward()
        model.backward(dJ_dpred, LR)

    if epoch % DRAW_FREQ == 0 and epoch > 1:
        y_db = []
        for x_db in X_db: y_db.append(model(x_db))
        axes[(epoch // DRAW_FREQ) - 1].scatter(X_db[:, 0], X_db[:, 1], c=y_db, cmap='bwr')
        print(epoch)
plt.show()