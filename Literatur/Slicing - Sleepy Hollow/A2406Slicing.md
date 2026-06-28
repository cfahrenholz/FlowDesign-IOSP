<!-- Page 1 of 10 -->


PLANUNG Slicing
ANFORDERUNGSANALYSE FÜR ENTWICKLER, TEIL 3
Das Messer richtig ansetzen
Feine Schnitte durch die Anforderungen von der Interaktion bis zur CQS-Funktion.
Ziel der Anforderungsanalyse für Sie als Entwickler ist, Ih- einen Request für „die Maschinerie“ und deren Response
nen einen glasklaren Ansatzpunkt für den darauf folgen- in etwas Verständliches für den User.
den Entwurf und dann die Codierung zu geben. Sie müssen Jedes Frontend besteht in Bezug auf die Input-Output-Paa-
nicht nur das Gefühl haben, die Anforderungen zu verstehen, re, die es akzeptiert, jeweils aus einem Teil, der die Input-
sondern auch die Möglichkeit, den Code zu überprüfen, der Daten vom User sammelt (collect) und in einen Request für
daraus entstanden ist. Hat Ihr Gefühl guten Verständnisses die eigentliche Verarbeitung übersetzt, sowie einem Teil,
Sie getrogen, oder war es berechtigt? der deren Response zum User hin in verständlicher Weise
Eine solche Überprüfung kann nur skalierbar mit automa- projiziert (project). Sammlung und Projektion kompensie-
tisierten Tests erfolgen. Allein mit ihnen können Sie sowohl ren die Unfähigkeit beziehungsweise den Unwillen von
zügig die Reife des Codes in ganzer Breite für die aktuelle Usern, direkt mit verarbeitbaren Request-Response-Daten-
Anforderung feststellen („Habe ich die Anforderung schon strukturen umzugehen. Menschliche Benutzer wollen
erfüllt?“) wie auch die Stabilität des Codes in Bezug auf alle strukturierte Eingabefelder für ihren Input haben und nicht
vorher schon erfüllten Anforderungen („Werden alle anderen JSON-Datenstrukturen formulieren; sie wollen auch nicht
Anforderungen immer noch erfüllt?“). YAML interpretieren, sondern zum Beispiel eine 3D-Grafik
Automatisierte Tests erfordern als Ansatzpunkt eine Funk- mit den produzierten Daten sehen.
tion und Testfälle. Deshalb bin ich davon überzeugt,
dass das Ziel jeder Anforderungsanalyse eine Liste
von Funktionen mit präziser Signatur, aufgedeckten
Abhängigkeiten von Zustand beziehungsweise Res-
sourcen und Testfällen sein muss. Wenn Sie also mit
einem Product Owner (PO) oder Kunden über An-
forderungen sprechen, haben Sie immer im Blick,
dass Sie die Frage beantwortet bekommen: „Welche
Funktion soll ich implementieren?“
Diese Funktion nenne ich auch Triggerfunktion,
denn sie wird von Anwendern der Software im Rah-
men ihrer Interaktion durch eine Benutzerschnitt-
stelle angestoßen. Anwender wünschen sich von
Software ein gewisses Verhalten. Dazu „reizen“ sie Die grund-
die Software „an der Oberfläche“ und erwarten eine legende Code-
Reaktion: Input-Daten werden in irgendeiner Form struktur für die
eingegeben, eine Funktion wird ausgelöst, Output- Verarbeitung
Daten werden angezeigt. von Interaktio-
Jede Software ist ganz grundsätzlich in dieser nen (Bild 1)
Weise aufgebaut, vergleiche Bild 1. Dabei ist es un-
wesentlich, ob ihre Nutzer Menschen oder andere
Software sind.
User stellen an Software vermittels deren Front-
end eine Anfrage (Input) und bekommen von der
Software ein Ergebnis (Output). Ob das Frontend
konsolenbasiert ist, ein GUI hat, eine HTML- Seite
ist oder einen REST-Endpunkt veröffentlicht, ist
einerlei.
Das Frontend ist der Vermittler zwischen dem User
in der Umwelt der Software und „der Maschine-
rie“ in der Software, die für ihn die wahre Black-
box ist. Dort wird das gewünschte Verhalten er-
zeugt. Das Frontend übersetzt dazu die Anfrage in
34 6.2024 www.dotnetpro.de
003344--004433__SSlliicciinngg__eeaa__ffss__eeaa__ffss..iinndddd 3344 2299..0044..2244 1100::0011


---


<!-- Page 2 of 10 -->


