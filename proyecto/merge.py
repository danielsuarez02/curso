lista=[0, 10, 2, 30, 4, 50, 6, 70, 8, 90]


pares=2
while pares<len(lista)*2:
	n=0
	for n in range(0,len(lista),pares):
		for n2 in range(0,pares-1):
			if  len(lista)>n+n2 and len(lista)>n+n2+1 and lista[n+n2]>lista[n+n2+1]:
				aux=lista.pop(n+n2+1)
				lista.insert(n+n2,aux)
				print(lista)
		
	pares+=2


print(lista)