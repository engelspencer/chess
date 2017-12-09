import pygame, sys
from pygame.locals import *

#Frames per second
FPS = 60

#Global variables
WINDOWWIDTH = 800
WINDOWHEIGHT = 800

#Main function
def main():
	pygame.init()
	global DISPLAYSURF
	
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
	pygame.display.set_caption('Chess')
	
	#main game loop
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update()
		FPSCLOCK.tick(FPS)

if __name__ == '__main__':
	main()