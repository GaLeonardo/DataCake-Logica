"""
Dada a seguinte arvore binária de palavras, faça uma função que busque nessa arvore pela
palavra-chave. O output da sua função deve ser o caminho até chegar no item procurado. Por
exemplo, se o input de buscar for “goiaba” o output deve ser uma string “Maça -> morango ->
Goibana”.
"""
#Arvore Binarias De Palavra
Arvore_Palavras = [ 'Goiaba', 'Morango', 'Limão', 'Maça', 'Pera', 'Abacaxi',  'Banana', 'Laranja',  'Cebola']

#Classe da arvore
class Arvore(object):
    def __init__(self, key, left=None, right=None, path=''):
        #Construtor da chave, direções e caminho
        self.key = key
        self.left = left
        self.right = right
        self.path = path
 
    def get(self, key, path):
        #Método GET responsável por procurar e armazenar o caminho até palavra-chave na árvore 
        path += f"{Arvore_Palavras[self.key]}"
        if self.key == key:
            return path
        node = self.left if key < self.key else self.right
        if node is not None:
            path += " -> "
            return node.get(key, path)

#Criação da Árvore
root = Arvore(Arvore_Palavras.index("Maça"))

#Criação do lado esquerdo da Árvore
root.left = Arvore(Arvore_Palavras.index("Morango"))
root.left.left = Arvore(Arvore_Palavras.index("Goiaba"))
root.left.right = Arvore(Arvore_Palavras.index("Limão"))

#Criação Lado direito da Árvore
root.right = Arvore(Arvore_Palavras.index("Pera"))
root.right.right = Arvore(Arvore_Palavras.index("Abacaxi"))
root.right.right.right = Arvore(Arvore_Palavras.index("Laranja"))
root.right.right.right.left = Arvore(Arvore_Palavras.index("Banana"))
root.right.right.right.right = Arvore(Arvore_Palavras.index("Cebola"))

#Input da palavra-chave com um sistema para verificar se a palavra existe na Árvore
palavra_chave = ''
while True:
    palavra_chave = str(input('Digite a palavra-chave para Pesquisa: '))
    if palavra_chave.capitalize() in Arvore_Palavras:
        break
    else:
        print(f'Palavra-chave {palavra_chave} não existente na Árvore. Digite novamente\n')

#Inicializa o método de procura pela palavra-chave
found = root.get(Arvore_Palavras.index(palavra_chave), '')
if found:
    print(found)



















