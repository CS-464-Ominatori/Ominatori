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

labels = open("../train_object_labels.txt", 'r')
truth = open("../../shared/train_truth_with_genreIDs.txt", 'r')
input = open("./temp_train_object_labels.txt", 'w')
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

labels = open("../test_object_labels.txt", 'r')
truth = open("../../shared/test_truth_with_genreIDs.txt", 'r')
input = open("./temp_test_object_labels.txt", 'w')
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
	
	