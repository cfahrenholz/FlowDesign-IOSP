<!-- Page 1 of 4 -->


PLANUNG IODA
IODA-ARCHITEKTUR, TEIL 3
IODA am Beispiel
Die Wortzählung veranschaulicht die Anwendung der IODA-Architektur in der Praxis.
Nachdem die beiden vorangegangenen Artikel [1] und [2] nicht überlegen, wie Abhän-
einen so langen Ausflug in die Theorie unternommen ha- gigkeiten zur Compilezeit ver-
ben, kehren wir nun zurück zur Praxis. Sie fragen sich sicher, sus Laufzeit verlaufen.
wie denn eine Architektur ohne funktionale Abhängigkeiten Das soll nicht bedeuten, dass
überhaupt zu einem lauffähigen Programm führen kann. das DIP keinen Platz in einer
In Bild 1 sehen Sie deshalb die bereits bekannte Wortzäh- Anwendung nach IODA-Archi-
lung in einer IODA-Architektur. Kontrastierend zur Clean Ar- tektur hat. Obwohl es keine
chitecture ist darin vor allem Folgendes hervorhebenswert: funktionalen Abhängigkeiten
Die IODA-Architektur betont die Notwendigkeit der Kap- gibt, können auch dort manche
selung von APIs in Portalen und Providern. Deshalb habe Tests von einer derartigen Ent-
ich hier erstmals den Zugriff auf den Kommandozeilenpa- kopplung profitieren – und
rameter in einen eigenen Dialog herausgezogen: die Klas- Das Wortzählungs-Beispiel, zwar Tests von Integrationen.
se Commandline; sie verbirgt den Umgang mit dem „API“ strukturiert nach dem IODA- In diesem Beispiel habe ich
string[] args. Über die Kommandozeile teilt der Benutzer Architekturm uster (Bild 1) auf Interfaces aber ganz be-
der Anwendung etwas mit. Demgegenüber ist das UI für die wusst verzichtet, um den grund-
Kommunikation mit dem Benutzer per Standard-Input/- sätzlich anderen Ansatz der
Output zuständig. IODA- Architektur zu unterstreichen.
In einer IODA-Architektur sind die Operationen durch ge- Allerdings kommt das Prinzip Inversion of Control (IoC)
meinsame Daten verbunden (Bild 2). Sie legt damit nahe, zum Einsatz. Bei Adaptern ist es sehr wahrscheinlich, dass sie
sich darüber Gedanken zu machen und insbesondere die einmal (zum Beispiel in Tests) ersetzt werden müssen und al-
fließenden Daten durch eigene Datentypen auszudrücken. so ein Interface nützlich wäre. In Zukunft. Vielleicht. Deshalb
Das habe ich einmal exemplarisch mit WordCountResult sind Adapter auch keine statischen Klassen und veröffentli-
getan (vergleiche Bild 3). chen keine statischen Methoden. Und deshalb injiziere ich
Instanzen von Adaptern in die Integration. Damit sind Vorbe-
reitungen für einen späteren Einsatz des DIP getroffen, ohne
den Code dadurch allzu sehr zu verrauschen. Relevant ist das
ohnehin nur für die Integration, also im Controller (Bild 4).
Die Abhängigkeit des Controllers von einem API besteht
lediglich in der statischen Methode Main() mit dem args-Pa-
rameter. Die Integrationsleistung, die dieser Entry Point er-
bringt, besteht im Aufruf von Run(). Diese Funktion repräsen-
tiert auf höchster funktionaler Abstraktionsebene das gesam-
te Verhalten der Anwendung. Konkret genutzt wird das args-
API ohnehin erst im Dialog Commandline.
Operationen stehen über Daten in Kontakt (Bild 2) Main() selbst muss nicht automatisiert getestet werden.
Aber wenn ich das Anwendungsverhalten automatisiert tes-
ten wollte, würde es mir über die eine Funktion Run() zur Ver-
Der Eintritt in Anwendungen geschieht immer über Con- fügung stehen. In einem Test müsste ich den Konstruktor des
troller. Im Beispiel gibt es nur einen Entry Point, der mit ei- Controllers dann nur passend befüllen. Auch ohne Attrappen
ner gleichnamigen Klasse hervorgehoben ist. In bisherigen ist diese Möglichkeit nicht zu verachten. Aber wenn ich zum
Architekturmodellen sind Entry Points kein Thema. Beispiel in einem Test keine Benutzerinteraktion über ein UI
haben möchte, könnte ich nachträglich und unmittelbar be-
Vor allem erwähnenswert ist jedoch das, was fehlt. Haben Sie darfsgetrieben ohne großen Aufwand ein Interface IUI ein-
es bemerkt? In Bild 1 gibt es keine Interfaces! Der Code ge- führen. Die IODA-Architektur erlaubt mir, mit den Anforde-
mäß IODA-Architektur leidet nicht unter der zusätzlichen rungen zu wachsen. Sie dekretiert nicht von vornherein, dass
Komplexität, die das Dependency Inversion Principle (DIP) und wo ich Interface-Abstraktionen einziehen muss. Komple-
erzeugt. Er ist damit schon auf dieser Ebene viel verständli- xität durch kategoriale Abstraktionen ist nicht gesetzt und
cher, wie ich finde. Er ist weniger verrauscht. Sie müssen nicht modellimmanent, sondern richtet sich nach dem Bedarf.
40 10.2018 www.dotnetpro.de


