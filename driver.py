from player import Player 

class Game: 
	def __init__(self, players = 1):
		self.player_list = []
		self.players = players
		self.player_factory()


	def play_again(self): 
		print("Would you like to play again? ")

	def player_factory(self): 
		for i in range(self.players): 
			self.player_list.append(Player())

	def win(self): 
		print("wtf")
		
			



if __name__ == '__main__':
	game1 = Game(4) 
