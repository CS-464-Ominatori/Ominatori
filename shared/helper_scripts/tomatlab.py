#transforms tables into matlab friendly format, enter your own filenames
#to use like this run buildtables first
import os
import math

genre_count = 19

train_datapoints = sum(1 for line in open("../train_truth_with_genreIDs.txt", 'r'))
temp_train_input = open("../../object_label_classifier/python_scripts/temp_train_object_labels.txt", 'r')
temp_train_output = open("../train_truth_with_genreIDs.txt", 'r')

train_features = open("../../object_label_classifier/train_features.txt", 'w')
train_labels = open("../../object_label_classifier/train_labels.txt", 'w')

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

test_datapoints = sum(1 for line in open("../test_truth_with_genreIDs.txt", 'r'))
temp_test_input = open("../../object_label_classifier/python_scripts/temp_test_object_labels.txt", 'r')
temp_test_output = open("../test_truth_with_genreIDs.txt", 'r')

test_features = open("../../object_label_classifier/test_features.txt", 'w')
test_labels = open("../../object_label_classifier/test_labels.txt", 'w')

for i in range(0, test_datapoints):
	line = temp_test_output.readline()
	input_line = temp_test_input.readline()
	words = line.rstrip().split(' ')
	genres = [0]*genre_count
	for word in words:
		genres[int(word.rstrip()) - 1] = 1;
	binary_line = ' '.join(str(e) for e in genres)
	test_features.write(input_line)
	test_labels.write(binary_line + '\n')	
		
temp_test_input.close()
temp_test_output.close()
test_features.close()
test_labels.close()	

print("done")
