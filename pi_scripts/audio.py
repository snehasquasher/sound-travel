import pygame
import sqlite3
# import RPi.GPIO as GPIO
import csv
# module for handling sound in a python program 

#Initializing pygame mixer module 
pygame.mixer.init() 

# audio file names 
with open('pi_scripts/file_names.txt', 'r') as f:
    lines = f.readlines()

# Strip any leading or trailing whitespace from each line
lines = [line.strip() for line in lines]

# Convert the list to a set TO DO 
my_set = set()
for line in lines: 
    my_set.add(int(line))

print(my_set)

#define audio files + associated locations on the world map 
#creating sound_directory  
with open('recordings.csv','r') as file: 
    reader = csv.reader(file)
    #skip the header row 
    next(reader)
    
    #create dict to store data 
    sound_directory = {}
    
    #traverse each row in the CSV file and add them to the dict 
    for row in reader: 
        key = row[6]
        values = [float(row[4]),float(row[5])]
        sound_id = int(row[0])
        if sound_id in my_set: 
            print(key)
            sound_directory[key] = values
        
print(len(sound_directory))
        
#set-up the potentiometers
# pot1_pin = 18
# pot2_pin = 23
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(pot1_pin, GPIO.IN)
# GPIO.setup(pot2_pin, GPIO.IN)

# function mapping potentiometer values to longitude and latitude
def map_potentiometer_values(pot1_value, pot2_value):
    # Map the potentiometer values to longitude and latitude
    longitude = pot1_value * 0.01 - 180.0
    latitude = pot2_value * 0.01 - 90.0
    # Return the mapped longitude and latitude
    return longitude, latitude

# function to find the nearest audio file based on longitude and latitude
def find_nearest_audio_file(longitude, latitude):
    # Find the nearest audio file based on the distance from each location on the world map
    nearest_location = None
    nearest_distance = float("inf")
    for name,location_data in sound_directory.items():
        #using the shortest distance formula --> hopefully this works 
        distance = ((location_data[0] - longitude) ** 2 + (location_data[1] - latitude) ** 2) ** 0.5
        if distance < nearest_distance:
            nearest_location = name
            nearest_distance = distance
    # Return the audio file corresponding to the nearest location
    return nearest_location

# Main loop
while True:
    # Read the potentiometer values
    # pot1_value = GPIO.input(pot1_pin)
    # pot2_value = GPIO.input(pot2_pin)
    # Map the potentiometer values to longitude and latitude
    longitude, latitude = map_potentiometer_values(1200000,400)
    # Find the nearest audio file based on longitude and latitude
    nearest_location = find_nearest_audio_file(longitude, latitude)
    # Load and play the audio file
    audio_file_name = "/Users/snehasivakumar/CodingProjects/SoundTravel/sound-travel/samples_earth_fm/" + nearest_location + ".mp3"
    print("nearest_location",nearest_location)
    pygame.mixer.init() 
    pygame.mixer.music.load(audio_file_name)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)



# ORIGINAL CODE 
# # Create the I2C bus
# i2c = busio.I2C(board.SCL, board.SDA)

# # Create the ADC object using the I2C bus
# ads = ADS.ADS1015(i2c)

# # Create single-ended input on channel 0
# chan = AnalogIn(ads, ADS.P0)
# # chan2 = AnalogIn(ads, ADS.P1)

# # Create differential input between channel 0 and 1
# #chan = AnalogIn(ads, ADS.P0, ADS.P1)

# # Test Print
# print("{:>5}\t{:>5}".format('raw', 'v'))
# #load the sound giles 
# pygame.mixer.music.load("pi_scripts/test.wav")
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy() == True:
#     continue


