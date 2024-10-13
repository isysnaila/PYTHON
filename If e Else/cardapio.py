print('******LANCHONETE DA ZIZI******')
print('----------CARDÁPIO------------')
print('(1)Coxinha: R$6,00------------')
print('(2)Empada: R$8,00-------------')
print('(3)Espetinho: R$10,00---------')
print('(4)Quibe: R$7,00--------------')
print('------------------------------')
comida=str(input('Qual opção você deseja? (digite de 1 a 4)\n'))
if comida=='1':
  valor=6
  produto='Coxinha: R$6,00|'
elif comida=='2':
  valor=8
  produto='Empada: R$8,00|'
elif comida=='3':
  valor=10
  produto='Espetinho: R$10,00|'
elif comida=='4':
  valor=7
  produto='Quibe: R$7,00|'


segundaopcao=str(input('Deseja mais uma refeição? Digite 1 para SIM e 2 para NÃO\n'))
if segundaopcao=='1':
  print('******LANCHONETE DA ZIZI******')
  print('----------CARDÁPIO------------')
  print('(1)Coxinha: R$6,00------------')
  print('(2)Empada: R$8,00-------------')
  print('(3)Espetinho: R$10,00---------')
  print('(4)Quibe: R$7,00--------------')
  print('------------------------------')
  escolhacomida2 = str(input('Qual opção você deseja? (digite de 1 a 4)\n'))
  if escolhacomida2 == '1':
     valor2 = 6
     produto2 = 'Coxinha: R$6,00|'
  elif escolhacomida2 == '2':
     valor2 = 8
     produto2 = 'Empada: R$8,00|'
  elif escolhacomida2 == '3':
     valor2 = 10
     produto2 = 'Espetinho: R$10,00|'
  elif escolhacomida2 == '4':
     valor2 = 7
     produto2 = 'Quibe: R$7,00|'
else:
  valor2=0
  produto2=''






bebida=str(input('Deseja uma bebida? Digite 1 para SIM e 2 para NÃO\n'))
if bebida=='1':
  print('----------BEBIDAS-------------')
  print('(1)Água: R$3,00---------------')
  print('(2)Refrigerante: R$8,00-------')
  print('(3)Suco: R$6,00---------------')
  print('(4)Cerveja: R$10,00-----------')
  print('------------------------------')
  bebidaescolha=str(input('Qual bebida você deseja? (digite de 1 a 4)\n'))
  if bebidaescolha=='1':
     valorb=3
     produtob='Água: R$3,00|'
  elif bebidaescolha=='2':
     valorb=8
     produtob='Refrigerante: R$8,00|'
  elif bebidaescolha=='3':
     valorb=6
     produtob='Suco: R$6,00|'
  elif bebidaescolha=='4':
     valorb=10
     produtob='Cerveja: R$10,00|'
else:
   valorb=0
   produtob=""


segundaopcaob = str(input('Deseja mais uma bebida? Digite 1 para SIM e 2 para NÃO\n'))
if segundaopcaob=='1':
  print('----------BEBIDAS-------------')
  print('(1)Água: R$3,00---------------')
  print('(2)Refrigerante: R$8,00-------')
  print('(3)Suco: R$6,00---------------')
  print('(4)Cerveja: R$10,00-----------')
  print('------------------------------')
  bebidaescolha2 = str(input('Qual bebida você deseja? (digite de 1 a 4)\n'))
  if bebidaescolha2 == '1':
     valorb2 = 3
     produtob2 = 'Água: R$3,00|'
  elif bebidaescolha2 == '2':
     valorb2 = 8
     produtob2 = 'Refrigerante: R$8,00|'
  elif bebidaescolha2 == '3':
     valorb2 = 6
     produtob2 = 'Suco: R$6,00|'
  elif bebidaescolha2 == '4':
     valorb2 = 10
     produtob2 = 'Cerveja: R$10,00|'
     






  valortotal = valor+valorb+valor2+valorb2
  valortotalstr = str('%.2f' % valortotal)
  valortotalreal = (valortotalstr).replace('.', ',')
  print('-' * 30)
  print('PEDIDO: %s %s %s %s' % (produto,produto2,produtob,produtob2))
  print('TOTAL DO PEDIDO: R$%s' % valortotalreal)
  print('-' * 30)
else:
     valorb2=0
     produtob2=''
     valortotal = valor + valorb + valor2
     valortotalstr = str('%.2f' % valortotal)
     valortotalreal = (valortotalstr).replace('.', ',')
     print('-' * 30)
     print('PEDIDO: %s %s %s' % (produto, produto2, produtob))
     print('TOTAL DO PEDIDO: R$%s' % valortotalreal)
     print('-' * 30)



