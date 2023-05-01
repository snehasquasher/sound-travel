import pygame
import sqlite3
# import RPi.GPIO as GPIO
import csv
# module for handling sound in a python program 

#Initializing pygame mixer module 
pygame.mixer.init() 

# audio file names dictionary mapping 
with open('pi_scripts/audio_id_file_name.csv','r') as file: 
    reader = csv.reader(file)
    #skip the header row 
    next(reader)
    
    #create dict to store data 
    audio_ids = {}
    
    #traverse each row in the CSV file and add them to the dict 
    for row in reader: 
       
        audio_id = int(row[0])
        file_name = row[1]
        audio_ids[audio_id] = file_name


# define audio files + associated locations on the world map 
# creating sound_directory  
with open('recordings.csv','r') as file: 
    reader = csv.reader(file)
    #skip the header row 
    next(reader)
    
    #create dict to store data 
    sound_directory = {}
    
    #traverse each row in the CSV file and add them to the dict 
    for row in reader: 
        region = row[6]
        location = row[7]
        sound_id = row[16]
        values = [float(row[4]),float(row[5]),region,location] #latitude,longitude,location
        if sound_id != '' and int(sound_id) in audio_ids: 
            file_name = audio_ids[int(sound_id)]
            sound_directory[file_name] = values
        
    #write to a csv file 
    for key,value in sound_directory.items(): 
        print(key,value)
        
    with open('output.csv','w',newline = '') as file: 
        writer = csv.writer(file)
        writer.writerow(zip(sound_directory.keys(),sound_directory.values()))
        
#set-up the potentiometers
# pot1_pin = 18
# pot2_pin = 23
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(pot1_pin, GPIO.IN)
# GPIO.setup(pot2_pin, GPIO.IN)

# function mapping potentiometer values to longitude and latitude
def map_potentiometer_values(pot1_value, pot2_value):
    # Map the potentiometer values to longitude and latitude
    # longitude = pot1_value * 0.01 - 180.0
    # latitude = pot2_value * 0.01 - 90.0
    x_axis = map_range(pot1_value,-16,26512,0,800)
    y_axis = map_range(pot2_value,-16,26512,0,600)
    # Return the mapped longitude and latitude
    return x_axis,y_axis

# function to find the nearest audio file based on x_axis and y_axis
def find_nearest_audio_file(x_axis, y_axis):
    # Find the nearest audio file based on the distance from each location on the world map
    nearest_location = None
    nearest_distance = float("inf")
    for file_name,location_data in sound_directory.items():
        #using the shortest distance formula --> hopefully this works 
        distance = ((location_data[4] - x_axis) ** 2 + (location_data[5] - y_axis) ** 2) ** 0.5
        if distance < nearest_distance:
            nearest_location_file_name = file_name
            nearest_location = location_data[3:5]
            nearest_distance = distance
    # Return the audio file corresponding to the nearest location
    print(nearest_location)
    return nearest_location_file_name

#function to map the range of values 
def map_range(value, from_low, from_high, to_low, to_high):
    """
    Map a value from one range to another range.
    
    Parameters:
        value (float): The value to be mapped.
        from_low (float): The lower bound of the input range.
        from_high (float): The upper bound of the input range.
        to_low (float): The lower bound of the output range.
        to_high (float): The upper bound of the output range.
    
    Returns:
        float: The mapped value.
    """
    from_range = from_high - from_low
    to_range = to_high - to_low
    scaled_value = (float(value - from_low) / float(from_range))
    return to_low + (scaled_value * to_range)

while True:
    # Read the potentiometer values
    # pot1_value = GPIO.input(pot1_pin)
    # pot2_value = GPIO.input(pot2_pin)
    # Map the potentiometer values to longitude and latitude
    #longitude, latitude = map_potentiometer_values(27,133)
    # Find the nearest audio file based on longitude and latitude
    nearest_location = find_nearest_audio_file(28.3949, 84.124)
    # Load and play the audio file
    
    cursor_y = sound_directory[nearest_location][4]
    cursor_x = sound_directory[nearest_location][5]
    print(sound_directory[nearest_location])
    print("x:",cursor_x, "y:",cursor_y)
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


