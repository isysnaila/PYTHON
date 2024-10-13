def potencia(a, b):
   cont=1
   total=a
   while (cont<b):
       total=total*a
       cont+=1
   return total




a=int(input('Insira o primeiro número:\n'))
b=int(input('Insira o segundo número:\n'))
print(f"{a} elevado a {b} é igual a {potencia(a, b)}")