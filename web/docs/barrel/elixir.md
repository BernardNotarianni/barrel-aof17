# Librairie Elixir

Vous pouvez utiliser la librairie [`Barrex.Databas`](/git/?p=barrel-aof17.git/.git;a=blob;f=clients/elixir/lib/barrex.ex) pour acceder facilement
à une base Barrel.

N'oubliez pas d'installer les dependances nécessaire:

    $ cd clients/elixir
    $ mix deps.get
    $ mix compile

Pour lancer un shell incluant les librairies et dependances:

    $ iex -S mix

## Ouvrir une base de donnée

```elixir
database_url "http://192.168.1.89:8080/source"
db = Barrex.Database.open(database_url)
``` 

L'objet `db` ainsi créé peut etre utilisé pour toutes
les opérations sur barrel.

## Lire un document

Lire la dernière version d'un document:

```elixir
doc = Barrex.Database.get("chat", db)
IO.puts doc["message"]
```
## Créer un document

Utilisez la méthode `put` pour créer ou mettre à jour un document.
N'oubliez pas de bien renseigner le champ `id` obligatoire:

```elixir
doc = %{"id" => "chat", "message" => "hello world"}
Barrex.Database.put(doc, db)
```

Vous pouvez utiliser `post` si vous souhaitez laisser le serveur
assigner lui-même un `id` unique:

```elixir
doc = %{"message" => "hello world"}
Barrex.Database.post(doc, db)
```

## Mettre à jour un document existant

Un simple appel à la methode `put` permet de mettre à jour un doc existant.
Prenez bien soin de vérifier que le champ `_rev` correspond bien à la dernière
révision du document.

```elixir
doc = Barrex.Database.post("chat", db)
doc["message"] = "hello world"
Barrex.Database.put(doc)
```

## Supprimer un document

```elixir
doc = Barrex.Database.get("chat", db)
Barrex.Database.delete(doc, db)
```

## Ecouter les évenements de mises à jour

La méthode `changes(db)` retourne un [stream](https://hexdocs.pm/elixir/Stream)
des documents qui ont été modifiés.

```elixir
db = Barrex.Database.open(url)
Barrex.Database.changes(db)
  |> Stream.filter(fn(doc) -> doc["id"] == "chat" end)
  |> Stream.map(fn(doc) -> IO.puts doc["message"] end)
  |> Stream.run
```

