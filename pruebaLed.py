import timer 
import Adafruit_DHT 

sencor = Adafruit_DHT.DHT22
pin=23

while True :
	temperatura = Adafruit_DHT.read_retry(sencor,pin) #LO que hago aca es declarar una varible de temperatura para sacar analizar con el sencor la funcion read es para leer sus datos

	if temperatura is not None:
		print("La temperatura es {}".format(temperatura))
	
	else:
		print("Error[-]")