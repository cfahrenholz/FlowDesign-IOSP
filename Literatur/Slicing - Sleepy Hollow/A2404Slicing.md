<!-- Page 1 of 10 -->


PLANUNG Slicing
ANFORDERUNGSANALYSE FÜR ENTWICKLER, TEIL 1
Strukturiert zerlegen
Slicing bietet klar definierte, systematische Schritte durch Anforderungen von außen
nach innen, vom Groben zum Detail, vom breiten Scope zum dünn geschnittenen.
Die heute verfügbaren KI­Sprach­
modelle machen klar, dass die
Anforderungsanalyse in der Software­
entwicklung mehr Aufmerksamkeit
benötigt. Ohne bessere Anforderungs­
analyse kann das Potenzial der Sprach­
modelle einfach nicht gehoben wer­
den. Wenn Sie bisher noch kein Un­
wohlsein beim Umgang mit User Sto­
ries beschlichen hatte, sollten Sie es
spätestens jetzt fühlen.
Mein fester Glaube ist, dass die Soft­
wareentwicklung schon lange darun­
ter leidet, dass sie sich zu früh auf An­
forderungen einlässt. Ihre vorzeitige
Optimierung bestand und besteht in
vorzeitiger Entwicklung von Produk­
tionscode. Doch bisher haben Men­
schen das einfach mit Ad­hoc­Interak­
tionen kompensiert. War dafür nicht
die Co­Location im agilen Team Room
gedacht?
KI hingegen braucht mehr Klarheit. Selbst triviale
Eine KI als Entwickler zu prompten, Anforderungen
ohne selbst Anforderungen wirklich werden von der KI
verstanden zu haben, scheitert ansons­ falsch verstanden
ten. Wer etwas von der KI will, be­ (Bild 1)
kommt beim Prompten den Stand des
eigenen Verständnisses gespiegelt.
Dies mag das triviale Beispiel aus
Bild 1 verdeutlichen: Ich prompte ChatGPT, bekomme lauffä­ der eine Lücke in meinen Anforderungen gefunden und
higen Code – und bin nicht zufrieden. Der Grund: Die KI hat durch eigene Entscheidung ausgefüllt: Ich hatte mir keine
einfach meine Anforderungen missverstanden. Gedanken darüber gemacht, was passieren soll, wenn kein
Was war das Problem? Ich war nicht präzise genug. Die Be­ Name als Parameter angegeben wird. Doch die KI fühlte sich
grüßung Hallo, <Name>! ist okay. Doch die Art, wie der Benut­ unfähig, diesen Fall zu übergehen.
zer dem Programm seinen Namen mitgeben soll, entspricht Als Entwickler haben Sie gelernt, dem Kunden oder dem
nicht meinen Vorstellungen. Ich hatte mir ausgemalt, dass der Product Owner (PO) viele Fragen zu stellen. Ihnen wäre so
Name gleich auf der Kommandozeile angegeben wird. etwas wie hier nicht passiert. Doch dieses Beispiel ist ja auch
Aber so ist das eben: Was ich als Kunde im Kopf habe und trivial. Bei größeren, realen, komplexeren Anforderungen
nicht explizit ausdrücke, wird vom Entwickler – hier: ChatGPT tappt man dann aber doch leicht in dieselbe Falle wie Chat­
– interpretiert. Die KI hat eine plausible Annahme getroffen. GPT: Man macht Annahmen – und weiß es womöglich nicht
Ich hätte mir nicht nur über meine Vorstellung klar sein, einmal. Unknown assumptions.
sondern diese auch noch ganz genau ausdrücken müssen. Im User Stories sollen „nur“ Anlass für Diskussionen sein.
nächsten Anlauf, gezeigt in Bild 2, habe ich nachgebessert. Klar, was denn auch sonst. Auf einen Post­it­Zettel passt nicht
Nun ist das Verhalten des Programms so, wie ich es mir ge­ mehr als eine Anregung oder Erinnerung. Präzise Anforde­
dacht hatte. Endlich. Oder jedenfalls fast, denn die KI hat wie­ rungen sind viel, viel detailreicher. Doch wie sehen die aus?
42 4.2024 www.dotnetpro.de
004422--005511__SSlliicciinngg__eeaa__ffss..iinndddd 4422 0044..0033..2244 1155::5522


| Selbst triviale
Anforderungen
werden von der KI
falsch verstanden
(Bild 1) |  |
| --- | --- |



---


<!-- Page 2 of 10 -->


