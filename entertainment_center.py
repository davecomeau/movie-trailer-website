import media
import fresh_tomatoes

# Create Movie Objects
# Create a new Movie object for each movie that will be included in the website
# Each movie requires Title, Description Text, Poster Image URL, and YouTube URL
# 	Ex: new_movie_1 = media.Movie("Title","Description Text", "http://poster.url/poster.jpg","https://youtu.be/eb1vcaqAivY")

 
usual_suspects = media.Movie("The Usual Suspects",
						"A sole survivor tells of the twisty events leading up to a horrific gun battle on a boat, which begin when five criminals meet at a seemingly random police lineup.",
						"http://i.ytimg.com/vi/tjwXBkooYaI/movieposter.jpg?v=50fcf849",
						"https://www.youtube.com/watch?v=oiXdPolca5w")

top_secret = media.Movie("Top Secret",
						"Parody of WWII spy movies in which an American rock and roll singer becomes involved in a Resistance plot to rescue a scientist imprisoned in East Germany.",
						"http://upload.wikimedia.org/wikipedia/en/thumb/2/25/Top_secret_ver1.jpg/220px-Top_secret_ver1.jpg",
						"https://www.youtube.com/watch?v=_5bpyeY60r4")

shawshank = media.Movie("The Shawshank Redemption",
						"Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
						"http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
						"https://www.youtube.com/watch?v=6hB3S9bIaco")

boiler_room = media.Movie("Boiler Room",
						"A college dropout gets a job as a broker for a suburban investment firm, which puts him on the fast track to success, but the job might not be as legitimate as it sounds.",
						"http://ecx.images-amazon.com/images/I/51T43J1GWPL.jpg",
						"https://www.youtube.com/watch?v=UoTx9RpL5W4")

lego_movie = media.Movie("The Lego Movie",
						"An ordinary Lego construction worker, thought to be the prophesied 'Special', is recruited to join a quest to stop an evil tyrant from gluing the Lego universe into eternal stasis.",
						"http://upload.wikimedia.org/wikipedia/en/1/10/The_Lego_Movie_poster.jpg",
						"https://www.youtube.com/watch?v=fZ_JOBCLF-I")

neverending_story = media.Movie("The NeverEnding Story",
						"A troubled boy dives into a wonderous fantasy world through the pages of a mysterious book.",
						"https://s3.amazonaws.com/uploads.uservoice.com/assets/072/947/833/original/neverending2.jpg?AWSAccessKeyId=14D6VH0N6B73PJ6VE382&Expires=1489311567&Signature=P%2FJd3OEBOSZeyhyS2K0GqpSFzR4%3D",
						"https://www.youtube.com/watch?v=UeFni9dOv7c")

# List that contains each movie object to be included in the webpage
movies = [usual_suspects,
			boiler_room,
			lego_movie,
			neverending_story,	
			shawshank,	
			top_secret
			]

# Pass the movies list to the open_movies_page to begin generating the webpage
fresh_tomatoes.open_movies_page(movies)
