<!-- Page 1 of 10 -->


PLANUNG Sleepy Hollow
SLEEPY-HOLLOW-ARCHITEKTUR, TEIL 2
Ich packe meinen Koffer …
Von den Anforderungen zu einer testbaren, modularen, wandelbaren Implementation:
Wie geht das?
Dieser Artikel möchte Ihnen zeigen, wie Sie über eine An- summiert, an denen sie steht. Je geringer die Summe, desto
forderungsanalyse mit Slicing (siehe die Serie von [1] bis weiter vorne steht die Position in der Ordnung des gesamten
[2]) und das Sleepy-Hollow-Architekturmuster [3] einem sehr Teams.
geraden Weg von den Anforderungen zu einer testbaren, mo- Bild 1 zeigt das für die beiden Beispiele. Zur Erläuterung die
dularen, wandelbaren Implementation folgen können. Bestimmung der Prioritätsordnung:
Lassen Sie uns gleich in die Praxis einsteigen. Das Hand- Aufgabe A1 steht bei Peter und allen anderen an dritter
werkszeug habe ich in den bisherigen Artikeln ausführlich Stelle. Sie hat immer den Index 3, die Summe ihrer Indizes
vorgestellt. Jetzt soll es endlich in einem etwas größeren Bei- ist also 3+3+3=9. Aufgabe A2 steht bei Peter und Paul an
spiel zum Einsatz kommen. erster Stelle (Index 1) und bei Maria an zweiter Stelle (In-
dex 2); daraus ergibt sich die Summe 4. A3 steht bei Peter
Das Szenario
und Paul an zweiter Stelle (Index 2) und bei Maria an ers-
Es soll um ein Softwaresystem gehen, mit dem ein Team ge- ter (Index 1); die Summe ist 5.
meinsam Ordnungen herstellen kann. Jedes Teammitglied Die Positionen mit ihren Summen: (A1,9), (A2,4), (A3,5).
soll die Positionen in einer Ordnung allerdings nicht absolut Sortiert nach aufsteigenden Summen ergibt sich als kalku-
bewerten, sondern relativ. lierte Ordnung für das Team: A2, A3, A1. Diese Ordnung ist
Beispiel Priorisierung: Aufgaben sind in eine Ordung in Be- sozusagen das Ergebnis der „wisdom of the crowd“.
zug auf die zeitliche Abfolge ihrer Erledigung zu bringen.
In welcher Reihenfolge sollen die Aufgaben A1, A2, A3 be- Bei diesem Vorgehen wird (zunächst) bewusst nicht berück-
arbeitet werden? Teammitglied Paul findet, die Reihenfol- sichtigt, dass zum Beispiel der Abstand zwischen A1 und A2
ge sollte A2, A3, A1 sein; Teammitglied Maria hingegen viel größer ist (9-4=5) als der zwischen A3 und A2 (5-4=1). Es
denkt, die Prioritäten sollten A3, A2, A1 sein; und Peter geht um eine schnelle, grobe Einschätzung der Ordnung „aus
schließlich hält auch A2, A3, A1 für die beste Reihenfolge. dem Bauch heraus“.
Beispiel Komplexitätsschätzung: Issues sind in eine Ordnung Das Softwaresystem soll eine Möglichkeit bieten, Positio-
in Bezug auf den Aufwand, der für ihre Umsetzung nötig nen zu sammeln, die dann von Teammitgliedern in individu-
ist, zu bringen. Welches der Issues I1, I2, I3, I4 ist komple- elle Ordnungen gebracht werden. Diese individuellen Ord-
xer als welches andere und wird deshalb wahrscheinlich nungen werden zu einer gemeinschaftlichen Ordnung ver-
mehr Zeit brauchen? Peter meint, das komplexeste Issue sei rechnet und angezeigt.
I3, dem I1, I4, I2 in absteigender Komplexität folgen; Paul Teammitglieder sollen für die Bestimmung einer gemein-
hingegen sieht es so: I1, I3, I2, I4; und Maria schätzt die schaftlichen Ordnung nicht co-located sein müssen. Sie sol-
Komplexität so: I3, I4, I1, I2. len auch nicht zeitlich beschränkt sein; die gemeinschaftliche
Ordnung soll also asynchron stattfinden können.
In Ermangelung von Kriterien, aus denen
sich absolute Werte für Priorität oder Kom-
plexität ableiten ließen, ist eine solche sub-
jektive, relative Schätzung ehrlicher und
einfacher als eine, die künstlich absolute
Werte erzwingt (zum Beispiel Story Points).
Teammitglieder müssen nur „ein Gefühl
haben“, dass eine Position im Hinblick auf
das jeweilige Ordnungsthema vor einer an-
deren stehen sollte.
Eine gemeinschaftliche resultierende
Ordnung des Teams kann aus den verschie-
denen individuellen Ordnungen der Team-
mitglieder leicht berechnet werden. Für je-
de Position werden die Indizes der Stellen Berechnung der Ordnung für das Team (Bild 1)
30 12.2024 www.dotnetpro.de
003300--003399__SSlleeeeppyyHHoollllooww__eeaa__ffss__eeaa..iinndddd 3300 0044..1111..2244 1166::3388


---


<!-- Page 2 of 10 -->


