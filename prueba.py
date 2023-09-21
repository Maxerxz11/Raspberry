import board
import adafruit_dht
import time

# Configura el pin GPIO al que está conectado el sensor DHT
pin = board.D4  # Reemplaza 'D4' con el número de pin GPIO que estás utilizando

# Inicializa el sensor
dht_sensor = adafruit_dht.DHT22(pin)

try:
    while True:
        # Lee la temperatura y la humedad
        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity

        print(f'Temperatura: {temperature:.2f}°C')
        print(f'Humedad: {humidity:.2f}%')

        time.sleep(2)  # Espera 2 segundos antes de la siguiente lectura

except KeyboardInterrupt:
    pass

# Cierra el sensor al finalizar
dht_sensor.exit()
