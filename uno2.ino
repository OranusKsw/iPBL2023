#include <LiquidCrystal.h>

// Pin assignments
int red = 9;
int yellow = 8;
int green = 7;
int buzzer = 6;

// Pin input
int red_in = A2;
int yellow_in = A1;
int green_in = A0;

// LCD object
LiquidCrystal lcd(11, 10, 5, 4, 3, 2);

void setup()
{
  Serial.begin(9600);
  // Set pin input
  pinMode(red_in, INPUT);
  pinMode(yellow_in, INPUT);
  pinMode(green_in, INPUT);
  
  
  // Set pin modes
  pinMode(red, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(buzzer, OUTPUT);

  // Initialize LCD
  lcd.begin(16, 2);
  lcd.print("   Turning On   "); // Display initialization message
  lcd.setCursor(0, 1);
  lcd.print(" Trash Disposal");
  delay(2000); // Delay to show the message on the LCD
  lcd.clear(); // Clear the LCD screen
}

void loop()
{
  // Sequence 1: Wrong Disposal
  Serial.print("red pin = ");
  Serial.println(analogRead(red_in));
  Serial.print("yellow pin = ");
  Serial.println(analogRead(yellow_in));
  Serial.print("green pin = ");
  Serial.println(analogRead(green_in));
   
  if (analogRead(red_in) > 800)
  {
   lcd.setCursor(0, 0);
   lcd.print("Wrong Disposal ");
  digitalWrite(red, HIGH); // Turn on the red LED
    alarmWithSequenceTimer(5); // Start countdown for 5 seconds with alarm
    digitalWrite(red, LOW); // Turn off the red LED
    lcd.clear();
  }
  

  // Sequence 2: Image Processing
  else if (analogRead(yellow_in) > 800)
  {
    lcd.setCursor(0, 0);
  lcd.print("Image Processing");
    digitalWrite(yellow, HIGH); // Turn on the yellow LED
    sequenceTimer(5); // Start countdown for 5 seconds without alarm
    digitalWrite(yellow, LOW); // Turn off the yellow LED
    lcd.clear();
  }

  // Sequence 3: Success
  else if (analogRead(green_in) > 800)

  {
    lcd.setCursor(0, 0);
    lcd.print("Success !!!     ");
    digitalWrite(green, HIGH); // Turn on the green LED
    sequenceTimer(5); // Start countdown for 5 seconds without alarm
    digitalWrite(green, LOW); // Turn off the green LED
    lcd.clear();
  }
}

// Function to control alarm sound during countdown
void alarmWithSequenceTimer(int seconds)
{
  unsigned long startTime = millis();
  unsigned long elapsedTime = 0;
  bool buzzerOn = false;

  for (int i = seconds; i >= 0; i--)
  {
    lcd.setCursor(0, 1);
    lcd.print(i < 10 ? "0" : ""); // Pad single digit numbers with a leading zero
    lcd.print(i);

    if (i == seconds) // First second of the sequence
    {
      buzzerOn = true;
    }
    else if (i == 0) // Last second of the sequence
    {
      buzzerOn = false;
      noTone(buzzer); // Stop the alarm sound
    }

    if (buzzerOn)
    {
      if (i <= 5 && i > 0) // During the last 5 seconds of the sequence
      {
        tone(buzzer, 1000); // Start the alarm sound
        delay(500); // Delay for half a second (adjust as needed)
        noTone(buzzer); // Stop the alarm sound
        delay(500); // Delay for half a second (adjust as needed)
      }
    }

    delay(1000); // Delay for 1 second
  }
}

// Function for countdown timer without alarm
void sequenceTimer(int seconds)
{
  for (int i = seconds; i >= 0; i--)
  {
    lcd.setCursor(0, 1);
    lcd.print(i < 10 ? "0" : ""); // Pad single digit numbers with a leading zero
    lcd.print(i);
    delay(1000); // Delay for 1 second
  }
}
