def startGame():
    print("Comienza el juego")
    print("En esta historia, un crimen ha ocurrido a bordo del SS Elysium.")
    print("Usaremos lógica proposicional y un SAT-Solver para encontrar al culpable.")
    input("Presiona enter para continuar...") 

def logicGame():
    print("Hola, bienvenido al proyecto capstone de la asignatura Lógica. ¿Qué desea hacer?")
    print("1. Iniciar el juego")
    print("2. Conocer a los integrantes del equipo")
    print("3. Salir")

    option = int(input("Elige una opción: "))
    if option == 1:
        startGame()
    elif option == 2:
        print("Conocé a los integrantes del equipo")
    elif option == 3:
        exit()

logicGame()