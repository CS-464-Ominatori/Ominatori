with open('matlabColorFeatures.txt') as f:
    features = f.readlines()

with open('colorsFromAPI.txt') as f2:
    colors = f2.readlines()

writeFile = open('allColorFeatures.txt', 'w')
for i in range(len(features)):
	writeFile.write( features[i][:-1] + " " + colors[i][:-1] + "\n")  # python will convert \n to os.linesep


writeFile.close()
f.close()



