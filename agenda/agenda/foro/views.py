from django.shortcuts import render
from django.views.generic import TemplateView,View
from .models import Post
from .forms import PostForm

class Foro(TemplateView):
	template_name="foro.html"

class Posts(View):
	def get(self,request):
		posts = Post.objects.all()

		form=PostForm()
		context={'posts':posts,'form':form}
		return render(request,"posts.html",context)

class Form(View):
	def post(self,request):
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
		context={'form':form}
		return render(request,"form.html",context)

	def get(self,request):
		form=PostForm()
		context={'form':form}
		return render(request,"form.html",context)

class Listado(View):
	def get(self,request):
		return render(request,"blog.html")
