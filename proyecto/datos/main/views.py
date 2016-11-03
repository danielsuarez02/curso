from django.shortcuts import render
from django.views.generic import View
from .models import Cine,Pelicula

class Home(View):
	def get(self,request):
		cines = Cine.objects.all()



		context={
			'cines':cines,
		}
		return render(request,'main/home.html',context)

	def post(self,request):

		cine=request.POST.get('cineForm')

		cines = Cine.objects.all()

		context={
			'cine':cine,
			'cines':cines,
		}

		if len(cine)>0:
			cineObj=Cine.objects.get(id=cine)
			if cineObj is not None:
				peliculas=Pelicula.objects.filter(cines=cineObj)
				context['peliculas']=peliculas

		
		return render(request,'main/home.html',context)