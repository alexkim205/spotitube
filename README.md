# Spotitube
A lightweight tool that downloads tracks in any Spotify playlist to local Music folder as mp3 files.

## A Short Description
**spotitube** is a command-line program to download mp3 files of tracks in user Spotify playlists. It is not platform specific, and will run on Mac OS X, Windows, and Linux. It is released on public domain, so you can modify, redistribute, and use freely.

## Prerequisites

What things you need to install the software and how to install them

#### [youtube_dl](https://github.com/rg3/youtube-dl)
```
youtube_dl >= 2017.7.23
$ sudo -H pip install --upgrade youtube-dl
```
#### requests
```
requests >= 2.11.0
$ pip install requests
```

#### [spotipy](https://github.com/plamere/spotipy)
```
spotipy >= 2.4.4
$ pip install spotipy
```

#### [eyeD3](https://github.com/nicfit/eyeD3)
```
eyeD3 >= 0.8
$ pip install eyeD3
```

#### [google_api_python_client](https://github.com/google/google-api-python-client)
```
google_api_python_client >= 1.6.2
$ pip install --upgrade google-api-python-client
```

## Quick Start
```
$ python spotify.py -c CLIENT -cs CLIENT_SECRET -u URI
```

### Options
```
usage: spotify.py [-h] [-c CLIENT] [-cs CLIENT_SECRET] [-u URI]

required arguments:
  -c, --client              Spotify client key
  -cs, --client-secret      Spotify client secret key
  -u, --uri                 Spotify playlist URI

optional arguments:
  -h, --help                show this help message and exit
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Spotipy](https://github.com/plamere/spotipy) - Lightweight Python Spotify API
* [EyeD3](https://github.com/nicfit/eyeD3) - Used to edit metadata with Python audio data toolkit (ID3 and MP3)
* [Youtube_dl](https://github.com/rg3/youtube-dl) - Used to download Youtube videos/audio
* [Google_api_python_client](https://github.com/google/google-api-python-client) - Youtube API

## Authors

* **Alex Kim** - *Initial work*
