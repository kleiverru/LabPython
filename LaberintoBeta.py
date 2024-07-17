import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (90, 198, 237)
NEGRO = (1, 2, 3)
VERDE = (6, 255, 6)
ROJO = (244, 70, 17)

# Configuración del laberinto
laberinto = [
    "#####################",
    "#                   #",
    "#   #   ?   #   #   #",
    "#   #       #   #   #",
    "#   ###########   # #",
    "# ?             # # #",
    "#   #   #######   # #",
    "#   #   #         # #",
    "#   # ? #   ####### #",
    "#   #   #           #",
    "#   #   ########### #",
    "# ? #               #",
    "#   #########   #   #",
    "#              #  ? #",
    "########### ? ##### #",
    "#                   #",
    "#####################"
]

# Configuración del juego
ancho, alto = len(laberinto[0]) * 30, len(laberinto) * 30
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Laberinto")

# Coordenadas del jugador
jugador_x = 1
jugador_y = 1

# Lista de preguntas y respuestas sobre integrales
preguntas_respuestas = [
    {"pregunta": "¿Cuál es la integral de e^x?", "respuesta": "e^x + C"},
    {"pregunta": "¿Cuál es la integral de sen(x)?", "respuesta": "-cos(x) + C"},
    {"pregunta": "¿Cuál es la integral de cos(x)?", "respuesta": "sen(x) + C"},
    {"pregunta": "¿Cuál es la integral de tan(x)?", "respuesta": "-ln|cos(x)| + C"},
    {"pregunta": "¿Cuál es la integral de sec^2(x)?", "respuesta": "tan(x) + C"},
    {"pregunta": "¿Cuál es la integral de csc^2(x)?", "respuesta": "-cot(x) + C"},
    {"pregunta": "¿Cuál es la integral de sec(x)tan(x)?", "respuesta": "sec(x) + C"},
    {"pregunta": "¿Cuál es la integral de csc(x)cot(x)?", "respuesta": "-csc(x) + C"},
    {"pregunta": "¿Cuál es la integral de ln(x)?", "respuesta": "xln(x) - x + C"},
    {"pregunta": "¿Cuál es la integral de 1/(1+x^2)?", "respuesta": "arctan(x) + C"},
    {"pregunta": "¿Cuál es la integral de 1/√(1-x^2)?", "respuesta": "arcsen(x) + C"},
    {"pregunta": "¿Cuál es la integral de e^(x^2)?", "respuesta": "(√π/2)erf(x) + C"},
    {"pregunta": "¿Cuál es la integral de (1+e^x)/(1+e^(2x))? ", "respuesta": "x + ln(1 + e^x) - ln(1 + e^(2x)) + C"},
    {"pregunta": "¿Cuál es la integral de tan(x)sec(x)?", "respuesta": "sec(x) + C"},
    {"pregunta": "¿Cuál es la integral de 1/ln(x)?", "respuesta": "Li(x) + C"},
    {"pregunta": "¿Cuál es la integral de sen^2(x)?", "respuesta": "(1/2)(x - sen(x)cos(x)) + C"},
    {"pregunta": "¿Cuál es la integral de e^(-x^2)?", "respuesta": "(√π/2)erf(x) + C"},
    {"pregunta": "¿Cuál es la integral de sen^3(x)?", "respuesta": "(1/3)cos(x) - (1/3)cos^3(x) + C"},
    {"pregunta": "¿Cuál es la integral de 1/(1+e^x)?", "respuesta": "ln|e^x + 1| - x + C"},
    {"pregunta": "¿Cuál es la integral de e^xsen(x)?", "respuesta": "(1/2)e^x(sen(x) - cos(x)) + C"},
    {"pregunta": "¿Cuál es la integral de (2x+1)/(x^2+x+1)?", "respuesta": "ln|x^2 + x + 1| + C"},
    {"pregunta": "¿Cuál es la integral de tan^2(x)?", "respuesta": "tan(x) - x + C"},
    {"pregunta": "¿Cuál es la integral de x/(x^2+1)?", "respuesta": "ln|x^2 + 1|/2 + C"},
    {"pregunta": "¿Cuál es la integral de 1/√(1-tan^2(x))? ", "respuesta": "arcsen(tan(x)) + C"},
    {"pregunta": "¿Cuál es la integral de sen(x)cos(x)?", "respuesta": "(1/2)sen^2(x) + C"},
    {"pregunta": "¿Cuál es la integral de (e^x - e^(-x))/2?", "respuesta": "senh(x) + C"},
    {"pregunta": "¿Cuál es la integral de 1/(sen(x)+cos(x))? ", "respuesta": "tan(π/4 - x/2) + C"},
    {"pregunta": "¿Cuál es la integral de 1/√(1-sen^2(x))? ", "respuesta": "arccos(sen(x)) + C"},
]

# Estado del juego
jugando = True

# Función para dibujar el laberinto y el jugador
def dibujar_laberinto():
    ventana.fill(BLANCO)

    for y, fila in enumerate(laberinto):
        for x, celda in enumerate(fila):
            rect = pygame.Rect(x * 30, y * 30, 30, 30)
            if celda == "#":
                pygame.draw.rect(ventana, NEGRO, rect)
            elif celda == "?":
                pygame.draw.rect(ventana, VERDE, rect)
            if x == jugador_x and y == jugador_y:
                pygame.draw.circle(ventana, ROJO, (x * 30 + 15, y * 30 + 15), 10)

# Función para manejar eventos del teclado
def manejar_teclado(event):
    global jugador_x, jugador_y

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            if jugador_y > 0 and laberinto[jugador_y - 1][jugador_x] != "#":
                jugador_y -= 1
        elif event.key == pygame.K_DOWN:
            if jugador_y < len(laberinto) - 1 and laberinto[jugador_y + 1][jugador_x] != "#":
                jugador_y += 1
        elif event.key == pygame.K_LEFT:
            if jugador_x > 0 and laberinto[jugador_y][jugador_x - 1] != "#":
                jugador_x -= 1
        elif event.key == pygame.K_RIGHT:
            if jugador_x < len(laberinto[0]) - 1 and laberinto[jugador_y][jugador_x + 1] != "#":
                jugador_x += 1

# Función para mostrar la pregunta y verificar la respuesta
def mostrar_pregunta():
    global respuesta_ingresada

    pregunta_respuesta = random.choice(preguntas_respuestas)
    pregunta = pregunta_respuesta["pregunta"]
    respuesta_correcta = pregunta_respuesta["respuesta"]

    print("Pregunta:", pregunta)
    respuesta_ingresada = input("Respuesta: ")

    # Verificar la respuesta
    if respuesta_ingresada.lower() == respuesta_correcta.lower():
        print("¡Respuesta correcta!")
        # Eliminar la pregunta respondida del laberinto
        laberinto[jugador_y] = laberinto[jugador_y][:jugador_x] + ' ' + laberinto[jugador_y][jugador_x+1:]
    else:
        print("Respuesta incorrecta. Inténtalo de nuevo.")

reloj = pygame.time.Clock()

while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
        elif event.type == pygame.KEYDOWN:
            manejar_teclado(event)

    if laberinto[jugador_y][jugador_x] == "?":
        mostrar_pregunta()

    dibujar_laberinto()

    pygame.display.flip()

    if "?" not in "".join(laberinto):
        jugando = False

    reloj.tick(10)

pygame.quit()
sys.exit()
