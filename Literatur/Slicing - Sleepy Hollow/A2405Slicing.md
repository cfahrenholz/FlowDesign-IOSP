<!-- Page 1 of 8 -->


PLANUNG Slicing
ANFORDERUNGSANALYSE FÜR ENTWICKLER, TEIL 2
Den Stier bei den
Hörnern packen
Wie Sie die Komplexität beim Schreiben von Produktionscode mit einem iterativ-
inkrementellen testgestützten Vorgehen in den Griff bekommen.
Was ist der Zweck der Anforderungsanalyse? Die Ent- Um mit Iterationen möglichst schnell aus der Unsicherheit
wicklung von Verständnis. Nur mit Verständnis können zu kommen, sollten Anforderungen in überschaubare Ab-
Sie Code schreiben, der die Anforderungen erfüllt. Anforde- schnitte zerlegt werden, deren iterative Umsetzung zügig
rungen sind erfüllt, wenn der Code das gewünschte Verhal- verlaufen kann, am besten innerhalb von Stunden oder ma-
ten zeigt, also bei gegebenem Zustand auf Input mit erwar- ximal wenigen Tagen. Mit jedem Anforderungsabschnitt
tetem Output inklusive einer gegebenenfalls erwarteten Zu- wächst der Anteil der umgesetzten Anforderung, das heißt,
standsänderung reagiert. die Softwareentwicklung sollte inkrementell vorgehen –
Woher wissen Sie aber, dass Sie Anforderungen verstehen? wobei jedes Inkrement idealerweise für den Kunden einen
Indem Sie sie dem Product Owner (PO) oder Kunden „spie- kleinen Wertzuwachs der Software darstellt.
geln“, ihm also erzählen, was Sie meinen, verstanden zu ha- Um die Wartezeit bis zu einem Urteil über die Hypothese,
ben? Nein. Das kann nur eine erste Näherung sein, der Ver- dass eine Codeversion nun endlich tatsächlich die Anforde-
such einer Optimierung. rungen eines Abschnitts be-
Ultimativ zeigt sich Ihr Ver- friedigt, so kurz wie möglich
ständnis erst, wenn Ihr Code zu halten, sollten Überprü-
die Anforderungen erfüllt. fungen den Kunden nur sel-
Nicht weniger ist nötig, um ten involvieren. Ultimativ ist
den Kunden zu überzeugen. er natürlich die beurteilende
Wie stellen Sie fest, ob der Instanz, doch solide vorläufi-
Code tut, was er tun soll? Das ge Urteile lassen sich auch
können Sie nicht dem Kunden innerhalb des Softwaree nt-
überlassen. Denn bis der Code wicklungsteams fällen. Am
beim Kunden ist und dieser besten geschieht das durch
Gelegenheit hat, sich damit Wie soll ein automatisier- automatisierte Tests. Sie sind
auseinanderzusetzen, vergeht ter Test die von ChatGPT jederzeit reproduzierbar,
viel Zeit, in der es ungewiss g enerierte Domänenlogik nachvollziehbar, nicht sub-
ist, ob Ihr Aufwand erfolgreich überprüfen? (Bild 1) jektiv, schnell, analysierbar und dokumentierend. Die Mü-
oder vergeblich war. Solche Un- he, die zu ihrer Entwicklung aufgewendet werden muss,
gewissheit ist kein schöner emo- zahlt sich schnell aus. Nur automatisierte Tests skalieren
tionaler Zustand; vor allem aber führen längere Wartezeiten mit dem zunehmenden Aufwand, den die Vermeidung von
dazu, dass Sie beginnen, weitere Anforderungen umzuset- Regressionen erfordert (Stabilitätstests).
zen. Wartezeiten führen zu einer Erhöhung von Work-in-Pro-
cess (WIP), und das führt über kurz oder lang zu Unzuverläs- So weit die Rekapitulation des iterativ-inkrementellen testge-
sigkeit. Die Literatur zu diesem Zusammenhang ist reichlich; stützten Vorgehens der Agilität. Es bleibt allerdings noch e ine
Ihre persönliche Erfahrung sollte das ebenfalls bestätigen. Frage offen: Wenn Tests nicht manuell über die Benutzer-
Was folgt daraus? schnittstelle durchgeführt werden, wo setzen denn dann au-
Softwareentwicklung ist notwendig immer iterativ. Ein Ge- tomatisierte Tests im Code an?
fühl von Verständnis der Anforderungen führt nicht gerad- Automatisierte Tests setzen an Funktionen im Code an.
linig zu befriedigendem Code. Dafür sind realistische An- Bild 1 zeigt die Notwendigkeit dafür: Ist das Ergebnis, das der
forderungen zu komplex. Vielmehr ist jede Codelieferung Sparrechner ausgibt, korrekt? Ein Vergleich mit einem On-
nur eine Hypothese, die es zu überprüfen gilt. Wird sie fal- line-Sparrechner (Bild 2) lässt Zweifel aufkommen. Aber wie
sifizert, dann muss in einer nächsten Iteration die Abwei- soll ein automatisierter Test des Typescript-Codes punktge-
chung vom Soll verringert werden. nau an die Domänenlogik angelegt werden?
26 5.2024 www.dotnetpro.de
002266--003333__SSlliicciinngg__eeaa__ffss__eeaa..iinndddd 2266 2266..0033..2244 0099::4444


