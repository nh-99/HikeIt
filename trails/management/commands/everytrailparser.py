import json
import os

for trailFile in os.listdir(os.getcwd()):
	if ".json" in trailFile:
		f = open(trailFile,"r")
		parsedSon = json.loads(f.read())
		
		for trail in parsedSon:
			print round(float(trail['distance']["#text"]) * 0.000621371,2)
