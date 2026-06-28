<!-- Page 1 of 12 -->


PLANUNG Sleepy Hollow
SLEEPY-HOLLOW-ARCHITEKTUR
Den Kopf vom Körper
trennen
Als Architekturmuster für Testbarkeit schließt Sleepy Hollow an die Anforderungsanalyse
mit Slicing an und ist eine spezielle Interpretation der IODA-Architektur.
Automatisiertes Testen ist der Treiber für sauberen Code. Nein, KI-generierter Code muss automatisiert überprüft
Ja, es geht auch um Wandelbarkeit und Produktionseffi- werden. Dafür braucht es Testbarkeit. Und Testbarkeit ist Teil
zienz [1]. Aber wenn ich es ganz spitz auf einen Punkt brin- von und führt zu Clean Code Development.
gen soll, dann sage ich: Es geht um Testbarkeit, Testbarkeit,
Testbarkeit
Testbarkeit, also den Wert Korrektheit von Clean Code Deve-
lopment [1]. Alles andere folgt ganz natürlich aus der Test- Testbarkeit, also das Potenzial, automatisierte Tests möglichst
barkeit, etwa Verständlichkeit und Modularisierung. einfach überhaupt an Code anlegen zu können, setzt Schnitt-
Und darüber liegt heute, dass KI der Treiber für automati- stellen voraus. Das, was getestet werden soll, ist Logik [2]. Lo-
siertes Testen ist. KI ist also die Killerapplikation für Clean gik sind die Anweisungen im Code, die selbst Verhalten her-
Code Development. Warum? Weil Sie ohne automatisierte stellen: Ausdrücke, Kontrollflusssteuerungen, API-Zugriffe.
Tests der KI nichts glauben dürfen. Code, den KI produziert, Bild 1 zeigt beispielhaft die Logik für die Berechnung des
müssen Sie automatisiert testen, um zu beurteilen, ob die KI Durchschnitts von Zahlen, die einer Anwendung bei deren
mit ihm die Spezifikationen in Ihren Prompts erfüllt. Start auf der Kommandozeile mitgegeben werden.
Funktioniert diese Logik, ist sie korrekt? Wie kann ich das
feststellen? Ich kann sie ausführen und schauen, ob die Aus-
gabe mit meinen Erwartungen übereinstimmt. Doch das ska-
liert nicht; auf diese Weise kann ich nicht systematisch viele
Tests wiederholt verlässlich ausführen. Außerdem fehlt jeder
Nachweis, dass und was ich überhaupt getestet habe.
Solchen Code kann ich nicht wirklich als testbar bezeich-
nen. Ihm fehlt eine Schnittstelle, auf die ich automatisierte
Tests ansetzen kann. Im einfachsten Fall ist das eine Funkt ion
Pure Logik für die Berechnung des Durchschnitts mehrerer wie in Bild 2 gezeigt. Diese Funktion sollte so viel Logik wie
Z ahlen (Bild 1) irgend möglich enthalten beziehungsweise als Testansatz-
punkt repräsentieren. Im Beispiel habe ich mich deshalb da-
für entschieden, sogar die Konvertierung der Zeichenketten
Bei Menschen als Zulieferern konnten wir uns noch darauf hinter die Testfassade zu stellen.
herausreden, dass die sicher ihren Code irgendwie getestet Level 1 sauberer Programmierung ist erreicht: formale Test-
haben werden, bevor sie ihn uns gaben. Oder sie übergaben barkeit durch einen „Testpunkt“ (im Vergleich zu einem Ser-
ihn uns in einem Dialog, und wir glaubten einfach, dass das vice-Endpunkt). Aber was ist mit den nächsten Levels?
schon alles korrekt sein würde. Das war immer schon sehr
Wandelbarkeit
dünnes Eis, auf dem wir uns bewegt haben, doch es fühlte
sich noch plausibel an. Warum zieht Testbarkeit andere saubere Eigenschaften von
Mit der KI ziehen diese „Ausreden“ nicht mehr als Argu- Code nach sich? Wie fördert Testbarkeit die Wandelbarkeit?
ment, auf automatisierte Tests zu verzichten. Weder hat die Für Testbarkeit braucht es erstens Schnittstellen, auf die
KI für sich den Code, den sie uns präsentiert, in irgendeiner Tests überhaupt angesetzt werden können. Schnittstellen
Weise überprüft; noch übergibt sie ihn uns in einem Gespräch werden von Modulen angeboten. Sie fassen Logik in Funktio-
voller vertrauensheischender Formulierungen. Das müssten nen zusammen, von denen sie manche in ihrer Schnittstelle
wir erst im Chat anstoßen, und es würde Mühe machen. Ge- veröffentlichen und manche nicht. Veröffentlichte Funktio-
nauso macht es Mühe, den KI-Code durch Augenscheinnah- nen sind direkt testbar, private Funktionen nur indirekt via
me zu überprüfen, ganz davon zu schweigen, dass das unzu- veröffentlichte. parseArgs in Bild 3 ist eine solche schlecht
reichend wäre. testbare, weil private Funktion.
46 11.2024 www.dotnetpro.de
004466--005577__SSlleeeeppyyHHoollllooww__eeaa22..iinndddd 4466 3300..0099..2244 0099::5544


---


<!-- Page 2 of 12 -->


