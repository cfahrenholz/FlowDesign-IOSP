<!-- Page 1 of 9 -->


PLANUNG IODA
IODA-ARCHITEKTUR, TEIL 2
Das IODA-Architekturmodell
Entwurf eines neuen Architekturmusters auf der Basis der vier fundamental
unterschiedenen Ebenen Integration, Operation, Daten und APIs.
Der erste Teil dieser Artikelserie [1] hat die generelle Ent- Damit Sie wirklich verstehen, was ich mit funktionaler Ab-
wicklung der Architekturmuster von MVC über das hängigkeit meine, muss ich kurz den schon oft hier benutz-
Schichtenmodell bis zur Clean Architecture nachvollzogen ten Begriff „Logik“ definieren. Logik sind die Anweisungen,
und begründet, warum das Bedürfnis nach einem neuen Ar- die Funktionalität tatsächlich herstellen. Konkret sind dies
chitekturmodell entstand, das die bisher etablierten Modelle vor allem:
ablösen und deren Nachteile beseitigen soll: Das zentrale Transformationsanweisungen,
Problem der funktionalen Abhängigkeiten ist in ihnen nicht Kontrollflussanweisungen,
wirklich gelöst. Lediglich Linderung durch die Prinzipien De- Input-/Output-Anweisungen.
pendency Inversion (DIP) und Inversion of Control (IoC) wur-
de gebracht – und das zu einem hohen Preis. Komplexität Durch Abarbeitung nur dieser Anweisungen bekommt Soft-
wurde mit Komplexität bekämpft. ware ihr Verhalten. Wenn Logik passend zusammengestellt
Wie könnte nun ein Architekturmuster aussehen, das die ist, funktioniert Software.
Vorteile der bisherigen beibehält und die Nachteile hinter Aber was ist zu Anforderungen passende Logik? Das ist
sich lässt? Diese Vorteile sind: schwierig zu sagen. Das ist die Kunst der Programmierung.
Definition von „Standardverantwortlichkeiten“, die es von- Da kann leicht etwas schiefgehen. Deshalb muss Logik sorg-
einander abzugrenzen gilt, um die Verständlichkeit zu er- fältig getestet werden – natürlich automatisiert. Und um das
höhen und grundsätzliche Testbarkeit herzustellen. zu erreichen, muss Logik überhaupt erst einmal testbar sein.
Bewusstmachung der Wichtigkeit von klar
ausgerichteten Abhängigkeiten für Ver-
ständlichkeit und Testbarkeit.
Und die Nachteile:
Schlecht testbare funktionale Abhängig-
keiten.
Undurchsichtigkeit durch Entkopplungs-
aufwand.
Funktionale Abhängigkeiten
als Wurzelproblem
Der zentrale Nachteil der erwähnten populä-
ren Architekturmuster ist, dass sie auf funktio-
nalen Abhängigkeiten gründen. Die Notwen-
digkeit zu funktionalen Abhängigkeiten wur-
de nie hinterfragt. Und die funktionalen Ab-
hängigkeiten haben sich über die Jahrzehnte
auch nicht verändert. Sie existieren in der Im-
plementation einer Clean Architecture genau-
so wie in einer ersten Implementation der
Schichtenarchitektur noch ohne DIP/IoC.
Funktionale Abhängigkeiten lassen sich
nicht mit DIP/IoC wegzaubern. Ob sie existie-
ren, ist keine Sache der Compilezeitabhängig-
keiten, sondern der Laufzeitabhängigkeiten.
Wo immer eine Attrappe in einem Test gebaut
werden muss, um Logik gezielt testen zu kön-
nen, existiert eine funktionale Abhängigkeit. Unstrukturierter Code ist ein Flickenteppich aus Verantwortlichkeiten (Bild 1)
28 9.2018 www.dotnetpro.de


---


<!-- Page 2 of 9 -->


