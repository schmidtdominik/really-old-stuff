#include <Arduino.h>

bool on = false;
int32_t time;
const int32_t syncSteps = 100*2;
const int32_t txSpeed = 3000l;
int32_t realSpeed = 0;

uint8_t seq[] = {1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1};

void setup() {
  Serial.begin(2000000);
  pinMode(3, OUTPUT);
}

void loop() {
  for (int16_t i = 0; i < syncSteps; i++) {
    time = micros();
    while (micros()-time < txSpeed) {
      ;
    }

    if (on) {
      digitalWrite(3, LOW);
    } else {
      digitalWrite(3, HIGH);
    }
    on = !on;
  }
  for (int16_t i = 0; i < sizeof(seq)/sizeof(uint8_t); i++) {
    time = micros();
    while (micros()-time < txSpeed) {
      ;
    }

    if (seq[i] == 1) {
      digitalWrite(3, HIGH);
    } else {
      digitalWrite(3, LOW);
    }
  }

  digitalWrite(3, LOW);
  delay(1000000l);
}
