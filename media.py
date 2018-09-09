import webbrowser

class Movie() :
    """ This class defines various information related to movie and plays it trailer """
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        """this function make instances and contains information like
        movie title, stroryline, movie poster and a youtube url """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ this method will play the movie trailer """
        webbrowser.open(self.trailer_youtube_url)
