#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <DHT.h>

#define SCREEN_WIDTH 128  // OLED display width, in pixels
#define SCREEN_HEIGHT 64  // OLED display height, in pixels

#define OLED_RESET -1  // Reset pin
#define SCREEN_ADDRESS 0x3C

#define SENSOR_DATA_PIN 14

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
DHT dht(SENSOR_DATA_PIN, DHT22);

void setup() {
  pinMode(SENSOR_DATA_PIN, INPUT_PULLUP);

  Serial.begin(115200);
  dht.begin();

  // initialize the OLED object
  if (!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for (;;)
      ;  // Don't proceed, loop forever
  }  
}

void loop() {
  float humi  = dht.readHumidity();
  float tempC = dht.readTemperature();

  if ( isnan(tempC) || isnan(humi)) {
    Serial.println("Failed to read from DHT22 sensor!");
  } else {
    display.clearDisplay();
    
    display.setTextSize(1);
    display.setTextColor(WHITE);
    
    display.setCursor(0, 0);
    display.println("Humidity =");
    display.setCursor(64, 0);
    display.println(humi);

    display.setCursor(0, 32);
    display.println("Temperature =");
    display.setCursor(82, 32);
    display.println(tempC);
    display.display();
  }
  delay(100);
}
