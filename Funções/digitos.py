def quantdigitos(numero):
   numero_str = str(numero)
   quantdigitos_str = len(numero_str)
   quantdigitos = int(quantdigitos_str)
   return quantdigitos


numero=int(input('Insira um número:\n'))
print('Esse número tem', quantdigitos(numero), 'dígitos.')