class board():

	def __init__(self):
		self.board_state={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
		self.filled_boxes=[]


	def __str__(self):
		message=f"{self.board_state[1]}|{self.board_state[2]}|{self.board_state[3]} \n-+-+-\n{self.board_state[4]}|{self.board_state[5]}|{self.board_state[6]} \n-+-+-\n{self.board_state[7]}|{self.board_state[8]}|{self.board_state[9]}"
		return message

	def update(self,player,position,game):
		self.board_state[position]=player
		self.filled_boxes.append(position)
		print(self)
		self.checking_state(game)

	def checking_state(self,game):
		winning_comb=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
		for comb in winning_comb:
			if self.board_state[comb[0]]==self.board_state[comb[1]]==self.board_state[comb[2]] and self.board_state[comb[0]]!=' ':
				return game.update_scoreline(self.board_state[comb[0]])


		if " " in self.board_state.values():
			game.play(game.whose_turn(),self)
		else:
			b=board()
			game.play(game.whose_turn(),b)




class game():

	def __init__(self,best_of,starting_player,second_player):
		self.best_of=best_of
		self.starting_player=starting_player
		self.second_player=second_player
		self.current_player=self.starting_player
		self.scoreline={self.starting_player:0,self.second_player:0}



	def whose_turn(self):
		if self.current_player==self.starting_player:
			self.current_player=self.second_player
			return self.current_player

		else:
			self.current_player=self.starting_player
			return self.current_player

	def play(self,current_player,dboard):
		try:

			position=int(input(f"Player {current_player} where would you like to fill"))

		except:
			position=int(input(f"Player {current_player} Seems like you provided an invalid number \n where would you like to fill"))

		if position in dboard.filled_boxes:
			print("position already occupied")
			position=int(input(f"Player {current_player} where would you like to fill"))

		elif position not in dboard.board_state:
			print("invalid position , chose btw 1 and 9")
			position=int(input(f"Player {current_player} where would you like to fill"))


		dboard.update(current_player,position,self)

	def update_scoreline(self,winner):
		self.scoreline[winner]+=1
		if self.scoreline[winner]==self.best_of:
			self.end(winner)

		else:
			print(f'NEXT GAME')

			b=board()
			self.play(self.whose_turn(),b)



	def end(self,winner):
		message=f'{winner} wins by {self.scoreline[winner]} : ' 

		print(message)


class player():
	def __init__(self,letter):
		self.letter=letter

	def __str__(self):
		return self.letter

	def __repr__(self):
		return self.letter

instructions=f''' 

WELCOME PLAYERS \n
Read The Instructions Of The Game Carefully \n

1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9

Inorder to plant your letter in any space simply input the number associated with the cell

'''

print(instructions)

print('Are you readyyyyyyy')
print("player 1 ")
player1=input('choose a letter between X and O \nNote: The letter should be capital')
if player1=="X":
	first_player=player('X')
	second_player=player("O")

elif player1=="O":
	first_player=player('O')
	second_player=player("X")



try:
	best=int(input("best of how many"))
except:
	best=int(input("invalid input ,\n integer input only \n best of how many"))


gamee=game(best,first_player,second_player)
board1=board()
gamee.play(first_player,board1)




