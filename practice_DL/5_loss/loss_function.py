import numpy as np 

def mae(y_pred: np.array, y_true: np.array) -> np.array:
    """Returns mean average error
    """
    mean_abosolute_error = np.mean(np.abs(y_pred - y_true))
    return mean_abosolute_error

def binary_cross_entropy(y_pred: np.array, y_true: np.array, epsilon: float = 1e-15) -> np.array:
    """Returns Binary Cross Entropy
    """
    entropy = - (y_true * np.log(y_pred + epsilon) + (1 - y_true) * np.log(1 - y_pred + epsilon))
    return np.mean(entropy)

def mse(y_pred: np.array, y_true: np.array) -> np.array:
    """Returns mean squared error
    """
    mean_squared_error = np.mean((y_pred - y_true) ** 2)
    return mean_squared_error

def main():
    y_pred = np.array([0.1, 0.9, 0.5])
    y_true = np.array([0, 1, 0])
    print(f'MAE: {mae(y_pred, y_true):.4f}')
    print(f'Binary Cross Entropy: {binary_cross_entropy(y_pred, y_true):.4f}')
    print(f'MSE: {mse(y_pred, y_true):.4f}')

if __name__ == '__main__':
    main()
