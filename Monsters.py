from JSONProcessing import ReadJSON
from random import randint

class Monster():


	def __init__(self):
		Monster_Dict = ReadJSON(1)

		self.Monster_Complete= Monster_Dict

		#Selects a Monster for the room randomly
		self.SelectedMonster = self.Monster_Complete["Monsters"][randint(0,self.GetNumMonsters() -1)]

	def GetNumMonsters(self):
		return len(self.Monster_Complete["Monsters"])

	#*********************************************************
	#*********************************************************
	#						GET METHODS
	#*********************************************************
	#*********************************************************

	def GetMonstName(self):
		return self.SelectedMonster['name']

	def GetMonstDifficulty(self):
		return self.SelectedMonster['difficulty']
		
	def GetMonstDescr(self):
		return self.SelectedMonster['description']

	def GetMonstHealth(self):
		return self.SelectedMonster['health']

	def GetMonstDefense(self):
		return self.SelectedMonster['defense']

	def GetMonstReward(self):
		return self.SelectedMonster['reward']	

	#*********************************************************
	#*********************************************************
	#					TESTING METHODS
	#*********************************************************
	#*********************************************************
	def PrintDict(self):
		print(self.Monster_Complete)

	def PrintSelectedMonster(self):
		print(self.SelectedMonster)


