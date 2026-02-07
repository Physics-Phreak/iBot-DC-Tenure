#include <Arduino.h>

int main() {
  init();

  DDRB = 0b00000100; //D10 output, D9 input
  PORTB |= (1u << 1); //Pullup enabled

  int drop = 0;
  uint8_t inputState = 0x00;

  while (1){
    inputState = PINB & 0b00000010;

    if (!drop && !inputState){
      delay(20);
      drop = 1;
      PORTB ^= 0b00000100;
    }

    if (drop && inputState){
      drop = 0;
    }
  }
}