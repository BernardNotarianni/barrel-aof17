# Bienvenue sur Barrel-DB!

Ce serveur est à votre disposition pour jouer avec Barrel-DB.

Vous pouvez utiliser Barrel en utilisant une des 3 API suivantes:

* [Une API REST standard](barrel/rest.md)
* [Une librairie Python](barrel/python.md)
* [Une librairie Elixir](barrel/elixir.md)

Ces API sont relativement simples et peuvent éventuellement servir de modèle
si vous souhaitez implémenter une librairie client pour votre langage préféré
(Ruby, JS, F#, Haskell, Elm, PHP etc..)

N'hésitez pas à contribuer et nous tenir informés pendant ou après l'Agile Open :-)

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

Le plus simple est de cloner le repo git contenant les exemples.

Cloner le [repo original github](https://github.com/BernardNotarianni/barrel-aof17):

    $ git clone https://github.com/BernardNotarianni/barrel-aof17.git

Cloner le mirroir disponible sur ce serveur, pour l'utilisateur `aof`:

    $ git clone aof@<IP de ce serveur>:/home/aof/barrel-aof17

Le mot de passe de l'utilisateur `aof` est `aof`.

Par exemple sur une machine Windows:

```text
C:\Users\berna>git clone aof@192.168.1.89:/home/aof/barrel-aof17
Cloning into 'barrel-aof17'...
The authenticity of host '192.168.1.89 (192.168.1.89)' can't be established.
ECDSA key fingerprint is SHA256:ZFFeMsqka8jJeMWptx7dAM3cbp24dpTzVIT/E2VIGso.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.1.89' (ECDSA) to the list of known hosts.
aof@192.168.1.89's password: <entrez le mot de passe aof>
remote: Counting objects: 255, done.
remote: Compressing objects: 100% (175/175), done.
rRemote: Total 255 (delta 60), reused 247 (delta 57)
Receiving objects: 100% (255/255), 1.40 MiB | 2.61 MiB/s, done.
Resolving deltas: 100% (60/60), done.
Checking connectivity... done.

C:\Users\berna>dir barrel-aof17
 Le volume dans le lecteur C n’a pas de nom.
 Le numéro de série du volume est 52A8-97FB

 Répertoire de C:\Users\berna\barrel-aof17

16/01/2017  16:21    <DIR>          .
16/01/2017  16:21    <DIR>          ..
16/01/2017  16:21    <DIR>          admin
16/01/2017  16:21    <DIR>          clients
16/01/2017  16:21            11 357 LICENSE
16/01/2017  16:21                94 README.md
16/01/2017  16:21    <DIR>          web
               2 fichier(s)           11 451 octets
               5 Rép(s)  20 346 445 824 octets libres

C:\Users\berna>
```

## Acceder aux stores/bases de données barrel

Ce serveur contient une instance de barrel par défaut, configuré sur le **port 8080**.
Celcui est configuré avec deux store (base de données) par défaut:

* source
* targedb

Vous pouvez par exemple faire un `HTTP GET /_stores` pour récupérer la liste des stores disponibles.

## Quelques liens utiles

* L'API REST de Barrel est disponible sur ce serveur sur le port 8080
* Un swagger est disponible sur ce serveur (port 8080) sur l'url `/api-docs`
* Un wiki est disponible sur le port 8001 de ce serveur
* Une [page de download](/downloads) avec quelques utilitaires
