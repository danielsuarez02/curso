lista=list(map(int,input("Dame una lista de numeros").split(" ")))

for n in lista:
	for n in range(0,len(lista)-1):
		if lista[n]>lista[n+1]:
			aux=lista.pop(n)
			lista.insert(n+1,aux)


print(lista)