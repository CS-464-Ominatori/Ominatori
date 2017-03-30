#get ordered list of movies vs ids, enter your own path
import os

listdir = os.listdir("C:/Users/burcu/Desktop/Data")

file = open("../index.txt","w")
for i in range(0, len(listdir)):
	f = open("C:/Users/burcu/Desktop/Data/" + listdir[i] + "/info.txt")
	line = f.readline()
	words = line.split(':')
	file.write(str(i) + "," + listdir[i] + ',' + words[1].rstrip() + '\n')
	f.close()
file.close();

