import numpy as np
from typing import List, Dict
import random

def solution():
    """Solutions to broadcasting Questions"""
    # Q1. Numpy adopts the trailing broadcast: check the dimension from the rightmost axis
    # If it is 1: Equal or 2: the number of the dimensional axis is one

    # Q2. if shapes are (3,4) vs (4, ) => (3, 4), 
    # (8, 1, 6, 1) vs (7, 1, 5) => (8, 1, 6, 1)  x (1, 7, 1, 5) => (8, 7, 6, 5)
    # (3, 4) vs (3, ): impossible! change into => (3, 4) vs (1, 3)
    # (2, 3) vs (2, 3, 4) => (1, 2, 3) vs (2, 3, 4): impossible change into (2, 3) -> (1, 2, 3)

    # Q3
    rng = np.random.default_rng()
    sales = rng.integers(100, 1_000, size=(30, 5))
    region_tax = rng.uniform(0.0, 0.10, size=(1, 5))
    revenue = sales * (1 - region_tax)

    # Q4
    rng = np.random.default_rng()
    temperatures = rng.integers(0, 40, size=(365,))
    monthly_data = rng.integers(0, 40, size=(12, 31))
    ## shape is (12,)
    monthly_means = np.mean(monthly_data, axis=1)
    ### dimensional operation
    monthly_means = montly_means[:, np.newaxis]

    # Q5: Word Embedding
    ## embeddings: (10000, 300) vs Query (300,)
    embeddings = rng.uniform(0.0, 1.0, size=(10000, 300))
    query = rng.uniform(0.0, 1.0, size=(300,))
    ## query is stretched like (1, 300) => (10000, 300)
    distances = np.sqrt(((embeddings - query) ** 2).sum(axis=1))
    ## distances (1000,)

    # Q6: matrix broadcast (instead of np.subtract_outer)
    x = np.array([1, 2, 3, 4, 5])
    x1 = x[:, np.newaxis]
    x2 = x[np.newaxis, :]
    diff = x1 - x2
    diff = x.reshape(-1, 1) - x.reshape(1, -1)

    # Q7: machine learning and broadcasting
    batch_size = 64
    features = 20
    X = rng.uniform(0.0, 1.0, shape=(batch_size, features))
    X_mean = np.mean(X, axis = 1)
    X_std = np.std(X, axis=1)
    X_norm = (X - X_mean) / X_std

    # Q8
    height = 252
    width = 252
    img = rng.integers(0, 256, size=(height, width, 3))
    weights = [0.299, 0.587, 0.114]
    gray = img * weights
    mask = rng.integers(0, 50, size=(height, width))
    brightened = img + mask[:, :, np.newaxis]

    # Q9
    points = np.random.rand(100, 3)       # 100 points in 3D
    norms = np.linalg.norm(points, axis=1) # shape (100,) — length of each point
    unit_vectors = points / norms[:, np.newaxis]

def main():
    solution()

if __name__ == '__main__':
    main()
