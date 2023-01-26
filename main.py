import os
import spotipy
import climage
import argparse
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from colors import colors

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))

def get_args():
    parser = parser = argparse.ArgumentParser()

    parser.add_argument('--artist', help='Artist name')
    parser.add_argument('--album', help='Album name')

    return parser.parse_args()

def get_top5_songs(artist_name):
    track_array = []
    results = sp.search(artist_name, limit=5)

    for idx, track in enumerate(results['tracks']['items']):
        track_array.append(colors.BOLD + colors.OKBLUE + track['name'])

    return track_array

def get_artist_cover_url(artist_name):
    cover = ""
    results = sp.search(q='artist:' + artist_name, type='artist')
    items = results['artists']['items']

    if len(items) > 0:
        artist = items[0]
        cover = artist['images'][0]['url']

    return cover

def output_fetch(output, artist_name):
    track_array = get_top5_songs(artist_name)
    output_sequance = '\n'

    i = 0
    num_of_new_lines = 0
    for char in output:
        if(char != '\n'):
            output_sequance += char
        else:
            num_of_new_lines += 1
            if(i < len(track_array) and num_of_new_lines > 3):
                empty=""
                output_sequance += f"{empty:>8}{track_array[i]}"
                i += 1

            output_sequance += char

    # Outputs the fetching information
    print(output_sequance)

def main():
    args = get_args()

    if (args.artist is not None):
        artist_name = args.artist
    else:
        artist_name = "Mac Miller"

    try:
        cover_url = get_artist_cover_url(artist_name)
        output = climage.convert_url(url=cover_url, is_unicode=True, width=24)
        output_fetch(output=output, artist_name=artist_name)
    except:
        print("Error in argument value")

if __name__ == "__main__":
    main()