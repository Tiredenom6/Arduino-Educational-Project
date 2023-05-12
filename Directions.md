# Arduino Game Controller Lab Directions

### Required Tools and Hardware
  1)  Arduino board or Arduino knock-off (i.e. Weemos). A cheaper model board can be found at the following link,
          [ELEGOO UNO R3 Board](https://www.amazon.com/ELEGOO-Board-ATmega328P-ATMEGA16U2-Compliant/dp/B01EWOE0UU/ref=asc_df_B01EWOE0UU/?tag=hyprod-20&linkCode=df0&hvadid=309751315916&hvpos=&hvnetw=g&hvrand=3132673754217622362&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9003488&hvtargid=pla-455309014075&psc=1&tag=&ref=&adgrpid=67183599252&hvpone=&hvptwo=&hvadid=309751315916&hvpos=&hvnetw=g&hvrand=3132673754217622362&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9003488&hvtargid=pla-455309014075).
  2)  Install and setup PyCharm the Python IDE. This can be found at the following link, [PyCharm](https://www.jetbrains.com/pycharm/).
  3)  Install the Arduino IDE. This can be found here [Arduino](https://www.arduino.cc/en/software).

### Inital Setup 

Adding the appropriate libraries for Arduino. 

         1) Open the IDE
         2) In the top of the screen go to "Tools" 
         3) In the pop down menu, click on "Manage Libraries"
         4) In the search bar, enter the following "ezButton" and click install on the result.
         ezButton is a useful arduino library that allows for simple button mapping using the digial inputs of the pins. 

Adding the appropriate libraries for PyCharm. 


## Familiarizing with Arduino

### Pin Types 
An Arduino is a physical component with different input and output pins. The analog to digital converter pins have the prefix A# while the digital pins have the prefix D#. When coding in arduino it is important to know which pins you will be working with. The difference is as follows, 

1) Digital (D) pins can be used to send and receive binary (on/off) signals or pulses, such as for controlling LEDs, motors, or reading the state of switches or sensors. These pins can be programmed to send a high or low voltage signal, which is interpreted as either a logical 1 or a logical 0.

2) Analog (A) pins, are designed to read analog signals. Analog signals are continuous and can have any value within a range, unlike digital signals which only have two values. These pins can be used to read signals from sensors that output analog voltages or currents, such as temperature sensors or light sensors. They can also be used as pulse width modulation (PWM) outputs, which allow you to create analog-like signals by rapidly turning a digital signal on and off.


         
      



