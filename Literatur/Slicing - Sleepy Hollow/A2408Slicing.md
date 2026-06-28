<!-- Page 1 of 10 -->


PLANUNG Slicing
ANFORDERUNGSANALYSE FÜR ENTWICKLER, TEIL 5
Grobe Schnitte durch
die Anforderungen
Die Ebenen Kontexte und Worker ergänzen die Slicing-Hierarchie und tragen in großen
Softwaresystemen zu präzisen, testbaren Anforderungen und robuster Architektur bei.
Teile und herrsche!“ ist ein immer wieder zitiertes Prinzip kümmert“ (horizontales Modul) oder „Code, der sich um
nicht nur in der Politik, sondern auch in der Softwareent­ die Benutzeranmeldung kümmert: vom UI bis zur Persis­
wicklung. Wenn etwas zu groß oder zu unübersichtlich ist, tenz“ (vertikales Modul).
dann sollte man es in Teile zerlegen, von denen jeder für sich Benannt: Module haben einen Namen, der den darin ver­
überschaubar ist. Und die Beziehungen zwischen den Teilen sammelten Code kurz und knapp mit einem Etikett ver­
werden zu einem weiteren „Teil“, den man dann ebenfalls sieht, zum Beispiel „Repository“ oder „Authentifizierung“.
leichter überblicken kann. Ja, es ist geradezu so, dass die Be­ Logik: Logik ist der Code, der in einem Modul versammelt
ziehungen dann erst überhaupt managebar werden, weil sie wird, und der Code, der das „thematische“ Verhalten eines
nun explizit sind. Wo vorher in einem zu großen Ganzen As­ Moduls erzeugt. Wenn die Logik auch noch Daten braucht,
pekte nur erahnbar waren und ihre Beziehungen im Nebel können diese ebenfalls im Modul angesiedelt werden.
lagen, liegt beides nach einer Tei­
lung übersichtlich und klar vor.
Hoffentlich. Denn die Teilung
muss einen Sweet Spot treffen: Sie
darf nicht zu grob sein, denn dann
bringt sie keinen Klarheitsgewinn.
Sie darf allerdings auch nicht zu
fein sein, denn dann schafft sie
neue Unübersichtlichkeit. Zu viel
von allem kann genauso überfor­
dern wie zu groß.
Doch was, wenn der Sweet Spot
immer noch dort liegt, wo die ent­ Schrittweise Zerlegung eines Ganzen in Teile (Bild 1)
stehenden Teile zu groß für einfa­
ches Verständnis sind? Dann kann
das Prinzip auf sie erneut angewandt werden. Und nochmal, Funktionen: Die Logik eines Moduls muss von außen gezielt
falls nötig. Und nochmal und nochmal und immer so weiter. angesprochen werden können. Das geschieht über Funk­
„Teile und herrsche!“ ist ein rekursives Prinzip, das zu einer tionen mit ihren Namen und Parametern, zum Beispiel
rekursiven Struktur führt: einem Baum aus Teilen, die wiede­ Load(), Store(), Map(), Serialize().
rum Ganze sein können mit weiteren Teilen, eine sogenann­ Schnittstelle: Was die Umwelt eines Moduls vom Modul
te Holarchie. Bild 1 zeigt eine solche Zerlegung eines Ganzen wissen darf, veröffentlicht es in seiner Schnittstelle. Sie ist
in kleinere und kleinere Teile. im einfachsten und besten Fall eine Liste von außen sicht­
Der Bereich in der Softwareentwicklung, auf den „Teile barer/aufrufbarer Funktionen. Weitere Funktionen und
und herrsche!“ vor allem angewendet wird, ist der Code. Das auch Daten mögen ebenfalls zum Modul gehören, doch da­
Prinzip folgt der Empfehlung, Code zu modularisieren. Darum von bekommt die Außenwelt keine Kenntnis. Die Schnitt­
geht es auch beim Prinzip der Separation of Concerns (SoC). stelle sorgt dafür, dass Module Codedetails tatsächlich kap­
Module sind benannte Aggregate von Logik, gekapselt in seln – deshalb sind Namensräume in C# keine Module, son­
Funktionen und versehen mit einer Schnittstelle: dern eben nur Horizonte einzigartiger Bezeichner. Durch
Aggregat: Module versammeln Code in sich, der sich irgend­ eine Schnittstelle würde zum Beispiel unterschieden zwi­
wie (thematisch) ähnelt. Als Abstraktionen ziehen Module schen den Funktionen Load() und Store(), die öffentlich
eine Linie um Code, der „irgendwie zusammengehört“, sind, und Map() und Serialize(), die von diesen aufgerufen
zum Beispiel „Code, der sich um die Persistenz der Daten werden, aber nicht öffentlich sind, das heißt privat.
30 8.2024 www.dotnetpro.de
003300--003399__SSlliicciinngg__eeaa__ttiibb..iinndddd 3300 0011..0077..2244 1177::0044


---


<!-- Page 2 of 10 -->


