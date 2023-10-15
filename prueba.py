import RPI.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.output(11, 1)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, 1)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15, 1)

try:
    while (True):
        pregunta = input("RGB:")
        if (len(pregunta) == 3):
            GPIO.output(11, int(pregunta[0]))
            GPIO.output(13, int(pregunta[1]))
            GPIO.output(15, int(pregunta[2]))

except KeyboardInterrupt:
    GPIO.cleanup()
