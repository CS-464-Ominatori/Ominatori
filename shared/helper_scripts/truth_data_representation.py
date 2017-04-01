import os

# Constants
my_path = "C:/Users/burcu/Desktop/Data"
ID_prefix = "ID:"
title_prefix = "Title:"
genre_prefix = "Genres:"

ACTION = 1
ADVENTURE = 2
ANIMATION = 3
COMEDY = 4
CRIME = 5
DOCUMENTARY = 6
DRAMA = 7
FAMILY = 8
FANTASY = 9
HISTORY = 10
HORROR = 11
MUSIC = 12
MYSTERY = 13
ROMANCE = 14
SCIFI = 15
TVMOVIE = 16
THRILLER = 17
WAR = 18
WESTERN = 19

train_listdir = os.listdir(my_path + '/_train/')
train_output_file = open("../train_truth_with_genreIDs.txt", "w")

# Get all the info.txt files for every  train movie
for dir in train_listdir:
    try:
        file_name = "%s\_train\%s\info.txt" % (my_path, dir)  # File to read
        entry_line = ""  # Entry string for output file
        for line in open(file_name):
            # if line[:3] == ID_prefix:
                # entry_line += line[3:-1] + " "
            # elif line[:6] == title_prefix:
            #     entry_line += line[6:-1] + ','
            if line[:7] == genre_prefix:
                genres = line[7:].split() # Convert genre to ID
                genreIDs = set()
                for genre in genres:
                    genre = genre.lower()
                    if genre == "action":
                        genreIDs.add(ACTION)
                    elif genre == "adventure":
                        genreIDs.add(ADVENTURE)
                    elif genre == "animation":
                        genreIDs.add(ANIMATION)
                    elif genre == "comedy":
                        genreIDs.add(COMEDY)
                    elif genre == "crime": 
                        genreIDs.add(CRIME)
                    elif genre == "documentary":
                        genreIDs.add(DOCUMENTARY)
                    elif genre == "drama":
                        genreIDs.add(DRAMA)
                    elif genre == "family":
                        genreIDs.add(FAMILY)
                    elif genre == "fantasy":
                        genreIDs.add(FANTASY)
                    elif genre == "history":
                        genreIDs.add(HISTORY)
                    elif genre == "horror":
                        genreIDs.add(HORROR)
                    elif genre == "music":
                        genreIDs.add(MUSIC)
                    elif genre == "mystery":
                        genreIDs.add(MYSTERY)
                    elif genre == "romance":
                        genreIDs.add(ROMANCE)
                    elif genre == "science-fiction":
                        genreIDs.add(SCIFI)
                    elif genre == "tv-movie":
                        genreIDs.add(TVMOVIE)
                    elif genre == "thriller":
                        genreIDs.add(THRILLER)
                    elif genre == "war":
                        genreIDs.add(WAR)
                    elif genre == "western":
                        genreIDs.add(WESTERN)
                entry_line += " ".join(map(str, genreIDs))
        train_output_file.write(entry_line + '\n')
    except IOError:
        print("Wrong file or file path: " + file_name)
train_output_file.close()

test_listdir = os.listdir(my_path + '/_test/')
test_output_file = open("../test_truth_with_genreIDs.txt", "w")
# Get all the info.txt files for every test movie
for dir in test_listdir:
    try:
        file_name = "%s\_test\%s\info.txt" % (my_path, dir)  # File to read
        entry_line = ""  # Entry string for output file
        for line in open(file_name):
            # if line[:3] == ID_prefix:
                # entry_line += line[3:-1] + " "
            # elif line[:6] == title_prefix:
            #     entry_line += line[6:-1] + ','
            if line[:7] == genre_prefix:
                genres = line[7:].split() # Convert genre to ID
                genreIDs = set()
                for genre in genres:
                    genre = genre.lower()
                    if genre == "action":
                        genreIDs.add(ACTION)
                    elif genre == "adventure":
                        genreIDs.add(ADVENTURE)
                    elif genre == "animation":
                        genreIDs.add(ANIMATION)
                    elif genre == "comedy":
                        genreIDs.add(COMEDY)
                    elif genre == "crime": 
                        genreIDs.add(CRIME)
                    elif genre == "documentary":
                        genreIDs.add(DOCUMENTARY)
                    elif genre == "drama":
                        genreIDs.add(DRAMA)
                    elif genre == "family":
                        genreIDs.add(FAMILY)
                    elif genre == "fantasy":
                        genreIDs.add(FANTASY)
                    elif genre == "history":
                        genreIDs.add(HISTORY)
                    elif genre == "horror":
                        genreIDs.add(HORROR)
                    elif genre == "music":
                        genreIDs.add(MUSIC)
                    elif genre == "mystery":
                        genreIDs.add(MYSTERY)
                    elif genre == "romance":
                        genreIDs.add(ROMANCE)
                    elif genre == "science-fiction":
                        genreIDs.add(SCIFI)
                    elif genre == "tv-movie":
                        genreIDs.add(TVMOVIE)
                    elif genre == "thriller":
                        genreIDs.add(THRILLER)
                    elif genre == "war":
                        genreIDs.add(WAR)
                    elif genre == "western":
                        genreIDs.add(WESTERN)
                entry_line += " ".join(map(str, genreIDs))
        test_output_file.write(entry_line + '\n')
    except IOError:
        print("Wrong file or file path: " + dir)
test_output_file.close()