---


<!-- Page 2 of 4 -->


PLANUNG IODA
Mit IoC wird die Integration behutsam auf
einen späteren eventuellen Einsatz von DIP
vorbereitet (Bild 4)
Eine Datenklasse verbindet Operationen (Bild 3)
Ein weiterer Unterschied der Implementation nach dem
IODA- Architekturmodell zeigt sich, wenn ich in die Klassen
hineinzoome. Da ist erstens der Controller, der gar keine Lo-
gik enthält (Bild 5). Er ist abgesehen von Main() ausschließlich
für die Integration zuständig. Er ist gewissermaßen eine Ab-
straktionsmaschine. Seine Methoden komponieren aus Tei-
len schrittweise etwas Umfassenderes, Abstrakteres – das an
der Spitze in Run() kulminiert.
Wie gesagt: Wenn das Problem umfänglicher wäre, hätte
ich diese Menge an Integration in eine eigene Klasse ausge-
lagert; doch für dieses Beispiel finde ich die Co-Lokation mit
dem Entry Point in Ordnung.
Dass ich auf diese Art und Weise mit der Integration umge-
he, ist andererseits auch wieder dem IODA-Architekturmo- Die Leistung des Controllers besteht vor allem in der Integration
dell geschuldet. Darin werden auf der grundlegenden Ebene (Bild 5)
(Bild 6) die Funktionen betont. Sie stellen das Verhalten her.
Sie können IODA gewissermaßen als Function-first-Ansatz
verstehen, bei dem die Abstraktion durch Komposition im egal, aber zweitrangig. Sollte die Anwendung wachsen, kann
Vordergrund steht. ich die integrierenden Methoden aus dem Controller leicht in
Wo die Funktionen in Klassen zusammengefasst werden eine andere Klasse verschieben.
(Abstraktion durch Kategorisierung), ist dann natürlich nicht Um die Integration allerdings auch in Entscheidungsfällen
logikfrei zu halten, ist ein Trick nötig. Bild 5 zeigt in hervorge-
hobenen Passagen, wo ich diesen Trick angewandt habe.
Im ersten Fall geht es um die Entscheidung, ob ein Text aus
einer Datei zu verarbeiten ist oder ob der Benutzer ihn ein-
gibt. Eine solche Entscheidung erfordert Logik: eine Transfor-
mation als Bedingung plus eine Kontrollanweisung. Damit
darf eine Integration nicht „kontaminiert“ werden. Solche
Logik muss in einer Operation stecken, um testbar zu sein.
Um dennoch ein alternatives Verhalten der Integration zu
erhalten, wird das Ergebnis der Entscheidung über Conti-
nuations (Funktionszeiger) aus der Operation herausgereicht
(Bild 7). Je nachdem, ob die Verarbeitung einer Datei (onFile)
oder einer Benutzereingabe nötig ist (onUser), wird die eine
oder andere Methode aufgerufen. Das ist für Sie sicher unge-
wohnt – aber es dient dem Grundsatz der IODA-Architektur:
Die zwei Ebenen der IODA-Architektur (Bild 6) Funktionale Abhängigkeiten sind zu vermeiden! ▶
www.dotnetpro.de 10.2018 41


|  |  |
| --- | --- |
|  |  |



---


<!-- Page 3 of 4 -->


