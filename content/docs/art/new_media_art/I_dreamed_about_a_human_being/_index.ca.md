---
id: 8968
title: 'He somiat amb un ésser humà'
date: '2012-09-13'
author: "Fran Simó"
description: >
  "I dreamed about a human being" és una investigació artística que
  intenta abordar qüestions sobre la identitat, la privacitat, el creixent poder computacional 
  i la difusió d’algoritmes increïblement potents disponibles per al seu ús gratuït.
images:
  - fran_simo_0002_Untitled1_mean_.jpg
dateCreated: 2012
artForm: Photograph
schemaOrgType: VisualArtwork
BookToC: true
categories:
- new media art
- NFT
tags:
- artificial intelligence
- computer vision
- creative commons
- face detection
- faces
- flickr
- machine learning
- portraits
- post photography
- life
- opensea
- software
---
![fran_simo_0001_Untitled1_medium_.jpg](fran_simo_0001_Untitled1_medium_.jpg)

# He somiat amb un ésser humà

Com imaginarà un robot un rostre humà? “I dreamed about a human being” és com espiar dins del cervell d’un robot.“I dreamed about a human being” és part d’un projecte que explora l’ús de la intel·ligència artificial aplicada a la fotografia utilitzant codi i dades obertes a Internet. El projecte ja té una base de dades de 56 milions d’imatges. Tenim eines increïbles i bases de dades d’imatges gegants d’accés gratuït però no acabem de comprendre què podem fer amb elles o què significa que estiguin allà.

IDAAHB ens qüestiona sobre identitat, privacitat, l’increment del poder computacional i l’accés lliure a poderosos algoritmes matemàtics. Tot amb un sentit estètic i educacional.

Aquesta primera sèrie d’imatges és el resultat de càlculs estadístics sobre 257 rostre detectats per un algoritme que aprèn a reconèixer retrats amb una estètica específica. La cerca es va realitzar sobre 5 milions d’imatges publicades a Flickr amb llicències creative commons. “Mean”, la imatge de la dreta, és la mitjana d’aquestes 257 fotografies. Està composta per 17 nadons, 106 homes, 79 dones, 18 nines, 23 nens i 14 errors.

Una altra manera de percebre aquesta acumulació d’imatges és passar les imatges a tota velocitat desenfocant una mica la vista. Es pot apreciar el mateix “efecte mitjà” mirant el següent vídeo, que té 2582 imatges passant a una velocitat de 25 per segon <a href="http://vimeo.com/49552899">http://vimeo.com/49552899</a>

<strong>Actualització 14/2/2013</strong>: També podeu veure les "fulles de contacte" aquí <a title="Mugs from the cloud" href="http://cloudmugshots.fransimo.info/">http://cloudmugshots.fransimo.info/</a>

<strong>Actualització 6/8/2013</strong>: La base de dades ja conté 75 milions d’imatges i ha reconegut 345.625 cares.

<strong>Actualització 25/1/2015</strong>: La base de dades ja conté 88 milions d’imatges i ha reconegut 1.250.415 cares.

## L’algoritme

L’algoritme utilitzat per reconèixer els rostre és capaç de trobar qualsevol objecte dins d’una fotografia però per a això cal ensenyar-li què busquem amb imatges similars.

Quan vaig començar el projecte no m’interessava trobar cares sinó retrats amb una estètica definida. El primer pas va ser reunir una col·lecció de retrats que seguissin aquesta estètica perquè l’algoritme començés a aprendre.

La composició utilitzada per entrenar l’algoritme és un conjunt de rostre frontals amb il·luminació regular, ulls sota els punts d’intersecció superiors de la regla de terços i la boca al terció inferior mitjà. Retrats similars als de les fotos carnet o els “mug shots”, els retrats dels acusats de crims. L’objectiu era ensenyar l’algoritme a trobar retrats dins de les fotografies.

Dit amb altres paraules, l’algoritme reencuadra una fotografia per convertir-la en un retrat tipus foto carnet. És possible que en la fotografia no hi hagi rostre o que aquests no compleixin amb l’estètica desitjada, llavors es ignora.

A sota podem veure un exemple de l’algoritme funcionant. Una foto d’una persona amb un paisatge de fons. L’algoritme reconeix la cara i la encuadra. Veiem com els ulls tendeixen a estar a les línies centrals dels terços i la boca queda al terció inferior mitjà.

{{< figure
  src="ejemplo_recorte.png"
  alt="'Me on the top of matanga hill' by fraboof"
  link="http://www.flickr.com/photos/fraboof/2126593950/"
  caption="'Me on the top of matanga hill' by fraboof"
  class="image-general"
>}}

