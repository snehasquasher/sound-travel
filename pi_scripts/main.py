import pygame
import sqlite3
# import RPi.GPIO as GPIO
import csv
# module for handling sound in a python program 
import time
# import board
# import busio
# import sys 
# import adafruit_ads1x15.ads1115 as ADS 
# from adafruit_ads1x15.analog_in import AnalogIn
import serial
from datetime import datetime


# ser = serial.Serial(
#         port='/dev/ttyUSB0',
#         baudrate = 115200,
#         parity=serial.PARITY_NONE,
#         stopbits=serial.STOPBITS_ONE,
#         bytesize=serial.EIGHTBITS,
#         timeout=1
#         )



#sound set-up 

# # Create the I2C bus
# i2c = busio.I2C(board.SCL, board.SDA)

# # Create the ADC object using the I2C bus
# ads = ADS.ADS1115(i2c)

# # Create single-ended input on channel 0
# chan0 = AnalogIn(ads, ADS.P0)
# chan1 = AnalogIn(ads, ADS.P1)

# # Create differential input between channel 0 and 1
# chan = AnalogIn(ads, ADS.P0, ADS.P1)


#Initializing pygame mixer module 
pygame.mixer.init() 

# audio file names dictionary mapping 
with open('audio_id_file_name.csv','r') as file: 
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
with open('fileNames_coordinates.csv','r') as file: 
    reader = csv.reader(file)
    #skip the header row 
    next(reader)
    
    #create dict to store data 
    sound_directory = {}
    
    #traverse each row in the CSV file and add them to the dict 
    for row in reader: 
        file_name = row[0]
        region = row[3]
        location = row[4]
        x_coordinate = int(row[5])
        y_coordinate = int(row[6])
        values = [region,location,x_coordinate,y_coordinate] #latitude,longitude,location
        sound_directory[file_name] = values
        
# function mapping potentiometer values to longitude and latitude
def map_potentiometer_values(pot1_value, pot2_value):
    # Map the potentiometer values to longitude and latitude
    # longitude = pot1_value * 0.01 - 180.0
    # latitude = pot2_value * 0.01 - 90.0
    x_axis = map_range(pot1_value,-2,26413,0,800)
    y_axis = map_range(pot2_value,-2,26413,0,600)
    # Return the mapped longitude and latitude
    return x_axis,y_axis

# function to find the nearest audio file based on x_axis and y_axis
def find_nearest_audio_file(x_axis, y_axis):
    # Find the nearest audio file based on the distance from each location on the world map
    nearest_location = None
    nearest_distance = float("inf")
    for file_name,location_data in sound_directory.items():
        #using the shortest distance formula --> hopefully this works 
        distance = ((location_data[2] - x_axis) ** 2 + (location_data[3] - y_axis) ** 2) ** 0.5
        if distance < nearest_distance:
            #breakpoint()
            nearest_location_file_name = file_name
            nearest_location = location_data[0:2]
            nearest_distance = distance
    # Return the audio file corresponding to the nearest location
    #print(nearest_location)
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

#Test serial write
#ser.write(b'#0(141,321)*')
#time.sleep(5)
last_location = ''
pygame.mixer.init() 
pygame.mixer.music.set_volume(0.5)
while True:
    # Read the potentiometer values
    
    #time.sleep(0.5)
    #print("2: {:>5}\t{:>5.3f}".format(, chan1.voltage))
    #time.sleep(0.5)
    
    # pot_1 = chan0.value 
    # pot_2 = chan1.value
    # print("POT: {:>5}\t{:>5.3f}".format(pot_1, pot_2))
    # Map the potentiometer values to longitude and latitude
    x_axis, y_axis = map_potentiometer_values(200,100)
    # Find the nearest audio file based on longitude and latitude
    nearest_location = find_nearest_audio_file(x_axis, y_axis)
    
    # Load and play the audio file
    cursor_y = sound_directory[nearest_location][3]
    cursor_x = sound_directory[nearest_location][2]
    
    
    #show_cursor(x, y)

    #print(sound_directory[nearest_location])
    #print("x:",cursor_x, "y:",cursor_y)
    audio_file_name = "samples_earth_fm/" + nearest_location
    #breakpoint()
    if(nearest_location != last_location):
        print("nearest_location",nearest_location)
        """
        x = int(cursor_x)
        y = int(cursor_y)
        serial_string = f'#0({x},{y})*'
        byte_str = serial_string.encode('utf-8')
        ser.write(byte_str)
        print("X,Y: {:>5}\t{:>5}".format(x, y))
        time.sleep(2)
        """
        try: 
            pygame.mixer.music.load(audio_file_name)
        except pygame.error as e:
            print("file is not found") 
        else:    
            pygame.mixer.music.play()
        
    else:
        pass
        
    x = int(x_axis)
    y = int(y_axis)
    # print("X,Y: {:>5}\t{:>5}".format(x, y))
    # serial_string = f'#0({x},{y})*'
    # byte_str = serial_string.encode('utf-8')
    
    # start_sec = datetime.now().second
    # ser.write(byte_str)
    # print("WRITING")
    time.sleep(2)
    #"""
    start = time.time()
    while(time.time() - start < 0.025):
        diff = time.time() - start
        #diff = start_sec - datetime.now().second
        #print(diff)
        """
    """
        #time.sleep(2)
    
    last_location = nearest_location
    #while( abs(pot_1 - chan0.value) < 5 or abs(pot_2 - chan1.value) < 5):
        #pass
    
    #def show_cursor(x , y):
       
    
    #while pygame.mixer.music.get_busy():
        #pygame.time.Clock().tick(10)
  


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
