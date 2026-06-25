<!-- Page 1 of 8 -->


PLANUNG IODA
IODA-ARCHITEKTUR, TEIL 1
Eine Kritik bisheriger
Architekturmodelle
Vom Monolithen über Schichten hin zu IODA (Integration, Operation, Daten, APIs).
Ich kann sie nicht mehr hören: wortliste bestimmt. Der Text wird
die Anpreisungen des Architek- entweder vom Benutzer eingege-
turmusters „Schichtenmodell“. In ben oder aus einer Datei gelesen,
der dotnetpro wie anderswo spukt die der Benutzer beim Programm-
es immer wieder als klassische start angibt.
und deshalb gute Organisation Das ist eine simple Aufgabe,
von Code herum. Mir scheint das denke ich. Dennoch ist alles drin,
inzwischen ein Fall von Cargo- was eine Software ausmacht: ein
Kult: Irgendwer hat irgendwann bisschen Benutzerschnittstelle,
seinen Code so strukturiert und ein bisschen Fachlogik, ein biss-
damit einen Vorteil erlangt – und chen Datenzugriff. Genug, um
nun folgen ihm Generationen von darauf das Schichtenmodell und
Entwicklern blind. andere Strukturierungsideen an-
Was aber, wenn sich die Welt zuwenden. In diesem Beispiel
weitergedreht hat? Was, wenn geht es nicht um Technologien.
man da etwas mechanisch tut, oh- Eine Konsolenanwendung reicht
ne wirklich konsequent über die völlig aus. Deren Anwendung
ursprünglichen Beweggründe könnte so aussehen:
nachzudenken? Das Ergebnis ist Eine funktionale Lösung mit kaum vorhandener
dann immer gleich: Es entsteht Struktur (Bild 1) $ wordcount.exe
Unwohlsein, die Dinge werden Text eingeben: Es blaut die
schwierig – doch man weiß nicht Nacht, die Sternlein blinken
so recht, warum. Man macht doch alles richtig, oder? Eher 6 Wörter, davon 5 verschieden
wohl nicht; vielleicht muss man sich einfach noch mehr be- $ wordcount.exe gedichtanfang.txt
mühen. Also die Anstrengungen verdoppeln, das Muster ein- 6 Wörter, davon 5 verschieden
zuhalten. Und so entsteht dann noch mehr Unwohlsein. $
„Been there, done that, got the t-shirt“, kann ich dazu sa-
gen. Einst war auch ich ein Anhänger des Schichtenmodells Der eingegebene Text hat zwar sieben Wörter, doch das Wort
und seiner mustergültigen Geschwister. Doch irgendwann „es“ steht in der Stoppwortdatei und wird deshalb nicht ge-
habe ich für mich realisiert: Der Schmerz ist größer als der zählt. Außerdem steht „die“ im Text zweimal, daher unter-
Nutzen. Ich muss die Muster nicht besser anwenden, sondern scheidet sich die Zahl der Wörter von der der verschiedenen.
andere Wege suchen, meine Software zu strukturieren. Sie können ja mal als Fingerübung selbst für die Challenge
Worauf ich dann gestoßen bin, davon möchte ich Ihnen hier ein Programm schreiben. Beobachten Sie sich dabei: Wie ge-
berichten. Es ist eine Geschichte der Erleichterung. Soft- hen Sie vor? Wie strukturieren Sie den Code und warum?
wareentwicklung macht mir wieder Spaß. Ich kann mich viel Wenn Sie mitmachen und später vergleichen möchten,
mehr auf die Lösung der Probleme konzentrieren, weil die dann lesen Sie erst einmal nicht weiter – Spoileralarm! Denn
Struktur mich nicht mehr in ein hinderliches Korsett zwängt. ich möchte Ihnen verschiedene „hoch entwickelte“ Lösun-
Aber der Reihe nach. Lassen Sie mich noch vor dem Mus- gen vorstellen, um daran zu zeigen, warum das Schichtenmo-
terspuk beginnen. dell und Verwandte keine Option mehr für mich sind.
Aber zuerst eine Lösungsvariante, wie sie gar nicht mehr
Am Anfang war der Monolith
geht. Oder wie sie häufig noch anzutreffen ist? Entscheiden
Hier ist eine Challenge: Schreiben Sie ein Programm, das die Sie, ob Ihnen Code wie in Bild 1 immer noch begegnet.
Gesamtzahl der Wörter sowie die Zahl der verschiedenen Den Code bezeichne ich als monolithisch: Er besteht nur
Wörter in einem Text unter Berücksichtigung einer Stopp- aus Logik. Rekombinierbare Strukturelemente wie Funktio-
24 8.2018 www.dotnetpro.de


---


<!-- Page 2 of 8 -->


