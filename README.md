# Movie Trailer Website

## About
The movie trailer webite project allows a user to create a website that showcases their favorite maovies, 
and allows playback of each movie's preview trailer in a modal window. Each movie also lists 3 related YouTube
videos, which can also be played back in the modal window.

## Requirements
This version of the Movie Trailer Website project requires that Google Data Python library to get data from YouTube.
The library and setup instructions can be found on the [Google Developers Website](https://developers.google.com/gdata/articles/python_client_lib#library).

## Usage
The project includes sample movie data. To generate the Movie Trailer Website, just execute the entertainment_center.py file:

```python
python entertainment_center.py
```

A browser window will open the fresh_tomatoes.html file that was generated from the entertainment_center.py script.


## Customization
To create a website with your own favorite movies, you will need to modify the entertainment_center.py file and create a new Movie object and add that object to the movies list.
The Movie object requires 4 parameters: 
* The movie title
* The movie description
* The URL of the poster image representing the movie
* The YouTube URL of the movie trailer

``` python
new_movie_object_1 = media.Movie("Title", "Description text", "http://image.url/poster.jpg", "https://youtu.be/6k01DIVDJlY")
```

Add the new object to the movies list:

```python
movies = [new_movie_object_1, new_movie_object_2]
```

Now run the entertainment_center.py file and your website is generated.


