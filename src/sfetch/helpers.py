import requests
import climage
from io import BytesIO
from PIL import Image
from sfetch.colors import colors
from difflib import SequenceMatcher


def similar(string_a, string_b):
    return SequenceMatcher(None, string_a, string_b).ratio()


def get_artist(sp, name):
    results = sp.search(q='artist:' + name, type='artist')
    items = results['artists']['items']

    if len(items) > 0:
        return items[0]
    else:
        return None


def get_top3_popular_songs(sp, artist):
    track_array = []
    results = sp.artist_top_tracks(artist['id'])

    track_array.append(results['tracks'][0]['name'])
    track_array.append(results['tracks'][1]['name'])
    track_array.append(results['tracks'][2]['name'])

    return track_array


def get_latest_album(sp, artist):
    results = sp.artist_albums(artist['id'], album_type='album')

    return results['items'][0]['name']


def get_artist_cover_url(sp, artist_name):
    results = sp.search(q='artist:' + artist_name, type='artist')
    items = results['artists']['items']

    if len(items) > 0:
        artist = items[0]
        cover = artist['images'][0]['url']

    return cover


def get_album(sp, artist, album_name):
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


def artist_fetch(sp, image, artist, artist_name):
    artist_array = []
    output_sequance = '\n'

    top_songs = get_top3_popular_songs(sp, artist)
    latest_album = get_latest_album(sp, artist)

    i = 0
    genres = ""
    for genre in artist['genres']:
        i = i + 1
        if (i == len(artist['genres']) or i == 3):
            genres += f"{genre}"
            break
        else:
            genres += f"{genre}, "

    artist_array.append(colors.BOLD + colors.BLUE + "Artist: " + colors.UNDERLINE + artist_name)
    artist_array.append(colors.BOLD + colors.GREEN + "1: " + colors.UNDERLINE + top_songs[0])
    artist_array.append(colors.BOLD + colors.GREEN + "2: " + colors.UNDERLINE + top_songs[1])
    artist_array.append(colors.BOLD + colors.GREEN + "3: " + colors.UNDERLINE + top_songs[2])
    artist_array.append(colors.BOLD + colors.LIGHTGREEN + "Latest Album: " + colors.UNDERLINE + latest_album)
    artist_array.append(colors.BOLD + colors.CYAN + "Genre: " + colors.UNDERLINE + genres)

    i = 0
    num_of_new_lines = 0
    empty = ""
    for char in image:
        if (char != '\n'):
            output_sequance += char
        else:
            num_of_new_lines += 1
            if (i < len(artist_array) and num_of_new_lines > 2):
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
    empty = ""
    for char in image:
        if (char != '\n'):
            output_sequance += char
        else:
            num_of_new_lines += 1
            if (i < len(album_information_array) and num_of_new_lines > 3):
                output_sequance += f"{empty:>8}{album_information_array[i]}"
                i += 1

            output_sequance += char

    # Outputs the fetching information
    print(output_sequance)


# Outputs only the information about the artist
def show_artist_info(sp, artist_name):
    artist = get_artist(sp, artist_name)

    try:
        cover_url = get_artist_cover_url(sp, artist_name)

        response = requests.get(cover_url)
        image = Image.open(BytesIO(response.content)).convert('RGB')
        converted = climage.convert_pil(image, is_unicode=True, width=24)

        artist_fetch(sp=sp, image=converted, artist=artist, artist_name=artist_name)
    except Exception:
        print("Error in argument value")


# Outputs album information from said artist
def show_album_info(sp, artist_name, album_name):
    artist = get_artist(sp, artist_name)

    if artist is not None:
        album = get_album(sp, artist=artist, album_name=album_name)
        cover_url = get_album_cover_url(album=album)
    else:
        # TODO EXIT
        print("Error in artist argument")

    if cover_url is not None:
        response = requests.get(cover_url)
        image = Image.open(BytesIO(response.content)).convert('RGB')
        converted = climage.convert_pil(image, is_unicode=True, width=24)

        album_fetch(
            image=converted,
            album=album,
            artist_name=artist_name,
            album_name=album['name']
        )
    else:
        print("Error album argument")