PLANUNG Sleepy Hollow
Erste Einschätzung
Überblick über
Wie ist Ihre Einschätzung dieses Projekts nach das ganze Software­
dieser Anforderungspräsentation? Das ist natür- system (Bild 2)
lich nur eine Skizze, und Sie stehen in keinem
Dialog mit einem Auftraggeber. Das ist für Sie in
dieser Größenordnung vielleicht ungewohnt.
Aber nehmen Sie es als Übung und lassen Sie
sich darauf ein, selbst wenn ich im Folgenden an-
dere Annahmen machen sollte als Sie. Es werden
auch Lücken bleiben, die Sie gern schließen würden,
ich aber offen lasse. Das ist dem Monolog geschuldet,
den dieser Artikel darstellt, und auch seinem notwen-
dig begrenzten Umfang.
Es geht allerdings nicht wirklich darum, diese Idee
marktreif umzusetzen (so sehr mir das immer mal wieder
in den Fingern juckt), sondern um die Demonstration der
Anwendung von Slicing und Sleepy Hollow. Das kann auch
mit divergierenden Annahmen und Lücken geschehen.
Damit im Hinterkopf: Wie ist dieses Projekt einzuschätzen? Ich identifiziere zwei Benutzergruppen (Rollen): Da ist der
Machbar? Wie ist der Aufwand? Was braucht es dafür? Wie PO, der die zu ordnenden Positionen festlegt; er leitet die
würden Sie vorgehen? Was ist Ihr Reflex? „Ordnungssitzung“. Und da sind Teammitglieder (Crowd),
So viel kann ich sagen: Das ist gut machbar. Der Aufwand die die Positionen in individuelle Ordnungen bringen. Je-
ist überschaubar. Ich habe es auch schon mal umgesetzt [4], de Benutzergruppe verdient eine eigene Benutzerschnitt-
die Implementation ist allerdings im Web nicht mehr lauffä- stelle. Die Benutzerschnittstellen bilden den Rahmen für In-
hig. Das hat Spaß gemacht; ich fand das Tool sehr nützlich teraktionen von Benutzern mit dem Softwaresystem.
und „mal etwas anderes“ als das ewige Planning Poker. Andererseits braucht das Softwaresystem eine Ressource,
Was braucht es dafür? eine Datenbank, um die Sitzungen mit ihren Positionen
Entscheidungen für Technologien: Frontend, Backend, (oder Einträgen) beziehungsweise den verschiedenen Ord-
Persistenz und so weiter. nungen der Teammitglieder zu speichern. Dafür scheinen
Das ist sicher ein verteiltes System, da die Teammitglieder mir zwei getrennte Provider nötig, die die persistenten Da-
nicht co-located sein müssen. ten in interne Datenstrukturen transformieren.
Die Usability bei der individuellen Ordnung sollte dem re- Außerdem gibt es noch nicht näher bestimme Domänenlo-
lativen, vergleichenden Schätzen gerecht werden. Drag- gik, die mit den Daten arbeitet, und vielleicht auch noch
and-drop kommt Ihnen da vielleicht in den Sinn, um die Po- ausgewiesene Domänendatenstrukturen auf einem höhe-
sitionen leicht in eine Wunschordnung zu bringen. ren Abstraktionsniveau als die DTOs der Provider.
Wie steht es mit der Security? Wie viel Aufwand muss da-
für getrieben werden? Meine Meinung: Es gibt kein Secu- Das sind alles keine tiefen Einsichten. Mich überrascht hier
rity-Problem. Die Daten, um die es geht, sind sehr flüchtig, nichts. Das zu erkennen hat mich fünf Minuten gekostet.
nicht persönlich und enthalten keine Geheimnisse. Dennoch ist dieser Überblick nützlich, denn er bietet mir ei-
Gibt es ein Skalierungsproblem? Meine Meinung: Nein, ne erste Checkliste für Entscheidungen:
denn die Datenmengen sind marginal, die Zugriffsraten Welche Technologie soll für die Benutzerschnittstellen zum
sind minimal, und die entscheidende Berechnung ist trivi- Einsatz kommen? Ich entscheide mich zunächst der Ein-
al und kann auch noch auf einem Client stattfinden. fachheit halber für ein Console-UI. Einem Web-UI steht
Die Domäne scheint einfach. Im Wesentlichen besteht sie später nichts im Wege, doch zu Anfang würde es mir mehr
aus der Logik, die individuelle Ordnungen der Teammit- Kopfschmerzen in puncto Gestaltung und Implementation
glieder zu einer gemeinsamen verrechnet. bereiten. Beides ist für das, worum es mir im Artikel geht,
jedoch unwesentlich. Welche UIs es gibt, ist wichtig, nicht
Ist das eine Aufgabe, die etwas Systematik verträgt, weil ich aber, wie genau sie ausgeprägt sind.
sie nicht „einfach runtercodieren“ kann? Aber sicher! Also Welche Technologie soll für die Datenbank zum Einsatz
los … kommen? Auch wenn ich mir die Interaktionen noch nicht
näher angeschaut habe, scheint mir nahezuliegen, dass die
Das ganze Softwaresystem aus 10 000 Meter
Zugriffsmuster sehr, sehr simpel sind. Im Grunde dreht sich
Flughöhe
alles um ein „Dokument“: eine Sitzung (Session) mit zu ord-
Die formellere Anforderungsanalyse mit Slicing beginnt in nenden Einträgen (Items). Zu einer Sitzung gehören ver-
großer Flughöhe mit einem Blick auf das gesamte Soft- schiedene Ordnungen der Teammitglieder. Alles könnte in
waresystem. Was ist von dort aus mindestens zu sehen? Bild 2 einem JSON-Objekt gespeichert werden. Aber irgendwie
zeigt den Überblick: fühlt es sich nicht so gut an, mehrere Teammitglieder ▶
www.dotnetpro.de 12.2024 31
003300--003399__SSlleeeeppyyHHoollllooww__eeaa__ffss__eeaa..iinndddd 3311 0044..1111..2244 1166::3388


---


<!-- Page 3 of 10 -->


