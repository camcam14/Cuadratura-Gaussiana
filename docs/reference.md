# Referencia de Funciones

Esta sección contiene la documentación técnica de las funciones desarrolladas en el módulo de integración por **Cuadratura de Gauss-Legendre**.

---

## Funciones del Módulo

### `gaussxw(N)`

Calcula los nodos $x_i$ y los pesos $w_i$ para la Cuadratura de Gauss-Legendre en el intervalo canónico $[-1, 1]$ apoyándose en la rutina `numpy.polynomial.legendre.leggauss`.

#### Parámetros

| Nombre | Tipo | Descripción |
| :--- | :--- | :--- |
| **`N`** | `int` | Número de puntos o nodos de integración ($N \ge 1$). |

#### Retorno

* **`x`** (`numpy.ndarray`): Arreglo unidimensional con los $N$ nodos en $[-1, 1]$.
* **`w`** (`numpy.ndarray`): Arreglo unidimensional con los $N$ pesos correspondientes.

#### Ejemplo de uso

```python
>>> x, w = gaussxw(3)
>>> print(x)
[-0.77459667  0.          0.77459667]
>>> print(w)
[0.55555556 0.88888889 0.55555556]