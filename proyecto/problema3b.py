#remplazar letras por asteriscos
lista=input("Dame varias palabras: ").split(" ")

i=""
for palabra in lista:
	print("*"*len(palabra))