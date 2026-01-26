---
title: 'Cartella Condivisa (Scatola Rossa)'
description: "Descrive Cartella Condivisa, un'opera d'arte che raccoglie fotografie condivise inavvertitamente tramite reti peer‑to‑peer, invitando gli spettatori a esplorare le immagini trovate e riflettere sulla privacy nell'era digitale."
date: '2016-05-07T19:51:21+02:00'
author: "Fran Simó"
images:
  - DSCF3138.jpg
dateCreated: 2016
artForm: Libro d'arte
schemaOrgType: VisualArtwork
BookToC: true
categories:
- arte dei nuovi media
tags:
- cybersecurity
- e2dk
- edonkey
- fotografia trovata
- reti grigie
- intimità
- fotografia
- post fotografia
- privacy
---

![Sahred folder box](DSCF3138.jpg)

{{% details title="Dettagli tecnici" open=true %}}
```
Art book (2015-2016)
10,50 x 20,50 x 38cm
29 A4 80gm pages
57 13x18cm photographs  
6 Folders
```
{{% /details %}}

# Cartella Condivisa (Scatola Rossa)

Nel contesto dell'era digitale, _[fotografia trovata](https://en.wikipedia.org/wiki/Found_photography)_ significa immagini trovate su siti pubblici come i social network, ad es. Flickr, Instagram, Google Street View, ecc. In questi casi, l'autore delle immagini intendeva renderle accessibili (anche se solo per obbligo legale, come accade con le registrazioni di sorveglianza).

Ma la fotografia trovata originale riguardava foto che non erano mai state destinate a essere pubbliche. I loro autori non le avevano pubblicate. Erano state conservate in scatole per anni.

Mi sono chiesto: dove posso trovare queste immagini? Dove sono le immagini digitali che non erano mai state destinate a essere mostrate? Dovrei comprare hard drive obsoleti nei mercatini dell'usato? Dovrei hackerare maliziosamente computer online?

![DSCF3142](DSCF3142.jpg)

Poi mi sono ricordato il protocollo di condivisione old-school: eDonkey con i suoi client primitivi.

All'inizio degli anni 2000 l'installazione del client ed2k di solito condivideva automaticamente la cartella “My Documents”. Windows metteva “My Photos” sotto “My Documents” così qualsiasi installazione standard condivideva tutte le fotografie scaricate da fotocamere digitali e telefoni.

Le persone condividono tutte le loro immagini per errore senza saperlo? Quanta informazione privata stanno condividendo?

Nel 2015 ho iniziato a cercare sistematicamente immagini nella rete ed2k.

_Cartella Condivisa_ mostra ciò che ho scoperto.

![](DSCF3150.jpg)

# Dati tecnici

## Il libro

Voglio che lo spettatore abbia la stessa esperienza che ho quando cerco immagini, trasformando un'esperienza mentale/digitale in una fisica.

**Quanto scoprirai su queste persone?**

Troverai una scatola e la aprirai. All'interno scoprirai cartelle che contengono informazioni personali/intime su quelle persone. I dati sono mascherati ma se rimuovi le gommette, l'inchiostro sotto la correzione (Tipp-ex) è visibile contro la luce. I link ed2k sono lì, devi solo incollarli in un client ed2k. Ho reso il codice pubblico per eseguire una ricerca massiva.

Presumo che le immagini siano condivise per errore. **Andare oltre nell'investigazione è una violazione dell'intimità?** Creo il libro come un mezzo per mettere il pubblico nella posizione di scegliere.

**Quanti dati/immagini stai condividendo senza saperlo?**

## Dummy del libro

Il libro finale sarà una scatola con cartelle all'interno con le stesse dimensioni del dummy. Conterrà foto e pagine all'interno delle cartelle. Le foto avranno gommette su di esse.  
Le pagine avranno Tipp-ex sopra i dati sensibili.  
Alcuni dettagli possono essere cambiati per evitare pubblicità di marchi commerciali e migliorare la qualità complessiva dell'oggetto.

## Ricerca

Per cercare e scaricare uso il server mldonkey. Ha un'interfaccia per automatizzare azioni come ricerche e download. Parte della ricerca è stata manuale, principalmente file RAW. Per JPG ho usato un semplice algoritmo che cerca il pattern IMG_0001, IMG_0002, IMG_0003…

Puoi trovare il codice qui https://github.com/fransimo/shared_folder (licenza GPL)

## Classificazione

Uso il numero di serie della fotocamera nei dati EXIF per il primo raggruppamento. Questo mi dà l'opportunità di seguire una fotocamera.

Per le immagini del telefono cellulare che non hanno numero di serie, uso i dati GPS. Tutte le immagini con dati GPS sono raggruppate manualmente e io personalmente controllo i pattern.

## Statistiche

La libreria contiene 17934 immagini dopo aver eliminato le immagini pedofile, che rappresentano il 13% dei file scaricati.  
4469 immagini hanno numero di serie della fotocamera (3747 sono JPG e 722 RAW)  
2405 immagini hanno dati GPS.

![](DSCF3152.jpg)

# Contenuto completo

{{< embedpdf url="Shared_folder_with_photos_and_scan.pdf" >}}
[PDF Download](Shared_folder_with_photos_and_scan.pdf)

