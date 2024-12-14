

const int ledPin = 2;
const int button = 8;
int state = 0 ;
// int buttonState = 0;
void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(button, INPUT_PULLUP);
}

void loop() {
  // buttonState = digitalRead(buttonPin);

  // analogWrite(ledPin , 255);
  if ((digitalRead(button)== 0))
    digitalWrite(ledPin , LOW);
  else 
    digitalWrite (ledPin , HIGH);
  // if (buttonState == HIGH) {
  //   digitalWrite(ledPin, HIGH);
  // } else {
  //   digitalWrite(ledPin, LOW);
  // }
}




// int button = 0 ;

// void setup() {  // هتجهز شوية حاجات
//   pinMode(13, OUTPUT);
//   pinMode(2, INPUT);
//   //        pin_nom   state
// }

// void loop() {  // تكرار الكود
//   button = digitalRead(2);

//   Serial.print(button);
//   if(button){
//     digitalWrite(13,!digitalRead(13));
//   }

//   // digitalWrite(2,HIGH);
// }