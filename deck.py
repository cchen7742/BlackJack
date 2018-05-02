import card
import random 


class Deck:
	def __init__(self):
		self.deck = []
		for suit in card.suits
			for rank in card.rank
				self.deck.append(Card(suit,rank))

	def shuffle_deck(self):
		random.shuffle(self.deck)

	def deal(self):
		return self.deck.pop()
		


