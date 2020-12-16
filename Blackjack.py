#This is my Milestone Project 2 game
#Blackjack

'''

One player vs dealer/Computer

Player can stand or hit
Player can pick their betting amount
Keep track of players total money
Alert the player for win/loss/bust

'''

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
player_stick = False
game_on = True

#Card class
#Each card needs to have a number and suit
class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

#Deck class
#Create a new deck and shuffle
class Deck():

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:

                #Create each card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

        #Shuffle the deck
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

#Player class
#Create a new player and allow them to store the bank
#Hold cards and get the value of those cards
class Player():

    def __init__(self):
        self.hand = []
        self.current_bet = 0
        self.bank = 100

    def get_hand_value(self):

        my_value = 0

        for c in self.hand:
            my_value += c.value

            #Check for Aces
            if (c.value == 11) and (my_value > 21):
                my_value = my_value - 10

        print('Players hand value is {my_value}'.format(my_value=my_value))
        return my_value


    def add_card(self,new_card):
        self.hand.append(new_card)
        print(f'Players new card is: {new_card}')

    def clear_hand(self):
        self.hand.clear()

    def __str__(self):
        return f'Player bank is {str(self.bank)}'

    def add_bet(self,my_bet):
        self.current_bet += my_bet

    def clear_bet(self):
        self.current_bet = 0

    def add_winnings(self, win_num):
        self.bank += win_num
        print(f'Player bank is {self.bank}')


#Dealer class is similar to Player
#No bank
class Dealer():

    def __init__(self):
        self.hand = []

    def add_card(self,new_card):
        self.hand.append(new_card)

    def clear_hand(self):
        self.hand.clear()

    def get_hand_value(self):
        self.my_value = 0

        for c in self.hand:
            self.my_value += c.value

            #Check for Aces
            if (c.value == 11) and (my_value > 21):
                my_value = my_value - 10

        print('Dealers hand value is {my_value}'.format(my_value=self.my_value))



#Game on
'''
New deck
Bets at start
Deal everyone 2 cards at start
Calculate total after each deal
Get action from players
Interpret action and decide if bust
Do dealer action
Determine the result of that round
Repeat if possible
'''

def check_round_over(player_in, b=None):
    if b == 'Blackjack':
        print('Congratulations you have 21!')
        player1.add_winnings(player_in.current_bet*2)





print('Welcome to Blackjack!')
new_deck = Deck()
player1 = Player()
print(f'Your player is ready')
print(player1)
dealer = Dealer()
print('Dealer is ready')
print('Lets lose some money!')


while game_on:

    round_on = True
    while round_on:



        #Get players bet
        getting_player_bet = True
        while getting_player_bet == True:

            if (player1.bank < 2):
                print('You do not have enough money, game over.')
                quit()

            else:
                #Check for a valid input
                try:

                    player_bet = int(input('Player input bet (min 2$ & whole number): '))

                    if (player_bet > player1.bank) or (player_bet < 2):
                        print('That is not a valid number for a bet')
                        continue

                    elif (player_bet >= 2) and (player_bet <= player1.bank):
                        print('Your bet for this round is {}'.format(str(player_bet)))
                        player_bet = False
                        break

                #if they don't enter a number
                except:
                    print('Thats invalid')

        #Deal initial cards
        ace1 = Card('Hearts', 'Ace')
        ace2 = Card('Diamonds', 'Jack')

        player1.add_card(ace1)
        dealer.add_card(new_deck.deal_one())
        player1.add_card(ace2)
        dealer.add_card(new_deck.deal_one())

        pvalue = player1.get_hand_value()
        print(pvalue)
        if pvalue == 21:
            check_round_over(player1, 'Blackjack')


        print(f'Dealers first card value is {dealer.hand[0].value}')

        #Action & gameplay

        #while (player_stick == False) and (pvalue <= 21)

        print('Round over')
        round_on = False

    print('Test end')
    game_on = False


#Sort and accept player action
#Automate dealer action