PLANUNG Slicing
Ein anderer Bereich, der jedoch ebenfalls von der Anwen­ Korrektheit treibt die Zerlegung von Code. Und was treibt die
dung von „Teile und herrsche!“ profitiert, sind die Anforde­ Zerlegung von Anforderungen?
rungen. Was, wenn nicht sie, ist oft groß, komplex und un­ Ich denke, Anforderungen drehen sich um Wert. Software
überschaubar? Doch in was sollen große Anforderungen zer­ soll nützlich sein, das heißt dem Kunden helfen, seinen Ge­
legt werden? Die Zerlegung führt zu einer Einengung des winn zu vergrößern.
Scopes von Anforderungen. Scopes mögen unterschiedlich Das gesamte Softwaresystem, das zu entwickeln Sie beauf­
viele Featu res enthalten. Doch was genau sind Scopes und tragt sind, stellt den größten, den gesamten Wert für den Kun­
Features? Lassen sich diese ebenso formal definieren wie Mo­ den dar. Dafür ist er bereit, viel Geld zu bezahlen. Die kom­
dule, die Code in unterschiedlich weiten Horizonten zusam­ pletten Anforderungen beschreiben dieses Softwaresystem.
menfassen? Wenn sie umgesetzt sind, ist der komplette Wert realisiert.
Vielleicht ergibt sich eine Antwort, wenn ich zuerst eine an­ Leider, leider ist es nun in der Softwareentwicklung so, dass
dere Frage stelle: Warum überhaupt zerlegen? Irgendwie we­ die kompletten Anforderungen zu keinem Zeitpunkt wirklich
gen der Übersichtlichkeit und Klarheit. Doch lässt sich das komplett sind. Anforderungen sind erstens weitgehend un­
noch genauer fassen? klar und verändern sich auch noch durch den Kontakt mit
Was ist der Zweck von Modulen? Ich denke, es geht vor al­ Versionen des Softwaresystems („Der Appetit kommt beim
lem um … Korrektheit. Ja, wenn ich einen Begriff nennen Essen“).
sollte als Antrieb von Modularisierung, dann wäre es Korrekt­ Während Software oft horizontal in Module zerlegt wird, ist
heit. Und Korrektheit setzt Testbarkeit voraus; denn nur mit das bei Anforderungen weniger möglich. Bei Anforderungen
automatisierten Tests kann verlässlich und dokumentiert und geschieht die Zerlegung deshalb in Inkremente unterschied­
skalierbar festgestellt werden, ob Logik schon (Reife) und lichen Umfangs, die jeweils einen Teilwert des Gesamtwerts
noch (Stabilität) korrekt ist. darstellen. Dabei ist es jedoch unwesentlich, wie tief deren
Inkremente als Zerlegungshierarchie für Anforderungen (Bild 2)
Alles andere lässt sich daraus ableiten, zum Beispiel Wie­ Umsetzung in der Hierarchie der Funktionsaufrufe über Mo­
derverwendbarkeit oder Verständlichkeit oder Wandelbar­ dulgrenzen im Code geht.
keit. Ausgangspunkt und Voraussetzung ist stets Testbarkeit. Ein Inkrement ist ein Scope, von dem der Kunde oder ein
Korrekt kann nur sein, was getestet wurde. PO meint, dass die Umsetzung wieder einen kleinen oder grö­
Ausreichend getestet werden kann nur, was einen über­ ßeren Mehrwert darstellen würde. Ein breiteres Inkrement
schaubaren Umfang hat. Das ist die Grundlage für Ver­ wäre zum Beispiel die Zugriffsverwaltung für eine Software
ständlichkeit. von der Registrierung über das Anmelden und das Zurückset­
Wiederverwendet werden kann nur, was eine klar umrisse­ zen des Passworts bis zur Profilpflege. Darin wäre ein schma­
ne Funktion hat und eine klare Schnittstelle anbietet. Bei­ leres Inkrement die Anmeldung. Und darin wäre ein noch
des leistet Testbarkeit, die nur gegeben ist, wenn fokussier­ dünneres Inkrement die Beschränkung der Anmeldung auf
te Tests formuliert und an einem Modul auch einfach ange­ maximal drei Fehlversuche innerhalb von fünf Minuten.
setzt werden können. Wie für Module soll natürlich auch für Inkremente die re­
Auch Wandelbarkeit setzt klare Schnittstellen und über­ kursive Teilbarkeit gelten. Und zwar über möglichst viele
schaubaren Scope voraus. Beides fördert testbare Module. Zerlegungsebenen hinweg. Ist das mit den üblichen Re­ ▶
www.dotnetpro.de 8.2024 31
003300--003399__SSlliicciinngg__eeaa__ttiibb..iinndddd 3311 0011..0077..2244 1177::0044


---


<!-- Page 3 of 10 -->


PLANUNG Slicing
Die Slicing-Zerlegungs-
hierarchie für Anforde-
rungen (Bild 3)
präsentationen für Inkremente möglich? Welche Ebenen ste­ wortung ziehen, Testfälle zu formulieren. Das heißt, er muss
hen denn überhaupt zur Verfügung? nicht wirklich präzise beschreiben, was für ihn Korrektheit
User Stories bedeutet. Das erlaubt ihm, unklar zu bleiben.
Epics als Aggregate von User Stories Unklarheit jedoch führt zu Halluzinationen und Präsump­
User Story Maps als Aggregate von Epics tionen bei Ihnen. Wie generative KI auch schließen Sie Lü­
Use Cases sind eher orthogonal zur User­Story­Zerlegungs­ cken: manchmal durch Annahmen, manchmal durch Erfin­
hierarchie (Bild 2) dungen beziehungsweise Missverständnisse. Das führt min­
destens zu unerwarteten Iterationen, wenn nicht sogar zu
Sie sehen: Für Anforderungen sind die etablierten, greifba­ Konflikten.
ren Zerlegungsebenen sehr überschaubar. Große Anforde­ Dass dem PO nicht alles sofort klar sein kann, ist selbstver­
rungshorizonte lassen sich damit nur schwer inkrementell ständlich. Doch die Anforderungsanalyse sollte zumindest
zerlegen. herausarbeiten, wo Unklarheiten beziehungsweise Unb e­
Darüber hinaus haben Inkre­
mente allerdings keinen Bezug
zum Code. Wert ist nicht mit
Korrektheit – oder konkreter: mit
Testbarkeit – verbunden. Das
lässt unnötigen, gar gefährlichen
Interpretationsspielraum für Sie
als Entwickler und führt schnell
zu teuren Iterationen. Ganz da­
von zu schweigen, dass Sie mit
dem ganzen Anschluss von Wert
an Korrektheit allein dastehen.
Das macht User Stories und
Use Cases nicht überflüssig –
doch es begrenzt ihren Wert. Vor
allem halte ich sie nicht für die
Endpunkte einer Anforderungs­
analyse, von denen aus Sie in
Entwurf und Codierung starten
sollten. Das würde den PO zu
früh aus seiner Verantwortung
entlassen. Denn weil konkrete
Ansatzpunkte für Tests fehlen,
kann sich der PO aus der Verant­ Amazon als Beispiel für ein umfangreiches Softwaresystem (Bild 4)
32 8.2024 www.dotnetpro.de
003300--003399__SSlliicciinngg__eeaa__ttiibb..iinndddd 3322 0011..0077..2244 1177::0044


---


<!-- Page 4 of 10 -->