PLANUNG Sleepy Hollow
Je eine Applikation für die Benutzergruppen
scheint aus Usability­Gründen angezeigt. Beide
greifen natürlich auf dieselben Daten zu (Bild 3)
potenziell gleichzeitig ein Sitzungsdokument mit ihren Ein PO soll nur seine Sitzungen bearbeiten können. Sitzun-
Ordnungen verändern zu lassen. Deshalb sehe ich die indi- gen haben zwar eine ID, doch wenn die außerhalb des
viduellen Ordnungen getrennt von den Sitzungen. Und wie Teams bekannt würde, könnte ein anderer PO die Sitzung
sollen die Daten persistiert werden? Ich würde mal ganz einsehen. Das ist zwar kein großes Problem, glaube ich,
einfach anfangen mit … einem Dateisystem. Wenn ich die aber das zu unterbinden ist einfach mit einer Identifikation
Daten in meiner Dropbox ablege, können mehrere Prozes- des PO.
se sehr einfach darauf zugreifen. Die Details sind in den Ein Teammitglied soll den Einträgen einer Sitzung nicht
Providern gekapselt. Wenn ich später meine, eine Mongo- mehrere Ordnungen geben können. Veränderung ist zwar
DB einsetzen zu müssen, implementiere ich nur die Provi- möglich, doch dadurch wird keine weitere Ordnung ange-
der neu. Auch das Persistenzmedium ist für das, worum es legt. Also muss erkannt werden, wer gerade die Einträge
mir hier geht, unwesentlich. Dass es eines gibt und in wel- einer Sitzung „in Ordnung bringen will“.
cher Granularität es angesprochen wird, ist entscheidend;
das drückt sich in den Providern aus. Damit bei der Identifikation keine persönlichen Daten not-
Soll das Softwaresystem verteilt laufen? Sicher. Das ist nö- wendig werden, deren Validität und Zugehörigkeit auch
tig, um den Teammitgliedern Freiheit in Bezug auf Ort und noch geprüft werden müssten, will ich es mir einfach machen:
Zeit für ihre Ordnungen zu geben. Jeder Client, den PO oder Teammitglieder nutzen, generiert
eine ID bei der ersten Nutzung und merkt sie sich. Fertig.
Näheres zu Domäne oder Datenstrukturen will ich an dieser Dass innerhalb einer Sitzung die Clients gewechselt werden,
Stelle noch nicht entscheiden, dazu möchte ich näher heran- ist unwahrscheinlich. Dass das (bei Teammitgliedern) „zum
zoomen … Mogeln“ bewusst gemacht wird, ist möglich, aber ich will es
nicht mit mehr Aufwand berücksichtigen.
Applikationen für jede Rolle
Also reicht es, bei den Applikationen noch einen weiteren
Die Verteilung des Codes für das Softwaresystem wird von Provider für die Client-ID hinzuzufügen, die in irgendeiner
nichtfunktionalen Anforderungen getrieben. Wenn Logik ei- Form von lokalem Speicher (auf der Festplatte oder im Brow-
ne nichtfunktionale Anforderung nicht erfüllen kann, dann ser) gehalten wird.
muss verteilt werden. Das ist offensichtlich hier der Fall: Die Die Domäne habe ich nach ein wenig Nachdenken jetzt
Rollen haben sehr unterschiedliche Anforderungen an die ebenfalls differenziert:
Benutzerschnittstelle. PO und Crowd gehen mit den Sitzun- In der PO-Applikation ist Domänenlogik nötig, um all die
gen und ihren Einträgen jeweils ganz anders um. Das scheint individuellen Ordnungen der Teammitglieder zu einer ge-
mir konsequent ausgedrückt durch spezialisierte Applikatio- meinsamen zu verrechnen. Dort gibt es zu Recht den Über-
nen für die Rollen (Bild 3). blick über alle eingereichten Ordnungen.
Bei dieser Spaltung des Softwaresystems frage ich mich, wie In der Crowd-Applikation für die Teammitglieder ist wahr-
Benutzer sich ihren Applikationen gegenüber identifizieren scheinlich nur eine Datenstruktur nötig, die es einfach
(Authentifizierung). Ist eine Identifikation überhaupt nötig? macht, Positionen einer Sitzung neu anzuordnen. Logik für
Ja, ich denke, eine Identifikation ist aus zwei Gründen nötig: „Berechnungen“ ist dort nicht gefragt.
32 12.2024 www.dotnetpro.de
003300--003399__SSlleeeeppyyHHoollllooww__eeaa__ffss__eeaa..iinndddd 3322 0044..1111..2244 1166::3388


---


<!-- Page 4 of 10 -->


PLANUNG Sleepy Hollow
So weit der erste Zoomschritt in das Softwaresystem hinein. Die Frontends sind Clients, die in Terminalfenstern laufen.
Sind damit alle nichtfunktionalen Anforderungen bedacht? Für meine Zwecke hier ist das der kleinstmögliche Einstieg.
Nein. Also noch mal hineinzoomen … Aber wie setze ich das Backend um? Es soll HTTP-End-
punkte für den Aufruf der Frontends bieten und auf meine
Worker für die Sicherheit
Dropbox zugreifen. Ich könnte es mit C# oder Typescript un-
Die Persistenz findet auf einem anderen Rechner statt als den ter Nutzung des Dropbox-API realisieren. Da ich jedoch Fan
Client-Rechnern für PO und Teammitglieder. Von Verteilung der Automatisierungsplattform Make.com bin, sehe ich na-
würde ich deshalb aber noch nicht sprechen. Wenn ein PO- türlich überall Nägel für diesen Hammer: Das Backend rea-
Client auf eine Festplatte auf einem Server zugreift, tut er das lisiere ich in Form von Make.com-Szenarien. In Make.com ist
mit eigenem Code. Das Persistenzmedium erscheint ihm als der Zugriff auf die Dropbox trivial und schön visuell.
„dumm“; in der Nutzung der APIs des Persistenzmediums In Bild 4 unterscheidet sich das Backend in der grundsätz-
steckt die Intelligenz, die liegt beim Client. lichen Darstellung nicht von den Frontends. Das ist korrekt:
Dafür braucht ein Client jedoch das Wissen über die APIs Egal wie die Implementation aussieht, es wird Portale, Pro-
und auch noch unmittelbare Zugriffsrechte auf das Persis- vider und Domäne geben. Die werden in immer gleicher Wei-
tenzmedium. Bei einer Inhouse-Desktop-Applikation würde se dargestellt. Die Ausprägungen hingegen mögen stark va-
ich darüber nicht weiter nachdenken. Wenn die Applikatio- riieren:
nen jedoch potenziell im Web laufen und dann auch noch Wenn ich mich entscheiden sollte, das Crowd-Frontend mit
Code im Browser am Start ist … würde ich die APIs und C# und das PO-Frontend mit Python zu implementieren,
Credentials nicht in den Clients haben wollen. ist der Code für die gleich benannten Provider natürlich
Diese minimale Sicherheitsanforderung veranlasst mich unterschiedlich.
dazu, ein Backend für die Datenbank auszuprägen. Das Soft- Ein Provider in C# sieht sicher anders aus als einer, der in
waresystem zerfällt damit in drei Worker (Bild 4). Wie die Wor- Make.com den Zugriff auf die Dropbox tatsächlich durch-
ker zu ihren Zugriffsrechten auf den Datenbankserver kom- führt.
men (Autorisierung), ist eine andere Sache. Die lasse ich hier
aus, weil ich schon mit der bisherigen Sicherheitsanforde- Die „Kärtchen“ in den Abbildungen sind nur Platzhalter. Sie
rung zu einem Backend-Worker gekommen bin. Mehr woll- zeigen an, was ich mindestens brauche und nicht vergessen
te ich nicht. darf. Implementationsdetails sind auf dieser Flughöhe nicht
Im Worker für die Datenbank erwarte ich keine Domänen- zu sehen.
logik. Eine solche könnte dort zentral angesiedelt werden, Bisher hat die Flughöhe auch immer noch einen Überblick
falls sie von der Nähe zu den Daten profitieren würde, doch über das Gesamtsystem gestattet. Ich bin breadth-first vorge-
in diesem Szenario ist das nicht der Fall. Das Backend ist in- gangen. Mit dem nächsten Schritt näher ans System heran
sofern im Grunde nur ein Gateway zu den konkreten Funk- wird sich das ändern. Ich muss mich konzentrieren, um ge-
tionen für den Umgang mit dem Persistenzmedium. nauer hinschauen zu können.
Weiter geht es mit dem konkreten Umgang der Rollen mit
den Frontends. Wie soll die Bedienung aussehen? Da-
raus leiten sich Schnittstellen und Datenstruk-
turen ab.
Das Frontend für den PO
Der PO stößt die Ordnung von Positi-
onen für einen gewissen Zweck an. Er
definiert eine Sitzung mit ihren Positio-
nen, die anschließend von den Teammit-
gliedern individuell geordnet werden sol-
len – um am Ende zu einer gemeinschaft-
lichen Ordnung verrechnet zu werden.
Ich sehe ganz grob folgende Aktivitäten
beim PO:
Der PO legt eine Sitzung mit einer kurzen
Beschreibung an, zum Beispiel „Sprint KW
19: Ordne die User Stories in absteigender
Komplexität an.“
Zerlegung des Der PO füllt die Sitzung mit Einträgen, das
Softwaresystems heißt den zu ordnenden Positionen, zum
in Worker, um nicht­ Beispiel „User können sich mit E-Mail und
funktionale Anf orderun­ Passwort anmelden“, „User können ihr
gen zu erfüllen (Bild 4) Passwort zurücksetzen“, „User können ▶
www.dotnetpro.de 12.2024 33
003300--003399__SSlleeeeppyyHHoollllooww__eeaa__ffss__eeaa..iinndddd 3333 0044..1111..2244 1166::3388


