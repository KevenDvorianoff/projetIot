import smbus
import time

bus = smbus.SMBus(1)

RGB_ADDR = 0x62
TEXT_ADDR = 0x3e

def setRGB(r,g,b):
	bus.write_byte_data(RGB_ADDR,0x00,0)
	bus.write_byte_data(RGB_ADDR,0x01,0)
	bus.write_byte_data(RGB_ADDR,0x04,r)
	bus.write_byte_data(RGB_ADDR,0x03,g)
	bus.write_byte_data(RGB_ADDR,0x02,b)
	bus.write_byte_data(RGB_ADDR,0x08,0xAA)

def textCommand(cmd):
	bus.write_byte_data(TEXT_ADDR,0x80,cmd)

def setText(text):
	textCommand(0x01)
	time.sleep(.05)
	textCommand(0x08 | 0x04)
	textCommand(0x28)
	time.sleep(.05)
	count = 0
	row = 0
	for c in text:
		if c == '\n' or count == 16:
			count = 0
			row += 1
			if row == 2:
				break
			textCommand(0xc0)
			if c == '\n':
				continue
		count += 1
		bus.write_byte_data(TEXT_ADDR,0x40,ord(c))