PLANUNG IODA
Das Ergebnis einer Entscheidung gibt eine Operation über
Continuations bekannt (Bild 7) Nur Operationen rufen externe APIs auf (Bild 8)
Das Prinzip hat also Vorrang vor der Implementation. Das Doch nicht nur die Funktionshierarchie folgt dem IODA-
ist nicht anders als in der Clean Architecture. Dort führt es zu Modell. Auch die Klassen sind so strukturiert (Bild 10). Es gibt
einem Anstieg der Komplexität durch Interfaces. Hier führt eine Klasse mit der Verantwortlichkeit Integration, mehrere
es in manchen Fällen lediglich zur Nutzung des ungewohn- mit der Verantwortlichkeit Operation und auch eine Daten-
ten programmiersprachlichen Mittels Funktionszeiger. klasse.
Bitte lassen Sie hier jedoch aus einem Stirnrunzeln wegen Wenn Sie genau hinschauen, dann fällt ihnen jetzt aller-
mangelnder Gewohnheit keine Abneigung gegen die IODA- dings vielleicht eine Diskrepanz auf. Die Klasse Business logic
Architektur entstehen. Seien Sie versichert, dass es zu sol- ist ein Blatt im Klassendiagramm und also als operational ein-
chen Konstrukten nicht in allen Entscheidungsfällen kom- gestuft. Im Funktionsbaum sind hingegen nicht alle ihre Me-
men muss. Ich habe es hier lediglich zur Unterstreichung des thoden als Operationen eingetragen. Ihr Count_words() ist ei-
Prinzips gewählt. ne Integration (vergleiche Bild 3). Wie kann das sein?
Es ist eine Sache der Übung, Code wie den aus Bild 5 zu le- Die Lösung: Das IODA-Architekturmodell ist fraktal. Es
sen. Wenn Sie das ein paarmal getan haben, fällt es Ihnen kann eine IODA-Hierarchie innerhalb einer IODA-Hierar-
leicht. Das ist zumindest meine Erfahrung nach Jahren, in chie existieren (Bild 11).
denen ich so gearbeitet und es in Clean-Code-Development- Die Hierarchie aus Integration, Operation, Daten und APIs
Trainings vermittelt habe. Auch DIP und IoC waren am An- ist zwar zunächst auf Funktionen gemünzt. Dort gilt es, aus
fang ungewohnt in ihrer Manifestation im Code. Heute ge- der funktionalen Abhängigkeit hinauszukommen.
hen wir damit routiniert um – merken aber eben leider nicht Wenn Funktionen jedoch mit Modulen kategorisiert, das
mehr, welcher Overhead dadurch entstehen kann. heißt nach dem Zweck zusammengefasst werden, dann erge-
Ebenso ist es mit Continuations als Mittel, um Logik auf
Operationen zu beschränken. Wenn Sie heute damit anfan-
gen, ist es morgen Routine. Achtung: Das ist allerdings kein
Selbstzweck! Wichtiger als die Einhaltung des Prinzips ist im-
mer noch der eigentliche Zweck, nämlich Wandelbarkeit des
Codes durch Verständlichkeit und Testbarkeit zu erreichen.
Mehr dazu finden Sie in meinem Blog-Artikel unter [3].
Falls ein Spritzer Logik in einer Integration weder die Ver-
ständlichkeit noch die Testbarkeit spürbar beeinträchtigt, ist
die Logik dort verzeihlich. Doch das ist mir für die hiesige
Darstellung eigentlich schon zu differenziert. Deshalb habe
ich in der Beispielimplementation darauf verzichtet.
Struktur fraktal
Die Funktionshierarchie der IODA-Umsetzung folgt wieder
der Hierarchie aus Bild 8: integrierende Funktio nen über
Operationen über Daten (Bild 9). Funktionen in grünen Käs-
ten enthalten keine Logik und haben ausgehende Pfeile, ru-
fen also andere Funktionen auf. Funktionen in roten Kästen
sind die Blätter des Aufrufbaumes, enthalten Logik, haben
aber keine ausgehenden Pfeile. So einfach wie konsequent.
Das Ergebnis ist extrem gute Testbarkeit, wo sie gebraucht
wird: dort, wo Logik steht, bei den Operationen. Außerdem
erhält man hohe Verständlichkeit durch die Einhaltung des
SLA in den Integrationen (vergleiche Bild 5). Der Funktionsbaum, nach IODA strukturiert (Bild 9)
42 10.2018 www.dotnetpro.de


---


<!-- Page 4 of 4 -->


