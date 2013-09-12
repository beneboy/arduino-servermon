int RED = 9;
int BLUE = 10;
int GREEN = 11;

void setup() {
  pinMode(RED, OUTPUT);
  pinMode(BLUE, OUTPUT);
  pinMode(GREEN, OUTPUT);
  analogWrite(RED, 0);
  analogWrite(GREEN, 0);
  analogWrite(BLUE, 0);
  Serial.begin(9600);
  Serial.write(1);
}

void loop(){
  int newRed = 0, newGreen=0, newBlue=0;

  if (Serial.available() >= 3) {

    newRed = Serial.read();
    newGreen = Serial.read();
    newBlue = Serial.read();

    Serial.print("RED: ");
    Serial.println(newRed, DEC);

    Serial.print("GREEN: ");
    Serial.println(newGreen, DEC);

    Serial.print("BLUE: ");
    Serial.println(newBlue, DEC);

    analogWrite(RED, newRed);
    analogWrite(GREEN, newGreen);
    analogWrite(BLUE, newBlue);
  }
}
