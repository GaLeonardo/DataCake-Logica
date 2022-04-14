"""
Dado o array [9, 2, 3, 1, 4] encontre todos os números que estão faltando para completar o
intervalo 0 a n, onde n é o maior número dentro do array. Adicione os números faltando dentro
do array.
"""

#Array para completar
Array = [9, 2, 3, 1, 4]

#Função Completa Array com a lista como argumento
#Pega o maior numero com a função max
#Organiza a lista do menor para o maior
#Itera sobre a lista verificando se os numeros baixo do maior_numero são existentes
#Caso não seja ele é inserido na lista

def CompletaArray(lista):
    maior_numero = max(lista)
    lista.sort()
    
    for i in range(maior_numero):
        if lista[i] != i:
            lista.insert(i ,i)
    return lista    
print(CompletaArray(Array))