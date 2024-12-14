const int buttonPin = 34;
const int ledPin = 2;

int buttonState = 0;
void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
}

void loop() {  // تكرار الكود
  //buttonState = digitalRead(buttonPin);

  //  Serial.print(buttonState);
  //  if (buttonState) {
  //   digitalWrite(ledPin, !digitalRead(ledPin));
  //  }

  // digitalWrite(2,HIGH);
 int x = analogRead(buttonPin);
 analogWrite(ledPin, x/16);
}


// const int buttonPin = 2;
// // const int ledPin = 13;

// int buttonState = 0;
// void setup() {
//   pinMode(LED_BUILTIN, OUTPUT);
//   pinMode(buttonPin, INPUT);
// }

// void loop() {  // تكرار الكود
//   buttonState = digitalRead(buttonPin);
//   digitalWrite(LED_BUILTIN, HIGH);
//   delay(1000); // Wait for 1000 millisecond(s)
//   digitalWrite(LED_BUILTIN, LOW);
//   delay(1000); // Wait for 1000 millisecond(s)
//   Serial.print(buttonState);
//   // if (buttonState == HIGH) {
//   //   digitalWrite(LED_BUILTIN, HIGH);
//   // } else {
//   //   digitalWrite(LED_BUILTIN, LOW);
//   // }

//   // digitalWrite(2,HIGH);
// }




// // int button = 0 ;

// // void setup() {  // هتجهز شوية حاجات
// //   pinMode(13, OUTPUT);
// //   pinMode(2, INPUT);
// //   //        pin_nom   state
// // }

// // void loop() {  // تكرار الكود
// //   button = digitalRead(2);

// //   Serial.print(button);
// //   if(button){
// //     digitalWrite(13,!digitalRead(13));
// //   }

// //   // digitalWrite(2,HIGH);
// // }
// // void setup()
// // {
// //   pinMode(LED_BUILTIN, OUTPUT);
// // }

// // void loop()
// // {
// //   digitalWrite(LED_BUILTIN, HIGH);
// //   delay(1000); // Wait for 1000 millisecond(s)
// //   digitalWrite(LED_BUILTIN, LOW);
// //   delay(1000); // Wait for 1000 millisecond(s)
// // }

// // const int buttonPin = 2;
// // const int ledPin = 13;

// // int buttonState = 0;
// // void setup() {
// //   pinMode(ledPin, OUTPUT);
// //   pinMode(buttonPin, INPUT);
// // }

// // void loop() {
// //   // buttonState = digitalRead(buttonPin);
// //   // Serial.print(buttonState);

// //   // if(buttonState){
// //   //   digitalWrite(ledPin,!digitalRead(ledPin));

// //   // }
// //   digitalWrite(ledpin , HIGH);
// //   delay(1000);
// //   digitalWrite(ledpin , LOW);
// //   delay(1000);
// // }




// // // int button = 0 ;

// // // void setup() {  // هتجهز شوية حاجات
// // //   pinMode(13, OUTPUT);
// // //   pinMode(2, INPUT);
// // //   //        pin_nom   state
// // // }

// // // void loop() {  // تكرار الكود
// // //   button = digitalRead(2);

// // //   Serial.print(button);
// // //   if(button){
// // //     digitalWrite(13,!digitalRead(13));
// // //   }

// // //   // digitalWrite(2,HIGH);
// // // }