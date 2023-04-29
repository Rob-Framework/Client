// Motor A connections
int enA = 9;
int in1 = 2;
int in2 = 3;

// Motor B connections
int enB = 10;
int in3 = 4;
int in4 = 5;

String command;
String subCommand;

int speed = 55;
int speedIncrement = 10;
int minSpeed = 55;
int maxSpeed = 255;

void setup() {
  // Set all the motor control pins to outputs
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);

  // Turn off motors - Initial state
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);

  Stop();
  speed = minSpeed;

  Serial.begin(9600);
  Serial.println("<Arduino is ready>");
}

void loop() {
  /*MoveFront(); // Move forward
  delay(5000);
  Stop();
  delay(1000);
  MoveRear(); // Move backward
  delay(5000);
  Stop();
  delay(1000);
  MoveLeft(); // Move left
  delay(5000);
  Stop();
  delay(1000);
  MoveRight(); // Move right
  delay(5000);
  Stop();
  delay(1000);*/

  if (Serial.available()) {
    command = Serial.readStringUntil("\n");
  }


  if (command =="increase") {
    SetSpeed(true);
    return;
  } else if (command == "decrease"){
    SetSpeed(false);
    return;
  }

  if (subCommand == "forward" || subCommand == "backward") {
    if (command == "stop"){
        subCommand = "";
        command = "";
        Stop();
        return;
    }
    else if (command == "slow_stop") {
        subCommand = "";
        command = "";
        Break();
        delay(1000);
        Stop();
        return;
    }
    else {
      if (subCommand != "") {
      command = subCommand;
      }
    }
  }
  
    if (command == "forward") {
      if (subCommand != command) {
        speed = minSpeed;
      }
      subCommand = command;
      MoveFront();
    } else if (command == "backward") {
      if (subCommand != command) {
        speed = minSpeed;
      }
      subCommand = command;
      MoveRear();
    } else if (command == "stop") {
      subCommand = "";
      Stop();
    }else if (command == "break") {
      if (subCommand == "forward" || subCommand == "backward") {
      } else {
        subCommand = "";
      }
      subCommand = "";
      Break();
    }else if (command == "slow_stop") {
      subCommand = "";
      Break();
      delay(1000);
      Stop();
    }else if (command == "right") {
      if (subCommand == "forward" || subCommand == "backward") {
      } else {
        subCommand = "";
      }
      subCommand = "";
      MoveRight();
      delay(1000);
      Stop();
    }else if (command == "left") {
      if (subCommand == "forward" || subCommand == "backward") {
      } else {
        subCommand = "";
      }
      MoveLeft();
      delay(1000);
      Stop();
    }
  
  command = "";
}

void SetSpeed(bool increase) {
  if (increase) {
    speed = speed + speedIncrement;
  } else {
    speed = speed - speedIncrement;
  }

  if (speed < minSpeed) {
    speed = minSpeed;
  } else if (speed > maxSpeed) {
    speed = maxSpeed;
  }

    if (subCommand == "forward") {
      MoveFront();
    } else if (subCommand == "backward") {
      MoveRear();
    }
}

void MoveFront() {
  if (speed < minSpeed) {
    speed = minSpeed;
  } else if (speed > maxSpeed) {
    speed = maxSpeed;;
  }

  // Move forward
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(enA, speed);
  analogWrite(enB, speed);
}

void MoveRear() {
  if (speed < minSpeed) {
    speed = minSpeed;
  } else if (speed > maxSpeed) {
    speed = maxSpeed;
  }
  
  // Move backward
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, LOW);
  digitalWrite(in4, HIGH);
  analogWrite(enA, speed);
  analogWrite(enB, speed);
}

void MoveRight() {
  // Move left
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
  analogWrite(enA, 150);
  analogWrite(enB, 150);
}

void MoveLeft() {
  // Move right
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  analogWrite(enA, 150);
  analogWrite(enB, 150);
}

void Stop() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  analogWrite(enA, 0);
  analogWrite(enB, 0);
}

void Break() {
  digitalWrite(in1, HIGH);
  digitalWrite(in2, HIGH);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, HIGH);
  analogWrite(enA, 255);
  analogWrite(enB, 255);
  delay(500);
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
  analogWrite(enA, 0);
  analogWrite(enB, 0);
}
