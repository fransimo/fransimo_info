---
title: 'Shared Folder (Red box)'
date: '2016-05-07T19:51:21+02:00'
author: fran
aliases: /es/blog/2016/05/07/shared-folder-red-box/
image: DSCF3138.jpg
---
![Sahred folder box](DSCF3138.jpg)

````
Libro de artista  
10,50 x 20,50 x 38cm  
29 páginas A4 80gm  
57 fotografías 13x18cm  
6 Carpetas
````

# Shared Folder (Red box)



Cuando la _[found photography](https://en.wikipedia.org/wiki/Found_photography)_ entra en la era digital se basa en imagenes encontradas en webs públicas, como redes sociales: Flickr, Instagram, Google Street View. En todos estos casos el creador de las imágenes tuvo la intención de hacer estas imágenes accesibles (aunque solo fuera por una obligación legal, como los sistemas de vigilancia)

La _found phtography_ original trabajaba sobre imágenes que nunca tuvieron las intención de ser públicas. Sus autores no las publicaron. Se mantuvieron en cajas por años.

Me pregunté a mi mismo ¿Dónde puedo encontrar esas imágenes? ¿Dónde están las imágenes digitales que nunca se han querido hacer públicas? ¿Debería comprar discos duros obsoletos en los marcados de pulgas? ¿Debería hackear maliciosamente ordenadores?

![DSCF3142](DSCF3142.jpg)

Entonces recordé el antiguo protocolo eDonkey y sus clientes primitivos.

A principio de los 2000 la instalación de algunos de estos programas tenía por costumbre compartir la carpeta «Mis Documentos». Windows ubicaba “Mis Fotos” dentro de “Mis Documentos”. Por eso, cualquier instalación por defecto compartía todas las fotos que habían sido descargadas de las cámaras digitales o teléfonos.

¿Hay personas compartiendo todas sus imágenes por error sin saberlo? ¿Cuanta información privada están compartiendo?

En 2015 comencé una búsqueda sistemática de imágenes en la red ed2k.

_Shared folder_ muestra lo que descubrí

![](DSCF3150.jpg)

# Datos técnicos

## El libro



Quise que el espectador tuviera la misma sensación que tuve cuando vi las imágenes, transformando una experiencia digital/mental en una física.

**¿Cuánto vas a descubrir acerca de esta gente?**

Encontrarás una caja y la abrirás. Dentro descubirás carpetas que contienen información personal e íntima sobre personas. Los datos relevantes están enmascarados, pero puedes quitar los [gommettes](https://www.google.es/search?q=gommettes&espv=2&biw=1437&bih=778&source=lnms&tbm=isch&sa=X&ved=0ahUKEwie17Ki1NHMAhUK1B4KHdUbBbAQ_AUIBigB) (pegatinas), la tinta que está tapada con Tipp-ex puede verse a contra luz. Los links ed2k están ahí, solo necesitas pegarlos en un cliente eDonkey y descargarás las mismas fotos que encontré. El código que usé para las búsqueda masiva es público.

Asumo que las imágenes han sido compartidas por error. **¿Seguir con esta investigación es una violación a la intimidad?** Creé el libro como un medio para poner a los espectadores en la posición de elegir.

**¿Cuántos datos o imágenes estás compartiendo sin saberlo?**

## La maqueta del libro

El libro final será una caja con carpetas dentro, con la mismas dimensiones que la maqueta. Contendrá imágenes y páginas dentro de las carpetas. Las fotografías tendrán gommettes sobre ellas. Las páginas tendrá Tipp-ex sobre la información sensible.

Algunos detalles podrían cambiar para evitar marcas comerciales y mejorar la calidad general del objeto.

## Búsqueda

Para buscar y descargar utilicé el servidor mldonkey. Tiene una interfaz que permite la automatización de las búsquedas y descargas. Parte de las búsquedas fueron manuales, especialmente para las fotografías en formato RAW. Para los JPGs utilicé un algoritmo muy sencillo que buscaba el patrón: IMG\_0001, IMG\_0002, IMG\_0003…

Puedes encontrar el código aquí [https://github.com/fransimo/shared\_folder](https://github.com/fransimo/shared_folder) (GPL license).

## Clasificación

Utilicé el número de serie de la cámara que está disponible en los EXIFs para el primer sistema de agrupación. Este dato me daba la oportunidad de seguir a una cámara.

Para los móviles, que no registran el número de serie, usé los datos GPS. Las fotografías que tenían datos de GPS se agrupaban por ubicación y luego las verifiqué manualmente.

## Estadísticas

La biblioteca contiene 17934 fotografías, después de haber borrado la pedofilia, que representaba el 13% de las descargas.

4469 imágenes tenían datos del número de serie (3747 eran JPGs y 722 RAWs)  
2405 imágenes tenían datos GPS.


![](DSCF3152.jpg)

# Contenido completo

{{< embedpdf url="Shared_folder_with_photos_and_scan.pdf" >}}
[PDF Download](Shared_folder_with_photos_and_scan.pdf)
