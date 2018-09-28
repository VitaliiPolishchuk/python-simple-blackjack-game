class Balance():

	def __init__(self, money = 0):
		self.money = money

	def bet(self):
		'''
		set bet 
		'''
		while True:
			try:
				bet_money = int(input('How much money you want to bet? :'))
			except:
				print('Please Enter integer')
				continue
			if self.money < bet_money:
				print('You can`t allow if\nYou balance is: ' + self.balance)
			else:
				self.bet_money = bet_money
				break

	def win(self):
		'''
		you win bet
		'''
		print('You win $' + str(self.bet_money))
		self.money += self.bet_money

	def lose(self):
		'''
		you lose bet
		'''
		print('You lose $' + str(self.bet_money))
		self.money -= self.bet_money

	def show(self):
		'''
		show balance
		'''
		print('You have $' + str(self.money))