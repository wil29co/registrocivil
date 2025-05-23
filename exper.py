from PyQt5.QtCore import QTimer

def saludar():
    print("¡Hola cada segundo!")

# Crear un temporizador que dispare cada 1 segundo
temporizador = QTimer()
temporizador.timeout.connect(saludar)
temporizador.start(5)

