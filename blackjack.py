import random


def play_jack():
    stop_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    from art import logo
    print(logo)
    result = True
    com_card = []
    my_card = []
    n = 0
    my_score = 0
    com_score = 0
    while result:
        if stop_game == 'y':
            n = n + 1
            cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
            my_card.append(random.choice(cards))
            my_card.append(random.choice(cards))
            com_card.append(random.choice(cards))
            com_card.append(random.choice(cards))
            for blackjack in my_card:
                if blackjack == 11:
                    print("You win!!!")
                    result = False
            for blackjack in com_card:
                if blackjack == 11:
                    print("You lose!!")
                    result = False
            my_score = my_score + my_card[n-1] + my_card[n]
            com_score = com_score + com_card[n-1] + com_card[n]
            print(f"Your card: {my_card}, current score: {my_score}")
            print(f"Computer's first card: {com_card}, score = {com_score}")
            print()
            if my_score > 21:
                print("You lose!")
                result = False
            if com_score > 21:
                print("You win")
                result = False
            stop_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
        elif stop_game == 'n':
            result = False
        else:
            print('Invalid enter')
play_jack()
