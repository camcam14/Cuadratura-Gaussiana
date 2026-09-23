# Referencia de Funciones

Documentación técnica detallada de las funciones utilizadas, con formato *docstrings* (PEP 257)[cite: 6].

---

### `gaussxw(N)`

Calcula los puntos de integración y pesos para la Cuadratura de Gauss-Legendre en el intervalo $[-1, 1]$.

**Argumentos:**
* `N` (*int*): Número de puntos o nodos de integración.

**Retorna:**
* `x` (*ndarray*): Arreglo unidimensional con los nodos de integración $x_i$.
* `w` (*ndarray*): Arreglo unidimensional con los pesos asociados $w_i$.

**Ejemplo de uso:**
```python
>>> x, w = gaussxw(3)
>>> print(x)
[-0.77459667  0.          0.77459667]
