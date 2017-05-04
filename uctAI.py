import copy
import random
class uctAI:
	uctTree = {} #empty dictionary where keys are length-42 strings of board and value is board value from -1 to 1
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

	def writeTree(self):
		with open("uctTree.txt", "wb") as tree_doc:
			for key in self.uctTree:
				tree_doc.write(key + "  " + str(self.uctTree[key]) + "\n")

	def uctMoves(self, board, player, depth):
		m = [0, 0, 0, 0, 0, 0, 0]
		nodelist = []
		
		replica = copy.deepcopy(board)
		lMoves = self.legal(board) #all legal moves
		childlist = []
		indexlist = []
		for col in range(board.columns):
			replica = copy.deepcopy(board) #TODO move this inside loop
			if lMoves[col]: #meaning it's true
				replica.move(player, col+1)
				childlist.append(replica.tostring()) #WRONG, BUG, must append board with the move taken
				indexlist.append(col)
				
		chosenchild = ""
		chosenindex = 0
		maxval = -10 #or is there a better value to put this as? min should be -1
		for ch in childlist:
			if not ch in self.uctTree: # TODO too deterministic
				chosenchild = ch
				chosenindex = indexlist[childlist.index(ch)]
				break
			else: #choose node with highest value 
				if self.uctTree[ch] > maxval:
					maxval = self.uctTree[ch]
					chosenchild = ch
					chosenindex = indexlist[childlist.index(ch)]
		if chosenchild == "":
			print "ERROR NO CHILD CHOSEN"
            
        #if chosenchild has a value, then just update the move counts, update currnode, propagate back up tree
        
		if not chosenchild in self.uctTree:
			#then add with board eval function
			self.uctTree[chosenchild] = self.check(board, player) #BUG, doesn't include current move
        
        #m[chosenindex] = 1
		#return m
		return chosenindex+1
        
        
        
        #if self.currnode == "":
        #    .......(7).......(14).......(21).......(28).......(35).......(42)
        
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