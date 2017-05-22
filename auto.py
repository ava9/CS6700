#!/usr/bin/python
import os

os.system("mkdir temp")

for i in range(1, 101):
	os.system("cp miniAIb.py temp/")
	os.system("mv temp/miniAIb.py temp/miniAIb"+str(i)+".py")

	os.system("cp minimaxAI.py temp/")
	os.system("mv temp/minimaxAI.py temp/minimaxAI"+str(i)+".py")

	os.system("cp playAIvsAI.py temp/")
	os.system("mv temp/playAIvsAI.py temp/playAIvsAI"+str(i)+".py")

	filedata = open("temp/playAIvsAI"+str(i)+".py", 'r').read()
	filedata = filedata.replace('miniAIb', "miniAIb"+str(i))
	filedata = filedata.replace('minimaxAI', "minimaxAI"+str(i))
	with open("temp/playAIvsAI"+str(i)+".py", 'w') as file:
		file.write(filedata)

	filedata = open("temp/miniAIb"+str(i)+".py", 'r').read()
	filedata = filedata.replace('miniAIb', "miniAIb"+str(i))
	with open("temp/miniAIb"+str(i)+".py", 'w') as file:
		file.write(filedata)

	filedata = open("temp/minimaxAI"+str(i)+".py", 'r').read()
	filedata = filedata.replace('minimaxAI', "minimaxAI"+str(i))
	with open("temp/minimaxAI"+str(i)+".py", 'w') as file:
		file.write(filedata)

os.system("touch temp/output.txt")

for i in range(1, 101):
	if (i == 101):
		os.system("python temp/playAIvsAI"+str(i)+".py >> temp/output.txt")
	else:
		os.system("python temp/playAIvsAI"+str(i)+".py >> temp/output.txt &")

#os.system("fgrep -o "-" temp/output.txt | wc -l")
