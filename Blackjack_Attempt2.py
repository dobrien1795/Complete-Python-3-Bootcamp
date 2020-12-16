#Blackjack game
#Attempt 2

'''


Game Play
To play a hand of Blackjack the following steps must be followed:

Create a deck of 52 cards
Shuffle the deck
Ask the Player for their bet
Make sure that the Player's bet does not exceed their available chips
Deal two cards to the Dealer and two cards to the Player
Show only one of the Dealer's cards, the other remains hidden
Show both of the Player's cards
Ask the Player if they wish to Hit, and take another card
If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
Determine the winner and adjust the Player's chips accordingly
Ask the Player if they'd like to play again

'''

#Imports

import random

#Global variables

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True
game_on = True
dealer_playing = False
first_chip = True

#Classes

#Card Class
class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

#Deck Class
class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Ca rd(suit,rank))


        #Shuffle the newly created deck
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

#Hand Class
class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,new_card):
        self.cards.append(new_card)
        self.value += values[new_card.rank]
        self.adjust_for_aces()

    def adjust_for_aces(self):
        for card in self.cards:
            if card.rank == 'Ace':
                if self.value > 21:
                    self.value = self.value - 10
                else:
                    continue

    def __str__(self):
        return f'Your hand value is {self.value}'

class Chips():

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet*2

    def lose_bet(self):
        self.total -= self.bet

#Functions

#Player bet input
def take_bet(chips):

    getting_bet = True
    global game_on

    while getting_bet:

        #If plyaer doesn't have enough chips
        if chips.total < 2:
            getting_bet = False
            game_on = False
            break
        else:
            try:
                #Get bet amount from input
                bet = int(input('Please enter your bet, $2 minimum: '))
            except:
                #Not a number
                print('Invalid input')
                continue
            else:
                 if (bet >= 2) and (bet <= chips.total):
                    chips.bet = bet
                    print(f'Bet is {bet}')
                    getting_bet = False
                    break
                 else:
                     print('Invlid chip input')
                     continue


#Taking hit
def hit(deck,hand):

    hand.add_card(deck.deal())

#Player hit or stand action
def hit_or_stand(deck,player_hand):

    #Variable to control loop
    global playing
    global dealer_playing

    while playing:
        try:
            action = input('Do you want to Hit or Stand (H/S)?: ').upper()
        except:
            print('Invalid input')
            continue
        else:
            #Add new card to hand if Hit
            if action =='H':
                hit(deck,player_hand)
                break
            elif action == 'S':
                print('Stand inputted')
                dealer_playing = True
                break
            else:
                print('Invalid Input')
                continue

#Showing cards before end of hand
def show_some(player,dealer):

    print('Player: Your hand value is ' + str(player.value))
    print(f'Dealer: Your first card value is {str(values[dealer.cards[0].rank])}')

#Showing all cards after end of hand
def show_all(player,dealer):

    print('Player: Your hand value is ' + str(player.value))
    print('Dealer: Your hand value is ' + str(dealer.value))


#Check if player busts
def player_bust(hand,chips):

    if hand.value > 21:
        print('You are bust')
        chips.lose_bet()
        return True
    else:
        return False

#Check if dealer busts
def dealer_bust(hand,chips):

    if hand.value > 21:
        print('Dealer is bust')
        chips.win_bet()
        return True
    else:
        return False

def winner(player_hand, dealer_hand,chips):

    if player_hand.value > dealer_hand.value:
        print('Player wins')
        chips.win_bet()
        print('Chips left: ' + str(chips.total))
    elif player_hand.value < dealer_hand.value:
        print('Dealer wins')
        chips.lose_bet()
        print('Chips left: ' + str(chips.total))
    elif player_hand.value == dealer_hand.value:
        push()
        print('Chips left: ' + str(chips.total))

def push():
    print('Its a draw')

while game_on:

    #Opening Statements
    print('Welcome to Blackjack, lets play!')

    #Create new deck
    new_deck = Deck()

    #Deal player cards
    player_hand = Hand()
    player_hand.add_card(new_deck.deal())
    player_hand.add_card(new_deck.deal())

    #Deal dealer cards
    dealer_hand = Hand()
    dealer_hand.add_card(new_deck.deal())
    dealer_hand.add_card(new_deck.deal())

    #Players Chips
    if first_chip == True:
        player_chips = Chips()

    #Get first bet from player
    take_bet(player_chips)

    #Show cards
    show_some(player_hand,dealer_hand)

    while playing:

        #Player hit or stand
        hit_or_stand(new_deck,player_hand)

        #Show cards in between deals
        show_some(player_hand,dealer_hand)

        #Player bust
        if player_bust(player_hand,player_chips) == True:
            show_some(player_hand,dealer_hand)
            playing = False

        #Dealer hit or stand
        while dealer_playing:

            show_all(player_hand, dealer_hand)

            #Dealer hitting less than 17
            if dealer_hand.value < 17:
                dealer_hand.add_card(new_deck.deal())

            #Dealer standing/bust if over 17/21
            elif dealer_hand.value >= 17:
                if dealer_bust(dealer_hand,player_chips) == True:
                    show_all(player_hand, dealer_hand)
                    dealer_playing = False
                    playing = False
                    break
                else:
                    #Show final hands
                    show_all(player_hand,dealer_hand)

                    #Check winner
                    winner(player_hand,dealer_hand,player_chips)
                    dealer_playing = False
                    playing = False
                    break

    #If they don't have enough chips to play again
    print('Your chips balance is: ' + str(player_chips.total))
    if player_chips.total < 2:
        game_on = False
        break

    #Play again?
    again = input('Would you like to play again? (Y/N): ').upper()
    if again == 'Y':
        playing = True
        first_chip = False
    else:
        print('Game over')
        playing = False
        game_on = False
        break
