from random import randint

class Deck():

	#for i in self.cards 27 times. Check error

	dic_cards = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
	cards_sample = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'A'] * 4

	def __init__(self):
		self.cards = self.cards_sample

	def hit(self):
		'''
		return random card from deck
		'''
		num_card = randint(0, len(self.cards) - 1)
		return self.cards.pop(num_card)

	def show_deck(self, player, diller, balance):
		'''
		show player, diller deck and player balance
		'''
		player.show()
		diller.show()
		balance.show()

	def show_deck_incognito(self, player, diller, balance):
		'''
		show player deck, diller card and player balance
		'''
		diller.show_incognito()
		balance.show()

	def result(self, player, diller, balance):
		'''
		show resulr end of round
		'''

		self.show_deck(player, diller, balance)

		print('You have cards sum: ' + str(player.points))
		print('Diller has cards sum: ' + str(diller.points))

		if player.points > 21:
			balance.lose()
		elif diller.points > 21:
			balance.win()
		elif player.points > diller.points:
			balance.win()
		else:
			balance.lose()

	def fill_cards(self):
		'''
		fill deck if it necessary
		'''
		if len(self.cards) < 8:
			print("Recreate cards")
			self.cards_sample = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'A'] * 4
			self.cards = self.cards_sample
	def replay(self):
		'''
		ask to replay
		'''
		self.fill_cards()
		while True:
			player_choice = input('Do you wonna play again?')
			if player_choice == "yes":
				return True
			elif player_choice == "no":
				return False