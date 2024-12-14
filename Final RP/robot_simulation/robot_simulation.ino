#include <PS4Controller.h>
#include <BluetoothSerial.h>
#include <ESP32Servo.h>

// BluetoothSerial serialBt;
Servo gripperServo;

// define motors
#define RIGHT_MOTOR_FWD 14
#define LEFT_MOTOR_FWD 27
#define RIGHT_MOTOR_BWD 26
#define LEFT_MOTOR_BWD 25

// define (IR) sensor
#define SENSOR1 15
#define SENSOR2 2
#define SENSOR3 0

// PWM control pins for speed control of motors (enable pins)
#define PWM_RIGHT 12
#define PWM_LEFT 33

#define GRIPPER_PIN 15

bool mask1 = 0 ;
bool mask2 = 0 ;
bool mask3 = 0 ;
bool mask4 = 0 ;
bool mask5 = 0 ;
bool mask6 = 0 ;

bool gripperSwitch = 0;
void notify() {
  int yAxisValue = (PS4.data.analog.stick.ly);  //Left stick  - y axis - forward/backward car movement
  int xAxisValue = (PS4.data.analog.stick.rx);  //Right stick - x axis - left/right car movement
  if (PS4.Right() && mask1 == 0) {
    turnRight();
    // mask1 = 1 ; 
    // mask2 = 0 ;
  } else if (PS4.Left() && mask2 == 0) {
    turnLeft();
    // mask1 = 0 ;
    // mask2 = 1 ; 
  }

  if (PS4.Down() && mask3 == 0) {
    moveBackward();
    // mask3 = 1 ; 
    // mask4 = 0 ;
  } else if (PS4.Up() && mask4 == 0) {
    moveForward();
    // mask3 = 0 ;
    // mask4 = 1 ; 
  }
  if (PS4.R2() && mask5 == 0) {
    openGripper();
    // mask5 = 1 ;
    // mask6 = 0 ; 
  }
  else if (PS4.L2() && mask6 == 0) {
    closeGripper();
    // mask5 = 0 ;
    // mask6 = 1 ; 
  }
}

void onConnect() {
  Serial.println("Connected!.");
}

void onDisConnect() {
  Serial.println("Disconnected!.");
}

// Define robot states
enum RobotMode {
  AUTONOMOUS,
  MANUAL
};

// RobotMode currentMode = AUTONOMOUS;  // Start in autonomous mode

void setup() {
  Serial.begin(115200);
  // serialBt.begin("EL-Nokta"); // Initialize Bluetooth
  Serial.println("Robot ready!");
  PS4.begin("e8:d8:19:90:b9:a0");  //mac address for PS4 controller
  PS4.attach(notify);
  PS4.attachOnConnect(onConnect);
  PS4.attachOnDisconnect(onDisConnect);
  pinMode(RIGHT_MOTOR_FWD, OUTPUT);
  pinMode(LEFT_MOTOR_FWD, OUTPUT);
  pinMode(RIGHT_MOTOR_BWD, OUTPUT);
  pinMode(LEFT_MOTOR_BWD, OUTPUT);

  pinMode(SENSOR1, INPUT);
  pinMode(SENSOR2, INPUT);
  pinMode(SENSOR3, INPUT);

  pinMode(PWM_RIGHT, OUTPUT);
  pinMode(PWM_LEFT, OUTPUT);

  gripperServo.attach(GRIPPER_PIN);
  gripperServo.write(0);  // gripper position fixed
}

void loop() {
  // int value = digitalRead(SENSOR1);
  // Serial.println(value);
  // lineFollowing();
  // serialBt.println(value);
  // Check if in autonomous mode
  // if (currentMode == AUTONOMOUS) {
  //   lineFollowing();

  //   // Check for end of line or other condition to switch mode
  //    if (reachedEndOfLine() || timeToSwitchMode()) {

  //   //   currentMode = MANUAL;  // Switch to manual mode
  //   //   Serial.println("Switching to manual mode!");
  //    }
  // }

  // Check if in manual mode
  // if (currentMode == MANUAL) {
  //   manualControl();
  // }
}