PLANUNG Slicing
stimmtheiten liegen. Dazu darf der PO keine Erwartungen Kann ich für eine App schon erkennen, welche Dialoge sie
haben, die nur enttäuscht werden können. Vielmehr muss für anbieten sollte? Ja! Dann kann ich die Ebene der Perspek­
sie „ein Plan“ her, der daraus bestehen kann, einen Anforde­ tiven überspringen.
rungsbereich zunächst auszuklammern oder nur einen Pro­
totyp zu bauen. Drei Ebenen der Slicing­Hierarchie habe ich bisher aller­
Ohne einen systematischen Ansatz, der zur Aufdeckung dings ausgelassen: zwei weiter oben und die unterste. Für
von Unklarheiten führt, können Sie allerdings nie sicher sein, den Anfang schien mir das dem Erklärungsfluss zuträglicher.
dass sie schon alle aufgedeckt sind. User Stories und Use Ca­ In vielen Fällen kommen Sie auch ohne diese Ebenen aus.
ses sind dafür zu weit weg vom Code. Doch nun will die Hierarchie vervollständigen. In diesem Ar­
Hier setzt nun Slicing an, das ich Ihnen in dieser Artikelse­ tikel stelle ich Ihnen Kontexte und Worker vor, im nächsten
rie vorstelle. Es bietet eine viel tiefere Zerlegungshierarchie zum Abschluss die Features.
und ist zudem auf jeder Ebene in softwaretechnischen Mit­
Kontexte
teln zur Umsetzung gegründet (Bild 3).
Bitte beachten Sie, dass sich im Slicing Anforderungen und Kontexte sind nur relevant für sehr umfangreiche Software­
Softwarestruktur berühren. Wert geht Hand in Hand mit Kor­ systeme mit vielen unterschiedlichen Benutzergruppen. Sie
rektheit. Slices – Teile der Anforderungen – haben Entspre­ sind leicht zu übersehen, weil das Kennzeichen für sie subtil
chungen bei Modulen – Teilen des Codes. sein kann. Sehen Sie sich als Beispiel die Ama­
Dadurch ist es möglich, den PO bei der zon­Homepage in Bild 4 an. Sie steht für
Analyse „eng zu führen“. Sie sitzen ein wirklich großes Softwaresys­
ihm mit einer Checkliste gegen­ tem; so groß, dass Sie es wohl
über, die garantiert, dass gar nicht als ein Software­
Anforderungen entweder system, sondern als Öko­
klar formuliert sind – system von Software­
oder nicht zur Umset­ systemen bezeichnen
zung in Produktions­ würden.
code kommen. Das Genau das ist aber
ultimative Kriterium mein Punkt: Oft füh­
dafür sind die Funk­ len sich große Soft­
tionen ab der Zerle­ ware systeme aus
gungsebene En try dem Stand nicht
Point: Solange diese monolithisch an.
weder formuliert Nur: Woraus beste­
sind noch Testfälle hen sie dann, was
dafür vom PO defi­ sind ihre Teile? Ist
niert sind, herrscht nach dem Überblick
keine Klarheit. Produk­ über das ganze System
tionscode sollten Sie nicht sofort ein Sprung auf die
anfassen, um solche unprä­ App­Ebene angezeigt? Ist
zisen Anforderungen umzuset­ die Homepage von Amazon
zen; sie müssen offensichtlich wei­ eine App und die Prime­Video­
ter geschärft werden. Dafür sind ande­ Stark vereinfachender Ausschnitt App für den Desktop eine andere?
re Wege als Iterationen über Produktions­ aus dem Überblick über das Ich denke, der Sprung wäre viel zu groß.
code zu suchen. Amazon-Softwaresystem (Bild 5) Nicht dass sich keine App erkennen ließe –
In den bisherigen Artikeln dieser Serie doch gibt es vielleicht noch weitere? Wenn
habe ich Ihnen vorgestellt, wie Sie Anfor­ Apps sich auf eine Rolle konzentrieren, um
derungen mit Slicing in mehreren Schnitten dünner und dün­ deren Benutzern ein bestmögliches Bedienerlebnis zu bieten,
ner schneiden, um dorthin zu kommen. Ausgangspunkt war lässt sich dann für das „Amazon­Softwareökosystem“ die
immer das gesamte zu realisierende Softwaresystem. Von Zahl der Apps einfach nach einem Überblick bestimmen
dort bin ich die Slicing­Hierarchie in mehr oder weniger gro­ (Bild 5)? Nein, das ist unmöglich. Mit dem Bild bekommen Sie
ßen Schritten hinuntergestiegen. Wie weit ich mich getraut bestimmt schon ein Gefühl dafür, wie verrückt es wäre, Apps
habe, in einem Schritt zu gehen, hing davon ab, wie gut ich erkennen zu wollen. Es braucht vorher mindestens eine grö­
mir schon die Teile vorstellen konnte, um die es auf der tie­ bere Zerlegung des Gesamtsystems. Das Bild kann nicht al­
feren Ebene geht. le Benutzerrollen und auch nicht alle Ressourcen listen.
Kann ich von der System­Ebene schon erkennen, welche Ein so großes System wird zum Glück nie an Sie zur Ent­
Entry Points es braucht? Nein? Dann kann ich noch nicht wicklung herangetragen. Es kann nicht mit einem Master­
dorthin springen, sondern muss zuerst gröbere Schnitte plan geschaffen werden, sondern ist Ergebnis einer jahrzehn­
machen. telangen Bottom­up­Entwicklung. Was heute als Ganzes ▶
www.dotnetpro.de 8.2024 33
003300--003399__SSlliicciinngg__eeaa__ttiibb..iinndddd 3333 0011..0077..2244 1177::0044


---


<!-- Page 5 of 10 -->


