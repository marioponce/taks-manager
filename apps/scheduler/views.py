from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.template import loader

from .models import Person
from .forms import PersonForm

def people(request):
    """Renders the list of people in the database."""
    people = Person.objects.all()
    context = {"people": people}

    return render(request, "scheduler/people.html", context)

def add_person(request):
    """Calls the FarmerForm and adds a person instance to the db."""
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(people)
    else:
        form = PersonForm()

    context = {"form": form}
    return render(request, "scheduler/add_person.html", context)

def edit_person(request, person_id):
    """Calls the PersonForm and edits a specific person instance to the db."""
    person = Person.objects.get(id=person_id)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect(people)
    else:
        form = PersonForm(instance=person)

    context = {"form": form}
    return render(request, "scheduler/edit_person.html", context)

def delete_person(request, person_id):
    """Deletes a specific person instance from the db."""
    farmer = Person.objects.get(id=person_id)
    farmer.delete()
    return redirect(people)





