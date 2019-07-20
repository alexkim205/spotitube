from __future__ import print_function
# from __future__ import unicode_literals

import spotify
import youtube
import argparse
import os
import pandas as pd
from unicodedata import normalize

if __name__ == "__main__":
    # PARSE ARGS
    parser = argparse.ArgumentParser()
    optional = parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    required.add_argument("-n", "--username", help="Username")
    required.add_argument("-k", "--key-file", help="Read Spotify client/secret keys from text file")
    required.add_argument("-u", "--uri", help="Spotify playlist URI")
    optional.add_argument("-a", "--audio-quality", help="Audio bitrate (128, 160, 192, 256*, 320 kbit/s)")
    parser._action_groups.append(optional)

    # Set Args
    args = parser.parse_args()
    if args.key_file:
        key_file = args.key_file
    if args.uri:
        uri = args.uri
    if args.audio_quality:
        audioquality = args.audio_quality
    if args.username:
        username = args.username
    audioquality = args.audio_quality if args.audio_quality else '160'
    
    DEVELOPER_KEY = "AIzaSyAiafRmd3aEjduD7AZX7yJ0qQLAej4cI5E"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    # Read keys from text file
    dt = pd.read_csv(key_file, sep="\t", header=None)
    SPOTIFY_CLIENT_ID = dt[1][0]
    SPOTIFY_CLIENT_SECRET_ID = dt[1][1]

    # Spotify Youtube API
    sp = spotify.set_sids(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET_ID)
    yt = youtube.set_yids(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, DEVELOPER_KEY)

    music_dir = os.path.expanduser("~/Music/")

    # Spotify get tracks and generate search lists
    playlist_id = uri.split(':')[2]

    pl_info, pl = spotify.get_playlist_info(sp, username, playlist_id, limit = 100)
    pl_name = normalize('NFKD', pl['name'])

    pl_dir = music_dir + pl_name  + "/"
    songlistdir = pl_dir + "songlist.txt"
    if not os.path.isdir(pl_dir):
        os.makedirs(pl_dir)

    # Maybe more official way to loop through offsets (pages) to get all tracks
    #  use "next" and  "href" in JSON
    parsed = 100
    total = pl_info['total']

    while parsed < total:
        pl_info_temp = spotify.get_playlist_info(sp, username, playlist_id, limit = 100, offset = parsed)[0]
        pl_info["items"].extend(pl_info_temp["items"])
        parsed += 100

    s_list, metadata = spotify.get_search_info(sp, pl_info, songlistdir)

    # Download youtube links
    youtube.youtubedl(yt, s_list, metadata, pl_dir, songlistdir, audioquality)
