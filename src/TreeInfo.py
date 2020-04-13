from Services import FileService
from Services import DataService
from Models import Movie

def program():

    althabet = ["0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]

    DataService.createTable(Movie.Movie("Test"))

    rawdirectories =  FileService.tree("/Volumes/VIDEO/MOVIE")
    results = []
    for directory in rawdirectories:
        lastDir = FileService.getLowestDirectory(directory)
        if lastDir in results or lastDir in althabet:
            continue
        movie = Movie.Movie(lastDir)
        results.append(movie)

        movie.Name = movie.Name.replace("'","")

        DataService.insertInto(movie)
    pass

program()