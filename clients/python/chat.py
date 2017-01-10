#!/usr/bin/env python

import requests
import sseclient
import json

from threading import Thread

url = 'http://localhost:8080/source/chat'


def read_doc():
    r = requests.get(url)
    if r.status_code == 404:
        return {'id': 'chat', 'message': ''}
    return r.json()


class Sender(Thread):

    """This thread sends your message to the server"""

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        headers = {'Content-Type': 'application/json'}
        while True:
            message = raw_input('Your message:')
            doc = read_doc()
            doc['message'] = message
            headers = {'Content-Type': 'application/json'}
            requests.put(url, headers=headers, data=json.dumps(doc))


class Receiver(Thread):

    """This thread receives and print messages from the server"""

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        url = 'http://localhost:8080/source/_changes?feed=eventsource'
        response = requests.get(url, stream=True)
        client = sseclient.SSEClient(response)

        for event in client.events():
            doc = read_doc()
            print(doc['message'])


thread1 = Sender()
thread2 = Receiver()

thread1.start()
thread2.start()
