import requests
import requests as requests
import json
from pprint import pprint
r = requests.get('https://www.strava.com/api/v3/athlete/activities/?access_'
                 'token=f380b4d526a251e907aab630589de6731acf69bd')
pprint(r.json())