PLANUNG Slicing
Die immer relevanten
Ebenen der Anforderungs-
analyse (Bild 2)
Der von der Sammlung zusammengestellte Request wird Die drei Ebenen sind in jedem Softwaresystem im Spiel. In
an eine Funktion im Inneren der Software zur Verarbeitung jeder Anforderungsanalyse ist es mithin zentral, Folgendes
(process) übergeben, die anschließend mit einem Respon- zu identifizieren:
se antwortet. Es kann sein, dass diese Funktion der Black- Wer sind die Benutzer des Systems, und über welche Art
box auf internen oder externen Zustand (state) lesend und/ von Frontend wollen sie mit ihm interagieren? Die Antwort
oder schreibend zugreift. besteht aus einer Anzahl von Portalen mit zugehörigen
Technologien.
Wie Sie sich denken können, ist die Funktion, die ich mit Trig- Welche Interaktionen sollen zwischen Benutzern und Sys-
gerfunktion bezeichne, in Bild 1 process(). Wenn sie aufgeru- tem ablaufen? Wie wollen User „das System reizen“, um
fen wird, sind die Feinheiten der Request-Sammlung abge- ihm das gewünschte Verhalten zu entlocken? Die Antwort
schlossen, bei der die Frontend-Technologie eine Rolle spielt, besteht aus einer Anzahl von technologiespezifischen
die schlecht automatisiert zu testen ist. Und die Feinheiten Frontend-Elementen.
der Projektion von Ergebnissen für den User mittels Front- Welche Form soll die in jeder Interaktion getriggerte Funk-
end-Technologien, die schlecht zu testen sind, spielen auch tion haben? Die Antwort besteht mindestens aus einer ▶
für sie keine Rolle; sie sind nachgelagert in der Interaktion.
In Bezug auf die im zweiten Teil der Artikelserie [1] vorge-
stellte Slicing-Hierarchie sind damit drei Ebenen im Blick
(Bild 2):
Im Gesamtsystem ist verortet, dass und wo Benutzer mit
ihm umgehen. Das geschieht immer durch einen Adapter,
der Portal genannt wird. Dieses Portal kapselt die
Details von Sammlung und Projektion. Es ist
strikt vom Code zu trennen, der die eigentliche
Arbeit der Transformation von Input in Output Das gesamte
übernimmt. Software-
Jede Input-Output-Wandlung findet im Rahmen system im Blick
einer Interaktion statt, die innerhalb eines Portals zu Beginn der
verortet ist. Outside-in-An-
Und jede Interaktion triggert eine Funktion, den forderungsanalyse
Entry Point für die Verarbeitung des Inputs, der entlang der Slicing-
in Form eines Requests angeliefert wird. Hierarchie (Bild 3)
www.dotnetpro.de 6.2024 35
003344--004433__SSlliicciinngg__eeaa__ffss__eeaa__ffss..iinndddd 3355 2299..0044..2244 1100::0011


---


<!-- Page 3 of 10 -->


PLANUNG Slicing
Funktionssignatur. Um automatisierte Tests dort ansetzen
zu können, muss allerdings auch geklärt sein, welcher Zu-
stand wie von der Funktion gebraucht wird. Außerdem sind
dazu passende Testfälle zu sammeln. Hier geht es um die
Entry Points.
Interaktionen
Auch wenn eine Hierarchie die Entwicklung des Verständ-
nisses von einem Ende her nahelegt – entweder top-down
oder bottom-up –, möchte ich für die Erkundung der Slicing-
Hierarchie anders vorgehen.
Die oberste Ebene des Big Picture hat der vorherige Arti-
kel [1] beschrieben: Dort oben geht es ums ganze Software-
system (Bild 3). Benutzer wollen gewöhnlich in vielerlei Weise mit einer Software
Im Sinne einer Outside-in-Analyse soll zunächst geklärt durch ein Portal interagieren. Welche Interaktionen nötig sind,
werden, welcher Kontaktpunkte mit der Umwelt es bedarf. können sie allerdings nicht einfach aufzählen (Bild 4)
Denn jedes Softwaresystem hat nur einen Zweck in Bezug
auf seine Umwelt, das heißt für seine User. Ihr Bedarf treibt
Verhalten und Struktur im Inneren des Softwaresystems. Aufgaben sollen in Listen angelegt werden können.
Immer. Deshalb Outside-in-Analyse. Wenn eine Aufgabe überfällig ist, soll daran erinnert
Darüber hinaus kann jedes Softwaresystem diesen Bedarf werden.
nur erfüllen, wenn es Zugriff auf alle nötigen Ressourcen in
der Umwelt hat. Diese Abhängigkeiten müssen also auch Zählen Sie jetzt einfach nur die Interaktionen auf, die Ihnen
von Anfang gesammelt werden. dazu einfallen. Eine Interaktion ist eine Antwort auf die Fra-
ge: Wann soll was passieren?
Wie es nach einer solchen initialen Analyse weitergeht, hängt Welche Interaktionen stehen in Ihrer Liste? Ich komme
allerdings von der Komplexität eines Softwaresystems ab. nach der sehr knappen Anforderungsbeschreibung mindes-
Kann nur ein kleiner Schritt gemacht werden, weil die Anfor- tens auf diese:
derungen so umfangreich sind? Oder kann in der Hierarchie Liste einrichten
tiefer gesprungen werden, weil schon Klarheit herrscht? Liste umbenennen
Für mich ist ein Kriterium für die Sprungtiefe, inwiefern ich Liste löschen
wichtige beziehungsweise interessante Entry Points erken- Listen anzeigen
nen kann. Liegen die auf der Hand, muss ich mich nicht Liste auswählen, um sie mit ihren Aufgaben anzuzeigen
zwangsläufig durch Context, App und so weiter nach unten Aufgabe einrichten in einer Liste
graben. Aus diesem Grund springe ich auch mit der Beschrei- Aufgabe bearbeiten
bung der Slicing-Hierarchie nun über einige Ebenen hinweg Aufgabe löschen
zu den Interaktionen. Zu denen haben Sie sofort einen Bezug; Benachrichtigen über überfällige Aufgabe
damit kann ich Sie hoffentlich auf den Haken nehmen für
eine spätere Reise zu höherliegenden Ebenen. Das sind vor allem grundlegende CRUD-Interaktionen. Nicht
Interaktionen sind das sichtbare und technologische Pen- spannend, da steckt keine Kreativität drin – dennoch darf kei-
dant zu Entry Points. Wo ein Entry Point immer nur eine Funk- ne vergessen werden und der Code dazu muss fehlerfrei sein.
tion darstellt, die nur Sie als Entwickler interessiert, ist eine Aber es gibt noch weitere Interaktionen:
Interaktion etwas, das für den Benutzer unmittelbar relevant Programm starten
ist. Er kann sie sehen und spüren. Ein Mausklick, ein Tasten- Aufgabe in einer Liste verschieben
druck, eine Geste kann eine Interaktion starten, die durch Liste in der Liste der Listen verschieben
eine Reaktion der Software mit einer Ausgabe in Form von Programm beenden
Text, Bild, Ton oder auch noch anderen Modalitäten endet.
Die unmittelbar einleuchtende Frage an POs, Benutzer und Was noch? Ist Ihnen noch etwas eingefallen? Nein? Das be-
Kunden während der Anforderungsanalyse ist deshalb: „Wel- deutet nicht, dass es nicht weitere Interaktionen gibt. Welche
che Interaktionen wünscht ihr euch denn?“ das sind, kann nur ein Gespräch mit dem Kunden oder PO er-
Leider ist die Antwort auf diese Frage meistens unmöglich. geben.
Interaktionen in nicht trivialer Software sind einfach so zahl- Worin unterscheidet sich das von der üblichen Anforde-
reich. Sie gehen in die Hunderte, gar Tausende (Bild 4). Sie rungsanalyse? Im Ziel! Ziel des Gesprächs ist immer eine Lis-
lassen sich nicht aus dem Stand aufzählen. Selbst ein kleines te von Triggerfunktionen, denn diese stehen hinter den Inter-
Beispiel macht schon deutlich, wie schwierig es ist, sie zu aktionen. Deshalb sollte nach meiner Ansicht jede Anforde-
identifizieren. Als Szenatio mag eine Aufgabenverwaltung rungsanalyse das Ziel haben, dem PO die Liste der Inter-
dienen: aktionen zu entlocken. Auf welchem Weg auch immer.
36 6.2024 www.dotnetpro.de
003344--004433__SSlliicciinngg__eeaa__ffss__eeaa__ffss..iinndddd 3366 2299..0044..2244 1100::0011


