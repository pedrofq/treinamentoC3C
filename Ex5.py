qntAtualEstoque = int(input("Digite a quantidade do estoque atual: "))
qntMaximaEstoque = int(input("Digite a quantidade máxima em estoque: "))
qntMinimaEstoque = int(input("Digite a quantidade mínima em estoque: "))

qntMediaEstoque = (qntMaximaEstoque + qntMinimaEstoque)/2

if(qntAtualEstoque >= qntMediaEstoque):
    print("Não efetuar compra")
else:
    print("Efetuar compra")
