lista=[2,5,1,4,9,7,8,6] #list(map(int,input("Dame una lista de numeros").split(" ")))

print("la lista: ",lista)

for i in range(1,len(lista)):
	j=i
	while j>0 and lista[len(lista)-j] < lista[len(lista)-j-1]:
		lista[len(lista)-j],lista[len(lista)-j-1]=lista[len(lista)-j-1],lista[len(lista)-j]
		j-=1
	print(lista)

lista=[2,5,1,4,9,7,8,6] #list(map(int,input("Dame una lista de numeros").split(" ")))

print("la lista: ",lista)

for i in range(1,len(lista)):
	j=len(lista)-i
	while j<len(lista) and lista[j] < lista[j-1]:
		lista[j],lista[j-1]=lista[j-1],lista[j]
		j+=1
	print(lista)