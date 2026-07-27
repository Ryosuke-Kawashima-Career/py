import torch
import numpy as np

def sigmoid(x: torch.tensor) -> torch.tensor:
    """Returns Sigmoid
    """
    denom = torch.exp(x) if x < 0 else 1
    numerator = 1.0 + torch.exp(-np.abs(x))
    return denom / numerator

def tanh(x: torch.tensor) -> torch.tensor:
    """Returns the tangent hyperbolic function"""
    denom = torch.exp(x) - torch.exp(-x)
    numer = torch.exp(x) + torch.exp(-x)
    return denom / numer

def relu(x: torch.tensor) -> torch.tensor:
    """Returns the rectified linear unit"""
    return np.max(x, 0.0)

def leaky_relu(x: torch.tensor) -> torch.tensor:
    """Cope with the dying neurons and saturation issues"""
    return np.max(0.01 * x, x)
    