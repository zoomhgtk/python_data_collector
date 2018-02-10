#! /usr/bin/env/python3

# download every single XKCD comic
# example from "Automate the boring stuff with python"

import requests, os, bs4

base_url = 'http://xkcd.com'
os.mkdirs('xkcd', exist_ok=True) # store comic in this dir

while not url.endwith('#'):
    # xkcd's very first comic's url ends with a numbersign #
    
    # TODO: Download the page

    # TODO: Find the URL of the comic image

    # TODO: Download the image

    # TODO: Save the image to ./xkcd

    # TODO: Get the "Prev" button's url

print ('Done.')
