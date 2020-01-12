from ecranLCD import *
from grovepi import *
from capacitive2 import *
from donnees import *
import time
import pygame

pygame.init()
pygame.mixer.init(buffer=8)

ultrasonic = 4

instrument = "Piano"
newInstrument = instrument
lastTemps = time.time()

setRGB(255,0,0)
setText(instrument)

son = [
pygame.mixer.Sound("{}/Do.wav".format(instrument)),
pygame.mixer.Sound("{}/Do.wav".format(instrument)),
pygame.mixer.Sound("{}/Do.wav".format(instrument)),
pygame.mixer.Sound("{}/Do.wav".format(instrument)),
pygame.mixer.Sound("{}/Do.wav".format(instrument)),
pygame.mixer.Sound("{}/Do.wav".format(instrument)),
pygame.mixer.Sound("{}/Do.wav".format(instrument)),
pygame.mixer.Sound("{}/Do.wav".format(instrument)),
pygame.mixer.Sound("{}/Do.wav".format(instrument)),
pygame.mixer.Sound("{}/Do.wav".format(instrument)),
pygame.mixer.Sound("{}/Do.wav".format(instrument)),
pygame.mixer.Sound("{}/Do.wav".format(instrument))
]

setup(0x5b)
last_touched = readData(0x5b)
lastTap = 0

cont = True

while cont:
	distance = ultrasonicRead(ultrasonic)
	if distance < 3:
		cont = False
	elif distance < 10:
		newInstrument = "Piano"
		setRGB(255,0,0)
	elif distance < 17:
		newInstrument = "Flute"
		setRGB(0,255,0)
	elif distance < 24:
		newInstrument = "Saxophone"
		setRGB(0,0,255)
	elif distance < 31:
		newInstrument = "Batterie"
		setRGB(128,128,0)
	elif distance < 38:
		newInstrument = "Marimba"
		setRGB(128,0,128)

	if newInstrument != instrument:
		setText(newInstrument)
		newTemps = time.time()
		temps = newTemps - lastTemps
		temps = int(temps)
		envoyer(instrument,temps)
		lastTemps = newTemps
		instrument = newInstrument
		son = [
		pygame.mixer.Sound("{}/Do.wav".format(instrument)),
		pygame.mixer.Sound("{}/Do.wav".format(instrument)),
		pygame.mixer.Sound("{}/Do.wav".format(instrument)),
		pygame.mixer.Sound("{}/Do.wav".format(instrument)),
		pygame.mixer.Sound("{}/Do.wav".format(instrument)),
		pygame.mixer.Sound("{}/Do.wav".format(instrument)),
		pygame.mixer.Sound("{}/Do.wav".format(instrument)),
		pygame.mixer.Sound("{}/Do.wav".format(instrument)),
		pygame.mixer.Sound("{}/Do.wav".format(instrument)),
		pygame.mixer.Sound("{}/Do.wav".format(instrument)),
		pygame.mixer.Sound("{}/Do.wav".format(instrument)),
		pygame.mixer.Sound("{}/Do.wav".format(instrument))
		]
	
	currentTap = readData(0x5b)
	for i in range(12):
		pin_bit = 1 << i
		if currentTap & pin_bit and not lastTap & pin_bit:
			son[i].play()
	lastTap = currentTap

newTemps = time.time()
temps = newTemps - lastTemps
temps = int(temps)
envoyer(instrument,temps)
setRGB(0,0,0)
setText("Debrancher")

