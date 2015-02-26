#!python

# author: karen, date: 26 Feb 2015

#---------------------
# LIBRARIES
#---------------------

import serial # pySerial need to be installed
from pyo import *
import time

from skype import skype_callto

#---------------------
# METHODS
#---------------------

def play_transformed_signal(pitch_shift, spin):
	
	s.start()
	start = time.time()
	inp = Input(chnl=0, mul=0.5)
	indel = Delay(inp, delay=5)
	if spin == 'up': pitch_shift += 100
	elif: spin == 'down': pitch_shift -= 100
	b = FreqShift(indel, shift=pitch_shift).out()
	s.gui(locals())

	# terminate after 10s
	while  True:
		if time.time()-start > 10 : 
			s.stop()
			break
	
	# return new pitch
	return pitch_shift

def play_file(path):

	s.start()
	sf = SfPlayer(path, speed=1).out()
	s.gui(locals())
	s.stop()

def get_number():
	start = time.time()
	number = ''
	while time.time()-start <  20:
		number += ser.readline():
	return number

#---------------------
# SET UP
#---------------------

#TODO: Start jack in bash

initial_instructions = 'path..'
# serial port arduino
ser = serial.Serial('/dev/tty.usbserial', 9600)

# mic input
pa_list_devices()
print "Default input:", pa_get_default_input()
s = Server(duplex=1)
# If mic is not the default, assigned it from the list printed by pa_list_devices
# s.setInputDevice(0)
s.boot()


#---------------------
# MAIN LOOP
#---------------------


while  True:
	
	# wait for new user		
	while True:
		if 'pick_up' in ser.readline(): break

	# delay cuz the user needs to take the receiver to its ear
	time.sleep(1)

	# read instructions to user
	play_file(initial_instructions)
	
	# user now adjust voice transformaion of desire
	start = time.time()
	shift = 0 # shift paramther in Hertz
	while True:
		# check if user hang-up
		if 'hang_up' in ser.readline(): continue
		# user adjusts pitch transformation of desire
		elif '1' in ser.readline(): shift = play_transformed_signal(shift, 'up')
		elif '2' in ser.readline(): shift = play_transformed_signal(shift, 'down')
		# user is happy. continue to skype call
		elif '3' in ser.readline(): break 
		
		# TODO: repeat instruction  after some time when nothing happend


	# instruct the user to dial a number
	play_file(dial_instructions)

	# get number from serial port
	number = get_number()
	# start transformation 
	skype_callto(number)