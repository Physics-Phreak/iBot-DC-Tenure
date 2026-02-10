#include <Arduino.h>

const int buzzerPin = 10;

int main(){
  init();

  pinMode(buzzerPin, OUTPUT);

  while(1){
    tone(buzzerPin, 1000);
    delay(1000);
    noTone(buzzerPin);
    delay(1000);
  }
}