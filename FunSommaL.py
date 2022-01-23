def somma_lista(lista):
    x=0
    for i in lista:
        x=x+i
    return x

lista={1,2,3,4,5,-4}
x=somma_lista(lista)
print(x)