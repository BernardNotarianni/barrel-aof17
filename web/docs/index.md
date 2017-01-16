# Bienvenue sur Barrel-DB!

Ce serveur est à votre disposition pour jouer avec Barrel-DB.

Vous pouvez utiliser Barrel en utilisant une des 3 API suivantes:

* [Une API REST standard](barrel/rest.md)
* [Une librairie Python](barrel/python.md)
* [Une librairie Elixir](barrel/elixir.md)


## Jouer directement sur ce serveur

Vous pouvez vous connecter en SSH sur ce serveur en utilisant le compte d'invité:

    Login: aof
    Password: aof

Pour tester le chat, vous pouvez dans un terminal lancer le chat Python:

```sh
$ cd barrel-aof17/clients/python
$ python chat.py
```
Puis dans un autre terminal lancer le chat Elixir:

```sh
$ cd barrel-aof17/clients/elixir
$ iex -S mix
> Barrex.Chat.receiver()
```

Enfin, tapez quelques messages dans le chat python pour les voir apparaitre en temps réel
dans le chat Elixir :-)

## Jouer depuis votre ordinateur



## Quelques liens utiles

* L'API REST de Barrel est disponible sur ce serveur sur le port 8080
* Un swagger est disponible sur ce serveur (port 8080) sur l'url `/api-docs`
* Un wiki est disponible sur le port 8001 de ce serveur
* Une [page de download](/downloads) avec quelques utilitaires
