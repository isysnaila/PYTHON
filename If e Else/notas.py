import sys
nota1=int(input('Insira a primeira nota: entre 0 e 25: \n'))
if (nota1<0)or(nota1>25):
 print('Nota inválida!')
 sys.exit()
nota2=int(input('Insira a segunda nota:\n'))
if (nota2<0)or(nota2>25):
 print('Nota inválida!')
 sys.exit()
nota3=int(input('Insira a terceira nota:\n'))
if (nota3<0)or(nota3>25):
 print('Nota inválida!')
 sys.exit()
nota4=int(input('Insira a quarta nota:\n'))
if (nota4<0)or(nota4>25):
 print('Nota inválida!')
 sys.exit()
total=nota1+nota2+nota3+nota4
print('-'*30)
print('A nota total é:%d pontos.'%total)
if total>=80:
 print('ALUNO APROVADO! EXCELENTE!')
if (total>=60)and(total<=79):
 print('ALUNO APROVADO')
if (total>=40)and(total<=59):
 print('ALUNO EM RECUPERAÇÃO')
if total<40:
 print('ALUNO REPROVADO')
print('-'*30)