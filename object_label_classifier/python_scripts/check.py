#checks if movies in labels.txt is ordered correctly
#check if labels.txt and labels-with-names.txt has the same values
#check if dictionary has all the words in labels.txt
#check if truth and index are ordered the same
import os

labelsWithNames = open("../labels_with_names.txt", "r")
index = open("../../shared/index.txt", "r")
labels = open("../labels.txt", "r") 
dictionary = open("../dictionary.txt", "r")
truth = open("../../shared/truth_with_movieID_and_genreIDs.txt", 'r')

dict = []
dictWords = dictionary.readline().split(',')
for word in dictWords:
	dict.append(word)
dictionary.close()

for line in index:
	words = line.split(',')
	namesWords = labelsWithNames.readline().split(',')
	labelWords = labels.readline().split(',')
	truthwords = truth.readline().split(' ')
	if(words[1].rstrip() != namesWords[0]):
		print("ERROR not in index with-" + namesWords[0] + "-vs-" + words[1] + '-')
		exit();
	if(words[2].rstrip() != truthwords[0]):
		print("ERROR wrong order with-" + truthwords[0] + '-' + words[2] + '-')
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
truth.close()

numlines = sum(1 for line in open('../labels_with_names.txt')) 
print("no of lines in labels: " + str(numlines))
numlines = sum(1 for line in open('../../shared/index.txt'))
print("no of lines in index: " + str(numlines))
numlines = sum(1 for line in open('../labels.txt'))
print("no of lines in labels-with-names: " + str(numlines))		
print("note: no of lines doesn't include the final empty line")	