horaInicio = int(input("Digite a hora de início do jogo: "))
horaFinal = int(input("Digite a hora final do jogo: "))

horasAteMeiaNoite = 24 - horaInicio  #Calculo da hora incial até meia noite
if(horaFinal < horaInicio):  #Se a hora final for menor que a hora de início, o dia virou 
    duracaoJogo = horaFinal + horasAteMeiaNoite
elif(horaFinal > horaInicio):    #Se a hora final for maior que a hora inicial, o dia é o mesmo
    duracaoJogo = horaFinal - horaInicio
else:
    duracaoJogo = 24    #caso horaFinal seja igual a horaInicio, passou 24h

print("Duração do jogo: %d " %(duracaoJogo))