PLANUNG IODA
In funktionaler Abhängigkeit wechseln sich Logik und Funk­
Zur Laufzeit ruft eine innere Schale eine äußere auf (Bild 2) tionsa ufrufe ab (Bild 3)
Schauen Sie sich Bild 1 an, die Ausgangssituation im ersten Funktionale Abhängigkeiten verhindern die Einhaltung
Teil des Artikels. Dort sehen Sie nur Logik, sogar Logik mit des Prinzips Single Level of Abstraction (SLA). Logik ist per
ganz unterschiedlicher Verantwortlichkeit. Teile der Logik definitionem auf einem niedrigeren Abstraktionsniveau als
erfüllen die eine Funktion, zum Beispiel Zerlegung des Tex- der Aufruf von Logik mit einer Funktion. Das Resultat:
tes in Wörter, andere Teile der Logik erfüllen eine andere schlechte Verständlichkeit.
Funktion, etwa die Bestimmung der verschiedenen Wörter.
Jede dieser Verantwortlichkeiten kann fehlerbehaftet sein. Dass man Prinzipien wie DIP/IoC anwenden muss, um die
Jede verdient eigenständige Tests. Das ist in dem Verantwort- Kompromittierung von SRP und SLA wettzumachen, ent-
lichkeitsmischmasch aber nicht machbar. Die Testbarkeit der schärft die Lage nicht, sondern macht sie schlimmer. Denn
Verantwortlichkeiten ist gleich null. DIP/IoC erzeugen künstlich Komplexität, wie selbst Robert C.
Vergleichen Sie damit Bild 2. In der Clean Architecture sind Martin beklagt [2].
Verantwortlichkeiten getrennt. Der Anteil an Logik, der sich Das zentrale Problem der üblichen Architekturmuster ist
um die Wortzählung kümmert, ist nun in einer eigenen Funk- mithin Code, der wie in Bild 3 aussieht: In einer Funktion
tion freigestellt. Damit kann die Wortzählungslogik separat wechseln sich Logik und Aufrufe anderer Funktionen ab.
von der Benutzerschnittstellenlogik oder von der Logik zum Dieses Bild stellt ganz deutlich die Laufzeitabhängigkeiten
Laden des Textes aus einer Datei getestet werden. dar. Es ändert sich also auch mit noch so viel DIP/IoC nichts.
Allerdings: Die Logik zur Wortzählung ist noch funktional Durch Anwendung der Prinzipien wird höchstens diese Rea-
abhängig. Innerhalb von Count_words() wird weitere Logik lität kaschiert – bis Sie in den Tests auf unschöne Weise da-
in Retrieve() aufgerufen, deren Funktionalität für die Logik in ran erinnert werden.
Count_words() relevant ist. Um die Logik von f() für sich genommen testen zu können,
Diese funktionale Abhängigkeit verhagelt die Testbarkeit müssen Sie Attrappen einführen. Und selbst dann wird nur
von Count_words(). Durch die Abhängigkeit kann bei einem die gesamte Logik getestet, sodass bei einem Fehler unklar
fehlschlagenden Test nicht eindeutig bestimmt werden, wo ist, ob dieser im ersten, zweiten oder dritten Abschnitt der Lo-
das Problem liegt: in der Logik von Count_words(), die eigent- gik seine Ursache hat. Die Logikanteile zwischen den funktio-
lich getestet werden soll, oder in der Logik von Retrieve()? nalen Abhängigkeiten sind für sich genommen immer noch
Aufgelöst wird diese Unsicherheit durch DIP/IoC: Sie erset- nicht testbar.
zen die Abhängigkeit im Test einfach durch eine Attrappe. Eine Funktion wie f() hat deshalb aus meiner Sicht immer
Erstens macht das aber Aufwand, weil dafür in streng typi- n+2 Verantwortlichkeiten. n steht dabei für die Zahl der funk-
sierten Sprachen ein Interface nötig ist (DIP). Zweitens macht tionalen Abhängigkeiten.
das Aufwand, weil die Attrappe überhaupt codiert werden Vor jedem Funktionsaufruf steht Logik (n) und auch nach
muss. Drittens muss die Attrappe verfügbar gemacht werden dem letzten noch mal (+1); jede dieser Logik-Passagen tut
(IoC). Viertens muss die Attrappe so konfiguriert werden, etwas anderes und stellt eine Verantwortlichkeit dar. Viel-
dass sie zu dem passt, was in der zu testenden Funktion pas- leicht ist das nicht immer so, aber diese Verallgemeinerung
siert; die Attrappe erzwingt sowohl Wissen über die Verarbei- halte ich für hilfreich. Sie macht das Problem deutlicher als
tung in der zu ersetzenden Funktion wie in der zu testenden. eine Erbsenzählerei, ob wirklich um jeden Funktionsaufruf
Und schließlich: Funktionale Abhängigkeiten widerspre- herum Logik steht.
chen ganz prinzipiell sauberer Softwareentwicklung. Die Integration der ganzen Funktionsaufrufe mit der Logik
Funktionale Abhängigkeiten verhindern die Einhaltung ist eine separate, übergeordnete Verantwortlichkeit (+1).
des Single Responsibility Principle (SRP), weil mit ihnen die
abhängige Funktion immer mindestens zwei Verantwort- Die Verantwortlichkeiten, die ich hier meine, sind formal,
lichkeiten hat: einerseits die Erfüllung einer Funktionalität nicht inhaltlich. Sie ergeben sich allein aus der Struktur. Da-
mit Logik, andererseits den Aufruf von Funktionen in pas- rüber hinaus kann es also innerhalb der Logikblöcke weitere
sender Reihenfolge mit den richtigen Parametern. Letzte- Verantwortlichkeiten geben.
res nenne ich Integration. Das Resultat: schlechte Testbar- Die Testbarkeit einer Codebasis steht damit in umgekehrt
keit, schlechte Verständlichkeit. proportionalem Verhältnis zur funktionalen Abhängigkeit ▶
www.dotnetpro.de 9.2018 29


---


<!-- Page 3 of 9 -->


