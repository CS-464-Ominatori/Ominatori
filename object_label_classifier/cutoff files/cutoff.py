import sys
import os
import math

cutoff = sys.argv[1]
cutoffF = float(sys.argv[1])

dictfile = open("../dictionary.txt", 'r')
dict = []
line = dictfile.readline()[:-1]
words = line.split(',')
for word in words:
	dict.append(word)
dictfile.close()

labels = open("../train_object_labels.txt", 'r')
input = open("./temp_train_object_labels_cutoff_" + cutoff + ".txt", 'w')
for line in labels:
	all_words = line.split(',')
	words = []
	for x in range(0, len(all_words), 2):
		if(float(all_words[x + 1])>cutoffF):
			words.append(all_words[x])
			
	for word in dict:
		if (word in words):
			input.write("1 ")
		else:
			input.write("0 ")
	input.write('\n')
	
labels.close()
input.close()

labels = open("../test_object_labels.txt", 'r')
input = open("./temp_test_object_labels_cutoff_" + cutoff + ".txt", 'w')
for line in labels:
	words = line.split(',')
	for word in dict:
		if (word in words):
			input.write("1 ")
		else:
			input.write("0 ")
	input.write('\n')	
labels.close()
input.close()

print("building temp files done")
	
genre_count = 19

train_datapoints = sum(1 for line in open("../../shared/train_truth_with_genreIDs.txt", 'r'))
temp_train_input = open("./temp_train_object_labels_cutoff_" + cutoff + ".txt", 'r')
temp_train_output = open("../../shared/train_truth_with_genreIDs.txt", 'r')

train_features = open("./train_features_cutoff_"+cutoff+".txt", 'w')
train_labels = open("./train_labels_cutoff_"+cutoff+".txt", 'w')

for i in range(0, train_datapoints):
	line = temp_train_output.readline()
	input_line = temp_train_input.readline()
	words = line.rstrip().split(' ')
	for word in words:
		train_features.write(input_line)
		train_labels.write(word + '\n')
		
temp_train_input.close()
temp_train_output.close()
train_features.close()
train_labels.close()	

test_datapoints = sum(1 for line in open("../../shared/test_truth_with_genreIDs.txt", 'r'))
temp_test_input = open("./temp_test_object_labels_cutoff_" + cutoff + ".txt", 'r')
temp_test_output = open("../../shared/test_truth_with_genreIDs.txt", 'r')

test_features = open("./test_features_cutoff_"+cutoff+".txt", 'w')
test_labels = open("./test_labels_cutoff_"+cutoff+".txt", 'w')

for i in range(0, test_datapoints):
	line = temp_test_output.readline()
	input_line = temp_test_input.readline()
	words = line.rstrip().split(' ')
	genres = [0]*genre_count
	for word in words:
		genres[int(word.rstrip()) - 1] = 1
	binary_line = ' '.join(str(e) for e in genres)
	test_features.write(input_line)
	test_labels.write(binary_line + '\n')	
		
temp_test_input.close()
temp_test_output.close()
test_features.close()
test_labels.close()	

os.remove("./temp_test_object_labels_cutoff_" + cutoff + ".txt")
os.remove("./temp_train_object_labels_cutoff_" + cutoff + ".txt")
print("building matlab files done")