#include <Arduino.h>
#include <DHT11.h>

const int readPin = 9;
DHT11 dht(readPin);

int temp, hum;

int main(){
  init();

  Serial.begin(9600);

  while(1){
    int result = dht.readTemperatureHumidity(temp, hum);

    Serial.print(temp);
    Serial.print(", ");
    Serial.println(hum);

    delay(1000);
  }
}