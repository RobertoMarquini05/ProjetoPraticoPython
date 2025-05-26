def validate_CPF():
    cpf = (input("Digite o CPF a ser validado\n"))
    
    if (len(cpf) != 11):
        print("CPF inválido: Deve conter 11 digitos")
        return
    elif not cpf.isdigit():
        print("CPF inválido: deve conter apenas números.")
        return
    else:
        print("CPF Válido !")
    
