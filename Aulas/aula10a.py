'''CONDIÇÕES'''
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1+n2)/2
print('Sua média é:{:.2f}'.format(media))
if media >=5:
    print('Parabéns, você foi aprovado!')
else:
    print('Você é muito burro ta loco.')