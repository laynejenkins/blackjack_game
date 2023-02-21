import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    random_card = random.randint(0, len(cards)-1)
    return cards[random_card]


while True:
    dealer_total = 0
    player_total = 0
    actual_dealer_hand = []
    player_hand = []
    # starting hand (2 cards each)
    actual_dealer_hand.append(deal_card())
    actual_dealer_hand.append(deal_card())
    player_hand.append(deal_card())
    player_hand.append(deal_card())
    # TODO == display 2nd+ card as '*' in displayed hand
    # displayed_dealer_hand = actual_dealer_hand[1:] = '*'
    print(f"Dealer has: {actual_dealer_hand}")
    print(f"Your hand: {player_hand}")
    # determine immediate blackjack
    for card in actual_dealer_hand:
        dealer_total += card
    for card in player_hand:
        player_total += card
    if dealer_total == 21 and player_total == 21:
        print('Tied blackjack!')
        break
    elif dealer_total == 21 and player_total != 21:
        print('House has a blackjack! House wins!')
        break
    elif player_total == 21:
        print('You got a blackjack, you win!')
        break
    # see if player wants to hit or stay. They bust if they go over and game ends.
    while True:
        player_hit_stay = input("Hit or stay?\n").lower()
        if player_hit_stay == "hit":
            player_total = 0
            player_hand.append(deal_card())
            for card in player_hand:
                player_total += card
            print(f"Your hand: {player_hand}. Total = {player_total}")
            if player_total > 21:
                print("You bust!")
                break
        else:
            break
    if player_total > 21:
        break
    # see if house hits or stays
    print(f"Dealer has: {actual_dealer_hand}")
    while dealer_total <= 16:
        dealer_total = 0
        actual_dealer_hand.append(deal_card())
        print("Dealer draws!")
        print(f"Dealer has: {actual_dealer_hand}")
        for card in actual_dealer_hand:
            dealer_total += card
        if dealer_total > 21:
            print("House busts! You win!")
            break
    if dealer_total > 21:
        break
    # determine if house or player wins. End game.
    if dealer_total == player_total:
        print('Push!')
        break
    elif dealer_total > player_total:
        print('House wins!')
        break
    else:
        print('You win!')
        break
