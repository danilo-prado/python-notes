'''CRIE UM PROGRAMA QUE LEIA NOME, ANO DE NASCIMENTO E CARTEIRA DE TRABALHO E CADASTRE-OS (COM IDADE) EM UM DICIONÁRIO
SE POR ACASO A CTPS FOR DIFERENTE DE ZERO, O DICIONÁRIO RECEBERÁ TAMBÉM O ANO DE CONTRATAÇÃO E O SALÁRIO. CALCULE E
ACRESCENTE, ALÉM DA IDADE, COM QUANTOS ANOS A PESSOA VAI SE APOSENTAR.'''

dic = {'nome': input('NOME: '),
       'nasc': int(input('ANO NASCIMENTO: ')),
       'ctps': int(input('CTPS (0 NÃO TEM): ')),
       'ano': int(input('ANO DE CONTRATAÇÃO: ')),
       'salario': int(input('SALÁRIO: R$'))}

if dic['ctps'] != 0:
    print('='*30)
    print('====FICHA DE CADASTRO====')
    print(f'O nome é {dic["nome"]}')
    print(f'Idade tem o valor de {dic["nasc"]}')
    print(f'CTPS tem o valor {dic["ctps"]}')
    print(f'Contratação tem o valor de {dic["ano"]}')
    print(f'Salário tem o valor de R${dic["salario"]}')
    print(f'Aposentadoria tem o valor de {dic["ano"]+ 35}')
else:
    print('NÃO POSSUI CTPS')
