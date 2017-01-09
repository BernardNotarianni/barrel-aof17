#!/usr/bin/env python

import json
import pprint
import requests
import sseclient


url = 'http://localhost:8080/source/_changes?feed=eventsource'
response = requests.get(url, stream=True)
client = sseclient.SSEClient(response)

for event in client.events():
    pprint.pprint(json.loads(event.data))
