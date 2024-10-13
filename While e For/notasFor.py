notas=[]
soma=0
y=0
x=0
for cont in range(0,5):
   notas.append(int(input('Insira sua nota:')))
while y<5:
   soma+=notas[y]
   y+=1
print('*'*20)
print('RESUMO DAS NOTAS:')
print('*'*20)
while x<5:
   print('Nota ',x,'= %5.2f'%notas[x])
   x+=1
print('-'*20)
print('Média=%5.2f'%(soma/y))