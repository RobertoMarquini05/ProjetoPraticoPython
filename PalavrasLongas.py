def contador_palavras(texto):
    
    palavras_longas = []
    for palavra in texto.split():
        if len(palavra) > 10:
            palavras_longas.append(palavra)

    if (palavras_longas):
        for palavra in palavras_longas:
            print(palavra)
    else:
        print("Nenhuma palavra encontrada !")