import webbrowser

class Movie():
	""" Movie class 
		
		Movie objects contain information about a movie, including description 
		and preview URLS. Each object can open its preview trailer in a webbrowser.

		Attributes:
			title: A text field containing the name of the movie

 			storyline: A Text field that stores a brief description 
					   of the movie's story

			poster_image_url: A text field that stores the image URL of the movies poster

			trailer_youtube_url: A text field that stores the TouTube URL of the 
					   movie's preview Trailer

			related_clips: A list that stores dictionaries populated in the that stores data 
							(title,  youtube url, thumbnail image url, youtube video_id) about YouTube videao clips related to the movie.
							Ex:
							 movie_1.related_clips = [ {'title': title, 'url': url, 'thumbnail':thumbnail_url, 'video_id':youtube_video_id},
														{'title': title, 'url': url, 'thumbnail':thumbnail_url, 'video_id':youtube_video_id},
														{'title': title, 'url': url, 'thumbnail':thumbnail_url, 'video_id':youtube_video_id} ]

		
	"""
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.related_clips = []


	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

