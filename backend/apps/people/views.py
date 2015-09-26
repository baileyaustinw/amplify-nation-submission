from django.core import serializers
from django.http import HttpResponse
from collections import Counter
import json

from people.models import Person

# View that returns data in JSON format
def person(request):
	k = []
	# Grab all Person objects
	people = Person.objects.all()
	
	# Add the car makes to an empty array
	# Will contain duplicates
	for x in range(0, len(people)):
		k.append(people[x].car_make)

	# Use a Counter to show how many time each car make occurs
	# The occurrences represent how many People objects have this car_make
	c = dict(Counter(k))

	# Return the Counter Dictionary as a JSON object
	return HttpResponse(json.dumps(c))