PLANUNG Slicing
(Systemlandschaft) vorliegt, ist zusammengewachsen. Es be­ Homonym bedeutet wörtlich „gleicher Name“.
stand schon aus Teilen, die später „nach oben hin“ zu einem Polysemie bedeutet wörtlich „mehrere Bedeutungen“.
Ganzen verbunden wurden. Lassen Sie uns trotzdem Ama­
zon als Beispiel nutzen, weil es so greifbar und vertraut ist. Lustig ist solche Mehrdeutigkeit in Sprachspielen. Was den­
Was also tun, um Anforderungen an ein (unbekannt) gro­ ken Sie, wenn Sie den Satz „der gefangene floh“ hören? (Da
ßes System (halbwegs) in den Griff zu bekommen? Im Slicing Sie ihn hier lesen und nicht hören, habe ich alle Worte be­
steht am Anfang die Zerlegung in Kontexte. Sie entsprechen wusst klein geschrieben.) Sie können entweder verstehen,
den Bounded Contexts des Domain Driven Design (DDD) [1] dass es um einen entflohenen Gefangenen handelt, oder um
[2] (Bild 6). einen Floh, der gefangen wurde.
Was ist der Treiber für Kontexte? Wie kann aus diffuser Un­ Nicht lustig ist es, wenn Mehrdeutigkeit unerkannt in An­
übersichtlichkeit etwas mehr Klarheit durch Teilung entste­ forderungen an Software vorhanden ist. Zwei Situationen
hen? Bei Apps war das Kriterium die Benutzerrolle. Jede Rol­ sind typisch für die Anforderungsanalyse, sobald mehrere
le, die ein Softwaresystem nutzt, gibt Anlass zu der Überle­ Benutzergruppen berücksichtigt werden müssen:
gung, ob es sich lohnt, für sie eine eigene App zu realisieren. Es werden unterschiedliche Worte gebraucht, die letztlich
Für Kontexte sind es ebenfalls Benutzerrollen, die motivie­ dasselbe bedeuten. Begriffe werden zunächst parallel ver­
ren – allerdings in Gruppen. Die Frage ist: Lassen sich Grup­ wendet, bis sich nach zahlreichen Konflikten und Missver­
pen von Rollen identifizieren, die zusammen eine „Sprach­ ständnissen herausstellt, dass eigentlich doch dasselbe ge­
gemeinschaft“ oder „Kultur“ darstellen? meint ist. Es liegt also weniger Trennung vor als zunächst
Ja, genau: Sprachgemeinschaft, das heißt eine Gemein­ gedacht.
schaft, in der dieselbe Sprache gesprochen
wird. Nicht eine natürliche Sprache wie
Deutsch oder Englisch, sondern eine Fachspra­
che mit Fachbegriffen. Fachsprachen sind cha­
rakteristisch für Wissensbereiche, deren Ex­
perten oft auch spezielle Verhaltensformen tei­
len (zum Beispiel Titel, Kleidung, Rituale);
DDD nennt diese Bereiche auch Domänen.
Wir als Softwareentwickler haben eine Fach­
sprache, die für Laien nicht verständlich ist.
Mediziner, Tischler, Juristen, Gebäudereiniger
haben ebenfalls Fachsprachen. Das ist Alltags­
wissen und bereitet kein Problem, solange die
Mitglieder dieser Fachsprachgemeinschaften
unter sich sind. Schwierig wird es, wenn solche Ein Eventhandler ruft
Gruppen sich gemeinschaftsübergreifend treffen. Die Ken­ einen Entry Point (Bild 6)
ner der einen Fachsprache sind Laien der anderen und um­
gekehrt. Wenn der Jurist zum Arzt geht, weiß er genauso we­
nig, was ein Komedonon ist, wie der Mediziner wohl nicht
weiß, was das Legalitätsprinzip im Strafrecht bedeutet. Umgekehrt kann hilfreiche, gar notwendige Trennung
Solche Zusammentreffen von Laien und Experten sind übersehen werden, wenn unterschiedliche Parteien diesel­
schwierig genug. Wirklich heikel wird es jedoch, wenn es ben Worte gebrauchen, aber doch letztlich Unterschiedli­
nicht offensichtlich ist, dass unterschiedliche Sprachen auf­ ches gemeint ist. Dann leidet die Anforderungsanalyse da­
einandertreffen. Hier einige Beispiele: runter, dass Polysemie vorliegt. Kennzeichnend sind dafür
Was bedeutet der Begriff Domäne? Weinkenner bezeich­ auch Konflikte und Missverständnisse. Perfider ist aller­
nen damit ein zusammenhängendes Areal von Weinber­ dings, dass eine „Harmonie“ gesehen wird, wo es Reibung
gen. Für DDDler ist es ein Wissens­ oder Fachbereich. Für geben sollte.
Programmierer, die mit SQL arbeiten, steht der Begriff für
den Bereich, dem die Werte in den Datensätzen einer Ta­ Als Beispiel mag der Begriff Produkt dienen. Ist Produkt das­
belle angehören. selbe für alle Benutzerrollen, die am Amazon­Softwaresys­
Was bedeutet der Begriff Konkurrenz? Ein Betriebswirt­ tem hängen (Bild 5)? Oberflächlich betrachtet ist ein Produkt
schaftler versteht darunter etwas anderes (Wettbewerb) als doch schlicht das, was verkauft werden soll, oder? Es hat a lso
ein Strafrechtler (Zusammenhang von Straftatbeständen). eine Bezeichnung, eine Beschreibung, einen Verkaufspreis –
Was bedeutet der Begriff Bank? Die einen denken dabei an so einfach sieht es zumindest der Kunde.
ein Geldinstitut, die anderen an ein Sitzmöbel. Die Lagerhaltung denkt darüber hinaus sicher noch zum
Beispiel an Produktnummer, Lagermenge, Mindestbestell­
Wenn Begriffe mehrere Bedeutungen haben, wird das Homo­ menge. Und der Einkauf interessiert sich außerdem zum Bei­
nymie oder Polysemie genannt: spiel für den Einkaufspreis und verkaufte Stückzahlen und
34 8.2024 www.dotnetpro.de
003300--003399__SSlliicciinngg__eeaa__ttiibb..iinndddd 3344 0011..0077..2244 1177::0044


---


<!-- Page 6 of 10 -->


