from hand import Hand 
from chips import Chips 
from deck import Deck
from card import Card

class Player(Hand, Chips):

	def __init__(self, bank = 100): 
		Hand.__init__(self) 
		Chips.__init__(self, bank)

	def hit(self, card): 
		self.add_card(card)
		print(self)
		print('Total value: {}'.format(self.value))

	def stay(self) 
		continue 


if __name__ == '__main__':
	player1 = Player() 
	player1.hit(Card('Two','Hearts'))
	player1.hit(Card('Ace','Hearts'))




