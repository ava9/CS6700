import random
import copy

class decentAI:

	# check if legal move
	def legal(self, board):
		arr = [0, 0, 0, 0, 0, 0, 0]
		for c in range(0, board.columns):
			if (board.colFull(c + 1)):
				arr[c] = False
			else:
				arr[c] = True
		return arr

	# check 
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
			if replica.colFull(c):
				continue
			else:
				replica.move(player, c)
				ret = self.check(replica, player)
				m[c - 1] = m[c - 1] + ret
			
			if replica.winner(player) != player:
				continue
			else: 
				# arbitrary high number, should test
				m[c - 1] = 10
				return m

			for c2 in range(board.columns):
				if replica.colFull(c2):
					continue
				else:
					replica.move(opp, c2)
					ret = self.check(replica, opp)
					m[c - 1] = m[c - 1] - ret

				if replica.winner(opp) != opp:
					continue
				else: 
					# arbitrary high magnitude numbers, should test
					m[c - 1] = -9
					m[c2 - 1] = 9
					break
				m[c] = m[c] + self.allMoves(replica, player, depth - 1)[c]
		return m

	# choose move to make
	#def chooseMove(self, board, opp, depth):
		# aMoves = self.allMoves(board, opp, depth)
		# maxScore = max(a)
		# legalMoves = self.legal(board)
		# ret = []

		# for c in range(len(legalMoves)):
		# 	if ((maxScore and legalMoves[c]) != aMoves[c]):
		# 		# continue
		# 	else:
		# 		ret.append(c)

		# if (len(ret) > 1):
		# 	# randomly select one of better moves - need to change later
		# 	r = random.randint(0, len(ret) - 1)
		# 	ret = ret[r] + 1
		# else:
		# 	ret = ret[0] + 1

		# return ret
