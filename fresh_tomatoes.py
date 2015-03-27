import media
import webbrowser
import os
import re
try:
    import gdata.youtube
except ImportError:
    raise ImportError('\n\nThis app requires the Google Data Library be installed. \n\nVisit this URL for installation instructions:\nhttps://developers.google.com/gdata/articles/python_client_lib#library\n\n')

import gdata.youtube.service
yt_service = gdata.youtube.service.YouTubeService()

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .movie-tile h2{
			min-height: 66px;
		}
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
		.thumb {
			width: 45px;
			height: 30px;
		}
		.clip-link {
			margin-left: 63px;
		}
        .related-container{
            background-color: #d6d6d6;
            overflow: hidden;
            border-radius: 5px;
        }
        .related-container h3 {
            font-size: 1em;
            text-align: left;
            padding: 8px;
        }
        .related-container h3 .title {
            font-weight: bold;
        }
        .related-clip {
            padding: 8px;
            margin: 8px;
            overflow: hidden;
            vertical-align: top;
            background-color: #e6e6e6;
			border: 1px solid #eee;

        }
        .related-clip h3 {
            color: blue;
            margin:0;
            padding: 5px;
            text-align: left;
        }
        .related-clip p {
            vertical-align: top;
            margin: 0;
            margin-left: 65px;
            text-align: left;
			color: #333399;

        }
        .related-clip img {
            width: 60px;
            height: 40px;
            margin-right: 5px;
            float: left;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
		// Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-clip-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });

        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
    <div class='related-container'>
        <h3>YouTube videos related to <span class='title'>{movie_title}</span></h3>
        <div class="related-clip movie-clip-tile" data-trailer-youtube-id="{clip_id_1}" data-toggle="modal" data-target="#trailer">
            <img src="{thumbnail_1}" alt="{clip_1}" />
            <p>{clip_1}</p>
        </div>
        <div class="related-clip movie-clip-tile" data-trailer-youtube-id="{clip_id_2}" data-toggle="modal" data-target="#trailer">
            <img src="{thumbnail_2}" alt="{clip_2}" />
            <p>{clip_2}</p>
        </div>
        <div class="related-clip movie-clip-tile" data-trailer-youtube-id="{clip_id_3}" data-toggle="modal" data-target="#trailer">
            <img src="{thumbnail_3}" alt="{clip_3}" />
            <p>{clip_3}</p>
        </div>
    </div>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        trailer_youtube_id = extract_video_id(movie.trailer_youtube_url)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,

			# Thumbnail images for the clips
			thumbnail_1 = movie.related_clips[0]['thumbnail'],
			thumbnail_2 = movie.related_clips[1]['thumbnail'],
			thumbnail_3 = movie.related_clips[2]['thumbnail'],

			# Clip URL's
			clip_url_1 = movie.related_clips[0]['url'],
			clip_url_2 = movie.related_clips[1]['url'],
			clip_url_3 = movie.related_clips[2]['url'],

			# Clip's title
			clip_1 = movie.related_clips[0]['title'],
			clip_2 = movie.related_clips[1]['title'],	
			clip_3 = movie.related_clips[2]['title'],
			
			#Clip video ID
			clip_id_1 = movie.related_clips[0]['video_id'],
			clip_id_2 = movie.related_clips[1]['video_id'],	
			clip_id_3 = movie.related_clips[2]['video_id']

        )
    return content

# Get YouTube related Clips for a specified movie
def get_related_clips(movies):
    for movie in movies:
		# Clips Dictionary will contain the related clip data
        clips = []

		# Query YouTube for related movie data
        trailer_youtube_id = extract_video_id(movie.trailer_youtube_url)
        related_feed = yt_service.GetYouTubeRelatedVideoFeed(video_id=trailer_youtube_id)

		# Add related clip data
        for entry in related_feed.entry:
			clip = {'title': entry.title.text,'url': entry.media.player.url,'thumbnail':entry.media.thumbnail[0].url}
			clip['video_id'] = extract_video_id(clip['url'])
			movie.related_clips.append(clip)

# Obtain the YouTube video ID from a URL
def extract_video_id(url):
    youtube_id_match = re.search(r'(?<=v=)[^&#]+', url)
    youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', url)
    trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None
    return trailer_youtube_id


# Dump movie object data to console (DEBUGGING)
def dump_movies(movies):
	for movie in movies:
		print "\n================================="
		print movie.title
		print movie.trailer_youtube_url
		for clip in movie.related_clips:
			print clip['video_id']


def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Append list of related movie clips for each movie
  get_related_clips(movies)    

  #dump_movies(movies)

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
