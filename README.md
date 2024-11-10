# Spotify Fetch

Neofetch-like tool for fetching spotify artist and album information.

![](/images/example.png)

# Requirements

1. Register a [spotify app](https://developer.spotify.com/dashboard/login) and name it `sfetch` or whatever name you would like. 

The redirect URI can be any valid URI such as `http://localhost`, `http://example.com`.

Once you have successfully registered an app, find your `Client ID` and `Client Secret`.

Don't share your `Client ID` and `Client Secret`.

2. Put the following variables you just got in your `.zshrc` or `.bashrc` or whatever shell you are using
```bash
export SPOTIPY_CLIENT_ID='your_client_id'
export SPOTIPY_CLIENT_SECRET='your_client_secret'
```

# Installation

Install from source
```bash
git clone https://github.com/mihasket/sfetch.git
cd sfetch
pip install .
```

# Usage example

For displaying artist information
```bash
sfetch --artist "C418"
```

For displaying album information
```bash
sfetch --artist "C418" --album "Volume Beta"
```
