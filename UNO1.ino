// C++ code
//
#include <Servo.h>
int servoPin2 = 2;
int servoPin3 = 3;
int servoPin4 = 4;
int Red = 8;
int Yellow = 9;
int Green = 10;
Servo servo_2;
Servo servo_3;
Servo servo_4;

void setup()
{
  pinMode(Green, OUTPUT);
  pinMode(Yellow, OUTPUT);
  pinMode(Red, OUTPUT);
  servo_2.attach(servoPin2, 500, 2500);
  servo_3.attach(servoPin3, 500, 2500);
  servo_4.attach(servoPin4, 500, 2500);
  
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available() > 0)
  {
    Serial.println("available");
    char userInput;
    userInput= Serial.read(); //serialString();

  
    if (userInput != '\0')
    {
      //Serial.println(userInput);
      if (userInput == '1')
      {
        servo_2.write(0);
        delay(1000); 
      }
      else if (userInput == '2')
      {
        servo_3.write(0);
        delay(1000); 
      }
      else if (userInput == '3')
      {
        servo_4.write(0);
        delay(1000); 
      }
      else if (userInput == 'r')
      {
        Serial.println("red led");
        digitalWrite(Red, HIGH);
        delay(500);
      }
      else if (userInput == 'g')
      {
        Serial.println("green led");
        digitalWrite(Green, HIGH);
        delay(500);
      }      
      else if (userInput == 'y')
      {
        Serial.println("yellow led");
        digitalWrite(Yellow, HIGH);
        delay(500);
      }
      else if (userInput == 'q')
      {
        Serial.println("no led");
        digitalWrite(Red, LOW);
        digitalWrite(Green, LOW);
        digitalWrite(Yellow, LOW);
        delay(500);
      }
      else if (userInput == 'm')
      {
        servo_2.write(90);
        servo_3.write(90);
        servo_4.write(90);
        delay(1000); // Wait for 1000 millisecond(s)
      }
  }

  }
}
