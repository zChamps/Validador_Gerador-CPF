def validadorCPF():
    import re
    import random

    #sys é do sistema do py
    import sys

    while True:
        while True:
            cpf_bruto = re.sub(r"[^0-9]", "", input("Digite o CPF a ser verificado: ") ) 
            if cpf_bruto.isdigit():
                break
            else:
                print("Digite um CPF somente contendo números!")
        
        teste = cpf_bruto.replace(".", "").replace("-", "").replace(",", "").replace(" ", "")
        cpf_sequencial = cpf_bruto == cpf_bruto[0] * len(cpf_bruto)
        if len(teste) < 11 or len(teste) > 11:
            print("O CPF informado não está com a quantia de caracteres correta! Digite novamente.")
            
            continue
        elif cpf_sequencial is True:
            print("CPF digitado não é válido, tem somente 1 número repetido!")
            continue
        else:
            break  
    
    nove_digitos = cpf_bruto[0:9]
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

    cpf_completo = novo_cpf + str_segundo_digito
    cpf_com_ponto = f"{cpf_completo[:3]}.{cpf_completo[3:6]}.\
{cpf_completo[6:9]}-{cpf_completo[9:]}"

    if cpf_completo == cpf_bruto:
        print(f"O CPF {cpf_com_ponto} é válido!")

    else:
        print(f"O CPF {cpf_bruto} não é válido!")