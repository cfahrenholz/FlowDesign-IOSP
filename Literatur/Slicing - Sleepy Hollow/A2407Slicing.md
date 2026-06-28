<!-- Page 1 of 10 -->


PLANUNG Slicing
ANFORDERUNGSANALYSE FÜR ENTWICKLER, TEIL 4
Die Benutzerschnittstelle
treibt das Slicing
Die Struktur der Oberfläche gibt wertvolle Hinweise darauf, wo der Entwurf beginnen
sollte. Klarheit gewinnen Sie besten durch eine schrittweise Annäherung.
Das Verhalten von Software wird durch Interaktionen mit Die Datensammlung vor dem Entry Point ist nötig, weil Be-
dem Benutzer getriggert. Jeder Interaktion steht eine nutzer Entry Points nicht direkt ansprechen können; sie sind
Funktion gegenüber, ein Entry Point. In HTTP-Servern wird ja keine Programmierer. Der collect-Schritt macht den Entry
das durch das Protokoll nahegelegt und ist mit MVC-Frame- Point vermittels einer Frontend-Technologie zugänglich. Der
works leicht umsetzbar. Bild 1 zeigt ein sehr simples Beispiel project-Schritt leistet dasselbe für das Ergebnis des Entry
dafür: Points; er rückübersetzt es in die Welt des Anwenders.
Die eigentliche Arbeit wird vom Code hinter der „Proces- Dass im Beispiel der Anwender eine andere Software ist,
sor-Fassade“ verrichtet. Dessen Entry Points sind Wurzeln die Daten nicht „eingibt“, sondern über ein Protokoll sendet
eines womöglich sehr tiefen Funktionsbaums, in dem das beziehungsweise empfängt, tut der Allgemeinheit dieses
gewünschte Verhalten durch Logik [1] hergestellt wird. Verarbeitungsflusses keinen Abbruch. Genauso sieht es aus,
Hinter der Grenze der Entry Points gibt es keine Abhängig- wenn eine Software eine grafische Benutzeroberfläche hat.
keit mehr von der Frontend-Technologie – hier ein MVC- Die Entry Points werden in diesem Fall nur durch eine ande-
Framework. re Technologie zugänglich gemacht.
Um die Aufrufe der Entry Points herum sorgt das Frontend Sie als Softwareentwickler sind primär verantwortlich für
explizit oder implizit dafür, Daten vom Benutzer zu beschaf- die Herstellung des Verhaltens hinter Entry Points. Benutzer-
fen (collect) beziehungsweise für ihn aufzubereiten (pro­ schnittstellen sind so betrachtet lediglich ein notwendiges
ject). Beides ist abhängig von der Frontend-Technologie. In Übel – machen dafür jedoch leider oft viel Mühe. Deshalb legt
Bild 2 sehen Sie ein Beispiel dafür. der Slicing-Ansatz für die Anforderungsanalyse so viel Wert
darauf, die Entry Points einer Soft-
ware herauszuarbeiten. Ab dort
herrscht einfach Klarheit, und Sie
sind in Ihrem Element. Sobald Ent ry
Points mit Signatur und Testfällen
definiert sind, kann ein Entwurf mit
Ein HTTP-MVC-Router anschließender Codierung ernst-
ruft Entry-Point-Funk- haft beginnen.
tionen auf (Bild 1) Jenseits des Trivialen ist es aller-
dings so, dass Software Dutzende,
gar Hunderte von Entry Points hat,
weil auf dutzendfache, gar hundert-
fache Weise mit ihr interagiert wer-
den kann (Bild 3).
Angesichts dessen stellt sich die
Frage, wie all diese Entry Points ge-
funden und ausreichend spezifiziert
werden können. Denn eines ist klar:
Sie lassen sich nicht einfach aufzäh-
len. Sie können den PO nicht fra-
gen: „Wie lauten die Entry Points,
die du dir wünschst?“ Und selbst ei-
ne Frage nach allen Interaktionen
läuft ins Leere.
44 7.2024 www.dotnetpro.de
004444--005533__SSlliicciinngg__eeaa..iinndddd 4444 0011..0066..2244 1122::1144


---


<!-- Page 2 of 10 -->


