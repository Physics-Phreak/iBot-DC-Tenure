#include <Arduino.h>

int main() {

  init();
  DDRB = 0b00100000;
  
  while (1) {
    PORTB = 0b00100000;
    delay(500);
    PORTB = 0b00000000;
    delay(500);
  }
}