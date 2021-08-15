# -*- coding: utf-8 -*-

import numpy as np
import pandas

x = np.array([[0.80, 1], [0.85, 1], [0.89, 1], [0.87, 1], [0.82, 1], [0.74, 1], [0.77, 1]])
yhat = np.array([[0.25], [0.23], [0.18], [0.21], [0.23], [0.32], [0.29]])


def main():
    xtx = np.dot(x.T, x)
    xtx_1 = np.linalg.inv(xtx)
    w = xtx_1.dot(x.T).dot(yhat)
    print('k: ' + str(w[0][0]))
    print('b: ' + str(w[1][0]))


def save_data():
    d = np.hstack((np.array([x[:, 0]]).T, yhat))
    pandas.DataFrame(d).to_csv("data.csv", index=False)


if __name__ == '__main__':
    # main()
    save_data()