PLANUNG Slicing
Was sollte das persönliche Zielbild für Anforderungen sein? es nicht egal sein, was Sie nach einem Anforderungsge­
Wie kommt man da hin? spräch mit dem PO in den Händen halten. Und dem PO kann
Meine Vorstellung von der Anforderungsanalyse ist, dass es eigentlich auch nicht egal sein, denn er möchte ja, dass Sie
Entwickler den PO „ziehen“. Sie sitzen nicht brav da und hö­ möglichst zügig seine Wünsche erfüllen.
ren sich an, was der PO blumig beschreibt. Nein, sie haben
Verständnis ist gut, Korrektheit ist besser
ein klares Bild davon, was das Ergebnis einer Anforderungs­
analyse ist. Sie haben eine Vorstellung von der Form klarer Wann hat man Anforderungen verstanden? Wie weiß der PO,
Anforderungen. Sie legen den PO deshalb „auf den Grill“, dass man Anforderungen verstanden hat?
bis ihr Ziel erreicht ist. Die Antwort ist leider nicht: „Wenn ich dem PO erklären
kann, was er haben will.“ Erklärungen sind schwach. Der PO
will keine schönen Worte, sondern Taten. Worte, selbst wenn
sie ihm plausibel erscheinen, sind mehrdeutig und lücken­
haft. Seine wie Ihre. Anforderungen umzusetzen ist schlim­
mer, als „Stille Post“ zu spielen: Schon der Organisation ist
letztlich unklar, wie Software ihr helfen kann und was sie sich
also wünschen soll. Dem PO ist unklar, was die Organisation
darüber weiß, was ihr helfen kann. Was der PO von seinem
Verständnis ausdrückt, ist missverständlich, lückenhaft, gar
fehlerhaft. Was Sie von dem, was der PO sagt, verstehen, ist
unvollständig und fehlerhaft. Was Sie mit Ihrem Verständnis
umsetzen, ist unvollständig und fehlerhaft.
Erst wenn Ihre Umsetzung am Ende den PO oder die Or­
ganisation erreicht, entsteht dort Klarheit, ob man schon ge­
wusst hatte, was der Bedarf war, und ob Ihr Code ihn nun
deckt. Und wenn es schlecht läuft, hat der
Bedarf sich seit dem initialen Wunsch so­
Präzisere Anfor- gar verschoben.
derungen führen Das war und ist die Realität. Auch des­
zu einem besseren halb empfiehlt die Agilität, inkrementell
Ergebnis (Bild 2) vorzugehen und den Anforderungsball
flach zu halten mit „Anlässen für Gesprä­
che“. Sie setzt darauf, dass in Dialogen
eher Missverständnisse, Lücken und
Fehler aufgedeckt werden. Und sie setzt
auf kleinere, schmalere Anforderungen,
die Schritt für Schritt umgesetzt werden,
um bei Missweisungen keine zu großen
Nachbesserungen machen zu müssen.
Trotz solchen inkrementellen Vorge­
hens kommt allerdings auch die Agilität
nicht um Iterationen herum. Selbst inner­
Um dieses Zielbild geht es mir in dem Ansatz, den ich Sli­ halb eines Inkrements werden Sie es schwer haben, in einem
cing nenne. In dem durchläuft die Anforderungsanalyse eine Durchgang von der Anforderung zu „perfektem“ Code zu
schrittweise Verfeinerung, die auf einen Punkt zuläuft. Die­ kommen. Selbst in Bezug auf gegebene Anforderungen wer­
ser ist der Endpunkt der Analyse und der Startpunkt des den Sie Nachbesserungsrunden durchlaufen.
Entwurfs. Slicing definiert für den Endpunkt eine Form; im Das ist grundsätzlich nicht zu vermeiden, denke ich. Auch
Analyseprozess wird diese Form mit Inhalt aus der Domäne eine bessere Anforderungsanalyse schafft Iterationen nicht
gefüllt, um die es dem PO geht. ab. Doch Iterationen sind kein Selbstzweck. Weniger ist bes­
Die Verfeinerungen des Slicing sind kompatibel mit dem ser. Auch leichtgewichtiger ist besser.
agilen inkrementellen Vorgehen. Allerdings binden sie bei Wie können Sie da hinkommen? Alles beginnt damit, zu
jedem Schritt den Schnitt durch die Anforderungen an Code verstehen, was Verständnis ist beziehungsweise wie sich
an. Auf diese Weise wird die Anforderungsanalyse für Sie als Verständnis „nachweisen“ lässt.
Entwickler ein Handlauf zum Code. Sehen Sie sich die Anforderungen in Bild 3 an: Ich habe
Sie als Entwickler brauchen einen eigenen Blick auf An­ ChatGPT gebeten, Code zur Generierung von Zahlenfolgen zu
forderungen. User Stories sind nicht genug. Ihr Verständnis schreib en. Diese Zahlenfolgen habe ich durch Beispiele be­
soll sich in einer Weise entwickeln, dass Ihnen der anschlie­ schrieben. ChatGPT hat mich verstanden. Woran erkenne ich
ßende Entwurf und die Codierung leichter fallen. Ihnen kann das? Erkenne ich das Verständnis bei ChatGPT an dessen ▶
www.dotnetpro.de 4.2024 43
004422--005511__SSlliicciinngg__eeaa__ffss..iinndddd 4433 0044..0033..2244 1155::5522


