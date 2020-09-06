import numpy as np
from scipy.stats import norm
import sys


def update_W(X, Mu, Var, Pi):
    n_points, n_clusters = len(X), len(Pi)
    pdfs = np.zeros(((n_points, n_clusters)))
    for i in range(n_clusters):
        pdfs[:, i] = Pi[i] * norm.pdf(X, Mu[i], Var[i])
    W = pdfs / pdfs.sum(axis=1).reshape(-1, 1)
    return W


def update_Pi(W):
    Pi = W.sum(axis=0) / W.sum()
    return Pi


def update_Mu(X, W):
    n_clusters = W.shape[1]
    Mu = np.zeros((n_clusters, 2))
    print(Mu)
    for i in range(n_clusters):
        Mu[i] = np.average(X, weights=W[:, i])
    return Mu


def update_Var(X, Mu, W):
    n_clusters = W.shape[1]
    Var = np.zeros((n_clusters, 2))
    for i in range(n_clusters):
        Var[i] = np.average((X - Mu[i]) ** 2, axis=0, weights=W[:, i])
    return Var


if __name__ == "__main__":
    K, N, M = list(map(int, sys.stdin.readline().strip().split()))
    Mu = []
    Var = []
    Pi = []
    for i in range(K):
        pr, mu, std = list(map(float, sys.stdin.readline().strip().split()))
        Pi.append(pr)
        Var.append(std ** 2)
        Mu.append(mu)

    X = list(map(float, sys.stdin.readline().strip().split()))
    for i in range(M):
        W = update_W(X, Mu, Var, Pi)
        print(W)
        Pi = update_Pi(W)
        Mu = update_Mu(X, W)
        Var = update_Var(X, Mu, W)

    for i in range(K):
        print(str(Pi[i]) + " " + str(Mu[i]) + " " + str(Var[i]))