PLANUNG Slicing
Datenverarbeitung
im Rahmen einer
Interaktion (Bild 2)
Die Lösung kann nur darin bestehen, die Menge aller In- top über ein eigenes Icon starten kann oder für die es einen
teraktionen mit ihren zugehörigen Entry Points zu untertei- eigenen URL gibt. Ein Beispiel sind Produktivitätsapplika-
len. Sogar mehrfach zu unterteilen, je nachdem, wie umfang- tionen wie E-Mail-Client, Kalender, Aufgabenverwaltung,
reich und unübersichtlich die Anforderungen sind. Im Slicing Notizen und Adressenverwaltung. Alle diese Themen gehö-
gibt es dafür eine konkrete Hierarchie (Bild 4), die orthogonal ren auf hoher Abstraktionsebene zusammen (Bild 7), und Mi-
zu User Stories oder Use Cases ist. crosoft hat mit Outlook auch alles unter einem Applika-
Orthogonal zu User Stories und Use Cases ist die Hierar- tionsdach versammelt.
chie der Scopes beim Slicing deshalb, weil sich erstens die- Doch es gibt auch noch einen anderen Weg, um mit der
se Scopes vertikal und horizontal in jenen verorten lassen umfangreichen Anforderung „Produktivitätsunterstützung“
(Bild 5). Und zweitens, weil diese auf technische Artefakte ab- umzugehen. Sie können jeder Rolle mit ihren Anforderungen
gebildet sind, jene mit Technik jedoch nichts zu tun haben. eine eigene Applikation geben. Das ist der Ansatz, den Sie
User Stories und Use Cases bieten interessante Blickwin- auf iPhones ganz natürlich umgesetzt sehen (Bild 8).
kel auf Anforderungen. Aber sie sind nicht angebunden an Sobald Sie mehrere Rollen als Nutzer eines Softwaresys-
die Realität der Arbeit eines Softwareentwicklers nach der tems identifiziert haben, müssen Sie entscheiden, ob Sie ei-
Anforderungsanalyse. Sie lassen ihn ohne Ansatzpunkte für nen One-size-fits-all-Ansatz umsetzen oder lieber ein Best-
den darauf folgenden Entwurf und die Codierung zurück. of-breed-Angebot machen wollen: ▶
Deshalb empfehle ich Ihnen, nach Gesprächen über User
Stories und Use Cases das Slicing-Messer in die Hand zu
nehmen und den Scope, der nach Arbeit mit diesen Werkzeu-
gen abgesteckt wurde, feiner und feiner zu schneiden, bis
Sie zumindest Entry Points herausgearbeitet haben
(Bild 6). Slicing liefert einfach konkrete Strukturelemen-
te für die Programmierung.
Applikationen
Wenn ein Softwaresystem zu groß ist, um gleich vom
Gesamtüberblick – der sogenannten Softwarezelle –
direkt bis hinunter zur Ebene der Interaktionen zu
springen, dann können Sie sich dem System schritt-
weise annähern. Meine Empfehlung: Schauen Sie
zuerst die Rollen an, die Sie als Nutzer des Systems
identifiziert haben. Fragen Sie sich für jede Rolle:
Wäre es für diese Rolle vorteilhaft, eine eigene Ap- Software wird
plikation anzubieten? durch viele, sehr
Mit Applikation meine ich eine „getrennte Soft- viele Interaktionen
ware“, die der Benutzer zum Beispiel auf dem Desk- getriggert (Bild 3)
www.dotnetpro.de 7.2024 45
004444--005533__SSlliicciinngg__eeaa..iinndddd 4455 0011..0066..2244 1122::1144


---


<!-- Page 3 of 10 -->


PLANUNG Slicing
One size fits all: Alle Rollen arbeiten mit derselben An-
wendung. Die Anwendung integriert die Teil-Lösun-
gen für die unterschiedlichen Rollen unter dem Dach
einer Benutzerschnittstelle und auf der Basis einer
Technologie.
Best of breed: Alle Rollen bekommen ihre eigenen An-
wendungen. Die Anwendungen werden über Ressour-
cen, allgemeiner: über Standards integriert. Jede An-
wendung kann eine optimale Benutzerschnittstelle an-
bieten und die für sie am besten geeignete Technolo-
gie nutzen (etwa Web versus Desktop versus Mobile).
Zusätzlich bietet eine Best-of-breed-Umsetzung mehr
Möglichkeiten paralleler Entwicklung. Die Arbeitstei-
lung ist einfacher, und auch eine jeweils eigene Entwick-
lungsgeschwindigkeit (Release-Zyklus) ist möglich. Hier
sind Anforderungen und Umsetzungen stärker vonei- Ausschnitt aus der Scope-Hierarchie des Slicing (Bild 4)
nander entkoppelt.
Ich halte den Best-of-breed-Ansatz für unterschätzt.
Zu selten werden große Softwaresysteme zum Nutzen für An- Ressource zu einem Verbindungsglied werden kann; die ist
wender und Entwickler wirklich in separate Anwendungen vorher schon zu sehen (A) oder wird bei der Aufspaltung zur
aufgeteilt. Anwender profitieren von besseren Benutzer- Integration eingeführt (B). Jede Applikation steht für einen
schnittstellen, Entwickler profitieren von übersichtlicheren kleineren Scope als das Gesamtsystem. Jede Applikation ist
Codebasen. Es müssen weniger Kompromisse eingegangen ein Inkrement, das heißt, sie bietet bei Lieferung für sich ge-
werden, um unterschiedliche Rollen zufriedenzustellen. Der nommen dem Anwender einen Nutzen.
Nachteil von explizitem Aufwand für die Verbindung der Der kleinere Scope besteht aus einer reduzierten Anzahl
Apps ist im Grunde ein Vorteil: Darin manifestiert sich Ent- von Interaktionen je Applikation. Auch wenn die Interaktio-
kopplung. Veränderungen in einem Bereich schlagen weni- nen für ein ganzes Softwaresystem nicht bekannt sind und
ger schnell auf andere Bereiche durch. auch für die einzelnen Applikationen noch nicht klar sind, so
Jede Applikation ist wiederum ein System für sich mit ei- ist dennoch gewiss, dass es je Applikation weniger sind als
genen Portalen, Providern und einer spezifischeren Domäne für das Gesamtsystem (Bild 10). Auf diese Weise können Sie
als das Ganze. Die Zerlegung des Gesamtsystems in Appli- sich auf jeden Fall besser konzentrieren: bei der weiteren
kationen ist also selbstähnlich. Bild 9 zeigt, wie dabei eine Analyse und bei der späteren Implementation.
User Stories und Use Case definieren
Scopes, die gewöhnlich viele Slices in
einer Slicing-Hierarchie umfassen (Bild 5)
46 7.2024 www.dotnetpro.de
004444--005533__SSlliicciinngg__eeaa..iinndddd 4466 0011..0066..2244 1122::1144


