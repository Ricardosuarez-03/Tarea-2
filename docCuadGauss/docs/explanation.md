# Explicacion del metodo de cuadratura Gaussiana

La cuadratura Gaussiana es un metodo por el cual se pueden aproximar resultados de integrales definidas, en especial de aquellas que son mas dificiles de calcular analiticamente.

El metodo consiste en evaluar la funcion en una cierta cantidad de puntos equidistantes llamados puntos de muestreo (usualmente representados por x_i) y multiplicarla por su peso asociado (w_i).Llegando a la idea de que usualmente entre mayor cantidad de puntos se use mas exacta es la aproximacion de la integral.

La forma usual de la integral es :

$$
\int{a}^{b} f(x)\,dx \sim \sum_{i=1}^{N} w_i f(x_i)
$$ 


