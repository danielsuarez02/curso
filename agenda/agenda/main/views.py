from django.shortcuts import render
from django.views.generic import TemplateView,View
from .models import Producto

class Home(TemplateView):
	template_name="home.html"

class Productos(View):
	def get(self,request):
		productos = Producto.objects.all()
		return render(request,"productos.html",{'productos':productos})