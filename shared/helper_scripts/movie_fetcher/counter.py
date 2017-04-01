import os

if __name__ == "__main__":

    path = "Data"
    if path != "":
        if not os.path.exists(path):
            os.makedirs(path)
            os.chdir(path)

    counts = {}

    with open('Data/genres.txt', 'r') as content_file:
        x = content_file.read()

    x = x.strip().split('\n')
    for c in x:
        counts[c] = 0

    for subdir, dirs, files in os.walk(os.path.abspath(path)):
        for dir in dirs:
            if dir == '_test':
                continue

            print dir
            movie_map = {}
            try:
                f = open(subdir + "/" + dir + '/info.txt', 'r')
            except Exception:
                continue

            id = f.readline()
            title = f.readline()
            genres = f.readline()
            genres = genres[genres.index(":")+1:].strip().split()
            f.close()

            for genre in genres:
                counts[genre] = counts.get(genre) + 1

    print counts

