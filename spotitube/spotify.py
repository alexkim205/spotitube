from __future__ import unicode_literals

# SPOTIFY DEPENDENCIES
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json

import os
import re

# SPOTIFY API
def set_sids(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET_ID):
    client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET_ID)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp

def get_playlist_info(sp, username, playlist_id, limit = 100, offset = 0):
    pl_info = sp.user_playlist_tracks(username, playlist_id, limit = 100, offset = offset)
    pl = sp.user_playlist(username, playlist_id)
    return (pl_info, pl)

def get_search_info(sp, pl_info, songlistdir):
    ids = []
    if os.path.isfile(songlistdir):
        with open(songlistdir) as f:
            ids = map(lambda s: s.strip(), f.readlines())

    #buzzwords = ["official"] # audio, lyric
    search_list = []
    metadata = []
    for song in pl_info["items"]:
        title = song["track"]["name"]

        if song["track"]["uri"].encode("utf-8") in ids: # check if song is already downloaded and in songlist.txt
            print (title + "\t" + "Song already downloaded").expandtabs(30)
            continue
        if (not u'US' in song["track"]["available_markets"]) and song["track"]["available_markets"]: # check if song is available in US
            print (title + "\t" + "Song not available in the US").expandtabs(30)
            continue

        album = song["track"]["album"]["name"]
        coverart = song["track"]["album"]["images"][0]["url"] # take largest coverart
        track_nom = song["track"]["track_number"]
        artists = []
        for artist in song["track"]["artists"]:
            artists.append(artist["name"])
        metadatartists = tuple(artists)
        genre = ', '.join(sp.artist(song["track"]["artists"][0]["uri"])["genres"]).title().encode("utf-8")
        idnom = song["track"]["uri"].encode("utf-8")
        metadata.append((title, album, coverart, track_nom, metadatartists, genre, idnom))

        search_title = re.sub(r'\([^)]*\)', '', title)
        search_artist = artists
        search_song = search_artist
        search_song.append(search_title)
        #search_song.extend(buzzwords)
        search_list.append(search_song)

    return search_list, metadata
