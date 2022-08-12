import requests

x = requests.get(
    'https://www.googleapis.com/customsearch/v1?key=AIzaSyCAQFXNFFbJ2h5Zh2spj8DYhdBnJmGhr7s&cx=d9293a34d8862f4b9&q=Drake Jungle')
raw_response = x.json()

result_arr = raw_response['items']

spotify_found = False
apple_found = False
amazon_found = False
tidal_found = False
youtube_found = False

all_found = False
# while all_found is not True:
if spotify_found and apple_found and amazon_found and tidal_found is True:
    all_found = True

for link in result_arr:
    print(f"{link['link']}\n")
    if 'spotify' in link['link'] and spotify_found is not True:
        spotify_found = True
        print(f" Spotify Link: {link['link']}")
    if 'apple' in link['link'] and apple_found is not True:
        apple_found = True
        print(f" Apple Music Link: {link['link']}")
    if 'amazon' in link['link'] and amazon is not True:
        amazon = True
        print(f" Amazon Music Link: {link['link']}")
    if 'tidal' in link['link'] and tidal_found is not True:
        tidal_found = True
        print(f" Tidal Link: {link['link']}")
    if 'youtube' in link['link'] and youtube_found is not True:
        youtube_found = True
        print(f" Tidal Link: {link['link']}")

    # if all_found is not True:
    #     result_arr = raw_response['queries']['nextPage']

# json_formatted_str = json.dumps(raw_response, indent=4)
# print(json_formatted_str)