PLANUNG IODA
der Funktionen in einer Codebasis. Je mehr Verantwortlich- Doch das ist aus meiner Sicht schon die Kür. Davor steht die
keiten eine Funktion hat, desto schwerer ist sie testbar. Und Pflicht, sprich die Erkennung der formalen Verantwortlich-
sie hat umso mehr Verantwortlichkeiten, je mehr funktio nale keiten aufgrund funktionaler Abhängigkeit. Nach der obigen
Abhängigkeiten sie enthält. Formel sind das in Bild 4 für Count_words() 1+2=3; die Test-
Außerdem ist eine solche Codebasis weniger verständlich. barkeit hat also nur den Wert 1/3=0,33.
Denn funktionale Abhängigkeiten widersprechen nicht nur Schauen Sie jetzt zum Vergleich Bild 5 an. Beide Datenzu-
dem SRP und dem SLA, sondern sorgen auch dafür, dass es griffsmethoden haben keine (!) funktionalen Abhängigkei-
beim Funktionsumfang keine Grenze gibt. Solange funktio- ten; sie enthalten reine Logik. Ihre formale Verantwortlich-
nale Abhängigkeiten okay sind, solange sind auch 100, 1000 keitszahl ist damit 1 und die Testbarkeit hat den Wert 1/1=1.
oder 10000 Zeilen lange Funktionen okay. Besser geht’s nicht. Die Klasse hat keine Abhängigkeiten; sie
Mit funktionalen Abhängigkeiten wächst der Methoden- ist – wie Presenter – ein Blatt im Baum der Laufzeithierarchie.
umfang ganz selbstverständlich bei Bedarf. Wenn zu 100 Zei- Keine Attrappen sind nötig, um sie zu testen.
len noch 40 dazukommen sollen, dann werden vielleicht 15 Dass der Test von Funktionen, die auf Ressourcen zugrei-
Zeilen in eine Funktion extrahiert und aufgerufen – eine fen, auch nicht ganz einfach ist, steht auf einem anderen
funktionale Abhängigkeit ist entstanden – und die 40 neuen Blatt. Für das hiesige Argument ist das nicht wichtig.
Zeilen werden dazugepackt. Am Ende sind in der Funktion
Auflösung funktionaler Abhängigkeiten
125 Zeilen. Und so geht es weiter und weiter.
Refactorings wie extract method scheinen sogar die Hemm- Wenn funktionale Abhängigkeiten Verständlichkeit und
schwelle gesenkt zu haben, Funktionen länger und länger zu Testbarkeit verringern, wie können sie dann verhindert wer-
machen. Es ist ja so einfach, etwas Gutes zu tun, also ein we- den? Soll Software etwa auf Funktionen verzichten?
nig Logik (inklusive funktionaler Abhängigkeiten) zu extra- Natürlich nicht. Funktionen sind wertvolle Strukturie-
hieren. Da darf man es sich anschließend gönnen, weitere Lo- rungsmittel für Logik. Um funktionale Abhängigkeiten loszu-
gik auf allen Ebenen dazuzupacken. Das verringert die Ver- werden, brauchen wir davon mehr und nicht etwa weniger.
ständlichkeit des Codes weiter, weil dadurch Funktionalität Dass es jedoch auch ohne funktionale Abhängigkeiten
in der Tiefe gestaffelt wird. Jeder Überblick, wie Logik Ver- geht, zeigen schon die Funktionen in Bild 5. Sie sind Beispie-
halten erzeugt, geht auf diese Weise verloren. Die Konse- le für eine Art von Funktionen, die ohne auskommt. Ich nen-
quenz können dann nur lange Debugging-Sitzungen sein, in ne sie Operationen.
denen die Logik in der Tiefe verfolgt wird. Operationen enthalten ausschließlich Logik. Sie rufen kei-
Wenn Sie es kurz und knackig mögen, lautet mein Vor- ne weiteren Funktionen auf, über deren Logik sie Kontrolle
schlag, Sie berechnen die Testbarkeit einer Funktion so: 1 ge- haben. Dass eine Operation einen Vergleichsoperator be-
teilt durch die Anzahl der Verantwortlichkeiten. Der Wert 1 nutzt oder einen API-Funktionsaufruf wie File.ReadAllLines()
stellt danach den höchsten Wert für Testbarkeit dar. Eine tätigt, zählt nicht als funktionale Abhängigkeit. Solche Funk-
Funktion hat dann nur eine Verantwortlichkeit. Je weiter der tionen aufzurufen ist der Job einer Operation. Ob sie das kor-
Wert gegen 0 tendiert, desto schlechter ist die Testbarkeit. rekt im Sinne ihrer Verantwortlichkeit tut, gilt es mit automa-
Verantwortlichkeiten zu erkennen ist eine Kunst, wenn es tisierten Tests zu prüfen.
um inhaltliche geht. Die Auffassungen können da schon im Software kann allerdings nicht nur aus Operationen beste-
Detail auseinandergehen. Wie viele Verantwortlichkeiten hen. Dann würde die ganze Logik eingepackt in Funktionen
identifizieren Sie etwa in der hervorgehobenen Logik in Bild 4? nur nebeneinanderstehen, ohne zusammenzuwirken. Opera-
tionen müssen also aufgerufen werden. Irgendwo muss es
Funktionen geben, die wiederum Operationen als Funktio-
nen aufrufen – allerdings ohne dass dadurch funktionale Ab-
hängigkeiten entstehen. Glücklicherweise ist das ebenfalls
möglich. Beispiele dafür sehen Sie in Bild 6. Count_words_in_
file() und Count_words() sind Funktionen, die andere Funk-
Funktionen ohne funktionale Abhängigkeiten sind bestens
Schlecht testbare Logik trotz Schichtung (Bild 4) testbar (Bild 5)
30 9.2018 www.dotnetpro.de


---


<!-- Page 4 of 9 -->