PLANUNG Slicing
den Lieferanten. Das Management schließlich denkt eher in Bild 7 zeigt eine typische Situation: Die Softwareentwick­
Produktgruppen. lung gibt sich mit einer One­size­fits­all­„Überdomäne“ zu­
Das, was verschiedene Benutzerrollen mit einem Begriff frieden, die alle Rollen glücklich machen soll.
verbinden, kann gleich, ähnlich oder ganz verschieden sein. Für den Anfang als Überblick ist das vielleich noch hin­
Das ist das Problem, aus dem heraus DDD entstanden ist. nehmbar. Doch das sollte nicht das Ende der Zerlegung sein.
Denn DDD bedeutet, die Domäne, das heißt den Technisch gibt es (leider) auch Möglichkei­
Fachbereich, an den Anfang beziehungs­ ten, das Kunststück solchen Spagats zu
weise in die Mitte der Softwareent­ vollbringen, zum Beispiel Views oder
wicklung zu stellen. Alles dreht sich OLAP­Datenbanken, die automa­
um das Wissensgebiet mit seiner je tisch mit relationalen Daten­
eigenen Sprache, die Domänen­ banken synchronisiert werden.
sprache, die in der Domäne all­ Letztlich sind das jedoch Krü­
gegenwärtig ist. Allgegenwär­ cken. Es wird eine Quadratur
tig und ganz natürlich inner­ des Kreises versucht. Was ei­
halb der Gemeinschaft der Do­ gentlich nicht zusammenge­
mänenexperten, deshalb nennt hört, versucht man damit
DDD sie auch Ubiquitous Lan­ doch irgendwie zusammen­
guage. Aber außerhalb nicht passend zu machen. Das ist
bekannt oder nur selten und in aufwendig und teuer und er­
anschlussfähigen Ausschnitten zeugt Komplexität. Außerdem
genutzt. sind große, zentrale Datenmo­
Für DDD steht am Anfang der Soft­ delle wie ein Klotz am Bein, der
wareentwicklung die Identifikation der stetig wächst. Bei Änderungen müs­
in den Anforderungen eines Softwaresys­ sen Sie sehr, sehr vorsichtig sein, damit
tems versteckten Domänen mit ihren Spra­ Für viele Softwareprojekte nicht auch ja für keine Benutzerrolle (Stakehol­
chen. Jede beschreibt einen Kontext, in dem nur der Anfang, sondern auch das der) ein Nachteil entsteht. Das Ganze wird
sie gültig ist. Bounded Context nennt DDD Ende: eine riesige One-size-fits- immer steifer und fragiler.
ihn vielleicht in Anlehnung an Wittgensteins all-Domäne mit einem riesigen Dem sollen Kontexte abhelfen, die Spra­
Ausspruch: „Die Grenzen meiner Sprache Datenmodell (Bild 7) chen und damit domänenspezifischen
bedeuten die Grenzen meiner Welt.“ (Satz Code separieren. Jeder Kontext kann
5.6, Tractatus Logico­Philosophicus). dann getrennt als Subsystem betrachtet
Sprachen ziehen Grenzen. Sie inkludieren alle die, die sie werden, mit eigener Domäne und eigenen Ressourcen und
verstehen; sie exkludieren alle anderen. Deshalb beginnt In­ eigenen Datenmodellen. Bild 8 zeigt, wie ein solches „mehr­
tegration von Menschen damit, ihnen die Sprache der Ge­ sprachiges“ Gesamtsystem in Kontexte mit jeweils eigenen
meinschaft zu vermitteln, deren Teil sie werden wollen. Domänen zerlegt werden kann. ▶
Doch bei DDD und beim Slicing geht es um das Gegenteil!
Es soll eben nicht inkludiert werden, es soll kein Ganzes aus
Teilen geschmiedet werden! Vielmehr soll exkludiert, ge­ Ein großes System zerlegt in
trennt werden. Grenzen sollen ganz bewusst eingezogen kleinere Kontexte mit eigenen
werden. In den Anforderungen ist unbewusst schon viel zu Datenmodellen (Bild 8)
viel inkludiert, zu einer Masse „verrührt“ worden. Das gilt es
zu scheiden. Die unterschiedlichen, vermischten Sprachen in
den Gesprächen über Anforderungen sollen erkannt und se­
pariert werden. Und das nicht nur auf dem Papier, sondern
letztlich im Code.
Denn was passiert, wenn Sie ohne klare Domänenspra­
chentrennung anfangen zu codieren? Es entstehen große Da­
tenmodelle, Objektemodelle wie Datenbankmodelle. Die­
se Modelle müssen alles abdecken; um im Beispiel zu
bleiben: die Sichtweise und die Bedürfnisse von Kun­
den, Lagerhaltung, Einkauf und Management müs­
sen irgendwie erfüllt werden. Das bläht Datenmodel­
le ungeheuer auf. Womöglich widersprechen sich An­
sprüche sogar, zum Beispiel ein Zugriff auf Details für
Kunden und das Big Picture fürs Management. Hohe Nor­
malisierung wäre hilfreich für Ersteres, hohe Denormalisie­
rung für Letzteres.
www.dotnetpro.de 8.2024 35
003300--003399__SSlliicciinngg__eeaa__ttiibb..iinndddd 3355 0011..0077..2244 1177::0044


---


<!-- Page 7 of 10 -->


PLANUNG Slicing
Gleichzeitig gilt jedoch: „Kein Kontext ist
eine Insel.“ Kontexte existieren mehr oder we­
niger vernetzt. Schließlich bilden sie ja ein
Ganzes. Sie stehen also in Verbindung. Daten
des einen sind relevant für andere. Im Bild ste­
hen dafür die Ressourcen zwischen den Kon­
texten. Sie dienen dem Austausch von Daten.
Zum Beispiel könnte der Lebenszyklus eines
Produktes beim Einkauf beginnen. Von dort
fließen Produktdaten zur Lagerverwaltung.
Und schließlich fließen vom Einkauf und vom
Lager Daten zum Kundenkontext, damit das
Produkt auch gekauft werden kann. Deshalb
fließen auch Daten zurück vom Kundenkon­
text zur Lagerverwaltung, denn die ist für
Nachbestellungen oder gar die Auslieferung
zuständig.
Ein Kontext wird unterteilt in Apps (Bild 9) Und getrennt von all dem fließen Daten über
Produkte vom Einkauf und der Lagerverwal­
tung zum Managementkontext. Dort werden
Auffällig ist hier nicht nur, dass jeder Kontext eine kleine­ sie aggregiert für das Big Picture, das Manager sehen wollen.
re, fokussiertere Domäne abdeckt. Dazu gehört auch, dass je­ Kontexte sind Module oberhalb von Services. Ihre Kontrak­
der Kontext seine eigenen persistenten Datenmodelle hat: te sind nicht nur plattformneutral, sondern bestehen aus Res­
„Produkt“ gibt es in jedem Kontext in mehr oder weniger sourcen, zum Beispiel Datenbanken oder Warteschlangen.
ähnlicher Form und sogar mit womöglich gleichen Daten. Hinter diesen Kontrakten ist verborgen, wie Kontexte arbei­
Dem Prinzip DRY (Don’t Repeat Yourself) wird also wider­ ten. Es ist nicht zu erkennen, mit welcher Programmierspra­
sprochen. Und das ganz bewusst! Denn DRY hat nicht nur che sie implementiert sind, ob sie aus einem oder mehreren
Vorteile. Der entscheidende Nachteil von DRY ist die Inflexi­ Services bestehen oder wie sie ihre Daten halten.
bilität: Wenn es Inhalte und Strukturen nur einmal gibt, müs­ Die Kommunikation zwischen Kontexten ist asynchron.
sen alle Nutzer sich immer absprechen, wenn daran etwas Das bedeutet, es gibt keine sofortigen Veränderungen über
verändert werden soll. Ansonsten können Abhängigkeiten zu Kontextgrenzen hinweg. Es gibt keine ACID­Transaktionen,
einer Falle werden und Instabilität fördern. die ein Kontekt auf Ressourcen eines anderen ausführen
Die mehrfache Haltung von Daten in verschiedenen Daten­ könnte. (Ganz davon abgesehen, dass er sie ja nicht kennen
modellen hingegen entkoppelt und macht flexibel. Änderun­ kann.) Über verschiedene Kontexte hinweg gilt Eventual
gen im Lagerverwaltungskontext können durchaus vorge­ Consistency (EA) [3].
nommen werden, ohne sich mit anderen Kontexten abstim­ EA macht zunächst keine Freude. Irgendwie scheint sie im­
men zu müssen. Die Bildung von Kontexten entkoppelt. mer nur hinderlich und ganz unnatürlich. Doch das Gegen­
teil ist der Fall. EA
ist das Natürlichs­
te überhaupt. Nur
in der Softwareent­
wicklung wird immer
wieder versucht, diese
Natürlichkeit zu über­
winden – was zu mancher
Verrenkung führen kann.
Dennoch ist EA ein Preis, den
es zu zahlen gilt. Was Sie dafür
bekommen, ist Unabhängigkeit,
Flexibilität und Klarheit. Ich finde,
die sind es wert.
Doch das hängt selbstverständlich
von der Größe des Softwaresystems ab.
Ein monolithisches Soft- Nicht immer lohnt sich eine Aufteilung
waresystem (Bild 10) in Kontexte. Doch seien Sie sensibel für
die Möglichkeit. Horchen Sie genau hin,
wenn Stakeholder über Anforderungen spre­
36 8.2024 www.dotnetpro.de
003300--003399__SSlliicciinngg__eeaa__ttiibb..iinndddd 3366 0011..0077..2244 1177::0044