---


<!-- Page 4 of 10 -->


PLANUNG Slicing
Anforderungen können Smartart und Diagramme hingegen rech-
zuerst durch die Brille von ne ich einer anderen Perspektive zu.
User Stories und Use Cases Sendungen (Serienbriefe, Etiketten, Um-
betrachtet werden - doch schläge) gehören ebenfalls zu einer ande-
schlussendlich sollten sie ren Perspektive.
mit Slicing „auf den Punkt Und so weiter.
g ebracht“ werden (Bild 6)
Ich denke, wenn Sie es zulassen, so zu den-
ken, dass die Benutzerschnittstelle einer Ap-
plikation eben kein Monolith sein muss, son-
dern aus Teilen, Modulen, Bereichen beste-
hen kann, dann werden Sie bei der Diskus-
sion über Anforderungen erspüren, wo sich
Grenzen ziehen lassen.
Der Zweck im Rahmen des Slicings ist
auch hier, es Ihnen leichter zu machen, auf
die Interaktionen zu kommen. Beim Slicing geht es nicht um
UX. Sie sollen die Perspektiven nicht visuell gestalten.
Perspektiven
Wenn ein UX-Spezialist Ihnen in den Analysegesprächen
Aber was, wenn selbst je Applika- zur Seite steht, ist das wunderbar. Zu früh können UI und UX
tion die Interaktionen noch nicht nicht eingebunden werden. Dennoch ist das primäre Interes-
deutlich zu erkennen sind? Wie se beim Slicing nicht die Gestaltung, nicht das Wie, sondern
können Sie dann den Scope weiter einengen? Für mich ist das Was. Was sollen Benutzer durch das Frontend anstoßen
dann die nächste Ebene innerhalb der Applikationen die der können? In welcher Granularität sollen sie Verhalten aus der
Perspektive. Software „herauskitzeln“?
Innerhalb des gesamten Frontends einer Applikationen
Dialoge
lassen sich oft „Bereiche“ unterscheiden, die sehr verschie-
den sind. Dieselbe Benutzerrolle nimmt in ihnen noch mal Wenn Ihnen Perspektiven etwas abstrakt vorgekommen
unterschiedliche Perspektiven ein. Ihr Blickwinkel wechselt sind, atmen Sie hoffentlich nun auf, wenn ich mit Ihnen eine
zum Beispiel von Fachlichkeit zu Sicherheit, oder innerhalb Ebene tiefer in der Slicing-Hierarchie steige; dort finden sich
der Fachlichkeit wechselt sie von den Stammdaten zu den die Dialoge.
Bewegungsdaten (Bild 11). Jede Perspektive umfasst einen oder mehrere Dialoge, die
Sehen Sie ein Frontend nicht als „monolithisch“ an. Was konkrete Benutzerschnittstellenelemente zusammenfassen.
Anwender grundsätzlich durch das Frontend mit einer Appli- Dialoge sind Fenster, Formulare, Seiten oder auch Tabs da-
kation tun wollen, ist durchaus sehr verschieden. Indem Sie rin. Gewöhnlich sind es rechteckige Bildschirmausschnitte,
diese Perspektiven identifizieren, bilden Sie innerhalb des die Sie minutiös mit Controls oder Widgets füllen, in denen
Scopes einer Applikation wiederum Untermengen von Inter- Anwender entweder Daten erfassen, Verarbeitung triggern
aktionen: die im einen Bereich versus die im anderen Bereich. oder Daten angezeigt bekommen.
Wieder gilt: Sie kennen die Interaktionen ja noch nicht. Auf der Ebene der Dialoge werden Interaktionen das ers-
Nur eines ist gewiss: Wenn Sie das ganze Frontend in sinn- te Mal verlässlich sichtbar. Ohne Interaktion öffnet sich kein
volle Teilbereiche zerlegen, wird jeder weniger davon ent- Dialog. Das beginnt mit dem Applikationsstart. Als Beispiel
halten, die dann auch leichter zu identifizieren sein werden. kann eine simple Fakturierungsanwendung dienen, die aus
Wie manifestieren sich Perspektiven in einer Applikation? folgenden Perspektiven mit ihren Dialogen besteht: ▶
Meistens sind es Gruppen von Dialogen,
Forms beziehungsweise Seiten. Sie starten
zum Beispiel eine Desktop-Anwendung und
finden darin im Menü verschiedene Bereiche,
in die Sie „einsteigen kön-
nen“. Denken Sie etwa an
Microsoft Word:
Die zentrale Perspektive
in Word ist die Bearbei-
tung des Textes; dazu
gehören auch Dialoge
wie Absatzformatierung oder die Forma- Mehrere Rollen mit ihren unterschiedlichen
tierung mit Nummerierungen oder Auf- Ansprüchen werden mit einer Applikation
zählungen. bedient (Bild 7)
www.dotnetpro.de 7.2024 47
004444--005533__SSlliicciinngg__eeaa..iinndddd 4477 0011..0066..2244 1122::1144


