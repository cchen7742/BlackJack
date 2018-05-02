class Card: 

	suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
	ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 
			'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
	
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		

	def __str__(self):
		return self.rank + ' of ' self.suit 

		
		
