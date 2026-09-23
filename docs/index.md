# Cuadratura Gaussiana

Implementación del método de integración numérica de Gauss-Legendre en Python.

## Descripción de la Función

Se evalúa la integración de la siguiente función en el intervalo $[0, 2]$:

$$ f(x) = x^6 - x^2 \sin(2x) $$

---

## Resultados Obtenidos según $N$

Al evaluar con la cuadratura gaussiana cambiando el número de puntos $N$, se obtuvieron los siguientes valores:

| Puntos ($N$) | Resultado de la Integral |
| :---: | :---: |
| 1 | 306.819934 |
| 2 | 317.264152 |
| 3 | 317.345390 |
| 4 | 317.344227 |
| **5** | **317.344247** |

---

## Conclusión

A partir de $N = 4$ y $N = 5$, la cuadratura gaussiana alcanza una excelente precisión y el resultado converge a **317.3442**.