#include <Arduino.h>

const int trigPin = 10;
const int echoPin = 2;

const float soundSpeed = 343.0; //mps

uint64_t duration;
float distance;

int main() {
  init();
  Serial.begin(9600);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  while(1) {
  
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    duration = pulseIn(echoPin, HIGH);
    distance = (float)duration * soundSpeed / 2000.0; //distance in milimeters

    Serial.println(distance);
    delay(100);
  }
}