|  | sie ihm plausibe
haft. Seine wie I
mer, als „Stille P
letztlich unklar,
also wünschen s
darüber weiß, w
Verständnis aus
fehlerhaft. Was S
unvollständig un
umsetzen, ist un
Erst wenn Ihr
ganisation erreic
wusst hatte, was
Präzisere Anfor-
derungen führen
zu einem besseren
Ergebnis (Bild 2) |
| --- | --- |



---


<!-- Page 3 of 10 -->


PLANUNG Slicing
Anforderungen für einfache
Zahlenfolgen werden von
ChatGPT korrekt verstanden
(Bild 3)
Erläuterungen, zum Beispiel „Die Zahlen­
reihe, die du beschreibst, folgt der Fibo­
nacci­Sequenz, bei der jede Zahl die Sum­
me der beiden vorhergehenden Zahlen ist,
mit den Startwerten 1 und 1“? Das liegt
nahe. Ich habe die Fibonacci­Sequenz im
Kopf gehabt, und ChatGPT sagt, es habe
aus den Beispielen herausgelesen, dass es
sich um die Fibonacci­Zahlen handelt.
Treffer!
Doch für mich ist nicht das wirklich
Ausdruck von Verständnis. Oder selbst
wenn, ist es recht unerheblich, denn in
der obigen Kaskade der Anforderungs­
analyse gibt es immer noch Schritt 5: die
Umsetzung. Bei der Umsetzung kann
auch das beste Verständnis noch stolpern.
Deutlicher wird das Verständnisprüfungsproblem in Bild 4. das aber nur auf, weil es sich wieder um ein sehr einfaches
Eigentlich schlägt sich die KI ganz gut. Sie erkennt sofort, Beispiel handelt. Wäre es komplizierter, könnte ich bei der Er­
dass es sich um zwei Generierungsregeln handelt, die ab­ läuterung etwas übersehen oder hineininterpretieren.
wechselnd zum Einsatz kommen. Damit haben so manche Nein, die Erklärungen von ChatGPT sollten mir egal sein.
Menschen ein Problem. Doch sollte ich damit zufrieden sein Das, was zählt, ist … der Code. „Im Code steckt die Wahr­
und glauben, dass ChatGPT wirklich verstanden hat? heit“, also lasse ich mir für den Code Testfälle aus meinen Bei­
Ich könnte jetzt genauer auf die Erläuterungen der KI spielen generieren (Bild 5). Wenn ich die laufen lasse, zeigt
schauen, um mir einen Eindruck von ihrem Verständnis zu sich ganz unmissverständlich: Irgendetwas ist faul.
verschaffen. Dabei würde mir auffallen, dass sie die zweite ChatGPT hatte nicht verstanden oder sein Verständnis
Regel nicht wirklich korrekt erkannt hat. Letztlich fällt mir nicht zu hundert Prozent im Code abgebildet. Wo das Pro­
44 4.2024 www.dotnetpro.de
004422--005511__SSlliicciinngg__eeaa__ffss..iinndddd 4444 0044..0033..2244 1155::5522


---


<!-- Page 4 of 10 -->


