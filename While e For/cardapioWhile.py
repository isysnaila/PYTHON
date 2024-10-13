import sys
valor=0
produto=''
print('******LANCHONETE DA ZIZI******')
print('----------CARDÁPIO------------')
print('(1)Coxinha: R$6,00------------')
print('(2)Empada: R$8,00-------------')
print('(3)Espetinho: R$10,00---------')
print('(4)Quibe: R$7,00--------------')
print('(5)FINALIZAR PEDIDO-----------')
print('------------------------------')
comida=str(input('Qual opção você deseja? (escolha de 1 a 5)'))
if comida=='1':
  valor+=6
  produto+='Coxinha: R$6,00|'
elif comida=='2':
  valor+=8
  produto+='Empada: R$8,00|'
elif comida=='3':
  valor+=10
  produto+='Espetinho: R$10,00|'
elif comida=='4':
  valor+=7
  produto+='Quibe: R$7,00|'
else:
  produto=''
  valor=0
  print(produto)
  valorstr = str('%.2f' % valor)
  valorreal = (valorstr).replace('.', ',')
  print('TOTAL DO PEDIDO: R$%s'%valorreal)
  sys.exit()
print('-'*20)
print('Total: R$%5.2f'%valor)
print(produto)
print('-'*20)
opcao2=input('Deseja adicionar outro produto (Use 1 para SIM e 5 para finalizar.)')
while opcao2=='1':
  print('******LANCHONETE DA ZIZI******')
  print('----------CARDÁPIO------------')
  print('(1)Coxinha: R$6,00------------')
  print('(2)Empada: R$8,00-------------')
  print('(3)Espetinho: R$10,00---------')
  print('(4)Quibe: R$7,00--------------')
  print('(5)FINALIZAR PEDIDO-----------')
  print('------------------------------')
  comida=str(input('Qual opção você deseja (escolha de 1 a 5)'))
  if comida=='1':
      valor+=6
      produto+='Coxinha: R$6,00|'
  elif comida=='2':
      valor+=8
      produto+='Empada: R$8,00|'
  elif comida=='3':
      valor+=10
      produto+='Espetinho: R$10,00|'
  elif comida=='4':
      valor+=7
      produto+='Quibe: R$7,00|'
  else:
      print(produto)
      valorstr = str('%.2f' % valor)
      valorreal = (valorstr).replace('.',',')
      print('TOTAL DO PEDIDO: R$%s'%valorreal)
      sys.exit()
  print('-' * 20)
  print('Total: R$%5.2f' % valor)
  print(produto)
  print('-' * 20)
  opcao2=input('Deseja adicionar outro produto? (Use 1 para SIM e 5 para finalizar.)')
print('*'*20)
print(produto)
valorstr = str('%.2f' % valor)
valorreal = (valorstr).replace('.', ',')
print('TOTAL DO PEDIDO: R$%s'%valorreal)
print('*'*20)
