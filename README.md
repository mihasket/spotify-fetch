# Spotify Fetch

Neofetch-like tool for fetching spotify artist and album information.

![](/images/example.png)

# Requirements

1. Install [Spotipy](https://github.com/spotipy-dev/spotipy)
```bash
pip install spotipy
```

2. Install [my fork](https://github.com/mihasket/CLImage) of [CLImage](https://github.com/pnappa/CLImage) installed.
```bash
git clone https://github.com/mihasket/CLImage
cd CLImage
pip install .
```
Once you have successfully installed the fork, you can safely delete the directory.

3. Register a [spotify app](https://developer.spotify.com/dashboard/login) and name it `spotify-fetch` or whatever name you would like. 

![](/images/spotify_app_1.png)

Once you have successfully registered an app, find your `Client ID` and `Client Secret`

![](/images/spotify_app_2.png)

Don't share your `Client ID` and `Client Secret`.

4. Put the following variables you just got in your `.zshrc` or `.bashrc` or whatever shell you are using
```bash
export SPOTIPY_CLIENT_ID='your_client_id'
export SPOTIPY_CLIENT_SECRET='your_client_secret'
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
