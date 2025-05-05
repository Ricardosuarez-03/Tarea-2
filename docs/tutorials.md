#Tutorial del uso del metodo de cuadratura Gaussiana

```python
import numpy as np
```

Se importó numpy para poder utilizarlo luego para traer distintas funciones propias de este. Además se abrevió como np para facilitar la escritura del código.

```python
def gaussXyW(N):
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w
```

La función anterior calcula los pesos y los puntos de muestreo necesarios para hacer una cuadratura gaussiana.

```python
def gaussXyWesc(a, b, x, w):
    x_esc = 0.5 * (b - a) * x + 0.5 * (b + a)
    w_esc = 0.5 * (b - a) * w
    return x_esc, w_esc
```

La función de la celda anterior se encarga de escalar los puntos
y los pesos en un intervalo de a a b.

```python
Ns = np.arange(5,21)
Is = []
```

Se hace una matriz que contiene los números del 5 al 21
para luego usar en la formula de la cuadratura gaussiana.
También se hace una matriz vacía llamada Is para 
registrar los valores de cada aproximación hecha con la 
cuadratura gaussiana junto con el N respectivo usado.

```python
for N in Ns:
    x,w = gaussXyW(N)
    x_esc,w_esc = gaussXyWesc(0,np.pi,x,w)
    Integral = np.sum(w_esc * np.sin(x_esc ** 2))
    Is.append(Integral)
    print("N: ", N, "Valor aproximado de la integral: ", Integral)
```
El bucle for anteriror se encarga de evaluar la función gaussXyW en la 
cantidad N indicada en cada iteración, luego se escalan los puntos y los pesos 
y por último se hace la integral con los pesos y los puntos ya escalados.

También se imprime la cantidad de puntos usada a la par del valor aproximado obtenido
para el resultado de la integral.