---


<!-- Page 2 of 8 -->


PLANUNG Slicing
Der Code für die Benutzerschnittstelle davor und danach
macht das schwer. Wenn jedoch Benutzerschnittstelle und
Domäne getrennt werden, ist eine punktgenaue „Testsonde“
möglich (Bild 3). Damit lässt sich die Reife des Domänencodes
(„Ist der Code schon korrekt?“) und die Stabilität des Domä-
nencodes („Ist der Code noch korrekt?“) einfach und zügig
jederzeit von jedermann überprüfen.
Eine Anforderungsanalyse, die auf solche Testbarkeit ab-
zielt, die also als Ziel hat, automatisiert testbare Funktionen
zu finden, nenne ich Slicing.
Jedes Slice ist ein Ab-Schnitt der Gesamtanforderungen,
ein Inkrement. Speziell an diesem Inkrement ist, dass es ganz
konkret drei Dinge benennt:
Welche Funktion wird konkret getriggert als Wurzel für die
Herstellung des gewünschten Verhaltens? (Es können auch
mehrere Funktionen sein.) In Bild 3 ist es zum Beispiel End-
betrag_berechnen. Vergleichsrechnung mit https://www.zinsen-berechnen.de/
Welche Signatur hat diese Funktion, und mit welchem Zu- sparrechner.php (Bild 2)
stand arbeitet sie? Die benötigten Datenstrukturen sind al-
so genau zu klären. Im Beispiel sind das das Input-Tupel
(sparbetrag:number, zinssatz:number, jahre:number) und nicht aus der Analyse mit konkreten Funktionssignaturen
der Output-Typ number; Zustand ist nicht im Spiel. und Testfällen herausgehen.
Welche Testfälle sollen erfüllt werden, um zu belegen, dass Im ersten Teil der Artikelserie [1] habe ich deshalb ge-
das Verständnis der Anforderung korrekt umgesetzt wur- schrieben: „Setzen Sie [dem User Story Template] ein eige-
de? Im Beispiel ist es das Input-Output-Paar ((100, 6, 12), nes Template für sich als Entwickler gegenüber, mit dem Sie
20901,86). (Der erwartete Wert stammt aus Bild 2. Die Annah- die Qualität von Anforderungen aus Ihrer Perspektive beur-
me ist, dass der Online-Sparrechner korrekt funktion iert.) teilen: ‚A function with signature <signature> to satisfy the
test <test case> by implementing <causal chain>.‘“
Slicing ist damit konkreter als die übliche agile Anforde- Das meine ich wirklich genau so. Meine Begründung ist
rungsanalyse. Über User Stories oder Use Cases oder andere meine Erfahrung, die mich gelehrt hat, dass weniger Präzi-
Anforderungsformen soll gerne in jeder Weise ausführlich sion und weniger Klarheit schnell zu Rückfragen führen. Und
gesprochen werden. Slicing steht dem nicht im Wege. Als Rückfragen bedeuten Wartezeiten. Wartezeiten kosten aber
Entwickler sollten Sie jedoch nicht zufrieden sein, solange sie nicht nur Geld, sondern verleiten auch zu einer lokalen ▶
Die Domänenl ogik
ist eingefasst in
eine Funktion, auf
die ein automati-
sierter Test ange-
setzt ist. So kann
schnell geprüft
werden, ob die
Verhaltenserwar-
tung an die Do-
mäne erfüllt wird
(Bild 3)
www.dotnetpro.de 5.2024 27
002266--003333__SSlliicciinngg__eeaa__ffss__eeaa..iinndddd 2277 2266..0033..2244 0099::4444


---


<!-- Page 3 of 8 -->


