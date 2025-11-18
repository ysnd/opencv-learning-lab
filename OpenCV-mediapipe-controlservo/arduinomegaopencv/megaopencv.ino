#include <Servo.h>

Servo myServo;
int servoPin = 9;
int receivedValue;

void setup() {
    myServo.attach(servoPin);
    Serial.begin(9600);
}

void loop() {
    if (Serial.available() > 0) {
        receivedValue = Serial.read();
        if (receivedValue == '1') {
            myServo.write(0);  // Memutar servo ke 0 derajat
        } else if (receivedValue == '2') {
            myServo.write(90);  // Memutar servo ke 90 derajat
        }
    }
}