---


<!-- Page 8 of 10 -->


PLANUNG Slicing
chen. Trauen Sie Ihrem Gefühl, wenn Sie wiederholt etwas Das ist völlig okay, ja, sogar wünschenswert. Monolithische
nicht verstehen und Sie glauben, dass da irgendetwas mit den Apps zu entwickeln ist vergleichsweise einfach.
Begriffen nicht in Ordnung ist. Gehen Sie also an Anforde­ Haben Sie aber gemerkt, was ich gemacht habe? Ich habe
rungen immer mit dem Anspruch heran, die Domänenspra­ einen Begriff eingeführt, der für das Verständnis von Mono­
che herauszuarbeiten. Oder eben mehrere, falls diese sich in lithen nötig ist: den Betriebssystemprozess. Denn Monolith
den Anforderungsformulierungen verstecken sollten. bedeutet zunächst einmal, dass die gesamte Logik in nur ei­
Die Domänensprache, die Ubiquitous Language, ist ein nem Betriebssystemprozess gehostet wird (und darin auch
mächtiges Werkzeug für eine flüssige Verständigung mit al­ eigentlich nur in einem Thread). Dadurch kann die Kommu­
len Stakeholdern und auch innerhalb Ihres Entwicklungs­ nikation zwischen Codeteilen immer synchron sein, und prin­
Verschiedene
Arten verteilter
Softwaresysteme
(Bild 11)
teams. Am Anfang mag es umständlich klingen, auf präzise zipiell besteht von überall her Zugriff auf den gesamten Zu­
Begriffe zu bestehen, doch alsbald werden Sie es zu schätzen stand. Das führt schnell zu eng gekoppeltem Code, wenn
wissen, alles beim eindeutigen Namen nennen zu können. man sich nicht sehr bewusst mit guter Modularisierung dage­
Take away: Context is king. Nicht nur beim Umgang mit genstemmt.
generativer KI ist es wichtig, dass Sie den Kontext für einen Doch nicht alle Anforderungen lassen sich mit Logik in ei­
Chat zu Beginn richtig einstellen. Auch Ihre Projekte profitie­ nem Betriebssystemprozess erfüllen. Sicherheit, Skalierbar­
ren davon. keit, Robustheit oder auch Klarheit erfordern manchmal die
Verteilung von Logik auf mehrere Betriebssystemprozesse.
Worker
Das ist schon der Fall, wenn ein Softwaresystem auf zwei
Auf jeder Ebene der Slicing­Zerlegungshierarchie fragen Sie Kontexten besteht, denn in jedem gibt es mindestens eine
sich „Was ist das nächstkleinere Teil, in das ich die Elemen­ App mit mindestens einem Betriebssystemprozess. Doch
te dieser Ebene zerlegen kann?“ Und solange die Antwort auch in nur einem Kontext können es zwei Apps sein mit je
nicht Interaktion lautet, sind Sie noch weit vom Ziel entfernt. einem Betriebssystemprozess. Oder sogar in nur einem Kon­
So auch bei Kontexten. text mit einer App kann es zwei Betriebssystemprozesse ge­
Doch für Kontexte habe ich schon die nächste Zerlegungs­ ben, zum Beispiel Client und Server. Oder jede Ebene ist in
ebene vorgestellt: Es sind die Apps. Ein ganzes Softwaresys­ mehrere Teile der darunterliegenden Ebene zerlegt: mehre­
tem wird geteilt in Kontexte. Kontexte werden geteilt in Apps. re Kontexte, mehrere Apps, mehrere Betriebssystemprozesse
Und Apps werden geteilt in … Ja, was könnten hilfreiche klei­ (Bild 11).
nere Anforderungshorizonte sein? Leider ist der Begriff „Prozess“ schon sehr besetzt: Es gibt
Der Treiber für Kontexte sind unterschiedliche Domänen­ den technischen Prozess in Betriebssystemen, es gibt den Ge­
sprachen in den Anforderungen zum gesamten Softwaresys­ schäftsprozess, es gibt den industriellen Produktionsprozess,
tem. Der Treiber für Apps sind unterschiedliche Ansprüche es gibt den strafrechtlichen Prozess. Der Begriff ist in vielen
an die Bedienbarkeit und Verfügbarkeit für einzelne Rollen. Domänen zu Hause. Polysemie ist am Werk. Deshalb möchte
Zum Beispiel können innerhalb des Lagerverwaltungskon­ ich diese Ebene, die notwendig vorhanden ist, weil eine App
texts Lagerarbeiter andere Bedürfnisse haben als Disponen­ selbst verteilt sein können muss, anders nennen.
ten, und sie verdienen deshalb eigene Apps (Bild 9). Aus Sicht der Modularisation handelt es sich beim Betriebs­
Ist der nächste Schritt nun aber schon der zu Perspektiven, systemprozess um einen Service. Service wie in „serviceori­
wie im vorangegangenen Artikel [4] dargestellt? Nein, ich entierte Architektur“ oder „Microservice“. Module kapseln
denke, es kann noch ein Zwischenschritt hilfreich sein. Einer, Logik und gestatten den Zugriff über Schnittstellen.
der die Verteilung, die mit Kontexten eingesetzt hat, zu Ende Aus Sicht der technischen Verteilung handelt es sich tat­
denkt. sächlich um einen Prozess. Das ist einfach der bei Betriebs­
Auf der obersten Ebene, der Systemebene, sieht ein Soft­ systemen relevante Begriff. Der Prozess ist einer von mehre­
waresystem wie ein Monolith aus. Es ist ein Ganzes. Das kann ren Hosts, in denen Logik ablaufen kann
sich auch fortsetzen, wenn sein Umfang überschaubar ist und Aber was ist der Prozess, der Service aus Sicht der Anfor­
die Anforderungen sich rein mit Logik erfüllen lassen. Dann derungsanalyse? Ich nenne ihn Worker. Er ist ein Arbeiter im
besteht es aus einem Kontext mit einer App, und der gesam­ Rahmen einer Kooperation mehrerer, die zusammen „das
te Code läuft in nur einem Betriebssystemprozess (Bild 10). Team“ einer App bilden. ▶
www.dotnetpro.de 8.2024 37
003300--003399__SSlliicciinngg__eeaa__ttiibb..iinndddd 3377 0011..0077..2244 1177::0044


