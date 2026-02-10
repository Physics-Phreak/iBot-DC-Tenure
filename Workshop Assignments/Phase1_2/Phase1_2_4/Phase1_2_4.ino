#include <Arduino.h>
#include <Servo.h>

Servo servo;  
int pos = 0;

int main(){
  init();

  servo.attach(9);
  
  while(1){
    for (pos = 0; pos <= 180; pos += 1) {
      servo.write(pos);              
      delay(15);                       
    }
    for (pos = 180; pos >=  0; pos -= 1) { 
      servo.write(pos);              
      delay(15);                       
    }
  }
}