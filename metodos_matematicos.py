import numpy as np

# 1. Introdução

# 2. Estática dos Fluidos
def calcular_pressao(rho, g, h):
    """Calcula a pressão hidrostática."""
    pressao = rho * g * h
    return pressao