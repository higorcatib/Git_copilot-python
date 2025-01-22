# vamos solicitar dois números e depois vamos somar ele dando a opção para usuário de qual operacao ele quer fazer 

# Solicita o primeiro número ao usuário
numero1 = float(input("Digite o primeiro número: "))

# Solicita o segundo número ao usuário
numero2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada ao usuário
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Realiza a operação escolhida pelo usuário
if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    if numero2 != 0:  # Verifica se o divisor não é zero
        resultado = numero1 / numero2
    else:
        resultado = "Erro: Divisão por zero não é permitida."
else:
    resultado = "Operação inválida."

# Imprime o resultado
print("Resultado:", resultado)