---


<!-- Page 4 of 10 -->


PLANUNG Slicing
Hier sind typische Fragen, mit deren Hilfe Sie das Gespräch
leiten können:
„Welche Buttons möchtest du klicken können?“
„Welche Menüpunkte brauchst du?“
„Sollen Tastendrücke bei Eingabe der Daten das Verhalten
auslösen?“ Ein Eventhandler ruft einen Entry Point (Bild 6)
„Wann und wie soll Verhalten X eigentlich ausgelöst
werden?“
„Kommt es zu Verhalten Y durch einen ‚Reiz‘ des Anwen- die Triggerfunktionen gearbeitet werden, wenn die Entry
ders oder automatisch?“ Points präzise definiert sind. Das Vorgehen mit Slicing wirkt
auf diese Weise produktivitätsfördernd: In Arbeitsteilung
Alle laufen darauf hinaus, dass der PO ganz konkret werden können unabhängige Bereiche unabhängig vorangetrieben
muss. Das ist wichtig! Nur wenn er konkret wird, kann es werden.
Klarheit für Sie geben. Je umfangreicher die Anforderungen, Bei Webanwendungen passiert das in gewisser Weise
desto weniger kann ein PO allerdings dazu früh in der Ana- selbstverständlich durch die Schnittstelle zwischen Frontend
lyse sagen. Deshalb die Slicing-Ebenen oberhalb der Interak- (HTML/JS) und zum Beispiel REST-Backend. Ich plädiere je-
tionen. Doch dazu später mehr. doch dafür, auch innerhalb eines solchen Frontends noch ge-
Manchmal ist die Entscheidung, ob ein Verhalten durch nauer hinzuschauen. Mehr dazu, wenn wir auf die Worker-
Klick auf einen Button oder Menüpunkt ausgelöst werden Ebene der Slicing-Hierarchie schauen.
soll, natürlich nicht so wichtig. Vor allem geht es darum, die Ab einem gewissen Punkt wird das vereinfachte UI natür-
Auslösung des einen Verhaltens vom anderen zu unterschei- lich auch umständlich. Seien Sie sensibel für die Grenze zwi-
den. Insofern ist es auch nicht immer wichtig, sofort die fina- schen Nutzen und Nachteil. Vor allem wollte ich dadurch
le Benutzerschnittstelle zu kennen. Es kann auch mit einer klarmachen, welche Optionen es eröffnet, wenn die Anforde-
prototypischen Benutzerschnittstelle angefangen werden. rungsanalyse sich von vornherein auf die Herausarbeitung
Wieder das Beispiel Aufgabenverwaltung: Nach Klärung von Interaktionen konzentriert:
der Interaktionen wird das Verhalten implementiert, doch die Der PO wird zu Klarheit gezwungen.
Benutzerschnittstelle ist lediglich in der Konsole. Dort ist sie Ein beteiligter UX-Designer beziehungsweise UI-Techno-
sehr einfach und ohne spezielle UI-Technologiekenntnisse zu logiespezialist kann bei der Entscheidung helfen, damit
implementieren. Die Interaktionen werden durch Komman- optimale Interaktionen und dahinter Triggerfunktionen
doeingaben angestoßen (Bild 5). Mit einem solchen Frontend- entstehen.
Prototyp fällt die Konzentration auf das Wesentliche leichter: Sie als Entwickler bekommen bestmögliche Startpunkte für
die Domänenlogik. Sie steht hinter den Triggerfunktionen. Entwurf und Implementation von Code.
Später kann das Frontend – Sammlung und Projektion –
ausgetauscht werden, ohne den getesteten Code hinter den Ein weiterer zu berücksichtigender Punkt bei der Entwick-
Triggerfunktionen anfassen zu müssen. Es kann am Produk- lung der Interaktionen – denn nicht weniger ist es als eine
tionsfrontend auch parallel zur Verhaltenserzeugung durch Entwicklung; Interaktionen müssen aus den Vorstellungen
über das Softwareverhalten herausgeschält werden – ist der
Zustand des Frontends.
Hält das Frontend selbst Zustand, oder bekommt es immer
alle nötigen Daten von den Triggerfunktionen? Schauen Sie
Bild 5 erneut an. Aus der Systemanalyse ist klar geworden,
dass es mindestens zwei Codeteile gib, nämlich
das Frontend und
den Rest, die Blackbox dahinter, die getriggert wird.
Nach dem Kommando lc Liste 2 zeigt es die Liste der bisher
angelegten Listen für Aufgaben an. Welcher der beiden
Codeteile kennt diese Liste? Es ist anzunehmen, dass die
Blackbox die Listen kennt und verwaltet, wahrscheinlich so-
gar persistent. Wie soll dann die Triggerfunktion aussehen?
Zwei Varianten als Beispiel:
list_create(name:string):List
list_create(name:string):List[]
Eine Diskussion, ob List ein Domänendatentyp ist oder nur ei-
Prototypische Benutzerschnittstelle für eine Aufgabenverwal- ner für die Schnittstelle zwischen Frontend und Blackbox, er-
tung (Bild 5) spare ich Ihnen an dieser Stelle. Mir geht es darum, ob nur ▶
www.dotnetpro.de 6.2024 37
003344--004433__SSlliicciinngg__eeaa__ffss__eeaa__ffss..iinndddd 3377 2299..0044..2244 1100::0011


