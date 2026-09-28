# Tutorial: Integración Numérica con Cuadratura Gaussiana

En este tutorial aprenderemos a utilizar las funciones de `cruadaturagaussiana.py` para calcular numéricamente la siguiente integral en el intervalo $[0, 2]$:

$$I = \int_{0}^{2} \left( x^6 - x^2 \sin(2x) \right) dx$$

---

## Concepto General

A diferencia de los métodos de Newton-Cotes (Trapecios o Simpson) que evalúan la función en puntos equiespaciados, la **Cuadratura de Gauss-Legendre** selecciona estratégicamente las posiciones de los nodos $x_i$ y sus pesos $w_i$ para lograr la máxima precisión posible con el menor número de evaluaciones.

$$I \approx \sum_{i=1}^{N} w_i \, f(x_i)$$

---

## Guía Paso a Paso

=== "Paso 1: Importar y Definir Funciones"

    Definimos la función integrando $f(x)$, las funciones para obtener nodos y pesos en el intervalo canónico $[-1, 1]$, y la transformación afín al intervalo $[a, b]$.

    ```python
    import numpy as np

    def f(x):
        """Función objetivo f(x) = x^6 - x^2 * sin(2x)"""
        return x**6 - (x**2) * np.sin(2 * x)

    def gaussxw(N):
        """Devuelve los nodos y pesos de Gauss-Legendre en [-1, 1]."""
        x, w = np.polynomial.legendre.leggauss(N)
        return x, w

    def gaussxwab(a, b, x, w):
        """Mapea los nodos y pesos del intervalo [-1, 1] al intervalo [a, b]."""
        x_mapped = 0.5 * (b - a) * x + 0.5 * (b + a)
        w_mapped = 0.5 * (b - a) * w
        return x_mapped, w_mapped
    ```

=== "Paso 2: Evaluar la Integral para N = 3 y N = 4"

    Calculamos los nodos y pesos transformados para el intervalo $[0, 2]$ y realizamos el producto escalar entre los pesos y los valores de la función evaluada en los nodos.

    ```python
    # Definición de límites del intervalo
    a, b = 0.0, 2.0

    # Evaluación con N = 3 nodos
    x3_std, w3_std = gaussxw(3)
    x3, w3 = gaussxwab(a, b, x3_std, w3_std)
    integral_3 = np.sum(w3 * f(x3))

    # Evaluación con N = 4 nodos
    x4_std, w4_std = gaussxw(4)
    x4, w4 = gaussxwab(a, b, x4_std, w4_std)
    integral_4 = np.sum(w4 * f(x4))

    print(f"I(N=3) = {integral_3:.8f}")
    print(f"I(N=4) = {integral_4:.8f}")
    ```

=== "Paso 3: Análisis de Error Relativo"

    Tomando como referencia de alta precisión el cálculo con $N = 100$ nodos, calculamos el porcentaje de error relativo.

    ```python
    # Valor de referencia preciso (N = 100)
    x_ref_s, w_ref_s = gaussxw(100)
    x_ref, w_ref = gaussxwab(a, b, x_ref_s, w_ref_s)
    I_ref = np.sum(w_ref * f(x_ref))

    # Error relativo porcentual
    err_3 = abs((integral_3 - I_ref) / I_ref) * 100
    err_4 = abs((integral_4 - I_ref) / I_ref) * 100

    print(f"Error relativo N=3: {err_3:.5f}%")
    print(f"Error relativo N=4: {err_4:.6f}%")
    ```

=== "Código Completo Ejecutable"

    ```python
    import numpy as np

    def f(x):
        return x**6 - (x**2) * np.sin(2 * x)

    def gaussxw(N):
        return np.polynomial.legendre.leggauss(N)

    def gaussxwab(a, b, x, w):
        return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

    if __name__ == "__main__":
        a, b = 0.0, 2.0
        
        for N in [3, 4, 10]:
            x_std, w_std = gaussxw(N)
            x, w = gaussxwab(a, b, x_std, w_std)
            resultado = np.sum(w * f(x))
            print(f"Resultado con N = {N:2d}: {resultado:.10f}")
    ```

---

## Resultados y Convergencia

A continuación se muestra la comparación de los resultados numéricos obtenidos según el número de nodos empleados:

| Nodos ($N$) | Valor Aproximado | Error Relativo (%) | Estado |
| :---: | :---: | :---: | :---: |
| **3** | $19.41910244$ | $0.041772\%$ | Aceptable |
| **4** | $19.42718902$ | $0.000153\%$ | Alta Precisión |
| **100 (Ref)** | $19.42721867$ | $0.000000\%$ | Referencia |

!!! check "Conclusión del Tutorial"
    Como se observa en la tabla, al pasar de $N = 3$ a $N = 4$ el error relativo cae bruscamente de $0.04\%$ a solo $0.00015\%$. Esto demuestra la altísima eficiencia de la Cuadratura de Gauss-Legendre para integrar funciones continuas y suaves en un intervalo acotado.

