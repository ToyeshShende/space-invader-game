import button
import pygame


#create display window
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Main menu')

#load button images
start_img = pygame.image.load('start_btn.png')
exit_img = pygame.image.load('exit_btn.png')

#create button instances
start_button = button.Button(100, 200, start_img, 0.8)
# start_button= button.Button(x, y, image, scale)
exit_button = button.Button(450, 200, exit_img, 0.8)

#game loop
run = True
while run:

	screen.fill((200, 200, 240))

	if start_button.draw(screen):
		print("start")
		import main
	if exit_button.draw(screen):
		print('EXIT')
		break

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()