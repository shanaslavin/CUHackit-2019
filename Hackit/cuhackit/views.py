from django.shortcuts import render
from django.views.generic import DetailView,TemplateView
from cuhackit.models import dispenser
from django.core import serializers
from django.http import HttpResponse
from django.conf import settings
import stripe
from cuhackit.consumers import DispenserConsumer
import channels.layers

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY

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

def order_pad(request, dispenser_id):
    if(request.method == "GET"):
        return render(request, 'order.html', {"dispenser_id": dispenser_id, "key": settings.STRIPE_PUBLISHABLE_KEY})
    elif(request.method == "POST"):
        charge = stripe.Charge.create(
            amount=50,
            currency='usd',
            description='Someone purchased a pad',
            source=request.POST['stripeToken']
        )
        channel_layer = channels.layers.get_channel_layer()
        from asgiref.sync import async_to_sync
        async_to_sync(channel_layer.send)('dispensers', {'dispensed': dispenser_id})
        return HttpResponse("Thank You for your purchase")
        