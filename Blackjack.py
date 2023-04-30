import random
from art_blackjack import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(l1):
    if sum(l1) == 21 and len(l1)==2:
        return 0  #user or a computer has got a score of blackjack

    if 11 in l1 and sum(l1)>21:
        l1.remove(11)
        l1.append(1)

    return sum(l1)

def compare(user_score, computer_score):
    if user_score==computer_score:
        return "Draw"
    elif computer_score==0:
        return "Lose, computer has Blackjack"
    elif user_score==0:
        return "Win, you have Blackjack"
    elif user_score>21:
        return "You went over, you lose"
    elif computer_score>21:
        return "Computer went over, you win"
    elif user_score>computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over=False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21: #user or computer has blackjack or the user lost since he has score
                                                               # >21 so the game will end
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to get another card, type 'n' to pass")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n'") == "y":
    play_game()