---


<!-- Page 5 of 10 -->


PLANUNG Slicing
Sicherheit
Login
Passwort zurücksetzen Mehrere Rollen werden mit auf
Stammdaten ihre Bedürfnisse speziell zuge-
Kundenübersicht schnittenen Applikationen
Kundendetails b edient (Bild 8)
Produktübersicht
Produktdetails
Bewegungsdaten
Rechnungsübersicht
Rechnungsdetails
Überfällige Zahlungen
Zahlungseingang
Jede Perspektive hat es leichter gemacht, sich auf
die Frage zu konzentrieren: Welche Dialoge helfen
dem Benutzer, seine Arbeit zu erledigen?
Bei der Definition der Dialoge hilft es schon sehr,
UI/UX-Spezialisten zur Seite zu haben. Sie können
sagen, wie sich Daten am besten erfassen bezie-
hungsweise präsentieren lassen; dazu gehört die
Zusammenfassung in Dialoge.
Auf der Dialog-Ebene der Slicing-Hierarchie geht
es darum, welche Dialoge es gibt und wie sie zu-
sammenhängen (Bild 12). Von welchem Dialog kommt der Be- Manchmal führt ein Dialog „ins Nichts“ (zum Beispiel Log-
nutzer zu welchem anderen? Jeder Übergang steht schon für in, Passwort zurücksetzen oder Rechnungsübersicht). Das
eine Interaktion. Endlich kommen Sie also bei den ersten En- bedeutet, hier beendet eine Interaktion die Applikation.
try Points eines Softwaresystems an. Und schließlich gibt es bidirektionale Überhänge wie zum
Manchmal sind die Übergänge unidirektional wie zum Bei- Beispiel von Kundenübersicht zu Kundendetails. Dann ist
spiel vom Dialog der Rechnungsübersicht zu den überfälli- der Rückweg nicht optional und auch bedeutungsvoll. Sie
gen Zahlungen. Das bedeutet nicht, dass der Benutzer nicht wollen über das UI-Verhalten hinaus – ein Fenster wird ge-
von dort zurück kann – er könnte zum Beispiel einen mo- schlossen – die Software etwas tun lassen, zum Beispiel sol-
dalen Dialog einfach schließen –, sondern dass der Rück- len beim Rückweg veränderte Daten gespeichert werden.
weg kein Verhalten triggert, das Sie speziell codieren müss-
ten. Die UI-Technologie übernimmt für Sie den Rückweg. Ein solches Übergangsdiagramm könnten Sie auch schon auf
Manchmal gibt es Hin- und Rückwege zwischen Dialogen, der Perspektivenebene anfertigen. Doch dort ist gewöhnlich
die getrennt sind, wie zum Beispiel zwischen Login und so wenig klar, von wo aus die Übergänge getriggert werden,
Rechnungsübersicht. Das bedeutet, diese Interaktionen dass diese Interaktionen eher spekulativ als nützlich sind.
sind unabhängig voneinander. Die Be-
nutzerin kommt vom Login-Dialog zur
Rechnungsübersicht, muss nicht zurück Wenn ein Softwaresystem in Applikationen
(logout), kann aber. gespalten wird, können diese über Ressour-
Manchmal kommt ein Dialog „aus dem cen integriert werden. Die können dafür na-
Nichts“ (zum Beispiel Login). Das bedeu- türlich speziell und zusätzlich zu anderen
tet, hier wird die Applikation gestartet Ressourcen eingeführt werden (Bild 9)
und der Dialog erscheint als Erstes.
48 7.2024 www.dotnetpro.de
004444--005533__SSlliicciinngg__eeaa..iinndddd 4488 0011..0066..2244 1122::1144


