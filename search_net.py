from googlesearch import search
import urllib.request
from bs4 import BeautifulSoup
from song import *


def get_platform(url):
    if 'apple' in url:
        return 'Apple Music'
    elif 'spotify' in url:
        return 'Spotify'


def get_artist(st):
    no_name = st.split('by')[1]
    pre_plat = no_name.split('on')[0]
    remove_platform = pre_plat.split('|')[0]  # removes '|'

    artist = remove_platform  # sets to artist for readability

    return artist.strip()


def get_name(st):
    remove_by = st.split('by')[0]  # removes 'by'
    remove_dash = remove_by.split('-')[0]  # removes '-'
    remove_song = remove_dash.split('song')[0]  # removes 'song'

    name = remove_song  # set to name for readability

    string_unicode = name
    string_encode = string_unicode.encode("ascii", "ignore")
    string_decode = string_encode.decode()

    return string_decode


def google_scrape(url):
    # parses html to get text of the Google search page
    the_page = urllib.request.urlopen(url)
    soup = BeautifulSoup(the_page, "html.parser")
    return soup.title.text


def populate_song(google_title, s):
    s.name = get_name(google_title)
    s.artist = get_artist(google_title)
    s.platform = get_platform(s.url)
    return s


def searching(url):
    # takes a url from processing and scrapes googles home page
    # prints out the first 10 results
    s = Song()
    s.url = url

    # for url in search(url, stop=10): #  changes the amount of results returned
    g_title = google_scrape(url)
    populate_song(g_title, s)

    # print(song.name)
    # print(song.artist)
    # print(song.platform)
    # print(song.url)

    return s  # CHECK IF NEED s OR song VARIABLE