PLANUNG IODA
Das Schichtenmodell
definiert verständliche
Verantwortlichkeiten in
klaren Beziehungen (Bild 3)
So kann kein Fluss des Verständnisses entstehen. Der Code
„erzählt keine Story“, in der etwas entlang einer Kausalket-
te passiert. Es fehlen Bedeutungseinheiten, die Sie auf einen
Blick erfassen können. Alles müssen Sie sich durch Simula-
tion der Ausführung der Anweisungen erst erschließen.
Das ist gruselig aufwendig und fehlerträchtig. Und ob der
Unstrukturierter Code ist ein Flickenteppich aus Verantwortlich- Code wirklich korrekt ist, lässt sich nicht ermitteln, ohne ihn
keiten (Bild 2) manuell auszuführen. Keine der Verantwortlichkeiten kann
gezielt mit automatisierten Tests überprüft werden. So lässt
sich nicht zügig feststellen, ob der Code schon reif zur Aus-
nen oder Klassen sind vernachlässigbar. Die Anweisungen in lieferung ist oder nach einer Änderung immer noch korrekt,
der einzigen Funktion Main(), das heißt die Logik, tun zwar also regressionsfrei.
das, was sie tun soll – das Programm ist funktional –, doch ver- So geht’s nicht. Da sind wir uns einig, hoffe ich.
ständlich oder testbar ist diese Funktion nicht. Aber das war die Situation – zumindest früher, auch noch
Sicher, das sind kaum 50 Zeilen. Die zu verstehen sollte nach Einführung der strukturierten Programmierung. Vor
doch kein Problem sein. Warum hier mehr Aufwand mit mehr diesem Hintergrund sind die ersten Architekturmuster ent-
Struktur treiben? standen. Zunächst Model-View-Controller (MVC), dann das
Erstens ist das hier ein Beispiel mit überschaubarer Funk- Schichtenmodell. Was für ein Sonnenaufgang über dem Mo-
tionalität, um eben Strukturierungsansätze zu demonstrieren. nolithen!
Selbst wenn das später ein bisschen künstlich und nach Over-
Den Monolithen in Schichten spalten
engineering aussehen sollte, wird es hoffentlich helfen, die
wesentlichen Punkte zu illustrieren, um die es mir geht. MVC, Schichtenmodell, Hexagonale Architektur und auch
Zweitens glaube ich, dass wir sensibler sein sollten, was die die Clean Architecture verfolgen alle denselben Ansatz:
Strukturierung angeht. Wir sollten uns nicht überschätzen in Sie definieren einen Kanon von Verantwortlichkeiten und
der Fähigkeit, Code zu verstehen. Die Zeit für einen Bugfix verordnen die Spaltung der Logik nach diesen Verantwort-
oder zum Einbau einer Erweiterung ist immer knapp. Jede lichkeiten in Module.
Minute, die wir beim Verstehen von Code sparen können, be- Sie geben genau vor, wie die Module in Beziehung stehen,
vor wir ihn verändern, ist wichtig. Dafür aber müssen wir vor- das heißt, wie sie einander kennen und nutzen dürfen.
her, schon beim Schreiben, etwas tun. Der Code-Autor muss
an den späteren Code-Leser denken: „Programs must be Die Beliebtheit des Schichtenmodells scheint mir hierbei in
written for people to read, and only inciden- einer Kombination aus leicht zu verstehen-
tally for machines to execute.“ [1] den Verantwortlichkeiten in angenehmer
Was aber macht den Code in Bild 1 so Granularität und sehr klaren Beziehungen
schwer zu verstehen? Es ist die kunterbunte begründet zu sein (Bild 3).
Vermischung von Verantwortlichkeiten. Wenn ich dieses Muster auf den bisheri-
In Bild 2 habe ich die wesentlichen Verant- gen Code zur Lösung der obigen Challenge
wortlichkeiten farbig hervorgehoben. Sie anwende, dann ist damit tatsächlich etwas
sehen, das ist ein Flickenteppich. Verant- gewonnen: Verständlichkeit. Die Logik liegt
wortlichkeiten sind über die Logik verstreut. nicht mehr auf einem Haufen, sondern ist
Sie werden mit Kontrollstrukturen „geöff- verteilt auf Klassen als Module, sodass sich
net“, um dann andere dazwischenzuschie- Schichten steigern die Übersicht- schon beim Betrachten des Projekts eine ge-
ben und sie erst später zu „schließen“. lichkeit (Bild 4) wisse Übersicht einstellt (Bild 4). ▶
www.dotnetpro.de 8.2018 25


---


<!-- Page 3 of 8 -->