PLANUNG Slicing
Optimierung durch Beginn Wenn Sie Anforderungen
anderer Aufgaben. Das nicht so präzise schneiden
führt zur Vergrößerung von konnten, geht es weiter
WIP mit allen negativen mit Prototypen. Prototypen
Konsequenzen. Ich weiß, ich – in Code oder anderer Art –
wiederhole mich, doch dieser sind Analysehilfsmittel. Mit ih-
Zusammenhang ist so wichtig, nen unterstützen Sie den PO und
dass ich das für nötig halte. sich selbst dabei, die Anforderun-
Ganz davon zu schweigen, dass gen besser zu verstehen. Anforde-
ein PO oder Kunde durch Rückfragen rungen wollen auch entwickelt wer-
unterbrochen wird und sich schnell ge- den. Das Entwicklungsziel sind präzise
nervt fühlt. Das vergrößert die Spannun- Slices. Prototypen helfen Ihnen dabei,
gen im Team. indem sie bisheriges Verständnis greifba-
Mit weniger als solcher Präzision mit dem rer machen. Der PO oder Sie machen Be-
Entwurf und der Codierung zu beginnen ist Die Hierarchieebenen kanntschaft mit neuen Sichtweisen, spüren
eine Abkürzung, die leicht in eine Sackgasse des Slicing (Bild 4) Kon traste zum bisherigen Verständnis und
führt. Es ist eine vorzeitige Optimierung, um sich können erste Hypothesen darüber, was eigent-
nicht länger mit dem PO oder Kunden in Diskus- lich die wahren Anforderungen sind, leichtge-
sionen verhaken zu müssen. Außerdem macht alles nach der wichtig überprüfen. Prototypen sind getrennt von Produk-
Anforderungsanalyse mehr Spaß; dafür sind Sie Entwickle- tionscode. Mit Prototypen wird Produktionscode „nicht ver-
rin beziehungsweise Entwickler geworden, oder? wirbelt“ oder zumindest nicht verändert.
Doch es hilft nichts: Weniger Präzision rächt sich alsbald.
Dann ist der Codierspaß auch vorbei. Iterative Entwicklung gibt es für Code. Dort ist ihr Ziel, für
Also: Anforderungsanalyse für Softwareentwickler ist gegebene Anforderungen korrekten, befriedigenden Code
nicht nur inkrementell, sondern produziert so feine Schnitte, herzustellen.
dass jeder durch mindestens eine testbare Funktion inklus ive Iterative Entwicklung gibt es aber auch für Anforderun-
Testfällen spezifiziert ist. gen. Anforderungen selbst sind nicht korrekt, vollständig,
Das ist für mich der formale, sehr leicht zu erkennende verständlich, nur weil man bei einem Sprint-Planning „mal
Endpunkt einer Analyse. Dann können Sie aufstehen und darüber redet“. Verständnis kann man sogar für inkorrekte
den PO anderen Dingen überlassen. Sie sind bereit, den oder irrelevante Anforderungen entwickeln. Sie müssen also
Code hinter den „Triggerfunktionen“ der Slices zu entwer- verstehen, dass auch Anforderungen durch einen Schär-
fen und zu codieren. fungsprozess, durch Feedbackschleifen gehen müssen – vor
Dass Sie bei der Anforderungsanalyse mit Slicing Funk- und unabhängig von Code.
tionen, Signaturen, Testfälle im Hinterkopf haben, muss Korrekte, vollständige, relevante Anforderungen zu fin-
den PO übrigens nicht verwirren. Sie müssen ihm diese De- den, indem Iterationsschleifen inklusive Veränderung von
tails nicht aufdecken. Sie können trotzdem mit ihren Fragen Produktionscode durchlaufen werden, ist jedoch sehr teuer,
die Analyse so leiten, dass für Sie am Ende diese Präzision langwierig und belastet die Struktur des Produktionscodes.
herauskommt. Deshalb sollten Sie sensibel dafür sein, wann Anforderungen
noch nicht wirklich „gut“
Vom Wert der
sind. Solange das der Fall ist,
Protot ypen für die
sollten Sie ablehnen, für sie
Anforderungsanalyse
Produktionscode anzufassen.
Doch was, wenn solche Präzi- Iterationen zu ihrer Verbes-
sion sich bei allem Bemühen serung sind vor beziehungs-
nicht einstellen will? weise unabhängig von Pro-
Das ist misslich, aber kein duktionscode zu durchlau-
Beinbruch. Mangelnde Präzi- fen. Genau dafür sind Proto-
sion bei der Anforderungs- typen da.
analyse bedeutet nicht, dass Aber wie nun Anforderun-
Sie nicht weitermachen kön- gen als Entwickler angehen?
nen. Nur ist es ein anderer Welchem Weg folgen, wel-
Modus, in dem Sie fortfahren: che Methode anwenden, um
Wenn Sie Anforderungen das Ziel „A function with sig-
präzise „geslicet“ haben, nature <signature> to satisfy
geht es weiter mit Entwurf the test <test case> by imple-
und Codierung von Pro- Viele feine Schnitte durch die Hierarchie führen zu einer menting <causal chain>“ zu
duktionscode. i nkrementellen Entwicklung (Bild 5) erreichen?
28 5.2024 www.dotnetpro.de
002266--003333__SSlliicciinngg__eeaa__ffss__eeaa..iinndddd 2288 2266..0033..2244 0099::4444


---


<!-- Page 4 of 8 -->


