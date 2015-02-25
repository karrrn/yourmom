
#include <Keypad.h>

const byte ROWS = 4; //four rows
const byte COLS = 7; //three columns
char keys[ROWS][COLS] = {
  {'4','5','6','A','r','R','?'},
  {'7','8','9','M','u','?','?'},
  {'*','0','#','W','d','S','?'},
  {'?','?','S','m','M','L','?'}
};
byte rowPins[ROWS] = {9,10,11,12}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {2,3,4,5,6,7,8}; //connect to the column pinouts of the keypad

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

void setup(){
  Serial.begin(9600);
}

void loop(){
  char key = keypad.getKey();

  if (key != NO_KEY){
    Serial.println(key);
  }
}