PLANUNG IODA
Wer mit dem Schichtenmodell ver-
traut ist, erkennt hier Verantwortlich-
keiten, unter denen er sich etwas vor-
stellen kann. Zudem sind dem Be-
trachter sofort die grundsätzlichen Be-
ziehungen klar. Das ist auch der Sinn
der Einhaltung eines solchen Musters.
Bild 5 zeigt konkret die Schichtung
der Klassen der Umsetzung aus Bild 4.
Ordentlich, oder? Eine so organisierte
Codebasis macht Freude. Alles hat
seinen Platz. Da wissen Sie genau, wo
was passiert. Ja, damit ist etwas ge-
wonnen. Es ist besser als vorher, aber
noch nicht wirklich gut. Denn schau- Konkrete Schichtung der
en Sie sich einmal den Code der Busi- Anwendungslogik (Bild 5) Schlecht testbare Logik trotz Schichtung (Bild 6)
nesslogik an (Bild 6).
Die Verantwortlichkeiten sind sau-
ber getrennt, die Abhängigkeiten ausgerichtet – doch gut Wenn Bild 1 den Bewusstseinsstand in Sachen Anwen-
testbar ist deshalb die eigentliche Businesslogik immer noch dungsarchitektur bis Mitte der 1990er-Jahre in vielen Projek-
nicht. Denn die Businesslogik hängt immer noch von der Da- ten widerspiegelt, dann steht Bild 6 für Ende der 1990er.
tenzugriffslogik ab. Es besteht eine funktionale Abhängig-
Schichten entkoppeln
keit: Logik in einer Methode ruft eine andere Methode auf,
um zwischendurch deren Logik auszuführen. In einer Co-Evolution mit bewussterer Anwendungsstruktu-
Das hört sich normal an und findet sich bestimmt in Ihrem rierung befand sich ab Ende der 1990er-Jahre das Thema
Code auch allerorten. Doch das macht es nicht besser. Solche Testen. Die ersten Unit-Testing-Frameworks kamen auf.
funktional abhängige Logik ist schlicht nicht für sich allein Wo klare Verantwortlichkeiten in Modulen freigestellt wa-
testbar. ren, konnten überhaupt erst automatisierte Tests feingranu-
Natürlich ist die Logik in Bild 6 auch in anderer Hinsicht lar ansetzen. Aber um in einer sauberen Hierarchie automa-
noch suboptimal. Doch das ist sekundär für den Punkt, um tisierte Tests punktgenau nur gewisse Logik testen lassen zu
den es mir hier im Moment geht. Ich habe nur das minimal können, brauchte es Entkopplung der Verantwortlichkeiten.
Nötige getan, um den monolithischen Code nach dem Schich- Auftritt DIP: Mit dem Dependency Inversion Principle wur-
tenmodell zu strukturieren. Das fundamentale Pro blem des de es möglich, Tests auf eine Schicht zu fokussieren.
Schichtenmodells geht nicht weg, wenn ich die Wortzäh- Der Trick besteht darin, Compilezeitabhängigkeiten von
lungslogik noch weiter refaktorisiere. Der Klumpen in Count_ Laufzeitabhängigkeiten zu trennen. Zur Compilezeit besteht
words() dient also der Unterstreichung des grundsätzlich zu nach DIP keine direkte funktionale Abhängigkeit von Logik
lösenden Problems der funktionalen Abhängigkeiten. einer Schicht zu Logik einer anderen. Eine obere Schicht
Wer die Businesslogik testen will, kann das im Moment hängt nicht von einer konkreten unteren ab, sondern ledig-
trotz – oder wegen – Schichtenmodell nur tun, indem er eben- lich von einer Abstraktion (Bild 7).
falls die Logik der Datenzugriffsschicht ausführt. Das macht Abstraktionen sind gewöhnlich Interfaces. Die können von
einen Businesslogik-Test langsamer und/oder umständlicher, der niedrigen Schicht implementiert werden – aber man kann
weil eine Datei als Ressource bereitgestellt werden muss. auch eine Attrappe für eine niedrige Schicht so aussehen las-
Nicht wirklich dramatisch in diesem trivialen Beispiel, doch sen. Doch eins nach dem anderen. Zuerst zeigt Bild 8 die An-
wenn Sie sich das Szenario umfangreicher denken, kommt wendung mit verbesserter Schichtenarchitektur im Über-
schon einiges an Overhead zusammen. blick. Der geübte Softwerker lässt beim Anblick dieser Mo-
dule sogleich vor seinem geistigen Au-
ge ein Beziehungsgeflecht wie in Bild 9
entstehen und weiß: Alles hübsch ent-
koppelt und testbar. In Bild 10 sehen Sie,
wie mit einer Attrappe die Businesslo-
gik unabhängig von darunterliegenden
Details getestet wird. Statt einen Daten-
zugriff konkret zu durchlaufen, werden
die Stoppwörter im Test hart verdrahtet.
Das ist trivial in puncto Laufzeit und
Komplexität und einfacher, als eine
Mit dem DIP werden Schichten entkoppelt (Bild 7) Stoppwortdatei zu benutzen.
26 8.2018 www.dotnetpro.de


---


<!-- Page 4 of 8 -->


