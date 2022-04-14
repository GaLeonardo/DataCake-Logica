"""
Dado o Array de inteiros abaixo, ordene-o de tal forma que os números “1” estejam à esquerda.
Os itens devem ser modificados no lugar, ou seja, você não ira trocar posições e sim colocar os
números “1” no inicio do Array.
[2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]
"""

#Dados Array
Dados = [2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]

#Numero a ser reordenado
numero = 1

#Manipulação sem alterar os dados originais
c_Dados1 = Dados.copy()
c_Dados2 = Dados.copy()

#Conta quantas vezes o numero aparece e modifica os numeros iniciais
rep_Numero = c_Dados1.count(numero)
print(c_Dados1)
for i in range(rep_Numero):
    c_Dados1[i] = numero
    c_Dados2.remove(1)
print(c_Dados1)
print(c_Dados2)

#Reordena o restante da lista
for i in range(len(c_Dados2)):
    c_Dados1[i+rep_Numero] = c_Dados2[i]
print(c_Dados1)
    