import sys
import spotipy
import argparse
from src.helpers import show_album_info, show_artist_info
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from spotipy.cache_handler import MemoryCacheHandler


def get_args():
    parser = parser = argparse.ArgumentParser()

    parser.add_argument('--artist', help='Artist name')
    parser.add_argument('--album', help='Album name')

    return parser.parse_args()


def main():
    load_dotenv()

    try:
        auth_manager = SpotifyClientCredentials(cache_handler=MemoryCacheHandler())
        sp = spotipy.Spotify(auth_manager=auth_manager)
    except Exception:
        print("Spotify client credentials are not setup correctly!")
        sys.exit(1)

    args = get_args()

    # Output album information
    if (args.artist is not None and args.album is not None):
        show_album_info(sp, args.artist, args.album)
    # Output artist information
    elif (args.artist is not None and args.album is None):
        show_artist_info(sp, args.artist)
    # No arguments or only album argument
    else:
        print("No arguments or only album argument are not allowed!")


if __name__ == "__main__":
    main()
