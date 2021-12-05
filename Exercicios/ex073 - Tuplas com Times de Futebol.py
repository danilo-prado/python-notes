'''CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL,
NA ORDEM DE COLOCAÇÃO. DEPOIS MOSTRE:
A) APENAS OS 5 PRIMEIROS COLOCADOS
B) OS ÚLTIMOS 4 COLOCADOS DA TABELA
C) UMA LISTA COM OS TIMES EM ORDEM ALFABÉTICA
D) EM QUE POSIÇÃO NA TABELA ESTÁ O TIME DA CHAPECOENSE'''

tupla = ('','Atlético-MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Fortaleza', 'Bragantino', 'Fluminense', 'América-MG', 'Ceará SC', 'Internacional', 'Atlético-GO', 'Santos', 'Athletico-PR', 'São Paulo', 'Juventude', 'Cuiabá', 'Bahia', 'Grêmio', 'Sport Recife', 'Chapecoense')

print(f'Os cinco primeiros colocados são: {tupla[1:5]}')
print(f'Os quatro últimos colocados são: {tupla[-4:]}')
print(sorted(tupla[1:]))
print('A Chapecoense está na posição de número', tupla.index('Chapecoense'))