---


<!-- Page 5 of 10 -->


PLANUNG Sleepy Hollow
sich mit E-Mail und Passwort registrieren“, „User bekom-
men eine Registrierungsbenachrichtigung per E-Mail und
können sie bestätigen“.
Der PO veröffentlicht die Sitzung zur Ordnung durch die
Teammitglieder.
Der PO verfolgt die Entwicklung der gemeinschaftlichen
Ordnung.
Das ist das Mindeste. Weitere Aktivitäten könnten sein: Der
PO schaut sich ältere Sitzungen an, der PO löscht Sitzungen,
der PO verändert eine Sitzung, der PO leitet eine neue Sit-
zung von einer vorherigen ab, Veränderungen an der ge-
meinschaftlichen Ordnung werden automatisch dargestellt …
Im Slicing können Sie den Umgang mit einem Softwaresys-
tem in drei Schritten konkretisieren:
Perspektiven
Dialoge
Interaktionen
Wie bei Applikationen und Workern ist kein Slice zwingend
zu schneiden. Sie greifen dort zu, wo es nützlich für Sie ist,
um Klarheit zu gewinnen. Ziel sind die Interaktionen. Sie re-
präsentieren testbare Eintrittspunkte im Code.
Die Frage ist: Was soll automatisiert testbar werden, und
was soll andererseits ein Detail der Benutzerschnittstelle blei-
ben und nicht automatisiert getestet werden?
Aus meiner obigen Beschreibung der PO-Aktivitäten leite Skizze der Bedie­
ich schon mal zwei testwürdige Interaktionen ab: nung des PO­
Veröffentlichung einer Sitzung: Die Sitzung mit ihren Ein- Frontends (Bild 5)
trägen wird im Backend gespeichert. Anschließend können
die Teammitglieder mit ihrem Crowd-Frontend darauf zu-
greifen. flüssig. Und ich denke, ich komme mit zwei Dialogen aus:
Anzeige des aktuellen Stands der gemeinschaftlichen Ord- Publizieren
nung für die Reflexion mit dem Team: Die von den Team- Reflektieren
mitgliedern eingereichten individuellen Ordnungen wer-
den vom Backend geladen und zu einer gemeinschaftlichen Oder beide Interaktionen könnten sogar in einem Dialog zu-
Ordnung verrechnet. sammengefasst sein. Bild 5 skizziert, wie ich mir den Umgang
mit dem PO-Frontend in einem Terminalfenster vorstelle.
Wie wird eine Sitzung zusammengestellt? Das ist ein Detail Hervorgehoben habe ich Benutzereingaben und Interaktio-
der Benutzerschnittstelle. Im allereinfachsten Fall könnte ein nen. Hinzugekommen ist noch eine Interaktion fürs Starten,
PO eine JSON-Struktur in ein Textfeld eintragen. Aber das um auch bei erneutem Programmaufruf auf eine vorherige
ist natürlich nicht benutzerfreundlich, also wird das UI es dem Sitzung zugreifen zu können.
PO etwas bequemer machen, die Daten zu sammeln. Aber ich könnte natürlich auch eine stärker visuell ausge-
Wenn das ebenfalls testwürdig sein sollte, kann ich weite- richtete Benutzerschnittstelle entwerfen (Bild 6). An den Inter-
re Interaktionen explizieren, zum Beispiel: aktionen ändert das nichts. Auch hinter einem GUI oder ei-
Sitzung anlegen mit einer kurzen Beschreibung. nem Web-UI stehen dieselben Entry-Point-Funktionen.
Sitzung um einen Eintrag erweitern. Sie sehen, aus Sicht des Entwicklers ist das UI zunächst
Einen Eintrag aus einer Sitzung löschen. nicht so wichtig. Es trägt nichts zur „eigentlichen Verarbei-
tung“ bei. Das Verhalten der Software insgesamt, das heißt
Der Einfachheit halber möchte ich mich jedoch auf die bei- die Transformation von Input in Output, findet hinter dieser
den obigen Interaktionen konzentrieren: Veröffentlichung, Fassade statt.
Reflexion. Das macht die Fassade nicht unwichtig. Ohne gute Usabili-
Jetzt bin ich aber schon gleich auf der Ebene der Interak- ty wird auch die schönste Transformation nicht genutzt. Doch
tionen gelandet. Was ist mit Perspektiven und Dialogen? Wie ohne saubere Transformation, das heißt korrekte, verständli-
gesagt: Sie sind nicht zwingend für das Ziel von Slicing. In che, wandelbare Softwarestrukturen, lohnt sich kein Aufwand
diesem Fall brauche ich sie nicht, glaube ich. Die Benutzer- für Usability. Deshalb ist das UI im Detail für mich zweitran-
schnittstelle ist nicht weitläufig, also sind Perspektiven über- gig. Ich will mir (zunächst) nur so viel davon klarmachen, wie
34 12.2024 www.dotnetpro.de
003300--003399__SSlleeeeppyyHHoollllooww__eeaa__ffss__eeaa..iinndddd 3344 0044..1111..2244 1166::3388


---


<!-- Page 6 of 10 -->


