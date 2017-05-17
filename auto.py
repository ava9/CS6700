#!/usr/bin/python
import os

os.system("mkdir temp")

for i in range(1, 100):
	os.system("cp decentAI.py temp/")
	os.system("mv temp/decentAI.py temp/decentAI"+str(i)+".py")

	os.system("cp minimaxAI.py temp/")
	os.system("mv temp/minimaxAI.py temp/minimaxAI"+str(i)+".py")

	os.system("cp playAIvsAI.py temp/")
	os.system("mv temp/playAIvsAI.py temp/playAIvsAI"+str(i)+".py")

	filedata = open("temp/playAIvsAI"+str(i)+".py", 'r').read()
	filedata = filedata.replace('decentAI', "decentAI"+str(i))
	filedata = filedata.replace('minimaxAI', "minimaxAI"+str(i))
	with open("temp/playAIvsAI"+str(i)+".py", 'w') as file:
		file.write(filedata)

	filedata = open("temp/decentAI"+str(i)+".py", 'r').read()
	filedata = filedata.replace('decentAI', "decentAI"+str(i))
	with open("temp/decentAI"+str(i)+".py", 'w') as file:
		file.write(filedata)

	filedata = open("temp/minimaxAI"+str(i)+".py", 'r').read()
	filedata = filedata.replace('minimaxAI', "minimaxAI"+str(i))
	with open("temp/minimaxAI"+str(i)+".py", 'w') as file:
		file.write(filedata)

os.system("touch temp/output.txt")

for i in range(1, 100):
	if (i == 100):
		os.system("python temp/playAIvsAI"+str(i)+".py >> temp/output.txt")
	else:
		os.system("python temp/playAIvsAI"+str(i)+".py >> temp/output.txt &")