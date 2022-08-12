from collecturl import collect_url
from search_net import searching
from newplat_convert import conversion_array

def process(stream):
    # node function connecting the application processes

    url = collect_url(stream)  # get url from cmd args
    song_obj = searching(url)  # get data from Google search and put into song object
    conversion_array(song_obj)
