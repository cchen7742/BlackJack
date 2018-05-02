from card import Card

class Deck:
	def __init__(self):
		self.deck = []

		for suit in Card.suits:
			for rank in Card.ranks:
				self.deck.append(Card(suit,rank))

	def shuffle_deck(self):
		random.shuffle(self.deck)

	def deal(self):
		return self.deck.pop()



