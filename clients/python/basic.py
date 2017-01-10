#!/usr/bin/env python

import requests
import json

store = 'http://localhost:8080/source'

print "post a document"

doc = {'name': 'tom'}
headers = {'Content-Type': 'application/json'}
r = requests.post(store, headers=headers, data=json.dumps(doc))
print r.status_code
docid = r.json()['id']
revid = r.json()['rev']


print "get the document"

r = requests.get(store + '/' + docid)
print r.status_code


print "delete the document"

r = requests.delete(store + '/' + docid + '?rev=' + revid)
print r.status_code