PLANUNG Slicing
blem liegt, kann mir zunächst jedoch egal sein. Um festzustel­ Die Agilität hat im Grunde auch den Wert der Korrektheit
len, dass es eine Lücke zwischen Wunsch und Wirklichkeit als Beweis des Verständnisses erkannt und deshalb auf kur­
der Umsetzung gibt, muss ich nicht ChatGPT befragen, son­ ze Iterationszyklen gesetzt. Da sind zum einen die Sprints, die
dern den Code. nach zwei Wochen oder sogar einer Woche Feedback liefern
Den weiteren Dialog mit ChatGPT bis zum korrekten Code sollen. Zum anderen gibt es automatisierte Tests, die schon
skizziert Bild 6. Es brauchte noch ein paar Anläufe, um die KI vorher die Reife einer Umsetzung beurteilen sollen.
erkennen zu lassen, wie die Regel für die Zahlen mit gera­ Das geht in die richtige Richtung – allerdings bleibt eine
dem Index lautet. Bei keiner der Iterationen habe ich mich al­ Lücke in der agilen Anforderungsanalyse. Was ist denn das
lerdings auf die Erklärungen der KI verlassen. Immer habe Ziel, wann kann sie als abgeschlossen betrachtet werden?
ich die neue Funktion sofort gegen die Tests laufen lassen.
Testbarkeit für Korrektheit
In dieser Nussschale mit mir als Kunde und der KI als Ent­
wickler zeigt sich für mich, was relevantes Verständnis der Wenn sich ein wie immer geartetes Verständnis in der mehr
Anforderungen bedeutet: zufriedenstellendes Verhalten von oder weniger hohen Korrektheit von Code ausdrückt, dann
Code. Ich fühle mich sogar versucht zu sagen: Verständnis ist kann das Ziel der Anforderungsanalyse nur sein, die Korrekt­
sekundär. Verständnis allein hat keine Bedeutung. Verständ­ heit auch leicht überprüfbar zu machen. ▶
nis ist nur ein Mittel, um Code herzustellen,
der tut, was der Kunde von ihm erwartet.
Gerade wenn eine künstliche Intelligenz
den Code generiert, liegt ja auch die philoso­
phische Frage nahe: Kann eine KI überhaupt
verstehen? Kann sie verstehen, wie wir mei­
nen, dass Menschen verstehen?
Eine spannende Frage, finde ich. Lassen Sie
uns darüber bei einem Bier plaudern. Für die
Softwareentwicklung hingegen ist sie unbe­
deutend. Augenscheinlich kann KI codieren.
Augenscheinlich kann sie Code schreiben,
der unsere Formulierungen von Anforderun­
gen mehr oder weniger erfüllt. Welches „Ver­
ständnis“ die KI von diesen Anforderungen
hat, ist unerheblich, solange sie korrekten
Code liefert. Die Korrektheit von Code allein
ist der Lackmustest für die Umsetzung dessen,
was ein PO an Wünschen geäußert hat.
Warum musste ich aber so viele Schleifen
drehen, bevor die KI endlich die dritte Zahlen­
reihe korrekt erzeugen konnte (Bild 6)? Weil
ich wieder sparsam war mit meinen Formulie­
rungen. Ich habe für mich Offensichtliches
nicht gesagt, sondern auf Intelligenz gesetzt,
die schon verstehen wird, was ich meine. Hier
künstliche Intelligenz, in anderen Fällen baut
ein PO auf Ihre natürliche Intelligenz.
Mit etwas mehr Mühe bei der Anforde­
rungsformulierung hätte es auch sofort ge­
klappt, siehe Bild 7. Und noch immer nicht ha­
be ich der KI die Regel für die Zahlenfolge mit­
geteilt. Ob sie die aus den Beispielen ableiten
konnte, zeigt allein die Überprüfung des
Codes durch Tests.
Was tun, wenn der Code fehlschlägt, wie
zum Beispiel in Bild 5 zu sehen? Dann zeigt der
Fehlerort an, welcher Teil der Anforderungen
(!) nachzubessern ist. Hätte ich mich weniger
dumm angestellt, hätte ich schon den zweiten
Prompt auf die Zahlen mit geradem Index
konzentriert. Anforderungen für kompliziertere Zahlenfolgen werden nicht verstanden (Bild 4)
www.dotnetpro.de 4.2024 45
004422--005511__SSlliicciinngg__eeaa__ffss..iinndddd 4455 0044..0033..2244 1155::5522


---


<!-- Page 5 of 10 -->


PLANUNG Slicing
Schon die Anforderungsanaly­
se läuft also auf Testbarkeit hi­
naus. Ihr Verständnis ist sekun­
där, die Testbarkeit Ihres Codes
ist primär. Wenn er testbar ist,
muss der PO Sie nicht fragen:
„Haben Sie das verstanden?“,
sondern er lässt einfach Tests für
die Qualität Ihres Codes spre­
chen. Mein Dialog oben mit der
KI zeigt das beispielhaft.
Was aber braucht es für Test­
barkeit? Ansatzpunkte. Ihr Code Testfälle für die
muss von vornherein Ansatz­ Implementation
punkte für automatisierte Tests der dritten Zahlen-
haben, die dem PO Auskunft reihe (Bild 5)
über seine Reife geben (also den
Grad der schon erreichten Kor­
rektheit, die Anforderungskon­
formität).
Solche Ansatzpunkte sind …
Funktionen.
Im obigen Fall der Zahlenrei­
hengenerierung war die Funk­
tion f() der natürliche Ansatz­
punkt. Als Kunde hatte ich mir
schon eine Funktion gewünscht.
Doch das ist nicht der Normalfall.
Sie können von einem PO nicht
erwarten, dass er Ihnen sagt:
„Schreiben Sie eine Funktion f(),
die dieses und jenes tut.“
Diese Präzision ist jedoch nötig,
damit man Testbarkeit bekommt.
Besonders deutlich wird das, sobald Sie eine KI für die Code­
generierung zu Hilfe nehmen. Wie wollen Sie sonst ihr Elabo­
rat überprüfen? Sie sind ihr gegenüber der Kunde, der auf ei­
nen Blick sehen will, ob sein Wunsch schon erfüllt ist. gnatur alle Details verborgen – die Beschaffung des Namens
Das wird mittelfristig auch so bleiben, denke ich. Nicht der wie die Ausgabe der Begrüßung –, doch genau daraus ergibt
PO wird schon morgen einer KI sagen, welche Software sie sich schlechte Testbarkeit. Seiteneffekte wie Zugriff auf die
„ausspucken“ soll. Nein, Sie werden als Mittelsmann zwi­ Konsole lassen sich schwer automatisiert überprüfen.
schen PO und KI stehen. Sie werden derjenige sein, der frem­ Spüren Sie, wie die Testbarkeit an der Analyse „zieht“? Als
dem Code vertrauen muss. Bisher war das der PO; er konnte Erstes kommen Sie darauf, den Scope der Funktion zu veren­
sich nur Ihrer technischen Expertise als Entwickler anheim­ gen: string begrüßungFormulieren(string name). In der Funk­
geben. Nun ist es an Ihnen, jemand anderem zu vertrauen: tion steckt immer noch testwürdige Logik, doch es wurde ei­
der KI. Fragen Sie sich selbst: Was brauchen Sie dafür? nige Logik „herausgepresst“. Die kann in zwei weitere Funk­
Die Antwort: Funktionen, die automatisiert getestet wer­ tionen verpackt werden:
den können.
Solche Funktionen aus Anforderungen abzuleiten, das ist string nameBeschaffen()
für mich der Zweck von Slicing (vergleiche Bild 8). begrüßen(string begrüßung)
Wie hätte das bei der ersten Aufgabe ausgesehen? Dort hat
nur ein Programmlauf, also ein manueller Test, die Inkorrektheit Diese beiden Funktionen enthalten weiterhin die Seitenef­
aufdecken können. Wie anders hätte der Prompt, also die An­ fekte und lassen sich schwer testen. Viel wichtiger ist jedoch
forderungsformulierung ausgesehen, wäre das Ideal schon eine zunächst, dass die Frage explizit im Raum steht: Woher
Funktion gewesen, für die Code hätte erzeugt werden sollen? kommt der Name und wohin geht die Begrüßung?
Wäre eine Funktion begrüßen() passend gewesen? Nein, Solange der Name von der Konsole eingelesen werden
denn wie soll sie getestet werden? Zwar sind hinter ihrer Si­ soll, ist nameBeschaffen() besonders widerspenstig beim ▶
46 4.2024 www.dotnetpro.de
004422--005511__SSlliicciinngg__eeaa__ffss..iinndddd 4466 0044..0033..2244 1155::5522