PLANUNG IODA
Der Use Case beim Orchestrieren von Adaptern und Business­ Übliche Architekturmuster erzeugen Hierarchien hybrider Funk­
logik (Bild 6) tionen mit funktionalen Abhängigkeiten (Bild 7)
tionen aufrufen – aber selbst keine Logik enthalten. Auch sie Und noch mal: Daran ändert der ganze Wirbel um DIP/IoC
sind damit frei von funktionalen Abhängigkeiten. Diese Art und die Ausrichtung von Compilezeitabhängigkeiten nichts.
von Funktionen nenne ich Integration. Hybride Funktionen sind immer schwer zu testen.
Integrationen haben formal nur eine Verantwortlichkeit: Sobald Funktionen jedoch grundsätzlich in Operationen
Sie integrieren, das heißt, sie binden andere Funktionen zu und Integrationen getrennt werden, entsteht eine andere
einer größeren zusammen. Aus vielen verschiedenen Funk- Hierar chie (Bild 8). In ihr gibt es mehr Funktionen, die jedoch
tio nen entsteht eine neue auf höherem Abstraktionsniveau. alle kleiner sind als die bisherigen Hybriden. Logik befindet
Operationen abstrahieren von Logikdetails, die nötig sind, sich darin nur noch in den Blättern.
um Funktionalität herzustellen. Integrationen abstrahieren Mehr Funktionen entstehen, weil die Logikanteile in Hy-
von den Detailfunktionen, aus denen ein größerer Funktions- briden herausgezogen werden müssen in Operationen. Doch
baustein zusammengesetzt ist. das sollte Ihnen keine Angst machen. Im Gegenteil: Endlich
Aber wie steht es mit der Testbarkeit von Integrationen, die ist Logik viel leichter testbar. Endlich sind die Funktionen viel
mehrere Funktionen aufrufen? Da Integrationen nur eine for- übersichtlicher.
male Verantwortlichkeit haben, ist ihre Testbarkeit ebenfalls Das Mittel, um eine steigende Zahl von Funktionen in den
1/1=1. Wenn eine Integration überhaupt automatisiert getes- Griff zu bekommen, liegt außerdem auf der Hand: Klassen.
tet wird, müssen die aufgerufenen Funktionen nicht durch Nicht nur werden also Funktionen kleiner, sondern auch
Attrappen ersetzt werden. Im Gegenteil: Es ist wichtig, dass Klassen werden übersichtlicher, weil deren Zahl bei fallen-
die realen Funktionen im Test ausgeführt werden, um sicher- dem Umfang steigt.
zustellen, dass die Integration ihren Job tut und ein umfas- Durch die Brille der Mainstream-Objektorientierung be-
senderes Verhalten aus Einzelverhalten herstellt. trachtet mag das ungewöhnlich aussehen. Doch letztlich ist
In vielen Fällen müssen Integrationen aber gar nicht auto- es das, was auf die eine oder andere Weise immer wieder ver-
matisiert getestet werden, weil es keine Logik zu testen gibt sucht wurde. Nur sind die bisherigen Empfehlungen sperrig,
und die Sequenz der Funktionsaufrufe offensichtlich korrekt weil sie auf einem Paradigma basieren, das sie nicht hinter-
ist im Sinne der Hypothese, dass damit ein bestimmter Effekt fragen. Es lautet: Funktionen sind Hybride.
erzielt wird. Man kann dann sozusagen einen Induktions- Wird das Paradigma jedoch aufgegeben zugunsten einer
schluss wagen: Wenn die aufgerufenen Funktionen korrekt Unterscheidung von Integrationen und Operationen, tritt ▶
sind, dann ist die Integration ebenfalls korrekt.
Eine Ausnahme bildet die Integration an der Wurzel einer
Aufrufhierarchie. Aber auch dort müssen nicht zwangsläufig
Attrappen zum Einsatz kommen.
Funktionen spielen in den traditionellen Architekturmus-
tern keine Rolle. Funktionen sind dort in ihrer Art alle gleich.
Auch wird der Begriff Logik nicht benutzt, außer als Namens-
suffix. Fast alle Funktionen sind deshalb Hybride mit zweifa-
cher Verantwortlichkeit. Sie operieren und integrieren, sie
enthalten Logik und rufen andere Funktionen auf. Eine Aus-
nahme bilden lediglich die wenigen Funktionen am Fuße der Die Grundlage eines neuen Architekturmusters ist eine Hierar­
Abhängigkeitshierarchie (Bild 7). chie getrennter Verantwortlichkeitsarten (Bild 8)
www.dotnetpro.de 9.2018 31


---


<!-- Page 5 of 9 -->


