# Tutorial de Uso

A continuación se muestra un ejemplo paso a paso de cómo utilizar el módulo en Python para integrar la función objetivo $f(x) = x^6 - x^2 \sin(2x)$ en el intervalo $[0, 2]$.

## Paso 1: Importar bibliotecas e implementar el script

```python
import numpy as np

def gaussxw(N):
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w

def gaussxwab(a, b, x, w):
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

def func(x):
    return x**6 - (x**2 * np.sin(2 * x))

# Parámetros del problema
a, b = 0.0, 2.0
N = 5

# Mapeo y evaluación
x_nodes, weights = gaussxw(N)
x_mapped, w_mapped = gaussxwab(a, b, x_nodes, weights)
integral = np.sum(w_mapped * func(x_mapped))

print(f"Resultado de la integral con N={N}: {integral}")