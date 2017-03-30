#sample class used to combine partial lists
#strips labels before writing bc clarifai returned trailing spaces in one word (automated to be safe)
import os
f = [None]*6;
f2 = [None]*6;
f[0] = "0-256-names.txt"
f[1] = "256-2176-names.txt"
f[2] = "2176-2200-names.txt"
f[3] = "2200-4000-names.txt"
f[4] = "4000-4500-names.txt"
f[5] = "4500-5354-names.txt"
f2[0] = "0-256.txt"
f2[1] = "256-2176.txt"
f2[2] = "2176-2200.txt"
f2[3] = "2200-4000.txt"
f2[4] = "4000-4500.txt"
f2[5] = "4500-5354.txt"

path = "C:/Users/burcu/Desktop/labels/"

wName = open("../../labels-with-names.txt", "w")
wF = open("../../labels.txt", "w")

for i in range(0,6):
	file = open(path + f[i],"r")
	for line in file:
		words = line.split(',')
		for j in range(0, len(words)):
			word = words[j]
			wName.write(word.rstrip());
			if(j < len(words) - 1):
				wName.write(',')
		wName.write('\n')
	file.close();
	file2 = open(path + f2[i])
	for line in file2:
		words = line.split(',')
		for j in range(0, len(words)):
			word = words[j]
			wF.write(word.rstrip());
			if(j < len(words) - 1):
				wF.write(',')
		wF.write('\n')
	
wName.close();
wF.close();