PLANUNG Slicing
Slicing: Der Weg zur Funktion
Der Weg ist mit diesen Ebenen vorgezeichnet: Die Analyse
Ich schlage mit Slicing eine schrittweise Verfeinerung von beginnt beim System und endet beim Feature. Doch die Häu-
außen nach innen, von grob zu fein vor. Damit können Sie den figkeit, mit der einzelne Ebenen betrachtet werden, ist sehr
PO oder sogar Kunden an die Hand nehmen. Sie müssen ih- unterschiedlich. Um das ganze System oder um Contexts geht
nen nicht jedes technische Detail dabei verraten, auf das Sie es selten, sie sind vor allem initial das Thema. Um Interaktio-
aus sind. Sie können sie jedoch mit Grafiken unterstützend nen hingegen geht es ständig.
begleiten und sie so visuell durch den „Verfeinerungstrich- Nicht jedes Softwaresystem muss auch in gleicher Weise
ter“ führen. ausführlich auf jeder Ebene betrachtet werden. Je kleiner das
Die Hierarchieebenen sind (Bild 4): System ist, desto einfacher fallen Contexts, Apps, Workers,
System: Das gesamte Softwaresystem in seiner Umwelt im
Überblick.
Context: Das Softwaresystem, zerlegt in große thematische
Bereiche.
App: Ein Context, zerlegt in unterschiedliche, eigenständi-
ge Zugänge für Anwenderrollen.
Worker: Eine App, zerlegt in grobe selbstständige Einheiten
mit eigenen Schnittstellen für Mensch oder Software. Inkremente können nur iterativ umgesetzt werden; die Ergebnis-
Perspective: Ein Worker, betrachtet durch unterschiedliche se weichen am Ende oft von der ersten Idee ab (Bild 6)
Benutzerbrillen.
Dialog: Eine Perspective, zerlegt in thematisch fokussierte,
deutlich unterscheidbare „Fenster“ mit ihren Übergängen Perspectives aus; womöglich gibt es auf jeder Ebene nur ei-
beziehungsweise Verbindungen. ne Instanz, über die sogar nicht einmal näher gesprochen
Interaction: Die in einem Dialog triggerbaren Funktionen werden muss.
der Software mit ihren Ausgangspunkten und möglicher- Immer relevant sind allerdings das System als Big Picture
weise verschiedenen Endpunkten. und die Ebenen ab Dialog nach unten. Kein Softwaresystem
Entry Point: Die „Triggerfunktion“ hinter einer Interaktion ist zu klein, dass hier nicht näher hingeschaut werden könn-
mit konkreten Beschreibung der Nachrichten an/von eine(r) te und sollte.
„Triggerfunktion“ (Request, Response) und des für sie rele- Die Hierarchie soll Ihnen helfen, immer und immer wieder
vanten Zustands beziehungsweise ihrer Seiteneffekte. Schnitte (Bild 5) von oben nach unten, von außen nach innen
CQS Klassifizierung eines Entry Points gemäß Command- durchzuführen, um mit jedem Slice nur ein Feature eines En-
Query-Separation-Prinzip beziehungsweise Aufspaltung try Points umsetzen zu müssen. Wenn es fein geschnitten ist,
der „Triggerfunktion“ in mehrere Funktionen, die CQS- kann das zügig geschehen.
konform sind. Für jedes Feature, für jeden Entry Point, für jede Interak-
Feature: Die Anforderungen an eine „Triggerfunktion“ in tion ist dabei klar, was der größere Zusammenhang ist. Alle
feinere Inkremente zerlegen, ausgehend von ihren Nach- Feature-Slices sind eingebettet in ein Ganzes in unterschied-
richten und ihrem Zustand. licher Granularität. ▶
Vorschlag für ein Mapping der Slicing-Hierarchie auf entwicklerrelevante Strukturen (Bild 7)
www.dotnetpro.de 5.2024 29
002266--003333__SSlliicciinngg__eeaa__ffss__eeaa..iinndddd 2299 2266..0033..2244 0099::4444


---


<!-- Page 5 of 8 -->


