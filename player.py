class Player():
	def __init__(self, deck):
		starts_cards = [deck.hit(), deck.hit()]
		self.cards = []
		self.points = 0
		for card in starts_cards:
			self.add(card, deck)
			self.show()

	def add(self, card, deck):
		'''
		add card to player deck
		'''
		if card == 'A':
			while True:
				print("You wonna get 1 or 11 from card 'A'?")
				choice_points = 0
				try:
					choice_points = int(input('Enter your choice, please: '))
				except:
					print('Please, enter integer')
					continue
				else:
					print('You choose: ' + str(choice_points))
					if choice_points == 1 or choice_points == 11:
						self.cards.append(card)
						self.points += choice_points
						break
					else:
						print("Please Enter 1 or 11")
		else:
			self.cards.append(card)
			self.points += deck.dic_cards[card]

	def show(self):
		'''
		show you deck and point
		'''
		print('Your points is: ' + str(self.points))
		print('Your cards is: ')
		for card in self.cards:
			print(f"'{card}'")

	def game(self, deck):
		'''
		process gameplay player
		'''
		while True:
			print("Do you wonna hit or stand")
			player_choice = input("'hit' or 'stand': ")
			if player_choice == "hit":
				self.add(deck.hit(), deck)
				self.show()
			elif player_choice == "stand":
				break