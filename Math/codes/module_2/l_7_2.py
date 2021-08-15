# -*- coding: utf-8 -*-
import numpy as np


def main():
    x = np.array([[0.80, 0.72, 1], [0.85, 0.81, 1], [0.89, 0.75, 1], [0.87, 0.82, 1], [0.82, 0.74, 1], [0.74, 0.85, 1],
                  [0.77, 0.83, 1]])
    yhat = np.array([[0.25], [0.23], [0.18], [0.21], [0.23], [0.32], [0.29]])
    xtx = np.dot(x.T, x)
    xtx_1 = np.linalg.inv(xtx)
    w = xtx_1.dot(x.T).dot(yhat)
    print('k1: ' + str(w[0][0]))
    print('k2: ' + str(w[1][0]))
    print('b: ' + str(w[2][0]))


if __name__ == '__main__':
    main()
