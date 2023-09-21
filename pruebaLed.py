import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 4

while True:
    # LO que hago aca es declarar una varible de temperatura para sacar analizar con el sencor la funcion read es para leer sus datos
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)

    if temperatura is not None:
        print(temperatura)
        print(humedad)
        print("La temperatura es {}".format(temperatura, humedad))

    else:
        print("Error[-]")