PLANUNG Sleepy Hollow
Testbare Logik mit
automatisierten
Tests (Bild 2)
Zweitens braucht Testbarkeit Unabhängigkeit. Logik, die Abstraktionen und Indirektionen müssen zu Hilfe gerufen
getestet werden soll, sollte möglichst unabhängig von ande- werden (Stichwort Dependency Inversion Principle, DIP).
rer Logik sein, die gerade nicht getestet werden soll. Sie entkoppeln, machen also nicht nur testbarer, sondern
Warum sollte überhaupt ein Fokus auf einen Ausschnitt von auch wandelbarer.
Logik gelegt werden? Weil die Testfälle ansonsten zu um-
fangreich oder zu komplex werden. Aussagekräftige Testfäl- Wenn nun für die Testbarkeit Logik auf möglichst unabhän-
le brauchen hohe Pfadabdeckung. Je mehr Logik in Tests auf gige Funktionen und Module aufgeteilt wird, entstehen ver-
den Prüfstand kommt, desto vielfältiger die Kombinationen gleichsweise kleine Einheiten mit sehr fokussierter Funktio-
der Ausführungswege. nalität. Die begünstigen die Wandelbarkeit einer Codebasis,
Daraus folgt dreierlei: mindestens weil …
Es ist ein Kriterium zu finden, wie Logik aufgeteilt werden sie sich leichter in unterschiedlichen Zusammenhängen
kann. Dafür haben sich schon lange eine Separation of Con- neu kombinieren lassen,
cerns (SoC) und der Fokus auf Single Responsibility (SRP) sie mit wenig Aufwand auch einmal neu geschrieben wer-
als vorteilhaft erwiesen. Bei SoC geht es um orthogonale den können, falls sie eine Qualität verloren haben, die mit
Aspekte von Funktionalität, beim SRP um einzelne Ent- Refaktorisierung nicht wieder hergestellt werden kann.
scheidungen innerhalb von Aspekten. Das Mittel zur Auf-
teilung nach SoC sind üblicherweise Module, das nach SRP Level 2 sauberer Programmierung ist erreicht, weil Testbar-
Module und Funktionen. keit „Druck ausübt“ auf den Umfang und den Zusammen-
Logik, die auf verschiedene Funktionen aufgeteilt wurde, hang von Logik in Funktionen. Testbarkeit führt zu feinerer
sollte so wenig wie möglich voneinander abhängig sein, Granularität und geringerer Abhängigkeit.
egal ob sie im selben oder in verschiedenen Modulen liegt.
Verständlichkeit
Abhängig ist Logik von anderer Logik, wenn zwischen sie
Aufrufe anderer Funktionen gestreut sind (sogenannte Und wie fördert Testbarkeit die Verständlichkeit? Zum einen
funktionale Abhängigkeit [3], siehe Zeile 2 in Bild 3). Dann tut sie das schon durch Modularisierung. Kleinere Einheiten
ist Logik „in der Tiefe gestaffelt“, sodass nicht mehr zu von Logik sind leichter zu verstehen als größere. Je feiner Lo-
überblicken ist, was eigentlich getestet wird. gik auf Namensräume verteilt ist – explizite Namensräume,
Wo Abhängigkeiten unvermeidbar sind und die Testbarkeit Module, Funktionen –, desto ausführlicher ist ihre Intention
stören, sind Maßnahmen zu treffen, um sie zu entschärfen. durch Namen (identifier) beschrieben. Statt Logik im Kopf ▶
www.dotnetpro.de 11.2024 47
004466--005577__SSlleeeeppyyHHoollllooww__eeaa22..iinndddd 4477 3300..0099..2244 0099::5544


---


<!-- Page 3 of 12 -->


PLANUNG Sleepy Hollow
zu simulieren, um zu verstehen, was sie tut (beziehungswei-
se tun soll), lesen Sie das aus ihrem Namenspfad ab.
Dazu kommt, dass Logik viel weniger (oder gar nicht mehr)
voneinander abhängig ist. Ohne Tiefenstaffelung über funk-
tionale Abhängigkeiten liegt zu simulierende Logik komplett
vor Ihnen, wenn Sie eine Funktion anschauen. Kein Debug-
ging mit step-into ist mehr nötig, keine Sprünge in immer grö-
ßere Tiefen des Quellcodes in der IDE sind erforderlich, um
zu verfolgen, was passiert, wenn eine Funktion aufgerufen
wird. Auf diese Weise wird auch das Prinzip des Single Level
of Abstraction (SLA) quasi automatisch bedient. Nur öffentliche Funktionen sind direkt testbar (Bild 3)
Zuallererst jedoch sehe ich die Verständlichkeit durch ei-
nen veränderten Umgang mit Anforderungen gefördert:
Wenn die Testbarkeit im Vordergrund steht, geht es um An- bringt ein kopfloser Reiter Unheil über ein kleines Dorf an der
forderungen. Tests sind formalisierte Anforderungen, deren Ostküste der USA im Jahr 1799. Anders als sonst spielt der
Erfüllung sie automatisch überprüfen (siehe rechts unten in Kopf eines Protagonisten nur eine geringe Rolle, sein Körper
Bild 2). Für diese formalisierten (oder auch informelle) Anfor- hingegen eine umso größere. Er treibt die Handlung; wo er
derungen stellt sich die Frage: Welchen Scope können Sie ist, ist Action. Kopf und Körper gehören zusammen; doch das
eigentlich klar und lückenlos verstehen, umsetzen und mit Verhalten steckt im Körper.
Tests abdecken? Das ist aus meiner Sicht eine zu suchende Grundstruktur
Wenn Sie KI für die Codegenerierung benutzen, werden für Software: Kopf und Körper sind zu trennen. Das, was das
Sie schnell merken, dass Anforderungen sehr überschaubar Verhalten erzeugt, ist von dem, wo die Interaktion stattfindet,
sind, die diese Eigenschaften haben. Sie geben der KI keine zu separieren.
zehn Seiten Anforderungsdefinition und warten entspannt Bild 4 zeigt diese Struktur in ihrer einfachsten Form. Der
auf Code, der sie erfüllt und dem Sie einfach vertrauen. Nein, Body ist der Bereich, in dem „die Musik spielt“. Der Body um-
Sie werden schon intuitiv die Anforderungen recht fein fasst den testwürdigen und vor allem den testbaren Code.
schneiden und sich die Generierung von überschaubaren Testbar ist Code für mich, wenn die Logik von keiner User-
Funktionen und Modulen wünschen – für die dann auch die Interface-Technologie getrübt wird.
Tests überschaubar sind. Es gibt zwar Werkzeuge, mit denen man das UI und durch
Der Fokus auf solide Anforderungen, der durch das Primat das UI testen kann, doch die finde ich vergleichsweise um-
der Testbarkeit entsteht, führt zu kleineren Scopes für kleine- ständlich, um damit wirklich mehr als die Bedienung zu tes-
re Funktioneinheiten, die dann auch ver- ten. Für Integrationstests taugen sie nach
ständlicher sind. meinem Dafürhalten nicht.
Level 3 sauberer Programmierung ist Logik, die von Persistenz- oder Netz-
erreicht. Konzeptionell jedenfalls. Denn werktechnologie abhängig ist, ist zwar
es stellt sich die Frage: Wie sieht das auch nicht ganz leicht zu testen, doch die
praktisch aus? Automatisierung fällt hier deutlich leich-
ter als im User Interface. Die Schnittstel-
Sleepy Hollow – ein Architektur-
len sind stabiler.
muster für Testbarkeit
Wenn Testbarkeit der Treiber für sau-
SoC, SRP, SLA, DIP … all diese Prinzipien beren Code ist, dann ist diese Untertei-
mögen überwältigend klingen. Wie sol- lung des Codes der erste und fundamen-
len Sie ihnen gerecht werden? Wann ist tale Schritt hin zu mehr Sauberkeit. Mit
„sauberer Code“ mit seinen Vorteilen für ihm wird eine klare Grenze gezogen, wo
die langfristige Produktivität erreicht? Tests angelegt werden sollen und kön-
Genau genommen ist das wirklich nen: am Body.
nicht so einfach. Wer es auf Perfektion Die dortigen Tests sind notwendig In-
abgesehen hat, wird schnell frustriert tegrationstests. Mit ihnen wird das Zu-
und/oder gerät in Konflikte mit anderen, sammenspiel von Domäne und Providern
die es anders sehen. Das Sleepy-Hollow-Architekturmuster überprüft. Sie sind für mich Akzeptanz-
Um das zu vermeiden, möchte ich Ih- (Bild 4) tests auf sehr hohem Niveau.
nen das Sleepy-Hollow-Architekturmus- In Bild 5 sehen Sie, wie typische Modu-
ter vorstellen. Es schließt an die Anforde- le eines Softwaresystems auf Head und
rungsanalyse mit Slicing (siehe die dotnetpro-Artikel [4] bis Body verteilt werden:
[5]) an und ist eine spezielle Interpretation der IODA-Archi- Der Body umfasst die Logik für die Fachlichkeit (Domäne),
tektur [6]. Inspiriert ist die Bezeichnung „Sleepy Hollow“ den Zugriff auf Ressourcen (Provider) und potenziell weite-
durch den gleichnamigen Spielfilm von Tim Burton. In dem re, orthogonale Aspekte (zum Beispiel Logging).
48 11.2024 www.dotnetpro.de
004466--005577__SSlleeeeppyyHHoollllooww__eeaa22..iinndddd 4488 3300..0099..2244 0099::5544


