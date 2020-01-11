from ecranLCD import *
from grovepi import *
from capacitive2 import *
import time
import pygame

pygame.init()
pygame.mixer.init(buffer=8)

ultrasonic = 4

instrument = "Piano"
newInstrument = instrument

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

while True:
	distance = ultrasonicRead(ultrasonic)
	if distance < 7:
		newInstrument = "Piano"
		setRGB(255,0,0)
	elif distance < 14:
		newInstrument = "Flute"
		setRGB(0,255,0)
	elif distance < 21:
		newInstrument = "Saxophone"
		setRGB(0,0,255)
	elif distance < 28:
		newInstrument = "Batterie"
		setRGB(128,128,0)
	elif distance < 35:
		newInstrument = "Marimba"
		setRGB(128,0,128)

	if newInstrument != instrument:
		instrument = newInstrument
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
	
	currentTap = readData(0x5b)
	for i in range(12):
		pin_bit = 1 << i
		if currentTap & pin_bit and not lastTap & pin_bit:
			son[i].play()
	lastTap = currentTap
