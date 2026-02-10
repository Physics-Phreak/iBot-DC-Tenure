#include <Arduino.h>
#include <LiquidCrystal.h>

#define RS_PIN 7
#define RW_PIN 8
#define ENABLE_PIN 9

#define D4_PIN 5
#define D5_PIN 4
#define D6_PIN 3
#define D7_PIN 2


int main(){
  init();

  LiquidCrystal lcd(RS_PIN, RW_PIN, ENABLE_PIN,
                      D4_PIN, D5_PIN, D6_PIN, D7_PIN);

  lcd.begin(16, 2);
  lcd.print("Hello World");

  lcd.setCursor(2, 1);
  lcd.print("iBot Club");

  while(1){
    
  }
}