import json
import os

Monster_Path = "~/Documents/Python/Random-Dungeon-Creator/Monster.json"




def ReadJSON(Type):
	#Checks to see which Path to use for reading JSON
	if Type == 1:
		FilePath = Monster_Path

	#Opens the JSON File
	f=open(os.path.expanduser(FilePath), "r")

	#Reads into a String
	s=f.read()

	#Converts into a Dictonary
	JSON_Dict = json.loads(s)

	return JSON_Dict
