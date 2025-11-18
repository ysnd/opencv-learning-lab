#include <Servo.h>

Servo myServo;  // Servo instance

void setup() {
  Serial.begin(9600);
  myServo.attach(9);  // Sesuaikan pin servo
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');  // Baca data dari Python
    int thumbPos = data.toInt();  // Konversi menjadi integer
    int servoPos = map(thumbPos, 0, 100, 0, 180);  // Map posisi ke rentang servo (0-180)
    myServo.write(servoPos);  // Gerakkan servo
  }
}
