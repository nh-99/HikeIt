from django.core.management.base import BaseCommand, CommandError
from trails.models import Trail

import os
import json

class Command(BaseCommand):
    help = "Populate the database with trails"

    def handle(self, *args, **options):
        for trailFile in os.listdir(os.getcwd() + "/trails/management/commands/trails/"):
            if ".json" in trailFile:
                f = open(os.getcwd() + "/trails/management/commands/trails/" + trailFile,"r")
                parsedSon = json.loads(f.read())
                
                for trail in parsedSon:
                    trailModel = Trail()
                    trailModel.name = trail['title']["#text"]
                    trailModel.lat = float(trail['lat']["#text"])
                    trailModel.long = float(trail['lon']["#text"])
                    trailModel.difficulty = trail['difficulty']["#text"]
                    trailModel.distance = round(float(trail['distance']["#text"]) * 0.000621371,2)
                    trailModel.location = trail['location']["#text"]
                    trailModel.approved = True
                    trailModel.save()

        self.stdout.write('The database has been populated.')
