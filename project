#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <OneWire.h>
#include <DallasTemperature.h>

// --- Pin Configs ---
#define ONE_WIRE_BUS 4     // DS18B20
#define PH_PIN 34          // pH Sensor (Analog)
#define TDS_PIN 35         // TDS Sensor (Analog)

// --- LCD Setup ---
LiquidCrystal_I2C lcd(0x27, 16, 2);  // I2C address, columns, rows

// --- Temperature Sensor Setup ---
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature tempSensor(&oneWire);

void setup() {
  Serial.begin(115200);         
  tempSensor.begin();           

  lcd.init();                   
  lcd.backlight();              

  // Welcome message
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Water Quality");
  lcd.setCursor(0, 1);
  lcd.print("Monitoring...");
  delay(2000);
}

void loop() {
  // Show reading message
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Reading sensors");
  lcd.setCursor(0, 1);
  lcd.print("Please wait...");
  delay(1000);

  // === Temperature ===
  tempSensor.requestTemperatures();
  float temperature = tempSensor.getTempCByIndex(0);

  // === pH Sensor ===
  int phRaw = analogRead(PH_PIN);
  float voltagePH = phRaw * (3.3 / 4095.0);
  float pHValue = 7 + ((2.5 - voltagePH) / 0.18);  // Adjust if needed

  // === TDS Sensor ===
  int tdsRaw = analogRead(TDS_PIN);
  float voltageTDS = tdsRaw * (3.3 / 4095.0);
  float tdsValue = (133.42 * voltageTDS * voltageTDS * voltageTDS
                   - 255.86 * voltageTDS * voltageTDS
                   + 857.39 * voltageTDS) * 0.5;

  // === Display on LCD ===
  lcd.clear();
  
  // Row 1: Temp and pH
  lcd.setCursor(0, 0);
  lcd.print("Temp:");
  lcd.print(temperature, 1);
  lcd.print((char)223); // Degree symbol
  lcd.print("C");

  lcd.setCursor(11, 0);
  lcd.print("pH:");
  lcd.print(pHValue, 1);

  // Row 2: TDS
  lcd.setCursor(0, 1);
  lcd.print("TDS:");
  lcd.print(tdsValue, 0);
  lcd.print(" ppm");

  // === Print to Serial Monitor ===
  Serial.print("Temp: "); Serial.print(temperature); Serial.print(" °C | ");
  Serial.print("pH: "); Serial.print(pHValue); Serial.print(" | ");
  Serial.print("TDS: "); Serial.print(tdsValue); Serial.println(" ppm");

  delay(4000);  // Update every 3 seconds
}
