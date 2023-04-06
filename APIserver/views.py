from django.shortcuts import render,redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Roundinfo
import json
from django.forms.models import model_to_dict
from django.http import JsonResponse

# Create your views here.
def index(request):
	return render(request, "index.html")


@csrf_exempt
def create(request):

	if request.method == "GET":
		return render(request, "index.html")

	elif request.method =="POST":
		roundNumber = request.POST['roundNumber']
		url = '/contents/'+str(roundNumber)
		return redirect(url)

@csrf_exempt
def viewContents(request,id):

	print(type(id))
	findRound = int(id)

	#data = Roundinfo.objects.all()

	round_info = Roundinfo.objects.get(id=findRound)
	round_info_dict = model_to_dict(round_info)

	return JsonResponse(round_info_dict)