PLANUNG IODA
Auch Klassen
können dem
IODA-Schema
folgen
(Bild 10)
Das IODA-Architekturmodell ist fraktal (Bild 11)
ben sich durch die Beziehungen zwischen den Funktionen IODA-Architektur vor. Den spannt sie auf, um Verständlich-
auch Beziehungen zwischen den Modulen. Und Module be- keit und Testbarkeit zu motivieren.
kommen einen Platz in einer Hierarchie, der von ihren Funk-
Zusammenfassung
tionen abhängt.
Module, deren Integrationen keine Funktionen außerhalb Die Entwicklung der Architekturmuster von MVC über das
des Moduls aufrufen, sind in der Modulhierarchie dann Blät- Schichtenmodell bis zur Clean Architecture ist konsequent –
ter. Businesslogic ist dafür ein Beispiel. Intern jedoch können aber ich halte sie nicht für erschöpfend. Es kann und muss
auch solche Module aus Integrationen und Operationen be- weitergehen. Einiges ist schon besser geworden, doch zu viel
stehen. liegt mit der Sauberkeit von Code noch im Argen, selbst wenn
Falls Module allerdings Integrationen enthalten, die Funk- diese Architekturmodelle tapfer angewandt werden.
tionen aus anderen nutzen, sind sie Knoten in der Modulhie- Das zentrale Problem der funktionalen Abhängigkeiten ist
rarchie und werden als integrierende Module gewertet – in ihnen nicht wirklich gelöst. Lediglich DIP/IoC hat Linde-
selbst wenn sie Operationen enthalten sollten. rung gebracht – und das zu einem hohen Preis: Komplexität
Ganz formal betrachtet mag dies ein Widerspruch sein. wurde mit Komplexität bekämpft.
Darf ein Modul eine Integration sein, auch wenn es darin Mit der IODA-Architektur habe ich Ihnen nun eine Alter-
Operationen gibt? Wenn Sie wollen, können Sie solche Mo- native vorgestellt, die das Problem an der Wurzel packt. Die
dule in einer Hierarchie kennzeichnen. Ich tue das allerdings Vorteile der Architekturmuster werden beibehalten, der zen-
nicht. Wichtiger scheint mir, Augenmaß zu bewahren und zu tr ale Nachteil verschwindet. Unerwartet entstehen dabei zwei
schauen, wie der Anteil von Integration zu Operation in solch positive Effekte: Daten werden plötzlich im Modell sichtbar
einem Hybriden ist. Worum geht es bei dem Modul? Ist der und Kompositionsabstraktionen entstehen ganz natürlich.
Zweck integrativ oder operativ? Nach all den Jahren in tiefen funktionalen Abhängigkeiten
Wenn der Schwerpunkt bei integrierenden Funktionen ist das IODA-Denken natürlich eine gewaltige Umstellung.
liegt und der Zweck integrativ ist, dann besteht kein Anlass Doch die lohnt sich. Und irgendwann fragen Sie sich dann,
zur Sorge. Wenn das jedoch nicht der Fall ist, dann kann ge- warum die Strukturierung von Software Ihnen einmal schwer-
nau dieser hybride Charakter der Anlass sein, ein solches gefallen ist und das Testen Ihnen solche Mühe bereitet hat. ◾
Modul zu refaktorisieren und die wirklich integrierenden Tei-
le von den operierenden zu trennen. [1] Ralf Westphal, Eine Kritik bisheriger Architektur modelle,
Und noch eines ist bei der Klasse Businesslogic hervorzu- dotnetpro 8/2018, Seite 24 ff.,
heben. Schauen Sie noch einmal bei Bild 3 vorbei. Fällt Ihnen www.dotnetpro.de/A1808IODA
bei den Funktionen etwas auf? Sie sind alle statisch. [2] Ralf Westphal, Das IODA-Architekturmodell, dotnetpro
Ich habe die Domänenlogik statisch gemacht, weil es 9/2018, Seite 28 ff., www.dotnetpro.de/A1809IODA
schlicht keinen Grund gibt, es nicht zu tun. In einer IODA-Ar- [3] Ralf Westphal, Kontrollstrukturen in der Integration,
chitektur ist das völlig in Ordnung, ja sogar naheliegend. Hier www.dotnetpro.de/SL1810IODA1
werden keine Interfaces zwischen allen möglichen Klassen
gebraucht. Warum sollte ich also die Fachlogik mit einem In-
terface ausstatten oder auch nur mit Instanzmethoden? Ralf Westphal
Instanzmethoden sind schlicht weniger testbar als statische Ralf Westphal ist Trainer, Berater, Autor und
Methoden. Das vermeide ich, wo es geht. Und da es bei der Referent auf Entwicklerkonferenzen sowie
Fachlogik kein Signal für Instanzmethoden gibt – das wären Mitgründer von Clean Code Developer. Seine
zum Beispiel ein gemeinsamer Zustand oder API-Aufrufe –, Schwerpunkte sind nachhaltige Softwarearchi-
reichen mir statische Methoden völlig aus. tektur und zukunftsfähige Teamorganisation.
Das ist kein blinder Rückfall in ein Zeitalter prozeduraler info@ralfw.de
Programmierung, sondern eine bewusste Entscheidung. Sie
dnpCode A1810IODA
folgt Prinzipien und einer Systematik. Den Rahmen gibt die
www.dotnetpro.de 10.2018 43