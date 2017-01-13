#!/usr/bin/env python

from barrel import Database

database = Database('http://localhost:8080/source')

# Post a document without an id
doc = {'name': 'tom'}
r = database.post(doc)

# Get it back
docid = r['id']
print database.get(docid)

# Put a document with given id
dog = {'id': 'dog', 'name': 'dingo'}
database.put(dog)

dog = database.get('dog')

print(dog)

# Delete the document
database.delete('dog', dog['_rev'])

print(database.get('dog'))
