""" EE 250L Lab 02: GrovePi Sensors

List team members here.
Samantha Taylor

Insert Github repository link here:
https://github.com/usc-ee250-spring2021/lab02-samtaylor9.git
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a
default set of directories for modules when a program tries to `import` one.
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
from grove_rgb_lcd import *
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')


"""This if-statement checks if you are running this python file directly. That
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will
be true"""


if __name__ == '__main__':
    setText("Samantha Taylor\nEE250 Lab 2")

    # Connect the Grove Rotary Angle Sensor to analog port A2
    # SIG,NC,VCC,GND
    potentiometer = 2
    grovepi.pinMode(potentiometer,"INPUT")
    time.sleep(1)

    # Vcc of the grove interface is normally 5v
    grove_vcc = 5

    # Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
    full_angle = 300

    # Connect the Grove Ultrasonic Ranger to digital port D4
    # SIG,NC,VCC,GND
    ultrasonic_ranger = 4

    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)
        # FIXME: setText_norefresh("")

        # Read threshold value from potentiometer
        threshold_value = grovepi.analogRead(potentiometer)
        print(threshold_value)

        # Measure distance to object from ultrasonic ranger
        distance_to_object = (grovepi.ultrasonicRead(ultrasonic_ranger))
        print(distance_to_object)

        # Determines whether the object is within threshold distance
        if threshold_value > distance_to_object:
            setText_norefresh("%3dcm OBJ PRES\n%3dcm" % (threshold_value, distance_to_object))
        else:
            setText_norefresh("%3dcm         \n%3dcm" % (threshold_value, distance_to_object))
