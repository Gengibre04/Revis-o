#Você foi designado para desenvolver um programa que converta temperaturas 
#entre diferentes escalas. Suas tarefas são as seguintes:
def celsius_para_fahrenheit(celsius):
    """Converte Celsius para Fahrenheit usando a fórmula: Fahrenheit = (Celsius * 9/5) + 32."""
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    """Converte Fahrenheit para Celsius usando a fórmula: Celsius = (Fahrenheit - 32) * 5/9."""
    return (fahrenheit - 32) * 5/9

def mostrar_menu():
    """Exibe o menu de opções para o usuário."""
    print("Escolha uma opção de conversão:")
    print("1. Converter de Celsius para Fahrenheit")
    print("2. Converter de Fahrenheit para Celsius")

# Programa principal
mostrar_menu()
opcao = input("Digite o número da opção desejada: ")

if opcao == '1':
    # Converte de Celsius para Fahrenheit
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"{celsius}°C é igual a {fahrenheit}°F")

elif opcao == '2':
    # Converte de Fahrenheit para Celsius
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit}°F é igual a {celsius}°C")

else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")
    