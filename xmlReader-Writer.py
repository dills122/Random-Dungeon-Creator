import json


def ReadJSON():
	f=open("F://Python Projects//Tabletop-Creator//Monster.json", "r")

	s=f.read()

	#print(s)

	Monster = json.loads(s)

	print(Monster["Monsters"][0]["health"])

ReadJSON();