PLANUNG Sleepy Hollow
ich brauche, um die Interaktion zu erkennen,
die mir die Slicing-Entry-Points auf den Sleepy-
Hollow-Processor-Schnittstellen beschreiben. Alternative
Wenn ich sie nach Bild 2 schon hätte listen Skizze für das
können, hätte ich mir einigen Aufwand sparen PO­Frontend
können. Doch auf dieser Flughöhe habe ich sie (Bild 6)
noch nicht gesehen. Also habe ich hineinge-
zoomt. Die Slicing-„Zoomstufen“-Perspektive
konnte ich allerdings überspringen. Und bei
Interaktionen in Dialogen bin ich nicht streng
„von oben nach unten“ vorgegangen, weil der
Scope des Frontends so überschaubar ist.
Das Frontend für die Crowd
Für die Teammitglieder sieht der Client noch
einfacher aus. Was ist ihre Aufgabe? Ordnung
in die Positionen einer Sitzung bringen: Sobald
eine Sitzung publiziert ist, können Teammit-
glieder sie öffnen, sehen die Positionen in ihrer
Ordnung (beziehungsweise zu Anfang in der erfassten Rei- Theoretisch könnte ein solches verteiltes Ordnen auch
henfolge) und ordnen sie um. Wenn sie mit ihrer Ordnung zu- ohne Benutzerschnittstelle ablaufen:
frieden sind, reichen sie sie ein zur Verrechnung mit allen an- Der PO legt in einem Dropbox-Verzeichnis eine Datei (ses-
deren eingereichten, individuellen Ordnungen. sion.txt) mit den zu ordnenden Positionen ab. In jeder Zei-
Hören Sie schon aus dieser Beschreibung die Interaktionen le steht eine Position mit einer ID, zum Beispiel einem In-
heraus? Oder wäre es Ihnen lieber, sich an sie schrittweise dex 1..n.
über Perspektiven und Dialoge heranzuarbeiten? Die Teammitglieder öffnen diese Datei und speichern ihre
Ich denke, wir können einen Sprung wagen. Die Interak- individuelle Ordnung in einer neuen Datei (peter.txt, paul.
tionen für den Crowd-Client sind: txt, maria.txt) als Folge von Position-IDs, zum Beispiel „2,
Starten mit Öffnung einer Sitzung. 1, 3“.
Einreichen der eigenen Ordnung. Ein automatischer Prozess (oder ein von Hand gestarteter)
erzeugt eine Ergebnisdatei, die die Positionen mit IDs und
Wie die eigene Ordnung hergestellt wird, ist ein Detail der Bezeichnungen in einer weiteren Datei ablegt (result.txt).
Benutzerschnittstelle. In einem GUI- oder Web-Frontend ge-
schieht das anders als in einem Console-Frontend (Bild 7). Fertig. In dieser Variante gäbe es nur eine einzige Interak-
tion: den Start des Verrechnungsprozesses.
Was ich damit sagen will: Wir lassen uns oft durch Benut-
zerschnittstellen ins Bockshorn jagen. Und mit grafischen Be-
nutzerschnittstellen, die hübsch und animiert und ganz CI-
konform sein sollen, gleich doppelt. Die eigentlich interessan-
te Verhaltensweise von Software hat oft nichts damit zu tun.
Darum finde ich es beim Slicing wichtig, die Benutzer-
schnittstelle so abstrakt wie möglich, so konkret wie nötig zu
betrachten. Verlieren Sie nicht das Ziel aus den Augen: Es
geht (zunächst) nur darum, die Entry Points zu finden. Denn
sind die Entry Points definiert, kann die Arbeit am zentralen
Verhalten der Software beginnen. Die Domäne liegt hinter der
Schnittstelle der Processor-Integrationen von Sleepy Hollow.
Indem ich hier zwei Applikationen mit eigenen Frontends
„herausanalysiert“ habe, bin ich also schon über einen Proof
of Concept (PoC) weit hinausgegangen. Ob das Verfahren
„relative Ordnung“ (oder konkreter: relative, vergleichende
Schätzung) überhaupt interessant ist, könnte einfacher getes-
tet werden.
Ein allererster PoC für die Machbarkeit könnte mit Google
Skizze für das Sheet realisiert werden. Der PO trägt in einer Google-Sheet-
Crowd­Front­ Datei die Positionen ein, und die Teammitglieder „numme-
end (Bild 7) rieren“ diese in je eigenen Spalten nach ihren Vorstellun- ▶
www.dotnetpro.de 12.2024 35
003300--003399__SSlleeeeppyyHHoollllooww__eeaa__ffss__eeaa..iinndddd 3355 0044..1111..2244 1166::3388


---


<!-- Page 7 of 10 -->