PLANUNG IODA
Eine Schichtenarchi-
tektur mit DIP (Bild 8)
Injizieren der konkreten Implementation einer abstrakten
Abhängigkeit zur Laufzeit (Bild 11)
Mit einer Attrappe wird das Testen von abhängiger Logik einfach
Über Interfaces entkoppelte Schichten (Bild 9) (Bild 10)
Dass der Businesslogik überhaupt eine Attrappe unterge- bekannt ist, dann ist es MVC oder das Schichtenmodell. Zu-
schoben werden kann, liegt an der Anwendung des Prinzips sätzlich wird dann noch die Fahne der SOLID-Prinzipien
Inversion of Control (IoC). Dessen Manifestation besteht hier hochgehalten, zu denen das DIP gehört, sowie das SRP (Sin-
im Hineinreichen der Laufzeitabhängigkeit in die Business- gle Responsibility Principle), das sich mit Verantwortlichkeits-
logik durch ihren Konstruktor (Constructor Injection, Bild 11). trennung befasst. Nur leider sehe ich auch bei den Teams, die
Die Abhängigkeit vom Interface IDataaccess zur Compile- Code SOLID-gemäß in Schichten strukturieren, keine ent-
zeit wird zur Laufzeit durch die Injektion einer Implementa- spannten oder freudvollen Gesichter. Der Code ist immer
tion des Interfaces befriedigt. In Bild 12 sind die Compilezeit- noch schwer zu wandeln. Sonst würde man mit mir ja auch
und Laufzeitabhängigkeiten zusammen visualisiert. Das nicht über Clean Code Development sprechen wollen.
sieht jetzt schon nicht mehr so einfach aus wie das ursprüng- Wie kann das aber sein? Trotz sauberer Schichtung immer
liche Schichtenmodell, würde ich sagen. Logik ist auch im noch nicht sauber? Merkwürdig, oder?
Schichtenmodell bei vortrefflicher Ausrichtung der Bezie-
Schichten in Schale werfen
hungen immer noch funktional abhängig. Um trotz dieser Ab-
hängigkeiten Testbarkeit zu erlangen, müssen zusätzliche Dass daran irgendetwas faul ist, ist denn auch der Branche
Elemente eingeführt werden: Abstraktionen (hier: Inter- schon bewusst geworden. Seit 2005 hat sich das Schichten-
faces). Und aus einer Menge unidirektionaler Abhängigkei- modell gewandelt. Aus den Schichten sind Schalen der einen
ten werden zwei Mengen, von denen eine auch noch gegen- oder anderen Art geworden. Statt aus Kästchen bestehen ▶
läufige Abhängigkeiten enthält.
Das scheint der Preis der Wandelbarkeit zu sein. Verständ-
lichkeit entsteht durch Trennung von Verantwortlichkeiten
und klare Beziehungen. Testbarkeit entsteht durch DIP und
IoC. Ist eben so. Da müssen wir durch. Um das Leben aber
nun wenigstens ein bisschen einfacher zu machen, gibt es
Mock-Frameworks wie Moq (wie in Bild 10 benutzt) und De-
pendency-Injection-Frameworks wie MEF oder Unity.
Jetzt ist es nur noch eine Sache konsequenter Anwendung
von Prinzipien und Werkzeugen, um sauberen Code zu
schreiben. Zur grundlegenden Strukturierung von Logik
scheint damit alles gesagt. Das ist zumindest der Stand des
Bewusstseins, den ich bei Clean-Code-Development-Trai- Mit DIP unterscheiden sich die Abhängigkeiten zur Compilezeit
nings der CCD School oft sehe. Wenn ein Architekturmuster und zur Laufzeit (Bild 12)
www.dotnetpro.de 8.2018 27


---


<!-- Page 5 of 8 -->


