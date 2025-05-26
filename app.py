import CalculadorGorjeta, PedraPapelTestoura, ValidadorCPF, ContadorVogais, PalavrasLongas, GerarSenha, AdivinharNumero, Calculadora, GerenciadorTarefas, ContadorCedulas

print("1- Calculador de gorjeta")
print("2- Validar CPF")
print("3 - Contador vogais")
print("4 - Contador palavras longas")
print("5 - Gerar Senha")
print("6 - Pedra/Papel/Tesoura")
print("7 - Adivinhar o Numero")
print("8 - Calculadora")
print("9 - Gerenciador de Tarefas")
print("10 - Contador de Cedulas")
print("0 - Sair")

opcaoEscolhida = input("Digite qual projeto deseja rodar\n")

match opcaoEscolhida:
    case "1":
        CalculadorGorjeta.calcular_gorjeta()
    case "2":
        ValidadorCPF.validate_CPF()
    case "3":
        texto = input("Digite o texto para contar as vogais\n")
        ContadorVogais.contador_vogais(texto)
    case "4":
        texto = input("Digite as palavras que deseja realizar a conta\n")
        PalavrasLongas.contador_palavras(texto)
    case "5":
        GerarSenha.gerar_senha()
    case "6":
        PedraPapelTestoura.jogar()
    case "7":
        AdivinharNumero.jogar()
    case "8":
        Calculadora.calculadora()
    case "9":
        GerenciadorTarefas.gerenciador_tarefas()
    case "10":
        ContadorCedulas.caixa_eletronico()