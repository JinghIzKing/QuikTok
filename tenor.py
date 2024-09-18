import requests
import json
import os

def fetchURL(searchTerm: str) -> str:
    # set the apikey and limit
    apikey = "ADD YOUR TENOR API KEY HERE"  # set to your apikey
    lmt = 1
    ckey = "my_test_app"  # set the client_key for the integration and use the same value for all API calls

    # our test search
    search_term = searchTerm

    # get the top 1 GIFs for the search term
    r = requests.get(
        "https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (search_term, apikey, ckey,  lmt))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_1gifs = json.loads(r.content)
        print(top_1gifs)
        gif_url = top_1gifs['results'][0]['media_formats']['gif']['url']
    else:
        top_1gifs = None
    return gif_url
