#transforms tables into matlab friendly format, enter your own filenames
#to use like this run buildtables first
import os
import math

temp_input = open("../../object_label_classifier/python_scripts/temp_labels.txt", 'r')
temp_output = open("../truth_with_genreIDs.txt", 'r')

datapoints = sum(1 for line in open("../truth_with_genreIDs.txt", 'r'))
genre_count = 21

train_features = open("../../object_label_classifier/train_features.txt", 'w')
train_labels = open("../../object_label_classifier/train_labels.txt", 'w')
test_features = open("../../object_label_classifier/test_features.txt", 'w')
test_labels = open("../../object_label_classifier/test_labels.txt", 'w')

train_datapoints = math.floor(4*datapoints/5)

for i in range(0, train_datapoints):
	line = temp_output.readline()
	input_line = temp_input.readline()
	words = line.rstrip().split(' ')
	for word in words:
		train_features.write(input_line)
		train_labels.write(word + '\n')

for i in range(train_datapoints, datapoints):
	line = temp_output.readline()
	input_line = temp_input.readline()
	words = line.rstrip().split(' ')
	genres = [0]*genre_count
	for word in words:
		genres[int(word.rstrip()) - 1] = 1;
	binary_line = ' '.join(str(e) for e in genres)
	#for word in words:
	test_features.write(input_line)
	test_labels.write(binary_line + '\n')		
		
temp_input.close()
temp_output.close()
train_features.close()
train_labels.close()
test_features.close()
test_features.close()

print("done")
