#!/usr/bin/env python

from barrel import Store

store = Store('http://localhost:8080/source')

# Post a document without an id
doc = {'name': 'tom'}
r = store.post(doc)

# Get it back
docid = r['id']
print store.get(docid)

# Put a document with given id
dog = {'id': 'dog', 'name': 'dingo'}
store.put(dog)

dog = store.get('dog')

print(dog)

# Delete the document
store.delete('dog', dog['_rev'])

print(store.get('dog'))
