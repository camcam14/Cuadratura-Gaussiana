# Explicación del Método Numérico

## Cuadratura de Gauss-Legendre

A diferencia de los métodos de Newton-Cotes (como la regla del trapecio o de Simpson), que utilizan puntos equiespaciados, la **Cuadratura Gaussiana** selecciona óptimamente tanto las posiciones de los nodos $x_i$ como los pesos $w_i$ para maximizar la precisión de la aproximación.

Una regla de $N$ puntos integra exactamente polinomios de grado hasta $2N - 1$.

### Formulación Matemática

En el intervalo estándar $[-1, 1]$, la integral se aproxima como:

$$ \int_{-1}^{1} f(x) \, dx \approx \sum_{i=1}^{N} w_i f(x_i) $$

Donde los $x_i$ son las raíces del polinomio de Legendre de grado $N$, $P_N(x)$, y los pesos $w_i$ se obtienen a partir de sus derivadas.

### Cambio de Intervalo

Para integrar sobre un intervalo arbitrario $[a, b]$, se realiza la transformación lineal:

$$ x = \frac{b - a}{2} x' + \frac{b + a}{2} $$

$$ dx = \frac{b - a}{2} dx' $$

De este modo, la fórmula de integración resulta:

$$ \int_{a}^{b} f(x) \, dx \approx \frac{b - a}{2} \sum_{i=1}^{N} w_i f\left( \frac{b - a}{2} x_i + \frac{b + a}{2} \right) $$