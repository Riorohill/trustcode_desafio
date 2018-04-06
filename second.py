from random import randint

lista = [randint(0,5000000) for x in range(500)]
lista2 = [randint(0,5000000) for x in range(50000)]

for element in lista2:
    if (element in lista):
        print("Element {} from lista2 also in lista.".format(element))