PLANUNG Slicing
Die Analyse von pfeiler identifiziert
oben nach unten ver- werden sollten.
läuft iterativ. Die Anforderungsanaly-
Struktur jeder Ebene se läuft immer auf ein-
und ihre Slices ergeben zelne Funktionen mit
sich nicht einfach so, son- Signatur und Zustands-
dern wollen erarbeitet sein. information hinaus, um
Auf höheren Ebenen kann Testbarkeit zu garantieren.
sich auch durch Erkenntnisse
auf tieferen Ebenen etwas ver- Passen Sie gern alles andere an,
ändern; sogar die Implementa- aber behalten Sie diese beiden
tion eines Features kann sich nach Ebenen stets im Blick. Beide sollten
oben auswirken. Genauso ist die in jeder Anforderungsanalyse mit PO
Umsetzung eines Features selbst ite- oder Kunden ausgefeilt werden.
rativ, nicht geradlinig (Bild 6). Um das für Sie greifbar zu machen,
Die Ebenen der Hierarchie und das steige ich oben in der Hierarchie mit nä-
Vorgehen können POs und Kunden ver- Die Fixpunkte der Sli- heren Erläuterungen und Beispielen ein.
ständlich gemacht werden. Auch das Ziel ei- cing-Hierarchie (Bild 8)
Das System
ner glasklaren Vorstellung von der Anforde-
rung, die sich möglichst leicht ohne Rückfragen Aus ganz hoher Flughöhe betrachtet ist jedes
umsetzen lässt, werden PO und Kunden teilen. Softwaresystem zunächst „ein Ding“, eine Einheit ohne
Für Sie als Entwickler ist jedoch darüber hinaus interes- Struktur. Sie werden im Grunde beauftragt, eine Black Box
sant, dass jede Ebene eine technische Entsprechung hat. zu bauen, die in einer Umwelt einen bestimmten Dienst ver-
Bild 7 macht dafür einen Vorschlag. richtet (Bild 9).
Im Moment mag das für Sie etwas überwältigend erschei- Gewöhnlich sind die Anforderungen so umfangreich, dass
nen. Was sollen all die Ebenen? Muss das sein? Zum Glück Sie nicht einfach den Code hinschreiben können, der sie er-
ist die Antwort darauf: Nein, das muss nicht sein. Genauer: füllt, also die Logik. Nur Logik erzeugt ja Verhalten. Auch
Das muss nicht alles immer sein. deshalb müssen Sie die Black Box strukturieren. Das ist die
Die Hierarchieebenen stellen ein Angebot dar. Wenn Sie Aufgabe des Entwurfs. Die Mittel zur Strukturierung sind
sich bei der Anforderungsanalyse unsicher fühlen, können Module, zum Beispiel Klassen.
Sie daran Halt finden. Sie können sich fragen: „Wo bin ich?“, Die Frage, die sich im Entwurf stellt, ist: „Welche Module
„Wohin kann ich als Nächstes gehen?“ oder „Habe ich auch sollte es denn geben?“ Sie ist für nichttriviale Anforderungen
alles bedacht?“ schwer zu beantworten, und die Antwort ändert sich auch
Wenn Sie sich anschicken, einem SaaS-Platzhirsch wie über die Zeit. Deshalb sollten Sie jede Hilfe willkommen hei-
MailChimp seine Position streitig zu machen, tun Sie sicher ßen, die Sie bekommen können.
gut daran, sich sorgfältig von oben nach unten durch alle Slicing bietet dabei Unterstützung. Schon während der An-
Ebenen „zu graben“. Für den obigen Sparrechner jedoch forderungsanalyse erhalten Sie Hinweise auf Module, die es
sind zum Beispiel nur System, Dialog, Interaktion und Entry mindestens geben sollte. Weitere werden Sie während eines
Point relevant. Alles andere liegt auf der Hand. nachgelagerten expliziten Entwurfs finden (müssen).
Wer sich auf Slicing einlässt, wird ein Gefühl dafür bekom- Die „Basismodule“ für ein Softwaresystem ergeben sich
men, wann auf welcher Hierarchieebene eine weitere Anfor- aus der Kommunikation des Softwaresystems mit seiner Um-
derungsanalyse beginnen sollte. Am Anfang beginnt sie stets welt. Die Erfahrung hat gezeigt, dass es sich lohnt, dafür spe-
beim System. Doch wenn Sie sich von dort schon einmal bis zifische Module aufzusetzen.
zu Entry Points heruntergearbeitet haben, können Sie beim Kommunikation findet an der Grenze des Softwaresystems
nächsten Mal vielleicht bei schon gefundenen Interaktionen statt: Es hat einen Innenraum, in dem es das gewünschte Ver-
weitermachen oder in einen anderen Dialog einsteigen. halten mit Code herstellt. Und es existiert in einer Umwelt,
Die Hierarchie ist kein Korsett. Sie bietet vor allem Über- der es dient beziehungsweise aus der es Dienste benötigt
blick darüber, dass Software beziehungsweise Anforderun- (Bild 10).
gen überhaupt auf unterschiedlichen Abstraktionsebenen Jedes Softwaresystem dient Benutzern (User); das können
verstanden werden können, und macht einen konkreten Vor- Menschen oder andere Softwaresysteme sein.
schlag für solche Ebenen aus der Erfahrung heraus. Viele Softwaresysteme nutzen Ressourcen (Resource); das
Wenn Sie meinen, es gebe noch andere Ebenen, wenn Sie können Hardwareressourcen (zum Beispiel eine Festplatte
meinen, das gehe für Sie (meistens) zu weit oder nicht weit oder ein Timer) sein oder andere Softwaresysteme (etwa
genug … dann vertrauen Sie sich und verändern Sie die Hie- eine Datenbank oder SAP).
rarchie. Für mich gibt es dabei nur zwei Fixpunkte (Bild 8):
Anforderungsanalyse beginnt immer beim gesamten Sys- Das Softwaresystem, das Sie entwickeln sollen, ist abhängig
tem, in dem einige Aspekte als architektonische Grund- von Ressourcen, und seine Benutzer sind abhängig von ihm.
30 5.2024 www.dotnetpro.de
002266--003333__SSlliicciinngg__eeaa__ffss__eeaa..iinndddd 3300 2266..0033..2244 0099::4444


---


<!-- Page 6 of 8 -->


