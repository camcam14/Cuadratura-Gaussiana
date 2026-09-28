import numpy as np

def gaussxw(N):
    """
    Obtiene los nodos y pesos de la cuadratura de Gauss-Legendre.

    Parameters
    ----------
    N : int
        Número de puntos de integración.

    Returns
    -------
    tuple[numpy.ndarray, numpy.ndarray]
        Una tupla que contiene:
        - x: nodos de Gauss-Legendre.
        - w: pesos asociados a cada nodo.

    Examples
    --------
    >>> x, w = gaussxw(3)
    >>> len(x)
    3
    >>> len(w)
    3
    """
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w


def gaussxwab(a, b, x, w):
    """
    Transforma nodos y pesos de Gauss-Legendre desde el intervalo
    [-1, 1] hacia un intervalo arbitrario [a, b].

    Parameters
    ----------
    a : float
        Límite inferior del intervalo.
    b : float
        Límite superior del intervalo.
    x : numpy.ndarray
        Nodos en el intervalo [-1, 1].
    w : numpy.ndarray
        Pesos asociados a los nodos.

    Returns
    -------
    tuple[numpy.ndarray, numpy.ndarray]
        Una tupla que contiene:
        - x': nodos transformados al intervalo [a, b].
        - w': pesos transformados al intervalo [a, b].

    Examples
    --------
    >>> x, w = gaussxw(2)
    >>> x_new, w_new = gaussxwab(1.0, 3.0, x, w)
    >>> len(x_new)
    2
    """
    return (
        0.5 * (b - a) * x + 0.5 * (b + a),
        0.5 * (b - a) * w
    )


def func(varInd):
    """
    Evalúa la función que será integrada mediante cuadratura de Gauss.

    La función está definida como:

        f(x) = x^6 - x^2 sin(2x)

    Parameters
    ----------
    varInd : float or numpy.ndarray
        Punto o conjunto de puntos donde se evaluará la función.

    Returns
    -------
    float or numpy.ndarray
        Valor de la función evaluada.

    Examples
    --------
    >>> func(1)
    1 - sin(2)

    >>> func(np.array([1, 2]))
    array([...])
    """
    return varInd**6 - (varInd**2 * np.sin(2 * varInd))