# Concepts de Barrel-DB

## Base de données orientées documents

Barrel-DB est un base de données orientée documents. Vous stockez et retrouvez des
documents json à l'aide d'une API REST. Vous disposez des methodes POST, PUT et
DELETE pour manipuler les documents.

Les urls des documents prennent la forme:

    GET /<store>/<docid>

Par exemple:

    GET /source/cat


Pour créer un nouveau documents, nous pouvons renseigner le champ `id` avec l'id du
document:

```js
POST /source
{
  'id': 'cat',
  'name': 'Tom'
}
```

Si nous ne donnons pas d'`id` au document, barrel calculera un identifiant
unique (de type GUID) que l'on peut retrouver dans le body du résultat de la requete HTTP.

```js
POST /source
{
  "name": "Tom"
}

Body de la requete au retour:
{
  "id": "b0bd800d-58e2-4279-a5fe-c8e21dbe3040",
  "ok": true,
  "rev": "1-4ce4351b36db87b1b455421d9e0be43b"
}
```


## Gestion des conflits: utiliser les révisions

Barrel utilise un mecanisme de mises à jour concurrentes des documents de type "optimiste".
Il n'y a pas de système de transaction ou de "lock".

Pour vérifier que personne n'a pas modifier votre document entre le moment où vous l'avez lu
et celui ou l'écriture se déroule, vous devez utiliser le champs `rev` automatiquement
généré à chaque création ou mise à jour d'un document.

Ce champ est constitué d'un numéro de sequence incrémenté à chaque mise à jour et d'un MD5
calculé à partir du contenu du document.

Exemples:

```
1-4ce4351b36db87b1b455421d9e0be43b
2-7dce3773ba098f2c09b24697af544e63
3-dce8a2ab14c7e40b60c6550e8af8d0a5
```

Lors d'une mise à jour avec `PUT` ou d'une suppression avec `DELETE` vous devez indiquer
la dernière revision du document que vous voulez mettre à jour. Si lors de l'opération
Barrel se rend compte que la révision ne correspond pas, c'est probablement que quelqu'un d'autre
a mise à jour le document entre temps. Il vous retourne alors un code erreur 409 "Conflict"

Vous pouvez alors essayer de relire le document afin
de retrouver la denière révision et réassyer jusqu'à ce que cela passe.

```text
Pour mettre à jour un document:
1 - Lire le document
2 - Modifier le document
3 - Faire un PUT pour mettre à jour le document
4 - Si vous avez un code erreur 409, reprendre à l'épate 1
```

## Ecouter les évenements de mises à jour