PLANUNG Slicing
Für diese stellt es selbst eine Ressource dar. Beachten Sie die Wie hilft diese Sicht bei der Strukturierung? Die Erfahrung
Beziehungslinien in den Grafiken ab Bild 9: Sie enden nicht zeigt, dass der Code, der für die Kommunikation nötig ist, im-
mit einer Pfeilspitze, wie sonst üblich, sondern in einem mer getrennt werden sollte von anderem Code. Ja: immer,
Punkt. Er drückt die Abhängigkeitsbeziehung aus. Dadurch stets, auf jeden Fall. Die Gründe dafür sind vielfältig: Testbar-
wird sie klar unterschieden von Datenflüssen, in denen kei- keit, Flexibilität, Verständlichkeit. Vor allem sollte das dafür
ne Abhängigkeiten bestehen. nötige API (oder Framework) vom restlichen System isoliert
Natürlich sind die Zahlen der Benutzer und Ressourcen be- werden; kontaminieren Sie nicht weite Teile Ihrer Codebasis
liebig. Allerdings gibt es immer mindestens einen Benutzer. mit solchen Details.
Ressourcen sind optional. Damit gibt es nun etwas zu sehen in der Black Box bezie-
Benutzer und Ressourcen können auch beliebig um das hungsweise im Black Circle (Bild 12):
Softwaresystem herum angeordnet werden, selbst wenn sich Die Kommunikation zwischen Benutzern und Softwaresys-
Benutzer auf der linken Seite und Ressourcen auf der rechten tem kapseln Module, die im Slicing Portal heißen.
eingebürgert haben und irgendwie angesichts der Abhängig- Die Kommunikation zwischen Softwaresystem und Res-
keitsverhältnisse intuitiv sind, die auf diese Weise von links sourcen kapseln Module, die im Slicing Provider heißen.
nach rechts weisen. Darüber hinaus gibt es stets Code, der das „Eigentliche“
Bei den Benutzern geht es nicht um konkrete – Peter, Paul, der Software ausmacht. Er ist (weitgehend) unabhängig
Maria –, sondern um Kategorien, zum Beispiel Sachbearbei- von der Umwelt und den Kommunikationskanälen. Das ist
ter, Spieler, Kunde. Benutzer haben eine Rolle gegenüber die Domäne, die ebenfalls in mindestens einem Modul ge-
dem System. kapselt werden soll. „Weitgehend“ unabhängig deshalb,
Die Kommunikation mit Benutzern und Ressourcen ist im weil es sein kann, dass gewisse Technologien insbesonde-
Grunde immer bidirektional: Requests fließen in die eine re in Providern erfordern, dass sich die Domäne anpasst. Sie
Richtung zum Dienstleister hin, Responses fließen vom kennt deshalb immer noch nicht das API, aber ist auf Kom-
Dienstleister zurück (Bild 11). munikationsmuster abgestimmt, die einen performan- ▶
Ein Softwaresystem
arbeitet nicht im luft-
leeren Raum, sondern
in einer Umwelt (Bild 9)
Ein Softwaresystem
kommuniziert mit seiner
Umwelt (Bild 10)
Auch wenn die
Abhängigkeit zwischen
System und Umwelt unidirektional ist, so
läuft die Kommunikaton doch bidirektional.
Wer abhängig ist, sendet Requests und erhält Die Standardstruktur jedes
Responses vom Dienstleister (Bild 11) Softwaresystems (Bild 12)
www.dotnetpro.de 5.2024 31
002266--003333__SSlliicciinngg__eeaa__ffss__eeaa..iinndddd 3311 2266..0033..2244 0099::4455


---


<!-- Page 7 of 8 -->


