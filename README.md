# Forca-gpt
Jogo da forca usando chat GPT
Um joguinho simples usando o chat GPT primeira pedi para mostrar como ter palavras aleatorias ou pseudo aletorias e o codigo dado foi.

# Primeiro, instale uma biblioteca para obter uma lista de palavras
!pip install english_words

import random
from english_words import english_words_set

# Converter o conjunto para uma lista para facilitar a escolha aleatória
word_list = list(english_words_set)

# Escolher uma palavra aleatória
random_word = random.choice(word_list)

print("Palavra aleatória:", random_word)

porem queria palavras em portugues o que me gerou esse segundo codigo

# Se necessário, instale a biblioteca nltk para trabalhar com palavras
!pip install nltk

import random
import nltk
from nltk.corpus import words

# Baixar o corpus de palavras em inglês (usaremos para português)
nltk.download('words')

# Usaremos palavras em português
portuguese_words = [word for word in words.words() if word.isalpha()]

# Escolher uma palavra aleatória
random_word = random.choice(portuguese_words)

print("Palavra aleatória em português:", random_word)

e por fim pedi para criar um jogo da forca com palavras aleatorias.


import random

# Lista de palavras em português (pode ser carregada de um arquivo)
palavras = ["python", "jogador", "programador", "computador", "sistema", "linguagem"]

# Escolher uma palavra aleatória
palavra_secreta = random.choice(palavras)

# Criação de uma lista para rastrear o estado das letras adivinhadas
estado_palavra = ["_" for _ in palavra_secreta]

# Número máximo de tentativas
tentativas_restantes = 6

# Conjunto para rastrear letras já adivinhadas
letras_usadas = set()

print("Bem-vindo ao jogo da forca!")
print("A palavra tem", len(palavra_secreta), "letras.")

# Loop principal do jogo
while tentativas_restantes > 0:
    # Mostrar o estado atual da palavra
    print(" ".join(estado_palavra))
    
    # Entrada do jogador
    letra = input("Adivinhe uma letra: ").lower()

    # Verificar se a letra já foi adivinhada
    if letra in letras_usadas:
        print("Você já adivinhou essa letra. Tente outra.")
        continue
    
    letras_usadas.add(letra)

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

Dai foi so "juntar" os codigos e fazer umas alterações como mostrar letras chutadas (o que demorou um bom tempo), e para sempre também sempre ter palavras maisculas ja ele não reconhece palavras maiscula, porem não consegui resolver o pproblemas das palavras escolhidas que ainda vem em inglês.


