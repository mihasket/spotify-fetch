import sys
import spotipy
import argparse
from sfetch.helpers import show_album_info, show_artist_info
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from spotipy.cache_handler import MemoryCacheHandler


def main():
    load_dotenv()

    try:
        auth_manager = SpotifyClientCredentials(cache_handler=MemoryCacheHandler())
        sp = spotipy.Spotify(auth_manager=auth_manager)
    except Exception:
        print("Spotify client credentials are not setup correctly!")
        print("Visit https://spotipy.readthedocs.io/ for additional information.")
        sys.exit(1)

    parser = argparse.ArgumentParser()

    parser.add_argument('--artist', help='Artist name, example: sfetch --artist "Mac Miller"')
    parser.add_argument('--album', help='Album name, needs to be combined with artist argument, example: sfetch --artist "Mac Miller" --album "Swimming"')

    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    if (args.artist is not None and args.album is not None):
        show_album_info(sp, args.artist, args.album)
    elif (args.artist is not None and args.album is None):
        show_artist_info(sp, args.artist)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
