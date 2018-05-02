import deck 

class Hand: 
	values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
             'Queen':10, 'King':10, 'Ace':11}

	def __init__(self):
		self.hand = []
		self.value = 0
		self.aces = 0

	def add_card(self, card):
		self.hand.append(card)

	def determine_aces(self):
		if self.aces > 0: 
			



