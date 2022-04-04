primeiraAvaliacao = float(input("Digite a nota de primeira avaliação: "))
segundaAvaliacao = float(input("Digite a nota da segunda avaliação: "))

notasAvaliacoes ={
    "primeiraAvaliacao": primeiraAvaliacao,
    "segundaAvaliacao": segundaAvaliacao
}


mediaAvaliacoes = (notasAvaliacoes.get("primeiraAvaliacao") + notasAvaliacoes.get("segundaAvaliacao"))/2

if(mediaAvaliacoes >= 7):
    print("Aprovado! Média: %.2f" %(mediaAvaliacoes))
else:
      print("Reprovado! Média: %.2f" %(mediaAvaliacoes))
