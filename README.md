# Spotify Fetch

Neofetch-like tool for fetching spotify artist and album information.

![](/images/example.png)

# Dependencies
- [Spotipy](https://github.com/spotipy-dev/spotipy)
- My version of [CLImage](https://github.com/mihasket/CLImage)
- Original version of CLImage can be found [here](https://github.com/pnappa/CLImage)

# Requirements

1. You will need to have [Spotipy](https://github.com/spotipy-dev/spotipy) installed.
Install with pip install
```bash
pip install spotipy
```

2. You will need to have [my fork](https://github.com/mihasket/CLImage) of [CLImage](https://github.com/pnappa/CLImage) installed.
```bash
git clone https://github.com/mihasket/CLImage
cd CLImage
pip install .
```
Once you have successfully installed the fork, you can safely delete the directory.

3. Put the following variables in your `.zshrc` or `.bashrc` or whatever shell you are using
```bash
export SPOTIPY_CLIENT_ID='your_id'
export SPOTIPY_CLIENT_SECRET='your_secret'
```

# Installation

Install from source
```bash
git clone https://github.com/mihasket/spotify-fetch.git
cd spotify-fetch
pip install .
```

# Usage example

For displaying artist information
```bash
spotify-fetch --artist "C418"
```

For displaying album information
```bash
spotify-fetch --artist "C418" --album "Volume Beta"
```