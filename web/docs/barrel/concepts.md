# Concepts de Barrel-DB

## Base de données orientées documents

Barrel-DB est un base de données orientée documents. Vous stockez et retrouvez des
documents json à l'aide d'une API REST. Vous disposez des methodes POST, PUT et
DELETE pour manipuler les documents.

Les urls des documents prennent la forme:

    GET /<store>/<docid>

Par exemple:

    GET /source/cat


Pour créer un nouveau documents, nous pouvons renseigner le champ `id` avec l'id du document:

```js
POST /source
{
  'id': 'cat',
  'name': 'Tom'
}
```

Si nous ne donnons pas d'`id` au document, barrel calculera un identifiant
unique que l'on peut retrouver dans le body du résultat de la requete HTTP.

```js
POST /source
{
  'name': 'Tom'
}

Body de la requete au retour:
{
  'id': 'Tom'
}
```


## Gestion des conflits


## Ecouter les évenements de mises à jour

