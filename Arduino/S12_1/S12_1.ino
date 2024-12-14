//for esp
#include <HardwareSerial.h>

HardwareSerial mySerial(1);

const int potPin = 34;
const int ledPin = 25;
int potValue = 0;

void setup() {
  Serial.begin(115200);
  mySerial.begin(9600);

  pinMode(ledPin, OUTPUT);
}

void loop() {
  potValue = analogRead(potPin);
  int mappedValue = map(potValue, 0, 4095, 0, 255);

  mySerial.write(mappedValue);

  if (mySerial.available()) {
    int receivedValue = mySerial.read();
    analogWrite(ledPin, receivedValue);
  }

  delay(100);  // Small delay for stability
}


// #include <SoftwareSerial.h>

// //#include <SoftwareSerial.h>


// const int led = 5 ;
// const int potn = A0 ;

// const int rxpin1 = 0 ;
// const int txpin1 = 1 ;

// const int rxpin2 = 10 ;
// const int txpin2 = 11 ;

// SoftwareSerial Serial1(rxpin1, txpin1);
// SoftwareSerial Serial2(rxpin2, txpin2);

// int val1 ;
// int data [2];

// int val2[4];

// void binary(int value) {
//   int out = value/4;
//   if (out%2==0) {
//     digitalWrite (led ,LOW);
//   }
//   else {
//     digitalWrite (led,HIGH);
//     out /= 2;
//   }
// }


// void setup() {
//   Serial.begin(115200);
//   Serial1.begin(115200);
//   Serial2.begin(115200);

//   pinMode(led, OUTPUT);
//   pinMode(rxpin1, INPUT);
//   pinMode(txpin1, OUTPUT);
//   pinMode(rxpin2, INPUT);
//   pinMode(txpin2, OUTPUT);

// }

// void loop() {




//   if (Serial.available()>1) {
//     val2[0]=Serial2.read();
//     val2[1]=Serial2.read();
//     val2[2] = val2[1]<<8 | val2[0];
//     binary(val2[2]);

//     Serial.print(val2[1],HEX);
//     Serial.print(val2[0],HEX);
//     Serial.println(val2[2],HEX);
//   }


//   val1 = analogRead(potn);
//   data[0] = val1 & 0xFF;
//   data[1] = (val1 >> 8);

//   Serial.print(data[0], HEX);
//   Serial.print(" ");
//   Serial.println(data[1], HEX);

//   Serial1.write(data[0]);
//   Serial1.write(data[1]);
// }
// #include <SoftwareSerial.h>


// const int led = 5;
// const int potn = A0;

// const int rxpin = 0;
// const int txpin = 1;

// SoftwareSerial mySerial(rxpin, txpin);


// int val1;
// int data[2];

// int val2[4];

// void binary(int value) {
//   int out = value / 4;
//   if (out % 2 == 0) {
//     digitalWrite(led, LOW);
//   } else {
//     digitalWrite(led, HIGH);
//     out /= 2;
//   }
// }


// void setup() {
//   Serial.begin(115200);
//   mySerial.begin(115200);

//   pinMode(led, OUTPUT);
//   pinMode(rxpin, INPUT);
//   pinMode(txpin, OUTPUT);
// }

// void loop() {




//   if (Serial.available() > 1) {
//     val2[0] = mySerial.read();
//     val2[1] = mySerial.read();
//     val2[2] = val2[1] << 8 | val2[0];
//     binary(val2[2]);

//     Serial.print(val2[1], HEX);
//     Serial.print(val2[0], HEX);
//     Serial.println(val2[2], HEX);
//   }


//   val1 = analogRead(potn);
//   data[0] = val1 & 0xFF;
//   data[1] = (val1 >> 8);

//   Serial.print(data[0], HEX);
//   Serial.print(" ");
//   Serial.println(data[1], HEX);

//   mySerial.write(data[0]);
//   mySerial.write(data[1]);
// }

// #include <SoftwareSerial.h>


// const int led = 5;
// const int potn = A0;

// const int rxpin = 0;
// const int txpin = 1;

// SoftwareSerial mySerial(rxpin, txpin);


// int val1;
// int data[2];

// int val2[4];

// void binary(int value) {
//   int out = value / 4;
//   if (out % 2 == 0) {
//     digitalWrite(led, LOW);
//   } else {
//     digitalWrite(led, HIGH);
//     out /= 2;
//   }
// }


// void setup() {
//   Serial.begin(115200);
//   mySerial.begin(115200);

//   pinMode(led, OUTPUT);
//   pinMode(rxpin, INPUT);
//   pinMode(txpin, OUTPUT);
// }

// void loop() {




//   if (Serial.available() > 1) {
//     val2[0] = mySerial.read();
//     val2[1] = mySerial.read();
//     val2[2] = val2[1] << 8 | val2[0];
//     binary(val2[2]);

