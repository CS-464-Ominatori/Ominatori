#checks if movies in labels.txt is ordered correctly
#check if labels.txt and labels-with-names.txt has the same values
#check if dictionary has all the words in labels.txt
import os

labelsWithNames = open("../../labels-with-names.txt", "r")
index = open("../../index.txt", "r")
labels = open("../../labels.txt", "r") 
dictionary = open("../../dictionary.txt", "r")

dict = []
l = dictionary.readline();
dictWords = l.split(',')
for word in dictWords:
	dict.append(word)

for line in index:
	labelsWithNamesLine = labelsWithNames.readline();
	namesWords = labelsWithNamesLine.split(',')
	labelsLine = labels.readline()
	labelWords = labelsLine.split(',')
	words = line.split(',')
	if(words[1].rstrip() != namesWords[0]):
		print("ERROR not in index with-" + namesWords[0] + "-vs-" + words[1] + '-')
		exit();
	for i in range(0, len(namesWords) - 1):
		if(namesWords[i + 1] != labelWords[i]):
			print("ERROR not the same with-" + namesWords[i + 1] + "-vs-" + labelWords[i] + '-')
			exit();
		if(i%2 == 0 and labelWords[i] not in dict):
			print("ERROR not in dictionary with-"+labelWords[i]+'-')
			exit();
			
labelsWithNames.close()
index.close()
labels.close()

numlines = sum(1 for line in open('../../labels-with-names.txt')) 
print("no of lines in labels: " + str(numlines))
numlines = sum(1 for line in open('../../index.txt'))
print("no of lines in index: " + str(numlines))
numlines = sum(1 for line in open('../../labels.txt'))
print("no of lines in labels-with-names: " + str(numlines))		
print("note: no of lines doesn't include the final empty line")	