PLANUNG Slicing
ten/skalierbaren Umgang mit der Ressource via Provider Es ist erstaunlich, wie leicht hier etwas duch die Lappen ge-
leichter machen. hen kann. Gerne werden zum Beispiel die Uhrzeit oder ein
Zufallszahlengenerator als Ressource übersehen. Und mit ei-
Als Symbole für Portale und Provider – die beide Adapter ner genauen Vorstellung davon, was eigentlich die Domäne
sind – und Domäne haben sich Rechteck, Dreick und Kreis ist, hadern viele POs und Entwickler. Zur Erinnerung: In der
eingebürgert. Wenn Sie andere Symbole vorziehen, nutzen Beschreibung der Domäne kann keine Kommunikation mit
Sie eben die. Wichtig ist lediglich die visuelle und begriffli- der Umwelt vorkommen; die Domäne ist unabhängig von der
che Differenzierung. Umwelt. Zu ihr gehört höchstens, was übrig bleibt, wenn man
Slicing teilt diese Sicht auf ein Softwaresystem mit der vom Softwareverhalten die Kommunikation subtrahiert.
IODA-Architektur [2]. Das bedeutet, Portale und Provider „Höchstens“, weil es auch noch andere Belange als Kommu-
und Domäne sind innerhalb des Softwaresystems nicht von- nikation gibt, die zwar in Anforderungen auftauchen, doch
einander abhängig. Stattdessen werden sie von einem weite- nicht zum unverbrüchlichen Kern einer Software gehören,
ren Modul verbunden, der sogenannten Integration. Für sie etwa Sicherheit. Solche „supporting concerns“ verdienen
steht im Bild der Innenraum um die Module herum. Doch das ebenfalls Module – doch die ergeben sich nicht so einfach aus
ist ein Detail des Entwurfs und spielt für die Anforderungs- der Analyse; dafür ist der Entwurf zuständig.
analyse keine weitere Rolle.
Die Bewegung in der Slicing-Hierarchie
Wesentlich ist, dass dieses Bild vom Softwaresystem die
Analyse anleitet, zuerst die Benutzer in ihren Rollen und die Was kommt nach dieser „Systemerkundung“? Behalten Sie
Ressourcen zu sammeln. Das informiert den Entwurf, der auf immer das Ziel im Auge: einzelne „Triggerfunktionen“ mit
die Analyse folgt. Das hilft beim weiteren Fokussieren der Signaturen und Zuständen. Jetzt wissen Sie, dass diese Funk-
Anforderungsanalyse. tionen von Portalen ausgelöst werden. Dort finden die Inter-
Jedes dieser Module hat eine Schnittstelle. Besonders inte- aktionen mit den Benutzern statt. Die wollen etwas vom Sys-
ressant ist für eine Outside-in-Analyse die Benutzerschnitt- tem; das System erfüllt ihre Wünsche, wenn eine dafür zu-
stelle, also wie sich das Softwaresystem vermittels seiner Por- ständige Funktion im System angestoßen wird. Für die Über-
tale nach außen darstellt. Die Schnittstellen von Domäne und setzung der Benutzerwünsche in Funktionsaufrufe sind Por-
Providern sind Sache des Entwurfs. tale zuständig.
Dass seit Visual Basic 1.0 IDEs mit einem User-Interface- Nur weil Sie aber Benutzerrollen mit zugehörtigen Porta-
Designer so beliebt sind, ist sehr verständlich: Mit ihnen wur- len identifiziert haben, können Sie gewöhnlich nicht „einfach
de auch von außen nach innen die Implementation vorange- so“ eine Liste der „Triggerfunktionen“ aufstellen. In nichttri-
trieben. Die Eventhandler hinter den Steuerelementen wur- vialen Softwaresystemen sind das Hunderte oder Tausende.
den als Entry Points genutzt. Dahinter stand die richtige In- Deshalb bietet Slicing eine schrittweise Annäherung. So-
tuition – nur fehlten dabei die Systematik und das Bewusst- lange Ihnen nicht klar ist, welche „Triggerfunktionen“ nötig
sein für sauberen Code. Und so sind viele unwandelbare sind – und also die Anforderungsinkremente noch zu groß
Codebasen entstanden. Das will Slicing besser machen! sind für einen Start in die Produktionscodeentwicklung –,
Betrachten Sie eine solche „Sollstruktur“ eines Software- können Sie nicht anders, als das Softwaresystem gröber zu
systems als Checkliste. Während der Anforderungsanalyse zerlegen als in Funktionen. Wie grob, das müssen Sie ein-
können Sie immer wieder fragen: schätzen.
Kennen wir schon alle Benutzerrollen mit ihren unter- Ihr Bestreben ist es, so schnell wie möglich an die Ebene
schiedlichen Ansprüchen an das Softwaresystem? „Entry Point“ zu kommen. Wenn ein Sprung dahin nicht vom
Ist die Liste der Ressourcen schon komplett, von denen das System mit seinen Portalen möglich ist, überlegen Sie von un-
Softwaresystem abhängig ist? ten nach oben, ob Sie sich dafür bereit fühlen:
Verstehen wir schon wirklich, was die Domäne des Soft- „Wenn ich noch nicht weiß, welche konkreten Entry Points
waresystems ist? es geben soll, fühle ich mich dann zuversichtlich, zumindest
die Interaktionen der Benutzer mit dem Softwaresystem zu
Die Checkliste erinnert Sie jedoch nicht nur daran, dass Sie sammeln?“
nach Portalen und Providern suchen sollten, sondern legt Ih- „Wenn ich noch nicht klar sehe bei den Interaktionen, kann
nen auch nahe, deren Ausprägung zu analysieren. Zum Bei- ich mir wenigstens schon einen Überblick der Dialoge mit
spiel sollten Sie Antworten auf folgende Fragen mit dem PO ihren Verbindungen verschaffen?“
erarbeiten: „Wenn ich die Dialogebene noch überwältigend finde,
Welche Technologie soll zum Einsatz kommen? kann ich darüber strukturieren, indem ich verschiedene
Gibt es im Team schon Kompetenz für die erforderliche Perspektiven identifiziere, durch die Benutzer das System
Technologie? sehen und mit ihm interagieren?“
Wie sind die Interaktionsmuster an dieser Stelle zwischen Und so weiter.
System und Umwelt?
Welche nichtfunktionalen Anforderungen gelten an diesen Sehen Sie, wie Sie durch die Ebenen geleitet werden und auf-
Kontaktstellen (zum Beispiel Performance, Sicherheit)? steigen bis dorthin, wo Sie sich nach einem ersten System-
Wie sehen Datenstrukturen aus, die ausgetauscht werden? überblick schon wohl fühlen? Sie steigen dort in die Hierar-
32 5.2024 www.dotnetpro.de
002266--003333__SSlliicciinngg__eeaa__ffss__eeaa..iinndddd 3322 2266..0033..2244 0099::4455


---


<!-- Page 8 of 8 -->


