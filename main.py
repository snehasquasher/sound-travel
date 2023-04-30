import time
import sqlite3
# import RPi.GPIO as GPIO
from PIL import Image, ImageDraw

#connect to databse 
conn = sqlite3.connect("sound_files.db") 
#create cursor object 
cur = conn.cursor()
#create a new database named sound_files 
cur.execute("CREATE DATABASE my_database;")
with open('audiofiles.sql', 'r') as script_file:
    script = script_file.read()
    
cur.executescript(script)

#commit the changes 
conn.commit()

conn.close()

# # Set up the potentiometer
# pot_pin = 17
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(pot_pin, GPIO.IN)

# # Set up the LCD
# lcd = Adafruit_CharLCD(rs=26, en=19, d4=13, d5=6, d6=5, d7=11, cols=16, lines=2)

# # Load the images
# image1 = Image.open('image1.jpg')
# image2 = Image.open('image2.jpg')
# image3 = Image.open('image3.jpg')

# # Create an array of the images
# images = [image1, image2, image3]

# # Set the current image to the first image
# current_image = 0

# while True:
#     # Read the potentiometer value
#     pot_value = GPIO.input(pot_pin)
    
#     # Calculate the index of the image to display
#     index = int(pot_value / 1024 * len(images))
    
#     # Check if the index has changed
#     if index != current_image:
#         # Update the current image
#         current_image = index
        
#         # Display the new image on the LCD
#         lcd.clear()
#         lcd.message('Image {}'.format(current_image + 1))
#         images[current_image].show()
        
#     # Wait for a short time
#     time.sleep(0.1)