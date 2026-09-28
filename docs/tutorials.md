# Tutorial: Resolución de la Integral Definida

Utilizaremos el método mencionado para resolver la integral en el intervalo $[1, 3]$:

$$I = \int_{0}^{2} \left( x^6 - x^2 \sin(2x) \right) dx$$

---


```python
import numpy as np

Función a integrar: $f(x) = x^6 - x^2 * sin(2x)$
#def f(x):
    return x**6 - (x**2) * np.sin(2 * x)

Calculmos nodos y pesos de Gauss-Legendre en [-1, 1]:
#def gaussxw(N):
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w

Transforma nodos y pesos del intervalo [-1, 1] al intervalo [a, b]
#def gaussxwab(a, b, x, w):
     return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

Define los valores de N
#n2 = gaussxw(2)
    n3 = gaussxw(3)
    n4 = gaussxw(4)
    n5 = gaussxw(5)
    n6 = gaussxw(6)

Ajustados al intervalo de integración
#n2_r = gaussxwab(1.0, 3.0, n2[0], n2[1])
    n3_r = gaussxwab(1.0, 3.0, n3[0], n3[1])
    n4_r = gaussxwab(1.0, 3.0, n4[0], n4[1])
    n5_r = gaussxwab(1.0, 3.0, n5[0], n5[1])
    n6_r = gaussxwab(1.0, 3.0, n6[0], n6[1])


Evaluamos todo en la función principal:
#def func(varInd):
    return varInd ** 6 - (varInd ** 2 * np.sin(2 * varInd))

#resultN2 = np.sum(n2_r[1] * func(n2_r[0]))
    resultN3 = np.sum(n3_r[1] * func(n3_r[0]))
    resultN4 = np.sum(n4_r[1] * func(n4_r[0]))
    resultN5 = np.sum(n5_r[1] * func(n5_r[0]))
    resultN6 = np.sum(n6_r[1] * func(n6_r[0]))

Imprimimos todos los resultados:
#print(resultN2, resultN3, resultN4, resultN5, resultN6)