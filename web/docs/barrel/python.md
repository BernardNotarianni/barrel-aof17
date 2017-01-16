# Librairie Python

Vous pouvez utiliser la librairie [`barrel.py`](/git/?p=barrel-aof17.git/.git;a=blob;f=clients/python/barrel.py) pour acceder facilement
à une base Barrel.

N'oubliez pas d'installer les dependances nécessaire:

    $ pip install requests
    $ pip install sseclient

## Ouvrir une base de donnée

```python
from barrel import Database

database_url = "http://192.168.1.89:8080/source"
database = Database(database_url)
``` 

L'objet `database` ainsi créé peut etre utilisé pour toutes
les opérations sur barrel.

## Lire un document

Lire la dernière version d'un document:

```python
from barrel import Database

database = Database(database_url)
doc = database.get(docid)
```

## Créer un document

Utilisez la méthode `put` pour créer ou mettre à jour un document.
N'oubliez pas de bien renseigner le champ `id` obligatoire:

```python
database = Database(database_url)
doc = {'id': 'chat', 'message': 'hello world'}
database.put(doc)
```

Vous pouvez utiliser `post` si vous souhaitez laisser le serveur
assigner lui-même un `id` unique:

```python
database = Database(database_url)
doc = {'message': 'hello world'}
database.post(doc)
```

## Mettre à jour un document existant

Un simple appel à la methode `put` permet de mettre à jour un doc existant.
Prenez bien soin de vérifier que le champ `_rev` correspond bien à la dernière
révision du document.

```python
database = Database(database_url)
doc = database.get('chat')
doc['message'] = 'hello world'
database.put(doc)
```

## Supprimer un document

```python
database = Database(database_url)
doc = database.get('chat')
database.delete(doc)
```

## Ecouter les évenements de mises à jour

La méthode `changes(regex)` retourne un stream des documents qui ont été modifiés, dont le `docid`
match la regexp en parametre.

```python
database = Database(database_url)
for doc in database.changes('^chat'):
    print(doc['message'])
```

