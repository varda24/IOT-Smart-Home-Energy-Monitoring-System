// Smart Home Energy Monitoring System - ESP32 Code
// This code reads energy consumption data from sensors and transmits it

#include <WiFi.h>
#include <PubSubClient.h>

// WiFi credentials
const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";

// MQTT Broker
const char* mqtt_server = "YOUR_MQTT_BROKER";
const int mqtt_port = 1883;

WiFiClient espClient;
PubSubClient client(espClient);

// ADC pins for energy sensors
const int SENSOR_PIN_1 = 34;  // Analog input pin for sensor 1
const int SENSOR_PIN_2 = 35;  // Analog input pin for sensor 2

void setup() {
  Serial.begin(115200);
  delay(10);
  
  // Initialize ADC
  analogSetAttenuation(ADC_11db);
  
  // Connect to WiFi
  connectToWiFi();
  
  // Setup MQTT
  client.setServer(mqtt_server, mqtt_port);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  
  // Read sensor data
  int sensorValue1 = analogRead(SENSOR_PIN_1);
  int sensorValue2 = analogRead(SENSOR_PIN_2);
  
  // Convert to voltage and publish
  float voltage1 = (sensorValue1 / 4095.0) * 3.3;
  float voltage2 = (sensorValue2 / 4095.0) * 3.3;
  
  // Publish to MQTT topics
  char payload[50];
  sprintf(payload, "%.2f", voltage1);
  client.publish("energy/sensor1", payload);
  
  sprintf(payload, "%.2f", voltage2);
  client.publish("energy/sensor2", payload);
  
  delay(5000);  // Read every 5 seconds
}

void connectToWiFi() {
  Serial.print("Connecting to WiFi: ");
  Serial.println(ssid);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  
  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < 20) {
    delay(500);
    Serial.print(".");
    attempts++;
  }
  
  Serial.println();
  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("WiFi connected!");
    Serial.println(WiFi.localIP());
  } else {
    Serial.println("Failed to connect to WiFi");
  }
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    if (client.connect("ESP32Client")) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}