---


<!-- Page 6 of 10 -->


PLANUNG Slicing
Sobald Sie jedoch Dialoge in Eine Aufspaltung des Soft-
den Blick nehmen, wird Ihnen waresystems in mehrere Ap-
sehr schnell klar, wie sie zu- plikationen reduziert die Zahl
sammenhängen – und wie da- der Interaktionen, um die Sie
rüber dann auch Perspektiven sich kümmern müssen, um
verbunden sind. „voranzukommen“ (Bild 10)
Vielleicht spüren Sie bereits
am Beispiel in Bild 12, wie sich
Fragen aufdrängen. Klarheit
will hergestellt werden. Wenn
es für Sie zum Beispiel klar
ist, dass es die Perspek tiven
Stammdaten und Bewegungs-
daten gibt mit den Dialogen
Kundenübersicht, Pro dukt über-
sicht und Rechnungsübersicht,
dann ist noch nicht offensichtlich,
wie sie zusammenhängen.
Es ist eine aktive Entscheidung, die
Stammdaten aus der Rechnungsübersicht
zugänglich zu machen und nicht unabhängig da-
von. Die Idee dahinter: Meistens wollen Anwenderinnen
Rechnungen erfassen. Das führt zu Geldeingängen, das soll- fühlen; es gibt konkret etwas zu codieren. Sie spüren etwas
te im Vordergrund stehen. Stammdatenverwaltung ist nur von dem Appeal, den Visual Basic 1.0 nach seinem Release
eine notwendige, „lästige“ Aufgabe daneben. im Jahr 1991 unmittelbar für viele gehabt hat: Es schien, als
Diese Entscheidung hätte aber auch anders ausfallen kön- sei nun endlich visueller Softwareentwurf möglich. Software
nen. Alle drei Dialoge könnten gleichberechtigt von einem konnte scheinbar mit Dialogen und Steuerelementen struk-
„Shell-Dialog“ aus zugänglich sein, in dessen Rahmen sie turiert werden. Ein Doppelklick auf einem Menüeintrag oder
angezeigt werden (MDI). Button hat sofort den Ort geliefert, an dem der Code geschrie-
Ohne sich in Details zu verlieren, können Sie mit Dialog- ben werden konnte, der den Benutzerwunsch erfüllt.
übergangsdiagrammen schon darüber nachdenken, wie die Doch leider, leider war das ein Missverständnis. Denn die-
Bedienungswege in Ihrer Applikation laufen sollen. Sie bau- ses Vorgehen skaliert nicht. So lässt sich für wachsende Ap-
en sie auf hohem Abstraktionsniveau modellhaft auf. Prakti- plikationen kein sauberer Code entwickeln. Dennoch steck-
kabel sind dafür auch Post-It-Notizzettel, deren Beziehungen te darin eine Wahrheit, nämlich die, dass die Gestaltung der
Sie leicht verändern können, um zu erspüren, wie sich die Benutzerschnittstelle Klarheit darüber schafft, was denn an
grobe Bedienung wohl anfühlen würde (Bild 13). Verhalten wann wie getriggert werden soll.
Dialoge sind für Sie als Entwickler greifbar. Sie wissen, wie Deshalb ist für mich die Dialog-Ebene im Slicing so wich-
Sie einen Dialog implementieren. Hier können Sie sich wohl- tig. Sie gibt Ihnen dafür konkrete Anhaltspunkte – allerdings
ohne den Anspruch, die Lösung in
einem Button-Click-Eventhandler zu
schrei ben. Die gehört hinter einen En try
Point, der eben kein solcher Eventhand-
ler ist, sondern nur der Hebel, über den
eine Logik-Maschinerie in Gang gesetzt
und getestet werden kann. Eventhand-
ler gehören noch zum Frontend; sie ba-
sieren auf UI-Technologie.
Wenn Sie mit User Stories oder Use
Cases arbeiten, ist es wichtig, dass Sie
am Ende „abbiegen“ in Richtung Pers-
pektiven und Dialoge (Bild 6). Werden
Sie ganz konkret. Lassen Sie den PO
entscheiden, was er wo eingeben, aus-
lösen und sehen will. Das darf er nicht
Perspektiven unterteilen das Frontend mit einem Handwedeln an Sie abschie-
in Bereiche, in denen Benutzer sehr unter- ben. Sie riskieren sonst, dass Sie end-
schiedliche Anforderungen haben (Bild 11) lose teure Iterationen durchlaufen. ▶
www.dotnetpro.de 7.2024 49
004444--005533__SSlliicciinngg__eeaa..iinndddd 4499 0011..0066..2244 1122::1144


---


<!-- Page 7 of 10 -->