---


<!-- Page 5 of 10 -->


PLANUNG Slicing
Triggerfunktion und Entry Point sind dasselbe auf unterschiedlichen Ebenen der Slicing-Hierarchie (Bild 7)
die neu angelegte Liste oder alle Listen zurückgegeben wer- Eventhandler lassen sich nicht gut testen. Bei einer echten
den sollen. Trennung von „Model“ wie bei WPF sieht es besser aus, den-
Wenn es immer alle sind, benötigt das Frontend keinen ei- noch rechne ich zum Beispiel ein dortiges Command immer
genen Zustand, um als Reaktion auf lc alle Listen aktualisiert noch zur UI-Technologie. Darin darf nicht die Musik spielen,
zu zeigen. Wenn hingegen nur die neu angelegte zurück- die automatisiert getestet werden muss.
kommt, muss es sich zumindest die Namen aller anderen Lis- Triggerfunktionen sind mithin Funktionen, die getrennt
ten gemerkt haben, um sie anzeigen zu können. von Eventhandlern existieren. Sie gehören „zum Rest“ der
Ich will hier keiner der Varianten den Vorzug geben. Software und könnten von Eventhandlern aufgerufen wer-
Manchmal ist nur eine möglich, manchmal liegt eine nahe. den (auch wenn ich eine andere Anbindung vorziehe; doch
Welche Variante ist für die eine Interaktion günstig, welche das ist ein Detail).
für die andere? Im Slicing sähe ein Eventhandler wie in Bild 6 aus: Er küm-
Wichtig ist vor allem, dass im Rahmen der Interaktionsent- mert sich um die Sammlung von Input, um den Request zu
wicklung genau darüber gesprochen wird. Welche UI-Tech- schnüren. Er ruft die Triggerfunktion. Er kümmert sich um die
nologie soll genutzt werden, welche Herangehensweise un- Projektion des Response vom Entry Point.
terstützt sie? Zumindest Sie als Entwickler müssen sich darü- Bei HTTP-Endpunkten sind Sammlung und Projektion oft
ber Klarheit verschaffen. Davon hängt die Form der Trigger- trivial, weil sie von der Infrastruktur übernommen werden.
funktion ab. Das können Sie dankend annehmen. Doch der Controller
bleibt ein Adapter, der Verhalten nicht selbst erzeugt, son-
Entry Points
dern dafür den eigentlichen Entry Point aufruft.
Interaktionen finden dort statt, wo Anwender Ihre Software Was unterscheidet den Begriff Triggerfunktion von Entry
„reizen“. Heutzutage geschieht das oft im Rahmen von Point (Bild 7)? Es geht um dieselbe Funktion. Im Rahmen der
Events, die von Eventhandlern bedient werden. Das ist seit Diskussion um die Interaktionen ist diese Funktion aber noch
Visual Basic 1.0 (VB) so.
Der Erfolg von VB ist aus meiner Sicht zu einem guten Teil
darauf zurückzuführen, dass die Integration der Benutzer-
schnittstellengestaltung mit der Codierung des Verhaltens so
eng war. Wer wusste, wie das UI aussah, hatte sofort eine sim-
ple Grundstruktur für den Code: Jedem Button, jedem Menü-
punkt und so weiter stand sofort eine Funktion gegenüber, in
die Logik „gekippt“ werden konnte, die das getriggerte Ver-
halten erzeugte. Das war der Hit! Dass das leider nicht auto-
matisch zu sauberem Code führte, mussten Entwickler erst
leidvoll lernen.
Deshalb muss ich noch einmal klarstellen: Mit Entry Points
meine ich keine Eventhandler einer Benutzerschnittstellen-
technologie! Eventhandler-Funktionen sind technologiespe-
zifisch und gehören zum Portal als Adapter für die Verbin-
dung zwischen der Umwelt und der Innenwelt des Soft-
waresystems. Die Entry Points eines Teils der Aufgabenverwaltung (Bild 8)
38 6.2024 www.dotnetpro.de
003344--004433__SSlliicciinngg__eeaa__ffss__eeaa__ffss..iinndddd 3388 2299..0044..2244 1100::0011


---


<!-- Page 6 of 10 -->


