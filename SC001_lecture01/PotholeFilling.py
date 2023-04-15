"""
File: PotholeFilling.py
Name: Yongqi
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    for i in range(3):
        go_in()
        put_99()
        go_out()


def put_99():
    for i in range(99):
        put_beeper()



def go_in():
    """
    pre-condition:Karel is at the upper left of the pothole ,facing East.
    post-condition:Karel is in the pothole facing North.
    """
    move()
    turn_right()
    move()
    turn_left()
    turn_left()



def go_out():
    """
    pre-condition:Karel is in the pothole facing North.
    post-condition:Karel is at the upper left of the pothole, facing East.
    """
    move()
    turn_right()
    move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