PLANUNG Slicing
Beispielhaftes Dialogübergangsdia-
gramm mit Dialogen unterschiedlicher
Perspektiven (Bild 12)
Dialoge und ihre Übergänge sollten nicht erst mit Produk- Was könnte noch hinzukommen? Offensichtlich ist die Unter-
tionscode für den PO erfahrbar gemacht werden, sondern vor- scheidung zwischen:
her. Arbeiten Sie mit Papierprototypen, Mockups oder auch Neue Rechnung anlegen
codierten Prototypen. Aber Hände weg von Produktionscode! Bestehende Rechnung öffnen
Interaktionen
In beiden Fällen werden die Rechnungsdetails angezeigt.
Alle Interaktionen finden auf (beziehungsweise zwischen) Was könnten Anwenderinnen aber noch in einer Rech-
Dialogen statt. Sie sind der Ort für die UI-Steuerelemente, die nungsübersicht tun wollen?
Interaktion überhaupt ermöglichen. UI-Steuerelemente kön- Ich kann mir vorstellen, dass sie zum Beispiel …
nen Ereignisse auslösen, und in den Eventhandlern dieser Er- die Rechnungen filtern wollen, zum Beispiel nur die eines
eignisse können Entry Points angestoßen werden. bestimmten Kunden oder nur die in einem Zeitraum,
Wenn Sie die Dialoge einer Applikation identifiziert haben die Rechnungen sortieren wollen,
(oder auch nur eine Untermenge, die Ihnen für
ein Inkrement reicht), kennen Sie schon erste
Interaktionen: Das sind die, die einen Über-
gang zwischen Dialogen beinhalten. Für sie
stellt sich die Frage, wie genau sie ausgelöst
werden und wie die Entry Points dahinter aus-
sehen.
Darüber hinaus werden die meisten Dialoge
allerdings noch weitere Interaktionsmöglich-
keiten anbieten. Deshalb müssen Sie nun in
jeden Dialog hineinzoomen. Das ist der nächs-
te Level in der Slicing-Hierarchie. Sie machen
die Dialoge auf und skizzieren, wie es darin
aussieht. Was soll darin wann geschehen, das
relevant für Sie im Sinne einer Codierung
„hinter der Fassade“ eines Entry Points ist?
Als Beispiel soll der Dialog zur Rechnungs-
übersicht in der Variante (A) dienen (Bild 13).
Bekannt sind schon die Interaktionen der Dia-
logübergänge:
Kundenübersicht öffnen
Produktübersicht öffnen
Rechnungsdetails öffnen Ausschnitt mit alternativen Dialog-
Zahlungseingang verbuchen übergängen, modelliert mit Post-It-
Überfällige Zahlungen anzeigen Notizzetteln (Bild 13)
50 7.2024 www.dotnetpro.de
004444--005533__SSlliicciinngg__eeaa..iinndddd 5500 0011..0066..2244 1122::1144


---


<!-- Page 8 of 10 -->


PLANUNG Slicing
eine Rechnung archivieren wollen, wenn sie
bezahlt ist, oder
eine Rechnung löschen wollen, solange sie
noch nicht an den Kunden geschickt wurde.
Ihnen fallen vielleicht noch weitere Interaktio-
nen ein. Oder nennen Sie es Funktionalitäten.
Im Dialog haben Sie „Dinge“ vor sich, mit de-
nen, an denen, durch die Anwender etwas tun
wollen. Das entzündet bestimmt Ihre Fantasie.
Fachlichkeit trifft auf Software. An der Oberflä-
che, in den Dialogen müssen alle fachlichen Ak-
tivitäten und Prozesse steuerbar beziehungs-
weise im Ergebnis spürbar gemacht werden.
Das wirft natürlich nicht nur die Frage nach
den Interaktionen mit ihren Entry Points auf, Übergänge zwischen Dialogen mit wenigen oder gar keinen Details (Bild 14)
sondern auch die nach der Struktur:
Wie ist die Erfassung des Inputs für jede Inter-
aktion strukturiert?
Wie ist die Darstellung des Outputs für jede In-
teraktion strukturiert?
Wie genau soll die Verarbeitung getriggert
werden?
Das bedeutet, Sie müssen sich jetzt doch einige
Gedanken über das Layout der Benutzer-
schnittstelle machen. Spätestens auf der Dia-
log-Ebene der Slicing-Hierarchie ist es also
wichtig, jemanden von UI/UX hinzuzuziehen.
Mit einer solchen Expertin an der Seite finden
Sie die beste Darstellung und die optimalen
Entry Points. Denn je nachdem, wie leistungs-
fähig eine UI-Technologie ist, sind manche Ent-
ry Points nötig oder eben nicht. Betrachten Sie
das Beispiel der Sortierung in der obigen Liste:
Ja, Benutzer sollen die Rechnungen in der Zoom-in auf den Dialog zur Rechnungsübersicht mit seinen Interaktionen (Bild 15)
Übersicht sortieren können – aber müssen Sie
dafür einen Entry Point anbieten und die Sor-
tierung codieren? Oder kann das UI-Steuerele-
ment für die Übersicht selbst sorgen? Was das
UI „kostenlos“ bietet, müssen Sie nicht (unbe-
dingt) als explizite Interaktion modellieren.
Bei den Dialogübergängen haben Sie viele
Dialoge im Überblick ohne großartige Details.
Bild 14 zeigt ein Beispiel, wie ich ein solches Dia-
gramm oft anfertige: als Skizze auf einem Blatt
Papier. Schnell hingeworfen bekomme ich auf
diese Weise einen Eindruck vom Big Picture der
Interaktionen. Anschließend kann ich entschei-
den, wo ich hineinzoome.
Die visuellen Details, die ich auf einer solchen
Skizze mitgebe, haben höchstens den Zweck,
dass ich leicht erkennen kann, um was für eine
Kategorie von Dialog es sich grundsätzlich han-
delt, zum Beispiel Übersicht, Formular. Dann
muss ich mir weniger Mühe beim Entziffern der
Beschriftung geben. ▶ Detaillierte Definition der Entry Points für jede Interaktion (Bild 16)
www.dotnetpro.de 7.2024 51
004444--005533__SSlliicciinngg__eeaa..iinndddd 5511 0011..0066..2244 1122::1144


