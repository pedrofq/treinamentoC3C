codigo = 320214
senha = "C3c@9999#"
i = 0 

codigoUsuario = int(input("Digite o código: "))
if(codigoUsuario == codigo):
    senhaUsuario = input("Digite a senha: ")
    if(senhaUsuario == senha):
        print("Acesso permitido")
    else:
        print("Senha incorreta")
else:
    print("Usuário inválido")
    


