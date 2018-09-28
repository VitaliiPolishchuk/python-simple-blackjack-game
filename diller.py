class Diller():
	def __init__(self, deck):
		starts_cards = [deck.hit(), deck.hit()]
		self.cards = []
		self.points = 0
		for card in starts_cards:
			self.add(card, deck)

	def add(self, card, deck):
		'''
		add card to diller deck
		'''

		self.cards.append(card)

		if card == 'A':
			if self.points > 10:
				choice_points == 1 
			else: 
				choice_points == 11
			self.points += choice_points
		else:
			self.points += deck.dic_cards[card]

	def show_incognito(self):
		'''
		show diller card 
		'''
		print('Diller cards is: ' + self.cards[0])

	def show(self):
		'''
		show diller deck and point
		'''
		print('Your points is: ' + str(self.points))
		print('Your cards is: ')
		for card in self.cards:
			print(f"'{card}'")

	def game(self, deck):
		'''
		process gameplay diller
		'''
		while True:
			if self.points < 14:
				self.add(deck.hit(), deck)
			else:
				break