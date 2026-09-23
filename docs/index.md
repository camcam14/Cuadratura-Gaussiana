# Integración Numérica mediante Cuadratura Gaussiana

## Introducción al Problema

En el cálculo numérico, muchas integrales definidas no poseen una antiderivada elemental o resultan complejas de evaluar de forma analítica. En este trabajo se aborda la solución numérica de la siguiente integral en el intervalo $[0, 2]$:

$$ \int_{0}^{2} \left( x^6 - x^2 \sin(2x) \right) \, dx $$

El propósito de esta documentación es implementar y analizar la convergencia del método de **Cuadratura Gaussiana de Gauss-Legendre**, evaluando la precisión obtenida al variar el número de puntos de integración $N$.