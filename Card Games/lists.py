def get_rounds(number):

    return list((number, number+1, number+2))


def concatenate_rounds(rounds_1, rounds_2):

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):

    return number in rounds


def card_average(hand):

    average = sum(hand)/len(hand)
    return average


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    
    pass

def card_average(hand):

    average = sum(hand)/len(hand)
    return average


def approx_average_is_average(hand):

    average = card_average(hand)
    first_way = (hand[0] + hand[-1])/2
    med = int((len(hand)- 1)/2)
    sec_way = hand[med]

    return average == first_way or average == sec_way

def average_even_is_average_odd(hand):

    even_index = []
    odd_index = []
    for i in range(len(hand)):
        if i % 2 == 0:
            even_index.append(int(hand[i]))
        else:
            odd_index.append(int(hand[i]))
    return card_average(even_index) == card_average(odd_index)




def maybe_double_last(hand):
  
    if hand[-1] == 11:
       hand[-1] = 22
    return hand
