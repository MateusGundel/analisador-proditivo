class Analiser():
    def __init__(self):
        pass

    def create_first(self):
        pass

    def create_follow(self):
        pass

    def criar_ações(self):
        pass

    def preencher_tabela(self):
        pass

    def reconhecer_entrada(self):
        pass

    def is_terminal(self, caracter):
        list_non_terminal = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        return caracter.replace("'", "") in list_non_terminal

