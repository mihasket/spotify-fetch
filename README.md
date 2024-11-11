# Spotify Fetch

Command-line tool for displaying spotify artist and album information.

![](/images/example.png)

# Requirements

1. Make sure you have `python` and `pip` installed.

2. Register a [spotify app](https://developer.spotify.com/dashboard/login) and name it `sfetch` or whatever name you would like. 

The redirect URI can be any valid URI such as `http://localhost`, `http://example.com`.

Once you have successfully registered an app, find your `Client ID` and `Client Secret`.

Don't share your `Client ID` and `Client Secret`.

3. Put the following variables you just got in your `.zshrc` or `.bashrc` or whatever shell you are using
```bash
export SPOTIPY_CLIENT_ID='your_client_id'
export SPOTIPY_CLIENT_SECRET='your_client_secret'
```

Remember to restart your shell!

# Installation

### Install with `pip`

```bash
pip install sfetch
```

### Install from source

1. Clone the repository 
```bash
git clone https://github.com/mihasket/sfetch.git
cd sfetch
```

2. Make sure you have the latest version of PyPA’s build installed:
```bash
python3 -m pip install --upgrade build
```

3. Run this command in the same directory as `pyproject.toml`
```bash
python3 -m build
```

This will create two files in the `dist` directory. Example:
```
dist/
├── sfetch-1.0.0-py3-none-any.whl
└── sfetch-1.0.0.tar.gz
```
The `tar.gz` file is a source distribution whereas the `.whl` file is a built distribution

4. Install the `.whl` file. Example:
```bash
pip install dist/sfetch-1.0.0-py3-none-any.whl
```
The `1.0.0` is for the version of the application.

If you want to uninstall use:
```bash
pip uninstall sfetch
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

For additional help
```bash
sfetch --help
```