---


<!-- Page 4 of 12 -->


PLANUNG Sleepy Hollow
Außerdem ist im Body auch UI-nahe Logik zu finden, die Das Muster ist: Wo immer ein User Interface auftaucht – in
nicht von UI-Technologien abhängig ist. Bild 6 ist das sowohl im Client als auch im Server der Fall –,
Der Head versammelt die Logik, die eng mit User-Interface- ist das „vom Rest“ zu trennen, um „den Rest“ testbar zu ma-
Technologien verzahnt ist. chen.
Die Schnittstelle des Bodys
Im Grunde ist das schon alles Wesentliche von Sleepy Hol-
low. Auf diese Weise wird ein Maximum an Logik relativ ein- Wie funktioniert die Trennung zwischen Head und Body? Mit
fach automatisierbar testbar. Nur eine Schnittstelle ist nötig: einem Modul mit klarer Schnittstelle. An dieser Schnittstelle
die des Bodys. Durch sie laufen alle High-Level-Integrations- veröffentlicht der Body seine Leistungsangebote, die über ein
tests: die Akzeptanztests. User Interface angesteuert werden können.
Akzeptanztests nenne ich sie, weil sie aus der Perspektive Der Body ist für jedes User Interface eine Blackbox mit ei-
von Benutzern formuliert sind. Das einzige Zugeständnis an ner Fassade. Vor diese Fassade können ganz verschiedene
die Testbarkeit ist, dass sie nicht auf dem Frontend ausgeführt User Interfaces gesetzt werden. Die Blackbox ist UI-Techno-
werden. Doch ansonsten simulieren sie, wie Anwender das logie-agnostisch. Darin liegt der Sinn dieser Trennung: alle
Softwaresystem nutzen würden. Es sind also keine techni- Abhängigkeiten von UI-Technologie diesseits der Fassade.
schen Tests, und es sind auch keine Tests von Details. Jenseits der Fassade gibt es zwar weitere Technologieabhän-
Auf dem Niveau von Akzeptanztests ist keine hochprozen- gigkeiten, doch die sind leichter in automatisierten Tests zu
tige Pfadabdeckung der Logik zu erwarten. Ihre Aufgabe ist beherrschen.
nicht, alles bis ins Kleinste zu prüfen. Vielmehr sollen sie Woher kommen die Funktionen an der Schnittstelle eines
„nur“ sicherstellen, dass der verhaltensrelevante Teil des Bodys? Denn Funktionen sind Leistungsangebote, weil sie
Softwaresystems korrekt zusammengesetzt ist und grund- Logik enthalten oder Logik in anderen Funktionen aufrufen,
sätzlich seinen Job erledigen kann, vom UI bis zurück zum UI die das Verhalten herstellt, das die Leistung eines Bodys dar-
und möglichst End-to-End. stellt. Bodies sind Dienstleister für User vermittels User Inter-
Bitte beachten Sie die Terminologie von Sleepy Hollow! Ich faces.
spreche nicht von Frontend und Backend, und auch nicht von Für mich gibt es nur einen Weg zur Schnittstelle des Bodys:
Client und Server. Es geht nicht um Verteilung über Prozess- eine systematische Anforderungsanalyse mit Slicing (siehe
grenzen hinweg. Diese Verteilung ist unabhängig von der [4] bis [5]), deren Ergebnis eine Liste von Entry-Point-Funk-
Head-Body-Struktur. tionen ist. Sie werden durch Interaktionen von Anwendern
Bild 6 macht das deutlich. Sie sehen dort sogar eine ge- mit dem Softwaresystem über das User Interface getriggert.
schachtelte Anwendung des Architekturmusters. Das User Interface ist dazu da, Anwendern den Aufruf dieser
Einerseits sind Teile des Clients und der gesamte Server in Funktionen möglich zu machen.
einem Body zusammengefasst. User Interface steht dabei nicht nur für eine WPF-Oberflä-
Andererseits existieren getrennte Bodies für Client und che oder eine HTML-Seite, sondern auch zum Beispiel für
Server. HTTP-Endpunkte. User-Interface-Logik ist die Logik, die ▶
Aufteilung typischer
Module auf Head und Body
des Sleepy-Hollow-Archi-
tekturmusters (Bild 5)
www.dotnetpro.de 11.2024 49
004466--005577__SSlleeeeppyyHHoollllooww__eeaa22..iinndddd 4499 3300..0099..2244 0099::5544


