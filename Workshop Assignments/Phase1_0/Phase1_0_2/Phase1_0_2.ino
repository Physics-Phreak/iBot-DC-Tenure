#include <Arduino.h>
#include <stdint.h>

int main() {
  init();

  DDRB = 0xFF;
  PORTB = 0X00;

  uint16_t val = 0;
  int inc = 1;

  while(1){
    analogWrite(10, val);

    if (val == 255) inc = -1;
    if (val == 0) inc = 1;

    val += inc;
    delay(5);
  }

}

// Implements breathing on the onboard LED
/*
uint64_t lastCallTime;
int main() {
  init();
  DDRB = 0b00100000;
  
  uint64_t lastCallTime = micros();
  uint64_t delay = 500;

  uint16_t val = 0;
  int inc = 1;

  while(1) {
    pwm(5, val);
    
    if ((micros() - lastCallTime) > delay) {
      val += inc;
      lastCallTime = micros();
    }

    if (val == 1023) inc = -1;
    if (val == 0) inc = 1; 
  }
}
*/

// Wrote pwm in software for the fun of it, i know this isnt how it is supposed to be implemented
void pwm(int pin, int val) {
  static int ctr = 0;
  static int state = 0;

  if (ctr >= val && state == 1){
    PORTB &= ~(1u << pin);
    state = 0;
  } 

  if (ctr < val && state == 0) {
    PORTB |= (1u << pin);
    state = 1;
  }

  if (++ctr > 1023) ctr = 0;
}