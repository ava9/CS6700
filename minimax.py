import copy
import random
class minimaxAI:
	
	# check if legal move
	def legal(self, board):
		arr = [0, 0, 0, 0, 0, 0, 0]
		for c in range(0, board.columns):
			if (board.colFull(c + 1)):
				arr[c] = False
			else:
				arr[c] = True
		return arr
	
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
			if (not replica.colFull(c)):
				replica.move(player, c)
				ret = self.check(replica, player)
				m[c] = m[c] + ret #m[c - 1] = m[c - 1] + ret
			
			if (replica.winner(player) == player):
				# arbitrary high number, should test
				m[c] = 10 #m[c - 1] = 10
				return m

			for c2 in range(board.columns):
				if (not replica.colFull(c2)):
					replica.move(opp, c2)
					ret = self.check(replica, opp)
					m[c] = m[c] - ret #m[c - 1] = m[c - 1] - ret

				if (replica.winner(opp) == opp):
					# arbitrary high magnitude numbers, should test
					m[c] = -9 #m[c - 1] = -9
					m[c2] = 9 #m[c2 - 1] = -9
					break
				#m[c] = m[c] + self.allMoves(replica, player, depth - 1)[c]
                m[c] = m[c] + self.allMoves(replica, player, depth - 1)[c]
		return m

	def chooseMove(self, board, opp, depth):
		aMoves = self.allMoves(board, opp, depth) 
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