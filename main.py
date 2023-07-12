from gerador_CPF import geradorCPF
from validador_CPF import validadorCPF

while True:
    principal = input("Olá! Você deseja gerar ou validar um CPF? ")

    if principal.lower() == "gerar":
        while True:
            try:
                numero = int(input("Quantos CPF's deseja gerar? "))
                geradorCPF(numero)
            except ValueError:
                print("Digite um número válido!")
                continue

    elif principal.lower() == "validar":
        validadorCPF()

    elif principal.lower() == "sair":
        print("Aplicação fechada!")
        break

    else:
        print("Digite uma opção válida!")
        continue