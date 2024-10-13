
str=input('Digite uma palavra:\n')
letras=int(input('Quantas letras dessa palavra você deseja que sejam separadas?\n'))
print('Primeira parte:',(str[0:letras]))
print('Segunda parte:',(str[letras: ]))




nome=input('Olá! Qual o seu nome? \n')
sobre=input('Qual o seu sobrenome?\n')
nomesobre=nome+' '+sobre
numimprimir=int(input('Quantas vezes deseja imprimir seu nome e sobrenome na tela?\n'))
print('-'*20)
print('')
print((nomesobre+'\n')*numimprimir)
print('-'*20)



print('Olá! Tudo bem?')
valor=int(input('Insira um valor: \n'))
valorstr=str('%.2f'%valor)
valorreal=str(valorstr).replace('.',',')
print('-'*20)
print('O valor inserido foi R$ %s'%valorreal)



print('Olá!')
valor=float(input('Insira o valor da compra: \n'))
valordinheiro=float(input('Qual valor você tem em dinheiro?'))
troco=valordinheiro-valor
trocostr=str('%.2f'%troco)
trocoreal=str(trocostr).replace('.',',')
print('-'*20)
print('Seu troco é: R$ %s'%trocoreal)
print('-'*20)

