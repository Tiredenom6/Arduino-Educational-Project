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

3) 5V pins are power pins that output 5V of power.

4) GRND pins are pins that provide a ground. A ground is a sink for electricity to flow to out of a component or circuit. It can also be used as an electrical reference, indicating a voltage with respect to another voltage (most commonly zero). 
### Code       
The basic structure of an Arduino sketch consists of two main functions: setup() and loop(). The setup() function is executed only once when the board starts up or resets, and it is used to initialize variables, set pin modes, and configure the board for operation. The loop() function, on the other hand, is executed repeatedly while the board is powered on, and it is used to implement the main logic of the program.

Arduino code functions just as c++ does meaning the use of conditionals and loops is possible. Conditionals like if-else statements can be used to execute different blocks of code based on the value of a variable or a sensor input. Loops like for and while loops can be used to execute a block of code multiple times.

### Implementing Code on an Arduino 
To upload an Arduino sketch (The Code in the IDE) to an Arduino board, the board must be connected to the computer via a USB cable. When your code is written you can follow these steps,

          1) Verify your code. This will tell you if you have made any mistakes in your arduino code. To do this, click on the big check mark in the top left hand corner. 
          2) After the code is verified without issues, clicking on the arrow besides it will upload the code to the arduino. 
          
Once uploaded, the sketch will run on the board, cycling the loop function, until the board is reset or powered off.

### Physical Component Design
For a complete breakdown of the theory behind the hardware in this lab, view this [report](https://docs.google.com/document/d/e/2PACX-1vS3WdEL-KkDHfYp4SRyXxtGDpL3lxsCchkNDKFCQpd_L3ZP3N8ZAnA95ofz7l73UD2h2FUD6tp4fvtt/pub). 
For the purpose of this Lab, our hardware is designed around the Arduino. Arduino is a user friendly device becasue of all of the design tools that are free to use. A usefull tool is the web-based application TinkerCad. It allows users to design and simulate circuits using a virtual breadboard, as well as program and simulate Arduino boards. For an indepth toutorial see [here](https://www.youtube.com/watch?v=Z_D-hXzbY_4). 
 
 
## Getting Started with the Lab 
### Hardware Documentation and Diagrams
For the complete block diagram see the Tinkercad diagram [here](https://www.tinkercad.com/things/djGwU0sTQ8e) or view the circuit diagram in this repository named Diagram.brd or circuit named Circuit.png.

Arduino Joysticks have five pins. In this Lab you use two joysticks, so there are ten pins to worry about. 
      
          1) GND - Ground Pin
          2) +5V - 5 Volts Pin
          3) VRX - X direction analog output
          4) VRY - Y direction analog output
          5) SW  - Joystick switch 
          
### Setting up your Circuit
The Joysticks are set up as follows, 

1) Attach your VRX pin to the arduino pin A4.
2) Attach your VRy pin to the arduino pin A5.
3) Attach your VRX pin of your second joystick to the arduino pin A2.
4) Attach your VRY pin of your second joystick to the arduino pin A3.

Next you will need to apply a ground and power to both of your ground and 5V pins for the joysticks. This can be done by using the breadboard channels. For a guide on this see [here](https://www.youtube.com/watch?v=SVMKtyjULdk). 

The SW pin for joystick 1 will go to the digital pin 3 and the SW pin for joystick 2 will go to digital pin 2.

The buttons are setup a follows, 
1) Button one has one leg connected to digital pin D5 and another to ground.
2) Button two has one leg connected to digital pin D5 and another to ground.
3) Button three has one leg connected to digital pin D5 and another to ground.

### Code Setup 
After setting up your circuit follow these directions to see the lab in action, 

        1) Open the code named JOY in the Arduino IDE. It can be found in this github repository and downloaded. 
        2) Next verify using the checkmark button previously mentioned and upload the code using the arrow button to the Arduino. 
        3) Next open the PyCharm code name pycode in the PyCharm IDE. This code can be found in this repository named PIERUN.
        4) WARNING - The inputs of this program are mapped to keys on your keyboard, be sure to have important windows closed!.
        5) In the top left click on the green play button to run you python code and see results. 

Open a game and see the fruits of your labor using the controller you made!
          




