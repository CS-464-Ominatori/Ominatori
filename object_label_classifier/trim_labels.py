import sys
import os

labels = open("./train_object_labels.txt", 'r')
input = open("./clarifai_values_temp.txt", 'w')

for line in labels:
	words = line.split(',')
	for x in range(1, len(words), 2):
		input.write(words[x] + ",")	
input.write("\n")
labels.close()
input.close()

file = open("./clarifai_values_temp.txt", 'r')
input = open("./clarifai_values.txt", 'w')
for line in file:
    line = line.strip()
    input.write(line)
file.close()
input.close()

os.remove("./clarifai_values_temp.txt")