---


<!-- Page 9 of 10 -->


PLANUNG Slicing
Eine schrittweise
Annäherung an die
Entry Points einer
Anwendung über en-
ger und enger gezo-
gene Scopes von An-
forderungen (Bild 17)
Anschließend gehe ich die Übersicht Dialog für Dialog einen Rückgabewert (3), den der Zieldialog für die Anwen-
durch und überlege ganz genau, welche Interaktionen gera- derin geeignet projiziert.
de hier gebraucht werden. Als Beispiel dient die Rechnungs-
übersicht in Bild 15, ein Zoom-in auf den Dialog zur Rech- Ich greife mal beispielhaft die Filtern-Interaktion heraus. Für
nungsübersicht mit seinen Interaktionen. Für die ist nun sie gibt es einen eigenen Button im Dialog, und die Intention
sichtbar, wo genau sie ausgelöst werden. Und weitere Inter- ist klar:
aktionen kommen hinzu: Es soll nach Rechnungsdatum und/oder Kundenname ge-
Manche Interaktionen übernehme ich dabei von der Dia- filtert werden. Mir scheint es am einfachsten, wenn all die-
logübersicht, zum Beispiel (1) und (2). se Angaben aus den Eingabefeldern (von & bis Datum, Na-
Allerdings starten die Pfeile nun an unterschiedlichen me oder Namensteil des Kunden) immer in den Entry Point
Punkten: Wenn ein Dialog überhaupt von dem im Fokus er- hineingehen. Dort wird genau geschaut, was vorhanden ist
reichtbar ist, beginnt der Pfeil weiterhin an dessen Rand (1). und wie die interne Abfrage dann am besten läuft.
Manche Dialoge werden hingegen sehr spezifisch über Ele- Als Resultat liefert der Entry Point eine Liste von Rech-
mente angestoßen; dann beginnt der Pfeil nun im Dialog im nungsobjekten. Allerdings sind das nicht die Domänenob-
Fokus (2), zum Beispiel wählt der Benutzer genau eine Rech- jekte, sondern speziell für die Darstellung im UI zusammen-
nung aus, um für sie einen Zahlungseingang zu buchen. gestellte Objekte. Deshalb heißt der Typ RechnungPo; Po
Andere Interaktionen kommen hinzu. Sie waren im Über- steht dabei für ProjektionsObject, das heißt ein Objekt, des-
blick nicht zu sehen (3). Sie beginnen meistens deshalb sen Zweck allein ist, Daten zu transportieren, die einer Dar-
auch bei einem Steuerelement im Dialog im Fokus. Und sie stellung genügend Futter bieten. Das Objekt ist also ein
führen zurück zum Dialog. Zum Beispiel beim Filtern wech- DTO (Data Transfer Object), allerdings eines zwischen
selt ja nicht der Dialog, sondern nur die Projektion der Da- Frontend und Domäne. Wahrscheinlich stehen darin nur
ten innerhalb des Dialogs. die Angaben, die auch in der Tabelle der Übersicht zu se-
hen sind, und eine ID. Für alles Weitere muss das UI wieder
Entry Points
bei einem Entry Point anfragen, wie es zum Beispiel mit Öff­
Die Skizze eines Dialogs mit seinen Interaktionen ist dann nenDetails(id:string):RechnungsdetailsPo geschieht. Das
auch der Ort, an dem Sie zu den Entry Points übergehen. Sie führt zur Öffnung eines neuen Dialogs, der mehr Daten
sehen ja genau, was an Daten zur Verfügung steht und was an- braucht.
gezeigt werden soll. Das ist die Information, die Sie brauchen,
um informierte Entscheidungen darüber zu treffen, wie die Ich liebe digitale Tools. Doch die Analyse der Anforderungen
Schnittstellen der Entry-Point-Funktionen aussehen sollen. ist ein kreativer Prozess, der von vielen schnellen Iterationen
Als Beispiel in Bild 16 nochmal einige Interaktionen der profitiert. Da will ich schnell sein, wenn ich einen Gedanken
Rechnungsübersicht. Jeder Interaktionspfeil hat nun … habe. Deshalb benutze ich gern analoge Tools wie Papier und
einen Namen (1), der die Intention hinter der Aktion be- Stift, um das, was ich im Kopf habe, für mich oder auch ande-
schreibt und der Name der Entry-Point-Funktion wird, re greifbarer zu machen. Wenn es später sauberer nötig sein
Parameter (2), die an die Funktion übergeben werden und sollte, kann ich immer noch eine Reinzeichnung anfertigen.
vom UI aus den Eingabe-Steuerelementen „zusammenge- Meistens entfällt das jedoch, weil aus den Skizzen gleich
sammelt“ werden, und Code wird.
52 7.2024 www.dotnetpro.de
004444--005533__SSlliicciinngg__eeaa..iinndddd 5522 0011..0066..2244 1122::1144


