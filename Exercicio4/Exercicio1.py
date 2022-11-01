#um programa para calcular as notas obtidas pelo aluno.
#mostrar mensagem para ser digitado anota do 1º, 2º, 3º e 4º bimestre.
#mostrar na tela se o aluno foi aprovado, se está em recuperação ou foi reprovado sem chance de recuperação.
#cada bimestre vale 25 pontos num total anual de 100 pontos.

nota1 = float(input("Primeiro bimestre: "))
nota2 = float(input("Segundo bimestre: "))
nota3 = float(input("terceiro bimestre"))
nota4 = float(input("quarto bimestre "))

print("primeiro bimestre é: ",nota1)
print("segundo bimestre é: ",nota2)
print("terceiro bimestre é: ",nota3)
print("quarto bimestre é: ",nota4)

resultado = (nota1 + nota2 + nota3 + nota4)
print("resultado foi: ", resultado)

if resultado<40:
    print("Reprovado")

elif resultado <60:
    print("reprovado com recuperação")
elif resultado >=60:
    print("Aprovado")