PLANUNG Slicing
Auf der Ebene der Entry Points wird es wirklich relevant,
dass Sie sich Gedanken über die Zustandshaltung machen:
Frontend oder Blackbox? Dies hat Einfluss auf die Signatur
des Entry Points, wie oben gezeigt.
Ich tendiere dabei zu besserer Testbarkeit. Meine Frage ist:
Wie kann ich mehr Code leichter testen? Code im Frontend
ist tendenziell schwerer zu testen, also versuche ich ihn zu mi-
nimieren. Wenn also Zustandshaltung im Frontend Aufwand
bedeutet, ziehe ich den Code lieber in die Blackbox, wo er
unabhängig von Frontend-Technologie testbar ist.
Wenn die Zustandshaltung im Frontend hingegen trivial
ist, deklarativ beziehungsweise intentional funktioniert und
keinen (testwürdigen) Code braucht, dann lasse ich Zustand
auch mal im Frontend. Das erspart mir Datenverkehr mit der
Blackbox. Die Entry Points können sich mehr auf das Wesent-
liche konzentrieren. Wenn zum Beispiel die Listen einer Auf-
gabenverwaltung in einer GUI-Liste einer Desktop-Anwen-
dung angezeigt werden sollen, erübrigt sich eine Zustands-
haltung in der Blackbox jenseits der zu leistenden Persistenz.
Auch hier ist wieder zu sehen, wie UI/UX-Entscheidungen
nach innen wirken. Die Blackbox, also den Kern eines Soft-
waresystems, gänzlich unabhängig von der Umwelt, von den
Interaktionen, von den Frontend-Technologien zu halten, ist
eine durchaus schädliche Optimierung. Natürlich soll die
konkrete Nutzung von UI-Frameworks in Portalen gekapselt
sein – doch deren Paradigma darf nach innen wirken.
Das muss allerdings eine bewusste Entscheidung sein.
Denn je mehr die äußere Form nach innen wirkt, desto ab-
hängiger ist das Innen natürlich. Die äußere Form zu wech-
seln mag dadurch erschwert werden. Hier ist eine Balance
zwischen Effizienz und Flexibilität zu finden.
Oben habe ich eine Anzahl von möglichen Interaktionen
einer Aufgabenverwaltung gelistet. Zu jeder gehört eine
Triggerfunktion. Hier nochmal ein Auszug:
Liste einrichten: list_create()
Liste umbenennen: list_rename()
Liste löschen: list_delete()
Listen anzeigen: lists_all()
Alle Entry Points Programm starten: program_start()
werden in einem
Szenariotest über- Das ist trivial und bedarf eigentlich keiner Dokumentation
prüft (Bild 9) oder sogar Erwähnung. Das haben Sie immer im Hinterkopf.
Nur die letzte Interaktion lässt fragen, ob sich eine eigene
Triggerfunktion lohnt oder vielleicht bei Programmstart lists_
relativ schwammig. Vor allem ist wichtig zu verstehen, dass all() aufgerufen werden könnte. Um eine vorzeitige Optimie-
es sie gibt und mit welchen Daten sie grundsätzlich arbeitet: rung zu vermeiden, würde ich allerdings dafür plädieren, zu-
Es muss einen Request aus einer Input-Sammlung geben. nächst mit program_start() zu planen. Vielleicht ergibt eine
Es wird ein Response geliefert. spätere Analyse, dass bei Programmstart noch mehr oder et-
Es ist vielleicht Zustand/ein Seiteneffekt im Spiel. was anderes getan werden soll, als nur die Aufgabenlisten zu
listen.
Bei der Ebene des Entry Points darunter geht es um die Ver- Für den Level „Entry Points“ in der Slicing-Hierarchie ist
feinerung dieser Funktion: Wie genau sieht die Signatur aus? nun etwas mehr Detail gefragt: Wie soll denn die Signatur
Welche Daten sollen in welcher Struktur in den Entry Point ganz präzise aussehen? Ich zeige Ihnen einfach meine Ent-
hineingegeben werden, welche kommen am besten heraus, scheidungen und verzichte auf eine Diskussion, warum sie so
welche braucht er woher darüber hinaus, und auf welche hat ausgefallen sind. Es geht hier nicht darum, die absolut beste
er welchen Einfluss? Erst wenn das geklärt ist, können auch Signatur zu erarbeiten, sondern den Unterschied zwischen
Testfälle bestimmt werden. den Levels bei Slicing zu verdeutlichen. ▶
www.dotnetpro.de 6.2024 39
003344--004433__SSlliicciinngg__eeaa__ffss__eeaa__ffss..iinndddd 3399 2299..0044..2244 1100::0011


---


<!-- Page 7 of 10 -->


PLANUNG Slicing
Bild 8 zeigt die Entry Points für die
obigen Triggerfunktionen, wie
ich sie mir beispielhaft vor-
stelle. Sie sehen, ich habe
mich dafür entschieden,
das Frontend durchaus
Zustand halten zu lassen.
Jetzt sind alle Funktio-
nen mit Parametern und
Typen versehen. Zustand ist
implizit. Die Sprache ist Type-
script. Eine Klasse habe ich für die
Blackbox nicht angelegt. Die Funktionen
werden einfach von einem dateibasierten Mo-
dul exportiert. Ob das die beste Idee ist, lasse ich
dahingestellt. Es soll nicht um die Feinheiten des Ent-
wurfs und der Modularisierung gehen, sondern dar um, dass
die Entry Points eben eine Schnittstelle darstellen, die dem
Frontend bekannt ist. Die Entry Points isolieren die Blackbox
von der Umsetzung der Interaktionen mit dem Benutzer.
Zu den konkreten Schnittstellen gehören natürlich auch
Datentypen. List als Struktur für eine Aufgabenliste ist Teil Sprünge sind in der Slicing-
der Schnittstelle, die die Entry Points definieren. Und was ist Hierarchie erlaubt, sobald
mit den persistenten Daten? Klarheit über die Zerlegung
Die persistenten Daten sind nicht Teil der Schnittstelle. Von einer Ebene herrscht (Bild 10)
ihnen eine Idee zu haben ist nicht falsch. Sicher werden sie
in diesem Fall nah an List sein. Doch ich denke, für die For-
mulierung von Testfällen, die ja auch noch fehlen, sind die Die Listen werden alle abgerufen.
persistenten Daten gar nicht so wichtig. Überhaupt ist Persis- Es wird noch eine Liste hinzugefügt.
tenz nicht entscheidend, um ein Frontend an eine Blackbox Die Listen werden wieder abgerufen.
mit dieser Oberfläche zu binden. Sie muss nur zusichern, den Eine Liste wird umbenannt.
Zustand korrekt zu bewahren. Eine andere Liste wird gelöscht.
Jeder Entry Point könnte einzeln getestet werden. In die- Die Listen werden wieder abgerufen.
sem Fall glaube ich jedoch, dass ein „Szenariotest“ einfacher
ist. So nenne ich einen Test, der mehrere Funktionen im Ver- Zu jedem Schritt lassen sich Erwartungen formulieren. Bild 9
ein auf die Probe stellt. Ein Szenariotest simuliert eine Folge zeigt alle Entry Points in einem solchen Zusammenspiel. Dass
von Interaktionen, zum Beispiel
Das Programm wird gestartet; noch gibt es keine Listen.
Es wird eine Liste hinzugefügt.
Nicht alle Entry Points sind nur Command oder nur Query (Bild 11) Potenzial für Refaktorisierung im Sinne von CQS (Bild 12)
40 6.2024 www.dotnetpro.de
003344--004433__SSlliicciinngg__eeaa__ffss__eeaa__ffss..iinndddd 4400 2299..0044..2244 1100::0011