---


<!-- Page 9 of 10 -->


PLANUNG Slicing
Solange Apps nur aus einem Worker bestehen, müssen Sie so datennah viel schneller läuft. Dieselbe Performance wä­
darüber nicht großartig nachdenken. Apps stehen nicht in di­ re nicht zu realisieren, wenn die Daten zu Logik im Client
rektem Kontakt, selbst wenn sie zum selben Kontext gehören; transportiert werden müssten.
deshalb sind es ja Apps. Client und Application-Server und Datenbankserver (Bild 12):
Interessant werden Worker erst, wenn eine App in mehre­ Diese Verteilung liegt oft vor, wenn Sie eine Anwendung mit
re zerlegt werden sollte. Denn dann stehen diese Betriebssys­ einem HTML/CSS/JS­Client haben und einen MVC­Server
temprozesse in kooperativem Verhältnis. Sie brauchen einan­ und auch noch eine relationale Datenbank. Dann kann Lo­
der. Jetzt müssen Sie wirklich gut über die Kommunikation gik überall laufen. Und der MVC­Server hat mindestens die
zwischen ihnen nachdenken. Aufgabe, mit seiner Logik die Zugriffsdaten des Datenbank­
Verteilung von Logik auf Worker gerade innerhalb einer servers zu schützen, wenn nicht sogar zentral und daten­
App steigert die Komplexität enorm. Das Testen, das Deploy­ banknäher Domänenlogik auszuführen. Auch die moder­
ment, der Betrieb werden schwieriger. Und wofür? Was recht­ nen Server für Lambda­Funktionen gehören hierher.
fertigt diesen Preis? Darüber sollten Sie sich gut Gedanken Peer-to-Peer-Architektur: Hier sind die meisten Worker
machen. gleichberechtigt, um zum Beispiel Robustheit zu gewähr­
Inzwischen schwingt das Pendel in der Softwarearchitek­ leisten. Die Logik könnte auch in nur einem Worker laufen,
tur nicht umsonst auch wieder zurück: doch dann wäre sie anfällig für Störungen; die Gesamt­
Vor 40 Jahren waren Monolithen das einzige, was der dienstleistung wäre weniger verlässlich. Oder Peers kön­
Mainstream­Entwickler bauen konnte. nen gemeinsam an einer auf sie verteilten Aufgabe arbei­
Vor 30 Jahren wurde der Monolith langsam aufgebrochen ten; die Verteilung wäre dann nicht nur über Threads und
in Client und Server, zuerst im Unterneh­
mensnetzwerk, dann im Internet.
Vor 20 Jahren kamen serviceorientierte
Architekturen auf; es ging um eine wei­
tergehende Verteilung von Logik über
mehrere Server.
Vor 10 Jahren waren dann Microservices
en vogue; Docker­Container haben die­
sem Architekturstil einen Boost gegeben.
Seit einigen Jahren jedoch ist Ernüchte­
rung eingetreten. Selbst mit Docker und
Kubernetes ist der verteilte Betrieb von
Software immer noch um Größenordnun­
gen komplexer als der von monolithi­
scher Software. Der Modulith, der kom­
ponentenorientierte Monolith, gewinnt
an Akzeptanz.
Ich finde diese Entwicklung verständlich
und überfällig. Verteilung mag cool sein
und den ganzen Entwickler in Ihnen he­ Beispielhafte Zerlegung
rausfordern. Doch sie ist eben sehr teuer. einer App in Worker, um Logik
Das muss sich lohnen. zu verteilen. Jeder Worker ist wiederum ein „kleines“ Softwaresystem (Bild 12)
Und wann lohnt sich Verteilung? Aus­
schließlich dann, wenn eine nichtfunktio­
nale Anforderungen nicht mit Logik gelöst werden kann. Prozesse, sondern auch über Rechner hinweg möglich. Das
Oder genauer, wenn es um eine Verteilung auf Worker, also gäbe der Skalierbarkeit und Performance einen Schub.
verschiedene Betriebssystemprozesse geht: Wenn sich eine Cluster-Architektur: In einem Cluster sind auch Betriebssys­
nichtfunktionale Anforderung nicht mit Logik im selben Be­ temprozesse auf Augenhöhe vereinigt, doch sie arbeiten
triebssystemprozess umsetzen lässt. nicht gemeinsam an einem Problem. Vielmehr dienen sie
Wenn Sie auf eine App blicken, dann müssen Sie sich die­ der Lastverteilung bei einer wachsenden Zahl von Client­
se Frage stellen. Versuchen Sie, aus den Anforderungen nur Requests. Sehr vielen Clients werden deutlich weniger Ap­
an diese App herauszulesen, ob darin eine solche Anforde­ plication­Server im Cluster gegenübergestellt, die zum Bei­
rung versteckt ist. Wenn ja, dann und nur dann zerlegen Sie spiel wiederum auf ganz wenige Datenbankserver zugrei­
die App in mehrere Worker. Typische Verteilungen sind: fen. Auch das dient der Skalierbarkeit: Scale­out anstelle
Client-Server-Architektur: Im Client läuft Logik und im Ser­ von Scale­up. Es ist billiger und flexibler. Die funktionale
ver, oft einem Datenbankserver, läuft auch Logik nah an ei­ Verarbeitung der Daten bräuchte keine solche Verteilung,
ner Ressource. Warum ist die Logik dorthin verteilt? Weil sie doch die Last erfordert es womöglich.
38 8.2024 www.dotnetpro.de
003300--003399__SSlliicciinngg__eeaa__ttiibb..iinndddd 3388 0011..0077..2244 1177::0044


