#!/usr/bin/env python

import requests

from oauth_hook import OAuthHook

from throttle import throttle_hook

from settings import *

def example():
    oauth_hook = OAuthHook(access_token=OAUTH_TOKEN, access_token_secret=OAUTH_SECRET, 
                           consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, 
                           header_auth=False)

    client = requests.session(hooks={'pre_request': oauth_hook, 'response': throttle_hook})

    return client.get("https://api.twitter.com/1/users/show.json?screen_name=steveWINton")

if __name__ == "__main__":
    resp = example()
    print resp.content