chie ein und arbeiten sich nach unten vor, wo Sie meinen, ge-
nügend Informationen zu haben. Es gibt keinen Zwang, im-
mer alle Ebenen zu betrachten. Ihre Expertise und Ihr Ver-
ständnis der Anforderungen angesichts einer gewissen Sys-
temkomplexität bestimmen, welche Ebenen der Slicing-Hie-
rarchie für Sie hilfreich sind.
Die Hierarchie ist nur so tief, um Ihnen möglichst viele An- HANDS-ON-WORKSHOPS
laufpunkte zu geben. Für jeden Grad der Klarheit soll etwas
UND WEITERBILDUNG FÜR
dabei sein. Wichtig zu erinnern: Jede Ebene hat Bezug zu
SOFTWARE-ENTWICKLER UND
technischen Strukturen; es gibt ein Mapping, das Ihnen die
Übersetzung in Code erleichtern soll. Jede Ebene steht auch -ARCHITEKTEN
in einem Zusammenhang: Sie wissen genau, wie Sie an- TRAININGS
schließend fortfahren. Die Hierarchie ist ein Handlauf – in
beide Richtungen. Bei Klarheit bewegen Sie sich nach unten,
Architekturen für
bei Unklarheit steigen Sie zunächst auf, bis Sie sich eine Zer-
.NET-Anwendungen
legung in übersichtlichere Teile wieder zutrauen.
Trainer: David Tielke
Zusammenfassung
Natürlich wollen Sie so schnell wie möglich damit beginnen
können, Produktionscode zu schreiben, um Anforderungen
zu erfüllen. Doch Anforderungen sind meistens sehr umfang-
Async & Await
reich und auch noch unklar. Sie brauchen daher ein Vorge-
Trainer: Christian Giesswein
hen, das diese Komplexität bei den Hörnern packt. Mit einem
iterativ-inkrementellen testgestützten Vorgehen tun Sie das.
Wie aber finden Sie Inkremente? Wann wissen Sie, dass ein
Inkrement eine Mindestqualität hat? SignalR und
Im Slicing ist die Mindestqualität dadurch definiert, dass Event Signaling
Sie genau wissen, welche eine „Triggerfunktion“ an der Wur-
Trainer: Patrick Schnell
zel der Produktionscodehierarchie steht, die das Verhalten
eines Slices herstellt.
Zu diesen „Triggerfunktionen“ können Sie allerdings nicht
Azu re De v Ops – CI/ CD mit
„hinspringen“. Vielmehr müssen Sie sie durch eine schritt-
weise Verfeinerung der Anforderungen erarbeiten. Dazu lei- Azu re Pipe lines und Git
tet Sie die Slicing-Hierarchie an. Sie bietet Ihnen für jedes Trainer: Thomas Tomow
Gefühl von Klarheit einen Level, auf dem Sie mit einer wei-
teren Verfeinerung einsteigen können.
Ausgangspunkt ist immer das gesamte Softwaresystem in
Angewandte DevOps-Prozesse
seiner Umwelt. Erst wenn Sie darüber den Überblick haben –
für .NET Core Services
also insbesondere die Benutzer mit ihren Portalen identifiziert
Trainer: Michael Kaufmann
haben –, kennen Sie Ansatzpunkte für einen Abstieg durch
die Anforderungen in Richtung „Triggerfunktionen“. ◾
.NET MAUI –
[1] Ralf Westphal, Strukturiert zerlegen, dotnetpro 4/2024, Cross-Plattformentwicklung
Seite 42 ff., www.dotnetpro.de/A2404Slicing
leicht gemacht
[2] Ralf Westphal, IODA Architecture,
Trainer: Sebastian Seidel
www.dotnetpro.de/SL2405Slicing1
Mi cro soft Azu re
Ralf Westphal
ist Trainer, Berater und Mitgründer der Clean Cos mos DB
Code Developer Initiative (https://clean-code- Trainer: Thorsten Kansy
developer.de). Seine Schwerpunkte sind dauer-
haft hohe Produktivität für die Softwareent-
wicklung und zukunftsfähige Teamorganisation. REMOTE
https://ralfw.de TRAININGS MÖGLICH!
dnpCode A2405Slicing
developer-academy.de
Ihre Ansprechpartnerin: Susanne Herl
www.dotnetpro.de 5.2024 +49 731 88005-8835 • susanne.herl@ebnermedia.de
002266--003333__SSlliicciinngg__eeaa__ffss__eeaa..iinndddd 3333 2266..0033..2244 0099::4455
ddnnpp--00552244__DDeevvAAccaaddeemmyy__AAZZ__TTrraaiinniinngg__110022xx229977..iinndddd 7755 2255..0033..2244 1111::5522


| HANDS-ON-WORKSHOPS
UND WEITERBILDUNG FÜR
SOFTWARE-ENTWICKLER UND
-ARCHITEKTEN
TRAININGS
Architekturen für
.NET-Anwendungen
Trainer: David Tielke
Async & Await
Trainer: Christian Giesswein
SignalR und
Event Signaling
Trainer: Patrick Schnell
Azu re De v Ops – CI/ CD mit
Azu re Pipe lines und Git
Trainer: Thomas Tomow
Angewandte DevOps-Prozesse
für .NET Core Services
Trainer: Michael Kaufmann
.NET MAUI –
Cross-Plattformentwicklung
leicht gemacht
Trainer: Sebastian Seidel
Mi cro soft Azu re
Cos mos DB
Trainer: Thorsten Kansy
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
| Architekturen für
.NET-Anwendungen
Trainer: David Tielke
Async & Await
Trainer: Christian Giesswein
SignalR und
Event Signaling
Trainer: Patrick Schnell
Azu re De v Ops – CI/ CD mit
Azu re Pipe lines und Git
Trainer: Thomas Tomow
Angewandte DevOps-Prozesse
für .NET Core Services
Trainer: Michael Kaufmann
.NET MAUI –
Cross-Plattformentwicklung
leicht gemacht
Trainer: Sebastian Seidel
Mi cro soft Azu re
Cos mos DB
Trainer: Thorsten Kansy |  |



![A2405Slicing_p8_015](A2405Slicing_images/A2405Slicing_p8_015.png)



![A2405Slicing_p8_019](A2405Slicing_images/A2405Slicing_p8_019.png)



![A2405Slicing_p8_020](A2405Slicing_images/A2405Slicing_p8_020.png)
