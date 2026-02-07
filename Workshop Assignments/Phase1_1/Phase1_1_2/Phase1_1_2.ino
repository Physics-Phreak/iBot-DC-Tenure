#include <Arduino.h>

int main() {
  init();
  Serial.begin(9600);

  pinMode(A1, INPUT);

  uint16_t val = 0;

  while(1){
    val = analogRead(A1);
    Serial.println(val);

    delay(200);
  }
}