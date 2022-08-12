import time
import secrets

import googlesearch

from validate import validate_new_url

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")


def conversion_array(song):  # removes the links url from the list of needed conversion
    platform_array = ["Spotify",
                      "Apple Music",
                      "Youtube",
                      "Soundcloud"]

    if song.platform in platform_array:
        platform_array.remove(song.platform)

    convert_google_search(platform_array, song)


def convert_google_search(plat_list, song_obj):
    print(f"Song: {song_obj.name} - {song_obj.artist}\nGiven {song_obj.platform} url: {song_obj.url}\n\n")

    for plat in plat_list:  # for all platforms in the platform_array:
        query = song_obj.name + song_obj.artist + plat  # create string to be Google searched

        if plat == "Apple Music":
            plat = "apple"

        # tld = "co.in"
        for j in search(query, num=1, stop=1, pause=secrets.randbelow(3), user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'):
            valid = validate_new_url(plat.lower(), j, song_obj)  # sends original song to be checked against the new url
            if valid:
                print(f"{plat}: {j}\n")
            else:
                print(f"{plat}: Couldn't find a good match... Sorry!")

        print("----------------")