---


<!-- Page 5 of 12 -->


PLANUNG Sleepy Hollow
Head und Body sind orthogonal zu einer Client-Server-Verteilung von Logik (Bild 6)
„weiß“, welche Technologie für die Interaktionen eingesetzt aktionen gibt es bei der Anwendung? Nur eine: den Pro-
wird. Sie ist eng verzahnt etwa mit WPF oder ASP.NET Core grammstart. Bei dem werden die zu verrechnenden Werte auf
MVC. Sie ist schwer testbar – und deshalb ist sie in einem der Kommandozeile gleich mitgegeben. Das Ergebnis er-
Head zu konzentrieren und von weiterer Logik zu trennen, scheint als Ausgabe auf der Konsole.
dem Body. Auch das ist eine Anwendung des Prinzips SoC. Als UI-Technologien kommen Zugriff auf Kommandozeile
Als triviales Beispiel soll noch einmal die Berechnung des und Zugriff auf Konsole zum Einsatz. Beides gehört in den
Durchschnitts einer Reihe von Zahlen dienen. Welche Inter- Head. „Der Rest“ wird im Body zusammengefasst. Dessen
Schnittstelle hat nur eine Funktion, weil es auch nur eine In-
teraktion gibt. In Bild 7 trenne ich beide Aspekte und entkopp-
le auch noch durch ein Interface, um den Head selbst etwas
testbarer zu machen.
Technisch ist diese Trennung wahrlich kein Hexenwerk.
Der Trick liegt im Anlass für sie: die konsequente Entflech-
tung von User-Interface-Technologie und „dem Rest“ zum
Zweck der Testbarkeit auf sehr hohem Abstraktionsniveau.
Diese Trennung können Sie selbst dann vornehmen, wenn
Ihnen sonst keine Module einfallen. Domäne, Model, Provi-
der, Adapter oder was sonst noch so an Begriffen in Architek-
turmodellen herumschwirren mag, können Ihnen (zunächst)
egal sein. Tun Sie sich den Gefallen und ziehen Sie wenigs-
tens Head-Logik und Body-Logik auseinander.
In Bild 7 habe ich rot eingefärbt, wo Logik von User-Inter-
face-Technologie abgängig ist. Grün hinterlegt ist der Aufruf
des Bodys.
Diskussionswürdig könnte sein, dass ich die Umwandlung
der Zahlen auf der Kommandozeile in Zeile 5 komplett im
Head gelassen habe. Wäre nicht auch das Mapping testwür-
dig und sollte deshalb in den Body wandern? Dafür spräche
das Mehr an gut testbarer Logik. Dagegen spricht, dass Zah-
len in Form eines String-Arrays eigentlich zur Eigenart des
Konsole-User-Interface gehören. Wäre das User Interface ein
Logik sauber in Head und Body getrennt (Bild 7) HTTP-Controller, dessen Endpunkt die Zahlen als JSON-Ob-
50 11.2024 www.dotnetpro.de
004466--005577__SSlleeeeppyyHHoollllooww__eeaa22..iinndddd 5500 3300..0099..2244 0099::5544


---


<!-- Page 6 of 12 -->


PLANUNG Sleepy Hollow
jekt übergeben werden, würde die Umwandlung anders aus-
sehen. Das zeigt Bild 8 anhand eines val.town-Controller-
Skripts, das über einen URL direkt mittels POST und ein
JSON-Array mit Zahlen aufgerufen werden kann.
Die Schnittstelle des Bodys ist unverändert. Die Sammlung
der zu verrechnenden Zahlen erfolgt allerdings anders als
beim Konsolenprogramm – wie natürlich auch die Projektion
des Ergebnisses für den Anwender.
Sie spüren jetzt hoffentlich schon etwas von dem Vorteil,
den das Sleepy-Hollow-Architekturmuster bringt: Es entkop-
pelt sauber zwei sehr unterschiedliche Aspekte von Software.
Vor der Fassade kann das UI wechseln, hinter der Fassade
bleibt der Code unverändert. Nicht nur die Testbarkeit wird
gefördert, sondern auch die Wandelbarkeit.
Und wie in Bild 6 gezeigt, könnte jetzt sogar der val.town-
Server mit dem Endpunkt aus Bild 8 in einen neuen Body wan-
dern, zu dem weiterhin ein Console-Head gehört (Bild 9).
Der Body ist jetzt zwar nur ein Adapter, aber das Muster
wurde eingehalten. Diese Ausprägung des Bodys ist gut test-
bar, selbst wenn das bedeutet, einen Server aufzurufen. In In-
tegrationstests müssen nicht immer alle Ressourcen „abge-
klemmt“ und durch Surrogate ersetzt werden.
Die User-Interface-Pipeline
Die Schnittstelle des Bodys macht unabhängig von Frontend-
Technologien und abstrahiert die technologischen Details in- Ein alternativer Body, der die Verarbeitung an den val.town-
nerhalb des Bodys: Controller delegiert (Bild 9)
Aufruf einer Funktion in der Schnittstelle des Bodys (grün).
Trotz unterschiedlicher UI-Technologien ist das in beiden
Head-Implementationen gleich.
Ebenfalls gleich ist, was vor und nach diesem Aufruf pas-
siert. Es ist nicht derselbe Code, doch derselbe Zweck wird
für beide Implementationen erfüllt. Vor und nach dem Aufruf
des Bodys steht Code, der abhängig von der UI-Technologie
ist und eine Klammerfunktion hat. run() (links) und der HTTP-
Controller-Endpunkt (rechts) werden im Rahmen einer Inter-
Ein HTTP-Controller als alternatives User Interface erhält die zu aktion getriggert. Diese bekommt Input und liefert Output.
verrechnenden Zahlen als JSON-Array (Bild 8) Das macht die Reaktion auf einen „Reiz“ aus (Programmauf-
ruf auf der Kommandozeile beziehungsweise HTTP-Request
an einen Server). run() und die Controller-Funktion sind
Im Body gibt es zum Beispiel keine Kenntnis darüber, wo- Eventhandler der Interaktion; mit ihnen tritt die Kontrolle ins
her die zu verrechnenden Zahlen kommen. Softwaresystem ein.
Im Head gibt es zum Beispiel keine Kenntnis darüber, ob Wie Eventhandler für Interaktionen aussehen, ist abhängig
die Durchschnittsberechnung lokal oder verteilt stattfindet. von der User-Interface-Technologie, wie Bild 10 zeigt. Was ▶
In Bild 4 habe ich dieses Verhält-
nis von Head und Body mit einer
Abhängigkeit eingeführt; dafür
steht die Linie mit dem Punkt am
Ende (statt eines sonst üblichen
Pfeils für Abhängigkeiten). In
Bild 10 sehen Sie, wie diese Ab-
hängigkeit im Code des Con-
sole-Head und des Controller-
Head aussieht: Sie führt zum Zwei Head-Implementationen für denselben Body im Vergleich (Bild 10)
www.dotnetpro.de 11.2024 51
004466--005577__SSlleeeeppyyHHoollllooww__eeaa22..iinndddd 5511 3300..0099..2244 0099::5544


