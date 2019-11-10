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

    def criar_acoes(self, objetos, first_list, follow_list):
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

    def preencher_tabela(self, lista_criacao):
        print("tabela")
        print(lista_criacao)
        list_nt = []
        list_t = [" "]
        final_list = []
        for item in lista_criacao:
            for a in item['m']:
                if not a in list_nt:
                    list_nt.append(a)
                if not item['m'][a] in list_t:
                    list_t.append(item['m'][a])
        final_list = []
        final_list.append(list_t)
        for x in range(len(list_nt)):
            temp_list = []
            for y in range(len(list_t)):
                added = False
                if y == 0:
                    temp_list.append(list_nt[x])
                    added = True
                else:
                    for item in lista_criacao:
                        for a in item['m']:
                            if a == list_nt[x] and item['m'][a] == list_t[y]:
                                temp_list.append(item['acao'])
                                added = True
                if(not added):
                    temp_list.append(" ")                
            final_list.append(temp_list)
        return final_list
                
    def reconhecer_entrada(self, entrada, lista_criacao, objetos):
        # declaração de variáveis
        global conjunto
        response_data = {}
        pilha_entrada = []
        pilha = []
        # cria uma pilha com os valores da entrada
        pilha_entrada = entrada.split(" ")
        pilha_entrada.reverse()
        # define o primeiro simbolo da pilha de reconhecimento
        pilha.append("$")
        #adiciona o priemiro não terminar da gramática na pilha
        for a in objetos:
            pilha.append(a)
            break
        # verifica se o último da pilha é um não terminal
        while pilha[len(pilha)-1] != '$':
            if self.is_non_terminal(pilha[len(pilha)-1]):
                    # iteração na lista de ações
                    # print("reconhece = ", reconhece)
                    for item in lista_criacao:
                        reconhece = 0
                        for a in item['m']:
                            # compara o item do topo da pilha com e o item do topo da pilha de entrada com as ações motnadas
                            # print("pilha ", pilha[len(pilha)-1])
                            # print("pilha entrada ", pilha_entrada[len(pilha_entrada)-1])
                            # print("item [m] ", item['m'])
                            if pilha[len(pilha)-1] in item['m'] and item['m'][a][0] == pilha_entrada[len(pilha_entrada)-1]:
                                pilha.pop()
                                # print("ação ", item['acao'])
                                aux = []
                                for b in item['acao'].split("> ")[1]:
                                    if b == "'":
                                        aux[len(aux) - 1] = aux[len(aux) - 1] + b
                                    else:
                                        aux.append(b)
                                aux.reverse()
                                for i in aux:
                                    pilha.append(i)
                                reconhece = 1
                                conjunto = {'conjunto': [item['m'][a], pilha_entrada[len(pilha_entrada)-1]]}
                                # print(conjunto)
                                break
                        if reconhece == 0:
                            response_data = {'status': "Não reconheceu"}
                        # quando o topo das duas são não terminais iguais, retira das duasvii
                    #print("reconhece depois do for ", reconhece)
                #verifica se o topo da pilha é igual ao topo da pilha de entrada
            elif pilha[len(pilha)-1] == 'e':
                pilha.pop()
            elif pilha_entrada[len(pilha_entrada) - 1][0] == pilha[len(pilha)-1] and pilha[len(pilha)-1] != '$':
                    pilha_entrada.pop()
                    pilha.pop()
                    reconhece = 1
            if pilha[len(pilha)-1] == '$':
                    response_data = {'status': "Reconhecido"}
            print("entrada: ", pilha_entrada)
            print("pilha: ", pilha)
        return response_data

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
