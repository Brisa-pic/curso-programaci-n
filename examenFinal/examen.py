import random

class JuegoAdivinanza: #Definion de la clase 
    def __init__(self): #Atributos de la clase
        self.numeroSecreto = random.randint(1,100)
        self.intentos = 0

    def validarNumero(self):
        
        numeroJugador = int(input("Ingrese el numero: "))
        self.intentos +=1

        if numeroJugador > self.numeroSecreto:
            print("El numero secreto es menor")
            return False
            
        elif numeroJugador < self.numeroSecreto:
            print("El numero secreto es mayor")
            return False
           
        else:
            print("El numero es correcto, has ganado!!!")
            return True
            

    def registrarIntento(self):
        self.intentos += 1

    def reiniciar(self):
        self.intentos = 0
        self.numeroSecreto = random.randint(1,100)
        print("El juego se reinicio")

class Jugador: #Definicion de la clase Jugador

    def __init__(self, nombre): #Atributo de jugador
        self.nombre = nombre
        self.historial = []

    def registrarJugador(self):
        nombre = input("Ingrese el nombre del jugador: ")
        return Jugador(nombre)

    def historial(self, intentos, ganar):
        self.historial.append((intentos,ganar))

    def estadisticas(self):
        total = len(self.historial)
        partidasGanadas = 0
        for partida in self.historial:
            if partida[1]: #Si es True
                partidasGanadas +=1
        porcentajeGanadas = (partidasGanadas/total)*100
        partidasPerdidas = total-partidasGanadas

    def guardarEstadisticas(self):

        with open("estadisticas.txt", "w") as file:
            file.write("Jugador: {self.nombre}\nPartidas: {total}\nGanadas: {partidasGanadas}\nPerdidas: {partidasPerdidas}\nPorcentaje Ganadas: {porcentajeGanadas}\n")

        file.close() # Importante cerrar el file al final


def menu(): # Función principal del menú

    continuar = True
    jugador = None
    while continuar:
        seleccion=input("""BIENVENIDO
                        Elija una opcion del menú principal:
        1. Comenzar una nueva partida
        2. Ver las estadisticas del jugador
        3. Salir del juego
    Elija una opcion: """)
        print() # Muestra el menú con las opciones disponibles

        match seleccion: # Utiliza el match para ejecutar la opción seleccionada
            case "1":
                if jugador is None:
                    jugador = Jugador("")  # Crea el jugador sin nombre
                    jugador = jugador.registrarJugador()  #Asignar un nombre
                juego = JuegoAdivinanza()  # Nuevo juego
                ganar = False
                while not ganar:
                    juego.validarNumero()
                    
            case "2":
                jugador.estadisticas()

            case "3":
                print("Guardando estadisticas...")
                jugador.guardarEstadisticas()
                print("Saliendo...")
                break # Termina el bucle

            case _: 
                    print("Esa opcion no existe, intentalo de nuevo")

menu() # Llama a la función menu para iniciar el programa