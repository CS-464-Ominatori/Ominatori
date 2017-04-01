
import os
import json
import colorgram

path = "/Users/berceste/Desktop/Data"
listdir = os.listdir(path)
lowerlimit = max(0, int(sys.argv[1]));
upperlimit = min(len(listdir),int(sys.argv[2]));
print("labeling between " + str(lowerlimit) + " and " + str(upperlimit) + " of " + str(len(listdir)) + '\n')
file = open("/Users/berceste/Desktop/colors/" + str(lowerlimit) + "-"+str(upperlimit)+".txt","w")
fileWithNames = open("/Users/berceste/Desktop/colors/" + str(lowerlimit) + "-"+str(upperlimit)+"-names.txt","w") 
batchsize = 128;

for i in range(lowerlimit, upperlimit, batchsize):
	print("starting: " + str(i));
	k = min(batchsize, upperlimit - i); 
	names = [None]*(k)
	urls = [None]*(k)
	for j in range(0, k):	
		dir = listdir[i + j];
		names[j] = dir;
		colors = colorgram.extract(dir + "/w342.jpg", 6)
		print(colors)
		
		fileWithNames.write(names[j] + ',')
		listOfColors = str.split("<")
		for l in range(0, len(listOfColors)):
			start = l.index('(');
			end = l.index(')');
			color = l[start + 1, end] 
			file.write(color + ',')
			fileWithNames.write(color + ',')
		file.write('\n');
		fileWithNames.write('\n')
	
file.close()
