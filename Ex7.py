idades = {
    "primeiroHomem": int(input("Digite a idade do primeiro homem: ")),
    "segundoHomem": int(input("Digite a idade do segundo homem: ")),
    "primeiraMulher": int(input("Digite a idade da primeira mulher: ")),
    "segundaMulher": int(input("Digite a idade da segunda mulher: "))
}

if(idades.get("primeiroHomem") < idades.get("segundoHomem")):
    homemMaisNovo = idades.get("primeiroHomem")
    homemMaisVelho = idades.get("segundoHomem")
else:
    homemMaisNovo = idades.get("segundoHomem")
    homemMaisVelho = idades.get("primeiroHomem")

if(idades.get("primeiraMulher") < idades.get("segundaMulher")):
    mulherMaisNova = idades.get("primeiraMulher")
    mulherMaisVelha = idades.get("segundaMulher")
else:
    mulherMaisNova = idades.get("segundaMulher")
    mulherMaisVelha = idades.get("primeiraMulher")

somaMulherNovaHomemVelho = mulherMaisNova + homemMaisVelho
produtoMulherVelhaHomemNovo = mulherMaisVelha * homemMaisNovo

print("Soma homem mais velho com mulher mais nova: %d" %(somaMulherNovaHomemVelho))
print("Produto homem mais novo com mulher mais velha: %d" %(produtoMulherVelhaHomemNovo))

