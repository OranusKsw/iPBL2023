#For QR Code database
import pandas as pd
import sys

#For servo motor
from gpiozero import Servo
import time
from gpiozero.pins.pigpio import PiGPIOFactory

#import module for coding

data = {'Name': ['Mook', 'PP', 'Tatar'],
        'No': ['6422780583', '6422782894', '6422780294'],
        'Score': [10, 10, 10]} # data for testing

excel_file_path_old = 'C:/Users/COJ/PycharmProjects/trashinfo/info_data.xlsx' #locate path to variable
df = pd.read_excel(excel_file_path_old) #load database from excel turn into df
# board = pyfirmata.Arduino('COM3') #The code for raspi
recon_status = False #intialize status
open_the_door = False #intialize status
counter = 0 #intialize check time
PIN = 12 # servo pin TODO for testing only, delete after

while True: #Start checking
    input_data = str(input("Please scan your id ")) #Ask for input
    for index,row in df.iterrows(): #Select each row and column in dataframe for checking
         number=str(row['No']) # Locate the number that gonna check
         # print(number) variable check for testing
         if input_data == number:  #find the matching ID card
            selected_row=row #Locate the matching row
            recon_status = True #update the status
            open_the_door = True #update the status
            print("The door is opening") #indicate condition case to user
            print(f"You are "+selected_row['Name']) #indicate recognition data to user

            #triggering motor coding (This does to be done by connecting raspberrypi and servomotor)

            factory = PiGPIOFactory

            servo = Servo(PIN, pin_factory=factory, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

            print("Opening")
            servo.min()
            
            time.sleep(15)
            print("Closing")
            servo.max()
            print("Finished")


            #2nd draft

            # scan_trash = False
            #servo = AngularServo(10, initi6422780583
            #al_angle = 0)
            #try:
            # servo.angle = 90
            # time.sleep(15)
            # servo.angle = 0
            #finally:
            #  servo.detach()
            #if sensor.is_active: #senor locating inside trash to detect the presence of trash
            # break

            #1st draft

            # GPIO.setmode(GPIO.BCM)
            # pwm = GPIO.PWM(servo_pin, 50)
            # pwm.start(2.5)
            # pwm.ChangeDutyCycle(7.5)
            # time.sleep(15)
            # pwm.ChangeDutyCycle(2.5)
            sys.exit() #terminate all operation

         if not counter < max(df.index):
            print("Database doesn't have your info")
            add_name = str(input("Enter your name: "))
            add_No = str(input("Enter your No: "))
            new_data = pd.DataFrame({'Name': [add_name], 'No': [add_No], 'Score': [10]})
            df = pd.concat([df, new_data], ignore_index=True)
            # excel_file_path_new = 'C:/Users/COJ/PycharmProjects/trashinfo/info_data.xlsx'
            df.to_excel(excel_file_path_old, index=False)
            print(df)
            sys.exit()

         counter += 1








