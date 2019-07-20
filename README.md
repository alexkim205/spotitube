# Spotitube
A lightweight tool that uses Spotify and Youtube to downloads tracks from any Spotify playlist to the user's local Music folder as mp3 files.

## A Short Description
**spotitube** is a command-line program to download mp3 files of tracks in user Spotify playlists. It is not platform specific, and will run on Mac OS X, Windows, and Linux. It is released on public domain, so you can modify, redistribute, and use freely.

## Prerequisites
* An installation of conda
* ffmpeg, for MacOS users who have Homebrew, run `brew install ffmpeg`

Create a conda environment with the proper libraries by running `conda env create -f env.yml` in the root directory.

## How to Use
### Obtain Spotify Playlist URI
Go to your Spotify Playlist, right click, Share, copy URI:
### Obtain Spotify Client & Client Secret Key
To access user and public playlists, Spotify requires you to use their API which gives you a unique Client Key and a Client Secret Key relevant only to YOUR Spotify account.

1. Login with your credentials here: [https://developer.spotify.com/my-applications/#!/](https://developer.spotify.com/my-applications/#!/)
2. Go to My Applications on the sidebar and create an app. Your application name/description does not matter.
3. Your Client ID and Client Secret Keys will be generated.

### Run it in command line
```
$ python main.py -u USERNAME -k KEY_FILE -u URI
```

### Making your KEY_FILE

`key.txt`
```
SPOTIFY-C:	[Spotify Client Key]
SPOTIFY-CS:	[Spotify Client Secret Key]
```

### Options
```
$ python main.py -h
usage: main.py [-h] [-n USERNAME] [-k KEY_FILE] [-u URI] [-a AUDIO_QUALITY]

required arguments:
  -n USERNAME, --username USERNAME
                        Username
  -k KEY_FILE, --key-file KEY_FILE
                        Read Spotify client/secret keys from text file
  -u URI, --uri URI     Spotify playlist URI

optional arguments:
  -h, --help            show this help message and exit
  -a AUDIO_QUALITY, --audio-quality AUDIO_QUALITY
                        Audio bitrate (128, 160, 192, 256*, 320 kbit/s)
```

## Authors

* **[Alex Kim](https://github.com/alexkim205)** - Original author
