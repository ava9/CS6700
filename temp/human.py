from board import board

class humanInput:
	
	# accept a player's move
	def move(self, b, current):
		try:
			valid = False

			while (not valid):
				p = "[O] Player 1: "

				if (current < 0):
					p = "[X] Player 2: "

				print(p + "Choose a column number between 1 and 7")
				col = input()
				
				if (col <= 0):
					print "Please select a column number between 1 and 7"
				else:
					if (col >= 8):
						print "Please select a column number between 1 and 7"
					else:
						b.move(current, col)
						valid = True
						return True
					
		# handle invalid input
		except NameError:
			print "Please only enter a number"

		except SyntaxError:
			print ("Player " +p + ", Please select a column number between 1 and 7")
			print(p+'Pick a column')
				
