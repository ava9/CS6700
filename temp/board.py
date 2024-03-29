class board:
	columns = 0
	rows = 0
	array = []

	# init
	def __init__(self, col, row):
		self.columns = col
		self.rows = row
		self.setUp()

	# set up board
	def setUp(self):
		self.array = []

		for c in range(self.columns):
			self.array.append([0]*self.rows)
			
	def copyBoard(self, inarray):
		self.array = inarray
		
		

	# get board
	def getBoard(self):
		return self.array

	# check if column is full
	def colFull(self, col): 
		#print col #DEBUG
		if (self.array[col - 1][self.rows - 1] == 0): 
			return False 
		return True

	# check if board is full
	def boardFull(self): 
		for c in range(1, self.columns): 
			if (self.colFull(c)):
				continue
			else:
				return False
		return True

	# make board into length 42 string
	def tostring(self):
		s = ""
		for r in range(self.rows):
			for c in range(self.columns):
				if (self.getBoard()[c][r] == -1):
					s = s + "X"
				elif (self.getBoard()[c][r] == 1):
					s = s + "O"
				elif (self.getBoard()[c][r] == 0):
					s = s + "."
				else:
					continue
		return s                
            
	def toboard(self, str):
		#lol forget the "self" and convert the string to a board
		newb = [[0 for _ in range(self.rows)] for _ in range(self.columns)]
		strind = 0
		if len(str) != 42:
			print "ERROR string must be length 42"
        
		for r in range(self.rows):
			for c in range(self.columns):
				if str[strind] == "X":
					newb[c][r] = -1
				elif str[strind] == "O":
					newb[c][r] = 1
                    
				strind += 1
                
		return newb    
        
        
    # update board
	def update(self):
		arr = ['1 2 3 4 5 6 7']
		n = ""

		for r in range(0, self.rows):
			for c in range(0, self.columns):
				if (self.getBoard()[c][r] == -1):
					n = n + "X "
				else:
					if (self.getBoard()[c][r] == 1):
						n = n + "O "
					else:
						if (self.getBoard()[c][r] == 0):
							n = n + ". "
						else:
							continue
			arr.append(n)
			n = ""

		#for s in range(len(arr)):
			#print arr.pop(-1)

	# insert player move on board
	def move(self, player, col):
		c = col - 1

		for r in range(0, self.rows):
			if (self.array[c][r] != 0):
				continue
			else:
				self.array[c][r] = player
				return

	# check for winner
	def winner(self, player):
		b = self.getBoard()

		#vertical check
		for c in range(len(b)): 
			for r in range(len(b[c]) - 3): 
				if (b[c][r] == player):
					if (b[c][r+1] == player):
						if (b[c][r+2] == player):
							if (b[c][r+3] == player):
								return player
							else:
								continue
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
							if (b[c+3][r] == player):
								return player
							else:
								continue
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
							if (b[c+3][r+3] == player):
								return player
							else:
								continue
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
							if (b[c-3][r+3] == player):
								return player
							else:
								continue
						else: 
							continue
					else:
						continue
				else:
					continue
		return 0

