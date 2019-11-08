class Analiser():
    def __init__(self):
        pass

    def create_first(self, objetos):
        first_list = {}
        for objeto in objetos:
            for string in objetos[objeto]:
                string_separada = list(string)
                letter_check = string_separada[0]
                while self.is_non_terminal(letter_check):
                    letter_check = list(objetos[letter_check])[0]

                if objeto in first_list:
                    first_list[objeto].append(letter_check)
                else:
                    first_list.update({objeto: [letter_check]})
        return first_list

    def create_follow(self, objetos):
        initial_letter = None
        follow_list = {}
        for i, objeto in enumerate(objetos):
            for j, objeto2 in enumerate(objetos):
                for prod in objetos[objeto2]:
                    for num_letter, letter in enumerate(self.get_list_from_prod(prod)):
                        if letter == objeto:
                            if num_letter + 1 < len(self.get_list_from_prod(prod)):
                                letter_check = self.get_list_from_prod(prod)[num_letter + 1]
                                while self.is_non_terminal(letter_check):
                                    letter_check = self.get_list_from_prod(objetos[letter_check][0])[0]
                                if objeto in follow_list:
                                    if not letter_check in follow_list[objeto]:
                                        follow_list[objeto].append(letter_check)
                                else:
                                    follow_list.update({objeto: [letter_check]})
                        if i == j and letter == objeto and i != 0:
                            if objeto in follow_list:
                                follow_list[objeto].append(follow_list[initial_letter])
                            else:
                                follow_list.update({objeto: follow_list[initial_letter]})
            if i == 0:
                initial_letter = objeto
                if objeto in follow_list:
                    follow_list[objeto].append("$")
                else:
                    follow_list.update({objeto: ["$"]})
        return follow_list

    def criar_ações(self, objetos, first_list, follow_list):
        lista_criacao = []
        for objeto in objetos:
            for i, item in enumerate(objetos[objeto]):
                if i % 2 == 0:
                    list = []
                    for detail in first_list[objeto]:
                        if detail != 'e':
                            list.append(detail)
                    lista_criacao.append({"m": {objeto: list}, "acao": objeto + " -> " + str(item)})
                else:
                    lista_criacao.append(
                        {"m": {objeto: follow_list[objeto]}, "acao": objeto + " -> " + str(item)})
        return lista_criacao

    def preencher_tabela(self):
        pass

    def reconhecer_entrada(self, entrada, lista_criacao, objetos):
        pilha_entrada = []
        # cria uma pilha com os valores da entrada
        for letra in entrada:
            pilha_entrada.append(letra)
        pilha_entrada.reverse()
        # cria uma pilha de reconhecimento
        pilha = []
        pilha.append("$")
        pilha.append(objetos[0].esquerda) # o primeiro item da pilha é o primeiro da gramática
        # pega último item da pilha_entrada e o último da pilha, vê a relação e substitui ele


    def is_non_terminal(self, caracter):
        if "'" in caracter:
            caracter = caracter.replace("'", "")
        list_non_terminal = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        return caracter in list_non_terminal

    def get_list_from_prod(self, prod):
        lista = list(prod)
        index = 0
        while index != -10:
            index = -10
            for i, item in enumerate(lista):
                if item == "'":
                    index = i
                    break
            if index != -10:
                lista[index - 1] = lista[index - 1] + "'"
            final_list = []
            for a in lista:
                if a != "'":
                    final_list.append(a)
            lista = final_list
        return lista