---


<!-- Page 10 of 10 -->


PLANUNG Slicing
Zwischenstand
Spätestens bei den Dialogen werden Sie jedoch prakti-
Jetzt haben Sie die wesentlichen Ebenen der Slicing-Hierar- scherweise landen, denn die haben immer eine Entspre-
chie kennengelernt. Alles beginnt beim Gesamtsystem mit chung im Code. Interaktionen und Entry Points pro Dialog zu
dem Ziel, die einzelnen Interaktionen der Benutzer mit ihm sammeln ist für jedes Softwaresystem hilfreich.
herauszuarbeiten. Die sind auf solcher Flughöhe meistens Dorthin sollten Sie deshalb auch von anderen Ansätzen wie
nicht zu erkennen und kaum abzählbar. Deshalb ist eine User Stories oder Use Cases abbiegen. Tun Sie sich diesen
schrittweise Annäherung über mehrere Zerlegungsebenen Gefallen einer Konkretisierung mit dem Product Owner. Oh-
nötig (Bild 17). ne Dialoge mit ihren Interaktionen erhalten Sie keine Klar-
Auf jeder tieferen Ebene zerfallen die Elemente der darü- heit über den ganz handfesten Umgang der Anwender mit ei-
berliegenden in Teile, die jeweils einen überschaubareren nem Softwaresystem; das ist zentral für Akzeptanz und Nut-
Scope, also einen engeren Anforderungshorizont haben. Je- zen. Ohne Dialoge mit ihren Interaktionen gibt es keine Klar-
des dieser Teile auf jeder Ebene stellt ein Inkrement im Sin- heit über die Entry Points, mit denen Sie anschließend in Ent-
ne der Agilität dar. Die Lieferung des Gesamtsystems befrie- wurf und Codierung starten. ◾
digt den Kunden vollständig, aber auch die Lieferung nur ei-
nes Dialogs mit all seinen Interaktionen oder sogar die Liefe- [1] Ralf Westphal, Logic Makes the World Turn Around,
rung eines Entry Points stellt einen kleinen, werthaltigen www.dotnetpro.de/SL2407Slicing1
Fortschritt dar.
Keine der Ebenen des Slicings ist für Sie Pflicht. Sie steigen
ein, wo Sie Klarheit gewinnen möchten. Das ist eigentlich im- Ralf Westphal
mer beim System, das Sie zumindest einmal in seine Umwelt ist Trainer, Berater und Mitgründer der Clean
stellen sollten, um Rollen und Ressourcen zu identifizieren. Code Developer Initiative (https://clean-code-
Anschließend können Sie direkt zur Ebene der Interaktio- developer.de). Seine Schwerpunkte sind dauer-
nen hinunterspringen – doch meistens werden Sie die noch haft hohe Produktivität für die Softwareent-
nicht klar aus der großen Höhe des Systems erkennen kön- wicklung und zukunftsfähige Teamorganisation.
nen. Also überlegen Sie, ob eine Zerlegung in Applikationen https://ralfw.de
Ihnen helfen kann, sich zu fokussieren. Oder ob Perspektiven
dnpCode A2407Slicing
im Frontend helfen, Sie zu inspirieren.
Deutschland NRW Ruhrpott Essen
27./28. September 2024
KI, Cloud, .NET, Datenbanken, Agiles Arbeiten
Deutschlandweit bekannte Sprecher
Workshops & Sessions
004444--005533__SSlliicciinngg__eeaa..iinndddd 5533 0011..0066..2244 1122::1144


|  |
| --- |
|  |
