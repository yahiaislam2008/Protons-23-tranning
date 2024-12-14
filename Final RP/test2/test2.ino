#define RIGHT_MOTOR 14
#define LEFT_MOTOR 27
#define RIGHT_MOTOR_REV 26
#define LEFT_MOTOR_REV 25

#define PWM_RIGHT 12
#define PWM_LEFT 33




void setup() {
  Serial.begin(115200);

  pinMode(RIGHT_MOTOR, OUTPUT);
  pinMode(LEFT_MOTOR, OUTPUT);
  pinMode(RIGHT_MOTOR_REV, OUTPUT);
  pinMode(LEFT_MOTOR_REV, OUTPUT);

  //PWM control pins=outputs
  pinMode(PWM_RIGHT, OUTPUT);
  pinMode(PWM_LEFT, OUTPUT);
}

void loop() {
  analogWrite(PWM_RIGHT, 75);  //right motor
  analogWrite(PWM_LEFT, 75);   //left motor
  moveForward();
}

void moveForward() {
  Serial.println("Moving Forward");
  digitalWrite(RIGHT_MOTOR, HIGH);
  digitalWrite(LEFT_MOTOR, HIGH);
  digitalWrite(RIGHT_MOTOR_REV, LOW);
  digitalWrite(LEFT_MOTOR_REV, LOW);
}
