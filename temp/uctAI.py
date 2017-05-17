import copy
import random
import math
from board import board

class uctAI:
	uctTree = {} #empty dictionary where keys are length-42 strings of board and value is [board value from -1 to 1, # visits to this node]
	currnode = ""
	numsteps = 0
    
	# check if legal move
	def legal(self, board):
		arr = [0, 0, 0, 0, 0, 0, 0]
		for c in range(0, board.columns):
			if (board.colFull(c + 1)):
				arr[c] = False
			else:
				arr[c] = True
		return arr
	
	def checkfirstmoves(self, board, player):
		b = board.getBoard()
		ret = 0
        
		if b[3][0] == player:
			ret = ret + .2
		if b[2][0] != ((-1)*player):
			ret = ret + .05
		if b[4][0] != ((-1)*player):
			ret = ret + .05
			
		return ret
        
    
	# checks how many two-in-a-rows there are
	def check2(self, board, player):
		b = board.getBoard()
		ret = 0

		#vertical check
		for c in range(len(b)): 
			for r in range(len(b[c]) - 2): 
				if (b[c][r] == player):
					if (b[c][r+1] == player):
						
						ret = ret + .5
					else: 
						continue
				else:
					continue
				
		#horizontal check
		for c in range(len(b) - 2): 
			for r in range(len(b[c])): 
				if (b[c][r] == player):
					if (b[c+1][r] == player):
						ret = ret + .5
					else: 
						continue
				else:
					continue
				
		#left to right, bottom to top / diagonal check
		for c in range(len(b) - 2): 
			for r in range(len(b) - 3): 
				if (b[c][r] == player):
					if (b[c+1][r+1] == player):
						
						ret = ret + .5	
					else: 
						continue
				else:
					continue

		#left to right, top to bottom \ diagonal check
		for c in range(len(b) - 1, 1, -1): 
			for r in range(len(b[c]) - 2): 
				if (b[c][r] == player):
					if (b[c-1][r+1] == player):
						ret = ret + .5
					else: 
						continue
				else:
					continue
		return ret
    
    
	# checks how many three-in-a-rows there are, one board eval function
	def check(self, board, player):
		b = board.getBoard()
		ret = 0

		#vertical check
		for c in range(len(b)): 
			for r in range(len(b[c]) - 3): 
				if (b[c][r] == player):
					if (b[c][r+1] == player):
						if (b[c][r+2] == player):
							ret = ret + 1
						else: 
							continue
					else:
						continue
				else:
					continue

		#horizontal check
		for c in range(len(b) - 3): 
			for r in range(len(b[c])): 
				if (b[c][r] == player):
					if (b[c+1][r] == player):
						if (b[c+2][r] == player):
							ret = ret + 1
						else: 
							continue
					else:
						continue
				else:
					continue

		#left to right, bottom to top / diagonal check
		for c in range(len(b) - 3): 
			for r in range(len(b) - 4): 
				if (b[c][r] == player):
					if (b[c+1][r+1] == player):
						if (b[c+2][r+2] == player):
							ret = ret + 1	
						else: 
							continue
					else:
						continue
				else:
					continue

		#left to right, top to bottom \ diagonal check
		for c in range(len(b) - 1, 2, -1): 
			for r in range(len(b[c]) - 3): 
				if (b[c][r] == player):
					if (b[c-1][r+1] == player):
						if (b[c-2][r+2] == player):
							ret = ret + 1
						else: 
							continue
					else:
						continue
				else:
					continue
		return ret