---


<!-- Page 8 of 10 -->


die Implementation dahinter derzeit nur In-Memory Zustand
hält, ist für das Prinzip, um das es mir hier geht, unerheblich.
Die Anforderungen des Beispiels haben es erlaubt, schnell
auf eine ganze Reihe von Interaktionen mit ihren Entry Points
zu kommen. Manchmal ist das möglich. In anderen Fällen er-
geben sich für zum Beispiel eine User Story mehrere Interak-
tionen, doch die können nicht alle näher betrachtet werden HANDS-ON-WORKSHOPS
(breadth-first), sondern auf eine der Interaktionen ist beson-
UND WEITERBILDUNG FÜR
ders die Aufmerksamkeit zu lenken (depth-first), um für sie
SOFTWARE-ENTWICKLER UND
Signatur, Zustand/Seiteneffekte und Testfälle zu definieren.
Wie sehr sie in die Breite gehen, ist auch für die Methode -ARCHITEKTEN
OFFENE
unerheblich. Letztlich sollen Sie bei einem Entry Point an-
TRAININGS!
kommen, dessen Ausgestaltung Ihnen erlaubt, dahinter mit
Entwurf und Codierung zu beginnen. Und dann ist der nächs-
Unsere öffentliche
te Entry Point dran, und danach der nächste und so weiter.
Der Weg zu den Entry Points für die kleine Beispielsoftware
Hands-on Workshops
bestand aus drei Sprüngen in der Slicing-Hierarchie (Bild 10):
Der Einsprung erfolgt für die System-Ebene. Dort geht es
sind wieder da.
immer los: Überblick gewinnen, Frontends identifizieren.
Da das Beispiel so klein ist, sind wir sofort zur Interaktion-
Ebene gesprungen. Wir konnten alle Interaktionen ohne
weiteres aufzählen.
In 2024 können Sie folgende
Für jede Triggerfunktion hinter den Interaktionen haben
Workshops buchen
wir dann den Sprung zur Entry-Point-Ebene gemacht.
Sprünge über Ebenen hinweg sind okay, wenn das, was auf C# für Fortgeschrittene
der nächsten Ebene gesucht wird, auf der Hand liegt. Das war
27.-29.05.2024
bei den Interaktionen für die Aufgabenverwaltung klar. Zu
den Entry Points weiterzugehen war der nächste nötige
UX und UI-Design
Schritt.
Was aber nun? Können wir schon mit den Entry Points zu- für Entwickler 11.-12.06.2024
frieden sein? Wenn die dahinterstehende Funktionalität
überschaubar ist, ja. Dann einfach umsetzen. Und was, wenn Clean Code und Software Design
sie immer noch unhandlich groß ist? Dann gilt es, eine Ebene
28.-30.10.2024
tiefer zu steigen.
Architekturen für
Command Query Separation (CQS)
Wie können Entry Points formal (!) weiter zerlegt werden? .NET-Anwendungen 11.-13.11.2024
Was wäre für Sie als Entwickler ein relevanter struktureller
(!) Schnitt? Ich denke, das Prinzip der Command Query Se-
paration von Martin Fowler [2] ist hier hilfreich. Mit ihm kann
In Vorbereitung
Funktionalität zumindest auf einen Aspekt der Zustandsver-
änderung fokussiert werden:
Command: Eine Funktion verändert Zustand und liefert C#- Grundlagen 3 Tage
kein Resultat zurück. Oder wenn ein Resultat geliefert wird,
dann sind es Metadaten zur Aktivität, zum Beispiel die Zahl Azure DevOps – CI/CD mit
der gelöschten Datensätze oder die ID eines neu angeleg-
Azure Pipelines und Git 3 Tage
ten Datensatzes. Bei REST entspricht dem ein POST-Re-
quest. Ein Command kann inhaltlich fehlschlagen, weil zu
Erste Schritte mit Docker
verändernde Daten nicht im erwarteten Zustand sind.
Query: Eine Funktion verändert keinen Zustand und liefert für .NET-Entwickler 2 Tage
ein Resultat zurück, das auch auf Zustand basieren kann.
Dem entspricht bei REST ein GET-Request. Queries können
inhaltlich nicht fehlschlagen.
Die Unterscheidung von Veränderungen und Abfragen hat
mehrere Vorteile: ▶ developer-academy.de
Ihre Ansprechpartnerin: Susanne Herl
www.dotnetpro.de 6.2024 +49 731 88005-8835 • susanne.herl@ebnermedia.de
003344--004433__SSlliicciinngg__eeaa__ffss__eeaa__ffss..iinndddd 4411 2299..0044..2244 1100::0011
DDeevvAAccaaddeemmyy2244__AAZZ__OOffffeennee KKuurrssee__110022xx229977__VV22..iinndddd 7755 2244..0044..2244 1144::2200


