#!/usr/bin/env python

from barrel import Store
from threading import Thread

store_url = 'http://localhost:8080/source'
docid = 'chat'

store = Store(store_url)


def read_doc():
    doc = store.get(docid)
    if doc is None:
        return {'id': 'chat', 'message': ''}
    return doc


class Sender(Thread):

    """This thread sends your message to the server"""

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            message = raw_input('Your message:')
            doc = read_doc()
            doc['message'] = message
            store.put(doc)


class Receiver(Thread):

    """This thread receives and print messages from the server"""

    def __init__(self):
        Thread.__init__(self)

    def run(self):

        for doc in store.changes(docid):
            print(doc['message'])


thread1 = Sender()
thread2 = Receiver()

thread1.start()
thread2.start()
