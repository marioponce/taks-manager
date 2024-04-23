from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.views.decorators.csrf import csrf_exempt

from apps.scheduler.models import Person
from apps.scheduler.serializers import PersonSerializer

@api_view(["POST"])
def post_person(request):
    people = Person.objects.all()
    peopleSerializer = PersonSerializer(people, many = True)

    names = [person["name"] for person in peopleSerializer.data]

    if not request.data["name"] in names:
        personSerializer = PersonSerializer(data = request.data)
        if personSerializer.is_valid():
            personSerializer.save()

            return Response(status.HTTP_201_CREATED)
    else:
        return Response(status.HTTP_200_OK)