# Spotify Fetch

Neofetch-like tool for fetching spotify artist and album information.

![Artist information](/images/artist_information.png)

![Album information](/images/album_information.png)

# Dependencies
- [Spotipy](https://github.com/spotipy-dev/spotipy)
- My version of [CLImage](https://github.com/mihasket/CLImage)
- Original version of CLImage can be found [here](https://github.com/pnappa/CLImage)

# Requirements

Put the following variables in your `.zshrc` or `.bashrc` or whatever shell you are using
```bash
export SPOTIFY_CLIENT_ID='your_id'
export SPOTIFY_CLIENT_SECRET='your_secret'
```

# Usage

For displaying artist information
```bash
python main.py --artist "C418"
```

For displaying album information
```bash
python main.py --artist "C418" --album "Volume Beta"
```

# TO DO
- Update README
- List Dependencies
- Add licence
- Reorganize
- Save cache in .cache