---


<!-- Page 7 of 12 -->


PLANUNG Sleepy Hollow
in Eventhandlern passiert, ist jedoch immer gleich – nur wie
es genau passiert, ist wiederum abhängig von der UI-Tech-
nologie. Für jede Interaktion sieht der Prozess so aus:
Zuerst wird der Input des Anwenders gesammelt; das nen-
ne ich die Collection-Phase.
Dann wird der Body aufgerufen.
Schließlich wird das Ergebnis des Bodys in Output für den Die grundlegende User-Interface-Pipeline (Bild 11)
Anwender verwandelt; das nenne ich die Projection-Phase.
Die Body-Pipeline
Sammeln, transformieren, projizieren: Das ist die grundle-
gende Pipeline, die Input bei jeder Interaktion durchläuft In Bild 5 sehen Sie, dass ich einen Teil des User Interface in
(Bild 11). Sie entspricht dem uralten EVA-Prinzip: Eingabe – den Body übernommen habe. Warum das? Natürlich der Test-
Verarbeitung – Ausgabe. barkeit wegen.
Collection und Projection sind technologiespezifisch. Sie Sammlung und Projektion sind die Anteile des User Inter-
müssen deshalb im Head verbleiben. Sie sind von Head zu face, die schlecht zu testen sind, weil sie mit UI-Technologie
Head verschieden. verzahnt sind.
Der Benutzer liefert „irgendwie“ Daten beim Head an, zum Doch bevor Domäne oder Provider das für eine Interaktion
Beispiel auf der Kommandozeile oder in einem Web-Formu- gewünschte Verhalten herstellen können, mag es nötig sein,
lar oder per HTTP-Aufruf. Wie das geschieht, hängt von der den eingehenden Request noch etwas „zu kneten“. Und um
UI-Technologie ab. Damit der Body damit etwas anfangen die Arbeit von Domäne und Providern wirklich unabhängig
kann, müssen die Daten „gesammelt“ werden, zum Beispiel von der Umwelt zu machen, das heißt sogar von spezifischen
durch ein Mapping von Kommandozeilenparametern oder Interaktionen, kann es nötig sein, eine Response von dort am
Parsing einer HTTP-JSON-Payload. Das Ergebnis ist ein Re- Ende auch noch etwas „zu kneten“.
quest für den Body, der den Input von allen Details des User Für mich gibt es daher innerhalb des Bodys um die eigent-
Interface befreit erhält. liche Arbeit herum noch ein Pre-Processing und Post-Proces-
Auf dem Rückweg vom Body ist dasselbe mit dessen Res- sing (Bild 12):
ponse zu tun. „Projektion“ nenne ich die Transformation in Pre-Processing vor der Verhaltensgenerierung
UI-spezifischen Output, weil unter Umständen damit eine • Parsing
mehr oder weniger grafische Darstellung einhergeht. Aber • Validation
auch die Umwandlung in eine HTTP-Response wie in Bild 10 • Mapping
rechts unten ist eine Projektion. Post-Processing nach der Verhaltensgenerierung
Von außen gesehen ist damit alles getan, um den Body test- • Mapping
bar zu machen. Sleepy Hollow besteht nicht nur aus einer mo- • Formatting
dularen Trennung von Logik (Head versus Body), sondern
auch aus einer funktionalen im Sinne eines Datenfluss-Pro- Keiner dieser Schritte muss stattfinden, aber alle könnten
zesses: sammeln, transformieren, projizieren. stattfinden. Es hängt einfach davon ab, wie abstrakt Sie Do-
Doch damit nicht genug … mäne und Provider in Ihren Schnittstellen auslegen.
Die vollständige Body-Pipeline über
zwei Integrationsebenen (Bild 12)
52 11.2024 www.dotnetpro.de
004466--005577__SSlleeeeppyyHHoollllooww__eeaa22..iinndddd 5522 3300..0099..2244 0099::5544


---


<!-- Page 8 of 12 -->


