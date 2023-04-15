"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:yongchi
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():

            move()
        else:
            jump()



def jump():
    """
    Pre-condition:Karel is on the left, facing East
    Post-condition:Karel is on the right

    :return:
    """
    up()
    cross()
    down()



def up():
    """
    Pre-condition:Karel is on the left, facing East
    Post-condition:Karel is on the right
    :return:
    """
    while not front_is_clear():
        turn_left()
        move()
        turn_right()
def cross():
    """
    Pre-condition:Karel is on the left, facing East
    Post-condition:Karel is on the right
    :return:
    """
    if front_is_clear():
        move()
        turn_right()
def down():
    while front_is_clear():
        move()
    turn_left()



def turn_right():
    for i in range(3):
        turn_left()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