L’aprenentatge de l’algoritme és supervisat. Ensenyes, aprèn i l’avaluïs fins que el resultat és satisfactori. En cada iteració s’afegeixen rostre i se li expliquen els errors que ha comès.

Com a part de l’avaluació necessitava veure el conjunt d’imatges descrit estadísticament per la seva mitjana, mediana, màxim i mínim. Així vaig trobar “I dreamed about a human being”. En veure les imatges vaig pensar: “seria així com ens imaginarà un robot?”

<table>
<tbody>
<tr>
  <td><a href="/docs/art/new_media_art/I_dreamed_about_a_human_being/fran_simo_0001_Untitled1_medium_.jpg">
          <img class="alignnone size-full wp-image-1192" title="fran_simo_0001_Untitled1_medium_200" src="/docs/art/new_media_art/I_dreamed_about_a_human_being/fran_simo_0001_Untitled1_medium_200.jpg" alt="" width="170" height="170" />
  </a></td>
  <td><a href="/docs/art/new_media_art/I_dreamed_about_a_human_being/fran_simo_0003_Untitled1_dev_std_.jpg">
          <img class="alignnone size-full wp-image-1193" title="fran_simo_0003_Untitled1_dev_std_200" src="/docs/art/new_media_art/I_dreamed_about_a_human_being/fran_simo_0003_Untitled1_dev_std_200.jpg" alt="" width="170" height="170" />
  </a></td>
  <td><a href="/docs/art/new_media_art/I_dreamed_about_a_human_being/fran_simo_0004_Untitled1_variance_.jpg">
          <img class="alignnone size-full wp-image-1194" title="fran_simo_0004_Untitled1_variance_200" src="/docs/art/new_media_art/I_dreamed_about_a_human_being/fran_simo_0004_Untitled1_variance_200.jpg" alt="" width="170" height="170" />
  </a></td>
  <td><a href="/docs/art/new_media_art/I_dreamed_about_a_human_being/fran_simo_0005_Untitled1_skew_.jpg">
          <img class="alignnone size-full wp-image-1195" title="fran_simo_0005_Untitled1_skew_200" src="/docs/art/new_media_art/I_dreamed_about_a_human_being/fran_simo_0005_Untitled1_skew_200.jpg" alt="" width="170" height="170" />
  </a></td>
  <td><a href="/docs/art/new_media_art/I_dreamed_about_a_human_being/fran_simo_0007_Untitled1_range_.jpg">
          <img class="alignnone size-full wp-image-1197" title="fran_simo_0007_Untitled1_range_200" src="/docs/art/new_media_art/I_dreamed_about_a_human_being/fran_simo_0007_Untitled1_range_200.jpg" alt="" width="170" height="170" />
  </a></td>
  <td><a href="/docs/art/new_media_art/I_dreamed_about_a_human_being/fran_simo_0006_Untitled1_min_.jpg">
          <img class="alignnone size-full wp-image-1196" title="fran_simo_0006_Untitled1_min_200" src="/docs/art/new_media_art/I_dreamed_about_a_human_being/fran_simo_0006_Untitled1_min_200.jpg" alt="" width="170" height="170" />
  </a></td>
</tr>
<tr align="center">
<td>Mediana</td>
<td>Desviació estàndard</td>
<td>Variança</td>
<td>Asimetria</td>
<td>Rang</td>
<td>Mínim</td>
</tr>
</tbody>
</table>

Avui donem per assumpte que les càmeres, els telèfons, el nostre programari de fotografies i fins i tot Facebook poden reconèixer les cares. Per a la majoria això és “màgia”. No només ningú sap com ho fan sinó que ningú es pregunta com ho fan o què més poden fer.

El més fascinant del tema per a mi és la pregunta: “què més poden aprendre? què podem ensenyar-los a veure?” Les aplicacions típiques d’aquestes tecnologies sempre han estat la seguretat. Les aplicacions comercials estan poc desenvolupades. Per exemple, fer que un banc d’imatges es catalogui automàticament. Algoritmes similars s’utilitzen per al diagnòstic per imatge. Però “per què la poden utilitzar els artistes o els filòsofs?”

## Fotografia i intel·ligència artificial

“I dreamed about a human being” és part d’un projecte més gran que explora l’ús de la intel·ligència artificial aplicada a la fotografia utilitzant codi i dades obertes a Internet.

El projecte va començar l’any 2008. Té una base de dades de 56 milions d’imatges amb llicències creative commons. El 2011 es va parar la cerca d’imatges per començar a processar-les. En les últimes versions el sistema era capaç d’afegir 200.000 fotografies per dia a la base de dades.

