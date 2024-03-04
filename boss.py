import pygame
import random
from pygame import Vector2

class Boss:
	def __init__(self, pos: Vector2 = Vector2(0, 0)):
		self.pos = pos
		self.velo = Vector2(0, 0)
		self.speed = 2
		self.hp = 100
		self.stateList = ["idle", "follow"]
		self.currentState = self.stateList[1]
		self.ticker = 0

	def draw(self, screen):
		height = 100
		width = 45
		pygame.draw.rect(screen, (255, 255, 255), (self.pos.x - width/2, self.pos.y - height/2, width, height))
		
	def handleState(self, playerPos):
		stateDict = {"idle":self.idle, "follow":self.follow}

		stateDict[self.currentState](playerPos)

	def idle(self):
		pass

	def follow(self, playerPos:Vector2):
		if playerPos!=self.pos:
			self.velo = (playerPos-self.pos).normalize() * self.speed

	def move(self):
		self.pos += self.velo

	def update(self, screen, playerPos):
		self.handleState(playerPos)
		self.move()
		self.draw(screen)