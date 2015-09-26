from django.core import serializers
from django.http import HttpResponse
from collections import Counter
import json

from people.models import Person

def person(request):
	#serialized_data = serializers.serialize("json", Person.objects.all())
	#context = {'data': serialized_data}
	k = []
	people = Person.objects.all()
	
	for x in range(0, len(people)):
		k.append(people[x].car_make)

	c = dict(Counter(k))

	return HttpResponse(json.dumps(c))