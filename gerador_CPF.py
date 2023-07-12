

def geradorCPF(a):
    import random
    import pyperclip

    cpfs = []

    for i in range(a):
        nove_digitos = ""
        for i in range(0, 9):
            nove_digitos += str(random.randint(0, 9))





        multiplicacao1 = 10
        soma = 0
        soma2 = 0

        for numero in nove_digitos:
            resultado = int(numero) * multiplicacao1
            multiplicacao1 -= 1
            soma += resultado

        resto = (soma * 10)%11
        resto1 = resto > 9
        primeiro_digito = 0 if resto1 is True else resto



        str_primeiro_digito = str(primeiro_digito)
        novo_cpf = nove_digitos + str_primeiro_digito
        multiplicacao2 = 11

        for numero2 in novo_cpf:
            resultado2 = int(numero2) * multiplicacao2
            multiplicacao2 -= 1
            soma2 += resultado2

        resto2 = (soma2 * 10)%11
        resto3 = resto2 > 9
        segundo_digito = 0 if resto3 is True else resto2
        str_segundo_digito = str(segundo_digito)
        dois_digitos = str(primeiro_digito) + str(segundo_digito)
        cpf_inteiro = nove_digitos + dois_digitos

        pyperclip.copy(cpf_inteiro)
        print(cpf_inteiro)