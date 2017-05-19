from board import board
from human import humanInput
from decentAI75 import decentAI75
from randomAI import randomAI
from inorderAI import inorderAI
from minimaxAI75 import minimaxAI75
from uctAI import uctAI
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

	def begin(self, whoGoesFirst):
		#print "Would you like to go first? Enter: [y/n]"

		#note that if user enters anything other than "n", user goes first
		if (whoGoesFirst == 1):
			valid = True
			self.current = self.p2

		ai = True
		if (ai == True):
			opp = decentAI75() #1
			opp2 = minimaxAI75() #-1
			depth = 2
			depth2 = 4

		while(self.win == 0):
			self.b.update()
			if (ai == True):
				if (self.current < 0):
					#print "--------AI 2's Move-------"
					# 1
					self.b.move(self.current, opp2.chooseMove(self.b, self.current, depth2))
				elif (self.current > 0):

					self.b.move(self.current, opp.chooseMove(self.b, self.current, depth))
					valid = True
					#print "------AI 1's Move------"
					# -1
			elif not ai:
				valid = True

			self.win = self.b.winner(self.current)
			if (valid == False):
				continue
			else:
				self.current = self.current * -1

		self.b.update()
		# update print statement to print ai/user won
		
		#print opp.uctTree
		#opp.writeTree()
		#print"The winner is "
		print self.win

# playAgain = True
# count = 0
# while(playAgain == True):
# 	count = count + 1
p = play()
# 	if (count <=50):
p.begin(0)
# 	else:
# 		p.begin(1)
# 	#print "Would you like to play again? Enter: [y/n]"
	
# 	#note that if user enters anything other than "n", user plays again
# 	#if (raw_input() == "n"):
# 		#playAgain = False
# 	if (count > 100):
# 		playAgain = False
# 	else:
p.b.setUp()











