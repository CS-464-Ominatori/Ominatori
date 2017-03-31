#transforms tables into matlab friendly format, enter your own filenames
#to use like this run buildtables first
import os

temp_input = open("./color_features.txt", 'r')
temp_output = open("./truth_with_genreIDs.txt", 'r')
input = open("../bow_inputs.txt", 'w')
output = open("../bow_outputs.txt", 'w')

for line in temp_output:
	input_line = temp_input.readline()
	words = line.rstrip().split(' ')
	for word in words:
		input.write(input_line)
		output.write(word + '\n')

temp_input.close()
temp_output.close()
input.close()
output.close()

print("done")
