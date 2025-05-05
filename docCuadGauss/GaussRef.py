def gaussXyW(N):
    """Calcula los puntos y los pesos para la cuadratura Gaussiana.

    Parameters:
    N (int): Número de puntos a utilizar.

    Returns:
    tuple: Una tupla que contiene:
        - x (ndarray): Los puntos para la cuadratura.
        - w (ndarray): Los pesos de los puntos.

    Example:
        >>> gaussXyW(2)
        (array([-0.57735027,  0.57735027]), array([1., 1.]))

    """
    x, w = np.polynomial.legendre.leggauss(N)
    return x, w


def gaussXyWesc(a, b, x, w):
    """
    Escala los puntos y los pesos calculados en la función anterior para un intervalo [a,b].

    Ejemplo:
           gaussXyWesc(0, np.pi, x, w)
        Puntos escalados: [0.37024024, 2.77135241]
        Pesos escalados: [1.57079633, 1.57079633]

    Argumentos:
        a (float): Límite inferior del intervalo de integración escalado.
        b (float): Límite superior del intervalo de integración escalado.
        x (ndarray): Puntos para la cuadratura en el intervalo original.
        w (ndarray): Pesos respectivos para cada uno de los puntos en el intervalo original.

    Retorna:
        tupla: Retorna una tupla (x_esc, w_esc) con dos arrays:
            - x_esc (ndarray): Puntos para la cuadratura escalados para el nuevo intervalo.
            - w_esc (ndarray): Pesos para la cuadratura escalados para el nuevo intervalo.
    """
    x_esc = 0.5 * (b - a) * x + 0.5 * (b + a)
    w_esc = 0.5 * (b - a) * w
    return x_esc, w_esc

