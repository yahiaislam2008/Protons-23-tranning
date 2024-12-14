
#define RIGHT_MOTOR_FWD 19
#define LEFT_MOTOR_FWD 12
#define RIGHT_MOTOR_BWD 18
#define LEFT_MOTOR_BWD 14

#define SENSOR1 15
#define SENSOR2 27
#define SENSOR3 26



//PID PROPERTIES
const double KP = 0.072;
const double KD = 0.0;
const double KI = 0.0;

double lasterror = 0;
const int goal = 0;  // (right + left sensors) / 2
float error = 0,
      P = 0,
      I = 0,
      D = 0,
      PID_value = 0;
float previous_error = 0,
      previous_I = 0;

int speed = 255;
void setup() {
  Serial.begin(115200);

  pinMode(RIGHT_MOTOR_FWD, OUTPUT);
  pinMode(LEFT_MOTOR_FWD, OUTPUT);
  pinMode(RIGHT_MOTOR_BWD, OUTPUT);
  pinMode(LEFT_MOTOR_BWD, OUTPUT);

  pinMode(SENSOR1, INPUT);
  pinMode(SENSOR2, INPUT);
  pinMode(SENSOR3, INPUT);
}

void loop() {
  Calibrate();

}

void Calibrate() {
  sensor[1] = digitalRead(A1);
  sensor[2] = digitalRead(A2);
  sensor[3] = digitalRead(A3);

  else if ((sensor[1] == 0) && (sensor[2] == 0) && (sensor[3] == 1))
    error = 3;
  else if ((sensor[1] == 0) && (sensor[2] == 0) && (sensor[3] == 1))
    error = 2;
  else if ((sensor[1] == 0) && (sensor[2] == 1) && (sensor[3] == 1))
    error = 1;
  else if ((sensor[1] == 0) && (sensor[2] == 1) && (sensor[3] == 0))
    error = 0;
  else if ((sensor[1] == 1) && (sensor[2] == 1) && (sensor[3] == 0))
    error = -1;
  else if ((sensor[1] == 1) && (sensor[2] == 0) && (sensor[3] == 0))
    error = -2;
  else if ((sensor[1] == 1) && (sensor[2] == 0) && (sensor[3] == 0))
    error = -3;
}

void calculate_pid() {
  P = error;
  I = I + previous_I;
  D = error - previous_error;

  PID_value = (Kp * P) + (Ki * I) + (Kd * D);

  previous_I = I;
  previous_error = error;
}