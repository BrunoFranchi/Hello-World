from Primeira import Filme, Serie, Music, PlayList
from SeleniumScripts import SeleniumClass
pets = Filme('Pets 2 ',2019,90)
witcher = Serie('the witcher', 2019, 1)
coringa = Filme('coringa', 2019, 120)
scorpions = Music('scorpions', 1965, 'Rock and Roll')
coringa.dar_like()
coringa.dar_like()
coringa.dar_like()
witcher.dar_like()
witcher.dar_like()
witcher.dar_like()
witcher.dar_like()
'''
print(f'Filme: {coringa.nome} - Duração: {coringa.duracao} minutos - Likes: {coringa.likes}')

malevola = Filme('malevola', 2019, 90)
malevola.dar_like()

witcher = Serie('the witcher', 2019, 1)
witcher.dar_like()
witcher.dar_like()
print(f'Serie: {witcher.nome} - Temporadas: {witcher.temporada} - Likes: {witcher.likes}')

filmes_e_series = [coringa, witcher, malevola]

#for p in filmes_e_series:  Essa é uma maneira de acessar os atributos que nao estao sendo compartilhados
#                            atraves da classe mae (Polimorfismo)
#    detalhe = p.duracao if hasattr(p,'duracao') else p.temporada
#    print(f'{p.nome}, {p.likes}, Duração/Temporada: {detalhe} ')
'''
filmes_e_series = [witcher, coringa, scorpions]

Weekend = PlayList('The Best', filmes_e_series)

for p in Weekend:
    print(p)

print(coringa.nome)