---


<!-- Page 6 of 10 -->


PLANUNG Slicing
Es braucht mehrere
Anläufe, um die KI die
korrekte Bildungsregel
für die Zahlenreihe
„verstehen“ zu lassen
(Bild 6)
www.dotnetpro.de 4.2024 47
004422--005511__SSlliicciinngg__eeaa__ffss..iinndddd 4477 0044..0033..2244 1155::5522


|  |  |
| --- | --- |



---


<!-- Page 7 of 10 -->


PLANUNG Slicing
Präzisere Anfor-
derungen führen
aus dem Stand zu
einem besseren
Ergebnis (Bild 7)
48 4.2024 www.dotnetpro.de
004422--005511__SSlliicciinngg__eeaa__ffss..iinndddd 4488 0044..0033..2244 1155::5522


---


<!-- Page 8 of 10 -->


PLANUNG Slicing
Testen. Das triggert bei Ihnen hoffentlich die Frage: Muss der gen in Testfällen formalisiert wurden. Rein natürlichsprach­
Name wirklich von der Konsole eingelesen werden? Hat der liche Anforderungen sind nicht genug!
PO das so formuliert? Was wäre einfacher zu testen? Im ersten Beispiel waren die Anforderungen nur natürlich­
Eine gut testbare Funktion als Ziel der Anforderungsana­ sprachlich. Das schlechte Ergebnis war also kein Wunder. Im
lyse führt somit … ins Gespräch – und zwar in ein sehr kon­ zweiten Beispiel waren sie natürlichsprachlich und formal
kretes, zielgerichtetes. Ihr Ideal Testbarkeit lässt Sie am PO präzise, wenn auch nicht codiert. Die Beispiele waren für
„ziehen“. Sie können die Analyse geführt durch ein Struk­ ChatGPT genug, um daraus erstens Produktionscode abzu­
turelement des Codes mit Fragen vorantreiben: „Verstehe ich leiten und zweitens Tests zu formulieren.
das richtig, dass das Programm nach dem Namen fragen „Erklären ist gut, Tests sind besser“, könnte ich frei nach
soll?“, „Die Umsetzung ginge schneller und wäre besser zu Lenin formulieren. Ja, erklären Sie dem PO gern, was Sie
überprüfen, wenn der Name von der Kommandozeile gele­ nach seiner Präsentation der Anforderungen verstanden ha­
sen würde. Wäre das nicht auch eine Option? Das ließe sich ben. Damit reflektieren Sie aktiv und vertiefen Ihr Verständ­
einfacher umsetzen und testen“, und so weiter. nis. Gleichzeitig hat der PO eine Chance, darin Lücken, Miss­
Wie ein Trüffelschwein sollten Sie also während der Anfor­ verständnisse, Fehler zu erkennen – und auch er wird da­
derungsanalyse auf der Suche nach testbaren Funktionen durch angeregt, über seine Vorstellung nochmals zu reflek­
sein. Sie stecken überall in den User Stories (oder wie auch tieren. Super!
immer Ihnen Anforderungen präsentiert werden). Mal ist es Doch Sie beide sollten eine solche Erklärung nicht überbe­
eine Funktion für ein Post­it, mal mehrere. werten. Sie ist nicht mehr als vorläufig und ein Surrogat. Sie
In jedem Fall halte ich die Anforderungsanalyse für unvoll­ ist nicht das Real Thing. Denn das ist nur korrekter Produk­
endet, solange nicht klar ist, welche Funktionen hinter den tionscode.
Wünschen stecken: Sich in Analysedialogen zu drehen hat das primäre Ziel,
Welche Funktionen werden gebraucht? Klarheit in Form von Testbarkeit herzustellen. Es geht um das
Wie sieht ihre Signatur aus? Tupel (Funktionssignatur, Testfälle).
Slicing leitet aus Anforderungen testbare Funktionen ab (Bild 8)
Gibt es Seiteneffekte? Wenn ja, wie können die „herausge­ Was darüber hinaus vermittelt wird, steht unter hohem Ri­
drückt“ werden, um die Testbarkeit zu erhöhen? siko, unknown Unknowns auszulassen. Darauf müssen alle
Und schließlich: Welche Tests werden für eine belastbare Seiten vorbereitet sein.
Aussage über die Korrektheit gebraucht? Und was ist es, das es mehr braucht als (Funktionssignatur,
Testfälle)? Die Beschreibung einer „Kausalkette“ (Bild 9): Wie
Indem Ihr Sinnen und Trachten während der Analyse auf führt der Input für die Funktion zusammen mit Zustand, auf
Funktionen als Test­Ansatzpunkte ausgerichtet ist, führen im den sie zugreifen kann, zu Output und neuem Zustand?
Grunde Sie den PO. Nicht er sagt an und Sie folgen, sondern Diese „Kausalkette“ jedoch ist oft nicht klar. Oder anders
Sie haben einen (unausgesprochenen) Anspruch, den er er­ gesagt: Sie zu erarbeiten ist geradezu Ihre Aufgabe als Ent­
füllen soll. wickler. Deshalb ist es umso wichtiger, zumindest eine Vor­
Ihr Anspruch ist sogar doppelt, wenn Sie den PO nicht ge­ stellung von Testfällen zu haben. Der PO kann nicht sagen:
hen lassen, ohne klare Testfälle mit ihm abgesprochen zu ha­ „Hier ist eine ‚Kausalkette‘, aber ich habe keine Ahnung,
ben. Die Entwicklung des Codes hinter der Fassade der An­ wie Testfälle dafür aussehen.“ Wenn er ein Verständnis von
satzpunkte sollte nicht beginnen, ohne dass die Anforderun­ der „Kausalkette“ hat, muss er auch verstehen, wie ihre ▶
www.dotnetpro.de 4.2024 49
004422--005511__SSlliicciinngg__eeaa__ffss..iinndddd 4499 0044..0033..2244 1155::5522