//     Serial.print(val2[1], HEX);
//     Serial.print(val2[0], HEX);
//     Serial.println(val2[2], HEX);
//   }


//   val1 = analogRead(potn);
//   data[0] = val1 & 0xFF;
//   data[1] = (val1 >> 8);

//   Serial.print(data[0], HEX);
//   Serial.print(" ");
//   Serial.println(data[1], HEX);

//   mySerial.write(data[0]);
//   mySerial.write(data[1]);
// }
// // #include <SoftwareSerial.h>

// // const int led = 5 ;
// // const int potn = A0 ;

// // const int rxpin = 10 ;
// // const int txpin = 11 ;


// // SoftwareSerial mySerial =  SoftwareSerial(rxpin, txpin);

// // int val[4];

// // void binary(int dec) {
// //   int bval = dec/4;                                      // convert dec value to binary, scale to 8 bits

// //   if (bval%2==0) {
// //     digitalWrite (led ,LOW);
// //   }          // set LEDs accordingly
// //   else {
// //     digitalWrite (led,HIGH);
// //     bval=bval/2;
// //   }
// // }

// // void setup() {
// //   Serial.begin(115200);
// //   mySerial.begin(115200);
// //   pinMode(led, OUTPUT);

// // }

// // void loop() {

// //   int msgT = map(analogRead(potn), 0, 1023, 0, 255 );
// //   Serial.println(msgT);
// //   if (mySerial.available() > 1) {
// //     val[0] = mySerial.read();       // least significant 8 bits
// //     val[1] = mySerial.read();       // most significant 2 bits
// //     val[2] = val[1] << 8 | val[0];  // reassebled 10 bit value, sore in val[2]
// //     binary(val[2]);                 // convert to binary and display on LEDs

// //     Serial.print(val[1], HEX); Serial.print(" ");
// //     Serial.print(val[0], HEX); Serial.print(" ");
// //     Serial.println(val[2], HEX);
// //   }
// //   //if (50 < msgT ) {
// //   // Serial.write('1');
// //   // Serial.println('1');
// //   // }
// //   //else if (50 > msgT) {
// //   //  Serial.write('0');
// //   //  Serial.println('0');

// //   //if (Serial.available()) {
// //   // int  msgR = Serial.read();
// //   // Serial.println(msgR);
// //   // analogWrite(led, msgR);
// //   //if (msgR == '1') {
// //   //   digitalWrite(led, 1);
// //   //Serial.println(1);
// //   //}
// //   //else if (msgR == '0') {
// //   //   digitalWrite(led, 0);
// //   // Serial.println(0);
// //   // }
// //   //}

// //   delay(10);

// // }



// // // int but = 13;
// // // int state;
// // // int led = 2;
// // // void setup() {
// // //   pinMode(but, INPUT_PULLDOWN);
// // //   Serial.begin(115200);
// // //   Serial.println("sab7 elfol");
// // // }

// // // void loop() {
// // //   state = digitalRead(but);
// // //   if (state == 1) {
// // //     Serial.write('1');
// // //   } else if (state == 0) {
// // //     Serial.write('0');
// // //   }
// // //   delay(100);
// // // }



// // // #include <SoftwareSerial.h>

// // // const int led = 5 ;
// // // const int potn = A0 ;

// // // const int rxpin = 9 ;
// // // const int txpin = 10 ;

// // // SoftwareSerial mySerial(rxpin, txpin);


// // // int value ;
// // // int data [2];

// // // void setup() {
// // //   Serial.begin(115200);
// // //   mySerial.begin(115200);
// // //   pinMode(led, OUTPUT);

// // //   pinMode(rxpin, INPUT);
// // //   pinMode(txpin, OUTPUT);

// // // }

// // // void loop() {

// // //  // int msgT = map(analogRead(potn), 0, 1023, 0, 255 );
// // //  // Serial.println(msgT);
// // //   data[0] = val & 0xFF;
// // //   data[1] = (val >> 8);

// // //   Serial.print(data[0], HEX);
// // //   Serial.print(" ");
// // //   Serial.println(data[1], HEX);

// // //   mySerial.write(data[0]);
// // //   mySerial.write(data[1]);

// // //   //if (50 < msgT ) {
// // //   // Serial.write('1');
// // //   // Serial.println('1');
// // //   // }
// // //   //else if (50 > msgT) {
// // //   //  Serial.write('0');
// // //   //  Serial.println('0');

// // // //if (Serial.available()) {
// // //  // int  msgR = Serial.read();
// // //  // Serial.println(msgR);
// // //   //analogWrite(led, msgR);
// // //   //if (msgR == '1') {
// // //   //   digitalWrite(led, 1);
// // //   //Serial.println(1);
// // //   //}
// // //   //else if (msgR == '0') {
// // //   //   digitalWrite(led, 0);
// // //   // Serial.println(0);
// // //   // }
// // // 	//}

// // //   delay(10);
// // // }