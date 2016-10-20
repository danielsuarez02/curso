def quicksort(lista,inicio,fin): 
	if inicio==fin:
		return
	for i in range(inicio,int(fin/2)):
		if lista[i]>lista[fin-i]:
			lista[i],lista[fin-i]=lista[fin-i],lista[i]
			print(lista)
	quicksort(lista,inicio,int(fin/2))
	quicksort(lista,int(fin/2),fin)

lista=[2,5,1,4,9,7,8,6] #list(map(int,input("Dame una lista de numeros").split(" ")))

print("la lista: ",lista)

quicksort(lista,0,len(lista)-1)

print(lista)