PLANUNG IODA
Selbstverständlich ist das auch bei den Hybriden und Ope-
rationen in Bild 7 der Fall. Dort fließen Daten in der Hierarchie
von oben nach unten und von unten nach oben. Die Logik
enthaltenden Funktionen sind hier jedoch alle direkt verbun-
den. Deshalb sind Daten kein Thema.
Ohne eine Verbindung zwischen Logik in verschiedenen
Funktionen stellt sich die Datenfrage allerdings sehr deutlich.
Die Antwort darauf zeigt Bild 9.
Operationen sind abhängig von Daten, die sie entweder
austauschen (fließende Daten) oder die sie gemeinsam nut-
Operationen stehen über Daten in Kontakt (Bild 9) zen (stehende Daten, Zustand).
Zwar sind gewöhnlich fast alle Operationen über Daten
verbunden, doch interessant sind vor allem Datenstrukturen,
der gewünschte Effekt ganz natürlich ein. Das ist jedenfalls die Sie selbst definieren. Solche Datenklassen dürfen natür-
meine Erfahrung nach Jahren der Softwareentwicklung auf lich nicht der Forderung widersprechen, auf funktionale Ab-
diese Weise. hängigkeiten zu verzichten. Deshalb sollten Klassen, die Da-
ten sind, keine Methoden besitzen.
Operationen verbinden
Andere Klassen, die Daten haben, publizieren diese nicht.
Es gibt noch ein weiteres Problem, unter dem die üblichen Sie stehen deshalb in Bild 9 nicht auf der untersten Ebene.
Architekturmuster leiden: Sie bieten keinen Platz für Daten. In Bezug auf Klassen, die keine Funktionen haben, beste-
Das ist umso misslicher, als Daten schon früher in Programm- hen keine funktionalen Abhängigkeiten. Das Verhältnis zwi-
ablaufplänen und Nassi-Shneiderman-Diagrammen keine schen Integration und Operation setzt sich also fort zu den
Abbildung fanden und somit globalen Daten und daraus re- Daten.
sultierend unkontrolliert wachsenden Datenabhängigkeiten Zumindest zunächst. Denn am Ende ist diese Rigorosität
Vorschub geleistet wurde. nicht durchzuhalten. Sie würde Möglichkeiten der Objekt-
Auf Architekturebene sind Daten in den Diagrammen ent- orientierung zur Kapselung ungenutzt lassen. Deshalb kön-
weder gar nicht zu sehen oder sie werden in den Klassen der nen auch Klassen, die Daten sind, Methoden besitzen – aller-
Schichten und Schalen schlicht automatisch mitgedacht. So dings nur in begrenzter Weise.
wie hybride Funktionen Verantwortlichkeiten vermischen, Methoden von Datenklassen haben lediglich den Zweck,
vermischen die Klassen in den bisherigen Architekturen die Konsistenz der Daten sicherzustellen und den Datenzu-
ebenfalls Verantwortlichkeiten. Sie fassen Funktionen und griff zu ermöglichen. Stack und Queue sind dafür gute Bei-
Daten unterschiedslos zusammen. spiele: Das sind Klassen, die eine Datenstruktur implemen-
Das mag scheinbar durch die Objektorientierung nahege- tieren (abstrakter Datentyp), aber nur Methoden anbieten,
legt sein, die ja mit dem Anspruch a ngetreten war, gerade um die „Form“ der Daten aufrechtzuerhalten beziehungs-
Funktionen und Daten näher zusammenzubringen, um Kap- weise zu traversieren.
selung zu erreichen. Doch auch wenn
dies durch Mittel der Objektorientie-
rung möglich ist, bedeutet das nicht,
dass es unsystematisch geschehen
sollte. Leider liefern die Architektur-
muster hier jedoch keine Hinweise.
Ein modernes Architekturmuster,
das über Bisheriges hinausgeht, soll-
te also das Thema Daten ebenfalls
adressieren, um die beschriebene
Lücke zu schließen. Nicht nur funk-
tio nale Abhängigkeiten sind zu ent-
schärfen beziehungsweise ganz zu
eliminieren, sondern auch Datenab-
hängigkeiten sind zu explizieren.
Zum Glück ist das ganz leicht und
ergibt sich in natürlicher Weise aus
Bild 8. Integrationen enthalten keine
Logik. Wie kommunizieren also die
Operationen überhaupt miteinan-
der? Das kann nur über Daten ge-
schehen. Eine Datenklasse verbindet Operationen (Bild 10)
32 9.2018 www.dotnetpro.de


---


<!-- Page 6 of 9 -->


PLANUNG IODA
MVC und dem Schichtenmodell deutli-
cher gemacht wurde: die Kommunikation
mit der Außenwelt.
I/O-Operationen oder allgemeiner API-
Aufrufe auf Bibliotheken und Frame-
works, die nicht unter Ihrer Kontrolle ste-
hen, sind etwas Besonderes. Einerseits
geht von dort immer wieder eine Behinde-
rung von Tests aus, weil I/O vergleichs-
weise imperformant ist und/oder Einrich-
tungsaufwand bedeutet. Andererseits un-
terliegen externe Bibliotheken unkontrol-
lierten Änderungen oder sollen gar aus-
tauschbar sein. Beides legt nahe, API-Auf-
rufe in möglichst wenigen Modulen zu iso-
Konzentrische Architekturmuster (Bild 11) lieren. Hier kommt das Prinzipienduo DIP/
IoC dann tatsächlich zu gutem Einsatz.
Bei den konzentrischen Architektur-
Wenn Operationen Methoden auf solchen Datenobjekten mustern ist zumindest I/O deutlich auf die äußere Schale be-
benutzen, dann sehe ich darin keine belastende funktionale schränkt, die noch zum Softwaresystem gehört. In Bild 11
Abhängigkeit. Für Datenstrukturen müssen keine Abstrak- finden Sie zu diesem Zweck Adapter in der hexagonalen Ar-
tionen definiert werden, um sie in Tests zu ersetzen. Daten- chitektur und Controller, Gateways, Presenter in der Clean
klassen, die in dieser Weise funktional einfach und fokussiert Architecture.
gehalten werden, erzeugen keine zusätzliche Komplexität. Das Schichtenmodell ist in dieser Hinsicht wenig explizit
Sie machen nichts schwieriger zu verstehen. Im Gegenteil: und undifferenziert. Benutzerschnittstelle und Datenzugriff
Immer wieder hilft es, Logik aus Operationen herauszuziehen scheinen grundsätzlich verschieden zu sein (Bild 12). Das
in Datenstrukturen, um Operationen und Integrationen zu macht auch eine seiner Schwächen aus, die die konzentri-
entzerren. schen Muster ausgleichen.
Zur Veranschaulichung habe ich einmal die Businesslogik Ein besseres Architekturmodell sollte diese Klarheit und
unseres Beispiels in diesem Sinne verändert. Integrationen Differenzierung natürlich erhalten. In einer Funktionshierar-
und Operationen sind in Bild 10 sauber getrennt. Außerdem chie ohne funktionale Abhängigkeiten ist das jedoch sehr
ist ShredderedText als Datenklasse mit minimaler Logik her- leicht. API-Aufrufe gehören zur Logik, und Logik findet sich
ausgezogen und dient der Kommunikation zwischen den nur in Operationen (Bild 13).
Operationen Shred() und Filter(). Wie oben zugestanden, können zwar auch Datenklassen
Dass die Integration Eigenschaften auf ShredderedText Logik enthalten, doch die ist bewusst inhaltlich auf die Daten
aufruft, das Datenobjekt selbst also gar nicht nach Filter() in den Strukturen begrenzt und darf formal gerade keinen
hineinfließt, ist lediglich eine naheliegende Optimierung. Sie I/O beziehungsweise keine speziellen API-Aufrufe enthal-
ändert nichts am Zweck der Datenklasse, Daten zu sein und ten. Datenklassen sollen möglichst stabil sein, da von ihnen
Operationen zu verbinden. gewöhnlich viele Funktionen abhängig sind. Logik ist dem
abträglich, umso mehr, wenn sie auch noch von APIs abhän-
Verbindung zur Außenwelt
gig wäre.
In den konzentrischen Architekturmustern gibt es noch einen Die Klasse Dataaccess in Bild 5 liefert zwei Beispiele für
Aspekt, der hinzugekommen ist beziehungsweise gegenüber Operationen mit I/O-Logik. ▶
Konzentrische Abhängigkeiten ergeben mehr Sinn (Bild 12) Nur Operationen rufen externe APIs auf (Bild 13)
www.dotnetpro.de 9.2018 33