#####################################DONE WITH CHECK FUNCTIONS###########################		
		
	def writeTree(self):
		with open("uctTree.txt", "wb") as tree_doc:
			for key in self.uctTree:
				tree_doc.write(key + "  " + str(self.uctTree[key][0]) + "\n")

	def uctMoves(self, Board, player, depth):
		#try this, new tree each time
		self.uctTree = {}
		#
		nodelist = []
		nodelist.append(Board.tostring())
		currboard = Board
		
		Boardval = self.check(Board, player) + self.check2(Board, player) + self.checkfirstmoves(Board, player)
		normBoardval = Boardval/float(100)
		
		self.uctTree[Board.tostring()] = [normBoardval, 1]
		replica = copy.deepcopy(Board)
		
		iters = 0
		while (iters < 220):
			#if nodelist has odd length, look for upper bound, else look for lower bound
			#print currboard.columns #DEBUG 
			lMoves = self.legal(currboard) #all legal moves
			childlist = []
			indexlist = []
        
			for col in range(currboard.columns):
				replica = copy.deepcopy(currboard) 
				if lMoves[col]: #meaning it's true
					replica.move(player, col+1)
					childlist.append(replica.tostring()) 
					indexlist.append(col)
					
					
			#BUG BUG BUG WHAT IF THERE ARE NO LEGAL MOVES	OKAY FIXED 
			if len(childlist) == 0:
				#then the board is full and it's a draw (val = 0)
				#print "NO LEGAL MOVES"
				
				self.backpropogate(nodelist, 0)
				
				
				iters += 1
				self.numsteps = self.numsteps + 1
				
				currboard = Board #(the original)
				
				nodelist = []
				nodelist.append(Board.tostring())
				continue
			
			chosenchild = ""
			chosenindex = 0
			
			maxval = -100 #or is there a better value to put this as? min should be -1 (WHEN LOOKING FOR UPPER BOUND, simulate uctAI)
			minval = 100 #(WHEN LOOKING FOR LOWER CONFIDENCE BOUND, simulate opponent)
			
			unexplored = 0
			for ch in childlist:
				if not ch in self.uctTree: # TODO too deterministic, actually it's fine
					#unexplored += 1
					chosenchild = ch
					chosenindex = indexlist[childlist.index(ch)]
					break
				
				else: #choose node with highest value if nodelist has odd number elements, else choose node with lowest value 
					
					if (len(nodelist)%2) == 1: #odd, so find highest value
						if ( self.uctTree[ch][0] + math.sqrt(float(self.numsteps)/self.uctTree[ch][1]) ) > maxval:
							maxval = self.uctTree[ch][0] + math.sqrt(float(self.numsteps)/self.uctTree[ch][1])
							chosenchild = ch
							chosenindex = indexlist[childlist.index(ch)]
					
					else: #even, so find lowest value
						#CHECK ON THIS BECAUE IT WAS JUST COPY PASTE
						if ( self.uctTree[ch][0] + math.sqrt(float(self.numsteps)/self.uctTree[ch][1]) ) < minval:
							minval = self.uctTree[ch][0] + math.sqrt(float(self.numsteps)/self.uctTree[ch][1])
							chosenchild = ch
							chosenindex = indexlist[childlist.index(ch)]
			
			#if unexplored > 0:
			#	randindex = random.randint(0, unexplored-1)
			#	chosenchild = childlist[randindex]
			#	chosenindex = indexlist[randindex]
					
			if chosenchild == "":
				print "ERROR NO CHILD CHOSEN"
            
        
			if not chosenchild in self.uctTree:
				
				newboard = board(7,6)
				newboard.copyBoard(Board.toboard(chosenchild))
				normQval = 0
				
				#check if board is win state or lose state, else use board eval function
				if (newboard.winner(player) == player):
					normQval = 1
				elif (newboard.winner((-1)*player) == (-1)*player):
					normQval = -1
				else:	
					Qval = self.check(newboard, player) + self.check2(newboard, player) + self.checkfirstmoves(newboard, player)
					normQval = Qval/float(100)
				
				self.uctTree[chosenchild] = [normQval, 1]
			
				# now update everything back up the tree using the nodelist
				self.backpropogate(nodelist, normQval)
				
				iters += 1
				self.numsteps = self.numsteps + 1
				
				currboard = Board #(the original)
				
				nodelist = []
				nodelist.append(Board.tostring())
				
			else: 
				#take this new board and explore deeper
				nodelist.append(chosenchild)
				
				newboard = board(7,6)
				newboard.copyBoard(Board.toboard(chosenchild))
				currboard = newboard
				
				
        
		#NEED TO DO THIS WHERE IT LOOKS AT ALL CHILDREN AND TAKES MAX
		
		lMoves = self.legal(Board) #all legal moves
		childlist = []
		indexlist = []
        
		for col in range(Board.columns):
			replica = copy.deepcopy(Board) #TODO move this inside loop
			if lMoves[col]: #meaning it's true
				replica.move(player, col+1)
				childlist.append(replica.tostring()) 
				indexlist.append(col)
					
					
		if len(childlist) == 0:
			print "NO LEGAL MOVES 2"
			
		chosenchild = ""
		chosenindex = 0
			
		maxval = -100 #or is there a better value to put this as? min should be -1 (WHEN LOOKING FOR UPPER BOUND, simulate uctAI)
			
		for ch in childlist:
			if ( self.uctTree[ch][0] + math.sqrt(float(self.numsteps)/self.uctTree[ch][1]) ) > maxval: #use UCB or Q(s)??
				maxval = self.uctTree[ch][0] + math.sqrt(float(self.numsteps)/self.uctTree[ch][1])
				chosenchild = ch
				chosenindex = indexlist[childlist.index(ch)]
					
		if chosenchild == "":
			print "ERROR NO CHILD CHOSEN"
            
		
		return chosenindex+1
        
	def backpropogate(self, nodelist, val):
		#for each node in nodelist, update with newest val
		for n in nodelist:
			oldQ = self.uctTree[n][0]
			newQ = oldQ + (val-oldQ)/float(self.uctTree[n][1])
			self.uctTree[n][0] = oldQ
			self.uctTree[n][1] = self.uctTree[n][1] + 1
		
		
		
        
		#get all possible (legal) moves
        #if one hasn't been explored, do that (pick random or in order), random playout or baord eval, add to tree
        #propagate value back up the tree (update all nodes traversed)
        
    
	def chooseMove(self, board, opp, depth):
		'''aMoves = self.allMoves(board, opp, depth) 
		maxScore = max(aMoves)
		lMoves = self.legal(board)       
		arr = []

		for c in range(len(lMoves)):
			if ((lMoves[c] and maxScore) == aMoves[c]):
				arr.append(c)

		if (len(arr) > 1):
			# randomly select one of better moves - need to change later
			r = random.randint(0, len(arr) - 1)
			ret = arr[r] + 1
		else:
			ret = arr[0] + 1'''

		return self.uctMoves(board, opp, depth)