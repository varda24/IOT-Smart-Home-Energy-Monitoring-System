#include <Arduino.h>

#define POT_PIN 34

#define GREEN_LED 27
#define RED_LED 14
#define BUZZER 26

float voltage = 230.0;
float energy = 0.0;
float tariff = 8.0;

unsigned long previousMillis;

void setup() {

  Serial.begin(115200);

  pinMode(GREEN_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  pinMode(BUZZER, OUTPUT);

  previousMillis = millis();

  Serial.println("SMART HOME ENERGY MONITOR");
}

void loop() {

  int raw = analogRead(POT_PIN);

  float current = (raw / 4095.0) * 10.0;

  float power = voltage * current;

  unsigned long currentMillis = millis();

  float hours =
      (currentMillis - previousMillis)
      / 3600000.0;

  energy += (power / 1000.0) * hours;

  previousMillis = currentMillis;

  float cost = energy * tariff;

  if(power > 1500){

    digitalWrite(RED_LED,HIGH);
    digitalWrite(GREEN_LED,LOW);
    digitalWrite(BUZZER,HIGH);

  } else {

    digitalWrite(RED_LED,LOW);
    digitalWrite(GREEN_LED,HIGH);
    digitalWrite(BUZZER,LOW);
  }

  Serial.println("----------------");

  Serial.print("Voltage: ");
  Serial.println(voltage);

  Serial.print("Current: ");
  Serial.println(current);

  Serial.print("Power: ");
  Serial.println(power);

  Serial.print("Energy: ");
  Serial.println(energy);

  Serial.print("Cost: ");
  Serial.println(cost);

  delay(1000);
}