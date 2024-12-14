#include "BluetoothSerial.h"

int led =2 ;
BluetoothSerial serialBt ;

void setup() {
  Serial.begin(9600);
  serialBt.begin("Tmam");
  Serial.println("The device started , now u can pair it");
  pinMode(led, OUTPUT);
}

void loop() {
  
  if(serialBt.available() ){
    char msg = serialBt.read();
    Serial.println("available");
    if(msg == '1'){
      
      digitalWrite(led , HIGH);
      Serial.println("ON");
    }
    else if(msg == '0'){
      digitalWrite(led , LOW);
      Serial.println("OFF");
    }
  }

}