import os
import json
import colorgram

path = "/../../Users/berceste/Desktop/Data2"
listdir = os.listdir(path)
print("extracting fundamental 6 colors from all images " + '\n')
file = open("/Users/berceste/Desktop/colors/colorsFromAPI2.txt","w")fileWithNames = open("/Users/berceste/Desktop/colors/colorsFromAPINames2.txt","w")

for i in range(0, len(listdir)):
        print("starting: " + str(i))
        names = [None]*(len(listdir))
        dir = listdir[i]
        names[i] = dir
        colors = colorgram.extract("/Users/berceste/Desktop/Data2/" + dir + "/w342.jpg", 6)
        #print(colors)

        fileWithNames.write(names[i] + ',')

        for l in range(0, len(colors)):
                rgb = colors[l].rgb
                file.write(str(rgb[0]) + " " + str(rgb[1]) + " " + str(rgb[2]) + " ")
                fileWithNames.write(str(rgb[0]) + " " + str(rgb[1]) + " " + str(rgb[2]) + " ")
        file.write('\n')
        fileWithNames.write('\n')

file.close()
fileWithNames.close()