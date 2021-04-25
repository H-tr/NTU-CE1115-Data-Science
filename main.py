import requests
#import numpy as np
#import pandas as pd

movie_data = requests.get("https://api.themoviedb.org/3/movie/181808?api_key=e7b8c40ebe9e3b6c8c081edc3aa5aacb&language=en-US")
movie_dict = movie_data.json()
print('status code: ', movie_data.status_code)
print(movie_dict.keys())
print(type(movie_dict))