# importing required library
import pygame

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
imp = pygame.image.load("/home/pi/map-lcd.png").convert()

#screen_info = pygame.display.info()
#screen_size = (screen_info.current_w, screen_info.current_h)
screen_size = (X, Y)
image = pygame.transform.scale(imp, screen_size)

# Using blit to copy content from one surface to other
scrn.blit(image, (0, 0))

# paint screen one time
pygame.display.flip()
status = True
while (status):

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