PLANUNG Sleepy Hollow
gen. Ständig wird eine gemein-
schaftliche Ordnung auf einem
zweiten Tabellenblatt angezeigt.
Das sollte ein No-brainer sein.
So wäre die Herangehensweise
effizient und effektiv. Ob es über-
haupt mehr braucht als ein Goog-
le Sheet, würde sich herausstel- Signaturen der Entry Points (Bild 8)
len. Allerdings bliebe dabei der
Programmierspaß auf der Stre-
cke, und ich müsste mir ein anderes Szenario für die Demons- Unter der Oberfläche der Interaktionen, die in Dialogen
tration von Slicing und Sleepy Hollow ausdenken. von Workern in Applikationen stattfinden, liegt Code. Das
Aber sehen wir einmal darüber hinweg. Wir sind hier in Pendant von Interaktionen sind Entry Points, das heißt Funk-
einem Sandkasten, in dem vieles nicht ganz real(istisch) ist. tionen, die im Rahmen der Interaktionen getriggert werden.
Zumindest einmal wollte ich jedoch so weit zurücktreten und Sie sind Ansatzpunkte für automatisierte Tests. Durch sie
reflektieren. Nicht, dass Slicing oder Sleepy Hollow in den kann ein Softwaresystem „headless“ betrieben werden –
Verruf kommen, Projektaufwände in die Höhe zu treiben. oder eben auch mit verschiedenen Heads. Deshalb ist mir das
Nein, im Gegenteil: Es geht mir stets um „das rechte Maß“ Sleepy-Hollow-Architekturmuster so wichtig.
(das oft kleiner ist als das, wohin ein Projektteam tendiert). Bei geklärten Interaktionen ist also jetzt die Frage, wie da-
zu die Entry Points aussehen sollten. Das Command-Query-
Die Entry Points für die Interaktionen
Separation-Prinzip (CQS) kann hier auch helfen, um noch
Für mein Gefühl ist genügend Klarheit an der Oberfläche weiter zu differenzieren und Entry Points nicht zu überladen.
hergestellt. Die grobe Struktur des Softwaresystems ist defi- Zu Entry Points gehört als Erstes eine Signatur mit typisier-
niert, die Interaktionen sind herausgearbeitet. Damit bin ich ten Parametern und Rückgabewert. Für mich ist das in erster
bereit, unter die Oberfläche zu tauchen. Linie ein „Wunschkonzert“: Wie stelle ich mir die Entry Points
idealerweise vor? Wie vermeide ich, dass an ihnen (enge)
Kopplung zwischen Head und Body entsteht?
Ich versuche es mit einem ersten Pass über die Interaktio-
nen mit Blick durch die CQS-Brille:
PO-Frontend
• Starten: Eine Query, die gegebenenfalls eine Sitzung
für eine gegebene ID heraussucht.
• Publizieren: Ein Command, das eine Sitzung speichert,
also den Datenbankzustand verändert.
• Aktualisieren: Eine Query, die individuelle Ordnungen
liest und zu einer gemeinschaftlichen verrechnet (die
nicht in der Datenbank gespeichert wird).
Crowd-Frontend
• Starten: Eine Query, die eine Sitzung und gegebenen-
falls die schon vorhandene individuelle Ordnung eines
Users heraussucht.
• Einreichen: Ein Command, das eine individuelle Ord-
nung in der Datenbank speichert.
Aus CQS-Sicht sind die Interaktionen also sauber. Das ist ein
guter Anfang. Jetzt weiter ins Detail: die Signaturen.
Was soll an einen Entry Point übergeben werden? Was wur-
de in der Benutzerschnittstelle gesammelt?
Was soll ein Entry Point liefern? Was soll in der Benutzer-
schnittstelle projiziert werden?
Welche Seiteneffekte (Zustandsänderungen) treten auf?
Welche Daten(strukturen) zum Beispiel in einer Datenbank
sind wie beteiligt?
Bild 8 zeigt, wie ich mir die Signaturen und die groben Seiten-
effekte vorstelle. Wie Sie sehen, ist aus der reinen Query Star-
Die Schnittstellen für die Entry Points (Bild 9) ten nun ein Hybrid geworden. Es wird nicht nur aus der Da-
36 12.2024 www.dotnetpro.de
003300--003399__SSlleeeeppyyHHoollllooww__eeaa__ffss__eeaa..iinndddd 3366 0044..1111..2244 1166::3388


---


<!-- Page 8 of 10 -->


PLANUNG Sleepy Hollow
tenbankressource und auch der ClientID-Ressource gelesen. vor allem das, was von der Processor-Integration verbunden
Falls die Client-Instanz noch keine ID hat, wird auch eine ge- wird. Aber auch der Interactor kann noch dazugezählt wer-
schrieben. Das halte ich aber für einen vernachlässigbaren den, weil er ebenfalls dafür sorgt, dass Logik von den tech-
Seiteneffekt, der auch nur einmal pro Instanz auftritt. Für nologischen Feinheiten eines UI getrennt ist. Aber der Inter-
mich bleibt das Starten also eine Query. actor ist optional. Der Body ist vergleichsweise leicht zu tes-
Eine KI wie ChatGPT oder Claude hilft mir, aus der Tabel- ten (auch wenn darin Ressourcenabhängigkeiten stecken).
le zwei Interfaces abzuleiten (Bild 9). Durch das Sleepy-Hol- Der Head ist das UI in der einen oder anderen Ausprägung.
low-Architekturmuster weiß ich, dass und wo ich sie brauche Es ist technologiespezifisch und schwer zu testen. Deshalb
(siehe unten). wird es vom Body getrennt, isoliert.
Woher weiß ich, dass die Entry Points „gut und richtig“ Wie dieses Muster auf das hiesige Softwaresystem ange-
sind? Ich weiß es nicht. Ich muss es auch nicht zu 100 Prozent wendet werden kann, zeigt Bild 11. Die Strukturelemente der
wissen. Dieser erste aus der Anforderungsanalyse abgeleite- bisherigen „Zoomstufen“ finden sich darin – und auch die
te Entwurf für die Schnittstelle des Bodys muss nur gut genug neuen Integrationsbausteine: App, Interactor und Processor.
sein, um mir Gedanken über Akzeptanztests machen zu kön- Die Schnittstellen aus Bild 9 sind die für die Integratoren in
nen. Während ich die durchgehe, merke ich, ob die Entry der Mitte, die mit dem „You are here“-Symbol gekennzeich-
Points wirklich plausibel sind. Test-first-Vorgehen hilft bei net sind. Die Anforderungsanalyse hatte also vor allem das
der Ausgestaltung von Schnittstellen. Eine Form von „eating Ziel, genau diese Integrationen zu bestimmen und auszu-
your own dog food“. prägen. Sie sind die Ansatzpunkte für Akzeptanztests; von
Die Tests stellen sehr reduzierte Benutzerschnittstellen dar. ihnen aus werden die Schnittstellen der darunter hängen-
Ich merke also schon mit ihnen, ob meine Idee der Zustands- den schon sichtbaren und weiterer noch zu findender Bau-
haltung in den Prozessoren taugt. Haben Sie bemerkt, dass steine getrieben.
ich die Interfaces so gestaltet habe, dass ihre Implementatio- Die Verteilung auf Worker habe ich in Bild 11 bewusst über-
nen zustandsbehaftet sein müssen? Sie sehen es zum Beispiel gangen. Sie trägt nichts zum Verständnis des grundlegenden
daran, dass bei IPOProcessor.update() keine sessionID über- Architekturmusters bei. Am Ende läuft der Durchstich je In-
geben wird. Woher weiß die Implementation, um welche Ses- teraktion mit oder ohne Verteilung vom Prozessor bis zum
sion es geht? Sie hat sich die Session vorher bei start() oder Provider mit Ressourcenzugriff.
publish() gemerkt.
Akzeptanztests für die Entry Points
Prozessoren mit Zustand ziehe ich vor, weil damit mehr Lo-
gik testbar wird. Ein Head über dem Sleepy-Hollow-Body soll Da stehe ich nun mit zwei Schnittstellen für Integrationen „ir-
so wenig wie nur irgend möglich leisten. Es kann daher so- gendwo in der Mitte“ der Architektur. Was soll das? Ist das
gar dazu kommen, dass ich die Prozessoren nochmal mit ei- nicht ein bisschen wenig?
ner weiteren Schicht umwickle, die dem UI Arbeit abnimmt Nein, das ist der natürliche Endpunkt der Anforderungs-
und sie testbar macht. Mal sehen … analyse. Der ist sogar schon viel detaillierter als alles, was üb-
licherweise bei der Anforderungsanalyse herauskommt.
Die Sleepy-Hollow-Architektur
Überlegen Sie einmal, womit Sie Ihr PO sonst so zurücklässt,
Jetzt rede ich immer von Prozessoren, auf denen die Entry wenn er meint, die User Stories seien besprochen.
Points sitzen, aber wo sind die in der Architektur, wie ist de- Mit dem Sleepy-Hollow-Architekturmuster ist von vornhe-
ren Verhältnis zu den Strukturelementen, die ich schon he- rein klar, dass es Prozessoren gibt, die „ein API“ mit Funktio-
rausgearbeitet habe? nen anbieten, die quasi eins zu eins den Interaktionen der
Betrachten wir zur Erinnerung noch einmal das Sleepy- Benutzerschnittstelle entsprechen. Sie wissen sogar, was ▶
Hollow-Architekturmuster [3] in Bild 10.
Zu sehen sind die Arbeitspferde einer An-
wendung: Portale, Provider und Domäne.
Darin steckt die verhaltenserzeugende
Logik.
Ins Auge stechen jedoch mehr die gel-
ben Integratoren. Ihre Aufgabe ist es,
ganz ohne Logik die Arbeitspferde zu ei-
nem leistungsfähigen Gespann zusam-
menzuschirren. Diese Integratoren, die in
einer Übersicht wie Bild 3 ganz bewusst
nicht zu sehen sind, machen das Beson-
dere der IODA-Architektur [6] und des
darauf aufbauenden Sleepy-Hollow-Ar- Das Architekturmuster
chitekturmusters aus. Sleepy Hollow (Bild 10)
Als Body, der die eigentliche Leistung
einer Anwendung erbringt, bezeichne ich
www.dotnetpro.de 12.2024 37
003300--003399__SSlleeeeppyyHHoollllooww__eeaa__ffss__eeaa..iinndddd 3377 0044..1111..2244 1166::3388


