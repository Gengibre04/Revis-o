#Crie um programa em Python que leia um valor inteiro e exiba todos os números
#pares e ímpares no intervalo de 1 a esse valor, separando-os.
#Saída esperada:
#>> Digite um valor inteiro: 10 (input)
#>> Números pares até 10: 2, 4, 6, 8, 10 (output)
#>> Números ímpares até 10: 1, 3, 5, 7, 9 (output)
try:
    # Solicita ao usuário que insira um valor inteiro
    valor = int(input("Digite um valor inteiro: "))

    # Inicializa as listas para armazenar números pares e ímpares
    pares = []
    impares = []

    # Itera sobre o intervalo de 1 até o valor inserido pelo usuário
    for numero in range(1, valor + 1):
        if numero % 2 == 0:  # Verifica se o número é par
            pares.append(str(numero))
        else:  # Caso contrário, o número é ímpar
            impares.append(str(numero))

    # Exibe os números pares e ímpares
    print(f"Números pares até {valor}: {', '.join(pares)}")
    print(f"Números ímpares até {valor}: {', '.join(impares)}")
except ValueError:
    print("digite um número!")

