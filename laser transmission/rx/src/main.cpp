#include <Arduino.h>

int32_t lastOn;
int32_t txSpeed;
bool alreadySetup;
bool printed;
bool txStarted;
int16_t txZeros = 0;
int threshold = 910;

const int syncSteps = 50;

bool startedPlotting = false;

void setup() {
  Serial.begin(2000000);
}

void loop() {
  for (int i = 0; i < 100; i++) {
    Serial.println(analogRead(0));
  }

  while(true) {
    int plotValue = analogRead(0);
    if (plotValue > 600) {
      Serial.println(plotValue);
    }
  }
  // setup
  if (!alreadySetup) {
    uint16_t value = 0;
    uint16_t counts = 0;
    bool stillOn = false;

    Serial.println("Syncing...");
    while (counts < syncSteps) {
      value = analogRead(0);
      if (!txStarted) {
        do {
          value = analogRead(0);
        } while (value < threshold);
        txStarted = true;
      }

      if (value > threshold && !stillOn) {
       int32_t nextLastOn = micros();
       txSpeed = (txSpeed+(nextLastOn-lastOn))/2;
       lastOn = nextLastOn;
       counts++;
       stillOn = true;
       //Serial.print("Step"); Serial.print(counts); Serial.print("/"); Serial.println(syncSteps);
       //Serial.println(txSpeed);
     } else if (value < threshold) {
       stillOn = false;
     }

    }
    alreadySetup = true;
    txSpeed /= 2;
    Serial.println("reading transmission");
  }


  int32_t currentTime = (micros()-lastOn+txSpeed/2)%txSpeed;
  if (currentTime < 100 && txZeros < 30) {
    if (!printed) {
      //Serial.println("ON NOW");
      if (analogRead(0) > threshold) {
        Serial.print(1);
        txZeros = 0;
      } else {
        Serial.print(0);
        txZeros++;
      }
      printed = true;
    }
  } else {
    printed = false;
  }
}
