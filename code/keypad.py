# #####################################################
# Python Library for 3x4 matrix keypad using
# 7 of the avialable GPIO pins on the Raspberry Pi.
#
# This could easily be expanded to handle a 4x4 but I
# don't have one for testing. The KEYPAD constant
# would need to be updated. Also the setting/checking
# of the colVal part would need to be expanded to
# handle the extra column.
#
# Written by Chris Crumpacker
# May 2013
#
# main structure is adapted from Bandono's
# matrixQPI which is wiringPi based.
# https://github.com/bandono/matrixQPi?source=cc
# #####################################################

import RPi.GPIO as GPIO

GPIO.cleanup()
SIGNAL = 40
PICK = 26

class keypad():
    # CONSTANTS   
    KEYPAD = [
        [7, 4, '*', 'Leer'],
        [8, 5, 0, 'Leer'],
        [9, 6, '#', 'Sprache'],
        ['R/Note', 'Pause/Alarm', 'AutoWdh', 'Gr. Lautsprecher'],
        ['Oben', 'Wiederwahl', 'Anrufliste', 'Menue'],
        [12,13,14,15],
        ['Leer', 'Rechner', 'Speichern', 'Kl. Lautsprecher']]


    ROW = [11,13,18,16]
    COLUMN = [37,35,33,23,21,24,22]


    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

    def getKey(self):
       
        # Set all columns as output low
        for j in range(len(self.COLUMN)):
            GPIO.setup(self.COLUMN[j], GPIO.OUT)
            GPIO.output(self.COLUMN[j], GPIO.LOW)
       
        # Set all rows as input
        for i in range(len(self.ROW)):
            GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
       
        # Scan rows for pushed key/button
        # A valid key press should set "rowVal"  between 0 and 3.
        rowVal = -1
        for i in range(len(self.ROW)):
            tmpRead = GPIO.input(self.ROW[i])
            if tmpRead == 0:
                rowVal = i

        
        # if rowVal is not 0 thru 3 then no button was pressed and we can exit
        if rowVal <0 or rowVal >10:
            self.exit()
            return
       
        # Convert columns to input
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
       
        # Switch the i-th row found from scan to output
        GPIO.setup(self.ROW[rowVal], GPIO.OUT)
        GPIO.output(self.ROW[rowVal], GPIO.HIGH)

        # Scan columns for still-pushed key/button
        # A valid key press should set "colVal"  between 0 and 2.
        colVal = -1
        for j in range(len(self.COLUMN)):
            tmpRead = GPIO.input(self.COLUMN[j])
            if tmpRead == 1:
                colVal=j
        
        # if colVal is not 0 thru 2 then no button was pressed and we can exit
        if colVal <0 or colVal >10:
            self.exit()
            return

        #print colVal,rowVal
        # Return the value of the key pressed
        self.exit()
        return self.KEYPAD[colVal][rowVal]
       
    def exit(self):
        # Reinitialize all rows and columns as input at exit
        for i in range(len(self.ROW)):
                GPIO.setup(self.ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        for j in range(len(self.COLUMN)):
                GPIO.setup(self.COLUMN[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)

def sendSignal(signalport = SIGNAL, time = 1):
    GPIO.setup(signalport, GPIO.OUT)
    GPIO.output(24, 1)
    sleep(time)
    GPIO.output(24, 0)
    return

def getPick(signalport = PICK):
    '''
    Returns True if 
    '''
    GPIO.setup(signalport, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    return GPIO.input(signalport)

class signals():
    def __init__(self):
        kp = keypad()

    def get_signals(self):
        digit = kp.getKey()
        pick = getPick()
        
        return digit, pick


if __name__ == '__main__':
    # Initialize the keypad class
    kp = keypad()
    # Loop while waiting for a keypress
    digit = None
    while digit == None:
        digit = kp.getKey()
    # Print the result
    print digit  