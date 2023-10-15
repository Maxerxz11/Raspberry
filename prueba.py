import RPi.GPIO as GPIO
import time

# Deshabilitar las advertencias
GPIO.setwarnings(False)

# Configura los pines GPIO en modo BOARD
GPIO.setmode(GPIO.BCM)

# Define los números de pin físicos
RED_PIN = 17  # Reemplaza con el número de pin físico para el rojo
GREEN_PIN = 18  # Reemplaza con el número de pin físico para el verde
BLUE_PIN = 27  # Reemplaza con el número de pin físico para el azul

# Configura los pines como salida
GPIO.setup(RED_PIN, GPIO.OUT)


# Enciende el LED en rojo
GPIO.output(RED_PIN, GPIO.HIGH)


# Espera unos segundos
time.sleep(3)

# Apaga el LED
GPIO.output(RED_PIN, GPIO.LOW)


# Limpia los pines GPIO
GPIO.cleanup()
