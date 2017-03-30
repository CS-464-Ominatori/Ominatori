import os

# Constants
my_path = "C:/Users/burcu/Desktop/Data"
ID_prefix = "ID:"
title_prefix = "Title:"
genre_prefix = "Genres:"

ACTION = 1
ADVENTURE = 2 
FANTASY = 3 
SCIFI = 4 
WESTERN = 5
ANIMATION = 6
FAMILY = 7
BIOGRAPHY = 8
DOCUMENTARY = 9 
SPORT = 10
HISTORY = 11 
WAR = 12
COMEDY = 13
CRIME = 14
MYSTERY = 15
ROMANCE = 16 
DRAMA = 17
HORROR = 18 
THRILLER = 19
MUSIC = 20 
MUSICAL = 21

list_dir = os.listdir(my_path)
output_file = open("../truth.txt", "w")

# Get all the info.txt files for every movie
for dir in list_dir:
    try:
        file_name = "%s\%s\info.txt" % (my_path, dir)  # File to read
        entry_line = ""  # Entry string for output file
        for line in open(file_name):
            if line[:3] == ID_prefix:
                entry_line += line[3:-1] + " "
            # elif line[:6] == title_prefix:
            #     entry_line += line[6:-1] + ','
            elif line[:7] == genre_prefix:
                genres = line[7:].split() # Convert genre to ID
                genreIDs = set()
                for genre in genres:
                    genre = genre.lower()
                    if genre == "action":
                        genreIDs.add(ACTION)
                    elif genre == "adventure":
                        genreIDs.add(ADVENTURE)
                    elif genre == "fantasy":
                        genreIDs.add(FANTASY)
                    elif genre == "science":
                        genreIDs.add(SCIFI)
                    elif genre == "fiction": # This is a problem as Science Fiction is separated by space
                        genreIDs.add(SCIFI)
                    elif genre == "western":
                        genreIDs.add(WESTERN)
                    elif genre == "animation":
                        genreIDs.add(ANIMATION)
                    elif genre == "family":
                        genreIDs.add(FAMILY)
                    elif genre == "biography":
                        genreIDs.add(BIOGRAPHY)
                    elif genre == "documentary":
                        genreIDs.add(DOCUMENTARY)
                    elif genre == "sport":
                        genreIDs.add(SPORT)
                    elif genre == "history":
                        genreIDs.add(HISTORY)
                    elif genre == "war":
                        genreIDs.add(WAR)
                    elif genre == "comedy":
                        genreIDs.add(COMEDY)
                    elif genre == "crime":
                        genreIDs.add(CRIME)
                    elif genre == "mystery":
                        genreIDs.add(MYSTERY)
                    elif genre == "romance":
                        genreIDs.add(ROMANCE)
                    elif genre == "drama":
                        genreIDs.add(DRAMA)
                    elif genre == "horror":
                        genreIDs.add(HORROR)
                    elif genre == "thriller":
                        genreIDs.add(THRILLER)
                    elif genre == "music":
                        genreIDs.add(MUSIC)
                    elif genre == "musical":
                        genreIDs.add(MUSICAL)
                entry_line += " ".join(map(str, genreIDs))
        output_file.write(entry_line + '\n')
    except IOError:
        print("Wrong file or file path: " + dir)