| HANDS-ON-WORKSHOPS
UND WEITERBILDUNG FÜR
SOFTWARE-ENTWICKLER UND
-ARCHITEKTEN OFFENE
TRAININGS!
Unsere öffentliche
Hands-on Workshops
sind wieder da.
In 2024 können Sie folgende
Workshops buchen
C# für Fortgeschrittene
27.-29.05.2024
UX und UI-Design
für Entwickler 11.-12.06.2024
Clean Code und Software Design
28.-30.10.2024
Architekturen für
.NET-Anwendungen 11.-13.11.2024
In Vorbereitung
C#- Grundlagen 3 Tage
Azure DevOps – CI/CD mit
Azure Pipelines und Git 3 Tage
Erste Schritte mit Docker
für .NET-Entwickler 2 Tage |
| --- |
| developer-academy.de
Ihre Ansprechpartnerin: Susanne Herl
+49 731 88005-8835 • susanne.herl@ebnermedia.de |



| HANDS-ON-WORKSHOPS
UND WEITERBILDUNG FÜR
SOFTWARE-ENTWICKLER UND
-ARCHITEKTEN OFFENE |  |
| --- | --- |
| UND WEITERBILDUNG FÜR
SOFTWARE-ENTWICKLER UND
-ARCHITEKTEN OFFENE |  |
|  |  |
| TRAININGS!
Unsere öffentliche
Hands-on Workshops
sind wieder da.
In 2024 können Sie folgende
Workshops buchen
C# für Fortgeschrittene
27.-29.05.2024
UX und UI-Design
für Entwickler 11.-12.06.2024
Clean Code und Software Design
28.-30.10.2024
Architekturen für
.NET-Anwendungen 11.-13.11.2024
In Vorbereitung
C#- Grundlagen 3 Tage
Azure DevOps – CI/CD mit
Azure Pipelines und Git 3 Tage
Erste Schritte mit Docker
für .NET-Entwickler 2 Tage |  |



---


<!-- Page 9 of 10 -->


PLANUNG Slicing
Getrennte Testbarkeit dieser unter-
schiedlichen Weisen des Umgangs
mit Daten.
Technologische Trennung dieser
Modi, zum Beispiel kann ein Com-
mand Locks erfordern, Queries aber
nicht.
Wiederverwendbarkeit in unter-
schiedlichen Zusammenhängen we-
gen feingranularerer Funktionen.
Durch diese Brille betrachtet sind En-
try Points oft nicht eindeutig. Sie bie- Nach Refaktori-
ten Potenzial für eine Verfeinerung, sierung entspre-
das heißt Verkleinerung des Scopes chen alle Entry
durch Konzentration auf Command Points dem CQS
versus Query. (Bild 13)
Wie steht es in dieser Hinsicht mit
den bisherigen Entry Points der Auf-
gabenverwaltung? Bild 11 zeigt, dass
das Urteil nur in drei von fünf Fällen
eindeutig ist:
list_delete() ist ein Command, da
Zustand verändert wird – eine Liste
wird gelöscht –, aber keine Daten zurückgeliefert werden. mentation, die ich schon (vorschnell) vorgenommen hatte, um
Die Annahme ist, dass die per id identifizierte Liste existiert. die Szenariotests oben vorzustellen, zeigt Potenzial für die
lists_all() und program_start() sind beide Queries. Sie fra- Trennung: Es gibt nicht nur einen Widerspruch zu CQS, son-
gen lediglich die Liste der Listen ab und liefern Einträge dern auch zum Prinzip Don’t Repeat Yourself (DRY) (Bild 12).
zurück. In zwei Funktionen wird eine Liste über ihre ID herausge-
sucht.
Sowohl list_create() wie auch list_rename() hingegen sind Wenn diese Logik in eine eigene Funktion wandert, kann
keine reinen Kommandos, auch wenn das durch die Benen- dem CQS Genüge getan werden (Bild 13):
nung suggeriert wird. Der Widerspruch zum CQS besteht in list_rename() und list_delete() können sich besser auf ihre
ihren Responses, die die veränderten Daten zurückliefern. eigentliche Aufgabe konzentrieren.
Das ist naheliegend, jedoch streng genommen nicht erlaubt. Aufrufer von list_create() und list_rename() können sich die
Wie reagieren Sie darauf? bisher zurückgelieferte Liste über einen weiteren Entry
Das Wichtigste ist, diesen Widerspruch überhaupt entdeckt Point list_get() beschaffen.
zu haben. Jetzt können Sie eine bewusste Entscheidung tref-
fen, ob sie diese beiden Aspekte gekoppelt lassen oder sie Alle Entry Points entsprechen nun dem CQS:
aufdröseln. In manchen Fällen kann es bleiben, wie es ist, in list_delete() hat sich am wenigsten verändert. Die Funktion
anderen lohnt sich eine Trennung. sucht nur einfach nicht mehr selbst die zu löschende Liste
Insbesondere, wenn die zurückzuliefernden Daten schon heraus.
bei der Kommandoausführung ganz natürlich „anfallen“ und list_rename() delegiert die Beschaffung der umzubenen-
nicht zu umfangreich sind, wäre es dumm, sie nicht gleich zu- nenden Liste nun auch – liefert sie allerdings nicht mehr zu-
rückzuliefern. Das erspart dem Aufrufer einen zweiten Zu- rück. Die Funktion ist damit zu einem klaren Command ge-
griff, um sie zu beschaffen. Aber, wie gesagt, es kommt auf worden.
den Einzelfall an. list_create() retourniert jetzt nicht mehr die neue Liste, son-
Hier ist jedenfalls Potenzial für feinere Schnitte. Wie könn- dern nur deren ID. Auch hier liegt jetzt ein reinrassiges
ten diese aussehen? Ein Blick hinter die Kulissen der Imple- Command vor.
list_get() ist der neue Query Entry Point
zur Beschaffung einer einzelnen Liste.
Er kapselt die interne Methode, die
noch sowohl Liste als auch Index lie-
fert. Auf diese Weise konnten die Be-
dürfnisse beim Umbenennen und Lö-
schen mit einer Funktion befriedigt
Ein Convenience Entry Point als Integration anderer Entry Points (Bild 14) werden.
42 6.2024 www.dotnetpro.de
003344--004433__SSlliicciinngg__eeaa__ffss__eeaa__ffss..iinndddd 4422 2299..0044..2244 1100::0011


