from saltos import saltos

def test_saltos():
    # Prueba 1: Debería devolver True
    assert saltos([1, 1, 2]) == True, "Error en el caso 1"

    # Prueba 2: Debería devolver False
    assert saltos([3, 2, 1, 0, 4]) == False, "Error en el caso 2"

    # Prueba 3: Debería devolver True
    assert saltos([3, 3, 1, 2, 0, 1]) == True, "Error en el caso 3"

    # Prueba 4: Debería devolver False (lista vacía)
    assert saltos([]) == False, "Error en el caso lista vacía"

    # Prueba 5: Debería devolver True (ya estamos en el único índice)
    assert saltos([0]) == True, "Error en el caso un solo elemento"

    print("Todos los tests pasaron exitosamente.")

if __name__ == "__main__":
    test_saltos()
