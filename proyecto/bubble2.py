lista=list(map(int,"8 3 9 4 5 2 20 6 55 34".split(" ")))
print(lista)
for n in range(1,len(lista)):
	n3=-1

	for n2 in range(n-1,-1,-1):
		if lista[n]<lista[n2]:
			n3=n2
	if n3>-1:
		print(n)
		print(n3)
		aux=lista.pop(n)
		lista.insert(n3,aux)
	print(lista)


print(lista)