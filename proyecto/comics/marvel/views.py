from django.shortcuts import render
from django.views.generic import View
from .mv import Marvel
from .models import Heroe

class Home(View):
	def get(self,request):
		template_name='marvel/home.html'
		historial = Heroe.objects.all()

		context={
			'historial':historial
		}
		return render(request,template_name,context)

	def post(self,request):
		heroe=request.POST.get('heroe')
		
		heroes = request.POST.getlist('heroe')
		
		if len(heroes)>1:
			if len(heroes[0])>0:
				heroe=heroes[0]
			else:
				heroe=heroes[1]

		mv=Marvel()
		personaje=mv.get_personaje(heroe)

		print(heroe)
		historial = Heroe.objects.all()


		
		link=mv.get_imagen()

		if len(personaje)==0:
			personaje="Sin descripcion"

		if len(link)>0:
			if Heroe.objects.filter(nombre=heroe).count()==0:
				heroeModel=Heroe.objects.create(nombre=heroe,desc=personaje,img=link)
			#heroeModel.save()
	
		template_name='marvel/home.html'



		context={
			'personaje':personaje,
			'heroe':heroe,
			'link':link,
			'historial':historial
		}
		return render(request,template_name,context)

class Historial(View):
	def get(self, request):
		template_name='marvel/historial.html'
		
		historial = Heroe.objects.all()
		return render(request,template_name,{'historial':historial})
		
