import torch

def sigmoid(x: torch.Tensor) -> torch.Tensor:
    """Computes the Sigmoid activation function element-wise.
    
    Formula: σ(x) = 1 / (1 + exp(-x))
    Uses torch.where for numerical stability across positive and negative inputs.
    """
    return torch.where(
        x >= 0,
        1.0 / (1.0 + torch.exp(-x)),
        torch.exp(x) / (1.0 + torch.exp(x))
    )

def deriv_sigmoid(x: torch.Tensor) -> torch.Tensor:
    """Computes the derivative of the Sigmoid activation function element-wise.
    
    Formula: σ'(x) = σ(x) * (1 - σ(x))
    """
    return sigmoid(x) * (1.0 - sigmoid(x))

def tanh(x: torch.Tensor) -> torch.Tensor:
    """Computes the Hyperbolic Tangent (tanh) activation function element-wise.
    
    Formula: tanh(x) = (exp(x) - exp(-x)) / (exp(x) + exp(-x))
    """
    numerator = torch.exp(x) - torch.exp(-x)
    denominator = torch.exp(x) + torch.exp(-x)
    return numerator / denominator

def deriv_tanh(x: torch.Tensor) -> torch.Tensor:
    """Computes the derivative of the Tanh activation function element-wise.
    
    Formula: tanh'(x) = 1 - tanh^2(x)
    """
    return 1.0 - tanh(x) ** 2

def relu(x: torch.Tensor) -> torch.Tensor:
    """Computes the Rectified Linear Unit (ReLU) activation function element-wise.
    
    Formula: ReLU(x) = max(0, x)
    """
    return torch.maximum(x, torch.tensor(0.0, device=x.device, dtype=x.dtype))

def deriv_relu(x: torch.tensor) -> torch.Tensor:
    """Computes the derivative of the ReLU
    """
    return torch.where(x > 0, 1.0, 0.0, device=x.device, dtype=x.dtype)

def leaky_relu(x: torch.Tensor, alpha: float = 0.01) -> torch.Tensor:
    """Computes the Leaky Rectified Linear Unit (Leaky ReLU) activation function element-wise.
    
    Formula: LeakyReLU(x) = max(alpha * x, x)
    Solves the 'dying ReLU' problem by allowing a small non-zero gradient when x < 0.
    """
    return torch.maximum(alpha * x, x)

def deriv_leaky_relu(x: torch.Tensor, alpha: float) -> torch.Tensor:
    """Computes the derivative of the Leaky ReLU activation function.
    
    Formula: LeakyReLU'(x) = alpha if x < 0, else 1
    """
    return torch.where(x > 0, 1.0, alpha, device=x.device, dtype=x.dtype)

if __name__ == "__main__":
    # Verification with sample inputs
    test_tensor = torch.tensor([-3.0, -1.0, 0.0, 1.0, 3.0])
    
    print("--- Activation Function Output Verification ---")
    print(f"Input:      {test_tensor.numpy()}")
    print(f"Sigmoid:    {sigmoid(test_tensor).numpy()}")
    print(f"Tanh:       {tanh(test_tensor).numpy()}")
    print(f"ReLU:       {relu(test_tensor).numpy()}")
    print(f"Leaky ReLU: {leaky_relu(test_tensor).numpy()}")

    