---


<!-- Page 9 of 10 -->


PLANUNG Sleepy Hollow
grundsätzlich darüber und darunter passiert. Genaue Kennt- Die Formulierung der Testszenarien selbst ist davon jedoch
nis ist jedoch noch nicht nötig. Für den nächsten Schritt, den unabhängig. Darin spielen nur die unmittelbar zu testenden
wahren Abschluss der Anforderungsanalyse, reicht es, dass Bausteine (hier: die Prozessoren) eine Rolle.
Sie die Prozessoren mit ihren Schnittstellen kennen. Denn mit Aufgabe von Akzeptanztests ist nicht, die komplette Logik
diesen Schnittstellen legen Sie den PO final auf den Grill: Sie eines Bodys durchzuexerzieren. Es geht um das Big Picuture,
fordern von ihm Testszenarien, die Sie dann mit den Entry die wichtigsten Zusammenhänge, ein Gefühl dafür, ob typi-
Points umsetzen. Ohne solche Akzeptanztests sollten Sie den sche Use Cases abgedeckt sind.
PO nicht ziehen lassen. Es droht Unterspezifikation mit bitte- Für das vergleichende Ordnen mögen dies repräsentative
ren Folgen: unnötige Kommunikation, Konflikte, Unzuverläs- Akzeptanztests sein:
sigkeit, Nachbesserungen. Neue Sitzung publizieren.
Akzeptanztests, die für den PO Sinn ergeben, sind Teil des • Starten ohne SessionID.
Full Kitting [5], das Sie betreiben sollten, bevor Sie sich zu • Publizieren einer Session mit der Beschreibung „B“
weiterem Entwurf und Umsetzung zurückziehen. Sie sollten und den Einträgen „X“, „Y“, „Z“. Es wird eine Ses-
alles bei der Hand haben, was Sie brauchen, um gut passen- sionID geliefert.
den Code „in einem Rutsch“ liefern zu können. Das ist vor al- • Aktualisieren der Session in der Erwartung, dass die
lem ... Klarheit. So viel Klarheit, wie Sie nur kriegen können. Einträge „X“, „Y“, „Z“ in der Reihenfolge geliefert
Klare Schnittstellen und klare Erwartungen an Output für In- werden.
put sind das Mindeste. Sitzung individuell das erste Mal ordnen.
Akzeptanztests sind natürlicherweise Integrationstests. Sie • Starten mit einer SessionID. Es werden Beschreibung
setzen an Bausteinen an, die auf die eine oder andere Weise nur „B“ und die Einträge [{0, „X“}, {1, „Y“}, {2, „Z“}] ge-
„die Spitze des Eisbergs“ der Verarbeitung darstellen. Es stellt liefert.
sich daher die Frage, ob Sie im Akzeptanztest hinunter bis auf • Einreichen der individuellen Ordnung [2,1,0].
die eigentlichen Ressourcen testen (hier: Dropbox-Dateien) Sitzung individuell das erste Mal durch einen weiteren Cli-
oder ob Sie einfachere, billigere, besser kontrollierbare Res- ent ordnen lassen.
sourcen einschalten (Attrappen der einen oder anderen Art). • Starten mit einer SessionID. Es werden Beschreibung
Diese Entscheidung möchte ich hier nicht weiter diskutie- „B“ und die Einträge [{0, „X“}, {1, „Y“}, {2, „Z“}] ge-
ren. Nur so viel sei gesagt: Wenn Sie sich für Attrappen ent- liefert.
scheiden, müssen Sie für Akzeptanztests auch die Schnittstel- • Einreichen der individuellen Ordnung [0, 2, 1].
len der Provider für zu ersetzende Ressourcen kennen, um da- Starten einer existierenden Sitzung und Aktualisieren nach
für Surrogate bauen und Prozessoren unterschieben zu kön- individuellen Ordnungen.
nen. Das erfordert zu diesem Zeitpunkt weiteren Entwurfsauf- • Starten mit SessionID; es werden Beschreibung „B“
wand und verzögert das Aufsetzen von Akzeptanztests. und die Einträge „X“, „Y“, „Z“ geliefert.
Konkrete
Sleepy-
Hollow-
Architektur
für das Soft­
waresystem
(Bild 11)
38 12.2024 www.dotnetpro.de
003300--003399__SSlleeeeppyyHHoollllooww__eeaa__ffss__eeaa..iinndddd 3388 0044..1111..2244 1166::3388


---


<!-- Page 10 of 10 -->


