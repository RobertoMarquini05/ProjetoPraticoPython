def contador_vogais(texto):
    vogais = "aeiou"
    contador = 0
    for letra in texto.lower():
        if letra in vogais:  
            contador += 1
        
    print(f"O texto possuí: {contador} vogais")