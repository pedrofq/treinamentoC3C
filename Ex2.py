listaNumeros = []

primeiroValor = float(input("Digite o primeiro valor: "))
segundoValor = float(input("Digite o segundo valor: "))
terceiroValor = float(input("Digite o terceiro valor: "))

listaNumeros.append(primeiroValor)
if(listaNumeros[0] > segundoValor):
    listaNumeros.insert(0, segundoValor)
else:
    listaNumeros.append(segundoValor)

if(terceiroValor < listaNumeros[0]):
    listaNumeros.insert(0, terceiroValor)
elif(terceiroValor < listaNumeros[1]):
    listaNumeros.insert(1, terceiroValor)
else:
    listaNumeros.append(terceiroValor)

print(listaNumeros)