from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id='ecb8fded977d493e806550e5112b48b2',
        client_secret= 'b36e8245d8ed401091ed31a210f32918',
        show_dialog=True,
        cache_path="day46/token.txt"))

typed_correctly = True
while typed_correctly:
    date = input('Which year do you want to travel to? type the date in this format YYYY-MM-DD: ')
    formatted_date = date.split('-')

    if len(formatted_date[0])<4 or len(formatted_date[1])<2 or len(formatted_date[2])<2:
        print('error type the correct format')
    else:
        print('-'*60)
        print('loading')
        print('-'*60)
        break

URL = f'https://www.billboard.com/charts/hot-100/{date}/'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
song_list = []
artist_names = []


top_1 = soup.find('li', class_="lrv-u-width-100p")
song_list.append(top_1.select('h3')[0].getText().strip())
artist_names.append(top_1.select('span')[0].getText().strip())

top = soup.find_all('li', class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-l-050 lrv-u-padding-l-1@mobile-max")

top_100 = [title.select('h3') for title in top]
top_100_artist = [artist.select('span') for artist in top]

for title in top_100:
    song_list.append(title[0].getText().strip())

for artist in top_100_artist:
    artist_names.append(artist[0].getText().strip())

user_name = sp.current_user()['id']
year = formatted_date[0]
month = formatted_date[1]
day = formatted_date[2]
song_uri = []

for index,song in enumerate(song_list, 0):
    result = sp.search(q=f'track:{song} year:{year}',type='track')
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uri.append(uri)
    except IndexError:
        print(f"{song} does't exist in Spotify, Skipped")

play_list = sp.user_playlist_create(user=user_name,name=f'{year}-{month}-{day} Billboard 100', public=False, collaborative=False,description='top 100 playlist for the year serached')

sp.playlist_add_items(playlist_id=play_list['id'], items=song_uri)