PLANUNG IODA
Konzentrische Architekturmuster (Bild 13) Konzentrische Abhängigkeiten ergeben mehr Sinn (Bild 14)
die empfohlenen Architekturmuster nun aus konzentrischen Bild. Von außen nach innen, also in Richtung der Abhängig-
Kreisen. Verantwortlichkeiten sind ineinander organisiert keiten, wird Code immer „ruhiger“. Robert C. Martin sagt in
statt übereinander. Vertreter solch konzentrischer Architek- seinem Buch Clean Architecture [2]: „The outer circles are
turmuster sind die Hexagonale Architektur, die Onion Ar- mechanisms. The inner circles are policies.“ „Mechanisms“,
chitecture und die Clean Architecture (Bild 13). also technische Vorrichtungen, sind demnach eher Änderun-
Treiber für diese neue Grundorganisation ist eine Bedeu- gen unterworfen als „Policies“ (Regeln). Für Martin definie-
tungsaufladung der Verantwortlichkeiten. Dass es dezidierte ren die Schalen Ebenen: „[T]he further in you go, the higher
Verantwortlichkeiten gibt und dass es eine klare Richtung für level the software becomes.“ Aber was für Ebenen? Was ist
Abhängigkeiten gibt, hat sich nicht verändert. In der konzen- das Kriterium, um eine Ebene zu bestimmen?
trischen Anordnung drückt sich vielmehr aus, dass man „As you move inward, the level of abstraction and policy
erkannt hat, dass nicht alle Verantwortlichkeiten gleich sind. increases.“ Die Ebene, auf der Regeln liegen, wächst nach in-
Irgendetwas ist anders mit dem, was im Kern steht, im Ver- nen. Und auch das Abstraktionsniveau wächst nach innen.
gleich zu dem, was am Rand steht. Jedenfalls für Robert C. Martin.
Ich hatte mich auch schon lange beim Schichtenmodell ge- Bei den Regeln gehe ich noch mit. Beim Abstraktionsni-
fragt, warum Businesslogik überhaupt von Datenzugriffslo- veau bin ich jedoch anderer Meinung. Dazu später mehr.
gik abhängig sein soll. Warum sollte sich eine Geschäftsregel In jedem Fall erweitern die konzentrischen Architektur-
damit befassen, Daten zu beschaffen oder zu speichern? Dass muster das Bild um eine Dimension. Das ist gut so. Verant-
die Businesslogik Daten braucht, auf denen sie arbeitet, und wortlichkeiten liegen nicht alle auf einer Ebene, egal was da-
Daten erzeugt, ist klar. Muss sie dafür aber den Datenzugriff für das Kriterium ist. Was bedeutet das jetzt für den Code?
selbst steuern? Mir will das nicht in den Kopf. Das sieht für Bild 15 zeigt meine Bemühung, das Muster der Clean Ar-
mich wie eine Vermischung von Verantwortlichkeiten aus – chitecture auf das bisherige Beispiel zu übertragen. Bemüht
auch wenn es irgendwie so ganz normal erscheint. habe ich mich, weil ich es Ihnen einerseits leicht machen
In den konzentrischen Architekturen ist dieses Problem ge- möchte, zu sehen, wohin die Verantwortlichkeiten aus Bild 8
löst – zumindest scheinbar. Denn in konzentrischen Architek- gewandert sind; meine Clean Architecture soll also vergleich-
turen weisen die Abhängigkeiten von außen bar sein. Andererseits wollte ich aber auch
nach innen auf die Businesslogik hin (Bild 14). nicht zu weit von den Begriffen bei Robert C.
Die Businesslogik steuert nun augenschein- Martin abweichen; die Umsetzung soll also
lich nicht mehr den Datenzugriff. auch mit dem Muster vergleichbar sein.
Das ergibt mehr Sinn, finden Sie nicht Am einfachsten ist es für Sie bestimmt, die
auch? Je weiter außen eine Schale, desto Schalen der Clean Architecture in Bild 15 zu
mehr beschäftigt sie sich mit technischen De- identifizieren. Von außen nach innen stehen
tails und desto volatiler ist sie. Je weiter im In- dafür die Projektverzeichnisse adapters,
neren eine Verantwortlichkeit, desto zentra- usecases, domain. Als Adapter verstehe ich
ler ist sie, im wahrsten Sinne des Wortes, des- die Klassen, die den Zugriff auf Hardware
to zeitloser und konstanter. kapseln, zum Beispiel Tastatur oder Festplat-
In der Clean Architecture (Bild 13) stehen te. Das sind Martins „Mechanisms“.
Entities für sehr allgemeine, grundlegende Im Kern steht für mich die Domäne, bei der
Regeln. „Enterprise Business Rules“ können ich nicht weiter unterscheide, ob es sich um
sich naturgemäß nicht so häufig und radikal Entities oder Services handelt (wenn ich ein-
ändern wie „Application Business Rules“ der mal das Vokabular aus dem Domain Driven
darum herum liegenden Use Cases. Design (DDD) in Anschlag bringe). Die Ver-
Die konzentrischen Architekturmuster ad- Code-Artefakte in einer Clean antwortlichkeiten Dataaccess und Business-
dieren also den Aspekt der Volatilität zum Architecture (Bild 15) logic haben sich auch nicht sehr verändert.
28 8.2018 www.dotnetpro.de


---


<!-- Page 6 of 8 -->


