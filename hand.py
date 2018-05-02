from card import Card

class Hand: 
	def __init__(self):
		self.hand = []
		self.value = 0
		self.aces = 0

	def __str__(self):
		cards = '' 
		for i in self.hand:
			cards += str(i) + ', '
		return cards

	def add_card(self, card):
		self.hand.append(card)
		self.value += card.values[card.rank]
		if card.rank == 'Ace': 
			self.adjust_for_ace()


	def adjust_for_ace(self):
		if self.value > 21:
			self.value -= 10 




