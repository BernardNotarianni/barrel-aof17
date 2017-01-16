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

# API REST

## Header HTTP

Pour toute les requêtes HTTP, inclure dans le header `Content-Type: application/json`

Il n'y pas de filtre d'autorisation: tout le monde a accès à tout sur l'API HTTP Rest de ce serveur.

## `GET /<store>/<docid>`

Request:
```json
GET /source/chat
```

Reply:
```json
{
  "_rev": "1-435823fe88aa55869cba856df1a2d570",
  "id": "chat",
  "name": "tom"
}
```

## `POST /<store>`

Request:
```json
POST /source
{
  "name": "tom"
}
```

Reply:
```json
{
  "id": "98d5b5c8-af18-453a-bfb9-b0c6ca0da19b",
  "ok": true,
  "rev": "1-ddffb068a15dda0cf75c2e9223e375fa"
}
```

## `PUT /<store>/<docid>`

### Création d'un document

Il faut indiquer le même *docid* dans l'URL de la requete et dans le champ `id` du document JSON.

```json
PUT /source/chat
{
  "id": "chat",
  "name": "tom"
}
```

Reply:
```json
{
  "id": "chat",
  "ok": true,
  "rev": "1-435823fe88aa55869cba856df1a2d570"
}
```

### Mise à jour d'un document existant

Pour mettre à jour un document, il faut indiquer précisement le dernière révision dans le champ `_rev`.

```json
PUT /source/chat
{
  "_rev": "1-435823fe88aa55869cba856df1a2d570",
  "id": "chat",
  "name": "Grumpy Cat"
}
```

Reply:
```json
{
  "id": "chat",
  "ok": true,
  "rev": "2-8cfbb3023f94ddd1f1bf6ee7a9ba2019"
}
```

## `DELETE /<store>/<docid>`

Pour supprimer un document, indiquer dans le parametre d'URL `rev` la dernière révision.

```text
DELETE /source/chat?rev=2-8cfbb3023f94ddd1f1bf6ee7a9ba2019
```

Reply:
```json
{
  "id": "chat",
  "ok": true,
  "rev": "3-8a17b246465973518019470d6b4540fd"
}
```

## `GET /<store>/_all_docs`

Liste tous les documents disponibles dans un store:

```text
GET /source/_all_docs
```

Reply:
```json
{
  "offset": 0,
  "rows": [
    {
      "id": "chat",
      "rev": "3-8a17b246465973518019470d6b4540fd"
    },
    {
      "id": "98d5b5c8-af18-453a-bfb9-b0c6ca0da19b",
      "rev": "1-ddffb068a15dda0cf75c2e9223e375fa"
    }
  ],
  "total_rows": 2
}
```

## `GET /<store>/_changes?feed=eventsource`

Informe de toutes les modifications de doducment d'un store sous la forme de
[Server Sent Events](https://www.w3.org/TR/eventsource/) HTTP.

```text
GET /source/_all_docs
```

Reply:
```json
id: 546386C4D14C0
data: {"last_seq":7,"results":[]}

id: 546386CDC2CE0
data: {"last_seq":8,"results":[{"changes":["1-6a5f1ebdc7e3b20430b8b834dd505e32"],"id":"51b38616-b2fe-4772-9dbe-6c06575961d7","seq":8}]}

id: 546386D507634
data: {"last_seq":9,"results":[{"changes":["1-88ba268c6c1ba33270411ac6666a7fe1"],"id":"2285c50e-c30a-4aeb-ace8-10c5befb09bc","seq":9}]}
```