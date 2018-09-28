from random import randint
from deck import Deck
from balance import Balance
from diller import Diller
from player import Player

deck = Deck()

balance = Balance(100)

end_game = False

while not end_game:
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')

    balance.bet()

    player = Player(deck)
    diller = Diller(deck)

    deck.show_deck_incognito(player, diller, balance)

    for game_process in [player, diller]:
	    game_process.game(deck)

    deck.result(player, diller, balance)

    if not deck.replay():
	    end_game = True