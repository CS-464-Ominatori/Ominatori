#creates the input and output for matlab
import os

dictfile = open("../../dictionary.txt", 'r')
dict = []
line = dictfile.readline()
words = line.split(',')
for word in words:
	dict.append(word)
dictfile.close()

labels = open("../../labels.txt", 'r')
truth = open("../../truth.txt", 'r')
input = open("../../bow_inputs.txt", 'w')
output = open("../../bow_outputs.txt", 'w')
for line in labels:
	words = line.split(',')
	for word in dict:
		if (word in words):
			input.write("1 ")
		else:
			input.write("0 ")
	input.write('\n')
	tr = truth.readline().split(' ')
	for i in range(1, len(tr)):
		output.write(tr[i].rstrip() + " ")
	output.write('\n')
	
labels.close()
truth.close()
input.close()
output.close()

print("done")
	
	