---


<!-- Page 9 of 10 -->


PLANUNG Slicing
Wirkung ist. Allerdings kann er sagen „Hier sind Testfälle. So Protypen können alle möglichen Formen haben; sie müs­
sehen Ergebnisse für gewisse Eingaben aus. Aber ich habe sen nicht codiert sein. Für Benutzerschnittstellen könnten Sie
keine Ahnung, wie dazu die ‚Kausalkette‘ aussieht.“ zum Beispiel auch Papier benutzen.
Üblicherweise konzentriert sich die Anforderungsdiskus­ Prototypen simulieren Systemverhalten. Produktionscode
sion auf die „Kausalkette“, hinter der ein bestimmtes zu lö­ wird für sie nicht geschrieben oder verändert. Deshalb simu­
sendes Problem steht. Ich denke jedoch, dass sich die Diskus­ lieren sie nur. Sie sind nicht das Produktionssystem, sondern
sion hin zu Funktionen und Testfällen verschieben sollte. tun nur so. Sie vermitteln eine für die auszumerzende Unklar­
heit relevante Anmutung, wie das Produktionssystem ausse­
Prototypen gegen Unklarheit
hen beziehungsweise sich verhalten könnte.
Weniger Klarheit finde ich nicht akzeptabel für Sie als Ent­ Für das erste Beispiel könnten Sie zum Beispiel zwei Pro­
wickler. Der PO soll liefern, wenn er etwas haben will. Er soll totypen mit einem Shell­Skript schreiben (Bild 10). Das ist in
sich auf den Hosenboden setzen und sich selbst erst mal klar diesem trivialen Beispiel nicht viel weniger Aufwand als der
darüber sein, was er will. Das beweist er, wenn er fähig ist, C#­Code. Doch die andere Form vermittelt Ihnen hoffentlich
Testfälle zu formulieren. Sie helfen ihm gern, diese Testfälle schon ein Gefühl dafür, was ich damit meine, wenn ich sage,
zu formalisieren und Funktionen zu finden, auf die sie ange­ Prototypen seien kein Produktionscode.
setzt werden können. Anders ist die „Reifeprüfung“ (und Sie bestehen nur aus dem Allernötigsten, um den PO in die
auch die Stabilitätskontrolle) von Produktionscode nicht ska­ Lage zu versetzen, eine Entscheidung zu treffen, die ihn for­
lierbar möglich. maler Klarheit näher bringt, die sich für Sie in Funktionssig­
Aber was, wenn die Anforderungen sich einfach noch nicht naturen und Testfällen ausdrückt.
so klar formulieren lassen? Was, wenn sich Ihnen noch keine Solange Ihre Ansprüche an die Testbarkeit von Umsetzun­
Funktion anbietet, hinter deren Signatur die Anforderungen gen der Anforderungen nicht erfüllt sind, lassen Sie besser
implementiert werden könnten, um durch sie mit automati­ die Hände von Produktionscode! Seien Sie natürlich dem PO
sierten Tests überprüft zu werden? Was, wenn weder dem PO stets behilflich beim Ausräumen von Unsicherheiten. Produk­
noch Ihnen (gute) Testfälle einfallen? tionscode ist dafür jedoch kein Mittel. Prototypen sind es.
Der Grund dafür kann sein, dass der Scope der Anforde­ In Zeiten von KI als „Codierknecht“ verschiebt sich Ihre
rungen zu groß ist. Dann gilt es, feiner und feiner zu schnei­ Rolle immer weiter in Richtung Geburtshelfer für Anforde­
den, bis der Scope so überschaubar ist, dass sich das Tupel rungsklarheit. Die Codierung übernimmt später die KI. Sie
formulieren lässt. kann jedoch (noch) nicht so hilfreich beim Herauskitzeln von
Es kann allerdings auch sein, dass der PO noch nicht genau Klarheit sein. Dafür braucht es mehr Interaktion, mehr eigen­
weiß, was er wirklich will. Er hat noch keine exakte Vorstel­ ständige Kreativität und Kontextkenntnisse. Hier ist der An­
lung davon, wie korrekte Transformationen aussehen. Die satzpunkt, an dem Sie mit natürlicher Intelligenz und Einfüh­
erste Aufgabe (Bild 1) könnte dafür ein Beispiel sein. Auf die lungsvermögen glänzen können.
Frage „Wie soll der Benutzer dem Programm denn den Na­ Eine klare Formulierung der Anforderungen ist jedoch
men mitteilen?“ könnte der PO antworten: „Hm … keine Ah­ nicht zu verwechseln mit Verständnis. Im Zweifelsfall verste­
nung. Auf der Kommandozeile ist es einfach, aber vielleicht hen Sie die Anforderungen nicht – erkennen jedoch deren
unbequem. Gefragt zu werden ist schlechter zu testen, aber mehr oder weniger formale Klarheit.
bequemer. Ich kann mich noch nicht entscheiden …“ Und Verständnis ist nicht mit Lösungsansatz oder Lösung
Was tun in einem Fall von Unklarheit, Unsicherheit, Ent­ zu verwechseln. Im Zweifelsfall verstehen Sie – doch Sie er­
scheidungsmangel? Für mich ist die Antwort: Prototyping. kennen noch nicht, wie eine Lösung aussehen könnte.
Bisher waren Sie derjenige, der sowohl Verständnis
als auch die Lösung entwickeln musste. Mit Auftreten
der großen Sprachmodelle werden wir diese allerdings
zunehmend beides übernehmen lassen. Heute ist der
Scope noch klein, für den das in genügender Qualität
funktioniert. Doch ich bin gewiss, er wird wachsen.
Damit dieses Potenzial ausgeschöpft werden kann,
bleibt Klarheit der Anforderungen wichtig. Domänen­
experten inklusive POs werden es weiterhin schwer
haben, ihre Wünsche präzise genug alleine zu formu­
lieren. KI­gestützte Tools werden sich ihnen zwar an­
dienen, doch eine Lücke wird bestehen bleiben. Dort
ist „Hebammenkunst“ gefragt, für die Sie als Entwick­
ler prädestiniert sind.
Ausblick
Anforderungen müssen eine Idee von der Kausalkette vermitteln, die Um weniger Zeit in Iterationen zu verschwenden, um
Input zu Output transformiert (Bild 9) dem Softwareentwurf einen besseren Ausgangspunkt
50 4.2024 www.dotnetpro.de
004422--005511__SSlliicciinngg__eeaa__ffss..iinndddd 5500 0044..0033..2244 1155::5522


