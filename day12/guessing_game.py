"""

Conceito do jogo:

Jogo de adivinhação com base em palpítes dos números de 1 à 100.

Se jogar no nível Facil você terá 10 tentativas para adivinhar;
Se jogar no nível Dificil você terá 5 tentativas para adivinhar;

Escopo:

- Precisa ter uma variável que armazene o número aleatório;
- Preciso ter uma variável que armazene o número de tentativas;
- Ao iniciar o jogo irá perguntar se quer jogar no 'facil' ou 'dificil';
- Para cada tentativa irá dizer se chutei um número muito alto ou um numero muito baixo `se chute > x`;
- Se o chute for igual ao numero aleatório, termina o jogo, caso contrario caso a quantidade
de tentativas se esgote o jogo finaliza também;
- Criar de forma modularizada e não tudo numa mesma funcao;
- Se digitar algo que nao seja numero, irá gastar uma tentativa e não ira informar se o chute é ou nao proximo
ao numero

"""

from random import randint
from art import logo

number = randint(0, 100)

def attempts():
    level = input("Select a level of difficulty: (easy) or (hard): ").lower()
    if level == "easy":
        return 10  # easy
    else:
        return 5  # hard

def game():
    print(logo)
    max_attempts = attempts()  # Obtém o número de tentativas com base no nível
    attempts_left = max_attempts  # Inicializa as tentativas restantes

    while attempts_left > 0:
        print(f"You have {attempts_left} attempts remaining to guess the number.")
        user_num = int(input("Guess: "))
        
        if user_num > number:
            print("Too high")
        elif user_num < number:
            print("Too low")
        elif user_num == number:
            print("Correct!")
            return  # Sai do jogo após acertar
        attempts_left -= 1  # Decrementa as tentativas restantes

    print(f"Game Over! The number was {number}.")  # Mensagem quando as tentativas acabam

game()
