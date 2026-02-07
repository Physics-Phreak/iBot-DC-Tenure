#include <Arduino.h>

int val = 0;

int main(){
  init();

  Serial.begin(9600);

  while(1){
    val = analogRead(A1);
    Serial.println(val);

    delay(5);
  }
}
