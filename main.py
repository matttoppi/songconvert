# main file for song convert
import spotipy
from spotipy import SpotifyOAuth

from process import process
import sys
import requests
import json


def main():
    i_stream = sys.argv  # takes the cmd arguments and sets them to i_stream array
    process(i_stream)
    exit(0)


if __name__ == "__main__":
    main()
