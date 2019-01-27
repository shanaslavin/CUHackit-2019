from django.shortcuts import render
from django.views.generic import DetailView,TemplateView
from cuhackit.models import dispenser
from django.core import serializers
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect

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
        dispenser_r = dispenser.objects.get(pk = dispenser_id)
        dispenser_r.inventory -= 1
        dispenser_r.save()

    return HttpResponse("Success!")

class maintenance_view(TemplateView):
    model = dispenser
    template_name = 'maintenance.html'
    
def filled_view(request, dispenser_id):
    if(request.method == "POST"):
        dispenser_r = dispenser.objects.get(pk = dispenser_id)
        dispenser_r.inventory = dispenser_r.max_inventory
        dispenser_r.save()
        
    return redirect(reverse_lazy('maintain'))