#include <Arduino.h>

volatile int detected = 0;
volatile int newState = 0;

void detectInterrupt() {
  detected = digitalRead(2);
  newState = 1;
}

int main() {
  init();

  pinMode(2, INPUT);

  attachInterrupt(digitalPinToInterrupt(2), detectInterrupt, CHANGE);

  Serial.begin(9600);

  while(1) {
    if (newState) {
      if (detected) Serial.println("Object Detected");
      if (!detected) Serial.println("No Object in view");
      newState = 0;
    }
    delay(100);
  }
}