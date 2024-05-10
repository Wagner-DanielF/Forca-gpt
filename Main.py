import random
import nltk
from nltk.corpus import words

# Baixar o corpus de palavras em inglês (usaremos para português)
nltk.download('words')

# Usaremos palavras em português
portuguese_words = [word.lower() for word in words.words() if word.isalpha()]

# Escolher uma palavra aleatória
palavra_secreta = random.choice(portuguese_words)

#print("Palavra aleatória em português:", palavra_secreta)

# Criação de uma lista para rastrear o estado das letras adivinhadas
estado_palavra = ["_" for _ in palavra_secreta]

# Número máximo de tentativas
tentativas_restantes = 6

# Conjunto para rastrear letras já adivinhadas
letras_chutadas = set()

print("Bem-vindo ao jogo da forca!")
print("A palavra tem", len(palavra_secreta), "letras.")

# Loop principal do jogo
while tentativas_restantes > 0:
    # Mostrar o estado atual da palavra
    print(" ".join(estado_palavra))

    # Mostrar letras já chutadas
    if letras_chutadas:
        print("Letras já chutadas:", ", ".join(sorted(letras_chutadas)))
    else:
        print("Nenhuma letra chutada ainda.")

    # Entrada do jogador
    letra = input("Adivinhe uma letra: ").lower()

    # Verificar se a letra já foi adivinhada
    if letra in letras_chutadas:
        print("Você já adivinhou essa letra. Tente outra.")
        continue

    letras_chutadas.add(letra)

    # Verificar se a letra está na palavra secreta
    if letra in palavra_secreta:
        print("Bom trabalho! A letra", letra, "está na palavra.")

        # Atualizar o estado da palavra
        for i, char in enumerate(palavra_secreta):
            if char == letra:
                estado_palavra[i] = letra

        # Verificar se o jogador ganhou
        if "_" not in estado_palavra:
            print("Parabéns! Você adivinhou a palavra:", palavra_secreta)
            break
    else:
        tentativas_restantes -= 1
        print("Ops! A letra", letra, "não está na palavra. Você tem", tentativas_restantes, "tentativas restantes.")

# Verificar se o jogador perdeu
if tentativas_restantes == 0:
    print("Você perdeu! A palavra era:", palavra_secreta)
