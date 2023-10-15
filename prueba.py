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
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# Enciende el LED en rojo
GPIO.output(RED_PIN, GPIO.HIGH)
GPIO.output(GREEN_PIN, GPIO.LOW)
GPIO.output(BLUE_PIN, GPIO.LOW)

# Espera unos segundos
time.sleep(3)

# Apaga el LED
GPIO.output(RED_PIN, GPIO.LOW)
GPIO.output(GREEN_PIN, GPIO.LOW)
GPIO.output(BLUE_PIN, GPIO.LOW)

# Limpia los pines GPIO
GPIO.cleanup()
