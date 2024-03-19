import random

def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)

def validar_jugadores(cantidad):
    return cantidad >= 2 and cantidad <= 4

def seleccionar_nivel():
    print("Selecciona el nivel de tablero a jugar:")
    print("1. Nivel básico (Tablero de 20 posiciones)")
    print("2. Nivel intermedio (Tablero de 30 posiciones)")
    print("3. Nivel avanzado (Tablero de 50 posiciones)")
    print("4. Nivel experto (Tablero de 100 posiciones)")
    nivel = int(input("Elije una opción: "))
    while nivel < 1 or nivel > 4:
        nivel = int(input("Opción inválida. Por favor, elige una opción válida: "))
    return nivel

def jugar():
    cantidad_jugadores = int(input("Ingrese la cantidad de jugadores (2-4): "))
    while not validar_jugadores(cantidad_jugadores):
        cantidad_jugadores = int(input("Cantidad inválida de jugadores. Por favor, ingrese un número entre 2 y 4: "))
    
    nivel = seleccionar_nivel()
    meta = {1: 20, 2: 30, 3: 50, 4: 100}[nivel]

    jugadores = [0] * cantidad_jugadores
    pares_consecutivos = [0] * cantidad_jugadores
    ganador = None

    while ganador is None:
        for i in range(cantidad_jugadores):
            if ganador is not None:
                break
            input(f"\nTurno del jugador {i+1}. Presiona Enter para lanzar los dados...")
            dado1, dado2 = lanzar_dados()
            print(f"Jugador {i+1} lanzó: {dado1}, {dado2}")
            total = dado1 + dado2
            jugadores[i] += total

            if dado1 == dado2:
                pares_consecutivos[i] += 1
                if pares_consecutivos[i] == 3:
                    ganador = i + 1
                    break
            else:
                pares_consecutivos[i] = 0

            if jugadores[i] >= meta:
                ganador = i + 1
                break

            print(f"Jugador {i+1} está en la posición {jugadores[i]}")

    print(f"\n¡El jugador {ganador} ha ganado!")

if __name__ == "__main__":
    jugar()