---


<!-- Page 7 of 9 -->


PLANUNG IODA
Ein neues
Architekturmuster
Nun ist alles beisammen für
ein neues Architekturmuster,
wie ich es mir vorstelle, um
den Ballast der bisherigen
abzuwerfen. Ich nenne es die
IODA-Architektur, wegen Die Ebenen des neuen Archi­
der darin fundamental unter- tekturmusters (Bild 14)
schiedenen Ebenen (Bild 14).
Bitte beachten Sie, dass es
in diesem Architekturmuster zunächst keine inhaltlichen
Verantwortlichkeiten gibt. Auch darin unterscheidet es sich Die zwei Ebenen der IODA­Architektur (Bild 16)
vom Üblichen. Insofern beansprucht die IODA-Architektur
tatsächlich Universalität. Ob Game oder CRM oder Buchhal-
tung: Jeder Software steht diese „Anatomie“ gut zu Gesicht, Aber die IODA-Architektur lässt die inhaltlichen Verant-
glaube ich. wortlichkeiten nicht aus dem Blick. Orthogonal zu den Ebe-
Unterschieden werden zunächst lediglich formale Verant- nen in Bild 14 gibt es eine ebenfalls konzentrische Darstellung
wortlichkeiten. Integration hat einen ganz anderen Auftrag von Software (Bild 15). Hier trifft IODA eine Aussage zum
als Operation, und Operation hat einen ganz anderen Auftrag Muster der Verantwortlichkeiten.
als Daten. Und APIs sind Ihrer Verfügung ganz entzogen; Sie Zu unterscheiden ist zunächst das Softwaresystem von der
müssen sie nehmen, wie sie sind. Umwelt. Der Code, den Sie schreiben, gehört zum Soft-
Diese Grundstruktur ist jedoch nur eine mögliche, wenn waresystem. Alles andere ist Bestandteil der Umwelt. Ange-
auch die vordringliche Perspektive auf Software. Sie defi- deutet wird das durch die Kreislinie, die das Innen vom Au-
niert, wie Code aufgebaut werden sollte, unabhängig davon, ßen trennt.
was seine lösungsbezogene Aufgabe ist. Auf der Kreislinie angesiedelt sind Grundverantwortlich-
In dieser Perspektive geht es zunächst auch nur um Funk- keiten, die alle zur Kategorie Adapter gehören. Sie kapseln
tionen und Datenstrukturen. Das halte ich aber für wichtig, insbesondere I/O-Logik, aber auch andere API-Aufrufe.
weil damit deutlich in den Blick genommen ist, was Software Adap ter verbinden das Innen mit dem Außen.
ausmacht: Logik, deren Verhalten darin besteht, Daten zu Anders als die hexagonale Architektur teilt die IODA-Ar-
transformieren. chitektur die Adapter jedoch in zwei Gruppen: Portale und
Wenn ein Architekturmuster die zwei Seiten der Software- Provider. Durch Portale wird das Softwaresystem von der Um-
münze – Logik und Daten – in seinem Bild nicht deutlich re- welt gesteuert. Durch Provider greift das Softwaresystem auf
präsentiert, dann, glaube ich, fehlt etwas. Die IODA-Archi- Umweltressourcen zu, von denen es abhängig ist. Der Kon-
tektur tut das. Und sie macht eine klare Aussage darüber, wie takt mit der Umwelt ist also asymmetrisch.
Logik in Funktionen zu verpacken ist, um Verständlichkeit Benutzer triggern Logik über Portale, indem sie dort Input-
und Testbarkeit auf ein Mindestniveau zu heben. Daten anliefern. Ebenso erhalten Benutzer über Portale Out-
put-Daten zurück. Benutzer können Menschen sein oder an-
dere Softwaresysteme.
Portale gibt es allerdings in zwei Ausprägungen: als Con-
trol ler und als Dialoge. Controller machen ein Softwaresys-
tem über Entry Points zugänglich. Main() ist ein solcher Ent-
ry Point, die Klasse Program also ein Controller. Mittels Con-
trollern werden Softwaresysteme gestartet oder zumindest
aus einem inaktiven Zustand „geweckt“.
Dialoge hingegen bieten weitere Trigger im Rahmen des
Aufrufs über einen Entry Point. Denken Sie an einen Button
auf einem WPF-Fenster. Das Fenster ist ein Dialog, der mehr
oder weniger direkt innerhalb von Main() geöffnet wurde. In
Dialogen wartet Software aktiv auf einen Input durch einen
Benutzer.
Die Unterscheidung zwischen Portalen und Providern ist
nützlich, weil damit sprachlich das asymmetrische Verhältnis
eines Softwaresystems zu seiner Umwelt dokumentiert wird.
Auf der einen Seite wird es von der Umwelt vermittels APIs
gesteuert, auf der anderen Seite steuert es selbst die Umwelt
Die inhaltliche Dimension der IODA­Architektur (Bild 15) vermittels APIs.
34 9.2018 www.dotnetpro.de


