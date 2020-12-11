import pygame, sys, time

pygame.init()
# these are x, y coordinates that set the window size
windowSize = (800,600)

screen = pygame.display.set_mode(windowSize)
#declares windowSize as the size of the display/screen

myriadProFont = pygame.font.SysFont('myriadProFont',48)

helloWorldText = myriadProFont.render("hello world",1,(100,100,255),(255,255,255))
x,y = 0,0

while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()
  
  screen.blit(helloWorldText,(x,y))
  
  pygame.display.update()



