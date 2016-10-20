from django.shortcuts import render,HttpResponse
from django.views.generic import View

class Hola(View):
	def get(self,request):
		return HttpResponse("Llegaste a la vista ")