import copy
import random
class minimaxAIb52:
	
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



	# checks how many three-in-a-rows there are
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

	# get all moves
	def allMoves(self, board, player, depth):
		m = [0, 0, 0, 0, 0, 0, 0]
		ret = 0
		opp = player * -1

		if (board.boardFull() == True):
			return [0, 0, 0, 0, 0, 0, 0]

		if (depth <= 0):
			return [0, 0, 0, 0, 0, 0, 0]
		

		for c in range(board.columns):
			replica = copy.deepcopy(board)
			if (not replica.colFull(c+1)):
				replica.move(player, c+1)
				ret = self.check(replica, player)
				m[c] = m[c] + ret #m[c - 1] = m[c - 1] + ret
			
			if (replica.winner(player) == player):
				# arbitrary high number, should test
				m[c] = 100 #m[c - 1] = 10
				return m

			for c2 in range(board.columns):
				if (not replica.colFull(c2+1)):
					replica.move(opp, c2+1)
					ret = self.check(replica, opp)
					m[c] = m[c] - ret #m[c - 1] = m[c - 1] - ret

				if (replica.winner(opp) == opp):
					# arbitrary high magnitude numbers, should test
					if c == c2: #then don't do c (because that allows c2 to go on top)
						m[c] = -99
					else:
						m[c] = -99 #m[c - 1] = -9
						m[c2] = 99 #m[c2 - 1] = -9
                        #NOTE: not good to break if c = c2, also could be another case where you should block
						break
				#m[c] = m[c] + self.allMoves(replica, player, depth - 1)[c]
                m[c] = m[c] + self.allMoves(replica, player, depth - 1)[c]
		return m

#this is the minimax alg
	def minimaxMoves(self, board, player, depth):
		m = [0, 0, 0, 0, 0, 0, 0]
		ret = 0
		opp = player * -1

		if (board.boardFull() == True): #this could be a bug later on
			return [0, 0, 0, 0, 0, 0, 0]

		#if (depth <= 0):
		#	return [0, 0, 0, 0, 0, 0, 0]

		for c in range(board.columns):
			replica = copy.deepcopy(board)
			if (not replica.colFull(c+1)):
				replica.move(player, c+1)
				
				if (replica.winner(player) == player): #is this too deterministic?
				# arbitrary high number, should test
					m[c] = 100 #m[c - 1] = 10
					
					#return m
				elif (depth == 0):
					m[c] = self.check2(replica, player) + self.check(replica, player) + self.checkfirstmoves(replica, player)
				
				#elif (depth == 1):
					#m[c] = (-1)*self.check(replica, opp)
				
				else:
					tempm = self.minimaxMoves(replica, opp, depth-1)
					tempval = (-1)*max(tempm) #first take first occurence ( bug ), then take random occurence
					
					
					m[c] = tempval

		return m

		
		
	def chooseMove(self, board, opp, depth):
		aMoves = self.minimaxMoves(board, opp, depth) 
		#print aMoves
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
			ret = arr[0] + 1

		return ret
