import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# importing required library
import pygame

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)
# chan2 = AnalogIn(ads, ADS.P1)

# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)

# Test Print
print("{:>5}\t{:>5}".format('raw', 'v'))


# activate the pygame library .
pygame.init()
X = 1920
Y = 1000

# create the display surface object
# of specific dimension..e(X, Y).
scrn = pygame.display.set_mode((X,Y))
# scrn = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
# set the pygame window name
pygame.display.set_caption('image')

# create a surface object, image is drawn on it.
#screen_info = pygame.display.info()
#screen_size = (screen_info.current_w, screen_info.current_h)

photos_dir = "/media/pi/UNTITLED/SoundTravel/kaleb/Photos/"
file_name = "map0.png"
imp = pygame.image.load(photos_dir + file_name).convert()
screen_size = (X, Y)
image = pygame.transform.scale(imp, screen_size)

# Using blit to copy content from one surface to other
scrn.blit(image, (0, 0))

image_number = 0
old_chan = 0.0

# paint screen one time
pygame.display.flip()
status = True
while (status):


    # Potentiometer variance
    if (chan.voltage - old_chan > .3) and image_number < 2:
        image_number+=1
    elif (chan.voltage - old_chan < .5)  and image_number > 0:
        image_number-=1

    old_chan = chan.voltage

    file_name = "map" + str(image_number) + ".png"
    imp = pygame.image.load(photos_dir + file_name).convert()
    screen_size = (X, Y)
    image = pygame.transform.scale(imp, screen_size)
    scrn.blit(image, (0, 0))

    pygame.display.flip()

    print("1: {:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
    print("**image_number: ", image_number)
    time.sleep(0.5)


    # print("2: {:>5}\t{:>5.3f}".format(chan2.value, chan2.voltage))
    # time.sleep(0.5)
  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
    for i in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.K_ESCAPE or i.type == pygame.QUIT:
            status = False
            pygame.quit()
            exit()
            #scrn = pygame.display.set_mode((100,100)

# deactivates the pygame library