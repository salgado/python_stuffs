
# insertion sort

lista=[2, 89, 4, 100, 1]

print lista

#insertion
for i in range(1,len(lista)):
	temp = lista[i]
	j=i-1
	while(temp<lista[j] and j>=0):
		lista[j+1] = lista[j]
		j=j-1

	lista[j+1] = temp

print lista



