"""Program to mimic the game of Blackjack"""


# Create a deck of cards


def create_deck():
    """function that creates a 52-card deck of playing cards"""

    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # Create a dictionary with suits as keys and Ace through to King as values
    deck = {suit: cards.copy() for suit in suits}
    return deck


def deal(deck):
    """Deals a card from a deck.\nReturns a tuple containing card face and value as str"""

    import random
    suit = random.choice([x for x in deck])
    card = random.choice(deck[suit])
    deck[suit].remove(card)

    return suit, card


def value_card(card, hand):
    """Takes a card an returns it's value as an int"""
    face = card[-1]
    if face == "J" or face == "Q" or face == "K":
        value = 10
    elif face == "A":
        value = 11

    else:
        value = int(face)
    return value


def hand_value(hand):
    """Evaluates the score of a hand"""
    value = 0
    for x in hand:
        value += value_card(x, hand)
    return value


def initial_deal(hand, deck):
    """Deals two cards to a hand"""
    for i in range(2):
        hand.append(deal(deck))


def compare_hands(h1, h2):
    if h1 > h2:
        return "Player 1"
    elif h1 < h2:
        return "Computer"
    else:
        return "Tie"


def show_hand(hand):
    """Shows hand in readable format"""
    formatted_hand = ""

    for card in hand:
        formatted_hand += card[-1] + " of " + card[0] + " "
    return formatted_hand


def hit_me(hand, deck):
    """Option to deal card"""
    hand.append(deal(deck))


def winner(h1, h2):
    """Takes two hands and returns the winner"""

    score1 = hand_value(h1)
    score2 = hand_value(h2)

    if score2 < score1 <= 21:
        return "Player Wins"
    elif score1 < score2 <= 21:
        return "Dealer Wins"
    elif score1 == score2 <= 21:
        return "Tie. Dealer Wins"
    elif score1 > 21:
        return "Player Bust. Dealer Wins"
    elif score2 > 21:
        return "Dealer Bust. Player Wins"


def play_game():
    """Runs the game of Blackjack"""

    # Create the playing deck
    playing_deck = create_deck()

    # Two empty lists to populate with cards for the hands of the players
    player_hand = []
    comp_hand = []

    # Deal 2 cards to each player
    initial_deal(player_hand, playing_deck)
    initial_deal(comp_hand, playing_deck)

    print(show_hand(player_hand))

    player_turn = True
    while player_turn:
        if hand_value(player_hand) > 21:
            print("Player Bust")
            break
        choice = input("Would you like another card? (y/n) ")
        if choice == "y":
            card = deal(playing_deck)
            player_hand.append(card)
            print(show_hand(player_hand))
        else:
            player_turn = False
    print(f"Player's hand {show_hand(player_hand)}")

    comp_turn = True
    while comp_turn:
        print(f"Dealer's hand {show_hand(comp_hand)}")
        if hand_value(player_hand) > 21:
            comp_turn = False
        elif hand_value(comp_hand) < 17:
            card = deal(playing_deck)
            comp_hand.append(card)
        else:
            comp_turn = False

    print(winner(player_hand, comp_hand))


play_game()
