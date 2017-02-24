from random import randint


class CreateRoom():

	playerSizes = 0

	def __init__(self, playerSize):
		self.playerSizes=playerSize
		self.RoomType=self.CreateType()

	def CreateType(self):
		value=randint(0,4)
		types = ["Spooky","Light","Dark","Dangerous","Calm"]
		return types[value]

	def ReturnPlayerSize(self):
		return self.playerSizes


	