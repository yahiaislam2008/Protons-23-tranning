#include <BluetoothSerial.h>


BluetoothSerial serialBt;

//for sensor

// void read(bool state){
//    if (state == 1) {
//     serialBt.println("white");
//   } else {
//     serialBt.println("Black");
//   }
// }
#define Rmotor1 19
#define Lmotor2 12
#define h_Rmotor1 18
#define h_Lmotor2 14
#define sensor1 15
#define enb1 4
#define enb2 16

bool sensor1state;

void setup() {
  Serial.begin(115200);
  serialBt.begin("Tmam");
  Serial.println("The device started , now u can pair it");

  pinMode(Rmotor1, OUTPUT);
  pinMode(Lmotor2, OUTPUT);
  pinMode(h_Rmotor1, OUTPUT);
  pinMode(h_Lmotor2, OUTPUT);
  pinMode(sensor1, INPUT);
  pinMode(enb1, OUTPUT);
  pinMode(enb2, OUTPUT);
}
void loop() {
  analogWrite(enb1, 75);
  analogWrite(enb2, 100);
  // read(sensor1state);

  if (serialBt.available()) {
    char state = serialBt.read();
    // sensor1state = digitalRead(sensor1);
    Serial.println("available");

    if (state == 'f') {

      digitalWrite(Rmotor1, HIGH);
      digitalWrite(Lmotor2, HIGH);
      digitalWrite(h_Rmotor1, LOW);
      digitalWrite(h_Lmotor2, LOW);
      Serial.println('f');
      serialBt.println('f');
    } else if (state == 'b') {
      digitalWrite(Rmotor1, LOW);

      digitalWrite(Lmotor2, LOW);
      digitalWrite(h_Rmotor1, HIGH);
      digitalWrite(h_Lmotor2, HIGH);
      Serial.println('b');
      serialBt.println('b');
    } else if (state == 'r') {
      digitalWrite(Rmotor1, HIGH);
      digitalWrite(Lmotor2, LOW);
      digitalWrite(h_Rmotor1, LOW);
      digitalWrite(h_Lmotor2, HIGH);
    } else if (state == 'l') {
      digitalWrite(Rmotor1, LOW);
      digitalWrite(Lmotor2, HIGH);
      digitalWrite(h_Rmotor1, HIGH);
      digitalWrite(h_Lmotor2, LOW);
    } else if (state == 's') {
      digitalWrite(Rmotor1, LOW);
      digitalWrite(Lmotor2, LOW);
      digitalWrite(h_Rmotor1, LOW);
      digitalWrite(h_Lmotor2, LOW);
    }
  }
}