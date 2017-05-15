from board import board
from human import humanInput
from decentAI import decentAI
from randomAI import randomAI
from inorderAI import inorderAI
from minimaxAI import minimaxAI
from uctAI import uctAI
from uctAIrp import uctAIrp 
import random

class play:
	p1 = 1
	p2 = -1
	current = p1
	win = 0
	userInput = humanInput()
	b = board(7, 6)

	def __init__(self):
		self.current = self.p1
		self.win = 0

	def begin(self):
		print "Would you like to go first? Enter: [y/n]"

		#note that if user enters anything other than "n", user goes first
		if (raw_input() == "n"):
			valid = True
			self.current = self.p2

		ai = True
		if (ai == True):
			opp = uctAIrp()
			depth = 3
			
		draw = 0	
		while(self.win == 0):
			self.b.update()
			if self.b.boardFull() == True:
				draw = 1
				break
			
			if (ai == True):
				if (self.current < 0):
					print "--------AI's Move-------"
					#print "sdfsfsf"
					self.b.move(self.current, opp.chooseMove(self.b, self.current, depth))
				elif (self.current > 0):
					valid = self.userInput.move(self.b, self.current)
					print "------Human's Move------"
			elif not ai:
				valid = self.userInput.move(self.b, self.current)

			self.win = self.b.winner(self.current)
			if (valid == False):
				continue
			else:
				self.current = self.current * -1

		self.b.update()
		# update print statement to print ai/user won
		
		#print opp.uctTree
		#opp.writeTree()
		if draw == 1:
			print "Draw - No Winner"
		else:	
			print"The winner is "
			print self.win

playAgain = True
while(playAgain == True):
	p = play()
	p.begin()
	print "Would you like to play again? Enter: [y/n]"
	
	#note that if user enters anything other than "n", user plays again
	if (raw_input() == "n"):
		playAgain = False
	p.b.setUp()	










