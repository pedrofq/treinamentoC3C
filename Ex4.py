salarioFixo = float(input("Digite o salário do funcionário: "))
valorVendas = float(input("Digite o valor das vendas do funcionário: "))

if(valorVendas <= 1500):
    valorComissao = 0.03*valorVendas
else:
    valorComissao = 0.05*valorVendas

salarioTotal = salarioFixo + valorComissao

print("O salário total do funcionário foi de %.2f" %(salarioTotal))