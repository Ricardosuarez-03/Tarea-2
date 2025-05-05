## Referencias

### Funciones

#### gaussXyW

Calcula los puntos y los pesos para la cuadratura Gaussiana.

**Parametros:**

 **N** (int): Número de puntos a utilizar.

**Retorna:**

 **tupla**: Una tupla que contiene:
    
    x (ndarray): Los puntos para la cuadratura.
    w (ndarray): Los pesos de los puntos.

**Ejemplo:**

```python
   gaussXyW(2)

   (array([-0.57735027,  0.57735027]), array([1., 1.]))

```

x, w = np.polynomial.legendre.leggauss(N)

return x, w


#### gaussXyWesc

Escala los puntos y los pesos calculados en la función anterior para un intervalo [a,b].

**Parametros:**

  **a** (float): Límite inferior del intervalo de integración escalado.

  **b** (float): Límite superior del intervalo de integración escalado.

  **x** (ndarray): Puntos de cuadratura en el intervalo original.

  **w** (ndarray): Pesos de cuadratura en el intervalo original.

**Retorna:**

  **tupla**: Una tupla que contiene:
    
    x_esc (ndarray): Los puntos escalados.
    w_esc (ndarray): Los pesos escalados.

**Ejemplo:**

```python
   gaussXyWesc(0, np.pi, x, w)

   (array([0.37024024, 2.77135241]), array([1.57079633, 1.57079633]))

```

x_esc = 0.5 * (b - a) * x + 0.5 * (b + a)

w_esc = 0.5 * (b - a) * w

return x_esc, w_esc
 
