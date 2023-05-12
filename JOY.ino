#include <ezButton.h>


ezButton joystick1Button(3); // Connect Joystick 'Button' to pin 3
const int j1xPin = A4;       // Connect Joystick X direction to pin A4
const int j1yPin = A5;       // Connect Joystick Y direction to pin A5
int j1xOutput;
int j1yOutput;


ezButton joystick2Button(2); // Connect Joystick 'Button' to pin 2
const int j2xPin = A2;       // Connect Joystick X direction to pin A2
const int j2yPin = A3;       // Connect Joystick Y direction to pin A3
int j2xOutput;
int j2yOutput;


ezButton rightButton(5);     // Connect Right button to pin 5
ezButton topButton(10);      // Connect Top button to pin 10
ezButton bottomButton(7);    // Connect Bottom button to pin 7


void setup() {
  joystick1Button.setDebounceTime(50);
  joystick2Button.setDebounceTime(50);
  rightButton.setDebounceTime(50);
  topButton.setDebounceTime(50);
  bottomButton.setDebounceTime(50);


  Serial.begin(9600);  // Initialize serial communication at 9600 baud rate
}


void loop() {
  joystick1Button.loop();
  joystick2Button.loop();
  rightButton.loop();
  topButton.loop();
  bottomButton.loop();


  int j1BtnState = joystick1Button.getState();
  int j2BtnState = joystick2Button.getState();
  int rghtBtnState = rightButton.getState();
  int topBtnState = topButton.getState();
  int btmBtnState = bottomButton.getState();


  int jx1 = analogRead(j1xPin) - 518;  // Read X direction value and subtract 518 to center it around 0
  int jy1 = analogRead(j1yPin) - 510;  // Read Y direction value and subtract 510 to center it around 0


  if (jx1 < -10) {
    j1xOutput = 0;
  } else if (jx1 > 10) {
    j1xOutput = 2;
  } else {
    j1xOutput = 1;
  }


  if (jy1 < -10) {
    j1yOutput = 0;
  } else if (jy1 > 10) {
    j1yOutput = 2;
  } else {
    j1yOutput = 1;
  }


  int jx2 = analogRead(j2xPin) - 506;  // Read X direction value and subtract 506 to center it around 0
  int jy2 = analogRead(j2yPin) - 512;  // Read Y direction value and subtract 512 to center it around 0


  j2xOutput = -jx2 / 10;
  j2yOutput = jy2 / 10;


  Serial.print(j1xOutput);
  Serial.print(",");
  Serial.print(j1yOutput);
  Serial.print(",");
  Serial.print(j1BtnState);
  Serial.print(",");
  Serial.print(j2xOutput);
  Serial.print(",");
  Serial.print(j2yOutput);
  Serial.print(",");
  Serial.print(j2BtnState);
  Serial.print(",");
  Serial.print(rghtBtnState);
  Serial.print(",");
  Serial.print(topBtnState);
  Serial.print(",");
  Serial.println(btmBtnState);


  delay(150);  // Delay for 150
