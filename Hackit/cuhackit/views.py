from django.shortcuts import render
from django.views.generic import DetailView,TemplateView
from cuhackit.models import dispenser
from django.core import serializers
from django.http import HttpResponse

# Create your views here.

def dispenser_view_single(request, dispenser_id):
    dispensers = dispenser.objects.filter(pk = dispenser_id)
    data = serializers.serialize("json", dispensers)
    response = HttpResponse(data)
    return response

def dispenser_view(request):
    if(request.method == "GET"):
        dispensers = dispenser.objects.all()
        data = serializers.serialize("json", dispensers)
        response = HttpResponse(data)
        return response
    elif(request.method == "POST"):
        return HttpResponse()
    else:
        return HttpResponse()

class map(TemplateView):
    model = dispenser
    template_name = 'map.html'

def dispensed_view(request, dispenser_id):
    if(request.method == "GET"):
        inventory = dispenser.objects.filter(inventory = dispenser_id)
        print("Please print this ", inventory)
        return HttpResponse()

        