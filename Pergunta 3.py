"""
Dado o array de números inteiros [1, 15, 2, 7, 2, 5, 7, 1, 4] crie uma função que recebe um
argumento X e retorne true ou false caso haja no array uma combinação de soma entre dois
números que resulte no input X. Exemplo: Se X=2, a função deve retornar true pois existem dois
números 1 dentro do array 1+1 = 2. Caso X=1231 a função deve retornar false pois não existe
uma combina de dois números capazes de somar 1231.
"""

#Array de Números
Array = [1, 15, 2, 7, 2, 5, 7, 1, 4]

#Copia do Array
c_Array = Array.copy()

numero = None

#Verifica se a entrada realmente é um número inteiro
while True:
    try:
        numero = int(input('Digite o número desejado: '))
        break
    except:
        print('Número invalido, Tente novamente\n')

#Função Combinação com argumento sendo o números desejado para que a soma se alcance
#Primeiro For utilizado para retirar numeros que são maiores ou iguais ao números de soma
#Segundo For utilizado para iterar sobre todos os numeros, somandos-os e caso a soma resulte no números desejado
#É retornado True, caso nenhuma soma de dois números consiga atingir o resultado desejado, retorna False
def Combinação(numero):
    segundo_array = []
    for i in range(len(c_Array)):
        if c_Array[i] < numero:
            segundo_array.append(c_Array[i])
    
    for i in range(len(c_Array)):
        for y in range(len(c_Array)):
            if y != i:
                if c_Array[i] + c_Array[y] == numero:
                    return True
    return False
print(Combinação(numero))