Fa 10 anys tenir accés a aquestes quantitats d’informació i la capacitat per processar-les en un ordinador casolà amb algoritmes d’intel·ligència artificial podria haver-se considerat ciència ficció.

El fenomen que ens porta fins aquí té tres dimensions: les càmeres digitals i les xarxes socials, la filosofia de compartir del open source i l’augment de la capacitat dels ordinadors i les xarxes que es podrien resumir en la popularització de la tecnologia digital.

Les càmeres digitals i les xarxes socials propicien que existeixi una gran quantitat d’imatges capturades i publicades. Aquestes imatges són accessibles a través d’interfícies de programació públiques, el que permet programar ordinadors per accedir a aquestes imatges gairebé sense cap límit.

Els conceptes d’open source i la seva ideologia han deixat de pertànyer al món del programari i s’han estès a llicències d’ús de gairebé qualsevol tipus de contingut. Així, els usuaris permeten accés i concedeixen el permís per a la reutilització de manera explícita publicant les imatges amb llicències creative commons.

Al mateix temps moltes empreses i universitats han comprès que alliberar el codi de parts de les seves investigacions els ajuda a vendre productes o evolucionar projectes amb l’aportació de la comunitat de programari lliure. Com a conseqüència avui existeix codi obert de qualitat especialitzat en visió artificial i intel·ligència artificial. La tecnologia utilitzada en aquest projecte va ser desenvolupada i
alliberada per Intel, Compaq i Mitsubishi.

Tot això s’afegeix a l’increment de la capacitat computacional i de la velocitat de transferència de la xarxa.

Tots ens subint a la tecnologia digital com tots ens subint als cotxes. Van haver de passar 100 anys per veure l’impacte mediambiental. Però l’impacte d’aquesta tecnologia no acaba a l’aire, s’està entrant dins del nostre cervell alterant fins i tot la seva estructura. És necessari, almenys, intentar comprendre les capacitats de les tecnologies que estem utilitzant.

## Preguntes tècniques freqüents sobre el projecte

### Quin algoritme s’ha utilitzat?

haar-like features de Viola-Jones proposat el 2001 <a href="http://en.wikipedia.org/wiki/Haar-like_features">http://en.wikipedia.org/wiki/Haar-like_features</a>

### Puc descarregar la haar.xml?

Sí, està disponible aquí <a href="http://bit.ly/S6PShC">http://bit.ly/S6PShC</a>

### Com s’ha entrenat l’algoritme?

L’entrenament s’ha fet amb la biblioteca de visió artificial openCV versió 2.1 sobre Ubuntu 10.04. Per al reconeixement d’aquestes imatges s’ha usat la tercera versió de l’entrenament que s’ha fet amb 209 imatges positives i 3123 negatives. El processament ha tardat 3 setmanes en un ordinador amb un processador Intel Core i5 650 3.20GHz x 4 amb 12 Giga de RAM.

### Per què 257 sobre 5 milions?

5 milions d’imatges a 500 píxels ocupen gairebé un Terabyte, la mida del disc que tinc dedicat a la biblioteca del projecte. D’aquestes 5 milions d’imatges l’algoritme va trobar 166 mil rostre però només 257 tenien un retrat que ocupés el 70% de la fotografia i més de 6 megapíxels de resolució que creí acceptable per fer una còpia impresa de qualitat. “I dreamed about a human being” té una resolució de 3000x3000 píxels.

### Quin programari s’ha utilitzat?

- Base de dades: MySQL diverses versions amb els anys.
- Llenguatges de programació: PHP i C.
- Biblioteca de visió artificial: openCV 2.1 i 2.3
- Per a les tasques “humanes” de visualització Lightroom 4 i Photoshop 5.

### Com es va fer el render estadístic?

Després de l’entrenament s’avaluaren els possibles retrats en les 5 milions d’imatges guardant els resultats en una base de dades. Un programa en PHP va descarregar les imatges de Flickr i va generar JPGs amb la informació que va trobar l’algoritme de reconeixement.

Aquests JPGs s’importen a Lightroom on es pot fer una revisió humana. Els JPGs es poden veure amb i sense el reencuadre per poder avaluar-los.

Després de separar per resolució es van exportar les 257 imatges a 3000x3000. Moltes tenien més resolució però per al càlcul han de ser totes iguals.

Les 257 imatges s’obren en Photoshop com a capes, aquestes es agrupen en un objecte intel·ligent al que es demana que faci els càlculs estadístics.

