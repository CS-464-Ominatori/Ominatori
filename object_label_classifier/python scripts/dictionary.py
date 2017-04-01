#builds the dictionary using labels.txt 
import os

dict = set()

file = open("../train_object_labels.txt", "r")

for line in file:
	words = line.split(',')
	for i in range(0, len(words), 2):
		dict.add(words[i])
		
file.close()

file = open("../test_object_labels.txt", "r")

for line in file:
	words = line.split(',')
	for i in range(0, len(words), 2):
		dict.add(words[i])
		
file.close()

dictionary = open("../dictionary.txt", "w")

for word in dict:
	dictionary.write(word + ',')

print("dictionary is saved")