---


<!-- Page 8 of 9 -->


PLANUNG IODA
Die Unterscheidung zwischen Controllern und Dialogen
wiederum ist nützlich, weil damit sprachlich ihre Position in
der IODA-Hierarchie dokumentiert wird. Controller als Mo-
dule haben integrierende Funktion, Dialoge als Module ha-
ben operierende Funktion.
Schließlich steht die Domain in der Mitte. Sie betont das,
worum es eigentlich geht: die Fachlichkeit. Die darum krei-
senden Adapter können sich in Art und Zahl ständig ändern.
Doch von der Domain ist anzunehmen, dass sie davon recht
wenig betroffen im Kern eines Softwaresystems ruht.
Die Adapter haben sogar die Aufgabe, genau das sicher-
zustellen. Sie bilden quasi einen Schutzwall gegenüber der
Umwelt, zu der auch die zahllosen APIs gehören; sie schaffen
auf diese Weise einen Innenraum, der in eigener Geschwin-
digkeit evolvieren soll. Abstraktion durch Kategorisierung (Bild 18)
Aus dieser Perspektive betrachtet, ist Software auch in der
IODA-Architektur in klare Verantwortlichkeiten geteilt:
• Adapter ihren Ausgang von den Controllern nehmen. „Zufällig“ sage
° Portale ich, weil das nicht Absicht des Modells ist, sondern leider
- Controller technische Notwendigkeit. Wenn ein Entry Point eines Con-
- Dialoge trollers getriggert wird, bedeutet das gewöhnlich eine Instan-
° Provider zierung des Controllers. Vorher ist also kein Code gelaufen,
• Domain der integrierend hätte wirken können.
An dieser Stelle ist das aber ein Detail, um das Sie sich nicht
Das ist differenzierter als bei MVC oder beim Schichtenmo- sorgen sollten. Der Grundsatz bleibt: Es gibt keine funktiona-
dell oder auch der hexagonalen Architektur. Doch ich finde len Abhängigkeiten. Die IODA-Architektur hat zwei Ebenen,
es immer noch sehr allgemein und deshalb universell. Ob wobei die Hierarchie die grundlegende ist (Bild 16). Sie er-
Twitter-Klon, Game oder Hausverwaltung: Diese Verantwort- möglicht, dass in der darüberliegenden Ebene keine funktio-
lichkeiten lassen sich immer finden. nalen Abhängigkeiten existieren.
Wie in der Clean Architecture ist auch bei IODA zu erwar- In der IODA-Architektur ist getrennt, was getrennt sein
ten, dass äußere Verantwortlichkeiten in stärkerem Maß Ver- muss: formale und inhaltliche Verantwortlichkeiten. Die
änderungen unterliegen als innere. überkommenen Architekturmuster hingegen vermischen
Allerdings – und das ist der zentrale Unterschied zu allen hier die Verantwortlichkeiten – mit negativem Effekt für Ver-
anderen Architekturmodellen – stehen die Verantwortlich- ständlichkeit und Testbarkeit.
keiten in keiner funktionalen Abhängigkeit!
Echt abstrakt
Es gibt keine Abhängigkeitspfeile, die nur von außen nach
innen zeigen dürfen. Ein Dialog braucht keinen Provider, um Die Hierarchie der Integration fügt der IODA-Architektur
seinen Job zu machen. Die Domain ist von keinem Provider noch einen Aspekt hinzu, der bei den bisherigen Modellen
abhängig. unberücksichtigt geblieben ist: Abstraktion.
Verbunden werden die Verantwortlichkeiten vielmehr Von Abstraktion ist zwar in DIP die Rede – eine Verant-
durch integrierende Beziehungshierarchien – die „zufällig“ wortlichkeit soll nicht direkt von einer anderen abhängig
sein, sondern von einer Abstrak-
tion (Bild 17) –, doch diese Art der Ab-
straktion meine ich nicht.
Verwirrend, oder? Um es zu ver-
stehen, hier meine Sichtweise auf
Abstraktion. Es gibt mindestens
zwei verschiedene Arten:
Kategorisierung: Verschiedene
Elemente werden auf Gemein-
samkeiten untersucht. Ist eine
vorhanden, können die Elemente
unter dieser Gemeinsamkeit zu-
sammengefasst werden. Eine Ka-
tegorie wird gebildet. Beispiele
dafür zeigt Bild 18. Der Inhalt einer
Über Interfaces entkoppelte Schichten (Bild 17) Haribo-Color-Rado-Tüte wur- ▶
www.dotnetpro.de 9.2018 35


---


<!-- Page 9 of 9 -->


