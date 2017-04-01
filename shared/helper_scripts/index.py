#get ordered list of movies vs ids, enter your own path
import os

train_listdir = os.listdir("C:/Users/burcu/Desktop/Data/_train")
test_listdir = os.listdir("C:/Users/burcu/Desktop/Data/_test")

train_file = open("../train_index.txt",'w')
test_file = open("../test_index.txt", 'w')

for i in range(0, len(train_listdir)):
	f = open("C:/Users/burcu/Desktop/Data/_train/" + train_listdir[i] + "/info.txt")
	words = f.readline().split(':')
	train_file.write(str(i) + "," + train_listdir[i] + ',' + words[1].rstrip() + '\n')
	f.close()	
train_file.close();

for i in range(0, len(test_listdir)):
	f = open("C:/Users/burcu/Desktop/Data/_test/" + test_listdir[i] + "/info.txt")
	words = f.readline().split(':')
	test_file.write(str(i) + "," + test_listdir[i] + ',' + words[1].rstrip() + '\n')
	f.close()	
test_file.close();
