def calcular_gorjeta():
    try:
        valorConta = float(input("Digite o valor da conta\n"))
        porcentagem = float(input("Digite o valor da gorjeta\n"))
        gorjeta = valorConta * (porcentagem / 100)
        valorTotal = valorConta + gorjeta
        print(f"Valor da Gorjeta: R${gorjeta}")
        print(f"Valor total da conta: R${valorTotal}")
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos (use ponto para decimais, ex: 10.50).")