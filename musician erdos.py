import pandas as pd
from pprint import pprint
import os
import csv
import re
import sys
import json

maxInt = sys.maxsize

#to enable reading of large csv
while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)


def separate_artists(string):
    pattern = re.compile(r',|feat\.|&|vs|and|with|\+|ft\.|/|featuring| x ', re.IGNORECASE)
    musicians = pattern.split(string)
    return [musician.strip() for musician in musicians]


with open('artist_credit', 'r', errors='ignore') as file:
    reader = csv.reader(file, delimiter='\t')
    header = next(reader)#this is wrong
    credit_artist_names_dict = {col: [] for col in header}
    for rownum, row in enumerate(reader):
            credit_id = row[0]
            artist_names = row[1]
            seperate_artists_names = separate_artists(artist_names)
            #artist_count = int(row[2])
            credit_artist_names_dict[credit_id] = seperate_artists_names
            if rownum % 100000 == 0: print(rownum)

    print("done credit")


with open('recording', 'r', errors='ignore') as file:
    reader = csv.reader(file, delimiter='\t')
    header = next(reader)#this is wrong
    credit_song_names_dict = {col: [] for col in header}
    
    for rownum, row in enumerate(reader):
        
        try:
            credit_id = row[3]
            song_name = row[2].lower()
        except:
            credit_id = 0
            song_name = ""

        
        credit_song_names_dict[credit_id] = song_name
        
        if rownum % 100000 == 0: 
            print(rownum)
            print(f"{credit_id} {song_name}")
        #if rownum >= 500:
        #    break
    print("done canonical")


artist_link_dict = {}
#merge dicts
for keynum, key in enumerate(credit_artist_names_dict):
    artists = credit_artist_names_dict[key]
    for artist in artists:
        artist = artist.lower()
        artist_link_dict.setdefault(artist, {})
        for other_artist in artists:
            other_artist = other_artist.lower()
            if artist != other_artist:
                try:
                    song_name = credit_song_names_dict[key]
                except:
                    song_name = "N/A"

                if keynum % 100000 == 0: print(f'{artist}, {other_artist}, {song_name}')
                artist_link_dict[artist][other_artist] = song_name

print("done merge dicts")


with open("artist_link_dict.json", "w") as f:
    json.dump(artist_link_dict, f)

