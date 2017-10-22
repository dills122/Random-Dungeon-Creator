from random import randint
from Monsters import Monster


class CreateRoom():

	playerSizes = 0

	def __init__(self):
		#Sets the Player Size
		##self.playerSizes=playerSize
		#Sets the Room Type
		self.RoomType=self.CreateType()
		#Creates the Monster object for the room
		self.MonsterObj()

	def CreateType(self):
		value=randint(0,4)
		types = ["Spooky","Light","Dark","Dangerous","Calm"]
		return types[value]

	#def ReturnPlayerSize(self):
		#return self.playerSizes

	def MonsterObj(self):
		self.Monster = Monster()
		self.MonsterName = self.Monster.GetMonstName()
		self.MonsterDiff = self.Monster.GetMonstDifficulty()
		self.MonsterDescr = self.Monster.GetMonstDescr()
		self.MonsterHealth = self.Monster.GetMonstHealth()
		self.MonsterDefense = self.Monster.GetMonstDefense()
		self.MonsterReward = self.Monster.GetMonstReward()
	
	def GetMonster(self):
		return self.Monster	





	