---


<!-- Page 10 of 10 -->


PLANUNG Slicing
Im Szenariotest ist diese Be-
schaffung natürlich hinzu-
zufügen (Zeile 12 im rech-
ten Ausschnitt in Bild 13).
Aber wird dadurch
nicht auch etwas mehr
Klarheit hergestellt?
Solange nicht deut-
lich spürbare Performan-
ce-Verschlechterungen da-
gegen sprechen, ziehe ich ein
Slicing nach CQS unterhalb der
Entry Points vor. Ich möchte jeden Ent-
ry Point so dünn geschnitten haben, wie es
möglich ist.
Allerdings … ich mag auch die Bequemlichkeit,
die ein hybrider Entry Point wie zum Beispiel das ur-
sprüngliche list_rename() geboten hat. Deshalb finde
ich es okay, wenn Sie ganz bewusst nach einer Verfeine-
rung entlang des CQS die entstandenen Entry Points zu ei-
nem Convenience Entry Point zusammenfassen (Bild 14). In CQS-konforme Funktionen als Kern
dem kommen Command und Query (auch mehrere) zusam- der Benutzerinteraktionen sind das
men, um eine abstraktere Funktion zu bilden. Die muss auch Ziel immer feinerer Schnitte durch die
eigentlich nicht mehr separat getestet werden, falls die da rin Anforderungen entlang der Slicing-
vereinten Entry Points separat getestet wurden; dass Ihnen Hierarchie (Bild 15)
bei der Integration von zwei oder drei Entry Points ein Feh-
ler unterläuft, ist kaum zu erwarten.
wünschen. Aber nicht nur, dass Software etwas Bestimmtes
Zwischenstand
tun soll, sondern wie das konkret angestoßen werden soll, ist
Slicing leitet in kleinen Schritten durch eine für Sie als Ent- entscheidend. Die Granularität der Interaktionen ist bestim-
wickler relevante Hierarchie von Inkrementen. Alles beginnt mend für die Form der Entry-Point-Funktionen.
immer beim kompletten Softwaresystem – doch das Ziel ist Bei der Anforderungsanalyse werden Sie deshalb den
am Ende die einzelne CQS-fokussierte, testbare Funktion größten Teil der Zeit auf den Slicing-Ebenen ab Interaction
(Bild 15), die unabhängig von Frontend-Technologien ist. Hin- verbringen. Insbesondere das Aushandeln der Testfälle be-
ter ihr steht die Erzeugung von Verhalten mit einem beliebig nötigt viel Zeit. POs legen sich ungern fest.
tiefen Baum weiterer Funktionen, die die Logik enthalten, Um es Ihnen und POs in der Hinsicht einfacher zu machen,
um gegebenenfalls unter Rückgriff auf Ressourcen die nöti- können Sie allerdings noch eine Ebene tiefer steigen als CQS.
gen Datentransformationen durchzuführen, die der User Features sind Inkremente innerhalb derer für Entry Points; die
wünscht. Funktionen sind definiert, dennoch kann der Scope feiner ge-
Der Sprung vom Softwaresystem zu einer tieferen Ebene schnitten werden. Das soll im nächsten Artikel geschehen. ◾
ist jederzeit möglich, wenn Sie fühlen, dass Sie auf der Ziel-
ebene Klarheit haben. Slicing ist ein Tool, um Ansatzpunkte [1] Ralf Westphal, Den Stier bei den Hörnern packen,
für Ihren Softwareentwurf zu identifizieren, damit Sie mög- dotnetpro 5/2024, Seite 26 ff.,
lichst geradlinig zu lauffähigem, korrektem Code kommen. www.dotnetpro.de/A2405Slicing
Die Gestaltung der Benutzerschnittstelle ist dabei lediglich [2] Martin Fowler, Command Query Separation,
ein Hilfsmittel, falls die Entry Points für Sie noch nicht auf der www.dotnetpro.de/SL2406Slicing1
Hand liegen. Deshalb hat sie in diesem Artikel noch keine
Rolle gespielt.
Wenn Sie mit einer User Story oder einem Use Case kon- Ralf Westphal
frontiert sind, fragen Sie sich stets: „Weiß ich schon genug, ist Trainer, Berater und Mitgründer der Clean
um einen Entry Point zu formulieren?“ Wenn nein, bohren Sie Code Developer Initiative (https://clean-code-
hinein in die User Story. Brechen Sie den Use Case herunter. developer.de). Seine Schwerpunkte sind dauer-
„Grillen“ Sie den PO. Lassen Sie ihn nicht ziehen, bevor Ih- haft hohe Produktivität für die Softwareent-
nen nicht die konkreten Interaktionen sonnenklar sind, in de- wicklung und zukunftsfähige Teamorganisation.
nen User das Softwaresystem triggern wollen. https://ralfw.de
Interaktionen sind das, was Anwender wollen. Sie wollen
dnpCode A2406Slicing
das Softwaresystem so kontrollieren, dass es tut, was sie sich
www.dotnetpro.de 6.2024 43
003344--004433__SSlliicciinngg__eeaa__ffss__eeaa__ffss..iinndddd 4433 2299..0044..2244 1100::0011