'''FAÇA UM PROGRAMA QUE LEIA NOME E MÉDIA DE UMA ALUNO, GUARDANDO TAMBÉM A SITUAÇÃO EM UM DICIONÁRIO.
NO FINAL, MOSTRE O CONTEÚDO DA ESTRUTURA NA TELA'''

aluno = {}

aluno['nome'] = str(input('NOME: '))
aluno['media'] = float(input('MÉDIA: '))
print(f'O aluno {aluno["nome"]} teve a média {aluno["media"]}.')
if aluno['media'] >= 5:
    print(f'{aluno["nome"]} está APROVADO!')
else:
    print(f'{aluno["nome"]} está REPROVADO!')
