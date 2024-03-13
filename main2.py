import pygame
from pygame import Vector2
from parcle import ParticleEmitter
from globals import FPS, SCREEN_SIZE
from boss import Boss
from player import Player
pygame.init()

doExit = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_SIZE))

testParticleEmitter = ParticleEmitter(
	pos = Vector2(SCREEN_SIZE)//2,
	# celeste :)
	# updateAttributes = [["colorOverDistance", [250, [(91, 206, 250), (91, 206, 250), (0, 0, 0), (245, 169, 184), (245, 169, 184), (0, 0, 0), (255, 255, 255), (255, 255, 255), (0, 0, 0), (245, 169, 184), (245, 169, 184), (0, 0, 0), (91, 206, 250), (91, 206, 250), (12, 12, 12)]]]],
	# initAttributes = [["randAngle"], ["moveOnAngle", 20]],
	# fire
	# updateAttributes = [["colorOverLife", [(0, 0, 0), (100, 20, 200), (255, 75, 20), (255, 100, 50), (255, 125, 50), (255, 200, 75)]], ["randVelo", 2], ["gravity", -.025], ["randYVelo", [0, 1]]],
	# initAttributes = [["randAngle", [265, 275]], ["moveOnAngle", 20]],
	# fire fade
	# updateAttributes = [["drag"], ["gravity", .02], ["colorOverVelo", [10, "dom", [(0, 0, 0), (100, 20, 200), (255, 75, 20), (255, 100, 50), (255, 125, 50), (255, 200, 75)]]]],
	# initAttributes = [["randAngle"], ["moveOnAngle", 20]],
	# pink fade
	# updateAttributes = [["drag"], ["gravity", .02], ["colorOverVelo", [10, "dom", [(0, 0, 0), (100, 50, 50), (220, 100, 100), (220, 125, 125), (250, 150, 150), (0, 0, 0)]]]],
 	# initAttributes = [["randAngle"], ["moveOnAngle", 20]],
	#temp test
	# updateAttributes = [["gravity"], ["sizeOverVelo", [10, "avg", [10, 1]]], ["randAdjustColor", [5, [(0, 0, 0), (150, 150, 150)]]], ["deleteOnColor", (255, 0, 0)]],
	#im shitsing
	# initAttributes= [["gravity", 4],["randSize",[1,2]]],
	# updateAttributes= [["randXVelo", 24],["randAdjustSize",[0,2]],["colorOverVelo",[10, "dom",[(216, 190, 73),(115, 76, 53)]]]],
	maxParticles = 100000,
	ppf = 8,
	particleLifetime = 400,
	size = 10,
	)

boss = Boss(Vector2(400, 400))

tempColor = (25, 15, 532)
if tempColor[0] == 25:
	adjustTuple = (-25, 0, 0)

tempColor = tuple(map(lambda i, j: i + j, tempColor, adjustTuple))
print(tempColor)

guy = Player(1)
while not doExit:
	delta = clock.tick(FPS) / 1000
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			doExit = True #lets you quit parogram
	screen.fill((0, 0, 0))

	testParticleEmitter.update(screen, delta, pos = pygame.mouse.get_pos(), velo = -Vector2(pygame.mouse.get_rel())/7.5)

	boss.update(screen, guy.centerpos)
	guy.update(delta,screen)
	pygame.display.flip()
pygame.quit()