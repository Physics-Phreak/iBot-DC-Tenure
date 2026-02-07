#include <Arduino.h>

const int detectPin = 2;
const int LEDPin = 13;

volatile int detected = 0;

void detectInterrupt() {
  detected = 1;
}

int main() {
  init();

  pinMode(2, INPUT);
  pinMode(13, OUTPUT);

  digitalWrite(LEDPin, 0);

  attachInterrupt(digitalPinToInterrupt(detectPin), detectInterrupt, RISING);

  while(1) {
    if (detected) {
      digitalWrite(LEDPin, 1);
      detected = 0;
      delay(2000);
      digitalWrite(LEDPin, 0);
    }
    delay(100);
  }
}