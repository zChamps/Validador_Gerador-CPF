Bem vindo(a)! Esse projeto consiste em um verificador de válidade e/ou criação
de CPFs válidos.

Processo para verificar a válidade de um CPF:


1 - Verificar se o CPF possui exatamente 11 dígitos.

2 - Verificar se todos os dígitos do CPF não são iguais.

3 - Cálculo do primeiro dígito verificador do CPF:
    -Pegue os primeiros nove dígitos do CPF.
    -Multiplique cada dígito pelos fatores de 10 a 2, respectivamente.
    -Some os resultados das multiplicações.
    -Divida a soma por 11 e obtenha o resto.
    -Se o resto for igual a 0 ou 1, o primeiro dígito verificador deve ser 0. 
     Caso contrário, subtraia o resto de 11 para obter o primeiro dígito 
     verificador.

4 - Cálculo do segundo dígito verificador do CPF:
    -Pegue os primeiros dez dígitos do CPF (incluindo o primeiro dígito 
     verificador calculado).
    -Multiplique cada dígito pelos fatores de 11 a 2, respectivamente.
    -Some os resultados das multiplicações.
    -Divida a soma por 11 e obtenha o resto.
    -Se o resto for igual a 0 ou 1, o segundo dígito verificador deve ser 0. 
     Caso contrário, subtraia o resto de 11 para obter o segundo dígito 
     verificador.

5 - Se todas as etapas acima forem concluídas com sucesso, o CPF é considerado válido.