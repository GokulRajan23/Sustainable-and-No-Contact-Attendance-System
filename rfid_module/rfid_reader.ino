#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 5    // SDA pin of RC522
#define RST_PIN 22  // RST pin of RC522

MFRC522 rfid(SS_PIN, RST_PIN);  // Create MFRC522 instance

void setup() {
  Serial.begin(115200);
  SPI.begin();       // Init SPI bus
  rfid.PCD_Init();   // Init MFRC522 module

  Serial.println("RFID Reader Initialized.");
}

void loop() {
  // Look for new cards
  if (!rfid.PICC_IsNewCardPresent() || !rfid.PICC_ReadCardSerial()) {
    delay(50);
    return;
  }

  // Read UID
  Serial.print("Card UID: ");
  for (byte i = 0; i < rfid.uid.size; i++) {
    Serial.print(rfid.uid.uidByte[i] < 0x10 ? " 0" : " ");
    Serial.print(rfid.uid.uidByte[i], HEX);
  }
  Serial.println();

  // Halt PICC (RFID tag)
  rfid.PICC_HaltA();
}
