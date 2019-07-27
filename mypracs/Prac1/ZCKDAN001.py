#!/usr/bin/python3
"""

Readjust this Docstring as follows:
Names: Daniel Zuckerman
Student Number: ZCKDAN001
Prac: 1
Date: 29/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO

# Logic that you write
def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)	#Setting GPIO output pins for the 3 LEDS and setting the LEDS to off.
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)

    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)

    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)	#Setting up input pins for the 2 pushbuttons
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(16, GPIO.FALLING, bouncetime=200)	#interrupts for the pushbuttons
    GPIO.add_event_callback(16, buttonOneHandler)

    GPIO.add_event_detect(18, GPIO.FALLING, bouncetime=200)
    GPIO.add_event_callback(18, buttonTwoHandler)

    while True:
        pass

def buttonOneHandler (pin):	#When this button is pressed, the counter increments by 1 and is set back to 0 
    global counter              #when the maximum value is reached
    counter = counter+1
    if counter >= 8:
        counter = 0
    update()

def buttonTwoHandler (pin):	#when this button is pressed, the counter decrements by 1 and is set to 7
    global counter		#when the minimum value 0 is passed.
    counter = counter-1
    if counter < 0:
        counter = 7
    update()

def update():			#This function updates the 3 LEDS and turns on or off each LED dependent of the
    global counter		#binary value of the counter.
    binary_counter = '{0:03b}'.format(counter)
    if binary_counter[0:1] == '1':
        GPIO.output(11, GPIO.HIGH)
    else:
        GPIO.output(11, GPIO.LOW)
    if binary_counter[1:2] == '1':
        GPIO.output(13, GPIO.HIGH)
    else:
        GPIO.output(13, GPIO.LOW)
    if binary_counter[2:3] == '1':
        GPIO.output(15, GPIO.HIGH)
    else:
        GPIO.output(15, GPIO.LOW)

# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        counter = 0
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)

