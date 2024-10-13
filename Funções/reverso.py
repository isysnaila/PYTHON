def reverso(numero):
   numero_str = str(numero)
   reverso_str = numero_str[::-1]
   reverso = int(reverso_str)
   return reverso






numero=int(input('Insira um número:\n'))
reverso_numero = reverso(numero)
print(f"O reverso de {numero} é {reverso_numero}")