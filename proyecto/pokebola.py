class Pokemon(object):
	def __init__(self,nombre,poder):
		self.nombre=nombre
		self.vida=100
		self.poder=poder
 		

	def sayName(self):
		return self.nombre*2

	def checkVida(self):
		if self.vida<=0:
			print("Ya vali .$.@#",self.sayName())
		else:
			print("ahi te voy perro",self.sayName())


class Fuego(Pokemon):
	def __init__(self,nombre,poder=10):
		Pokemon.__init__(self,nombre,poder)
		self.tipo="Fuego"

	def ataquePrincipal(self,objeto):
		if objeto.tipo=="Agua":
			objeto.vida-=(self.poder/2)
		else if objeto.tipo=="Planta":
			objeto.vida-=self.poder*2
		else:
			objeto.vida-=self.poder

		print(self.sayName()," puto!")
		objeto.checkVida()

class Agua(Pokemon):
	def __init__(self,nombre,poder=10):
		Pokemon.__init__(self,nombre,poder)
		self.tipo="Agua"

	def ataquePrincipal(self,objeto):
		if objeto.tipo=="Fuego":
			objeto.vida-=(self.poder*2)
		else if objeto.tipo=="Planta":
			objeto.vida-=(self.poder/2)
		else:
			objeto.vida-=self.poder
		print(self.sayName()," puto!")
		objeto.checkVida()

class Planta(Pokemon):
	def __init__(self,nombre,poder=10):
		Pokemon.__init__(self,nombre,poder)
		self.tipo="Planta"

	def ataquePrincipal(self,objeto):
		if objeto.tipo=="Agua":
			objeto.vida-=(self.poder*2)
		else if objeto.tipo=="Fuego":
			objeto.vida-=(self.poder/2)
		else:
			objeto.vida-=self.poder
		print(self.sayName()," puto!")
		objeto.checkVida()

	

fuego=Fuego("fuego",50)
agua=Agua("agua",50)
planta=Agua("planta",50)