---


<!-- Page 10 of 10 -->


PLANUNG Slicing
Zusammenfassung
Drei Dimensionen des
Softwareuniversums Jetzt haben Sie alle Ebenen der Slicing­Hierarchie kennen­
(Bild 13) gelernt, um ohne große Sprünge vom Gesamtsystem bis zur
CQS­Funktion Anforderungen in immer feinere Scheiben zu
schneiden. Jedes Teil eines Ganzen stellt ein Inkrement dar,
das sich verfeinern und priorisieren lässt.
Auf den oberen Ebenen unterstützt die Zerlegung die Ar­
beitsteilung. Auf den unteren fördert sie die Testbarkeit.
Das Ganze von Anforderungen zu beherrschen durch Tei­
lung in kleinere und kleinere Scopes ist orthogonal zur Mo­
dularisierung und auch zur Komposition von Logik. Logik ist
immer mindestens in einem dreidimensionalen Raum verort­
bar, dessen Dimensionen Modul, Inkrement und Komposit
sind (Bild 13). Module umfassen: Klasse, Bibliothek, Kompo­
nente, Service; Komposite meinen: Funktionen als Operatio­
nen und Integrationen.
Ich nenne diesen Raum das Softwareuniversum, weil alle
Bestandteile von Code zur Entwicklungszeit und Laufzeit
Platz haben. Es gibt noch eine vierte Dimension, die der
Hosts, doch die habe ich hier der zeichnerischen Einfachheit
halber ausgelassen.
Wie Sie modularisieren oder „komponieren“, das heißt
Die Zerlegungsebene der Worker ist in der Slicing­Hierarchie Komposite finden, ist hinreichend an anderer Stelle beschrie­
etwas Besonderes. Alle Ebenen darüber und darunter stellen ben. Wie Sie aber technisch relevante Inkremente finden, die
Inkremente vor allem für funktionale Anforderungen dar. Ihnen einen Einstieg in Modularisierung und Komposition
Wenn eine Interaktion da ist, wird etwas berechnet; wenn bieten, das habe ich versucht, hier mit der Slicing­Hierarchie
eine App da ist, werden Daten verwaltet; wenn ein Kontext nachzuliefern. Sie ist mir jeden Tag ein treuer Helfer als
da ist, kann eine Gruppe von Rollen ihren Job machen. Checkliste und Handlauf. Mit den Zerlegungsebenen des Sli­
Das kann man von Workern nicht sagen. Wenn ein Worker cing fürchte ich keine Anforderungen mehr. Ich weiß, dass
fehlt, dann kann die ganze App ihren Dienst nicht versehen. ich sowohl ein 500­seitiges Anforderungsdokument wie auch
Die anderen Slices sind vertikal; sie stehen nebeneinander. eine User Story damit bewältigen kann.
Worker hingegen teilen ein App­Slice hingegen noch einmal User Stories oder Use Cases können mir dabei zur Hand ge­
horizontal. Mit ihnen geht es nicht darum, dass eine funktio­ hen. Doch letztlich will ich in Entwurf und Codierung nicht
nale Anforderung erfüllt wird oder nicht, sondern wie diese einsteigen, ohne wohldefinierte Entry Points in der Hand zu
erfüllt wird. Daten werden nicht nur gespeichert oder verar­ haben. Um allerdings zu denen zu kommen, brauche ich alle
beitet, sondern das geschieht auch noch sicher, skalierbar, darüberliegenden Ebenen der Slicing­Hierarchie. ◾
ausfallsicher und so weiter.
Worker­Slices sind sozusagen orthogonal zu den anderen [1] Martin Fowler, Bounded Context,
Slices. Slicing and dicing. Deshalb sehen auch Worker noch www.dotnetpro.de/SL2408Slicing1
so aus wie das ganze Softwareesystem am Anfang der Zerle­ [2] John Boldt, Domain Driven Design – The Bounded
gung (Bild 12): ein Kreis zur Demarkierung der (Prozess­) Context, www.dotnetpro.de/SL2408Slicing2
Grenze, ein Kern für den Teil der Domäne, der in dem Wor­ [3] Ralf Westphal, Eventual consistency for Mere Mortals,
ker implementiert wird, und eine Umwelt, zu der andere Wor­ www.dotnetpro.de/SL2408Slicing3
ker und Ressourcen oder User gehören. [4] Ralf Westphal, Die Benutzerschnittstelle treibt das
Diese Darstellung finde ich so einfach wie einleuchtend, Slicing, dotnetpro 7/2024, Seite 44 ff.,
simpel und nützlich, dass ich sie Softwarezelle nenne. Eine www.dotnetpro.de/A2407Slicing
biologische Zelle hat auch eine Membran (Grenze) und einen
Kern; sie steht auch mit der Umwelt im Austausch und trägt
einen Zustand in sich. Die Softwarezelle tut das auch. Porta­ Ralf Westphal
le und Provider sind Übergangsstellen für Daten zwischen ist Trainer, Berater und Mitgründer der Clean
Innenwelt und Außenwelt. Code Developer Initiative (https://clean-code-
Mit Softwarezellen lassen sich ganze Softwaresystem, ihre developer.de). Seine Schwerpunkte sind dauer-
Kontexte, deren App und die darin zusammenspielenden haft hohe Produktivität für die Softwareent-
Worker visualisieren. Softwarezellen erlauben also eine re­ wicklung und zukunftsfähige Teamorganisation.
kursive Zerlegung von Software. Worker sind dann allerdings https://ralfw.de
die letzte Ebene, die mit Softwarezellen beschrieben wird. In­
dnpCode A2408Slicing
nerhalb von Workern geht es anders weiter beim Entwurf.
www.dotnetpro.de 8.2024 39
003300--003399__SSlliicciinngg__eeaa__ttiibb..iinndddd 3399 0011..0077..2244 1177::0044