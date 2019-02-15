import random


def basico(lista1, lista2):
    resultado = []
    while True:
        sorteio1 = [random.choice(lista1), random.choice(lista2)]
        resultado.append(sorteio1)
        lista1.remove(sorteio1[0])
        lista2.remove(sorteio1[1])

        if len(lista1) <= 0:
            return resultado

def retorno_unico(lista):
    return random.choice(lista)

def retorno_duplo(lista1, lista2):
    return random.choice(lista1), random.choice(lista2)

def num_int_positivo(num, zero):
    # importante o booleano para inclusão ou não do zero
    if zero == True:
        cont = 0
    else:
        cont = 1

    valor = []

    while cont <= num:
        valor.append(cont)
        cont+=1
    return random.choice(valor)


nomes = ['A', 'B', 'C', 'D']
temas = ['1', '2', '3', '4']

# print(basico(nomes, temas))
# print(retorno_unico(nomes))
# print(retorno_duplo(nomes, temas))
# print(num_int_positivo(10, True))