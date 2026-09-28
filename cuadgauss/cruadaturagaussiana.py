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
        Nodos y pesos de Gauss-Legendre.

    Examples
    --------
    >>> x, w = gaussxw(3)
    >>> len(x)
    3
    """

    x, w = np.polynomial.legendre.leggauss(N)

    return x, w

def gaussxwab(a, b, x, w):
    """
    Transforma los nodos y pesos desde el intervalo [-1,1]
    al intervalo [a,b].

    Parameters
    ----------
    a : float
        Límite inferior del intervalo.
        
    b : float
        Límite superior del intervalo.
        
    x : numpy.ndarray
        Nodos de Gauss-Legendre.
        
    w : numpy.ndarray
        Pesos de Gauss-Legendre.

    Returns
    -------
    tuple[numpy.ndarray, numpy.ndarray]
        Nodos y pesos transformados al intervalo [a,b].

    Examples
    --------
    >>> x, w = gaussxw(2)
    >>> x_t, w_t = gaussxwab(1.0, 3.0, x, w)
    """
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w


n2 = gaussxw(2)

n3 = gaussxw(3)

n4 = gaussxw(4)

n5 = gaussxw(5)

n6 = gaussxw(6)

n2_r = gaussxwab(1.0, 3.0, n2[0], n2[1])

n3_r = gaussxwab(1.0, 3.0, n3[0], n3[1])

n4_r = gaussxwab(1.0, 3.0, n4[0], n4[1])

n5_r = gaussxwab(1.0, 3.0, n5[0], n5[1])

n6_r = gaussxwab(1.0, 3.0, n6[0], n6[1])

def func(varInd):
    """
    Evalúa la función a integrar.

    La función está definida por

        f(x) = x^6 - x^2 sin(2x)

    Parameters
    ----------
    varInd : float or numpy.ndarray
        Punto o conjunto de puntos donde se evalúa la función.

    Returns
    -------
    float or numpy.ndarray
        Valor de la función evaluada.

    Examples
    --------
    >>> func(1.0)
    0.09070257317431829
    """
    return varInd ** 6 - (varInd ** 2 * np.sin(2 * varInd))

resultN2 = np.sum(n2_r[1] * func(n2_r[0]))
resultN3 = np.sum(n3_r[1] * func(n3_r[0]))
resultN4 = np.sum(n4_r[1] * func(n4_r[0]))
resultN5 = np.sum(n5_r[1] * func(n5_r[0]))
resultN6 = np.sum(n6_r[1] * func(n6_r[0]))


print(resultN2, resultN3, resultN4, resultN5, resultN6)