PLANUNG Sleepy Hollow
• Aktualisieren der Session. Die Erwartung ist, dass sich in Anforderungen versteckt sind. Wir sind keine Experten
die Ordnung gegenüber der ursprünglichen verändert für Anforderungen. Die muss der PO schon selbst definie-
hat. Sie soll nun „Z“, „X“, „Y“ lauten. ren. Präzise!
Ich bekomme Klarheit darüber, wie meine grobe Architek-
Ich habe diese Tests zwar separat formuliert, doch für mich tur aussieht und wo die Startpunkte liegen, mit denen ich
spannen sie eigentlich einen Bogen. Ich würde sie zusammen in Entwurf und Codierung einsteige.
laufen lassen. Das nenne ich ein Szenario. In diesem Szena-
Zwischenstand
rio wird eine Sitzung definiert und publiziert, von zwei Team-
mitgliedern individuell geordnet und am Ende das Ergebnis Ausgehend von einer Anforderungsskizze habe ich mit Sli-
betrachtet. Da ist alles Wesentliche dabei, das in der Praxis cing eine Liste von Funktionen bestimmt, mit denen sich die
über zwei Clients verteilt passiert, nur ist es hier für besseren Anforderungen verhaltensmäßig abdecken lassen. Für zwei
Überblick und bessere Testbarkeit in einem Test zusammen- Verhaltensszenarien habe ich konkrete Vorstellungen entwi-
gefasst. ckelt, die ich als Akzeptanztests gegen die Funktionen lau-
Auf diese Weise muss ich mir weniger Gedanken über die fen lassen kann. Damit habe ich eine Ziellinie gezogen. Die
Überprüfung von Zuständen machen. Wird die Einreichung ist erreicht, sobald diese Tests grün sind.
einer individuellen Ordnung wirklich gespeichert? Das mer- Das Sleepy-Hollow-Architekturmuster hat mir ein Terrain
ke ich am Ende, wenn das Resultat stimmt oder nicht. geliefert, in dem ich genau verortet bin. Ich weiß, wo ich ste-
Allerdings fühle ich jetzt schon, dass hier und da die Pro- he, was ich habe – und ich weiß, was noch fehlt, was nun nä-
zessor-Schnittstellen nicht ausreichen. Wie unterscheide ich her zu entwerfen und dann zu codieren ist.
zum Beispiel die beiden Crowd-Clients? Sie laufen während Jetzt habe ich alles beieinander, um mit möglichst wenig
des Tests ja im selben Prozess, dürfen jedoch nicht dieselbe Kommunikation mit einem PO meinen eigentlichen Job zu
ClientID haben. Brauche ich dafür eine Attrappe für den Cli- machen. Ich habe Full Kitting so weit wie möglich betrieben.
entID-Provider? Das ist ein Detail, das ich bei der Implemen- Sicher gibt es noch eine Grauzone, nicht alles lässt sich vor
tation des Tests entscheide. der Codierung haarklein bestimmen. Ich will ja auch nicht in
Wie steht es mit der Abdeckung? Nicht der Code-Pfadab- einen Wasserfall zurückfallen. Doch ich empfinde, dass ich
deckung, sondern der Feature-Abdeckung. Ist in dem Akzep- mich zumindest gut präpariert habe. Ohne Vorbereitung in
tanztest alles Interessante getestet? Nein. Es fehlt die Verän- das Abenteuer Codierung einzusteigen ist zu wenig.
derung einer Sitzung, wie in Bild 5 als Möglichkeit gezeigt. Jetzt ist mein Rucksack gepackt, und ich habe eine Karte
Das wäre einen zweiten Szenariotest wert: in der Hand. Damit geht es nächstes Mal los in die Implemen-
Neue Sitzung publizieren wie oben. tation. ◾
Sitzung individuell ordnen wie oben.
Existierende Sitzung verändern. [1] Ralf Westphal, Strukturiert zerlegen, dotnetpro 4/2024,
• Starten der gerade publizierten Sitzung. Seite 42 ff., www.dotnetpro.de/A2404Slicing
• Publizieren mit den Einträgen „X“, „Y“, „Z“, „AA“; es [2] Ralf Westphal, Inkremente innerhalb von Interaktionen
wird eine neue Sitzungnummer zurückgeliefert. finden, dotnetpro 9/2024, Seite 32 ff.,
Sitzung individuell ordnen. www.dotnetpro.de/A2409Slicing
• Starten mit der neuen Sitzungnummer; es sollten die [3] Ralf Westphal, Den Kopf vom Körper trennen,
Beschreibung „B“ und die Einträge [{2, „Z“}, {1, „Y“}, dotnetpro 11/2024, Seite 46 ff.,
{0, „X“}, {3, „AA“}] zurückgeliefert werden. www.dotnetpro.de/A2411SleepyHollow
• Einreichen der individuellen Ordnung [2, 3, 0, 1]. [4] Ralf Westphal, TotalOrder: Konsequent vergleichend
Starten der neuen Sitzung und Aktualisieren. schätzen, www.dotnetpro.de/SL2412SleepyHollow1
• Starten mit neuer SessionID; es sollte „B“ und [„X“, [5] Goldratt UK, A Simple but Highly Effective Way to
„Y“, „Z“, „AA“] geliefert werden. Increase Output: Full-Kitting,
• Aktualisieren; das Ergebnis sollte [„Z“, „AA“, „X“, www.dotnetpro.de/SL2412SleepyHollow2
„Y“] sein, weil nur ein Teammitglied eine Ordnung [6] Ralf Westphal, IODA Architecture,
eingereicht hat. www.dotnetpro.de/SL2412SleepyHollow3
Das sind für einen PO greifbare Formulierungen, würde ich
sagen. Sie sind frei von technischen Feinheiten, und trotzdem Ralf Westphal
sind sie präzise für mich als Entwickler. Ich weiß genau, wel- ist Trainer, Berater und Mitgründer der Clean
che Funktion ich wie aufzurufen habe – während der PO nur Code Developer Initiative (https://clean­code­
in Interaktionen denkt. So begegnen wir uns auf Augenhöhe: developer.de). Seine Schwerpunkte sind dauer­
Der PO bekommt Klarheit darüber, was er will, was seine haft hohe Produktivität für die Softwareent­
Erwartungen sind. Es ist zu wenig, wenn er nur mit den wicklung und zukunftsfähige Teamorganisation.
Händen wedelt und sagt: „Na ja, du weißt schon …“ oder https://ralfw.de
„Du bist doch der Experte“. Klar, ich bin der Experte, Sie
dnpCode A2412SleepyHollow
sind der Experte. Für Codierung von Transformationen, die
www.dotnetpro.de 12.2024 39
003300--003399__SSlleeeeppyyHHoollllooww__eeaa__ffss__eeaa..iinndddd 3399 0044..1111..2244 1166::3388