PLANUNG IODA
de nach verschiedenen Kriterien kate- wendbarkeit geredet – doch das Mittel
gorisiert, wie zum Beispiel Geschmack Klasse ist dafür viel zu schwerfällig,
oder Form. und die vorzeitige Generalisierung lau-
Komposition: Verschiedene Elemente ert überall.
werden zu einem Ganzen vereint, eben In der IODA-Architektur hingegen
weil sie verschieden sind. Im Verein ist Abstraktion durch Komposition ganz
stellen sie auf höherer Ebene allerdings einfach: Wo eine Funktion andere inte-
etwas Neues dar. Ein Beispiel dafür griert, steht eine neue Funktion zur
zeigt Bild 19: Zahnräder, Schrauben, Verfügung, die produktiver macht, weil
Zeiger und Federn ergeben zusammen sie Details verbirgt (vergleiche dazu
ein Uhrwerk. meinen Blog-Artikel „Stratified Design
Abstraktion durch Komposition (Bild 19) over Layered Design“ [3]). Und sie tut
In der Softwareentwicklung finden wir das auch noch in einer Weise, die die
beide Arten der Abstraktion. Der Katego- Testbarkeit nicht kompromittiert.
risierung dienen Klassen und Interfaces. Diese Art der Ab- Wenn eine Funktion eine andere kennt, dann dient das der
straktion wird bei DIP aufgerufen. Abstraktion durch Komposition. Eine integrierende Funktion
Kategorisierung ist natürlich nützlich. Sie schafft Überblick zieht darüber verschiedene Funktionen zu einem neuen,
in der Vielfalt. Aber Kategorisierung ist nicht funktional. nützlichen und besser verständlichen Ganzen zusammen.
Komposition hingegen ist funktional. Das Neue, das aus der Es gibt sonst keinen Grund, warum eine Funktion eine an-
Komposition entsteht, stellt auf höherer Ebene wieder ein dere aufrufen sollte. Da ist IODA ganz strikt. Funktionen mit
nützliches Ganzes dar. Entweder sind die darin eingegange- ganz verschiedenen Aufgaben sollen einander nicht kennen.
nen Einzelteile alleine nicht nützlich oder es ist umständlich, Das ist aber in den bisherigen Architekturmodellen der Fall.
mit ihnen einen Zweck zu verfolgen. Die Komposition jedoch Ob das mit zwischengeschobener kategorisierender Abstrak-
verbirgt diese Details. Die Komposition vereinfacht, sie macht tion in Form eines Interface geschieht oder nicht, spielt dabei
produktiver. keine Rolle.
Beispiel dafür sind die Integrationen in der IODA-Architek- In einer IODA-Architektur verlaufen Pfeile also vom Ab-
tur. Sie ziehen Operationen (oder auch andere Integrationen) strakten zum Konkreten, vom Ganzen zu den Teilen, vom ho-
zu etwas funktional Größerem zusammen. Integrationen hen zum niedrigen Kompositionsniveau. Das ist grundsätz-
bringen etwas auf den Punkt. lich anders als in den bisherigen Architekturmustern.
Abstraktion durch Komposition findet sich in den bisheri- Bisher verliefen Pfeile vom einen zum anderen in Richtung
gen Architekturmodellen nicht. Es ist ein Irrglaube, dass es der Herstellung von Verhalten. Pfeile haben vor allem Ver-
bei den Schichten im Schichtenmodell um Abstraktion ginge. schiedenes auf demselben Kompositionsniveau verbunden.
Ebenso wenig ist eine Entity im Kern der Clean Architecture Mit IODA ändert sich das. Dort verlaufen Pfeile im Sinne von
abstrakter als ein Use Case oder ein Presenter in den Schalen Funktionsaufrufen nicht zwischen Verschiedenem, sondern
drumherum. zwischen Gleichem – nur liegt dieses Gleiche auf unter-
Eine gewisse Abstraktion durch Kategorisierung enthalten schiedlichen Abstraktionsniveaus. ◾
die Architekturmodelle jedoch trotzdem, weil die Blöcke be-
ziehungsweise Schalen mit ihren Verantwortlichkeiten für [1] Ralf Westphal, IODA-Architektur, Teil 1, Eine Kritik
eine größere Anzahl von Modulen stehen, die demselben bisheriger Architekturmodelle, dotnetpro 8/2018,
Zweck dienen. Seite 24 ff., www.dotnetpro.de/A1808IODA
Aber wie gesagt: Auch wenn Kategorisierung die Ver- [2] Robert C. Martin, Clean Architecture,
ständlichkeit erhöht, auf die Produktivität hat sie damit rela- A Craftsman’s Guide to Software Structure and Design,
tiv geringen Einfluss. Ganz anders die Komposition! Das be- Prentice Hall, 2017, ISBN 978-0-13-449416-6
weist die Geschichte der Programmiersprachen. Das beweist [3] Ralf Westphal, Stratified Design over Layered Design,
der Erfolg des OSI-Modells. Das beweist die Entwicklung von http://ccd-school.de/2017/06/stratified-design-over-
Frameworks. Eine Funktion wie File.ReadAllLines() ist dafür layered-design
ein triviales, dennoch passendes Beispiel. Die Produktivität
unserer Branche ist dramatisch gestiegen, weil wir Komposi-
tionen zu neuen Kompositionen vereint haben und so auf im- Ralf Westphal
mer höhere Ebenen der Einfachheit durch Abstraktion gestie- ist freiberuflicher Berater, Referent, Autor und
gen sind. Trainer für Themen rund um Softwarearchitek­
Leider hat das in den Softwarearchitekturmustern bisher tur und die Organisation von Softwareteams. Er
keinen Eingang gefunden. Meine Vermutung ist deshalb, ist Mitgründer von Clean Code Developer (CCD)
dass die sinkende Produktivität innerhalb von Projekten zu- und propagiert kontinuierliches Lernen.
mindest zum Teil darauf zurückzuführen ist. Es wird nicht info@ralfw.de
systematisch nach Kompositionen als Abstraktionen gesucht,
dnpCode A1809IODA
um produktiver zu werden. Da wird zwar von Wiederver-
36 9.2018 www.dotnetpro.de