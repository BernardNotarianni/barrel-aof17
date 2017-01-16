# Administration de Barrel

Cette page présente quelques commandes de base pour administrée
la base de données en cas de problèmes.

Ces commandes nécessite un accès SSH au serveur. Demandez à Bernard
qu'il vous communique ces accès si vous pensez que vous en avez besoin.

Démarrer le service:

    $ sudo systemctl start barrel.service

Consulter le log du service:

    $ journalctl -u barrel.service

Status du service:

    $ systemctl status barrel.service


## Installation du service systemd

    $ cd /etc/systemd/system
    $ sudo cp /home/bernard/barrel/barrel-aof17/admin/barrel.service
    $ sudo systemctl enable barrel.service
    $ sudo systemctl start barrel.service
    $ systemctl status barrel.service

## Connection du serveur au wifi

Source: https://doc.ubuntu-fr.org/wifi

Lister les périphériques réseaux supportant le Wifi:

    $ iw dev

Démarrer le reseau sur `wlp2s0`

    $ sudo ifconfig wlp2s0 up

Lister les réseaux visibles sur l'interface `wlp2s0`:

    $ sudo iw dev wlp2s0 scan | grep SSID

## Scan de l'IP du serveur barrel
   
    $ sudo nmap -sS -p 22 192.168.1.0/24 | grep barrel

