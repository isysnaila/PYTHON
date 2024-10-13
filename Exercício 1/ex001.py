nota1=int(input('Insira a primeira nota:'))
nota2=int(input('Insira a segunda nota:'))
nota3=int(input('Insira a terceira nota:'))
media=(nota1+nota2+nota3)/3
print('Sua nota média é:',media)



print('*******Cálculo de valor do terreno*******')
largura=int(input('Qual a largura do terreno?'))
comprimento=int(input('Qual o comprimento do terreno?'))
m2=largura*comprimento
print('')
print('Esse terreno possui ',m2,'m²')
valor=m2*850
print('O valor total para construir nesse terreno é de: R$',valor)
print('________________________________________________________')



print('------Média Salarial------')
nome=input('Qual o seu nome?')
salario=int(input('Quanto você recebe por mês?'))
horas=int(input('E quantas horas você trabalha por dia?'))
totaltrabalhado=horas*30
salarioporhora=salario/totaltrabalhado
print('')
print(nome,'recebe em torno de R$',salarioporhora,' por hora trabalhada')



print('------CÁLCULO DE IMC------')
nome=input('Ola! Seja bem vindo(a). Qual o seu nome?')
peso=float(input('Qual o seu peso atual?'))
altura=float(input('E qual a sua altura?'))
imc=peso/(altura*altura)
print('')
print('Certo',nome,'. O seu imc é:',imc)

