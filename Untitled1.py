#import module for coding

#For QR Code database
import pandas as pd
import sys

#For servo motor
from gpiozero import Servo
import time
from gpiozero.pins.pigpio import PiGPIOFactory


#database

excel_file_path_old = '/home/oranus/iPBL2023/info_data.xlsx' #locate path to variable
df = pd.read_excel(excel_file_path_old) #load database from excel turn into df

recon_status = False #intialize status
open_the_door = False #intialize status
counter = 0 #intialize check time

while True: #Start checking
    input_data = str(input("Please scan your id ")) #Ask for input

    for index,row in df.iterrows(): #Select each row and column in dataframe for checking
         number=str(row['No']) # Locate the number that gonna check

         if input_data == number:  #find the matching ID card
            selected_row=row #Locate the matching row
            recon_status = True #update the status
            open_the_door = True #update the status
            print("The door is opening") #indicate condition case to user
            print(f"You are "+selected_row['Name']) #indicate recognition data to user

            #triggering motor coding (This does to be done by connecting raspberrypi and servomotor)

            factory = PiGPIOFactory()

            servo = Servo(12, min_pulse_width=0.5/1000, max_pulse_width=1.5/1000, pin_factory=factory)
            print("Opening")
            servo.min()
            time.sleep(15)

            #todo recieve the signal from the camera to close the gate

            print("Closing")
            servo.max()
            time.sleep(5)

            sys.exit() #terminate all operation

         if not counter < max(df.index):
            print("Database doesn't have your info")
            add_name = str(input("Enter your name: "))
            add_No = str(input("Enter your No: "))
            new_data = pd.DataFrame({'Name': [add_name], 'No': [add_No], 'Score': [10]})
            df = pd.concat([df, new_data], ignore_index=True)
            df.to_excel(excel_file_path_old, index=False)
            print(df)
            sys.exit()

         counter += 1