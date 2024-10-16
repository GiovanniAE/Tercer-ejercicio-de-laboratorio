def saltos(mi_lista):
    """
    Función que determina si es posible llegar al final de una lista, dada una lista de números enteros donde cada 
    número representa la cantidad máxima de saltos que se pueden hacer desde esa posición.

    Parámetros:
    mi_lista (list): Lista de números enteros donde cada elemento indica la cantidad máxima de posiciones que 
                     se pueden avanzar desde esa posición.

    Retorna:
    bool: Retorna True si es posible llegar al final de la lista, False en caso contrario.
    """

    # Variable para controlar el alcance máximo posible que se puede alcanzar en la lista
    alcance = 0
    # Iterar sobre la lista para verificar si se puede alcanzar el final
    for i in range(len(mi_lista)):
        # Si el índice actual es mayor que el alcance máximo logrado hasta ahora, no se puede avanzar
        if i > alcance:
            return False
        # Actualiza el alcance con el máximo entre el alcance actual y el nuevo alcance posible desde la posición i
        alcance = max(alcance, i + mi_lista[i])
        # Si el alcance logrado ya es suficiente para llegar al final de la lista, retorna True
        if alcance >= len(mi_lista) - 1:
            return True
    # Si se termina el bucle sin alcanzar el final, retorna False
    return False
