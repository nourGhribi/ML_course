# -*- coding: utf-8 -*-
"""Gradient Descent"""
from costs import *


def compute_gradient(y, tx, w):
    """Compute the gradient."""
    e = y - tx.dot(w)
    gradient = - 1/len(y) * tx.T.dot(e)
    return gradient, compute_mse(y, tx, w)


def gradient_descent(y, tx, initial_w, max_iters, gamma):
    """Gradient descent algorithm."""
    # Define parameters to store w and loss
    ws = [initial_w]
    losses = []
    w = initial_w
    for n_iter in range(max_iters):
        g, loss = compute_gradient(y, tx, w)
        w = w - gamma * g
        # store w and loss
        ws.append(w)
        losses.append(loss)
    return ws, losses