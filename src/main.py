VALORACION_PARTIDA: tuple = ("Sigue practicando", "Buen resultado", "Excelente")
PUNTOS_X_ACIERTO: int = 3
PENALIZACION_X_ERROR: int = 1

def calcular_resultados(aciertos: int, errores: int) -> tuple[int, int]:
    cant_preguntas: int = aciertos + errores
    puntuación: int = (aciertos * PUNTOS_X_ACIERTO) - (errores * PENALIZACION_X_ERROR)
    return cant_preguntas, puntuación

def valorar_partida(puntuacion: int) -> str:
    if puntuacion < 10:
        return VALORACION_PARTIDA[0]
    elif puntuacion < 20:
        return VALORACION_PARTIDA[1]
    else:
        return VALORACION_PARTIDA[2]

def main():
    aciertos: int = int(input("Introduce la cantidad de aciertos: "))
    errores: int = int(input("Introduce la cantidad de errores: "))
    if (aciertos < 0) or (errores < 0):
        print("Error: Introduce números positivos")
    else:
        resultado: tuple = calcular_resultados(aciertos, errores)
        print(f"Preguntas respondidas: {resultado[0]}")
        print(f"Puntuación: {resultado[1]}")
        valoracion: str = valorar_partida(resultado[1])
        print(f"Valoración: {valoracion}")

if __name__ == "__main__":
    main()