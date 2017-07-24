# Spotitube
A lightweight tool that uses Spotify and Youtube to downloads tracks from any Spotify playlist to the user's local Music folder as mp3 files.

## A Short Description
**spotitube** is a command-line program to download mp3 files of tracks in user Spotify playlists. It is not platform specific, and will run on Mac OS X, Windows, and Linux. It is released on public domain, so you can modify, redistribute, and use freely.

## Prerequisites

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

## How to Use
### Obtain Spotify Playlist URI
Go to your Spotify Playlist, right click, Share, copy URI:
### Obtain Spotify Client & Client Secret Key
To access user and public playlists, Spotify requires you to use their API which gives you a unique Client Key and a Client Secret Key relevant only to YOUR Spotify account.

1. Login with your credentials here: [https://developer.spotify.com/my-applications/#!/](https://developer.spotify.com/my-applications/#!/)
2. Go to My Applications on the sidebar and create an app. Your application name/description does not matter.
3. Your Client ID and Client Secret Keys will be generated.

### Command-Line
Using your keys and URI:
```
$ python spotify.py -c CLIENT -cs CLIENT_SECRET -u URI
```


### Options
```
usage: spotify.py [-h] [-c CLIENT] [-cs CLIENT_SECRET] [-u URI]

required arguments:
  -c CLIENT, --client CLIENT                            Spotify client key
  -cs CLIENT_SECRET, --client-secret CLIENT_SECRET      Spotify client secret key
  -u URI, --uri URI                                     Spotify playlist URI

optional arguments:
  -h, --help                                            show this help message and exit
  -a AUDIO_QUALITY, --audio-quality AUDIO_QUALITY       Audio bitrate (128, 160, 192, 256*, 320 kbit/s)
```

## Built With

* [Spotipy](https://github.com/plamere/spotipy) - Lightweight Python Spotify API
* [EyeD3](https://github.com/nicfit/eyeD3) - Used to edit metadata with Python audio data toolkit (ID3 and MP3)
* [Youtube_dl](https://github.com/rg3/youtube-dl) - Used to download Youtube videos/audio
* [Google_api_python_client](https://github.com/google/google-api-python-client) - Youtube API

## Authors

* **[Alex Kim](https://github.com/alexkim205)** - Original author
