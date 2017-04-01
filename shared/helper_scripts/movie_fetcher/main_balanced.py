import tmdbsimple as tmdb
from sets import Set
import threading
import urllib
import os
import string
import time
import random

valid_chars = "%s%s" % (string.ascii_letters, string.digits)
tmdb.API_KEY = '2aa2155212f4aff92a1194b07a6739a8'
base_address = tmdb.Configuration().info().get("images").get("secure_base_url")
MAX_COUNT = 360
lock = threading.Lock()
visited = Set()
rand_str = lambda n: ''.join([random.choice(string.lowercase) for i in xrange(n)])


class GenreThread(threading.Thread):

    def __init__(self, genre_id):
        threading.Thread.__init__(self)
        self.genre_id = genre_id

    def run(self):

        # Exponential waits on API calls, in case of limit reached.
        while True:
            waitTime = 10
            try:
                total_pages = tmdb.Genres(self.genre_id).movies().get('total_pages')
                waitTime = 10
                break
            except Exception:
                print 'Waiting for refreshing API requests'
                time.sleep(waitTime)
                waitTime *= 2

        for i in range(current_pages.get(self.genre_id), total_pages):

            exit = False
            while True:
                try:
                    results = tmdb.Genres(self.genre_id).movies(page=i).get('results')
                    waitTime = 10
                    break
                except Exception:
                    time.sleep(waitTime)
                    waitTime *= 2

            for movie in results:
                if sizes.get(self.genre_id) >= MAX_COUNT:
                    exit = True
                    break

                thread = threading.Thread(target=search_thread, args=[movie, self.genre_id])
                thread.start()
                thread.join()
                time.sleep(0.01)

            if exit:
                current_pages[self.genre_id] = i + 2
                return


def search_thread(movie,genre_id):

    if movie.get('adult'):
        return

    movie_genres = movie.get("genre_ids") # int list of Genres, not a map

    poster = movie.get("poster_path")
    if movie_genres is None or poster is None or len(movie_genres) == 0:
        return

    id = movie.get("id")

    if id in visited:
        return
    else:
        visited.add(id)

    lock.acquire()
    try:
        b = False
        for genre in movie_genres: # Genre is int here
            if sizes.get(genre) is None or sizes.get(genre) >= MAX_COUNT:
                b = True
                break
        if not b:
            for genre in movie_genres:
                sizes[genre] = sizes.get(genre) + 1
    finally:
        lock.release()
    if b:
        return

    title = movie.get("title")

    '''Title will be folder and filename, so it should not include any special chars.'''
    title = "".join(c for c in title if c in valid_chars)

    if len(title) < 4:
        title = rand_str(10)

    if not os.path.exists(title):
        os.makedirs(title)

    f = open(title + '/info.txt', 'w')
    f.write("ID:%s\n" % id)
    f.write("Title:%s\n" % title)
    f.write("Genres:")

    for g in movie_genres:
        f.write(" %s" % genre_map.get(g))

    f.write("\n")
    f.close();

    waittime = 10
    while True:
        try:
            urllib.urlretrieve(base_address + '/w342' + poster, title + "/w342.jpg")
            waittime = 10
            break
        except Exception:
            time.sleep(waittime)
            waittime *= 2




if __name__ == "__main__":

    # Directory of downloads to be saved. It should be same in reader
    path = "Data"
    if path != "":
        if not os.path.exists(path):
            os.makedirs(path)
        os.chdir(path)

    genres = tmdb.Genres().list().get("genres");
    genre_map = {}
    sizes = {}
    current_pages = {}
    genre_size = len(genres)

    f = open('genres.txt', 'w')

    for g in genres:
        genre_map[g.get('id')] = g.get('name').replace(" ", "-")
        sizes[g.get('id')] = 0
        current_pages[g.get('id')] = 1
        f.write("%s\n" % g.get('name').replace(" ", "-"))
    f.close()

    threads = []
    for g in genres:
        t = GenreThread(g.get('id'))
        t.start()
        threads.append(t)
        time.sleep(5)

    for t in threads:
        t.join()

    print "\n--------------------------------------------------------"
    print sizes
    print "\n--------------------------------------------------------"
    if not os.path.exists('_test'):
        os.makedirs('_test')
    os.chdir('_test')

    MAX_COUNT /= 9;

    threads = []
    for g in genres:
        sizes[g.get('id')] = 0
        t = GenreThread(g.get('id'))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

