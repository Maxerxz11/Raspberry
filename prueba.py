from gpiozero import DistanceSensor
from time import sleep

# Configuración del sensor
# Ajusta los pines según tu conexión
sensor = DistanceSensor(echo=23, trigger=24)

try:
    while True:
        distancia = sensor.distance * 100  # Convertir a centímetros
        print(f'Distancia: {distancia:.2f} cm')
        sleep(1)

except KeyboardInterrupt:
    print("Programa interrumpido por el usuario")
finally:
    pass
