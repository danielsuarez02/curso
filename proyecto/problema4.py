#invertir la palabra
lista=input("Dame una frase: ")

inv=""
for n in range(0,len(lista)):
	inv+=lista[len(lista)-n-1]

print(inv)