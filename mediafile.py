import webbrowser
class Tollywoodmovies():
    def __init__(self,movie_title,movie_storyline,movie_poster_url,movie_youtube):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=movie_poster_url
        self.trailer_youtube_url=movie_youtube
    def show_movie_trailers(self):
        webbrowser.open(self.trailer_youtube_url)
