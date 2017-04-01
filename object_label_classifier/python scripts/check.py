#checks if movies in train_labels.txt is ordered correctly
#check if labels.txt and labels-with-names.txt has the same values
#check if dictionary has all the words in labels.txt
import os

dictionary = open("../dictionary.txt", "r")

dict = []
dictWords = dictionary.readline().split(',')
for word in dictWords:
	dict.append(word)
dictionary.close()

train_labels_with_names = open("../train_object_labels_with_names.txt", "r")
train_index = open("../../shared/train_index.txt", "r")
train_labels = open("../train_object_labels.txt", "r") 
for line in train_index:
	words = line.split(',')
	namesWords = train_labels_with_names.readline().split(',')
	labelWords = train_labels.readline().split(',')
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
			
train_labels_with_names.close()
train_index.close()
train_labels.close()

test_labels_with_names = open("../test_object_labels_with_names.txt", "r")
test_index = open("../../shared/test_index.txt", "r")
test_labels = open("../test_object_labels.txt", "r") 
for line in test_index:
	words = line.split(',')
	namesWords = test_labels_with_names.readline().split(',')
	labelWords = test_labels.readline().split(',')
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
			
test_labels_with_names.close()
test_index.close()
test_labels.close()

numlines = sum(1 for line in open('../train_object_labels_with_names.txt')) 
print(str(numlines))
numlines = sum(1 for line in open('../../shared/train_index.txt'))
print(str(numlines))
numlines = sum(1 for line in open('../train_object_labels.txt')) 
print(str(numlines))
numlines = sum(1 for line in open('../../shared/train_truth_with_genreIDs.txt')) 
print(str(numlines))
numlines = sum(1 for line in open('../../shared/test_index.txt'))
print(str(numlines))
numlines = sum(1 for line in open('../test_object_labels_with_names.txt')) 
print(str(numlines))
numlines = sum(1 for line in open('../test_object_labels.txt')) 
print(str(numlines))
numlines = sum(1 for line in open('../../shared/test_truth_with_genreIDs.txt')) 
print(str(numlines))