---


<!-- Page 10 of 10 -->


PLANUNG Slicing
zu bieten und um KI als Co­Pilot in der Programmierung ein­ Zusammenarbeit. Auch der PO wird es Ihnen danken, dass
setzen zu können, ist ein kritischer Blick auf die Anforde­ Sie ihn nicht mit Rückfragen stören.
rungsanalyse nötig. Sie als Softwareentwickler sollten einen So viel als Zielbild für die Anforderungsanalyse aus Ihrer
Anspruch daran haben, was formal das Ergebnis einer Anfor­ Sicht als Softwareentwickler. Es ist überschaubar, finden Sie
derungsanalyse sein soll, damit Sie Ihre eigentliche Aufgabe nicht? Mir fällt die Programmierung viel leichter, seitdem ich
der Herstellung von Code am besten erfüllen können. diesem Zielbild folge. Die Energie in Anforderungsanalyse­
Für mich besteht dieser Anspruch in hoher Testbarkeit. Mit gesprächen ist eine ganz andere. Ich fühle mich nicht mehr
der Arbeit an Produktionscode sollten Sie nicht beginnen, be­ als „Opfer“ oder „Empfänger“, sondern als Mitgestalter auf
vor Sie aus dem Gespräch mit dem PO nicht das Tupel (Funk- Augenhöhe mit dem PO.
tionssignaturen, Testfälle) für seine Anforderungen abgelei­ Einen Haken hat das Zielbild jedoch: Sie können zu den
tet haben. Zusätzliche Beschreibungen einer „Kausalkette“ Funktionen als Ansatzpunkte für Testfälle nicht springen. Bei
für die Transformation der Daten der Testfälle durch eine Lö­ realistischen Anforderungen liegen diese nicht auf der Hand.
Schon im ersten Beispiel hier
haben sie Sie nicht ange­
sprungen; vielmehr habe ich
sie für Sie herausgearbeitet –
ohne Ihnen zu sagen, was für
mich dafür die Methode oder
das Big Picture war.
Testfälle brauchen Funktio­
nen, auf die sie angesetzt
werden.
Prototypen für alternative Die zur Umsetzung von An­
Benutzerschnittstellen forderungen nötigen/nützli­
(Bild 10) chen Funktionen liegen nicht
auf der Hand.
Die Anforderungsanalyse
ist vielmehr ein eigener Ent­
sung sind natürlich auch hilfreich – doch darüber dürfen Sie wicklungsprozess mit Inkrementen und Iterationen, dessen
das Tupel nicht vergessen. Ziel nicht lauffähiger Code, sondern ausgefüllte Templates
Sie kennen das agile Template für User Stories: „As a (ro­ wie oben formuliert sind.
le), I want (function) so that (business value)“, bestehend aus Auch dieser Entwicklungsprozess profitiert von Systema­
role, goal, reason oder who, what, why. tik. Die möchte ich Ihnen mit Slicing bieten. Damit bewegen
Setzen Sie dem ein eigenes Template für sich selbst als Ent­ Sie sich in klar definierten Schritten durch Anforderungen
wickler gegenüber, mit dem Sie die Qualität von Anforderun­ von außen nach innen, vom Groben zum Detail, vom breiten
gen aus Ihrer Per spektive beurteilen: „A function with signa­ Scope zu dünn geschnittenem.
ture <signature> to satisfy the test <test case> by implemen­ Jeder Schritt dreht sich um etwas, das für den PO greifbar
ting <causal chain>.“ ist und gleichzeitig für Sie eine konkrete Entsprechung im
Wie gesagt: Es ist okay, diese formale Klarheit nicht sofort Code hat. Im Slicing nehmen Sie den PO an die Hand. Ge­
zu haben. Das ist keine Schande. Auch der PO sollte das ver­ meinsam reisen Sie „in verschiedenen Zoomstufen“ durch
stehen. Es ist vielmehr bei komplexeren Anforderungen zu die Anforderungen und Codestrukturen. Ein zusätzlicher
erwarten. Also: Keine Panik. Nutzen des Slicing: Es unterstützt Sie bei der Strukturierung
Die passende Reaktion ist dann entweder eine Verringe­ Ihres Codes; es ist verbunden mit einem sauberen Architek­
rung des Scope oder ein Prototyp. Beides ist keine Zeitver­ turstil. Analyse und Entwurf überlappen mit dem Slicing.
schwendung. Die ist vielmehr unvermeidbar, wenn Sie zu Im nächsten Artikel geht es los mit einem Blick auf Anfor­
früh, das heißt bei mangelnder Klarheit, beginnen, Produk­ derungen aus großer Flughöhe. ◾
tionscode zu verändern. Dann kommt es zu unnötigen, risiko­
reichen Iterationen.
Für Arbeit am Produktionscode ist „full kitting“ nötig, um Ralf Westphal
sie schnellstmöglich abzuschließen. Erst dann können ja die ist Trainer, Berater und Mitgründer der Clean
Testfälle zum Einsatz kommen für die „Reifeprüfung“. „Full Code Developer Initiative (https://clean-code-
kitting“ bedeutet, dass Sie sorgfältig überprüfen, ob Sie developer.de). Seine Schwerpunkte sind dauer-
schon alles haben, was Sie für die Arbeit am Produktionscode haft hohe Produktivität für die Softwareent-
brauchen. Ist alles zur Hand? Sind alle Fragen geklärt? Füh­ wicklung und zukunftsfähige Teamorganisation.
len Sie sich in der Lage, die Reife selbst (mittels Tests) zu prü­ https://ralfw.de
fen? Rückfragen sind Iterationen und verzögern Ihre Liefe­
dnpCode A2404Slicing
rung. Vermeiden Sie Rückfragen durch gute Vorbereitung in
www.dotnetpro.de 4.2024 51
004422--005511__SSlliicciinngg__eeaa__ffss..iinndddd 5511 0044..0033..2244 1155::5522