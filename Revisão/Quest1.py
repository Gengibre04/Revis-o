#Desenvolva um algoritmo em Python que receba 3 notas e faça a média. O 
#sistema deverá exibir:- Aprovado: se a média for maior ou igual a 7;- Reposição: se a média for menor que 7 mas maior ou igual a 4;- Reprovado: se a média for menor que 4
num1 = (float(input("Digite a primeira média:")))
num2 = (float(input("Digite a segunda média:")))
num3 = (float(input("Digite e terceira média:")))

if num1 + num2 + num3 / 3 >= 7:
    print("reposição")
elif num1 + num2 + num3 / 3 < 7:
    print("Reprovado")