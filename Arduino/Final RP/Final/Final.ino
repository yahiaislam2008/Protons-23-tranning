#include <PS4Controller.h>


void notify(){
  

}


void onConnect()
{
  Serial.println("Connected!.");
}

void onDisConnect()
{
  Serial.println("Disconnected!.");
}

void setup() {
  Serial.begin(115200);
  PS4.begin("e8:d8:19:90:b9:a0");   //mac address for PS4 controller
  PS4.attach(notify);
  PS4.attachOnConnect(onConnect);
  PS4.attachOnDisconnect(onDisConnect);
  Serial.println("Ready.");
}

void loop() {

  
}