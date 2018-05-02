class Chips: 
	def __init__(self, bank = 100): 
		self.bank = bank  
		self.bet = 0

	def win_bet(self): 
		self.bank += self.bet

	def lose_bet(self): 
		self.bank -= self.bet 
		

