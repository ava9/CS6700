from board import Board

class input:
	def move(self, b, player):
		try:
			valid = False

			while (valid == False):
				player = "[O] Player 1: "
				
				if player >= 0:
					continue
				else:
					p = "[X] Player 2: "
				
				print(p + "Choose a column number between 1 and 7")
				col = input()

				if (col <= 0):
					print "Please select a column number between 1 and 7"
				else:
					if (col >= 8):
						print "Please select a column number between 1 and 7"
					else:
						b.move(player, col)
						valid = True
						return True
		except NameError:
			print "Please only enter a number"

		except SyntaxError:
			print ("Player " +player + ", Please select a column number between 1 and 7")

