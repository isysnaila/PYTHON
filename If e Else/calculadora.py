numum=int(input('Insira um número:\n'))
numdois=int(input('Insira o segundo número: \n'))
sinal=str(input('Qual operação você deseja fazer? (USE /*+ OU -)\n'))
if (sinal=='/'):
   conta=numum/numdois
elif (sinal=='*'):
   conta=numum*numdois
elif (sinal=='-'):
   conta=numum-numdois
elif (sinal=='+'):
   conta=numum+numdois
print('-'*20)
print('O resultado é: %d'%conta)
print('-'*20)