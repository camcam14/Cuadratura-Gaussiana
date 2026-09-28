# Referencia de Funciones

Esta sección contiene la documentación técnica de las funciones desarrolladas en el módulo de integración por **Cuadratura de Gauss-Legendre**.

---

## `gaussxw`

Calcula los nodos de integración $x_i$ y sus respectivos pesos $w_i$ en el intervalo canónico $[-1, 1]$ para un grado $N$ dado.

```python
def gaussxw(N):
    """
    Calcula nodos y pesos para la Cuadratura de Gauss-Legendre.

    Parameters
    ----------
    N : int
        Número de puntos de integración (nodos).

    Returns
    -------
    x : numpy.ndarray
        Nodos de integración en el intervalo [-1, 1].
    w : numpy.ndarray
        Pesos asociados a cada nodo.

    Examples
    --------
    >>> x, w = gaussxw(2)
    >>> x
    array([-0.57735027,  0.57735027])
    >>> w
    array([1., 1.])
    """