from collections import deque
from time import perf_counter

INICIAL = (3, 3, 0)
OBJETIVO = (0, 0, 1)

# Acciones: (misioneros, canibales)
ACCIONES = [
    (1, 0),
    (2, 0),
    (0, 1),
    (0, 2),
    (1, 1)
]

NOMBRES = {
    (1, 0): "1 misionero",
    (2, 0): "2 misioneros",
    (0, 1): "1 canibal",
    (0, 2): "2 canibales",
    (1, 1): "1 misionero y 1 canibal"
}

def estado_valido(estado):

    m, c, b = estado

    # Limites de misioneres y canibales
    if not (0 <= m <= 3 and 0 <= c <= 3):
        return False

    # Posicion del bote
    if b not in (0, 1):
        return False

    # Orilla izquierda
    if m > 0 and c > m:
        return False

    # Seguridad en la orilla derecha
    mr = 3 - m
    cr = 3 - c

    if mr > 0 and cr > mr:
        return False

    return True

def obtener_sucesores(estado):

    m, c, bote = estado
    sucesores = []

    for m_en_bote, c_en_bote in ACCIONES:

        if bote == 0:

            nuevo = (m - m_en_bote, c - c_en_bote, 1)

        else:

            nuevo = (m + m_en_bote, c + c_en_bote, 0)

        if estado_valido(nuevo):
            sucesores.append((nuevo, (m_en_bote, c_en_bote)))

    return sucesores