void lineFollowing() {
  int s1 = digitalRead(SENSOR1);
  int s2 = digitalRead(SENSOR2);
  int s3 = digitalRead(SENSOR3);

  // Basic line-following logic based on sensor inputs
  if (s1 == LOW && s2 == HIGH && s3 == LOW) {
    moveForward();
  } else if (s1 == HIGH) {
    turnLeft();
  } else if (s3 == HIGH) {
    turnRight();
  } else {
    stopMotors();
  }
}
void moveForward() {
  Serial.println("Moving Forward");
  // Set motor speed using PWM (values between 0 and 255)
  analogWrite(PWM_RIGHT, 255);  // full speed
  analogWrite(PWM_LEFT, 255);  // full speed

  digitalWrite(RIGHT_MOTOR_FWD, HIGH);
  digitalWrite(LEFT_MOTOR_FWD, HIGH);
  digitalWrite(RIGHT_MOTOR_BWD, LOW);
  digitalWrite(LEFT_MOTOR_BWD, LOW);
}

void moveBackward() {
  Serial.println("Moving Backward");
  analogWrite(PWM_RIGHT, 255);  // full speed
   analogWrite(PWM_LEFT, 255);   // full speed

  digitalWrite(RIGHT_MOTOR_FWD, LOW);
  digitalWrite(LEFT_MOTOR_FWD, LOW);
  digitalWrite(RIGHT_MOTOR_BWD, HIGH);
  digitalWrite(LEFT_MOTOR_BWD, HIGH);
}

void turnLeft() {
  Serial.println("Turning Left");
  analogWrite(PWM_RIGHT, 255);  // full speed
  analogWrite(PWM_LEFT, 128);   // half speed for left motor

  digitalWrite(RIGHT_MOTOR_FWD, HIGH);
  digitalWrite(LEFT_MOTOR_FWD, LOW);
  digitalWrite(RIGHT_MOTOR_BWD, LOW);
  digitalWrite(LEFT_MOTOR_BWD, HIGH);
}

void turnRight() {
  Serial.println("Turning Right");
  analogWrite(PWM_RIGHT, 128);  // half speed for right motor
  analogWrite(PWM_LEFT, 255);   // full speed

  digitalWrite(RIGHT_MOTOR_FWD, LOW);
  digitalWrite(LEFT_MOTOR_FWD, HIGH);
  digitalWrite(RIGHT_MOTOR_BWD, HIGH);
  digitalWrite(LEFT_MOTOR_BWD, LOW);
}

void stopMotors() {
  analogWrite(PWM_RIGHT, 0);  // stop
  analogWrite(PWM_LEFT, 0);   // stop

  digitalWrite(RIGHT_MOTOR_FWD, LOW);
  digitalWrite(LEFT_MOTOR_FWD, LOW);
  digitalWrite(RIGHT_MOTOR_BWD, LOW);
  digitalWrite(LEFT_MOTOR_BWD, LOW);
}

void openGripper() {
  gripperServo.write(0);
  Serial.println("Opening Gripper");
}

void closeGripper() {
  Serial.println("Closing Gripper");
  gripperServo.write(90);
}
bool reachedEndOfLine() {
  //all sensors detect 3 black
  return (digitalRead(SENSOR1) == LOW && digitalRead(SENSOR2) == LOW && digitalRead(SENSOR3) == LOW);
}

bool timeToSwitchMode() {
  //switch after a set time, say 60 seconds
  static unsigned long startTime = millis();
  return (millis() - startTime > 60000);  // 60 seconds
}

void manualControl() {
  //   if (serialBt.available()) {
  //     char command = serialBt.read();
  //     Serial.print("Received command: ");
  //     Serial.println(command);

  //     switch (command) {
  //       case 'f': moveForward(); break;
  //       case 'b': moveBackward(); break;
  //       case 'l': turnLeft(); break;
  //       case 'r': turnRight(); break;
  //       case 's': stopMotors(); break;
  //       case 'o': openGripper(); break;
  //       case 'c': closeGripper(); break;
  //       default: Serial.println("Unknown command"); break;
  //     }
  //   }
  // }
}