PLANUNG Sleepy Hollow
Pre- und Post-Processing sind im Body, weil sie auf keiner
UI-Technologie basieren. Damit sind sie grundsätzlich gut
testbar.
Das, was in Bild 11 noch ein Prozessschritt war – die Trans-
formation von Request zu Response durch den Body –, ist in
Bild 12 aufgebrochen und verfeinert. Die Transformation ist
nicht monolithisch, sondern wiederum ein Prozess in Form ei-
nes Datenflusses. Die Reihenfolge der Verarbeitungsschritte
liegt auf der Hand: Sie läuft vom rohen Input über dessen Zu-
richtung für die Domäne über die zentrale Verarbeitung wei-
ter zur Aufbereitung des Ergebnisses in Form eines anspre-
chenden Outputs. In Bild 13 sehen Sie alle Schritte auf der un-
tersten Ebene ausgehend vom Benutzer und wieder zurück
zum Benutzer: Die Daten aus der Umwelt fließen in einem
„U“ durch das Softwaresystem; dabei wird Input in Output
verwandelt.
Jeder Verarbeitungsschritt des Bodys in diesem Datenfluss
kann für sich gut getestet werden, und für alle zusammen gilt
das ebenfalls. Der Datenfluss vom Benutzer durch das Softwaresystem zurück
Kein Verarbeitungsschritt im Body ist von UI-Technologie zum Benutzer (Bild 13)
abhängig.
Kein Verarbeitungsschritt ist von einem anderen abhängig.
sich allein getestet werden – oder alle zusammen unter dem
Auch wenn in Bild 13 die Schritte übereinander angeordnet Dach von Transform der Interaktion.
sind, um anzudeuten, dass hier die Verarbeitung unter die
Vertical Slice Architecture
Oberfläche der Software geht, sind die Schritte mit Pfeilen
verbunden. Das bedeutet, es fließen Daten zwischen ihnen, In Bild 4 mag das Sleepy-Hollow-Architekturmuster noch wie
ohne dass die Schritte sich kennen müssten. Diese „Verschal- eine einfachere Form der Schichtenarchitektur aussehen.
tung“ folgt dem Principle of Mutual Oblivion (PoMO) [7], aus- Sind dort nicht nur Businesslogik und Datenzugriff im Body
führlicher entwickelt in [8]. Deshalb kann jeder Schritt für zusammengefasst, und die Präsentationslogik ist zum Kopf ▶
Der Fokus bei Sleepy Hollow
liegt auf einer Strukturierung
des Codes für hohe Testbar-
keit jeder Interaktion (Bild 14)
www.dotnetpro.de 11.2024 53
004466--005577__SSlleeeeppyyHHoollllooww__eeaa22..iinndddd 5533 3300..0099..2244 0099::5544


---


<!-- Page 9 of 12 -->


PLANUNG Sleepy Hollow
ernannt? Nein, das wäre aus mehreren Gründen ein Missver-
ständnis:
Zum einen sind Teile dessen, was im Schichtenmodell Prä-
sentationslogik genannt wird, im Body (Pre- und Post-Pro-
cessing).
Zum anderen ist das Motiv für Sleepy Hollow ein anderes
als das hinter dem Schichtenmodell. Das Schichtenmodell
war getrieben vom Wunsch nach Wandelbarkeit und Wie-
derverwendbarkeit. Bei Sleepy Hollow geht es zunächst um
Testbarkeit.
Und schließlich liegt der Fokus bei Sleepy Hollow auf ein-
zelnen Interaktionen (Bild 14).
Ich sehe aus diesem Grund Sleepy Hollow auch als einen Ver- Vertical Slice Architecture nach Jimmy Bogard [9] (Bild 15)
treter der sogenannten Vertical Slice Architecture [9] [10]
(Bild 15). Deren Motivation ist:
„Vertical Slice Architecture was born from the pain of wor- Jedes Slice ist also zunächst „nur“ ein Datenfluss, der auf
king with layered architectures. They force you to make chan- mehrere Ebenen aufgeteilt ist. Bild 12 zeigt nur drei Ebenen,
ges in many different layers to implement a feature.“ [10] weil genau diese relevant im Zusammenhang mit dem Head
Anforderungen des Kunden beziehen sich nie auf Schich- sind. Letztlich gibt es jedoch beliebig viele Ebenen pro Slice,
ten oder Schalen (Onion Architecture, Clean Architecture), die jeweils durch Prozessschritte in einem Datenfluss reprä-
das heißt Module. Ihr Kontext sind stets eine oder mehrere In- sentiert sind, in die Sie „hineinzoomen“ können. In Bild 12
teraktionen. Deshalb empfehle ich auch eine Anforderungs- sind das sichtbar Transform, Pre- und Post-Process: Die grau-
analyse, die Interaktionen herausarbeitet und sofort unmiss- en Dreiecke zeigen an, was in/hinter diesen Schritten im De-
verständlich mit Entry Points in Form von Funktionen im tail steckt.
Code verbindet (siehe [4] bis [5]). Technisch ist die Umsetzung trivial. In Bild 17 sehen Sie je-
den Pipeline-Schritt aus den Bildern 11 und 12 als Funk-
tion umgesetzt.
Ja, Sie sehen richtig: Sleepy Hollow konzentriert sich
zunächst auf Funktionen. Denn da „spielt die Musik“.
Funktionen tun etwas; sie erzeugen Verhalten. Wie Ver-
halten erzeugt wird als Reaktion auf einen Reiz des An-
wenders im Rahmen einer Interaktion, bestimmt die Lo-
gik [2], die in den Blättern der Datenflusshierarchie
steckt (Integration Operation Segregation Principle
(IOSP) [11], näher entwickelt in [8]).
Anforderungsanalyse mit Slicing und Sleepy Hollow
fokussieren auf die Verhaltenserzeugung mit Daten-
flüssen für einzelne Interaktionen. Umgesetzt werden
diese Datenflüsse mit Funktionen – die natürlich alle
eine Heimat in einem Modul haben.
IODA-Architektur
Alle Funktionen in Bild 17 können Sie sehr leicht verste-
hen. Das liegt daran, dass sie kurz sind und keine Logik
enthalten. Es sind reine Integrationen [11]. So sehen
ganz natürlich mit einer imperativen Programmierspra-
Sleepy-Hollow-Interpretation der Vertical Slice Architecture (Bild 16) che implementierte Datenflüsse aus.
Integrationen sind Funktionen, die Funktionalität auf
höherer Abstraktionsebene aus Funktionen niedrigerer
Diese Eintrittspunkte des Slicing liegen auf der Schnittstel- Abstraktionsebene „komponieren“; Integrationen sind Com-
le des Bodys. Alles darüber und darum gehört zum Head. positions (Komposite).
Anders als in der „klassischen“ Vertical Slice Architecture Diese Idee der Unterscheidung zwischen Integration und
besteht ein Slice für mich nicht aus dünner geschnittenen Operation – Funktionen, die nur Logik enthalten – lässt sich
Schichten, wie noch Bild 15 andeutet. Vielmehr sind Slices vor nun auch auf Klassen (oder Dateien wie in Typescript oder
allem U-Pipelines, von denen so viele „nebeneinander liegen“, Python) ausdehnen: Wenn ein Modul vor allem Funktionen
wie es Interaktionen in einem Softwaresystem gibt (Bild 16). enthält, die integrieren, dann ist es ein integrierendes Modul.
54 11.2024 www.dotnetpro.de
004466--005577__SSlleeeeppyyHHoollllooww__eeaa22..iinndddd 5544 3300..0099..2244 0099::5544


---


<!-- Page 10 of 12 -->


