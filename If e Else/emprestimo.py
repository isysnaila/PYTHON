print('------Empréstimo Bancário------')
valorcasa=int(input('Qual o valor da casa que  você deseja comprar?\n'))
salario=int(input('Qual o seu salário mensal?\n'))
anos=int(input('Por quantos anos você deseja pagar?\n'))
print('-'*30)
meses=int(anos*12)
prestacao=valorcasa/meses
porcentagem=(salario*30)/100
if prestacao>porcentagem:
   print('Seu empréstimo infelizmente não foi autorizado pois a prestação excede a 30% do seu salário.')
   print('-' * 30)


else:
   prestacaostr=str('%.2f'%prestacao)
   prestacaoreal=str(prestacaostr).replace('.',',')
   print('Parabéns! Seu empréstimo foi autorizado! Sua prestação será no valor de R$ %s , durante %d meses.'%(prestacaoreal,meses))
   print('-' * 30)
