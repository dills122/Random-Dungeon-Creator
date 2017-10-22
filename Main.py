from Create import CreateRoom
from random import randint

def mainArea():
	#Creates a single room 
	Crt =CreateRoom()

	Monster = Crt.GetMonster()

	print(Monster.GetMonstName())


#3 - 12 Players 
#*****ISSUE************
#Need to fix the and operator to get this to work plus implement elseif instead of ifs maybe
#*****ISSUE************s
def CalculateRoomSize(PlayerSize):
	value = 0
	if(PlayerSize == 3):
		value=randint(5,9)

	if(PlayerSize > 5 & PlayerSize < 9):
		value=randint(9,15)

	if(PlayerSize > 9 & PlayerSize < 12):
		value=randint(15, 30)

	return value


#Figure out how to implement a list or tuple
def CreateDungeon():
	Rooms = 
	#Get User input for the player size

	#Temp
	PlayerSize = 6

	RoomsVal = CalculateRoomSize(PlayerSize)

	for x in range(RoomsVal):
		RoomObj = CreateRoom()
		Rooms.__add__(RoomObj)

#mainArea()
CreateDungeon()
#print(CalculateRoomSize(6))