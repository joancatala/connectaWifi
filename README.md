* Aquest script s'anomena conectaWifi.py
Aquest script conectaWifi es una utilitat escrita amb Python que m'he preparat per a conectar el meu Thinkpad x250 amb OpenBSD 6.3 de manera que configure un fitxer hostname.iwm0 per a connectar-me a un wifi als llocs on normalment em connecte.

Fins ara ho feia manualment i modificaba o comentaba el fitxer de configuracio, pero amb aquest script ja ho tinc automatitzat.

https://github.com/joancatala/conectaWifi/blob/master/captura-pantalla.png

* Com Funciona

A OpenBSD jo tinc la interficie iwm0:

bash-4.4$ dmesg | grep iwm0
iwm0 at pci2 dev 0 function 0 "Intel Dual Band Wireless AC 7265" rev 0x61, msi
iwm0: hw rev 0x210, fw ver 16.242414.0, address 34:02:86:e7:01:a8
bash-4.4$

Simplement cal crear tants fitxers /etc/hostname.iwm0-n com vullgues. Per exemple, a l'opcio 1 del menu tinc el fitxer /etc/hostname.iwm0-1, a l'opcio 2 del menu tinc /etc/hostname.iwm0-2, i aixi totes les altres.

Normalment, el fitxer te les seguents linies:

nwid EL_TEU_NOM_DE_LA_WIFI
wpakey CONTRASENYA
dhcp 

Jo tinc sempre DHCP, pero tu pots configurar-te les Wifis com vullgues.

I aleshores, executant-lo, tenim en dos segons el nostre sistema connectat a la xarxa.

I aixo es tot.