PLANUNG Sleepy Hollow
Wenn es hingegen vor allem Funktionen enthält, die operie-
ren, also tatsächlich Verhalten mittels Logik herstellen, dann
ist es ein operierendes Modul.
Integrationen und Operationen abstrahieren durch Kompo-
sition: Sie fassen Verschiedenartiges zu etwas Neuem zu-
sammen.
Module hingegen abstrahieren durch Aggregation: Sie fas-
sen Ähnliches unter einem Oberbegriff zusammen. Ähnlich
ist, was sich demselben Thema widmet; konkret drückt sich
Ähnlichkeit beziehungsweise Zusammengehörigkeit da-
durch aus, dass Zustand gemeinsam genutzt wird.
Basierend auf dem IOSP definiert die IODA-Architektur des-
halb eine modulare Grundstruktur für Software, die ohne
funktionale Abhängigkeiten [3] auskommt.
In Bild 18 sehen Sie, dass die eigentlichen „Arbeitspferde“
einer Software – Domäne (Core) und Adapter für die Kommu-
nikation mit der Umwelt (Portale und Provider) – einander
nicht kennen. Sie sind anders als in der Schichtenarchitektur
oder auch der Clean Architecture nicht voneinander abhän-
gig, weder direkt noch indirekt. Höchstens teilen sie die
Kenntnis von Datenstrukturen.
Eine weitere Verantwortlichkeit, die Integration, ist einge-
führt, um diese „Arbeitspferde“ explizit zusammenzuschir- Triviale modellhafte Umsetzung der Sleepy Hollow Pipelines
ren. Diese Verantwortlichkeit ist auf der linken Seite in Bild 18 (Bild 17)
nicht visualisiert, aber mitgedacht; deshalb fehlen dort Bezie-
hungspfeile zwischen den „Arbeitspferden“.
In anderen Architekturen sind die Abhängigkeiten zwi- Das Sleepy-Hollow-Architekturmuster differenziert nun
schen Schichten beziehungsweise Schalen genauestens ein- die Integration der IODA-Architektur in Bild 18 rechts. Ganz
gezeichnet (meistens mit Pfeilen) oder durch räumliche Nä- konkret definiert Sleepy Hollow drei Ebenen der Integration
he von Modulen suggeriert (zum Beispiel Schichtung ohne (Bild 19):
Zwischenräume). Die IODA-Architektur kennt solche Ab- Eine Application integriert Sammlung und Projektion des
hängigkeiten nicht, deshalb sind links in Bild 18 keine Verbin- User Interface mit der Transformation. Die Application stellt
dungslinien. Verbindungen gibt es erst rechts und stets aus- den Datenfluss wie in Bild 11 her. Transform ist mithin Teil
schließlich von einer Integration nach unten weisend. der nächsten Integration. Eine Application veröffentlicht als
Ein integrierendes Modul in der IODA-Architektur hat den Einstiegspunkt zum Beispiel eine run()-Funktion.
Zweck, andere Module zu integrieren. Im integrierenden Interactor-Integrationen integrieren innerhalb von Transfor-
Modul findet sich keine Logik (beziehungsweise nur in Aus- mationen das Pre-/Post-Processing aus einem darauf spezi-
nahmefällen). Integrationen in IODA definieren Datenflüsse. alisierten Modul mit der eigentlichen Verarbeitung von ▶
Die Grundstruktur von Software nach der
IODA-Architektur [4] (Bild 18)
www.dotnetpro.de 11.2024 55
004466--005577__SSlleeeeppyyHHoollllooww__eeaa22..iinndddd 5555 3300..0099..2244 0099::5544


---


<!-- Page 11 of 12 -->


PLANUNG Sleepy Hollow
Die Ebenen der Integration im Sleepy-Hollow-
Architekturmuster (Bild 19)
Requests. „Interactor“ nenne ich diese Integrationen, weil Unit-Tests auf Domäne, Providern und Pre-/Post-Proces-
sie die Reaktionen auf die „Reize“ des Benutzers imple- sing. Unit-Tests, weil diese Module (zumindest auf der
mentieren. Sie repräsentieren die Interaktionen mit der „Flughöhe“ von Bild 19) keine Abhängigkeiten mehr auf-
„treibenden“ Umwelt. Dass die UI-Technologie hier abwe- weisen.
send ist, tut dem keinen Abbruch; sie ist nur ein Detail. In-
teractors veröffentlichen eine oder mehrere transform()- Selbstverständlich gilt für alle hier gezeigten Module, dass
Funktionen. sie weiter differenziert werden können. Ich will nicht sugge-
Die Processor-Integrationen schließlich veröffentlichen eine rieren, dass Sie zum Beispiel Ihre ganze Domänenlogik in ei-
oder mehrere process()-Funktionen, die an der Spitze der ne Klasse „Domain“ verpacken. Sie können, sollen und müs-
Integration von Domänenfunktionalität mit Providern steht. sen alle Aspekte geeignet auf mehrere Module aufteilen.
Hier wird das eigentliche Verhalten der Software produ- Das Architekturmuster macht nur einen allgemeinen Vor-
ziert. „Hier spielt die Musik.“ schlag für die grundsätzliche und minimale Differenzierung
inklusive Definition der Abhängigkeitsverhältnisse.
Diese Modularisierung bietet schon auf dieser allgemeinen
Fazit
Ebene einige Ansatzpunkten für automatisierte Tests (Bild 20):
Akzeptanztests auf Interactors, Testbarkeit ist der entscheidende Treiber für die Modulari-
Integrationstests auf Processors, sierung. Ausgehend von dieser Überzeugung habe ich das
Die Ansatzpunkte für Tests nach
Sleepy Hollow (Bild 20)
56 11.2024 www.dotnetpro.de
004466--005577__SSlleeeeppyyHHoollllooww__eeaa22..iinndddd 5566 3300..0099..2244 0099::5544


---


<!-- Page 12 of 12 -->


