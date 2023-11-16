import numpy as np

class AffineFunction:
    def __init__(self, n_x):
        self.w = np.random.randn(n_x)
        self.b = np.random.randn()

    def __call__(self, x):
        self.x = x
        z = np.dot(self.w, x) + self.b
        return z

    def backward(self, dJ_dz, lr):
        dz_dx = self.w
        dz_dw = self.x
        dz_db = 1

        dJ_dw = dJ_dz * dz_dw
        dJ_dx = dJ_dz * dz_dx
        dJ_db = dJ_dz * dz_db

        self.w = self.w - lr * dJ_dw
        self.b = self.b - lr * dJ_db

        return dJ_dx


class Sigmoid:
    def __call__(self, z):
        self.a = 1 / (1 + np.exp(-z))
        return self.a

    def backward(self, dJ_da):
        da_dz = self.a * (1 - self.a)
        dJ_dz = dJ_da * da_dz
        return dJ_dz


class Neuron:
    def __init__(self, n_x):
        self.affine = AffineFunction(n_x=n_x)
        self.act = Sigmoid()

    def __call__(self, x):
        z = self.affine(x)
        a = self.act(z)
        return a

    def backward(self, dJ_da, lr):
        dJ_dz = self.act.backward(dJ_da)
        dJ_dx = self.affine.backward(dJ_dz, lr)
        return dJ_dx


class BCELoss:
    def __call__(self, pred, y):
        self.pred, self.y = pred, y
        J = -(y * np.log(pred) + (1 - y) * np.log(1 - pred))
        return J

    def backward(self):
        dJ_dpred = (self.pred - self.y) / (self.pred * (1 - self.pred))
        return dJ_dpred
