#include <BluetoothSerial.h>
#include <ESP32Servo.h>

BluetoothSerial serialBt;
Servo gripperServo;  //gripper servo object

//Motor pin definitions
#define RIGHT_MOTOR 14
#define LEFT_MOTOR 27
#define RIGHT_MOTOR_REV 26
#define LEFT_MOTOR_REV 25

//enable pins
#define PWM_RIGHT 12
#define PWM_LEFT 33


#define GRIPPER_PIN 2

void setup() {
  Serial.begin(115200);
  serialBt.begin("Tmam");
  Serial.println("Welcome! The car and gripper are ready. Pair your Bluetooth device :)");

  //motor control pins=outputs
  pinMode(RIGHT_MOTOR, OUTPUT);
  pinMode(LEFT_MOTOR, OUTPUT);
  pinMode(RIGHT_MOTOR_REV, OUTPUT);
  pinMode(LEFT_MOTOR_REV, OUTPUT);

  //PWM control pins=outputs
  pinMode(PWM_RIGHT, OUTPUT);
  pinMode(PWM_LEFT, OUTPUT);

  //gripper servo
  gripperServo.attach(GRIPPER_PIN);
  gripperServo.write(0);  //open position
}

void loop() {
  //speed of motors
  analogWrite(PWM_RIGHT, 75);  //right motor
  analogWrite(PWM_LEFT, 75);   //left motor

  if (serialBt.available()) {
    char state = serialBt.read();
    // sensor1state = digitalRead(sensor1);
    Serial.println("available");

    if (state == 'f') {
      moveForward();
    } else if (state == 'b') {
      moveBackward();
    } else if (state == 'r') {
      turnRight();
    } else if (state == 'l') {
      turnLeft();
    } else if (state == 'o') {
      openGripper();
    } else if (state == 'c') {
      closeGripper();
    }
  }
}


void moveForward() {
  Serial.println("Moving Forward");
  serialBt.println("Moving Forward");
  digitalWrite(RIGHT_MOTOR, HIGH);
  digitalWrite(LEFT_MOTOR, HIGH);
  digitalWrite(RIGHT_MOTOR_REV, LOW);
  digitalWrite(LEFT_MOTOR_REV, LOW);
}


void moveBackward() {
  Serial.println("Moving Backward");
  serialBt.println("Moving Backward");
  digitalWrite(RIGHT_MOTOR, LOW);
  digitalWrite(LEFT_MOTOR, LOW);
  digitalWrite(RIGHT_MOTOR_REV, HIGH);
  digitalWrite(LEFT_MOTOR_REV, HIGH);
}


void turnRight() {
  Serial.println("Turning Right");
  serialBt.println("Turning Right");
  digitalWrite(RIGHT_MOTOR, HIGH);
  digitalWrite(LEFT_MOTOR, LOW);
  digitalWrite(RIGHT_MOTOR_REV, LOW);
  digitalWrite(LEFT_MOTOR_REV, HIGH);
}


void turnLeft() {
  Serial.println("Turning Left");
  serialBt.println("Turning Left");
  digitalWrite(RIGHT_MOTOR, LOW);
  digitalWrite(LEFT_MOTOR, HIGH);
  digitalWrite(RIGHT_MOTOR_REV, HIGH);
  digitalWrite(LEFT_MOTOR_REV, LOW);
}


void stop() {
  Serial.println("Stopping");
  serialBt.println("Stopping");
  digitalWrite(RIGHT_MOTOR, LOW);
  digitalWrite(LEFT_MOTOR, LOW);
  digitalWrite(RIGHT_MOTOR_REV, LOW);
  digitalWrite(LEFT_MOTOR_REV, LOW);
}


void openGripper() {
  Serial.println("Opening Gripper");
  serialBt.println("Opening Gripper");
  gripperServo.write(0);  // Set the servo angle to 0 to open the gripper
}

// Function to close the gripper
void closeGripper() {
  Serial.println("Closing Gripper");
  serialBt.println("Closing Gripper");
  gripperServo.write(90);  // Set the servo angle to 90 to close the gripper
}
