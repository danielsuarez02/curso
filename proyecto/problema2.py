#recibir varias palabras y devolver la mas larga
lista=input("Dame varias palabras: ").split(" ")

i=0
for n in range(0,len(lista)):
	if len(lista[n])>len(lista[i]):
		i=n
	


print(lista[i])