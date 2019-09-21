#include <Arduino.h>

const int threshold = 880;
const int txSpeed = 3000+8;

bool anchoring;
long timeAnchor;
int txIntervalPeakOffset = txSpeed*(1/3);
int value;

uint8_t message[200];
uint8_t messageIndex = 0;

bool sampled;
int16_t txZeros = 0;

void setup() {
  Serial.begin(2000000);

  /*for (int i = 0; i < 100; i++) {
    Serial.println(analogRead(0));
  }

  while(true) {
    int plotValue = analogRead(0);
    if (plotValue > 600) {
      Serial.println(plotValue);
    }
  }*/

  do {
    value = analogRead(0);
  } while (value < threshold);

  timeAnchor = micros();

  do {
    value = analogRead(0);
  } while (value > threshold);
}

void loop() {
  while (true) {
    if ((micros()-timeAnchor+txIntervalPeakOffset)%txSpeed < 50) {
      if (!sampled) {
        if (analogRead(0) > threshold) {
          //timeAnchor = micros();                                  TODO TODO
          message[messageIndex] = 1;
          txZeros = 0;
        } else {
          message[messageIndex] = 0;
          txZeros++;
          if (txZeros > 20) {
            break;
          }
          anchoring = true;
        }
        messageIndex++;
        sampled = true;
      }
    } else {
      sampled = false;
      if (anchoring && analogRead(0) > threshold) {
        timeAnchor = micros();
        anchoring = false;
      }
    }
  }

  for (uint8_t i = 0; i < 200; i++) {
    Serial.print(message[i]);
  }
  delay(100000000l);
}
