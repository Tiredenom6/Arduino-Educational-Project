import serial
import pydirectinput
import pyautogui

arduino = serial.Serial('COM3', 9600, timeout=.1)  # Establishes a serial connection with Arduino on COM3 port.

pydirectinput.PAUSE = 0  # Sets the delay between pydirectinput commands to 0.

keysDown = {}  # A dictionary to keep track of currently pressed keys.


def keyDown(key):
    """
    Simulates a key press event.

    Arguments:
    - key: The key to be pressed.
    """
    keysDown[key] = True  # Adds the key to the keysDown dictionary.
    pydirectinput.keyDown(key)  # Simulates a key press using pydirectinput.


def keyUp(key):
    """
    Simulates a key release event.

    Arguments:
    - key: The key to be released.
    """
    if key in keysDown:
        del keysDown[key]  # Removes the key from the keysDown dictionary.
        pydirectinput.keyUp(key)  # Simulates a key release using pydirectinput.


def handleJoyStickAsArrowKeys(x, y, j1click, j2click, r_btn, top_btn, bottom_btn):
    """
    Maps joystick inputs to arrow keys and performs corresponding actions.

    Arguments:
    - x: X-axis input from the joystick.
    - y: Y-axis input from the joystick.
    - j1click: Joystick button 1 click status (1 for pressed, 0 for not pressed).
    - j2click: Joystick button 2 click status (1 for pressed, 0 for not pressed).
    - r_btn: Right button click status (1 for pressed, 0 for not pressed).
    - top_btn: Top button click status (1 for pressed, 0 for not pressed).
    - bottom_btn: Bottom button click status (1 for pressed, 0 for not pressed).
    """
    if x == 0:
        keyDown('w')
        keyUp('s')
    elif x == 2:
        keyDown('s')
        keyUp('w')
    else:
        keyUp('w')
        keyUp('s')

    if y == 0:
        keyDown('d')
        keyUp('a')
    elif y == 2:
        keyDown('a')
        keyUp('d')
    else:
        keyUp('a')
        keyUp('d')

    if j1click == 0:
        keyDown('q')
    else:
        keyUp('q')

    if j2click == 0:
        keyDown('e')
    else:
        keyUp('e')

    if r_btn == 0:
        pydirectinput.click(button='right')

    if top_btn == 0:
        keyDown('esc')
    else:
        keyUp('esc')

    if bottom_btn == 0:
        pydirectinput.click(button='left')


while True:
    rawdata = arduino.readline()  # Reads a line of serial data from Arduino.

    try:
        string = str(rawdata.decode('utf-8'))  # Decodes the raw data as a UTF-8 string.
        j1xInput, j1yInput, j1Button, j2xInput, j2yInput, j2Button, rightButton, topButton, bottomButton = string.split(
            ',')

        j1xInput = int(j1xInput)
        j1yInput = int(j1yInput)
        j1Button = int(j1Button)
        j2xInput = int(j2xInput)
        j2yInput = int(j2yInput)
        j2Button = int(j2Button)
    rightButton = int(rightButton)
    topButton = int(topButton)
    bottomButton = int(bottomButton)

    handleJoyStickAsArrowKeys(j1xInput, j1yInput, j1Button, j2Button, rightButton, topButton, bottomButton)
    pyautogui.moveRel(j2xInput, j2yInput)

except ValueError:
Pass