PLANUNG IODA
Zur Laufzeit ruft eine innere Schale eine äußere auf (Bild 18)
sondern von einer weiter außen liegenden Schale! Genauer:
Der Use Case beim Orchestrieren von Adaptern und Business- von der Klasse Dataaccess in adapters. IStopwords ist in do-
logik (Bild 16) main definiert, um der Forderung nach den Verweisen nach
innen zu genügen. Die äußere adapters-Schale hängt nun
ganz sauber von der inneren domain-Schale ab – obwohl im-
Allerdings ist der vormalige PresentationlogicLayer nun zer- mer noch Businesslogik sich die Stoppwörter selbst beschafft
fallen in Controller und Presenter. (Bild 18). Das Schichtenmodell war da aus meiner Sicht ehrli-
Die Benutzerschnittstelle besteht aus zwei Teilen, weil der cher. Dort verliefen die grundsätzlichen Abhängigkeiten von
Use Case neu hinzugekommen ist. Dieser ist in der Clean Ar- oben nach unten, so wie auch zur Laufzeit der Kontrollfluss.
chitecture ganz explizit und hat laut Martin folgenden Auf- In der Clean Architecture ist das nicht mehr der Fall!
trag: „These use cases orchestrate the flow of data to and from Vollziehen Sie das wirklich einmal anhand von Bild 15 und
the entities […]“ Dafür ist im vorliegenden Fall nicht viel zu Bild 18 nach. Lassen Sie es sich auf der Zunge zergehen. Neh-
tun, aber ich habe mich deshalb zum Beispiel entschlossen, men Sie Bild 17 zu Hilfe. Hier geht um den Kern der konzen-
aus der Businesslogik das Laden des Textes herauszunehmen trischen Architekturen! Das ist so wichtig, dass ich es Ihnen
(Bild 16). Außerdem: Der Use Case „schiebt“ das Ergebnis der aufmale. Zunächst die Compilezeitabhängigkeiten in Bild 19.
Wortzählung nun an einen Presenter weiter, statt es seinem Blicken Sie hier durch? Das ist alles wunderbar nach DIP ent-
Aufrufer – dem Controller – zurückzugeben. Das ist in der koppelt. Der Use Case ist nicht von einer Domänenimplemen-
Clean Architecture auch ganz explizit beschrieben (Bild 17). tation abhängig (Pfeil mit gefüllter Spitze), sondern nur von
Tatsächlich trägt das „Anhängsel“ der Clean Architecture einer Abstraktion. Ebenfalls von dieser abhängig ist ihre Im-
in Bild 17 wesentlich dazu bei, den Code gemäß der Forderung plementation (Pfeil mit offener Spitze), die Businesslogik.
„Alle Compilezeitabhängigkeiten weisen nach innen“ zu Ebenso ist es mit den anderen Implementationen, die in
strukturieren. Ihm ist es geschuldet, dass die Implementation Bild 19 alle in der oberen Zeile stehen: Keine Pfeile zwischen
in Bild 15 fünf Interfaces statt bisher drei hat und diese auch ihnen. Alle Pfeile weisen nach unten auf Abstraktionen.
noch auf zwei Ebenen definiert sind. Beispiel Schale domain: Aber nicht nur die größere Zahl an Interfaces macht das
Die umschließende Schale usecases kennt von der Domäne Bild hier verwirrender. Hinzu kommt noch die Zuordnung
nur das Interface IBusinesslogic, so wie der bisherige Presen- von Abstraktionen und Implementationen zu Schalen. Schau-
tationlogicLayer von der darunterliegenden Schicht auch nur en Sie genau, wie die Beziehung zwischen äußeren und in-
dieses Interface kannte. So weit, so einfach und naheliegend. neren Schalen wechselt. In Bild 20 zoome ich beispielhaft he-
Zusätzlich jedoch definiert die Schale domain das Interface ran. Der Controller in der äußeren Schale kennt nur IUseCase
IStopwords. Das zählt für mich zu einer anderen Kategorie, als Abstraktion der inneren Use-Case-Schale (1). Die Abstrak-
daher habe ich es in das Verzeichnis dependencies gesteckt. tion gehört zur inneren Schale, die sie auch implementiert.
IStopwords wird nicht von der Businesslogik implementiert, Gleichzeitig (!) ist die innere Schale von der Abstraktion IPre-
senter abhängig, die jedoch von der äußeren implementiert
wird (2). Verwirrend, oder? Jedenfalls empfinde ich das so. ▶
Der Use Case
leitet Output über
einen Port weiter
an die umliegende
Adapter-Schale
(Bild 17)
Die Abhängigkeiten gemäß DIP in der Clean Architecture (Bild 19)
www.dotnetpro.de 8.2018 29


---


<!-- Page 7 of 8 -->


