#builds tables for bow model (temporary)
#run tomatlab.py after this
import os

dictfile = open("../dictionary.txt", 'r')
dict = []
line = dictfile.readline()[:-1]
words = line.split(',')
for word in words:
	dict.append(word)
dictfile.close()

labels = open("../labels.txt", 'r')
truth = open("../../shared/truth_with_genreIDs.txt", 'r')
input = open("./temp_labels.txt", 'w')
for line in labels:
	words = line.split(',')
	for word in dict:
		if (word in words):
			input.write("1 ")
		else:
			input.write("0 ")
	input.write('\n')
	
labels.close()
truth.close()
input.close()

print("done")
	
	