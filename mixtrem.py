from raspiomix import Raspiomix
import RPi.GPIO as GPIO
import pygame
import time

r = Raspiomix()
FPS = 4
GPIO.setmode(GPIO.BOARD)

GPIO.setup(r.IO0, GPIO.IN)

if GPIO.input(r.IO0) == 0:
	pygame.init()
	clock = pygame.time.Clock()
	movie = pygame.movie.Movie('museomix.mpg')
	screen = pygame.display.set_mode(movie.get_size())
	movie_screen = pygame.Surface(movie.get_size()).convert()
	
	movie.set_display(movie_screen)
	movie.play()
	playing = False

while True:
	if not(movie.get_busy()) and r.readAdc(3) > 0.0338:
		movie.rewind()
		movie.play()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			movie.rewind()
			playing = False
	screen.blit(movie_screen,(0,0))
	pygame.display.update()
	clock.tick(FPS)

