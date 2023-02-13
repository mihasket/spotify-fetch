import sys
import spotipy
import climage
import argparse
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from difflib import SequenceMatcher
from src.colors import colors
from spotipy.cache_handler import MemoryCacheHandler

load_dotenv()

try:
    auth_manager = SpotifyClientCredentials(cache_handler=MemoryCacheHandler())
    sp = spotipy.Spotify(auth_manager=auth_manager)

except:    
    print("Spotify client credentials are not setup correctly!")
    sys.exit(1)

def similar(string_a, string_b):
    return SequenceMatcher(None, string_a, string_b).ratio()

def get_args():
    parser = parser = argparse.ArgumentParser()

    parser.add_argument('--artist', help='Artist name')
    parser.add_argument('--album', help='Album name')

    return parser.parse_args()

def get_artist(name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']

    if len(items) > 0:
        return items[0]
    else:
        return None

def get_top3_popular_songs(artist):
    track_array = []
    results = sp.artist_top_tracks(artist['id'])

    track_array.append(results['tracks'][0]['name'])
    track_array.append(results['tracks'][1]['name'])
    track_array.append(results['tracks'][2]['name'])

    return track_array

def get_latest_album(artist):
    results = sp.artist_albums(artist['id'], album_type='album')

    return results['items'][0]['name']

def get_artist_genre(artist):
    return artist['genres'][0]

def get_artist_cover_url(artist_name):
    results = sp.search(q='artist:' + artist_name, type='artist')
    items = results['artists']['items']

    if len(items) > 0:
        artist = items[0]
        cover = artist['images'][0]['url']

    return cover

def get_album(artist, album_name):
    albums = []
    results = sp.artist_albums(artist['id'], album_type='album')
    albums.extend(results['items'])

    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])
    
    seen = set()  # to avoid dups
    albums.sort(key=lambda album: album['name'].lower())
    for album in albums:
        name = album['name']
        if name not in seen:
            # Checks for typos in album argument
            if similar(name, album_name) > 0.50:
                return album
            seen.add(name)
 
def get_album_cover_url(album):
    return album['images'][0]['url']

def get_album_total_tracks(album):
    return album['total_tracks']

def get_album_release_date(album):
    return album['release_date']

def artist_fetch(image, artist, artist_name):
    artist_array = []
    output_sequance = '\n'

    top_songs = get_top3_popular_songs(artist)
    latest_album = get_latest_album(artist)
    genre = get_artist_genre(artist)

    artist_array.append(colors.BOLD + colors.BLUE + "Artist: " + colors.UNDERLINE + artist_name)
    artist_array.append(colors.BOLD + colors.GREEN + "Top Song 1: " + colors.UNDERLINE + top_songs[0])
    artist_array.append(colors.BOLD + colors.GREEN + "Top Song 2: " + colors.UNDERLINE + top_songs[1])
    artist_array.append(colors.BOLD + colors.GREEN + "Top Song 3: " + colors.UNDERLINE + top_songs[2])
    artist_array.append(colors.BOLD + colors.LIGHTGREEN + "Latest Album: " + colors.UNDERLINE + latest_album)
    artist_array.append(colors.BOLD + colors.CYAN + "Genre: " + colors.UNDERLINE + genre.title())

    i = 0
    num_of_new_lines = 0
    empty=""
    for char in image:
        if(char != '\n'):
            output_sequance += char
        else:
            num_of_new_lines += 1
            if(i < len(artist_array) and num_of_new_lines > 2):
                output_sequance += f"{empty:>8}{artist_array[i]}"
                i += 1

            output_sequance += char

    # Outputs the fetching information
    print(output_sequance)

def album_fetch(image, album, artist_name, album_name):
    album_information_array = []
    output_sequance = '\n'

    total_tracks = str(get_album_total_tracks(album))
    release_date = get_album_release_date(album)
    album_information_array.append(colors.BOLD + colors.BLUE + "Artist: " + colors.UNDERLINE + artist_name)
    album_information_array.append(colors.BOLD + colors.GREEN + "Album: " + colors.UNDERLINE + album_name)
    album_information_array.append(colors.BOLD + colors.LIGHTGREEN + "Total Tracks: " + colors.UNDERLINE + total_tracks)
    album_information_array.append(colors.BOLD + colors.CYAN + "Release Date: " + colors.UNDERLINE + release_date)

    i = 0
    num_of_new_lines = 0
    empty=""
    for char in image:
        if(char != '\n'):
            output_sequance += char
        else:
            num_of_new_lines += 1
            if(i < len(album_information_array) and num_of_new_lines > 3):
                output_sequance += f"{empty:>8}{album_information_array[i]}"
                i += 1

            output_sequance += char

    # Outputs the fetching information
    print(output_sequance)

# Outputs only the information about the artist
def show_artist_info(artist_name):
    artist = get_artist(artist_name)

    try:
        cover_url = get_artist_cover_url(artist_name)
        image = climage.convert_url(url=cover_url, is_unicode=True, width=24)
        artist_fetch(image=image, artist=artist, artist_name=artist_name)
    except:
        print("Error in argument value")

# Outputs album information from said artist
def show_album_info(artist_name, album_name):
    artist = get_artist(artist_name)

    if artist is not None:
        album = get_album(artist=artist, album_name=album_name)
        cover_url = get_album_cover_url(album=album)
    else:
        print("Error in artist argument")

    if cover_url is not None:
        image = climage.convert_url(url=cover_url, is_unicode=True, width=24)
        album_fetch(image=image, album=album, artist_name=artist_name, album_name=album['name'])
    else:
        print("Error album argument")

def main():
    args = get_args()

    # Output album information
    if (args.artist is not None and args.album is not None):
        show_album_info(args.artist, args.album)
    # Output artist information
    elif (args.artist is not None and args.album is None):
        show_artist_info(args.artist)
    # No arguments or only album argument
    else:
        print("No arguments or only album argument are not allowed!")

if __name__ == "__main__":
    main()