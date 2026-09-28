# Cuadratura de Gauss-Legendre

## Descripción

Este programa utiliza la **cuadratura de Gauss-Legendre** para aproximar la integral definida de la función

\[
f(x)=x^6-x^2\sin(2x)
\]

en el intervalo

\[
[1,3].
\]

Se calcula la aproximación utilizando diferentes cantidades de puntos de integración:

- N = 2
- N = 3
- N = 4
- N = 5
- N = 6

Esto permite observar cómo mejora la precisión al aumentar el número de puntos.

---

## Implementación

### 1. Importación de NumPy

```python
import numpy as np
```

---

### 2. Función para obtener nodos y pesos de Gauss-Legendre

```python
def gaussxw(N):
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w
```

Esta función devuelve:

- `x`: nodos de integración.
- `w`: pesos correspondientes.

---

### 3. Transformación al intervalo [1,3]

```python
def gaussxwab(a, b, x, w):
    return (
        0.5 * (b - a) * x + 0.5 * (b + a),
        0.5 * (b - a) * w
    )
```

La cuadratura estándar trabaja en \([-1,1]\), por lo que esta función transforma los nodos y pesos al intervalo deseado.

---

### 4. Obtención de nodos y pesos para distintos valores de N

```python
n2 = gaussxw(2)
n3 = gaussxw(3)
n4 = gaussxw(4)
n5 = gaussxw(5)
n6 = gaussxw(6)
```

---

### 5. Transformación de los nodos y pesos al intervalo [1,3]

```python
n2_r = gaussxwab(1.0, 3.0, n2[0], n2[1])
n3_r = gaussxwab(1.0, 3.0, n3[0], n3[1])
n4_r = gaussxwab(1.0, 3.0, n4[0], n4[1])
n5_r = gaussxwab(1.0, 3.0, n5[0], n5[1])
n6_r = gaussxwab(1.0, 3.0, n6[0], n6[1])
```

---

### 6. Definición de la función a integrar

```python
def func(varInd):
    return varInd**6 - (varInd**2 * np.sin(2 * varInd))
```

Corresponde a

\[
f(x)=x^6-x^2\sin(2x).
\]

---

### 7. Aplicación de la cuadratura de Gauss

```python
resultN2 = np.sum(n2_r[1] * func(n2_r[0]))
resultN3 = np.sum(n3_r[1] * func(n3_r[0]))
resultN4 = np.sum(n4_r[1] * func(n4_r[0]))
resultN5 = np.sum(n5_r[1] * func(n5_r[0]))
resultN6 = np.sum(n6_r[1] * func(n6_r[0]))
```

Cada resultado corresponde a

\[
\sum_{i=1}^{N} w_i f(x_i).
\]

---

### 8. Impresión de resultados

```python
print(resultN2, resultN3, resultN4, resultN5, resultN6)
```

---

## Código completo

```python
import numpy as np

def gaussxw(N):
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w

def gaussxwab(a, b, x, w):
    return (
        0.5 * (b - a) * x + 0.5 * (b + a),
        0.5 * (b - a) * w
    )

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
    return varInd**6 - (varInd**2 * np.sin(2 * varInd))

resultN2 = np.sum(n2_r[1] * func(n2_r[0]))
resultN3 = np.sum(n3_r[1] * func(n3_r[0]))
resultN4 = np.sum(n4_r[1] * func(n4_r[0]))
resultN5 = np.sum(n5_r[1] * func(n5_r[0]))
resultN6 = np.sum(n6_r[1] * func(n6_r[0]))

print(resultN2, resultN3, resultN4, resultN5, resultN6)
```

---

## Resultados

Al ejecutar el programa se obtienen aproximaciones de la integral para cada valor de \(N\):

| Número de puntos (N) | Aproximación |
|---------------------|-------------|
| 2 | `resultN2` |
| 3 | `resultN3` |
| 4 | `resultN4` |
| 5 | `resultN5` |
| 6 | `resultN6` |


---

## Conclusión

La cuadratura de Gauss-Legendre permite aproximar integrales definidas con alta precisión utilizando un número reducido de puntos de evaluación. Al incrementar el número de nodos \(N\), la aproximación converge hacia el valor exacto de la integral, reduciendo el error numérico.