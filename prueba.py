import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
pin = 23

while True:
    # LO que hago aca es declarar una varible de temperatura para sacar analizar con el sencor la funcion read es para leer sus datos
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print("Error[-]")

except KeyboardInterrupt:
    print('Lectura del sensor detenida por el usuario.')

except Exception as e:
    print(f'Error: {e}')