PLANUNG IODA
Schicht war gut testbar, weil sie für sich stand. Die Logik in
den darüberliegenden Schichten konnte zwar grundsätzlich
schon gezielt angesprochen werden, nur müsste dann auch
immer die Logik darunterliegender Schichten beim Test mit
durchlaufen werden. Das kostet Zeit, und das macht es nicht
leicht, einen Bug zu lokalisieren.
Die Testbarkeit ist dann in der zweiten Variante des Schich-
tenmodells (Bild 8 und Bild 9) nachgezogen worden. Durch
Anwendung von DIP und IoC können für Tests untere Schich-
ten ausgeblendet werden. Wenn etwas schiefgeht, dann weiß
Zur Compilezeit hängt die äußere von der inneren Schale ab man, dass der Fehler in der Logik der zu testenden Schicht
(Bild 20) steckt. Allerdings: Dieser Fortschritt in der Testbarkeit hat
seinen Preis. Der wird deutlich in der Clean-Architecture-Va-
riante (Bild 15 und Bild 19). DIP und IoC addieren Komplexität,
Und Robert C. Martin gibt in seinem Buch für ein ähnliches die die Verständlichkeit nun – zumindest nach meinem Emp-
Beispiel zu: „Much of the complexity in that diagram was in- finden – massiv reduziert. Man ist über das Ziel hinausge-
tended to make sure that the dependencies between the com- schossen. „Mehr vom selben“ (hier: DIP und IoC) hat den
ponents pointed in the correct direction.“ Fortschritt, den die zweite Variante des Schichtenmodells ge-
Bitte lesen Sie das Zitat noch einmal! Komplexität ist der bracht hat, nicht vergrößert. Im Gegenteil!
Feind einfacher Wandelbarkeit. Clean-Code-Prinzipien und Aber wie kommt das? Ich glaube, es liegt daran, dass man
-Praktiken sollten sich also darum bemühen, Code-Komple- zu sehr auf die Compilezeitabhängigkeiten gestarrt hat.
xität zu reduzieren. Und als Beispiel für Sauberkeit gilt dann Von der Schichtung zur Konzentrik überzugehen hat etwas
ein Architekturmuster, über das der Pate der Clean-Code-Be- mit den Compilezeitabhängigkeiten zu tun. Im Schichtenmo-
wegung sagt, es sei komplex, damit Abhängigkeiten in eine dell war das Volatile (oder Instabile) – Robert C. Martins „Me-
gewisse Richtung weisen? Komplexität für Sauberkeit? chanisms“ – nicht konsequent in einer Position, wo Verände-
Ich muss sagen, dass ich nicht bereit bin, das zu akzeptie- rungen wenig Probleme machen. Relativ problemlos sind
ren. Diesen Preis möchte ich nicht bezahlen. Wandelbarkeit Veränderungen nämlich dort, wovon nur wenige oder keine
in Form von Verständlichkeit und Testbarkeit möchte ich Codeeinheiten abhängig sind. Im Schichtenmodell ist das nur
nicht dadurch bekommen, dass ich Komplexität bewusst in für die Präsentationslogik der Fall. Die Datenzugriffslogik
diesem Ausmaß erhöhe. Ich habe es bei der Implementation hingegen, die ebenfalls ein „Mechanism“ ist, muss – wegen
des Beispiels als Clean Architecture schon bemerkt, und nun, der Abhängigkeit anderer von ihr – Stabilität zusichern. Das
als ich Bild 19 erarbeitet habe, ist es mir noch deutlicher ge- wurde mit der Clean Architecture bewusst verändert. Dort
worden: Was in konzentrischen Kreisen noch klar aussieht sind nicht nur die Abhängigkeiten sauber ausgerichtet, son-
und eine simple Regel definiert – „Abhängigkeiten weisen dern auch die Verantwortlichkeiten nach Stabilität positio-
immer nach innen“ –, verliert diese Eigenschaften im Code. niert: Am stabilsten sind ganz allgemeine, grundlegende Re-
Die Krone wird dem aufgesetzt, wenn Sie sich klarmachen, geln im Kern, am instabilsten die Kommunikation mit der
wie die Laufzeitabhängigkeiten aussehen (Bild 21). Die wei- Umwelt in der äußeren Schale.
sen nämlich von außen nach innen und dann wieder nach au- Diese Sichtweise gefällt mir – allerdings hat die Implemen-
ßen. Das gute alte Schichtenmodell ist zu- tation eben einen hohen Preis. Bild 17 und
rück. Wofür also die Steigerung der Komple- Bild 20 machen es exemplarisch deutlich; die
Wir suchen zum nächstmöglichen Zeitpunkt
xität? Was ist wirklich gewonnen durch die Verständlichkeit der Zusammenhänge im
am Standort Nürnberg einen
konzentrischen Architekturmuster? Code sinkt.
Aber selbst wenn ich einmal über den
Reflexion
auch von Robert C. Martin beklagten Mehr-
Früher war nicht alles besser. Codezustände aufwand hinwegsehe, frage ich mich, was Web-Entwickler (m/w) ASP.NET, C# und JavaScript
wie in Bild 1 will niemand (wieder) haben. wirklich gewonnen ist. Denn Bild 21 zeigt ein
Die erste Variante des Schichtenmodells Bild, das sich im Grunde nicht vom Schich-
jedoch, die war gar nicht so schlecht. Die kla- tenmodell unterscheidet. Zur Laufzeit ist
Ihr Profil Ihre Aufgaben
re Trennung von Verantwortlichkeiten, kom- eine Businesslogik immer noch vom Daten-
biniert mit einer konsequenten Ausrichtung zugriff abhängig. Was soll das? Da mag zur
Abgeschlossenes Universitätsstudium der Entwicklung unserer Software-Suite
der Abhängigkeiten, hat die Verständlich- Compilezeit die Abhängigkeit umgekehrt
Fachrichtung Informatik DeltaMaster unter Einsatz moderner
keit deutlich gesteigert (Bild 4 und Bild 5). sein – Adapter außen hängt von Domäne in-
Webtechnologien in agilen Entwicklungs-
Für gute Wandelbarkeit war das allerdings nen ab –, doch zur Laufzeit gehen die Aufru-
Erfahrung in der Entwicklung von Web- prozessen einschließlich Testing
noch nicht genug. Die braucht nicht nur Ver- Die Laufzeitabhängigkeiten fe dorthin durch die Domäne in die Tiefe. Es
anwendungen mit ASP.NET und JavaScript
ständlichkeit, sondern auch Testbarkeit. Die- zeigen in der Clean Architecture ist letztlich nichts gewonnen. Die Abstrak-
Jetzt online bewerben!
Jetzt bewerben unter jobs@bissantz.de
se war in der ersten Schichtenvariante noch von außen nach innen und tion, von der die Businesslogik abhängig ist, Fundierte Kenntnisse in der Oberflächen-
begrenzt. Lediglich die Logik der untersten wieder nach außen (Bild 21) ist lediglich verschoben worden. Vorher ge- gestaltung mit HTML und CSS
www.bissantz.de/jobs
30 8.2018 www.dotnetpro.de