Sleepy-Hollow-Architekturmuster entwickelt. Noch vor jeder
anderen Architekturempfehlung legt es Ihnen nahe, zumin-
dest Head-Logik, die abhängig ist von UI-Technologie, und
Body-Logik, die davon unabhängig ist, durch eine Schnitt-
stelle zu trennen.
An dieser Schnittstelle können Sie Akzeptanztests anset-
zen. Hier manifestieren sich die Anforderungen des Product HANDS-ON-WORKSHOPS
Owners (PO) formal in Form von Testfällen, die Sie automati-
UND WEITERBILDUNG FÜR
siert jederzeit durchspielen können.
SOFTWARE-ENTWICKLER UND
Sleepy Hollow dient damit auch der Dokumentation Ihrer
Software. Was ist möglich? Welche Requests führen zu wel- -ARCHITEKTEN
chen Responses? TRAININGS
Mit einem vom Head getrennten Body können Sie gezielt
Experimente anstellen: Wie reagiert Ihre Kreation in unter-
Soft ware qua lität
schiedlichen Situationen? (Vielleicht wäre auch „Franken-
be ur tei len und ver bes sern
stein Architecture“ ein passender Name gewesen?)
In meiner Erfahrung macht die Anforderungsanalyse mit Trainer: David Tielke
Slicing mit dem Ziel einer Sleepy-Hollow-Modularisierung
die Gespräche mit POs geradliniger und konkreter. Sie wis-
sen erstens genau, worauf alles hinauslaufen muss. Sie wis-
Async and Await
sen zweitens, dass Sie die Erfüllung der Anforderungen je-
in der Praxis
derzeit selbst überprüfen können. ◾
Trainer: Christian Giesswein
[1] Clean Code Developer Wiki,
www.dotnetpro.de/SL2411SleepyHollow1
[2] Ralf Westphal, Logic Makes the Software Turn Around, Neuerungen bei C#,
www.dotnetpro.de/SL2411SleepyHollow2 .NET & SQL-Server & CoPilot
[3] Ralf Westphal, Functional Dependencies,
Trainer: Thorsten Kansy
www.dotnetpro.de/SL2411SleepyHollow3
[4] Ralf Westphal, Strukturiert zerlegen, dotnetpro 4/2024,
Seite 42 ff., www.dotnetpro.de/A2404Slicing
Einstieg in Angular für
[5] Ralf Westphal, Inkremente innerhalb von Interaktionen
finden, dotnetpro 9/2024, Seite 32 ff., .NET-Entwickler
www.dotnetpro.de/A2409Slicing Trainer: Patrick Schnell
[6] Ralf Westphal, IODA Architecture,
www.dotnetpro.de/SL2411SleepyHollow4 NEU!
[7] Ralf Westphal, Principle of Mutual Oblivion (PoMO),
Testen mit Playwright
www.dotnetpro.de/SL2411SleepyHollow5
Trainer: David Pinezich
[8] Ralf Westphal, Radical Object-Orientation,
www.dotnetpro.de/SL2411SleepyHollow6
[9] Jimmy Bogard, Vertical Slice Architecture,
www.dotnetpro.de/SL2411SleepyHollow7 .NET MAUI –
[10] Milan Jovanovic, Vertical Slice Architecture, Cross-Plattformentwicklung
www.dotnetpro.de/SL2411SleepyHollow8
leicht gemacht
[11] Ralf Westphal, Integration Operation Segregation
Trainer: Sebastian Seidel
Principle, www.dotnetpro.de/SL2411SleepyHollow9
How to make teams awesome –
Ralf Westphal
ist Trainer, Berater und Mitgründer der Clean Gruppen zu Teams machen
Code Developer Initiative (https://clean-code- Trainer: Janosch Felde
developer.de). Seine Schwerpunkte sind dauer-
haft hohe Produktivität für die Softwareent-
wicklung und zukunftsfähige Teamorganisation. REMOTE
https://ralfw.de TRAININGS MÖGLICH!
dnpCode A2411SleepyHollow
developer-academy.de
Ihre Ansprechpartnerin: Susanne Herl
www.dotnetpro.de 11.2024 +49 731 88005-8835 • susanne.herl@ebnermedia.de
004466--005577__SSlleeeeppyyHHoollllooww__eeaa22..iinndddd 5577 3300..0099..2244 0099::5544
ddnnpp--11112244__DDeevvAAccaaddeemmyy__AAZZ__TTrraaiinniinngg__110022xx229977..iinndddd 7755 2255..0099..2244 1100::3311


| HANDS-ON-WORKSHOPS
UND WEITERBILDUNG FÜR
SOFTWARE-ENTWICKLER UND
-ARCHITEKTEN
TRAININGS
Soft ware qua lität
be ur tei len und ver bes sern
Trainer: David Tielke
Async and Await
in der Praxis
Trainer: Christian Giesswein
Neuerungen bei C#,
.NET & SQL-Server & CoPilot
Trainer: Thorsten Kansy
Einstieg in Angular für
.NET-Entwickler
Trainer: Patrick Schnell
NEU!
Testen mit Playwright
Trainer: David Pinezich
.NET MAUI –
Cross-Plattformentwicklung
leicht gemacht
Trainer: Sebastian Seidel
How to make teams awesome –
Gruppen zu Teams machen
Trainer: Janosch Felde
REMOTE
TRAININGS MÖGLICH! |
| --- |
| developer-academy.de
Ihre Ansprechpartnerin: Susanne Herl
+49 731 88005-8835 • susanne.herl@ebnermedia.de |



| HANDS-ON-WORKSHOPS
UND WEITERBILDUNG FÜR
SOFTWARE-ENTWICKLER UND
-ARCHITEKTEN
TRAININGS |  |
| --- | --- |
| UND WEITERBILDUNG FÜR
SOFTWARE-ENTWICKLER UND
-ARCHITEKTEN
TRAININGS |  |
|  |  |
| Soft ware qua lität
be ur tei len und ver bes sern
Trainer: David Tielke
Async and Await
in der Praxis
Trainer: Christian Giesswein
Neuerungen bei C#,
.NET & SQL-Server & CoPilot
Trainer: Thorsten Kansy
Einstieg in Angular für
.NET-Entwickler
Trainer: Patrick Schnell
NEU!
Testen mit Playwright
Trainer: David Pinezich
.NET MAUI –
Cross-Plattformentwicklung
leicht gemacht
Trainer: Sebastian Seidel
How to make teams awesome –
Gruppen zu Teams machen
Trainer: Janosch Felde |  |



![A2411SleepyHollow_p12_024](A2411SleepyHollow_images/A2411SleepyHollow_p12_024.png)



![A2411SleepyHollow_p12_026](A2411SleepyHollow_images/A2411SleepyHollow_p12_026.png)
