import requests

people_url = 'http://pantheon.media.mit.edu/people_9-30-2015.json'

def get_people(*args, **kw):

    req = requests.get(people_url)

    #TODO Add filters
    return req.json()