|  |
| --- |
|  |
|  |



---


<!-- Page 8 of 8 -->


PLANUNG IODA
man je Klasse und je Interface eine Datei denkt). Das
einzig Positive, das ich der Clean Architecture abge-
sehen vom hübschen Bild abgewinnen kann, ist die
Tendenz zur Aufspaltung von Abstraktionen. Sie
scheint die Anwendung des Interface Segregation
Principle (ISP) nahezulegen. Schmalere Interfaces
helfen einfach bei der Entkopplung.
Wo vorher nur eine Präsentationslogikschicht und
eine Datenzugriffsschicht mit entsprechenden Ab-
straktionen waren, sind beide nun in mehrere Teile
Das vollständige Abhängigkeitsbild der implementierten Clean zerfallen: Controller und Presenter sind getrennt und
Architecture (Bild 22) es gibt IPresenter; ebenfalls getrennt sind IText und
IStop words, wo vorher nur IBusinesslogicLayer war.
Am Ende ist dieser positive Effekt für mich jedoch
hörte sie zur darunterliegenden Schicht (IDataaccessLayer in nicht ausschlaggebend. Viel wichtiger finde ich das Sinken
Bild 9), jetzt gehört sie zur Businesslogik selbst (siehe IStop- der Verständlichkeit durch eine gestiegene Artefaktzahl und
words in Bild 19). Dass nichts gewonnen ist, ist beim Testen den weiterhin hohen Testaufwand. Denn jede Laufzeitabhän-
deutlich zu bemerken. Das Architekturbild suggeriert, dass gigkeit ruft zur Testzeit nach einer Attrappe. ◾
eine innere Schale keine Abhängigkeit zu einer äußeren
hat – doch beim Testen stellt sich das Gegenteil heraus. In [1] Harold Abelson & Gerald Jay Sussman, Structure and
Bild 17 ist der Use Case Interactor – also Code der Use-Case- Interpretation of Computer Programs, MIT Press,
Schale – zur Laufzeit abhängig vom Presenter in der darüber- 2. Auflage, 1996, ISBN 978-0-262-51087-5
liegenden Schale. Dass der Use Case Output Port zur Use- [2] Robert C. Martin, Clean Architecture, A Craftsman’s
Case-Schale gehört, kaschiert das nur. Im Test muss trotzdem Guide to Software Structure and Design Clean Archi-
eine Attrappe gebaut werden. tecture, Prentice Hall, 2017, ISBN 978-0-1344-9416-6
Sind Sie noch da oder haben Sie schon halb abgeschaltet?
Das würde mich nicht wundern. Bei dem ganzen Hin und Her
der Abhängigkeiten von Compilezeit und Laufzeit kann Ralf Westphal
einem schon der Kopf schwirren. Ich jedenfalls verliere bei ist freiberuflicher Berater, Referent, Autor und
der Darstellung der vollständigen Abhängigkeiten der imple- Trainer für Themen rund um Softwarearchitek-
mentierten Clean Architecture den Überblick (Bild 22). tur und die Organisation von Softwareteams. Er
So sieht für mich ein Testalbtraum aus. Ganz zu schweigen ist Mitgründer von Clean Code Developer (CCD)
davon, dass damit das Rätselraten darum, für welche Klassen und propagiert kontinuierliches Lernen.
ein Interface definiert werden sollte, weiter angeheizt wird. info@ralfw.de
Im Zweifelsfall lautet dann die Antwort „Für alle!“, und da-
dnpCode A1808IODA
mit explodiert die Zahl der Dateien in einem Projekt (wenn
Wir suchen zum nächstmöglichen Zeitpunkt
am Standort Nürnberg einen
Web-Entwickler (m/w) ASP.NET, C# und JavaScript
Ihr Profil Ihre Aufgaben
Abgeschlossenes Universitätsstudium der Entwicklung unserer Software-Suite
Fachrichtung Informatik DeltaMaster unter Einsatz moderner
Webtechnologien in agilen Entwicklungs-
Erfahrung in der Entwicklung von Web- prozessen einschließlich Testing
anwendungen mit ASP.NET und JavaScript
Jetzt online bewerben!
Jetzt bewerben unter jobs@bissantz.de
Fundierte Kenntnisse in der Oberflächen-
gestaltung mit HTML und CSS
www.bissantz.de/jobs