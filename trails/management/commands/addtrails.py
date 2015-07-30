from django.core.management.base import BaseCommand, CommandError
from trails.models import Trail

class Command(BaseCommand):
  help = "Populate the database with seed trails"

  def handle(self, *args, **options):
    f = open('/home/noah/result.csv', 'r')
    for line in f:
      line =  line.split(';')
      trail = Trail()
      trail.name = line[0]
      trail.lat = float(line[1])
      trail.long = float(line[2])
      trail.difficulty = line[3]
      trail.distance = float(line[4].replace(' miles', ''))
      trail.location = line[5]
      trail.save()

    f.close()
    self.stdout.write('Database populated successfuly! :)')
