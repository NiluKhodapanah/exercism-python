"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
def value_of_card(card):
    if card == "J" or card == "Q" or card == "K":
        return 10
    elif card == "A":
        return 1
    else:
        return int(card)

def higher_card(card_one, card_two):
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    elif value_of_card(card_one) < value_of_card(card_two):
        return card_two
    else:
        return (card_one, card_two)
        
def value_of_ace(card_one, card_two):
    if value_of_card(card_one) + value_of_card(card_two) + 11 > 21:
        return 1
    elif card_one == "A" or card_two == "A":
        return 1
    else:
        return 11



def is_blackjack(card_one, card_two):
    black_jack = ["J" ,"Q" ,"K","10"]
    ace_card = ["A"]

    if (card_one in ace_card and card_two in black_jack) or (card_two in ace_card and card_one in black_jack):
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    sum_of_cards  = value_of_card(card_one) + value_of_card(card_two)
    if sum_of_cards in range(9,12):
        return True
    else:
        return False