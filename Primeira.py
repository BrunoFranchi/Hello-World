#import timss

#from controller.filme_controller import Bruno


class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'Name: {self._nome} Year: {self.ano} Likes: {self._likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def comits(self, max = 20):
        self.max = max
        comit = str(input(f'--{self.nome}-- Diga oque achou deste filme (Max 20 letras ): '))
        while len(comit) > max:
            print('Digite no máximo 5 caracteres')
            comit =str(input(f'--{self.nome}-- Diga oque achou deste filme (Max 20 letras ): '))
        print(comit)
        #comit = comit[:max]

    def __str__(self):
        return f'Name: {self._nome} Year: {self.ano} Time: {self.duracao} Likes: {self._likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f'Name: {self._nome} Year: {self.ano} Temporadas: {self.temporada} Likes: {self._likes}'

class Music(Programa):
    def __init__(self, nome, ano, estilo):
        super().__init__(nome, ano)
        self.estilo = estilo

    def __str__(self):
        return f'Nome: {self._nome} Year: {self.ano} Estilo: {self.estilo} Likes: {self._likes}'
'''
class PlayList(list): # aqui eu passo lista para a classe receber a herança de lista e chamo a super da classe list
    def __init__(self, nome, lista_de_selecionadas):
        self.nome = nome
        super().__init__(lista_de_selecionadas)
'''

class PlayList():
    def __init__(self, nome, lista_de_selecionadas):
        self.nome = nome
        self._lista_de_selecionadas = lista_de_selecionadas

    def __getitem__(self, item):
        return self._lista_de_selecionadas[item]

    @property
    def listagem(self):
        return self._lista_de_selecionadas

    @property
    def __len__(self):
        return len(self._lista_de_selecionadas)















