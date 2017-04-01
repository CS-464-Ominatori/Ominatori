#use with command line arguments. 
#arg1- lowerlimit index, arg2- upperlimit index. 
#e.g. 0-10 fetches labels for movies with indices 0 to 9 (inclusive)

from clarifai.rest import ClarifaiApp
import os
import json
import sys

app = ClarifaiApp()
folder = "test" #test or train
path = "C:/Users/burcu/Desktop/Data/_" + folder
listdir = os.listdir(path)
lowerlimit = max(0, int(sys.argv[1]));
upperlimit = min(len(listdir),int(sys.argv[2]));
print("labeling between " + str(lowerlimit) + " and " + str(upperlimit) + " of " + str(len(listdir)) + '\n')
file = open("C:/Users/burcu/Desktop/labels/" +  folder + str(lowerlimit) + "_"+str(upperlimit)+".txt","w")
fileWithNames = open("C:/Users/burcu/Desktop/labels/" +  folder + str(lowerlimit) + "_"+str(upperlimit)+"_names.txt","w") 
batchsize = 128;
for i in range(lowerlimit, upperlimit, batchsize):
	print("starting: " + str(i));
	k = min(batchsize, upperlimit - i); 
	names = [None]*(k)
	urls = [None]*(k)
	for j in range(0, k):	
		dir = listdir[i + j];
		names[j] = dir;
		urls[j] = "http://46.101.173.29/_test/" + dir + "/w342.jpg"
	
	response = app.tag_urls(urls)
	
	for j in range(0, k):
		fileWithNames.write(names[j] + ',')
		for l in range(0, len(response['outputs'][j]['data']['concepts'])):
			label = response['outputs'][j]['data']['concepts'][l]
			file.write(label['name'] + ',' + str(label['value']))
			fileWithNames.write(label['name'] + ',' + str(label['value']))
			if(l < len(response['outputs'][j]['data']['concepts']) - 1):
				file.write(',')
				fileWithNames.write(',')
		file.write('\n');
		fileWithNames.write('\n')
file.close()

