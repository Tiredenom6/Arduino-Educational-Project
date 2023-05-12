# Arduino Game Controller Lab Directions

This lab merges software with hardware to create a functioning physical device that recieves input and creates and drives a proccess. In this case, the arduino is recieving input from a series of sensors, converting them into a useable format, and then driving the game inputs based upon a python script. 

## Required Tools and Hardware
  1)  Arduino board or Arduino knock-off (i.e. Weemos). A cheaper model board can be found at the following link,
          [ELEGOO UNO R3 Board](https://www.amazon.com/ELEGOO-Board-ATmega328P-ATMEGA16U2-Compliant/dp/B01EWOE0UU/ref=asc_df_B01EWOE0UU/?tag=hyprod-20&linkCode=df0&hvadid=309751315916&hvpos=&hvnetw=g&hvrand=3132673754217622362&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9003488&hvtargid=pla-455309014075&psc=1&tag=&ref=&adgrpid=67183599252&hvpone=&hvptwo=&hvadid=309751315916&hvpos=&hvnetw=g&hvrand=3132673754217622362&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9003488&hvtargid=pla-455309014075).
  2)  Install and setup PyCharm the Python IDE. This can be found at the following link, [PyCharm](https://www.jetbrains.com/pycharm/).
  3)  Install the Arduino IDE. This can be found here [Arduino](https://www.arduino.cc/en/software).
  4)  Two Joystick Potentiometers or two potentiometers.
  5)  Four Buttons.  
## Inital Setup 

Adding the appropriate libraries for Arduino. 

         1) Open the IDE
         2) In the top of the screen go to "Tools" 
         3) In the pop down menu, click on "Manage Libraries"
         4) In the search bar, enter the following "ezButton" and click install on the result.
         ezButton is a useful arduino library that allows for simple button mapping using the digial inputs of the pins. 

Adding the appropriate libraries for PyCharm. 

          1) Open PyCharm IDE and open the project.
          2) Navigate to the bottom of the IDE and click on the Python Packages tab.
          3) In the search bar search for pyserial, pydirectinput, and pyautogui.
          4) For each of the libaries click install and wait for them to download.
          5) In the code, in the pycharm IDE, if the libary is not properly installed the name of the libary wil be highlighted in red.
          6) If there are any issues the following is a link to the Jetbarins guide to libary installation.
          https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html


## Familiarizing with Arduino
### Introduction 
Arduino code, also known as sketch, is written in the Arduino Integrated Development Environment (IDE), which is a software tool that provides a simplified and easy-to-use interface for programming Arduino boards. The Arduino code is written in the language C++ with some simplifications to make it simpler. Arduino is compeletly open source with extreme amounts of documentation on every faset of its structure. 

### Pin Types 
An Arduino is a physical component with different input and output pins. The analog to digital converter pins have the prefix A# while the digital pins have the prefix D#. When coding in arduino it is important to know which pins you will be working with. The difference is as follows, 

1) Digital (D) pins can be used to send and receive binary (on/off) signals or pulses, such as for controlling LEDs, motors, or reading the state of switches or sensors. These pins can be programmed to send a high or low voltage signal, which is interpreted as either a logical 1 or a logical 0.

2) Analog (A) pins, are designed to read analog signals. Analog signals are continuous and can have any value within a range, unlike digital signals which only have two values. These pins can be used to read signals from sensors that output analog voltages or currents, such as temperature sensors or light sensors. They can also be used as pulse width modulation (PWM) outputs, which allow you to create analog-like signals by rapidly turning a digital signal on and off.

### Code       
The basic structure of an Arduino sketch consists of two main functions: setup() and loop(). The setup() function is executed only once when the board starts up or resets, and it is used to initialize variables, set pin modes, and configure the board for operation. The loop() function, on the other hand, is executed repeatedly while the board is powered on, and it is used to implement the main logic of the program.

Arduino code functions just as c++ does meaning the use of conditionals and loops is possible. Conditionals like if-else statements can be used to execute different blocks of code based on the value of a variable or a sensor input. Loops like for and while loops can be used to execute a block of code multiple times.

### Implementing Code on an Arduino 
To upload an Arduino sketch (The Code in the IDE) to an Arduino board, the board must be connected to the computer via a USB cable. When your code is written you can follow these steps,

          1) Verify your code. This will tell you if you have made any mistakes in your arduino code. To do this, click on the big check mark in the top left hand corner. 
          2) After the code is verified without issues, clicking on the arrow besides it will upload the code to the arduino. 
          
Once uploaded, the sketch will run on the board, cycling the loop function, until the board is reset or powered off.

## Getting Started with Physical Components 
### Physical Component Design
For the purpose of this Lab, our hardware is designed around the Arduino. Arduino is a user friendly device becasue of all of the design tools that are free to use. A usefull tool is the web-based application TinkerCad. It allows users to design and simulate circuits using a virtual breadboard, as well as program and simulate Arduino boards. For an indepth toutorial see [here](https://www.youtube.com/watch?v=Z_D-hXzbY_4). 


