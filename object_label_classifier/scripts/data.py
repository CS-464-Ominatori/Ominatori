import os

genrecount = 21
truthfile = open("../../truth.txt", 'r')
check = open("../../index.txt", 'r')
labelclasses = open("../../bog_classes.txt", 'w')

for line in truthfile:
	checkline = check.readline();
	checkline = checkline.split(',')
	truthvalues = line.split(' ');
	truthvalues[len(truthvalues) - 1] = truthvalues[len(truthvalues) - 1].rstrip();
	if(checkline[2].rstrip() != truthvalues[0].rstrip()):
		print("Error: films ordered differently-" + checkline[2] + '-' + truthvalues[1] + '-')
		exit()
	for i in range(0, genrecount):
		if(str(i+1) in truthvalues):
			labelclasses.write("1 ")
		else:
			labelclasses.write("0 ")
	labelclasses.write("\n")

truthfile.close()
check.close()
labelclasses.close()
print("done")
	