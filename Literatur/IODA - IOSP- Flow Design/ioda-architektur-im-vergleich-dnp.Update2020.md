<!-- Page 1 of 84 -->



---


<!-- Page 2 of 84 -->


Die IODA Architektur im
Vergleich
Ralf Westphal und dotnetpro
Dieses Buch wird verkauft unter
http://leanpub.com/ioda-architektur-im-vergleich-dnp
Diese Version wurde veröffentlicht am 2020-12-27
Dies ist ein Leanpub-Buch. Leanpub bietet Autoren und Verlagen, mit
Hilfe von Lean-Publishing, neue Möglichkeiten des Publizierens. Lean
Publishing bedeutet die wiederholte Veröffentlichung neuer
Beta-Versionen eines eBooks unter der Zuhilfenahme schlanker
Werkzeuge. Das Feedback der Erstleser hilft dem Autor bei der
Finalisierung und der anschließenden Vermarktung des Buches. Lean
Publishing unterstützt den Autor darin ein Buch zu schreiben, das auch
gelesen wird.
© 2018-2020 dotnetpro und Ralf Westphal


---


<!-- Page 3 of 84 -->


Ebenfalls von Ralf Westphal
Test-first Codierung
Softwareentwurf mit Flow-Design
Software Anforderungsanalyse mit Slicing


---


<!-- Page 4 of 84 -->


Inhaltsverzeichnis
Vorwort . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1 - Eine Kritik bisheriger Architekturmodelle . . . . . . . . . . . 6
Am Anfang war der Monolith . . . . . . . . . . . . . . . . . . . 7
Den Monolithen in Schichten spalten . . . . . . . . . . . . . . . 12
Schichten entkoppeln . . . . . . . . . . . . . . . . . . . . . . . . 16
Schichten in Schale werfen . . . . . . . . . . . . . . . . . . . . . 20
Reflexion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
2 - Das IODA Architekturmodell . . . . . . . . . . . . . . . . . . 34
Funktionale Abhängigkeiten als Wurzelproblem . . . . . . . . . 34
Auflösung funktionaler Abhängigkeiten . . . . . . . . . . . . . 39
Operationen verbinden . . . . . . . . . . . . . . . . . . . . . . . 43
Verbindung zur Außenwelt . . . . . . . . . . . . . . . . . . . . 46
Ein neues Architekturmuster . . . . . . . . . . . . . . . . . . . 48
Echt abstrakt . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
3 - IODA am Beispiel . . . . . . . . . . . . . . . . . . . . . . . . . 57
Struktur fraktal . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
Zusammenfassung . . . . . . . . . . . . . . . . . . . . . . . . . 67
Update 2020 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
Logik frisch definiert . . . . . . . . . . . . . . . . . . . . . . . . 70
Integrationen konsequent benannt . . . . . . . . . . . . . . . . 74
Interactor . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
Processor . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
Interactor-Varianten . . . . . . . . . . . . . . . . . . . . . . 77
Reflexion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78


---


<!-- Page 5 of 84 -->


Vorwort
Seit Ende der 1990er befasse ich mich mit Softwarearchitektur explizit.
VorherhatteichSoftwareeinfach“irgendwiezusammengeschraubt”,glau-
be ich. Das hatte genügend gut geklappt, so dass ich damit Geld verdienen
konnte;dieKundenderFirma,dieichmitmeinemGeschäftspartnerhatte,
waren zufrieden mit unserer Software.
Doch dann irgendwann war das nicht mehr genug. In die Microsoft-
Bubble, in der ich mich damals befand, drang etwas Neues ein. Entwurfs-
muster für die Objektorientierung waren angesagt und dann kam sogar
Microsoft als Technologiehersteller mit Empfehlungen für die Strukturie-
rung von Software um die Ecke. Ich erinnere mich ans Schichtenmodell,
dann an N-Tier Architecture, dann an Emissaries and Executants (ich
glaube, so hieß das eine Zeit lang)… Auch wenn die Details verschwim-
men, eines habe ich noch im Gefühl: Softwarearchitektur war wichtig
geworden.
Wie es dann so kam, hat mich das Thema nicht wieder verlassen. Ich
war vom Technologieanwender zu einem “Planer” von Technologiean-
wendung geworden.
Allerdings konnte ich schon bald nicht mehr einfach akzeptieren, was
an Architekturmustern empfohlen wurde. Immer fehlte irgendetwas oder
kam mir nicht plausibel vor. Anfang 2005 habe ich dieses Gefühl dann
so ernst genommen, dass ich anfing, an einem eigenen Architekturmodell
zu tüfteln. Die Softwarezelle ward geboren. Hier zwei Bilder aus dieser
Zeit, mit denen ich das Konzept in meinem damaligen Blog erklärt und
entwickelt habe:¹
¹Interessanterweise war ich nicht der einzige, dem da etwas fehlte. Später habe ich
erfahren,dassAlistairCockburnzurselbenZeitanseinerHexgonalArchitecturegearbeitet
hat.EslagdaalsoetwasinderLuft…


---


<!-- Page 6 of 84 -->


Vorwort 2
EinefrüheFormderSoftwarezelleausdemApril2005
SoftwarezellenimVerbundfüreineverteilteArchitektur
Damals war mir sehr wichtig, die Geschäftslogik in den Mittelpunkt zu
rücken. Sie schien mir in anderen Architekturmustern zu wenig betont


---


<!-- Page 7 of 84 -->


Vorwort 3
und gerade für verteilte Anwendungen stiefmütterlich behandelt.²
Außerdem fand ich die ganze Herangehensweise an die Strukturierung
von Software zu technisch, zu mechanisch. Wenn Software entwickelt
wird, sich also entwickelt, über lange Zeit entwickelt, geradezu eine Evo-
lution durchläuft… dann, so war mein Gedanke, sollte sie durch ein orga-
nischeres Bild beschrieben werden. Deshalb der BegriffSoftwarezelle. Mit
ihr, aus ihr wollte ich Software wachsen sehen.
Vielleicht entstand damals mein Interesse für nachhaltige Softwareent-
wicklung, das später zur Mitgründung der Clean Code Developer Initia-
tive geführt hat. Mein Empfinden war einfach, dass viele Entwickler sich
redlich bemühten, das eine oder andere Architekturmuster anzuwenden,
um nicht zu schnell in die “Unwartbarkeit” zu laufen. Doch dieses Be-
mühen war zu selten von Erfolg gekrönt. Die Anwendung der Muster
funktionierte nicht wie gewünscht, was immer wieder zu Frust geführt
hat und der wiederum zu einer Hoffnung, dass Technologie das Dilemma
doch bitte lösen möge.
Doch Technologie nimmt uns in der Softwareentwicklung das Nachden-
ken nicht ab - außer vielleicht in Sonderfällen. Wir müssen weiterhin
verstehen und entscheiden. Und für das Entscheiden brauchen wir Heu-
ristiken, Prinzipien, Konzepte.
Seitdem hat mich das Thema Softwarearchitektur also nicht losgelassen.
Bei aller trivialen Korrektheit des Beraterspruchs “Es kommt darauf an…”
glaube ich, dass es einen Rahmen gibt, in dem sich Softwarearchitektur
bewegen sollte. Die konkrete Architektur eines Softwaresystems orien-
tiert sich nur daran, sie prägt ihn individuell im Hinblick auf die nicht-
funktionalen Anforderungen aus. Dabei kommt es natürlich darauf an,
wie man das tut.
Docheskommtebennichtdaraufan,dassmanestut.Softwarearchitektur
ausgehend von Prinzipien und Mustern nicht explizit zu betreiben, halte
ich für keine Option.
Aber welche Prinzipien und Muster? Darüber habe ich lange nachgedacht.
Die Beschäftigung mit dem Clean Code Development hat mir dabei ge-
²InAbbildung31findenSiedieSoftwarezelleauchheutenochwieder,selbstwennich
sie in der Artikelreihe nicht so genannt habe. Ich wollte das Neue der IODA Architektur
nicht noch mit einem solchen Begriff überladen, allemal, da ich auf die Konsequenzen für
dieVerteilungnichteingegangenbin.


---


<!-- Page 8 of 84 -->


Vorwort 4
holfen. Das eine hat das andere befruchtet. Deshalb spreche ich heute
auchwenigervonCleanCode;meineTrainingslaufenuntereineranderen
Überschrift, um den Bogen weit genug spannen zu können. Denn worum
geht es? Um langfristig hohe Produktivität.
SoftwarearchitekturisteinAspektdesWunsches,Softwareübermöglichst
lange Zeit möglichst anpassungsfähig (wandelbar) zu halten. Andere As-
pekte gehörenauch dazu: konsequente test-first Codierung, inkrementelle
Anforderungsanalyse und Umsetzung, Zurückhaltung bei der Verände-
rung von Produktionscode, Verzicht auf die Aufwandsschätzung zuguns-
ten von Vorhersagen usw.
Clean Code hat Appeal für Entwickler, nicht für Manager. Es ist damit ein
zu techschnischer Begriff für das, worum es geht.Programming with Ease
hingegen spannt für mich einen Bogen, der einerseits weit genug ist und
andererseits spezifisch genug. Ich möchte die Programmierung rundum
erleichtern. Dazu gehört auch, die grobe Strukturierung von Code. Denn
wer keine grundlegende Vorstellung von der Anatomie von Software
hat, von ihren wiederkehrenden Funktionsbausteinkategorien und deren
Zusammenhänge, der tut sich von Anfang an schwer mit jedem Software-
projekt. Und dabei geht es noch nicht einmal um die Erfüllung spezieller
nicht-funktionalerAnforderungen.Nein,esreichtschlichtTestbarkeitund
Wandelbarkeit auch bei einem Monolithen, d.h. nicht verteilter Software,
hoch halten zu wollen. Das ist Problem genug, um stets nach besseren
Ansätzen zu suchen.
Das habe ich getan und tue es noch mit der IODA Architektur. Mit ihr
stelleichdas,wasmitSoftwarezellenbegonnenhat,aufeinPrinzipienfun-
dament. Die Hexagonal Architecture und die Clean Architecture basieren
auf den Prinzipien DIP/IoC. Die IODA Architektur basiert auf IOSP und
PoMO als Ergebnisse einer Analyse der ursprünglichen Objektorientie-
rung, wie sie Alan Kay 1968 gedacht hatte.³
Ich habe nichts gegen DIP/IoC. Im Gegenteil! Aber für mich ist da eben
nichtSchluss.FürtestbarereundwandelbarereSoftwarebrauchenwirein
Architekturmuster, das darüber hinaus geht.
Mir scheint, dass ich 2015 das erste Mal den Begriff IODA Architektur in
³FüreineausführlicheHerleitungsiehemeineArtikelserieOOPasifyoumeantitbzw.
denBandSoftwareentwurfmitFlow-DesignausmeinerProgrammingwithEase Reihe.


---


<!-- Page 9 of 84 -->


Vorwort 5
einem Blogartikel⁴ benutzt hatte. 2018 habe ich den aktuellen Stand dazu
dann in drei Artikeln in der dotnetpro zusammengefasst. Diese Artikel
sind in diesem kleinen Buch zusammengefasst, um die Lektüre einfacher
undunabhängigvoneinemAbonnementderdotnetprozumachen.Vielen
Dank an Chefrefakteur Tilman Börner und die Ebner Media Group, eine
solche herausgelöste Veröffentlichung zu ermöglichen. Natürlich habe
ich diese Gelegenheit genutzt, die Artikel durchzusehen, hier und da zu
ergänzen und am Ende noch ein Update hinzuzufügen, das einzuarbeiten
schwierig gewesen wäre. Ich hoffe, auf diese Weise diese Perspektive auf
SoftwarearchitekturmustereinemgrößerenInteressentenkreiszugänglich
zu machen.
Viel Spaß bei der Lektüre!
-Ralf Westphal, Bansko/Bulgarien im Dezember 2020
⁴http://geekswithblogs.net/theArchitectsNapkin/archive/2015/04/29/the-ioda-
architecture.aspx


---


<!-- Page 10 of 84 -->


1 - Eine Kritik bisheriger
Architekturmodelle
Ich kann sie nicht mehr hören die Anpreisungen des Architekturmusters
„Schichtenmodell“. In der dotnetpro wie anderswo spukt es immer wieder
alsklassischeunddeshalbguteOrganisationvonCodeherum.Mirscheint
dasinzwischeneinFallvonCargoKult⁵:Irgendwerhatirgendwannseinen
CodesostrukturiertunddamiteinenVorteilerlangt–undnunfolgendem
Generationen von Entwicklern blind.
Was aber, wenn sich die Welt weitergedreht hat? Was, wenn man da
etwas mechanisch tut, ohne wirklich konsequent über die ursprünglichen
Beweggründe nachzudenken? Das Ergebnis ist dann immer gleich: Es
entsteht Unwohlsein, die Dinge werden schwierig – doch man weiß nicht
so recht, woher das kommt. Man macht doch alles richtig, oder? Eher
wohl nicht; vielleicht muss man sich einfach noch mehr bemühen. Also
die Anstrengungen verdoppeln, das Muster einzuhalten. Und so entsteht
dann noch mehr Unwohlsein.
„Been there, done that, got the t-shirt“, kann ich dazu sagen. Einst war ich
auch Anhänger des Schichtenmodells und anderer seiner mustergültigen
Geschwister. Doch irgendwann habe ich für mich realisiert: der Schmerz
ist größer als der Nutzen. Ich muss die Muster nicht besser anwenden,
sondern einen anderen Weg suchen, meine Software zu strukturieren.
Worauf ist dann gestoßen bin, davon möchte ich Ihnen im Folgenden
berichten. Es ist eine Geschichte der Erleichterung. Softwareentwicklung
macht mir jetzt wieder Spaß. Ich kann mich viel mehr auf die Lösung
der Probleme konzentrieren, weil die Struktur mich nicht mehr in ein
hinderliches Korsett zwängt.
Aber der Reihe nach. Lassen Sie mich noch vor dem “Musterspuk” begin-
nen.
⁵https://en.wikipedia.org/wiki/Cargo_cult


---


<!-- Page 11 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 7
Am Anfang war der Monolith
Hier ist eine Challenge:
SchreibenSieein Programm,das dieGesamtzahl derWortesowie die
Zahl der verschiedenen Worte in einem Text unter Berücksichtigung
einerStoppwortlistebestimmt.DerTextwirdentwedervomBenutzer
eingegeben oder aus einer Datei gelesen, die der Benutzer bei Pro-
grammstart angibt.
Das ist einesimple Aufgabe,denkeich. Dennochist da allesdrin, was eine
Software ausmacht: ein bisschen Benutzerschnittstelle, ein bisschen Fach-
logik, ein bisschen Datenzugriff. Genug, um darauf das Schichtenmodell
und andere Strukturierungsideen anzuwenden.
In diesem Beispiel geht es nicht darum, ein Technologiefeuerwerk abzu-
brennen. Eine Konsolenanwendung reicht völlig aus. Deren Anwendung
könnte so aussehen:
1 $ wordcount.exe
2 Text eingeben: Es blaut die Nacht, die Sternlein blinken
3 6 Worte, davon 5 verschieden
4 $ wordcount.exe gedichtanfang.txt
5 6 Worte, davon 5 verschieden
6 $
Der eingegebene Text hat zwar 7 Worte, doch das Wort „es“ steht in der
Datei mit den Stoppworten und wird deshalb nicht gezählt. Außerdem
steht „die“ im Text zweimal, daher unterscheidet sich die Zahl der Worte
von der der verschiedenen.
Sie können ja mal als Fingerübung selbst für die Challenge ein Programm
schreiben. Beobachten Sie sich dabei: Wie gehen Sie vor? Wie strukturie-
ren Sie den Code und warum?
Wenn Sie mitmachen und später vergleichen möchten, dann lesen Sie
erstmal nicht weiter. Spoileralarm! Denn ich möchte Ihnen verschiedene
„hoch entwickelte“ Lösungen vorstellen, um daran zu zeigen, warum das
Schichtenmodell und Verwandte keine Option mehr für mich sind.


---


<!-- Page 12 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 8
Aber zuerst eine Lösungsvariante, die gar nicht mehr geht. Oder ist sie
eine, die womöglich noch häufig anzutreffen ist? Entscheiden Sie, ob
Ihnen solcher Code wie in Abbildung 1 immer noch über den Weg läuft.
Den Code bezeichne ich als monolithisch: Nicht nur ist er nicht verteilt,
er besteht auch nur aus Logik. Rekombinierbare Strukturelemente wie
Funktionen oder Klassen sind vernachlässigbar. Der Code ist also quasi
strukturlos aus architektonischer Sicht.
Die Anweisungen in der einzigen Funktion Main(), d.h. die Logik, tut
zwar, was sie tun soll: das Programm ist funktional; doch verständlich
oder testbar ist die Logik nicht.


---


<!-- Page 13 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 9
Abbildung1:EinefunktionaleLösungmitunwesentlicherStruktur
Sicher,dassindkaum50Zeilen.Diezuverstehen,solltedochkeinProblem
sein. Warum sich hier mehr Aufwand mit mehr Struktur machen?
Erstens ist das hier ein Beispiel mit überschaubarer Funktionalität (und
auchnocheigentlichgeradlinigerLogik),umebenStrukturierungsansätze
zu demonstrieren. Selbst wenn das später ein bisschen künstlich und
overengineertaussehensollte,wirdeshoffentlichdiewesentlichenPunkte
illustrieren helfen, um die es mir geht.
Zweitensglaubeich,dasswirvielsensiblerseinsollten,wasdieStrukturie-
rung angeht. Wir sollten uns nicht überschätzen in der Fähigkeit, Code zu
verstehen. Die Zeit für einen Bugfix oder zum Einbau einer Erweiterung


---


<!-- Page 14 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 10
ist immer knapp. Jede Minute, die wir beim Verstehen von Code sparen
können, bevor wir ihn verändern, ist wichtig. Dafür aber müssen wir
vorher, schon beim Schreiben etwas tun. Der Code-Autor muss an den
späteren Code-Leser denken.
“Programs must be written for people to read, and only inci-
dentally for machines to execute.”, Harold Abelson & Gerald
Jay Sussman
Was macht den Code in Abbildung 1 aber so schwer zu verstehen? Es ist
die kunterbunte Vermischung von Verantwortlichkeiten.
In Abbildung 2 habe ich die wesentlichen Verantwortlichkeiten farblich
hervorgehoben.Siesehen,dasisteinFlickenteppich.Verantwortlichkeiten
sind verstreut über die Logik. Verantwortlichkeiten werden mit Kontroll-
strukturen „geöffnet“, um dann andere dazwischen zu schieben und sie
erst später zu „schließen“.


---


<!-- Page 15 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 11
Abbildung2:UnstrukturierterCodeisteinFlickenteppichausVerantwortlichkeiten
So kann kein Fluss des Verständnisses entstehen. Der Code „erzählt keine
Story“, in der etwas entlang einer Kausalkette passiert. Es fehlen Bedeu-
tungseinheiten, die Sie auf einen Blick erfassen können. Alles müssen Sie
sich durch Simulation der Ausführung der Anweisungen erst erschließen.
Das ist gruselig aufwändig und fehlerträchtig. Und ob der Code wirklich
korrektist,lässtsichnichtermitteln,ohneihnmanuellauszuführen.Keine
der Verantwortlichkeiten kann gezielt mit automatisierten Tests überprüft
werden. So lässt sich nicht zügig feststellen, ob der Code schon reif zur
Auslieferung ist oder nach einer Änderung immer noch korrekt, also
regressionsfrei.


---


<!-- Page 16 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 12
So geht’s nicht. Da sind wir uns einig, hoffe ich.
Aber das war die Situation zumindest früher auch nach Einführung der
Strukturierten Programmierung. Vor diesem Hintergrund sind die ersten
Architekturmuster entstanden. Zunächst Model-View-Controller (MVC)⁶,
dann das Schichtenmodell. Was für ein Sonnenaufgang über dem Mono-
lithen.
Den Monolithen in Schichten spalten
MVC, Schichtenmodell, Hexagonale Architektur⁷ und auch die Clean Ar-
chitecture⁸ verfolgen alle denselben Ansatz:
1. Sie definieren einen Kanon von Verantwortlichkeiten und verord-
nen die Spaltung der Logik nach diesen Verantwortlichkeiten in
Module.
2. Sie geben genau vor, wie die Module in Beziehung stehen, d.h.
einander kennen und nutzen dürfen.
Die Beliebtheit des Schichtenmodells scheint mir hierbei in einer Kom-
bination aus leicht zu verstehenden Verantwortlichkeiten in angenehmer
Granularität und sehr klaren Beziehungen zu bestehen (Abbildung 3).
⁶https://de.wikipedia.org/wiki/Model_View_Controller
⁷https://en.wikipedia.org/wiki/Hexagonal_architecture_%28software%29
⁸https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html


---


<!-- Page 17 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 13
Abbildung 3: Das Schichtenmodell definiert verständliche Verantwortlichkeiten in klaren
Beziehungen
Wenn ich dieses Muster auf den bisherigen Code zur Lösung der obigen
Challengeanwende,dannistdamittatsächlichetwasgewonnen:Verständ-
lichkeit. Die Logik liegt nicht mehr auf einem Haufen, sondern ist verteilt
auf Klassen als Module, so dass sich schon beim Betrachten des Projektes
eine gewisse Übersicht einstellt (Abbildung 4).
Abbildung4:SchichtensteigerndieÜbersichtlichkeit
Wer mit dem Schichtenmodell vertraut ist, sieht hier erstens Verantwort-
lichkeiten, unter denen er sich etwas vorstellen kann. Zweitens sind dem
Betrachter sofort die grundsätzlichen Beziehungen klar. Das ist ja auch
der Sinn der Einhaltung eines solchen Musters. Sie müssen kein Rad neu
erfinden,sondernkönnensichdaraufverlassen,dassSienichtsgrobfalsch
machen, wenn Sie nach dem Schema strukturieren. Mit einem Architek-


---


<!-- Page 18 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 14
turmuster setzen Sie eine Brille auf, durch die Sie die Logik analysieren
können; was Sie dabei identifizieren, stecken Sie in die kanonischen Mo-
dule. Und Sie können auch noch annehmen, dass ein anderer Entwickler,
der auch das Muster kennt, ihre Struktur versteht; er findet sich darin also
von vornherein leicht(er) zurecht.
Die nächste Abbildung zeigt konkret die Schichtung der Klassen der Um-
setzungausAbbildung4.Ordentlich,oder?EinesoorganisierteCodebasis
macht Freude. Alles hat seinen Platz. Da wissen Sie genau, wo was pas-
siert.
Abbildung5:KonkreteSchichtungderAnwendungslogik
Ja, damit ist etwas gewonnen. Es ist besser als vorher, aber noch nicht
wirklich gut. Denn schauen Sie sich einmal den Code der Businesslogik
an:


---


<!-- Page 19 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 15
Abbildung6:SchlechttestbareLogiktrotzSchichtung
Die groben Verantwortlichkeiten sind grundsätzlich hübsch getrennt, die
Abhängigkeitensindsauberausgerichtet–dochguttestbaristdeshalbdie
eigentlicheBusinesslogikimmernochnicht.DenndieBusinesslogikhängt
immer noch von der Datenzugriffslogik ab. Es besteht eine funktionale
Abhängigkeit: Logik in einer Methode ruft eine andere Methode auf, um
zwischendurch deren Logik auszuführen.
Das hört sich normal an und findet sich bestimmt in Ihrem Code auch
allerorten. Doch das macht es nicht besser. Solche funktional abhängige
Logik ist schlicht nicht für sich allein testbar.
Natürlich ist die Logik in Abbildung 6 auch in anderer Hinsicht noch
suboptimal. Doch das ist sekundär für den Punkt, um den es mir hier
im Augenblick geht. Ich habe nur das minimal Nötige getan, um den
monolithischen Code nach dem Schichtenmodell zu strukturieren. Das
fundamentaleProblemdesSchichtenmodellsgehtnichtweg,wennichdie
Wortzählungslogik noch weiter refaktorisiere. Der Klumpen in Count_-
words() dient also der Unterstreichung des grundsätzlich zu lösenden
Problems der funktionalen Abhängigkeiten.


---


<!-- Page 20 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 16
Wer die Businesslogik testen will, der kann das im Moment trotz oder
wegen Schichtenmodell nur tun, indem er ebenfalls die Logik der Daten-
zugriffsschicht ausführt. Das macht einen Businesslogik-Test langsamer
und/oder umständlicher, weil eine Datei als Ressource bereitgestellt wer-
den muss.
NichtwirklichdramatischindiesemtrivialenBeispiel,dochwennSiesich
das Szenario umfangreicher denken… dann kommt schon etwas zusam-
men an Overhead.
Wenn Abbildung 1 den Bewusstseinsstand in Sachen Anwendungsarchi-
tektur bis Mitte der 1990er in vielen Projekten widerspiegelt, dann steht
Abbildung 6 für den Ende der 1990er.
Schichten entkoppeln
In einer Co-Evolution mit bewussterer Anwendungsstrukturierung be-
fand sich ab Ende der 1990er das Thema Testen. Die ersten Unit Testing
Frameworks kamen auf.
Wo klare Verantwortlichkeiten in Modulen freigestellt waren, konnten
überhaupt erst automatisierte Tests feingranular ansetzen. Aber um in
einer sauberen Hierarchie automatisierte Tests punkgenau nur gewisse
Logik testen lassen zu können, brauchte es Entkopplung der Verantwort-
lichkeiten.
Auftritt DIP: Mit dem Dependency Inversion Principle⁹ wurde es möglich,
Tests auf eine Schicht zu fokussieren.
Der Trick besteht darin, Compilezeitabhängigkeiten von Laufzeitabhän-
gigkeiten zu trennen. Zur Compilezeit besteht nach DIP keine direkte
funktionale Abhängigkeit von Logik einer Schicht zu Logik einer anderen.
Eine obere Schicht hängt nicht von einer konkreten unteren ab, sondern
lediglich von einer Abstraktion:
⁹https://de.wikipedia.org/wiki/Dependency-Inversion-Prinzip


---


<!-- Page 21 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 17
Abbildung7:MitdemDIPwerdenSchichtenentkoppelt
Abstraktionen sind gewöhnlich Interfaces oder abstrakte Klassen. Die
könnenvonderniedrigenSchichtimplementiertwerden–abermankann
aucheineAttrappefüreineniedrigeSchichtsoaussehenlassen.Docheins
nach dem anderen.
Zuerst die Anwendung mit verbesserter Schichtenarchitektur in im Über-
blick. Hinzugekommen sind die Interfaces für die Module der bisherigen
Schichten:
Abbildung8:EineSchichtenarchitekturmitDIP
Der geübte Softwerker lässt beim Anblick dieser Module sogleich vor
seinem geistigen Auge ein Beziehungsgeflecht wie entstehen und weiß:
alles hübsch entkoppelt und testbar.


---


<!-- Page 22 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 18
Abbildung9:ÜberInterfacesentkoppelteSchichten
Und was ist der Nutzen des ganzen Aufwands? Im nächsten Codeaus-
schnitt sehen Sie, wie nun mit einer Attrappe die Businesslogik unabhän-
gig von darunterliegenden Details getestet werden kann. Die Implementa-
tion der aufrufenden Logik ist von der aufgerufenen durch das Interface
entkoppelt; erst zur Laufzeit wird bestimmt, wer aufgerufen wird.
Statt einen Datenzugriff konkret zu durchlaufen, werden die Stoppworte
im Test hart verdrahtet. Das ist trivial in puncto Laufzeit und Komplexität
und einfacher, als eine Stoppwortdatei zu benutzen.
Abbildung10:MiteinerAttrappewirddasTestenvonabhängigerLogikeinfach
Dass der Businesslogik aber überhaupt eine Attrappe untergeschoben
werden kann, ist der Anwendung des Inversion of Control (IoC)¹⁰ Prin-
zips geschuldet. Dessen Manifestation besteht hier im Hineinreichen der
Laufzeitabhängigkeit in die Businesslogik durch ihren Konstruktor (*con-
structor injection).
¹⁰https://de.wikipedia.org/wiki/Inversion_of_Control


---


<!-- Page 23 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 19
Abbildung 11: Injizieren der konkreten Implementation einer abstrakten Abhängigkeit zur
Laufzeit
Die Abhängigkeit vom Interface IDataaccess zur Compilezeit wird zur
Laufzeit durch die Injektion einer Implementation des Interfaces befrie-
digt. Nachfolgende sind die Compilezeit- und Laufzeitabhängigkeiten zu-
sammen visualisiert.
Abbildung12:MitDIPunterscheidensichdieAbhängigkeitenzuCompilezeitundLaufzeit
Das sieht jetzt schon nicht mehr so einfach aus wie das ursprüngliche
Schichtenmodell, würde ich sagen. Logik ist auch im Schichtenmodell bei
vortrefflicher Ausrichtung der Beziehungen immer noch funktional ab-
hängig. Um trotz dieser Abhängigkeiten Testbarkeit zu erlangen, müssen
zusätzliche Elemente eingeführt werden: Abstraktionen (hier: Interfaces).
Und aus einer Menge unidirektionaler Abhängigkeiten werden zwei Men-
gen, von denen eine auch noch gegenläufige Abhängigkeiten enthält.


---


<!-- Page 24 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 20
Das scheint der Preis der Wandelbarkeit zu sein. Verständlichkeit entsteht
durch Trennung von Verantwortlichkeiten und klare Beziehungen. Test-
barkeit entsteht durch DIP und IoC. Ist halt so. Da müssen wir durch.
UmdasLebennunwenigstensabereinwenigeinfacherzumachen,gibtes
Mock-FrameworkswieMoq¹¹(inAbbildung10benutzt)undDependency-
Injection-Frameworks wie Simple Injector¹² oder Unity¹³.
Jetzt ist es nur noch eine Sache konsequenter Anwendung von Prinzipien
und Werkzeugen, um sauberen Code zu schreiben. Alles scheint gesagt
zur grundlegenden Strukturierung von Logik.
Das ist zumindest der Stand des Bewusstseins, den ich bei Clean Code
Development Trainings¹⁴. Wenn ein Architekturmuster bekannt ist, dann
ist es MVC oder das Schichtenmodell. Zusätzlich wird dann noch die
FahnederSOLID-Prinzipien¹⁵hochgehalten,zudenen das DIPgehörtwie
auchdasSRP(SingleResponsibilityPrinciple),dassichmitVerantwortlich-
keitstrennung befasst.
NurleiderseheichebenfallsbeidenTeams,dieCodeSOLIDeinSchichten
strukturieren keine entspannten und freudvollen Gesichter. Der Code ist
immer noch schwer zu wandeln. Sonst würde man mit mir ja auch nicht
über Clean Code Development sprechen wollen.
Wie kann das aber sein? Trotz sauberer Schichtung immer noch nicht
sauber? Merkwürdig, oder?
Schichten in Schale werfen
Dass irgendetwas noch faul ist im Staate Dänemark, ist denn auch der
Branche schon bewusst geworden. Seit 2005 hat sich das Schichtenmodell
gewandelt. Aus den Schichten sind Schalen der einen oder anderen Art
geworden. Statt aus Kästchen bestehen die empfohlenen Architekturmus-
ternunauskonzentrischenFormen.Verantwortlichkeitensindineinander
organisiert statt übereinander.
¹¹https://github.com/Moq/moq4
¹²https://simpleinjector.org/index.html
¹³https://github.com/unitycontainer/unity
¹⁴https://ralfw.de/trainings/training-products/
¹⁵https://en.wikipedia.org/wiki/SOLID_(object-oriented_design)


---


<!-- Page 25 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 21
Vertreter solch konzentrischer Architekturmuster sind die Hexagonale
Architektur¹⁶, die Onion Architecture¹⁷ und die Clean Architecture¹⁸:
Abbildung13:KonzentrischeArchitekturmuster
Treiber für diese neue Grundorganisation ist eine Bedeutungsaufladung
der Verantwortlichkeiten. Dass es dezidierte Verantwortlichkeiten gibt,
dass es eine klare Richtung für Abhängigkeiten gibt, hat sich nicht verän-
dert.InderkonzentrischenAnordnungdrücktsichvielmehraus,dassman
erkannt hat, dass nicht alle Verantwortlichkeiten gleich sind. Irgendetwas
ist anders mit dem, was nun im Kern steht, im Vergleich zu dem, was am
Rand steht.
Ich hatte mich auch schon lange beim Schichtenmodell gefragt, warum
Businesslogik überhaupt von Datenzugriffslogik abhängig sein soll. War-
um sollte sich eine Geschäftsregel damit befassen, Daten zu beschaffen
oder zu speichern? Dass Businesslogik Daten braucht, auf denen sie ar-
beitet, und Daten erzeugt, ist selbstverständlich. Muss sie dafür aber den
Datenzugriff selbst steuern? Mir will das nicht in den Kopf. Das sieht für
mich wie eine Vermischung von Verantwortlichkeiten aus – auch wenn
es irgendwie so ganz normal erscheint.
In den konzentrischen Architekturen ist nun dieses Problem gelöst. Oder
zumindest scheinbar gelöst. Denn in konzentrischen Architekturen wei-
¹⁶https://en.wikipedia.org/wiki/Hexagonal_architecture_%28software%29
¹⁷http://jeffreypalermo.com/blog/the-onion-architecture-part-1/
¹⁸https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html


---


<!-- Page 26 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 22
sen die Abhängigkeiten von außen nach innen auf die Businesslogik hin
(Abbildung14).DieBusinesslogiksteuertnunaugenscheinlichnichtmehr
den Datenzugriff.
Abbildung14:KonzentrischeAbhängigkeitenmachenmehrSinn
Das macht mehr Sinn, finden Sie nicht auch? Je weiter außen eine Schale,
desto mehr beschäftigt sie sich mit technischen Details und desto volatiler
ist sie. Je weiter im Inneren eine Verantwortlichkeit, desto zentraler ist sie,
im wahrsten Sinne des Wortes, desto zeitloser und konstanter.
In der Clean Architecture (Abbildung 13) stehen Entities für sehr all-
gemeine, grundlegende Regeln. „Enterprise Business Rules“ können sich
naturgemäßnichtsohäufigundradikaländernwie„ApplicationBusiness
Rules“ der darum herum liegenden Use Cases.
Die konzentrischen Architekturmuster addieren also den Aspekt der Vo-
latilität zum Bild. Von außen nach innen, also in Richtung der Abhängig-
keiten wird Code immer „ruhiger“. Robert C. Martin sagt in seinem Buch
“Clean Architecture”¹⁹:
“The outer circles are mechanisms. The inner circles are poli-
cies.”
„Mechanisms“, also technische Vorrichtungen, sind eher Änderungen un-
terworfen als „Policies“ (Regeln).
¹⁹http://www.amazon.de/Clean-Architecture-Craftsmans-Software-Structure/dp/
0134494164


---


<!-- Page 27 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 23
Für ihn definieren die Schalen Ebenen:
“[T]he further in you go, the higher level the software beco-
mes.”
Aber was für Ebenen? Was ist das Kriterium, um eine Ebene zu bestim-
men?
„As you move inward, the level of abstraction and policy
increases.”
Die Ebene, auf der Regeln liegen, wächst nach innen. Und auch das
Abstraktionsniveau wächst nach innen. Jedenfalls für Robert C. Martin.
BeidenRegelngeheichnochmit.BeimAbstraktionsniveaubinichjedoch
ganz anderer Meinung. Aber dazu später mehr.
InjedemFallerweiterndiekonzentrischenArchitekturmusterdasBildum
eine Dimension. Das ist gut so. Verantwortlichkeiten liegen nicht alle auf
einer Ebene, egal, was dafür das Kriterium ist.
Aber was bedeutet das jetzt für den Code? Abbildung 15 zeigt meine
Bemühung, das Clean Architecture Muster auf das bisherige Beispiel zu
übertragen.
Bemüht habe ich mich, weil ich es Ihnen einerseits leicht machen möchte
zu sehen, wohin die Verantwortlichkeiten aus Abbildung 8 gewandert
sind; meine Clean Architecture soll also vergleichbar sein. Andererseits
wollte ich aber auch nicht zu weit von den Begriffen bei Robert C. Martin
abweichen; die Umsetzung soll also auch mit dem Muster vergleichbar
sein.


---


<!-- Page 28 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 24
Abbildung15:CodeartefakteineinerCleanArchitecture
AmeinfachstenistesfürSiebestimmt,dieSchalenderCleanArchitecture
in Abbildung 15 zu identifizieren. Von außen nach innen stehen dafür die
Projektverzeichnisse adapters, usecases, domain.
Als Adapter verstehe ich die Klassen, die den Zugriff auf Hardware kap-
seln, z.B. Tastatur oder Festplatte. Das sind Martins „mechanisms“.
Im Kern steht für mich die Domäne, bei der ich nicht weiter unterscheide,
ob es sich umEntities oder Services handelt (wenn ich einmal das Domain
Driven Design (DDD) Vokabular in Anschlag bringe).
Die Verantwortlichkeiten Dataaccess und Businesslogic haben sich auch
nicht sehr verändert. Allerdings ist das vormalige PresentationlogicLayer
nun zerfallen in Controller und Presenter.
Die Benutzerschnittstelle besteht aus zwei Teilen, weil der UseCase neu
hinzugekommen ist. Der ist ganz explizit in der Clean Architecture und
hat laut Martin folgenden Auftrag:


---


<!-- Page 29 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 25
„These use cases orchestrate the flow of data to and from the
entities […]”
Dafür ist im vorliegenden Fall nicht viel zu tun, aber ich habe mich
deshalb z.B. entschlossen, aus der Businesslogik das Laden des Textes
herauszunehmen:
Abbildung16:DerUseCasebeimOrchestrierenvonAdapternundBusinesslogik
Außerdem: Der Use Case „schiebt“ das Ergebnis der Wortzählung nun
an einen Presenter weiter, statt es seinem Aufrufer – dem Controller
– zurückzugeben. Das ist in der Clean Architecture auch ganz explizit
beschrieben:


---


<!-- Page 30 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 26
Abbildung17:DerUseCaseleitetOutputübereinenPortweiterandieumliegendeAdapter-
Schale
Tatsächlichträgt das „Anhängsel“der Clean Architecturein Abbildung 17
wesentlich dazu bei, den Code gemäß der Forderung „alle Compilzeitab-
hängigkeitenweisennachinnen“zustrukturieren.Ihmistgeschuldet,dass
die Implementation in Abbildung 15 fünf Interfaces statt der bisherigen
drei hat und diese auch noch auf zwei Ebenen definiert sind.
Beispiel Schaledomain: Die umschließende Schaleusecases kennt von der
Domäne nur das Interface IBusinesslogic, so wie das bisherige Presentati-
onlogicLayer vonderdarunterliegendenSchichtauchnurdiesesInterface
kannte.
So weit, so einfach und naheliegend.
Zusätzlich jedoch definiert die Schale domain das Interface IStopwords.
Das gehört für mich zu einer anderen Kategorie, deshalb habe ich es
in das Verzeichnis dependencies gesteckt. IStopwords wird nicht von der
Businesslogik implementiert, sondern von einer weiter außen liegenden
Schale! Genauer: von der Klasse Dataccess in adapters.
IStopwords ist in domain definiert, um der Forderung nach den Verweisen
nach innen zu genügen. Die äußere adapters-Schale hängt nun ganz sau-
bervonderinnerendomain-Schaleab–obwohlimmernochBusinesslogic
sich die Stoppworte selbst beschafft (Abbildung 18).
Das Schichtenmodell warda ausmeiner Sicht ehrlicher.Dort verliefendie
grundsätzlichen Abhängigkeiten von oben nach unten, so wie auch zur
Laufzeit der Kontrollfluss. In der Clean Architecture ist das nicht mehr
der Fall!


---


<!-- Page 31 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 27
Abbildung18:ZurLaufzeitrufteineinnereSchaleeineäußere
Vollziehen Sie das wirklich einmal nach anhand von Abbildung 15 und
Abbildung 18. Lassen Sie sich das auf der Zunge zergehen. Nehmen Sie
Abbildung 17 zur Hilfe. Hier geht es um den Kern der konzentrischen
Architekturen!
Das ist so wichtig, ich male es Ihnen auf. Zunächst die Compilezeitabhän-
gigkeiten in der nächsten Abbildung. Blicken Sie hier durch?
Abbildung19:DieAbhängigkeitengem.DIPinderCleanArchitecture
Das ist alles wunderbar nach DIP entkoppelt. Der Use Case ist nicht
von einer Domänenimplementation abhängig (Pfeil mit gefüllter Spitze),
sondern nur von einer Abstraktion (IBusinesslogic). Ebenfalls von der
abhängig ist ihre Implementation (jetzt Pfeil mit offener Spitze), die Busi-
nesslogic; sie nutzt aber nicht, sondern implementiert. Ebenso ist es mit
den anderen Implementationen, die in Abbildung 19 alle in der oberen
Zeile stehen. Keine Pfeile zwischen ihnen. Alle Pfeile weisen nach unten
auf Abstraktionen.


---


<!-- Page 32 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 28
Aber nicht nur die größere Zahl an Interfaces macht das Bild hier verwir-
render, finde ich. Dazu kommt ja noch die Zuordnung von Abstraktionen
und Implementationen zu Schalen. Schauen Sie genau hin, wie die Bezie-
hung zwischen äußeren und inneren Schalen wechseln. Ich zoome einmal
beispielhaft heran:
Abbildung20:ZurCompilezeithängtdieäußerevonderinnerenSchaleab
Der Controller in der äußeren Schale kennt nur IUseCase als Abstrakti-
on der inneren Use-Case-Schale (1); die Abstraktion gehört zur inneren
Schale, die sie auch implementiert. Gleichzeitig (!) ist die innere Schale
von der Abstraktion IPresenter abhängig, die jedoch von der äußeren
implementiert wird (2).
Verwirrend, oder? Jedenfalls empfinde ich das so. Und Robert C. Martin
gibt in seinem Buch für ein ähnliches Beispiel zu:
„Much of the complexity in that diagram was intended to
make sure that the dependencies between the components
pointed in the correct direction.”
Bitte lesen Sie das Zitat noch einmal!
KomplexitätistderFeindeinfacherWandelbarkeit.CleanCodePrinzipien
und Praktiken sollten sich also darum bemühen, Code-Komplexität zu
reduzieren. Und als Beispiel für Sauberkeit gilt dann ein Architekturmus-
ter, über das der Pate der Clean-Code-Bewegung sagt, es sei komplex
damit Abhängigkeiten in eine gewisse Richtung weisen? Komplexität für
Sauberkeit?


---


<!-- Page 33 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 29
Ich muss gestehen, das bin ich nicht bereit zu akzeptieren. Diesen Preis
möchte ich nicht bezahlen. Wandelbarkeit in Form von Verständlichkeit
und Testbarkeit möchte ich nicht dadurch bekommen, dass ich Komplexi-
tät bewusst in diesem Ausmaß erhöhe.
Ich habe es bei der Implementation des Beispiels als Clean Architecture
schon bemerkt und nun, als ich Abbildung 19 erarbeitet habe, ist es
mir noch deutlicher geworden: Was in konzentrischen Kreisen noch klar
aussieht und eine simple Regel definiert – „Abhängigkeiten weisen immer
nach innen“ –, verliert diese Eigenschaften im Code.
Die Krone wird dem aufgesetzt, wenn Sie sich klarmachen, wie die Lauf-
zeitabhängigkeiten aussehen: Die weisen nämlich von außen nach innen
und dann wieder nach außen. Das gute, alte Schichtenmodell ist zurück.
Wofür also die Steigerung der Komplexität? Was ist wirklich gewonnen
durch die konzentrischen Architekturmuster?
Abbildung 21: Die Laufzeitabhängigkeiten zeigen von außen nach innen und wieder nach
außeninderCleanArchitecture


---


<!-- Page 34 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 30
Ist die Hoheit über die Definition der Abstraktionen so entscheidend? Im
Schichtenmodell hat z.B. die Datenzugriffsschicht ihr Interface definieren
und implementieren dürfen; in der Clean Architecture hingegen definiert
es die Domäne. Die Hoheit über die Abstraktion soll weiter innen liegen,
weil dort mehr Stabilität herrscht? Den Preis dafür finde ich sehr hoch.
Reflexion
Früher war nicht alles besser. Codezustände wie in Abbildung 1 will
niemand (wieder) haben.
Die erste Variante des Schichtenmodells jedoch, die war gar nicht so
schlecht. Die klare Trennung von Verantwortlichkeiten kombiniert mit
einerkonsequentenAusrichtungderAbhängigkeitenhatdieVerständlich-
keit deutlich gesteigert (Abbildungen 4 und 5).
Für gute Wandelbarkeit war das allerdings noch nicht genug. Die braucht
nicht nur Verständlichkeit, sondern auch Testbarkeit. Die war in der ers-
ten Schichtenvariante noch begrenzt. Lediglich die Logik der untersten
Schicht war gut testbar, weil sie für sich stand. Die Logik in den darüber
liegenden Schichten konnte zwar grundsätzlich schon gezielt angespro-
chen werden, nur musste dann auch immer die Logik darunter liegender
Schichten beim Test mit durchlaufen werden. Das kostet Zeit und das
macht es nicht leicht, einen Bug zu lokalisieren.
Die Testbarkeit ist dann in der zweiten Variante des Schichtenmodells
(Abbildungen 8 und 9) nachgezogen worden. Durch Anwendung von DIP
und IoC können für Tests untere Schichten ausgeblendet werden. Wenn
etwas schiefgeht, dann weiß man, dass der Fehler in der Logik der zu
testenden Schicht steckt.
Allerdings: Dieser Fortschritt in der Testbarkeit hat seinen Preis. Der
wird deutlich in der Clean Architecture Variante (Abbildungen 15 und
19). DIP und IoC addieren Komplexität, die die Verständlichkeit nun –
zumindest nach meinem Empfinden – massiv reduziert. Man ist über das
Ziel hinausgeschossen. „Mehr vom Selben“ (hier: DIP und IoC) hat den
Fortschritt, den die zweite Variante des Schichtenmodells gebracht hat,
nicht vergrößert. Im Gegenteil!
Aber wie kommt das? Ich glaube, es liegt daran, dass man zu sehr auf die
Compilezeitabhängigkeiten gestarrt hat.


---


<!-- Page 35 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 31
Von der Schichtung zur Konzentrik überzugehen hat etwas mit dem Com-
pilezeitabhängigkeiten zu tun. Im Schichtenmodell war das Volatile (oder
Instabile), Robert C. Martins „mechanisms“, nicht konsequent in einer
Position, wo Veränderungen wenig Probleme machen.
Relativ problemlos sind Veränderungen nämlich dort, wovon nur wenige
oder keine Codeeinheiten abhängig sind. Im Schichtenmodell ist das nur
für die Präsentationslogik der Fall. Die Datenzugriffslogik hingegen, die
ebenfalls ein „mechanism“ ist, muss wegen der Abhängigkeit anderer von
ihr, Stabilität zusichern.
Das wurde mit der Clean Architecture bewusst verändert. Dort sind nicht
nurdieAbhängigkeitensauberausgerichtet,sondernauchdieVerantwort-
lichkeiten nach Stabilität positioniert: am stabilsten sind ganz allgemeine,
grundlegende Regeln im Kern, am instabilsten die Kommunikation mit
der Umwelt in der äußeren Schale.
Diese Sichtweise gefällt mir – allerdings hat die Implementation eben ei-
nenhohenPreis.Abbildungen17und20machenesexemplarischdeutlich:
die Verständlichkeit der Zusammenhänge im Code sinkt.
Aber selbst wenn ich einmal über den auch von Robert C. Martin beklag-
ten Mehraufwand hinwegsehe, frage ich mich, was wirklich gewonnen
ist. Denn Abbildung 21 zeigt ein Bild, das sich im Grunde nicht vom
Schichtenmodell unterscheidet. Zur Laufzeit ist eine Businesslogik immer
noch vom Datenzugriff abhängig.
Was soll das? Da mag zur Compilezeit die Abhängigkeit umgekehrt sein
– Adapter außen hängt von Domäne innen ab –, doch zur Laufzeit gehen
die Aufrufe dorthin durch die Domäne in die Tiefe.
Es ist letztlich nichts gewonnen. Die Abstraktion, von der die Businesslo-
gik abhängig ist, ist lediglich verschoben worden. Vorher gehörte sie zur
darunterliegendenSchicht(IDataaccessLayer inAbbildung9),jetztgehört
sie zur Businesslogik selbst (siehe IStopwords in Abbildung 19).
Dass nichts gewonnen ist, ist deutlich zu bemerken beim Testen. Das
Architekturbildsuggeriert,dasseineinnereSchalekeineAbhängigkeithat
zu einer äußeren – doch beim Testen stellt sich das Gegenteil heraus. In
Abbildung 17 ist der Use Case Interactor – also Code der Use-Case-Schale
– zur Laufzeit abhängig vom Presenter in der darüberliegenden Schale.


---


<!-- Page 36 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 32
Dass der Use Case Output Port zur Use-Case-Schale gehört, kaschiert das
nur. Im Test muss trotzdem eine Attrappe gebaut werden.
Sind Sie noch da oder haben Sie schon halb abgeschaltet? Das würde
mich nicht wundern. Bei dem ganzen hin und her der Abhängigkeiten
von Compilezeit und Laufzeit, kann einem schon der Kopf schwirren. Ich
jedenfalls verliere bei der Darstellung der vollständigen Abhängigkeiten
der implementierten Clean Architecture den Überblick (Abbildung 22).
So sieht für mich ein Testalbtraum aus. Ganz zu schweigen davon, dass
damit das Rätselraten darum, für welche Klassen ein Interface definiert
werden sollte, weiter angeheizt wird. Im Zweifelsfall lautet dann die
Antwort „Für alle!“ und damit explodiert die Zahl der Dateien in einem
Projekt (wenn man je Klasse und je Interface eine Datei denkt).
Abbildung22:DasvollständigeAbhängigkeitsbildderimplementiertenCleanArchitecture
Das einzig Positive, das ich der Clean Architecture abgesehen vom hüb-
schen Bild abgewinnen kann, ist die Tendenz zur Aufspaltung von Abs-
traktionen.SiescheintdieAnwendungdesInterfaceSeggregationPrincip-
le (ISP)²⁰ nahezulegen. Schmalere Interfaces helfen einfach bei der Ent-
kopplung.
Wo vorher nur eine Präsentationslogikschicht und eine Datenzugriffs-
schicht mit respektiven Abstraktionen waren, sind beide nun zerfallen
in mehrere Teile: Controller und Presenter sind getrennt und es gibt
IPresenter; ebenfalls getrennt sind IText und IStopwords, wo vorher nur
IDataAccessLayer war.
²⁰https://en.wikipedia.org/wiki/Interface_segregation_principle


---


<!-- Page 37 of 84 -->


1-EineKritikbisherigerArchitekturmodelle 33
Am Ende ist dieser positive Effekt für mich jedoch nicht ausschlaggebend.
Viel wichtiger finde ich das Sinken der Verständlichkeit durch eine ge-
stiegene Artefaktzahl und den weiterhin hohen Testaufwand. Denn jede
Laufzeitabhängigkeit ruft zur Testzeit nach einer Attrappe.


---


<!-- Page 38 of 84 -->


2 - Das IODA
Architekturmodell
Wie könnte ein Architekturmuster aussehen, das die Vorteile der bisheri-
gen beibehält und ihre Nachteile hinter sich lässt?
Die Vorteile sind:
- Definition von „Standardverantwortlichkeiten“, die es voneinander ab-
zugrenzen gilt, um die Verständlichkeit zu erhöhen und grundsätzliche
Testbarkeit herzustellen.
• Bewusstmachung der Wichtigkeit von klar ausgerichteten Abhän-
gigkeiten für Verständlichkeit und Testbarkeit.
Und die Nachteile:
• Schlecht testbare funktionale Abhängigkeiten.
• Undurchsichtigkeit/zusätzliche Komplexität durch Entkopplungs-
aufwand.
Funktionale Abhängigkeiten als
Wurzelproblem
Der zentrale Nachteil der erwähnten populären Architekturmuster ist
ihre Gründung auf funktionalen Abhängigkeiten. Die Notwendigkeit zu
funktionalenAbhängigkeitenwurdeniehinterfragt.Unddiefunktionalen
Abhängigkeiten haben sich über die Jahrzehnte auch nicht verändert. Sie
existieren in der Implementation einer Clean Architecture genauso wie in
einer ersten Implementation der Schichtenarchitektur noch ohne DIP/IoC.
Funktionale Abhängigkeiten lassen sich nicht wegzaubert mit DIP/IoC.
Ob sie existieren, ist keine Sache der Compilezeitabhängigkeiten, sondern


---


<!-- Page 39 of 84 -->


2-DasIODAArchitekturmodell 35
der Laufzeitabhängigkeiten. Wo immer eine Attrappe in einem Test ge-
baut werden muss, um Logik gezielt testen zu können, da existiert eine
funktionale Abhängigkeit.
Damit Sie wirklich verstehen, was ich mit funktionalen Abhängigkeit
meine,mussichkurzdenschonhäufighierbenutztenBegriff„Logik“defi-
nieren.Logik sind die Anweisungen,die Funktionalität für den Anwender
tatsächlich herstellen. Das sind vor allem:
• Transformationsanweisungen/Operatoren
• Kontrollflussanweisungen
• Input-/Output-Anweisungen oder allgemeiner API-Calls
Durch Abarbeitung nur dieser Anweisungen bekommt Software ihr Ver-
halten. Wenn Logik passend zusammengestellt ist, funktioniert Software.
Aber was ist zu Anforderungen passende Logik? Das ist schwierig zu
sagen. Das ist die Kunst der Programmierung. Da kann leicht etwas
schiefgehen. Deshalb muss Logik sorgfältig getestet werden – natürlich
automatisiert. Um das zu erreichen, muss Logik überhaupt erstmal testbar
sein.
Schauen Sie noch einmal Abbildung 2 an. Dort sehen Sie ausschließlich
Logik, sogar Logik mit ganz unterschiedlicher Verantwortlichkeit. Teile
der Logik erfüllen die eine Teilfunktionalität, z.B. Zerlegung des Textes in
Worte, andere Teile der Logik erfüllen eine andere Teilfunktionalität, z.B.
Bestimmung der verschiedenen Worte.
Jede dieser Verantwortlichkeiten kann fehlerbehaftet sein. Jede verdient
eigenständige Tests. Das ist in dem Verantwortlichkeitsmischmasch aber
nicht machbar. Die Testbarkeit der Verantwortlichkeiten ist gleich Null.
Vergleichen Sie damit Abbildung 18. In der Clean Architecture sind Ver-
antwortlichkeiten getrennt. Der Anteil an Logik, der sich um die Wortzäh-
lung kümmert, ist nun freigestellt in einer eigenen Funktion. Damit kann
die Wortzählungslogik separat von der Benutzerschnittstellenlogik oder
von der Logik zum Laden des Textes aus einer Datei getestet werden.
Allerdings: Die Logik zur Wortzählung ist noch funktional abhängig. In-
nerhalb von Count_words() wird weitere Logik in Retrieve() aufgerufen,
deren Funktionalität für die Logik in Count_words() relevant ist.


---


<!-- Page 40 of 84 -->


2-DasIODAArchitekturmodell 36
Diese funktionale Abhängigkeit verhagelt die Testbarkeit von Count_-
words(). Durch diese Abhängigkeit kann bei einem fehlschlagenden Test
nicht eindeutig bestimmt werden, wo das Problem liegt: in der Logik von
Count_words(), die eigentlich getestet werden soll, oder in der Logik von
Retrieve()?
Aufgelöst wird diese Unsicherheit durch DIP/IoC: Sie ersetzen dann die
Abhängigkeit im Test einfach durch eine Attrappe.
• Erstens macht das aber Aufwand, weil dafür in streng typisierten
Sprachen ein Interface nötig ist (DIP).
• Zweitens macht das Aufwand, weil die Attrappe überhaupt codiert
werden muss.
• Drittens muss die Attrappe verfügbar gemacht werden (IoC).
• Viertens muss die Attrappe so konfiguriert werden, dass sie zu dem
passt, was in der zu testenden Funktion passiert; die Attrappe er-
zwingt sowohl Wissen über die Verarbeitung in der zu ersetzenden
Funktion wie in der zu testenden.
Und schließlich: Funktionale Abhängigkeiten widersprechen ganz prinzi-
piell sauberer Softwareentwicklung.
• Funktionale Abhängigkeiten verhindern die Einhaltung des Single
Responsibility Principle (SRP), weil mit ihnen die abhängige Funkti-
on immer mindestens zwei Verantwortlichkeiten hat: einerseits die
Erfüllung einer Funktionalität mit Logik, andererseits den Aufruf
von Funktionen in passender Reihenfolge mit den richtigen Para-
metern. Letzteres nenne ich Integration als eine besondere Form
der Komposition. Das Resultat: schlechte Testbarkeit, schlechte Ver-
ständlichkeit.
• Funktionale Abhängigkeiten verhindern die Einhaltung des Prin-
zips Single Level of Abstraction (SLA). Logik ist per definitionem
auf einem niedrigeren Abstraktionsniveau als der Aufruf von Logik
in einer anderen Funktion. Das Resultat: schlechte Verständlichkeit.
Dass man Prinzipien wie DIP/IoC anwenden muss, um die Kompromittie-
rungvonSRPundSLAwettzumachen,entschärftdieLagenicht,sondern
mach sie schlimmer. Denn DIP/IoC erzeugen künstlich Komplexität, wie
oben selbst Robert C. Martin beklagt.


---


<!-- Page 41 of 84 -->


2-DasIODAArchitekturmodell 37
DaszentraleProblemderüblichenArchitekturmusteristmithinCode,der
wie folgt aussieht: in einer Funktion wechseln sich Logik und Aufrufe
anderer Funktionen ab.
Abbildung23:InfunktionalerAbhängigkeitwechselnsichLogikundFunktionsaufrufeab
Dieses Bild stellt ganz deutlich die Laufzeitabhängigkeiten dar. Es ändert
sichalsoauchmitnochsovielDIP/IoCnicht.DurchAnwendungderPrin-
zipien wird höchstens diese Realität kaschiert – bis Sie in Tests unschön
daran erinnert werden.
Um die Logik von f() für sich genommen testen zu können, müssen Sie
Attrappeneinführen.UndselbstdannwirdnurdiegesamteLogikgetestet,
so dass bei einem Fehler unklar ist, ob der im ersten, zweiten oder dritten
Abschnitt der Logik seine Ursache hat; oder der Fehler liegt sogar in
einer fehlerhaften Attrappe. Die Logikanteile zwischen den funktionalen
Abhängigkeiten sind für sich genommen immer noch nicht testbar.
EineFunktionwief() hatdeshalbausmeinerSichtimmern+2 Verantwort-
lichkeiten. n steht dabei für die Zahl der funktionalen Abhängigkeiten.
• Vor jedem Funktionsaufruf steht Logik (n) und auch nach dem
letzten nochmal (+1); jede dieser Logik-Passagen tut etwas anderes
undstellteineVerantwortlichkeitdar.Vielleichtistdasnichtimmer
so, aber diese Verallgemeinerung halte ich für hilfreich. Sie macht
das Problem deutlicher, als eine Erbsenzählerei, ob wirklich um
jeden Funktionsaufruf herum Logik steht.
• Die Integration der ganzen Funktionsaufrufe mit der Logik ist eine
separate, übergeordnete Verantwortlichkeit (+1).
Die Verantwortlichkeiten, die ich hier meine, sind formal, nicht inhaltlich.
Sie ergeben sich allein aus der Struktur. Darüber hinaus kann es also
innerhalb der Logik-Blöcke weitere Verantwortlichkeiten geben.


---


<!-- Page 42 of 84 -->


2-DasIODAArchitekturmodell 38
Die Testbarkeit einer Codebasis steht damit in umgekehrt proportionalem
VerhältniszurfunktionalenAbhängigkeitderFunktionenineinerCodeba-
sis. Je mehr Verantwortlichkeiten eine Funktion hat, desto schwerer ist sie
testbar. Und sie hat umso mehr Verantwortlichkeiten, je mehr funktionale
Abhängigkeiten sie enthält.
Außerdem ist eine solche Codebasis weniger verständlich. Denn funktio-
nale Abhängigkeiten widersprechen nicht nur dem SRP und dem SLA,
sondern sorgen auch dafür, dass es keine Grenze gibt beim Funktionsum-
fang. Solange funktionale Abhängigkeiten ok sind, solange sind auch 100,
1.000 oder 10.000 Zeilen lange Funktionen ok.
MitfunktionalenAbhängigkeitenwächstderMethodenumfangganzselbst-
verständlich bei Bedarf. Wenn zu 100 Zeilen noch 40 dazu kommen sollen,
dann werden vielleicht 15 in eine Funktion extrahiert und aufgerufen –
eine funktionale Abhängigkeit ist entstanden – und die 40 neuen Zeilen
werden dazu gepackt. Am Ende sind in der ursprünglichen Funktion 125
Zeilen. Und so geht es weiter und weiter. Refactorings wie extract method
scheinen sogar die Hemmschwelle gesenkt zu haben, Funktionen länger
und länger zu machen. Es ist ja so einfach, etwas (scheinbar) Gutes zu tun,
d.h. ein wenig Logik (inkl. funktionaler Abhängigkeiten) zu extrahieren.
Da darf man sich anschließend gönnen, weitere Logik auf allen Ebenen
dazu zu packen.
Das verringert die Verständlichkeit des Codes weiter, weil dadurch Funk-
tionalität in der Tiefe gestaffelt wird. Jeder Überblick, wie Logik Verhal-
ten erzeugt, geht auf diese Weise verloren. Die Folge können nur lange
Debugging-Sitzungensein,indenenLogikdanninderTiefeverfolgtwird.
Wenn Sie es kurz und knackig mögen, ist mein Vorschlag, Sie berechnen
die Testbarkeit einer Funktion so: 1 / Anzahl der Verantwortlichkeiten.
Der Wert 1 stellt danach den höchsten Wert für Testbarkeit dar. Eine
Funktion hat dann nur eine Verantwortlichkeit. Je weiter der Wert gegen
0 tendiert, desto schlechter die Testbarkeit.
Verantwortlichkeiten zu erkennen ist durchaus eine Kunst, wenn es um
inhaltliche geht. Die Geschmäcker können da schon im Detail auseinan-
dergehen. Wie viele Verantwortlichkeiten identifizieren Sie in der hervor-
gehobenen Logik in Abbildung 6?
Doch das ist schon die Kür, aus meiner Sicht. Davor steht die Pflicht, d.h.
die Erkennung der formalen Verantwortlichkeiten aufgrund funktionaler


---


<!-- Page 43 of 84 -->


2-DasIODAArchitekturmodell 39
Abhängigkeit.NachderobigenFormelsinddasinAbbildung6fürCount_-
words() 1+2=3; die Testbarkeit hat also nur den Wert 1/3=0,33.
Schauen Sie jetzt zum Vergleich Abbildung 24 an. Beide Datenzugriffsme-
thoden haben keine (!) funktionalen Abhängigkeiten; sie enthalten reine
Logik.IhreformaleVerantwortlichkeitszahlistdamit1unddieTestbarkeit
hat den Wert 1/1=1. Besser geht’s nicht.
Abbildung24:FunktionenohnefunktionaleAbhängigkeitensindbestenstestbar
Dass die Methoden von Dataaccess gut testbar sein würden, war aber
schon in Abbildung 21 erkennbar, wenn Sie dorthin jetzt nochmal zurück-
blättern. Die Klasse hat keine Abhängigkeiten; sie ist – wie Presenter –
ein Blatt im Baum der Laufzeithierarchie. Keine Attrappen nötig, um sie
zu testen. (Dass der Test von Funktionen, die auf Ressourcen zugreifen,
auch nicht ganz einfach ist, steht auf einem anderen Blatt. Für das hiesige
Argument ist das nicht wichtig.)
Auflösung funktionaler Abhängigkeiten
Wenn funktionale Abhängigkeiten Verständlichkeit und Testbarkeit ver-
ringern, wie können die verhindert werden? Soll Software auf Funktionen
verzichten? Natürlich nicht!
Funktionen sind wertvolle Strukturierungsmittel für Logik. Um funktio-
nale Abhängigkeiten los zu werden, brauchen wir davon mehr, nicht
weniger.


---


<!-- Page 44 of 84 -->


2-DasIODAArchitekturmodell 40
Dass es ohne funktionale Abhängigkeiten geht, zeigen schon die Funktio-
nen in Abbildung 24. Sie sind Beispiele für eine Art von Funktionen, die
ohne auskommt. Ich nenne sie Operationen.
OperationenenthaltenausschließlichLogik.SierufenkeineweiterenFunk-
tionen auf, über deren Logik Sie Kontrolle haben, d.h. deren Quellcode
Ihnen (leicht) zugänglich ist. Dass eine Operation einen Vergleichsopera-
tor benutzt oder einen API-Funktionsaufruf wie File.ReadAllLines() tätigt,
zählt nicht als funktionale Abhängigkeit. Solche Funktionen aufzurufen
ist der Job einer Operation. Ob sie das korrekt im Sinne ihrer Verantwort-
lichkeit tut, gilt es mit automatisierten Tests zu prüfen.
Software kann allerdings nicht nur aus Operationen bestehen. Dann wür-
de die ganze Logik eingepackt in Funktionen nur nebeneinanderstehen,
ohne zusammen zu wirken. Operationen müssen also aufgerufen werden.
Irgendwo muss es zumindest eine Funktion geben, die wiederum zumin-
dest Operationen als Funktionen aufrufen – allerdings, ohne dass dadurch
funktionale Abhängigkeiten entstehen.
Zum Glück ist das ebenfalls möglich. Beispiele sehen Sie in Abbildung 16.
Count_words_in_file() und Count_words() sind Funktionen, die andere
Funktionen aufrufen – allerdings selbst keine Logik enthalten. Auch sie
sind damit frei von funktionalen Abhängigkeiten. Diese Art von Funktio-
nen nenne ich Integration.
Integrationen haben formal nur eine Verantwortlichkeit: sie integrieren,
d.h. sie binden andere Funktionen zusammen zu einer größeren. Aus
vielen verschiedenen Funktionen wird eine neue auf höherem Abstrak-
tionsniveau.
OperationenabstrahierenvonLogik-Details,dienötigsind,umFunktiona-
lität herzustellen. Integrationen abstrahieren von den Detail-Funktionen,
aus denen ein größerer Funktionsbaustein zusammengesetzt ist. Operatio-
nen und Integrationen sind Kompositionen; die mittel, mit denen sie das
tun, sind jedoch verschieden.
AberwiestehtesmitderTestbarkeitvonIntegrationen,diemehrereFunk-
tionen aufrufen? Da Integrationen nur eine formale Verantwortlichkeit
haben, ist ihre Testbarkeit ebenfalls 1/1=1.
Wenn eine Integration überhaupt automatisiert getestet wird, müssen
die aufgerufenen Funktionen nicht durch Attrappen ersetzt werden. Im


---


<!-- Page 45 of 84 -->


2-DasIODAArchitekturmodell 41
Gegenteil! Es ist wichtig, dass die realen Funktionen im Test ausgeführt
werden, um sicherzustellen, dass die Integration ihren Job tut und ein
umfassenderes Verhalten aus Einzelverhalten herstellt.
In vielen Fällen müssen Integrationen aber gar nicht automatisiert ge-
testet werden, weil es keine Logik zu testen gibt und die Sequenz der
Funktionsaufrufe offensichtlich korrekt ist im Sinne der Hypothese, dass
damit ein bestimmter Effekt erzielt wird. Man kann dann sozusagen einen
“Induktionsschluss” wagen: Wenn die aufgerufenen Funktionen korrekt
sind, dann ist die Integration ebenfalls korrekt.
Eine Ausnahme bildet die Integration an der Wurzel einer Aufrufhierar-
chie. Aber auch dort müssen nicht zwangsläufig Attrappen zum Einsatz
kommen.
Funktionen spielen in den traditionellen Architekturmustern keine Rolle.
Funktionen sind dort in ihrer Art alle gleich. Auch wird der Begriff Logik
nicht benutzt außer als Namenssuffix. Fast alle Funktionen sind deshalb
Hybride mit zwiefacher Verantwortlichkeit. Sie operieren und integrieren,
sie enthalten Logik und rufen andere Funktionen auf. Eine Ausnahme
bilden lediglich die wenigen Funktionen am Fuße der Abhängigkeitshier-
archie.


---


<!-- Page 46 of 84 -->


2-DasIODAArchitekturmodell 42
Abbildung 25: Übliche Architekturmuster erzeugen Hierarchien hybrider Funktionen mit
funktionalAbhängigkeiten
Und nochmal: daran ändert der ganze Wirbel um DIP/IoC und die Aus-
richtungvonCompilezeitabhängigkeitennichts.HybrideFunktionensind
immer schwer zu testen.
Sobald Funktionen jedoch grundsätzlich in Operationen und Integratio-
nen getrennt werden, entsteht eine andere Hierarchie.
Abbildung26:DieGrundlageeinesneuenArchitekturmustersisteineHierarchiegetrennter
Verantwortlichkeitsarten
In ihr gibt es mehr Funktionen, die jedoch alle kleiner sind als die bisheri-
gen Hybride. Logik befindet sich darin nur noch in den Blättern.


---


<!-- Page 47 of 84 -->


2-DasIODAArchitekturmodell 43
Mehr Funktionen entstehen, weil die Logikanteile bisheriger Hybride her-
ausgezogen werden müssen in Operationen. Doch das sollte Ihnen keine
Angst machen. Im Gegenteil! Endlich ist Logik viel leichter testbar. End-
lich sind die Funktionen viel übersichtlicher.
DasMittel,umeinesteigendeZahlvonFunktionenindenGriffzubekom-
men, liegt außerdem auf der Hand: Klassen (oder allgemeiner: Module).
Nicht nur werden also Funktionen kleiner, sondern auch Klassen werden
übersichtlicher, weil deren Zahl steigt bei fallendem Umfang.
Durch die Brille der mainstream Objektorientierung betrachtet, mag das
ungewöhnlich aussehen. Doch letztlich ist es das, was auf die eine oder
andere Weise immer wieder versucht wurde. Nur sind die bisherigen
Empfehlungen sperrig, weil sie auf einem Paradigma basieren, das sie
nicht hinterfragen. Es lautet: Funktionen sind Hybride.
Wird das Paradigma jedoch aufgegeben zugunsten einer Unterscheidung
von Integrationen und Operationen, tritt der gewünschte Effekt ganz
natürlich ein. Das ist jedenfalls meine Erfahrung nach Jahren der Soft-
wareentwicklung auf diese Weise.
Operationen verbinden
Es gibt noch ein weiteres Problem, unter dem die üblichen Architektur-
muster leiden: sie bieten keinen Platz für Daten. Das ist umso missli-
cher, als dass Daten schon früher in Programmablaufplänen und Nassi-
Shneiderman-Diagrammen keine Abbildung fanden und somit globalen
Daten und daraus resultierend unkontrolliert wachsenden Datenabhän-
gigkeiten Vorschub geleistet wurde.
Auf Architekturebene sind Daten in den Diagrammen entweder gar nicht
zu sehen oder sie werden in den Klassen der Schichten und Schalen
schlicht automatisch mitgedacht. So wie hybride Funktionen Verantwort-
lichkeiten vermischen, vermischen die Klassen in den bisherigen Archi-
tekturenebenfalls Verantwortlichkeiten.Sie fassen Funktionen und Daten
unterschiedslos zusammen.
Das mag scheinbar durch die Objektorientierung nahegelegt sein, die
ja angetreten war, gerade Funktionen und Daten näher zusammen zu
bringen,umKapselungzuerreichen.DochauchwenndasdurchMittelder


---


<!-- Page 48 of 84 -->


2-DasIODAArchitekturmodell 44
Objektorientierungmöglichist,bedeutetdasnicht,dassesunsystematisch
geschehen sollte. Leider liefern die Architekturmuster hier jedoch keine
Hinweise.
Ein modernes Architekturmuster, das über Bisheriges hinausgeht, sollte
also das Thema Daten ebenfalls adressieren, um die Lücke zu schließen.
Nicht nur funktionale Abhängigkeiten sind zu entschärfen bzw. ganz zu
eliminieren, sondern auch Datenabhängigkeiten sind zu explizieren.
Zum Glück ist das ganz leicht und ergibt sich in natürlicher Weise aus
Abbildung 26. Integrationen enthalten keine Logik. Wie kommunizieren
also die Operationen überhaupt miteinander? Das kann nur über Daten
geschehen.
Selbstverständlich ist das auch bei den Hybriden und Operationen in
Abbildung 25 der Fall. Dort fließen Daten von oben nach unten und von
unten nach oben in der Hierarchie. Die Logik enthaltenden Funktionen
sind hier jedoch alle direkt verbunden. Deshalb sind Daten kein Thema.
OhneeineVerbindungzwischenLogikinverschiedenenFunktionen,stellt
sich die Datenfrage allerdings sehr deutlich. Die Antwort darauf zeigt die
folgende Abbildung:
Abbildung27:OperationenstehenüberDateninKontakt
Operationen sind abhängig von Daten, die sie entweder austauschen (flie-
ßende Daten) oder die sie gemeinsam nutzen (ruhende Daten, Zustand).
Zwar sind gewöhnlich fast alle Operationen über Daten verbunden, doch
interessant sind vor allem Datenstrukturen, die Sie selbst definieren.


---


<!-- Page 49 of 84 -->


2-DasIODAArchitekturmodell 45
Solche Datenklassen dürfen natürlich nicht der Forderung widersprechen,
auf funktionale Abhängigkeiten zu verzichten; sie hängen ja unter den
Operationen im Bild. Deshalb sollten Klassen, die Daten sind, keine Me-
thoden besitzen.
Andere Klassen, die Daten haben, publizieren ihre Daten hingegen nicht.
Sie stehen deshalb in Abbildung 27 nicht auf der untersten Ebene.
In Bezug auf Klassen, die keine Funktionen haben, bestehen keine funktio-
nalen Abhängigkeiten. Das Verhältnis zwischen Integration und Operati-
on setzt sich also fort zu den Daten.
Zumindest zunächst.
Denn am Ende ist diese Rigorosität nicht durchzuhalten. Sie würde Mög-
lichkeiten der Objektorientierung zur Kapselung ungenutzt lassen. Des-
halb können aus meiner Sicht auch Klassen, die Daten sind, Methoden
besitzen – allerdings nur in begrenzter Weise.
Methoden von Datenklassen haben lediglich den Zweck, die Konsistenz
derDatensicherzustellenunddenDatenzugriffzuermöglichen.Stackund
Queue sind dafür gute Beispiele: das sind Klassen, die eine Datenstruktur
implementieren (Abstrakter Datentyp (ADT)), aber nur Methoden anbie-
ten,umdie„Form“derDatenaufrechtzuerhaltenbzw.denZugriffdarauf
zu ermöglichen.
Wenn Operationen Methoden auf solchen Datenobjekten benutzen, dann
sehe ich darin keine belastende funktionale Abhängigkeit. Für Daten-
strukturen müssen keine Abstraktionen definiert werden, um sie in Tests
zu ersetzen. Datenklassen, die in dieser Weise funktional einfach und
fokussiert gehalten werden, erzeugen keine zusätzliche Komplexität. Sie
machen nichts schwieriger zu verstehen. Im Gegenteil! Immer wieder
hilft es, Logik aus Operationen herauszuziehen in Datenstrukturen, um
Operationen und Integrationen zu entzerren.
Als Beispiel habe ich einmal die Businesslogik des bisherigen Szenarios in
diesemSinneverändert.IntegrationenundOperationensindimfolgenden
Listingsaubergetrennt.AußerdemistShredderedText alsDatenklassemit
minimaler Logik herausgezogen und dient der Kommunikation zwischen
den Operationen Shred() und Filter().


---


<!-- Page 50 of 84 -->


2-DasIODAArchitekturmodell 46
Abbildung28:EineDatenklasseverbindetOperationen
Dass die Integration Eigenschaften auf ShredderedText aufruft, das Da-
tenobjekt selbst also gar nicht nach Filter() hineinfließt, ist lediglich eine
naheliegende Optimierung. Sie ändert nichts am Zweck der Datenklasse,
Daten zu sein und Operationen zu verbinden.
Verbindung zur Außenwelt
In den konzentrischen Architekturmustern gibt es noch einen Aspekt, der
hinzugekommen ist bzw. deutlicher gemacht wurde gegenüber MVC und
Schichtenmodell: die Kommunikation mit der Außenwelt.
I/O-OperationenoderallgemeinerAPI-AufrufeaufBibliothekenundFrame-
works, die nicht unter Ihrer Kontrolle stehen, sind etwas Besonderes. Ei-
nerseits geht von dort immer wieder Behinderung von Tests aus, weil I/O
vergleichsweise imperformant ist und/oder Einrichtungsaufwand bedeu-
tet. Andererseits unterliegen externe Bibliotheken unkontrollierten Ände-
rungenodersollengaraustauschbarsein.Beideslegtnahe,API-Aufrufein
möglichst wenigen Modulen zu isolieren. Hier kommt das Prinzipienduo
DIP/IoC dann tatsächlich zu gutem Einsatz.


---


<!-- Page 51 of 84 -->


2-DasIODAArchitekturmodell 47
BeidenkonzentrischenArchitekturmusternistzumindestI/Odeutlichauf
die äußere Schale beschränkt, die noch zum Softwaresystem gehört. In
Abbildung 13 finden Sie zu diesem Zweck Adapter in der Hexagonalen
Architektur und Controller, Gateways, Presenter in der Clean Architectu-
re.
Das Schichtenmodell ist in dieser Hinsicht wenig explizit und undifferen-
ziert. Nur Benutzerschnittstelle und Datenzugriff scheinen grundsätzlich
verschieden zu sein (Abbildung 14). Das macht auch eine seiner Schwä-
chen aus, die die konzentrischen Muster ausgleichen.
Ein besseres Architekturmodell sollte diese Klarheit und Differenzierung
natürlich erhalten. In einer Funktionshierarchie ohne funktionale Abhän-
gigkeiten ist das jedoch sehr leicht. API-Aufrufe gehören zur Logik und
LogikfindetsichnurinOperationen,alsoindenrotenFunktionseinheiten
im folgenden Bild; die Abhängigkeiten zum schwarzen “Fundament” aus
APIs findet sich nur dort.
Abbildung29:NurOperationenrufenexterneAPIsauf
Wie oben zugestanden, können zwar auch Datenklassen Logik enthalten,
doch die ist bewusst inhaltlich auf die Daten in den Strukturen begrenzt
und darf formal gerade keinen I/O bzw. spezielle API-Aufrufe enthalten.
Datenklassen sollen möglichst stabil sein, da von ihnen gewöhnlich viele
Funktionen abhängig sind. Logik ist dem abträglich, umso mehr, wenn sie
auch noch von APIs abhängig wäre.
Die Klasse Dataaccess in Abbildung 24 liefert zwei Beispiele für Operatio-
nen mit I/O-Logik.


---


<!-- Page 52 of 84 -->


2-DasIODAArchitekturmodell 48
Ein neues Architekturmuster
Nun ist alles beisammen für ein neues Architekturmuster, wie ich es mir
vorstelle, um den Ballast der bisherigen abzuwerfen. Ich nenne es die
IODAArchitektur wegenderdarinfundamentalunterschiedenenEbenen:
Abbildung30:DieEbenendesneuenArchitekturmusters
Bitte beachten Sie, dass es in diesem Architekturmuster zunächst keine
inhaltlichen Verantwortlichkeiten gibt. Auch darin unterscheidet es sich
vom Üblichen. Insofern beansprucht die IODA Architektur tatsächlich so-
gar Universalität: Ob Game oder CRM oder Buchhaltung, jeder Software
steht diese „Anatomie“ gut zu Gesicht, glaube ich.
Unterschieden werden zunächst lediglich formale Verantwortlichkeiten.
Integration hat einen ganz anderen Auftrag als Operation und Operation
hat einen ganz anderen Auftrag als Daten. Und APIs sind Ihrer Verfügung
ganz entzogen; Sie müssen sie nehmen, wie sie sind.
Diese Grundstruktur ist jedoch nur eine, wenn auch die vordringliche
Perspektive auf Software. Sie definiert, wie Code aufgebaut werden sollte,
unabhängig davon, was seine lösungsbezogene Aufgabe ist.
In dieser Perspektive geht es zunächst auch nur um Funktionen und
Datenstrukturen. Das halte ich aber für wichtig, weil damit deutlich in
den Blick genommen ist, was Software ausmacht: Logik, deren Verhalten
darin besteht, Daten zu transformieren.


---


<!-- Page 53 of 84 -->


2-DasIODAArchitekturmodell 49
Wenn ein Architekturmuster die zwei Seiten der Softwaremünze – Logik
und Daten – in seinem Bild nicht deutlich repräsentiert, dann glaube ich,
fehltetwas.DieIODAArchitekturtutdas.UndsiemachteineklareAussa-
gedarüber,wieLogikinFunktionenzuverpackenist,umVerständlichkeit
und Testbarkeit auf ein Mindestniveau zu heben.
Aber die IODA Architektur lässt die inhaltlichen Verantwortlichkeiten
nicht aus dem Blick. Orthogonal zu den Ebenen in Abbildung 30 gibt
es eine ebenfalls konzentrische Darstellung von Software (Abbildung 31).
Hier macht IODA eine Aussage zum Muster der Verantwortlichkeiten in
Anwendungen.
Abbildung31:DieinhaltlicheDimensionderIODAArchitektur
Zu unterscheiden ist zunächst das Softwaresystem von der Umwelt. Der
Code, den Sie schreiben, gehört zum Softwaresystem. Alles andere ist
Bestandteil der Umwelt. Angedeutet wird das durch die Kreislinie, die
Innen von Außen trennt.
Auf der Kreislinie angesiedelt sind Grundverantwortlichkeiten, die alle
zur Kategorie Adapter gehören. Sie kapseln insbesondere I/O-Logik, aber


---


<!-- Page 54 of 84 -->


2-DasIODAArchitekturmodell 50
auch andere API-Aufrufe. Adapter verbinden Innen mit Außen.
Anders als die Hexagonale Architektur teilt die IODA Architektur die
Adapter jedoch in zwei Gruppen: Portale und Provider.
• Durch Portale wird das Softwaresystem von der Umwelt gesteuert.
• Durch Provider greift das Softwaresystem auf Umweltressourcen
zu, von denen es abhängig ist.
Der Kontakt mit der Umwelt ist also asymmetrisch.
Benutzer triggern Logik über Portale, indem Sie dort Input-Daten anlie-
fern. Ebenso erhalten Benutzer über Portale Output-Daten zurück. Benut-
zer können Menschen sein oder andere Softwaresysteme.
Portale gibt es allerdings in zwei Ausprägungen: Controller und Dialo-
ge. Controller machen ein Softwaresystem über entry points zugänglich.
Main() ist ein solcher entry point, die Klasse Program also ein Controller.
Mittels Controller werden Softwaresysteme gestartet oder zumindest aus
einem inaktiven Zustand „geweckt“.²¹
Dialoge hingegen bieten weitere Trigger im Rahmen des Aufrufs über
einen entry point. Denken Sie an einen Button auf einem GUI-Fenster.
Das Fenster ist ein Dialog, der mehr oder weniger direkt innerhalb von
Main() geöffnet wurde. In Dialogen wartet Software aktiv auf einen Input
durch einen Benutzer.
Die Unterscheidung zwischen Portalen und Providern ist nützlich, weil
damit sprachlich das asymmetrische Verhältnis eines Softwaresystems zu
seiner Umwelt dokumentiert wird. Auf der einen Seite wird es von der
Umwelt vermittels APIs gesteuert, auf der anderen Seite steuert es selbst
die Umwelt vermittels APIs.
Die Unterscheidung zwischen Controllern und Dialogen wiederum ist
nützlich, weil damit sprachlich ihre Position in der IODA-Hierarchie do-
kumentiert wird. Controller als Module haben integrierende Funktion,
Dialoge als Module haben operierende Funktion.
Schließlich die Domain in der Mitte. Sie betont das, worum es eigentlich
geht: die Fachlichkeit. Die darum kreisenden Adapter können sich in Art
²¹Achtung:HierhatsichseitErstveröffentlichungderArtikeletwasverändert.ImKapitel
Update2020 erkläreichdieWeiterentwicklung.


---


<!-- Page 55 of 84 -->


2-DasIODAArchitekturmodell 51
und Zahl ständig ändern. Doch von der Domain ist anzunehmen, dass
sie davon recht wenig betroffen im Kern eines Softwaresystems ruht. Die
Adapter haben sogar die Aufgabe, das sicherzustellen. Sie bilden quasi
einen Schutzwall zwischen der Umwelt, zu der auch die zahllosen APIs
gehören; sie schaffen einen Innenraum, der in eigener Geschwindigkeit
evolvieren soll.
Aus dieser Perspektive betrachtet, ist Software ebenfalls in der IODA
Architektur in klare Verantwortlichkeiten geteilt:
• Adapter
– Portale
* Controller
* Dialoge
– Provider
• Domain
Das ist differenzierter als bei MVC oder Schichtenmodell oder auch der
Hexagonalen Architektur. Doch ich finde es immer noch sehr allgemein
und deshalb universell. Ob Twitter-Clone, Game oder Hausverwaltung:
diese Verantwortlichkeiten lassen sich immer finden.
Wie in der Clean Architecture ist auch bei IODA zu erwarten, dass äußere
Verantwortlichkeiten mehr Veränderungen unterliegen als innere.
Allerdings – und das ist der zentrale Unterschied zu allen anderen Archi-
tekturmodellen – stehen die Verantwortlichkeiten in keiner funktionalen
Abhängigkeit!
Es gibt keine Abhängigkeitspfeile, die nur von außen nach innen zeigen
dürfen.EinDialogbrauchtkeinenProvider,umseinenJobzumachen.Die
Domain ist von keinem Provider abhängig.
Nur durch diese funktionale Unabhängigkeit kann die Peripherie auch
wirklich ihrem Schutzauftrag nachkommen.
Verbunden werden die Verantwortlichkeiten vielmehr durch integrieren-
de Beziehungshierarchien – die „zufällig“ ihren Ausgang von den Con-
trollern nehmen. „Zufällig“ sage ich, weil das nicht Absicht des Modells
ist, sondern leider technische Notwendigkeit. Wenn ein entry point eines
Controllers getriggert wird, bedeutet das gewöhnlich eine Instanziierung


---


<!-- Page 56 of 84 -->


2-DasIODAArchitekturmodell 52
des Controllers. Vorher ist also kein Code gelaufen, der integrierend hätte
wirken können. An dieser Stelle ist das aber ein Detail, um das Sie sich
nicht sorgen sollten. Der Grundsatz bleibt: es gibt keine funktionalen
Abhängigkeiten.
Die IODA Architektur hat zwei Dimensionen, wobei die Hierarchie die
grundlegende ist (Abbildung 32). Sie ermöglicht, dass in der darüber
liegenden keine funktionalen Abhängigkeiten existieren.
Abbildung32:DiezweiEbenenderIODAArchitektur
InderIODAArchitekturistgetrennt,wasgetrenntseinmuss:formaleund
inhaltliche Verantwortlichkeiten. Die überkommenen Architekturmuster
vermischen hier – mit negativem Effekt für Verständlichkeit und Testbar-
keit.
Echt abstrakt
Die Hierarchie der Integration fügt der IODA Architektur noch einen
Aspekthinzu,derbeidenbisherigenModellenunberücksichtigtgeblieben
ist: Abstraktion.
Von Abstraktion ist zwar in DIP die Rede – eine Verantwortlichkeit soll
nicht direkt von einer anderen abhängig sein, sondern von einer “Abstrak-
tion” (Abbildung 9) –, doch diese Art der Abstraktion meine ich nicht.


---


<!-- Page 57 of 84 -->


2-DasIODAArchitekturmodell 53
Verwirrend, oder?
Um es zu verstehen, hier meine Sichtweise auf Abstraktion. Es gibt min-
destens zwei verschiedene Arten:
• Kategorisierung oder auch Aggregation: Verschiedene Elemente
werden auf Gemeinsamkeiten untersucht. Ist eine vorhanden, kön-
nen die Elemente unter dieser Gemeinsamkeit zusammengefasst
werden. Eine Kategorie wird gebildet. Beispiele dafür zeigt das
nächste Bild: Der Inhalt einer Haribo Colo-Rado Tüte wurde nach
verschiedenen Kriterien kategorisiert, z.B. Geschmack oder Form.
Abbildung33:AbstraktiondurchKategorisierung
• Komposition: Verschiedene Elemente werden zu einem Ganzen ver-
eint, eben weil sie verschieden sind. Im Verein stellen Sie auf höhe-
rerEbeneallerdingsetwasNeuesdar.AlsBeispieldafür:Zahnräder,
Schrauben, Zeiger, Feder ergeben zusammen ein Uhrwerk. Integra-
tion ist eine Form von Komposition.


---


<!-- Page 58 of 84 -->


2-DasIODAArchitekturmodell 54
Abbildung34:AbstraktiondurchKomposition
In der Softwareentwicklung findet wir beide Arten der Abstraktion. Der
Kategorisierung dienen Klassen und Interfaces. Diese Art der Abstraktion
wird bei DIP aufgerufen.
Kategorisierung ist natürlich nützlich. Sie schafft Überblick in der Vielfalt.
Aber Kategorisierung ist nicht funktional.
Komposition hingegen ist funktional. Das Neue, was aus der Komposition
entsteht, stellt auf höherer Ebene wieder ein nützliches Ganzes dar. Ent-
weder sind die darin eingegangenen Einzelteile allein nicht nützlich oder
es ist umständlich mit ihnen einen Zweck zu verfolgen. Die Komposition
jedoch verbirgt diese Details. Die Komposition vereinfacht, sie macht
produktiver.
Beispiel dafür sind die Integrationen in der IODA Architektur. Sie ziehen
Operationen (oder auch andere Integrationen) zu etwas funktional Größe-
rem zusammen. Integrationen bringen etwas auf den Punkt.
Abstraktion durch Komposition findet sich in den bisherigen Architek-
turmodellen nicht. Es ist ein Irrglaube, dass es bei den Schichten im
Schichtenmodell um Abstraktion ginge. Ebensowenig ist eine Entity im
KernderCleanArchitectureabstrakteralseinUseCaseodereinPresenter
in den Schalen drumherum.
Eine gewisse Abstraktion durch Kategorisierung enthalten die Architek-
turmodellejedoch,weildieBlöckebzw.SchalenmitihrenVerantwortlich-
keiten für eine größere Zahl von Modulen stehen, die demselben Zweck
dienen.


---


<!-- Page 59 of 84 -->


2-DasIODAArchitekturmodell 55
Aber wie gesagt: Auch wenn Kategorisierung die Verständlichkeit erhöht,
auf die Produktivität hat sie damit relativ geringen Einfluss. Ganz anders
die Komposition! Das beweist die Geschichte der Programmiersprachen.
Das beweist der Erfolg des OSI Modells²².²³ Das beweist die Entwicklung
von Frameworks. Eine Funktion wie File.ReadAllLines() ist dafür ein tri-
viales, dennoch passendes Beispiel. Die Produktivität unserer Branche ist
dramatisch gestiegen, weil wir Kompositionen zu neuen Kompositionen
vereint haben und so auf immer höhere Ebenen der Einfachheit durch
Abstraktion gestiegen sind.
Leider hat das in den Softwarearchitekturmustern bisher keinen Eingang
gefunden. Meine Vermutung ist deshalb, dass die sinkende Produktivität
innerhalbvonProjektenzumindestzumTeildaraufzurückzuführenist.Es
wird nicht systematisch nach Kompositionen als Abstraktionen gesucht,
um produktiver zu werden. Da wird zwar von Wiederverwendbarkeit
geredet – doch das Mittel Klasse ist dafür viel zu schwerfällig und die
vorzeitige Generalisierung lauert überall.
In der IODA Architektur hingegen ist Abstraktion durch Komposition
ganz einfach: Wo eine Funktion andere integriert, steht eine neue Kom-
position zur Verfügung, die produktiver macht, weil sie Details verbirgt
(vgl. dazu meinen Blog-Artikel „Stratified Design over Layered Design“²⁴).
Und sie tut das auch noch in einer Weise, die die Testbarkeit nicht kom-
promittiert.
Wenn eine Funktion eine andere kennt, dann dient das der Abstraktion
durch Komposition. Eine integrierende Funktion zieht darüber verschie-
dene Funktionen zusammen zu einem neuen, nützlichen und besser ver-
ständlichen Ganzen.
Es gibt sonst keinen Grund, warum eine Funktion eine andere aufrufen
sollte. Da ist IODA ganz strikt. Funktionen mit ganz verschiedenen Auf-
gaben,solleneinandernichtkennen.DasistaberderFallindenbisherigen
Architekturmodellen. Ob das mit zwischengeschobener kategorisierender
Abstraktion in Form eines Interface der Fall ist oder nicht, spielt dabei
keine Rolle.
²²https://en.wikipedia.org/wiki/OSI_model
²³Man könnte meinen, das OSI Modell mit seinen Schichten sei Vorbild für die Schich-
tenarchitektur. Immerhin kommt in beiden Bezeichnungen der Begriff “Schicht” vor. Doch
nichts könnte ferner der Wahrheit sein: OSI-Schichten sind Abstraktionen der jeweils dar-
unterliegenden,dieArchitekturschichtenjedochnicht.
²⁴http://ccd-school.de/2017/06/stratified-design-over-layered-design/


---


<!-- Page 60 of 84 -->


2-DasIODAArchitekturmodell 56
In einer IODA Architektur verlaufen Abhängigkeitspfeile also vom Abs-
trakten zum Konkreten, vom Ganzen zu den Teilen, von hohem zu niedri-
gem Kompositionsniveau (siehe dazu auch meinen Blog-Artikel “Depen-
dencies Flow Down Abstractions”²⁵). Das ist grundsätzlich anders als in
den bisherigen Architekturmustern.
Bisher sind Pfeile vom Einen zum Anderen verlaufen in Richtung der
Herstellung von Verhalten. Pfeile haben vor allem Verschiedenes auf dem-
selben Kompositionsniveau verbunden. Mit IODA ändert sich das. Dort
verlaufen Pfeile im Sinne von Funktionsaufrufen nicht zwischen Ver-
schiedenem, sondern zwischen Gleichem – nur liegt dieses Gleiche auf
unterschiedlichen Abstraktionsniveaus. Das ist wie beim OSI Modell.
²⁵https://ralfw.de/2018/07/dependencies-flow-down-abstractions/


---


<!-- Page 61 of 84 -->


3 - IODA am Beispiel
Nach einem so langen Ausflug in die Theorie nun zurück zur Praxis.
Sie fragen sich bestimmt, wie denn eine Architektur ohne funktionale
Abhängigkeiten überhaupt zu einem lauffähigen Programm führen kann.
In Abbildung 35 sehen Sie deshalb die Wortzählung in einer IODA Archi-
tektur.
Abbildung35:DieWortzählungstrukturiertnachIODAArchitekturmuster
In diesem Überblick sind einige Dinge hervorhebenswert als Kontraste
gegenüber der Clean Architecture:
• DieIODAArchitekturbetontdieNotwendigkeitderKapselungvon
APIs in Portalen und Providern. Deshalb habe ich hier erstmals den
ZugriffaufdenKommandozeilenparameterineineneigenenDialog
herausgezogen: Klasse Commandline; sie verbirgt den Umgang mit
dem„API“string[] args.ÜberdieKommandozeileteiltderBenutzer
der Anwendung etwas mit. Demgegenüber ist UI zuständig für die
Kommunikation mit dem Benutzer über Standard-Input/-Output.


---


<!-- Page 62 of 84 -->


3-IODAamBeispiel 58
• In einer IODA Architektur sind die Operationen verbunden durch
gemeinsame Daten (Abbildung 27). Sie legt damit nahe, sich dar-
über Gedanken zu machen und insbesondere die fließenden Daten
durch eigene Datentypen auszudrücken. Das habe ich mal exempla-
risch mit WordCountResult getan (vgl. Abbildung 28).
• Der Eintritt in Anwendungen geschieht immer über Controller.²⁶
Im Beispiel gibt es nur einen entry point, den ich in mit einer
gleichnamigen Klasse hervorgehoben habe. In bisherigen Architek-
turmodellen sind entry points kein Thema.
Vor allem erwähnenswert ist jedoch das, was fehlt. Haben Sie es bemerkt?
InAbbildung35gibteskeineInterfaces!DerCodenachIODAArchitektur
leidet nicht unter der zusätzlichen Komplexität, die das DIP erzeugt. Er
ist damit schon auf dieser Ebene viel verständlicher, wie ich finde. Er ist
weniger verrauscht. Sie müssen nicht überlegen, wie Abhängigkeiten zur
Compilezeit vs. Laufzeit verlaufen.
Das soll nicht bedeuten, dass das DIP keinen Platz in einer Anwendung
nach IODA Architektur hat. Obwohl es keine funktionalen Abhängig-
keiten gibt, können auch dort Tests hier und da von einer derartigen
Entkopplung profitieren – und zwar Tests von Integrationen.
In diesem Beispiel habe ich auf Interfaces aber ganz bewusst verzichtet,
um den grundsätzlich anderen Ansatz der IODA Architektur zu unter-
streichen.
Allerdings kommt IoC zum Einsatz. Bei Adaptern ist die Wahrscheinlich-
keit groß, dass sie einmal (z.B. in Tests) ersetzt werden müssen und also
ein Interface nützlich wäre. In Zukunft. Vielleicht.²⁷ Deshalb sind Adapter
auchkeinestatischenKlassenundveröffentlichenkeinestatischenMetho-
den. Und deshalb injiziere ich Instanzen von Adaptern in die Integration.
Damit sind Vorbereitungen getroffen für einen späteren Einsatz des DIP,
ohne den Code dadurch allzu sehr zu verrauschen. Relevant ist das hier
ohnehin nur für die Integration, also im Controller (Abbildung 36).
²⁶Zur Erinnerung: Hier hat sich etwas im Architekturmodell seit Erstveröffentlichung
geändert,siehedasKapitelUpdate2020.
²⁷Merke: Auch noch so gut gemeinte Interfaces und Injektionen können vorzeitige
Optimierungen darstellen! Sie können also zur “Wurzel allen Bösen” nach Donald Knuth
gehören.


---


<!-- Page 63 of 84 -->


3-IODAamBeispiel 59
Abbildung 36: Mit IoC wird die Integration auf einen späteren eventuellen Einsatz von DIP
behutsamvorbereitet
Die Abhängigkeit des Controllers von einem API besteht lediglich in der
statischenMethodenMain() mitdemargs Parameter.DieIntegrationsleis-
tung, die dieser entry point erbringt, besteht im Aufruf von Run(). Diese
Funktion repräsentiert auf höchster funktionaler Abstraktionsebene das
gesamte Verhalten der Anwendung. Konkret genutzt wird der args-API
ohnehin erst im Dialog Commandline.
Main() selbst muss nicht automatisiert getestet werden. Aber wenn ich
das Anwendungsverhalten automatisiert testen wollte, würde es mir über
die eine Funktion Run() zur Verfügung stehen. In einem Test müsste ich
den Konstruktor von Controller dann nur passend befüllen. Auch ohne
Attrappen ist diese Möglichkeit nicht zu verachten. Aber wenn ich z.B.
in einem Test keine Benutzerinteraktion über ein UI haben möchte, dann
könnte ich nachträglich und unmittelbar bedarfsgetrieben und ohne gro-
ßen Aufwand ein Interface IUI einführen. Die IODA Architektur erlaubt


---


<!-- Page 64 of 84 -->


3-IODAamBeispiel 60
mir, mit den Anforderungenzu wachsen. Sie dekretiertnicht von vornher-
ein,dassundwoichInterface-Abstraktioneneinziehenmuss.Komplexität
durch kategoriale Abstraktionen ist nicht gesetzt, nicht modellimmanent,
sondern richtet sich nach dem Bedarf.
Ein weiterer Unterschied der Implementation nach dem IODA Architek-
turmodell zeigt sich, wenn ich in die Klassen hineinzoome.
Da ist erstens der Controller, der gar keine Logik enthält (Abbildung 37).
Er ist abgesehen von Main() ausschließlich für die Integration zuständig.
EristgewissermaßeneineAbstraktionsmaschine.SeineMethodenkompo-
nierenausTeilenschrittweiseetwasUmfassenderes,Abstrakteres–dasan
der Spitze in Run() kulminiert.
Abbildung37:DieLeistungdesControllersbestehtvoralleminderIntegration
Wie gesagt, wäre das Problem umfänglicher, hätte ich diese Menge an
IntegrationineineeigeneKlasseausgelagert;dochfürdiesesBeispielfinde


---


<!-- Page 65 of 84 -->


3-IODAamBeispiel 61
ich die Co-Lokation mit dem entry point ok.
Dass ich so mit der Integration umgehe, ist andererseits auch wieder
dem IODA Architekturmodell geschuldet. Darin werden auf der grund-
legenden Ebene (Abbildung 32) die Funktionen betont. Sie stellen das
Verhalten her. Sie können IODA gewissermaßen als function-first oder
composition-first Ansatz verstehen, bei dem die Abstraktion durch Kom-
position im Vordergrund steht. Klasse/Module kommen für mich erst
im zweiten Schritt dazu, um in die Menge der Funktionen Ordnung zu
bringen: aggregation-second.
Wo die Funktionen in Klassen zusammengefasst werden (Abstraktion
durch Kategorisierung), ist dann natürlich nicht egal, aber zweitrangig.
Sollte die Anwendung wachsen, kann ich die integrierenden Methoden
aus Controller leicht in eine andere Klasse verschieben.
Um die Integration allerdings auch in Entscheidungsfällen logikfrei zu
halten, ist ein Trick nötig. In Abbildung 37 sehen Sie hervorgehobene
Passagen, wo ich den angewandt habe.
Im ersten Fall geht es um die Entscheidung, ob ein Text aus einer Datei
zu verarbeiten ist oder ein vom Benutzer einzugebender. Eine solche
Entscheidung erfordert Logik: eine Transformation als Bedingung plus
eine Kontrollanweisung. Damit darf eine Integration nicht „kontaminiert“
werden. Solche Logik muss in einer Operation stecken, damit sie testbar
ist.
Um dennoch ein alternatives Verhalten der Integration zu erhalten, wird
das Ergebnis der Entscheidung über continuations (Funktionszeiger) aus
der Operation herausgereicht (Abbildung 38). Je nachdem, ob die Verar-
beitung einer Datei (onFile) oder einer Benutzereingabe nötig ist (onUser),
wird die eine oder andere Methode aufgerufen.


---


<!-- Page 66 of 84 -->


3-IODAamBeispiel 62
Abbildung 38: Das Ergebnis einer Entscheidung gibt eine Operation über continuations
bekannt
Das ist für Sie sicher ungewohnt – aber es dient dem Grundsatz der IODA
Architektur: funktionale Abhängigkeiten sind zu vermeiden!
In diesem Fall mag das overengineert sein; dennoch will ich es einmal
grundsätzlich darstellen, um “zu beweisen”, dass eine Beschränkung von
Logik auf die Blätter des Kompositionsbaums immer möglich ist (für eine
differenziertere Sicht siehe meinen Blog-Artikel “Kontrollstrukturen in
der Integration”²⁸).
Das Prinzip hat also Vorrang vor der Implementation. Das ist nicht an-
ders als in der Clean Architecture. Dort führt es zu einem Anstieg der
Komplexität durch Interfaces. Hier führt es in manchen Fällen lediglich
zur Nutzung des ungewohnten programmiersprachlichen Mittels Funkti-
onszeiger.
BittelassenSieauseinemStirnrunzelnaufgrundmangelnderGewohnheit
hier jedoch nicht eine Abneigung gegen die IODA Architektur entstehen.
SeienSieversichert,dasseszusolchenKonstruktennichtinallenEntschei-
dungsfällen kommen muss. Ich habe es hier lediglich zur Unterstreichung
des Prinzips gewählt.
Es ist eine Sache der Übung, Code wie in Abbildung 37 zu lesen. Wenn
Sie das ein paar Mal getan haben, fällt es Ihnen leicht. Das ist zumindest
meine Erfahrung nach Jahren, in denen ich so gearbeitet und es in Clean
Code Development Trainings vermittelt habe.
²⁸https://ccd-school.de/2017/02/kontrollstrukturen-in-der-integration/


---


<!-- Page 67 of 84 -->


3-IODAamBeispiel 63
Auch DIP und IoC waren am Anfang ungewohnt in ihrer Manifestation
im Code. Heute gehen wir damit routiniert um – merken aber eben leider
nicht mehr, welcher Overhead dadurch entstehen kann.
Ebenso ist es mit continuations als Mittel, um Logik auf Operationen
zu beschränken: Wenn Sie heute damit anfangen, ist es morgen Routine.
Achtung: das ist allerdings kein Selbstzweck! Wichtiger als die Einhaltung
des Prinzips ist immer noch der eigentliche Zweck: Wandelbarkeit des
Codes durch Verständlichkeit und Testbarkeit zu erreichen. Falls ein Sprit-
zer Logik in einer Integration weder Verständlichkeit noch Testbarkeit
spürbar beeinträchtigt, ist die Logik dort verzeihlich. Doch das ist mir für
die hiesige Darstellung eigentlich schon zu differenziert. Deshalb habe ich
in der Beispielimplementation darauf verzichtet.
Struktur fraktal
Die Funktionshierarchie der IODA-Umsetzung folgt selbstverständlich
derHierarchieausAbbildung29:integrierendeFunktionenüberOperatio-
nen über Daten (Abbildung 39). Funktionen in grünen Kästen enthalten
keine Logik und haben ausgehende Pfeile, rufen also andere Funktionen
auf: Abhängigkeit ohne funktionale Abhängigkeit; das ist ein feiner, aber
sehr wichtiger Unterschied. Funktionen in roten Kästen als die Blätter
des Aufrufbaumes enthalten Logik, haben aber keine ausgehenden Pfeile.
Ganz einfach, ganz konsequent.


---


<!-- Page 68 of 84 -->


3-IODAamBeispiel 64
Abbildung39:DerFunktionsbaumnachIODAstrukturiert
Das Ergebnis ist extrem gute Testbarkeit, wo sie gebraucht wird: dort, wo
Logik steht, bei den Operationen. Außerdem: hohe Verständlichkeit durch
die Einhaltung des SLA in den Integrationen (vgl. Abbildung 37).
Doch nicht nur die Funktionshierarchie folgt dem IODA-Modell. Auch
die Klassen sind so strukturiert (Abbildung 40). Es gibt eine Klasse mit
der Verantwortlichkeit Integration, mehrere mit der Verantwortlichkeit
Operation und auch eine Datenklasse.


---


<!-- Page 69 of 84 -->


3-IODAamBeispiel 65
Abbildung40:AuchKlassenkönnendemIODA-Schemafolgen
Wenn Sie genau hinschauen, dann fällt ihnen jetzt allerdings vielleicht
eine Diskrepanz auf. Die Klasse Businesslogic ist ein Blatt im Klassendia-
gramm und also als operational eingestuft. Im Funktionsbaum sind hin-
gegen nicht alle ihre Methoden als Operationen eingetragen. Ihr Count_-
words() ist eine Integration (vgl. Abbildung 28). Wie kann das sein?
Das IODA Architekturmodell ist fraktal.
Es kann eine IODA-Hierarchie innerhalb einer IODA-Hierarchie existie-
ren (Abbildung 41).


---


<!-- Page 70 of 84 -->


3-IODAamBeispiel 66
Abbildung41:DasIODAArchitekturmodellistfraktal
Die Hierarchie aus Integration, Operation, Daten und APIs ist zwar zu-
nächst auf Funktionen gemünzt. Dort gilt es, aus der funktionalen Abhän-
gigkeit hinauszukommen.
Wenn Funktionen jedoch mit Modulen kategorisiert werden, d.h. nach
Zweck zusammengefasst werden, dann ergeben sich durch die Beziehun-
gen zwischen den Funktionen auch Beziehungen zwischen den Modulen.
Und Module bekommen einen Platz in einer Hierarchie, der von ihren
Funktionen abhängt.
Module, deren Integrationen keine Funktionen außerhalb des Moduls
aufrufen,sindinderModulhierarchiedannBlätter.Businesslogic istdafür
ein Beispiel. Intern jedoch können auch solche Module aus Integrationen
und Operationen bestehen.
Falls Module allerdings Integrationen enthalten, die Funktionen aus an-
deren nutzen, sind sie Knoten in der Modulhierarchie und werden als
integrierende Module gewertet – selbst wenn sie Operationen enthalten
sollten.
Ganz formal betrachtet mag das ein Widerspruch sein. Darf ein Modul
eine Integration sein, auch wenn es darin Operationen gibt? Wenn Sie
wollen, können Sie solche Module in einer Hierarchie kennzeichnen. Ich
tue das allerdings nicht. Wichtiger scheint mir, Augenmaß zu bewahren
und zu schauen, wie der Anteil von Integration zu Operation in solch ei-


---


<!-- Page 71 of 84 -->


3-IODAamBeispiel 67
nemHybridenist.WorumgehtesbeidemModul?IstderZweckintegrativ
oder operativ?
WennderSchwerpunktbeiintegrierendenFunktionenliegtundderZweck
integrativ ist, dann besteht kein Anlass zur Sorge. Wenn das jedoch nicht
der Fall ist, dann kann genau dieser hybride Charakter der Anlass sein,
so ein Modul zu refaktorisieren und die wirklich integrierenden Teile von
den operierenden zu trennen.
UndnocheinesistbeiderBusinesslogic hervorzuheben.SchauenSienoch
einmalbeiAbbildung28vorbei.FälltihnenbeidenFunktionenetwasauf?
Sie sind alle statisch.
Ich habe die Domänenlogik statisch gemacht, weil es schlicht keinen
Grund gibt, es nicht zu tun. In einer IODA Architektur ist das völlig
ok, ja sogar naheliegend. Hier werden keine Interfaces zwischen allen
möglichen Klassen gebraucht. Warum sollte ich also die Fachlogik mit
einem Interface ausstatten oder auch nur mit Instanzmethoden?
Instanzmethoden sind schlicht weniger testbar als statische Methoden.
Das vermeide ich, wo es geht. Und da es kein Signal für Instanzmethoden
gibt bei der Fachlogik – das wäre z.B. gemeinsamer Zustand oder API-
Aufrufe –, reichen mir statische Methoden völlig aus.
Das ist kein blinder Rückfall in ein Zeitalter prozeduraler Programmie-
rung, sondern eine bewusste Entscheidung basierend auf der Grundstruk-
tur, die Integration und Operation trennt. Sie folgt Prinzipien und einer
Systematik. Den Rahmen gibt die IODA Architektur vor. Den spannt sie
auf, um Verständlichkeit und Testbarkeit zu motivieren.
Zusammenfassung
Die Entwicklung der Architekturmuster von MVC über Schichtenmodell
bis zu Clean Architecture ist konsequent – aber ich halte sie nicht für
erschöpfend. Es muss weitergehen und es kann auch weitergehen. Etwas
ist mit ihnen besser geworden, doch zu viel liegt noch im Argen mit
der Sauberkeit von Code, selbst wenn diese Architekturmodelle tapfer
angewandt werden.


---


<!-- Page 72 of 84 -->


3-IODAamBeispiel 68
Das zentrale Problem der funktionalen Abhängigkeiten ist in ihnen nicht
wirklichgelöst.LediglichLinderungdurchDIP/IoCwurdegebracht–und
das zu einem hohen Preis. Komplexität wurde mit Komplexität bekämpft.
MitderIODAArchitekturhabeichIhnennuneineAlternativevorgestellt,
die das Problem an der Wurzel anpackt. Die Vorteile der Architekturmus-
terwerdenbeibehaltenundderzentraleNachteilverschwindet.Dabeient-
stehen zwei unerwartete positive Effekte: Daten werden plötzlich sichtbar
im Modell und Kompositionsabstraktionen entstehen ganz natürlich.
Nach all den Jahren in tiefen funktionalen Abhängigkeiten ist das IODA-
Denken natürlich eine gewaltige Umstellung. Doch meine Erfahrung ist:
sie lohnt sich. Und irgendwann fragen Sie sich dann, warum die Struktu-
rierung von Software Ihnen überhaupt einmal schwer gefallen ist und das
Testen Ihnen solche Mühe bereitet hat.


---


<!-- Page 73 of 84 -->


Update 2020
2015 habe ich das erste Mal versucht, die Clean Code Prinzipien IOSP und
PoMO²⁹ “auf Architekturniveau zu heben”. Das hat sich als konsequent,
machbar und sehr nützlich mit der IODA Architektur herausgestellt. Ich
möchte über Softwarearchitektur nicht mehr anders nachdenken.
Die vorgestellten bisherigen Sotfwarearchitekturmuster haben in der ge-
schichtlichen Entwicklung der Programmierung ihre Bedeutung - doch
für mich sind sie mit IODA weithin überholt. Sie sind verhaftet in einem
kontraproduktivenGlauben,dassfunktionaleAbhängigkeitenunvermeid-
bar sind.
Andere Muster wie z.B. in 10 Common Software Architectural Patterns in
a nutshell³⁰ vorgestellt, behalten ihre grundsätzliche Bedeutung, doch ich
empfehle, sie stehts durch die IODA-Brille zu betrachten. Oder genauer:
Sie auf die Konformität mit IOSP und PoMO hin abzuklopfen. Beispiele:
• Wo stecken im Master-Slave Pattern funktionale Abhängigkeiten?
Wie können die entschärft werden, ohne die Essenz des Patterns -
die Unterscheidung zwischen Master und Slaves - aufzugeben?
• Im Pipe-Filter Pattern stecken von vornherein keine funktionalen
Abhängigkeiten.Esstellteinen1-dimensionalenDatenflussdar,wie
ich ihn im Flow-Design empfehle.³¹
In den vergangenen fünf Jahren bin ich keinen Anforderungen begegnet,
derenBewältigungnichtvonderAnwendungderIODAArchitekturmehr
profitiert hätte, als von anderen Architekturmustern. Lösungen habe ich
²⁹Zu diesen Prinzipien siehe einerseits dasClean Code Development Wiki, andererseits
aber vor allem ausführlich mein Buch “Sofwareentwurf mit Flow-Design”. Im Buch ent-
wickle ich ausführlich beide Prinzipien, die der IODA Architektur zugrunde liegen, aus der
ursprünglichenObjektorientierung,wieAlanKaysie1968vorschwebte.
³⁰https://towardsdatascience.com/10-common-software-architectural-patterns-in-a-
nutshell-a0b47a1e9013
³¹Siehe dazu den Band “Softwareentwurf mit Flow-Design” aus meiner Programming
withEase Buchreihe.


---


<!-- Page 74 of 84 -->


Update2020 70
damitimmerzügigergefunden,ProblemebeianderenCodebasenhabeich
damit leichter diagnostizieren können.
Auch wenn sich eine konsequente IODA Architektur gerade in existieren-
den Codebasen nicht immer herstellen lässt, stellt sie eine enorme Hilfe
daralsNordstern.Esiststetsklar,welchemZielsicheineRefaktorisierung
annähern sollte.
Insofern ist meine Haltung zur IODA Architektur unverändert. Ich emp-
fehlesieunbedingt.DasMusteristsogrundlegend,dassderBeraterspruch
“Es kommt darauf an…” für mich nicht greift. Das Herauslösen von Inte-
gration als Funktionsbereich ist von zeitlosem und universellem Wert in
jederlei Softwaresystem. Ja, das mag etwas unbescheiden klingen, doch
ich meine es ganz praktisch: So ist schlicht meine Erfahrung. Ich habe
durch die IODA Architektur noch keine Begrenzung erfahren, sondern
stets nur Bereicherung und Ermöglichung.
Andererseits ist auch die IODA Architektur nicht stehengeblieben. Es gibt
zwei Bereiche, in denen jetzt etwas mehr Klarheit herrscht.
Logik frisch definiert
Softwareentwicklungdrehtsichzunächstdarum,dierichtigeLogikzufin-
den.LogikstelltdasVerhaltenher,dasderAuftraggebersichwünscht.Erst
wenn diese Logik bestimmte Mengen überschreitet, muss sie in spezieller
Weisegeordnetwerden.DasistdasThemaderModularisierung(Aggrega-
tion) und Architektur. Und nur wenn die Logik eine gewisse Komplexität
überschreitet,musssichingespeziellerWeisegeteilt(Dekomposition)und
dann wieder zusammengesetzt werden (Komposition), um testbar und
verständlich zu sein.
Die Schwellen für Aggregation und (De)Komposition sind natürlich viel
niedrigeralsmeistangenommen.EineexpliziteStrukturierungistdeshalb
unerlässlich (Entwurf).
Aberwasistdaseigentlich,dasdagefunden,geteiltundzusammengefasst
werden soll? Was ist Logik?
Die übliche Definition lautet:
• Ausdrücke/Operatoren


---


<!-- Page 75 of 84 -->


Update2020 71
• Kontrollstrukturen
• API-Calls, insb. I/O
Das folgende Listing zeigt davon viel “auf einem Haufen”:
Mit dieser Definition von Logik lässt sich ordentlich leben. Sie ist in der
Praxis brauchbar. Logik lässt sich damit leicht identifizieren.
Aber diese Definition ist bei wachsenden Codebasen zu konkret. Denn
damit zählt lediglich das als Logik, was eben schon an Operatoren, Kon-
trollstrukturen und API-Calls vorhanden ist. Nur 3rd Party Code kann als
Logik gewertet werden.


---


<!-- Page 76 of 84 -->


Update2020 72
So war der Begriff ursprünglich auch gedacht. Mit Logik sollten die Bau-
steine beschrieben werden, aus denen Operationen ihr Verhalten zusam-
mensetzen können. Logik ist das, was schwer richtig zu finden und richtig
hinzukriegen ist und deshalb auch sehr testwürdig ist.
Mit dieser Definition lässt sich die rekursive Struktur von Software bei
wachsender Codebasis allerdings nicht flexibel herstellen:
Das, was ganz rechts als grüner Integrationskasten die Wurzel darstellt,
könnte der rote Operationskasten ganz rechts in der mittleren Hierarchie
sein. Das Rote ist insofern gar nicht rot, sondern grün. So war Abbildung
41 ursprünglich gemeint.
Aber warum nicht auch die rote Operation eine Operation sein lassen und
die grüne Integration darin als Logik nutzen?


---


<!-- Page 77 of 84 -->


Update2020 73
DieintegrierendeWurzeleiner“tieferenHierarchie”mussnichtalsOpera-
tion einer “höheren Hierarchie” angesehen werden, sondern kann deren
Operation als Black Box dienen und genutzt werden wie ein 3rd Party
API-Call.
UmdiesezweiteInterpretationderSelbstähnlichkeitzuermöglichen,muss
Logik allerdings anders definiert werden. Praktikabel erscheint mir diese
Formulierung:
• Kontrollstrukturen
• Binär vorliegende Funktionen
Operatoren der Programmiersprache liegen nur binär vor und können als
Funktionenangesehenwerden.3rdPartyAPI-Funktionenliegenebenfalls
binär vor. Die bisherige Definition wird von der neuen also umschlossen.
Neu hinzu kommen nun jedoch auch alle anderen Funktionen, die ledig-
lich binär vorliegen. Dazu zähle ich ebenfalls Funktionen, die in einem


---


<!-- Page 78 of 84 -->


Update2020 74
SoftwareprojektimplementiertundnurüberPaketreferenzengenutztwer-
den.
Wer also seinen Code nicht nur in Bibliotheken, sonden sogar in Pakete
verpackt, der kann sich damit in der Logik auf höhere und höhere Ebenen
hocharbeiten. Das halte ich für konform mit dem Prinzip des Stratified
Design³².
Code in Pakete zu verpacken ist für mich ein genügend großer Aufwand,
umeinegewisseStabilitätzugewährleisten,dieLogikbraucht.IstLogikin
einem Paket verpackt und damit erratischen Veränderungen während des
Tagesgeschäftes entzogen, glaube ich daran, dass Logik als Produkt gese-
hen wird, das mit Sorgfalt hergestellt wird und zur “Wiederverwendung”
taugt.
Liegt Logik hingegen lediglich verpackt in einer Funktion in einer Klasse
als Quellcode vor und wird in dieser Form über eine Codebasis genutzt,
finde ich die Lage prekär. So lässt sich keine “hausgemachte” Logik her-
stellen. Auch die Verpackung in eine Bibliothek ist mir zu wenig: In
Visual Studio ist die nur ein Projekt vom nutzenden in derselben Solution
entfernt. Dass ein binärer Bezug herrscht, ist nicht zu spüren. Für ein
Paket jedoch ist mehr Aufwand zu treiben. Das wird wahrlich nur binär
genutzt und muss speziell publiziert werden. Da steckt Aufwand drin; das
dämpftdieVeränderungsgeschwindigkeitundistdernötigenStabilitätfür
Wiederverwendung und somit Logik zuträglich.³³
Integrationen konsequent benannt
DiegrundsätzlicheStrukturinderIODAArchitekturistweiterhinkorrekt:
Es gibt keine funktionalen Abhängigkeiten zwischen den Funktionsberei-
chen Kern/Domäne und Peripherie mit Portalen und Providern als Ad-
apter. Die Verbindung zwischen diesen “Arbeitspferden” stellen spezielle
Integrationen her.
Das geschieht prinzipiell auf beliebig vielen Ebenen. Allerdings haben
sich zwei als Muster herausgebildet, die ich nun konkret benannt habe.
³²https://ccd-school.de/2017/06/stratified-design-over-layered-design/
³³DassdieVerwendungeigenerbinärerFunktionenalsLogikundsolchervon3rdParties
und von Kontrollstrukturen in einer Operation dann evtl. schneller zu einem Widerspruch
mit dem SLA führen kann, will ich hier nur anmerken. Darauf muss man ein Auge haben.
DasIOSPistebennichtdaseinzigezubeobachtendePrinzip.


---


<!-- Page 79 of 84 -->


Update2020 75
Damit verschiebt sich auch etwas bei den Portalen, was mir länger Kopf-
zerbrechen bereitet hatte. Da war etwas inkonsistent, holprig. Nun aber
empfinde ich das Gesamtbild als stimmiger.
Der schematische, grobe Prozess der Verhaltensproduktion als Datenfluss
sieht so aus:
Über ein Portal werden Eingaben aus der Umwelt empfangen, dazu wer-
den Daten über einen Provider aus einer Ressource beschafft, alles zu-
sammen wird von der Domäne verarbeitet, dabei fallen Daten an, die
in eine Ressource gehören und am Ende wird das Ergebnis der Umwelt
präsentiert.
Kein Funktionsbereich kennt in diesem Prozess andere; jede konsumiert
und produziert Daten unabhängig.
Interactor
Damit die unabhängigen Funktionsbereiche in einem Datenfluss zusam-
menspielen, müssen sie mindestens einmal integriert werden.
Diese Integration nenne ich nun ganz konkret Interactor. Der Interactor
sorgt für die Funktion von Software im Rahmen einer Interaktion. Er


---


<!-- Page 80 of 84 -->


Update2020 76
verdrahtet vom Portal über die Domäne und die Provider alles. Der In-
teractor stellt den Prozess her, der auf einen Reiz durch den Anwender
reagiert.EingabedatenwerdenlinksimBildvomPortalgesammelt;diesen
Anteil des Portals nenne ich Collector. Die Eingabedaten werden unter
Verwendung von Ressourcen in Ausgabedaten transformiert. Und rechts
im Bild werden die dann vom Portal dem Anwender präsentiert; diesen
Anteil des Portals nenne ich Projector.
Die Aufgabe des Interactors ist es, die Interaktion mit der Software zu er-
möglichen. Dazu muss er je Interaktion die Portal-Anteile “mit dem Rest”
integrieren. Deshalb ist der Interactor nur schwer automatisiert testbar.
Benutzerschnittstellen widersetzen sich solchen Versuchen notorisch; da
muss man schon sehr spezielles Testgeschütz auffahren. Das macht keine
Freude.
Deshalb,abernichtnurdeshalb,isteinezweiteIntegrationsebenesinnvoll:
Processor
Der Processor integriert alles zwischen den Portalen, also Domäne und
Provider. Er grenzt das Visuelle, die konkrete Interaktion mit der Umwelt
aus. Das, was übrig bleibt, ist dann prinzipiell viel leichter automatisiert
testbar.
Am Processor setzen aus meiner Sicht Akzeptanztests an. Die Funktionen


---


<!-- Page 81 of 84 -->


Update2020 77
des Processors sind deshalb das Ergebnis der Anforderungsanalyse.³⁴
Der Processor ist für mich das Herzstück in der IODA Architektur. Er
repräsentiert das Softwareverhalten ohne die Details der Benutzerschnitt-
stelle.ImIdealfall könntederselbeProcessormitalldem, waserintegriert,
einfach nur mit einer neuen Benutzerschnittstelle von einem anderen
Interactor integriert werden, um auf anderen Geräten zugänglich zu sein.
Damit zeichnet sich auch eine klare Arbeitsteilung ab, finde ich. Das
was “im Processor geschieht” kann getrennt vom einklammernden Portal
realisiert werden. Sobald die Processor-Schnittstelle klar ist, kann darin
wiederum parallel gearbeitet werden. Konsument und Produzent des Pro-
cessors und dessen, was davon integriert wird, sind unabhängig.
Bei geeigneter Gestaltung der Interaktions- bzw. Nachrichtengranularität
ist das auch eine Sollbruchstelle für eine simple Verteilung von Anwen-
dungsteilen: Der Kopf mit den Portalen und der Körper mit Processor,
ProvidernundDomänekönnenaufunterschiedlichenThreadsoderinver-
schiedenen Prozessen gehostet werden. Ich nenne das die Sleepy Hollow
Architecture³⁵.
Interactor-Varianten
Soweit grundsätzlich die nun konkretere Hierarchie der Integrationen in
der IODA Architektur. Dass es eine “Integration für alles” geben muss,
war ja immer klar. Nun hat sie einen Namen. Wie darin jedoch noch eine
innere Integration eingezogen werden könnte, war zunächst nicht klar.
Ein konsequenter test-first Ansatz bei der Codierung hat das jedoch ir-
gendwann klar gemacht. Es gab schlicht einen Bedarf für einen Processor.
Nach dieser Differenzierung blieb allerdings noch eine Erklärungslücke:
Der Interactor war ganz plausibel und einfach aufzusetzen bei Desktop-
Anwendungen. Dort heißt er für mich Application.
Aber wie ist es bei Web-Anwendungen, z.B. REST-Servern? In den Ar-
tikeln sind deren Controller noch den Portalen zugeschlagen.³⁶ Das hat
³⁴Ausführlich dazu im Band Software Anforderungsanalyse mit Slicing meiner Pro-
grammingwithEase Buchreihe.
³⁵https://ralfw.de/2019/05/sleepy-hollow-architecture-no-application-should-be-
without-it/
³⁶siehez.B.Teil2“EinneuesArchitekturmuster”


---


<!-- Page 82 of 84 -->


Update2020 78
sich inzwischen verändert. Ich finde es viel plausibler, Controller als eine
zweite Variante des Interactors neben der Application zu sehen.
Controller sind keine Portale; ihre Aufgabe ist nicht die Operation. Viel-
mehr sind sie Integrationen! Das hatte ich schon länger erkannt, aber es
standfürmichimWiderspruchdazu,dasssiedochauchNachrichtenvom
Anwender/Client empfangen.
Jetzt habe ich damit meinen Frieden gemacht, indem ich Controller zu
IntegrationenaufderInteractor-Ebeneerhobenhabe.Unddortintegrieren
sie ebenfalls einen Collector- und einen Projector-Anteil eines Portals.
Die wesentlichen Unterschiede zwischen Application und Controller:
• Die Application wird im Code explizit einmalig instanziiert. Ein
Controller hingegen wird von einer Infrastruktur bei Bedarf instan-
ziiert.
• Das Portal in einer Application wird von der Application angesto-
ßen, auf Benutzereingaben zu warten. Beim Controller liegt die
Benutzereingabe schon an, wenn er aufgerufen wird. Darin ist der
Collector nur noch ggf. für ihr Mapping oder die Validation zustän-
dig. Der Projector am Ende des Interaktionsprozesses hingegen ist
auch dort oft recht aktiv und rendert z.B. einen HTML-Response.
Aber es kann auch sehr dünn sein, weil die Infrastruktur die Seria-
lisierung einer Ergebnisdatenstruktur übernimmt.
Interessanterweise habe ich im Beispiel in Teil 3 schon die Interactor-
Klasse Controller genannt.³⁷ Aber in der Gliederung in Teil 2 taucht der
Controller noch neben Dialog im Portal auf.³⁸ Das ist die Inkonsistenz, die
mich länger umgetrieben hat. Nun ist sie aber aufgelöst.
ControllersindnurInteractorsundkeinePortale.Vielmehrintegrierensie
Portale.
Reflexion
Software unterliegt einer Evolution. Prinzipien und Architekturmuster
unterliegen ebenfalls einer Evolution. Zu glauben, dass irgendetwas in
³⁷sieheAbbildung40
³⁸sieheGliederunginTeil2“EinneuesArchitekturmuster”


---


<!-- Page 83 of 84 -->


Update2020 79
der Softwareentwicklung letztendgültig sei, ist naiv. Technologien und
Konzepte haben eine begrenzte Nützlichkeitsdauer. Je grundlegender sie
sind, desto länger ist die natürlich.
Das bedeutet nicht, dass das Alte durch das andere Neue ersetzt wird.
Vielmehr erweitert das Neue das Alte. Das Alte wird assimiliert. Und
natürlich kommt es immer auf den Kontext an. Das Alte wurde in einem
gewissen Kontext entwickelt. Wo der besteht, hat das Alte womöglich
auchnochseineGültigkeit.DochwennderKontexteinanderergeworden
ist… dann kann sich das Alte als sperrig bis untauglich herausstellen. Das
Alte muss dann durch etwas Neues ersetzt werden.
In den 1970ern gab es eine bestimmte Form von Benutzerschnittstellen,
vor deren Hintergrund das MVC-Architekturmuster Sinn machte. In den
1990ern änderte sich das und MVC wurde durch das Schichtenmodell
abgelöst - bis es später im Web wieder zu neuen Ehren gelangte.
Das Schichtenmodell-Architekturmuster hatte seine Zeit - bis es durch
den Auftritt von Testautomatisierungstools erweitert werden musste, um
schließlich sogar durch andere Architekturmuster abgelöst zu werden, die
unter dem Einfluss von Domain Driven Design entstanden.
Alles ist im Fluss. Und dabei zeigt sich, was darunter liegend ruht. Es gibt
auch Konstanten - im positiven wie im negativen Sinn. Das SRP hat sich
als positive Konstante herauskristallisiert; richtig verstanden halte ich es
für ein ganz wichtiges Prinzip.
FunktionaleAbhängigkeitenhabensichalsnegativeKonstanteherauskris-
tallisiert. Das Leiden an ihnen konnten auch weiterentwickelte Architek-
turmuster im Verein mit Prinzipien nicht wirklich lindern. Dort setzt die
IODA Architektur an. Sie erlaubt sich, bisherige Muster nicht als final
anzusehen, sondern macht einen Vorschlag, wie darüber hinaus gegangen
werden kann.
Ich glaube, damit ist ein sehr wesentlicher Schritt getan. Die Herausarbei-
tung von Integration als eigenständige formale Verantwortlichkeit, die es
vonanderenzutrennengilt,istimSinnedesSRPlangeüberfälliggewesen.
Begünstigt mag diese Erkenntnis durch die Funktionale Programmierung
oder Entwicklungen in der Kommunikation in verteilten Anwendungen
sein.SobefruchtensichebenganzunterschiedlicheBereichederSoftware-
entwicklung oder empfangen Impulse aus anderen Disziplinen. Alan Kay


---


<!-- Page 84 of 84 -->


Update2020 80
als “Vater der Objektorientierung” hat es vorgemacht mit seiner Analogie
der biologischen Zellen, denen er Objekte angelehnt hat.
Ist mit der IODA Architektur dann nun das Ende der Architekturmuster-
entwicklung erreicht? Das glaube ich nicht. Aber ich kann noch nicht dar-
über hinaus sehen. Schlimm ist das nicht. Irgendwann wird es vielleicht
wieder einen Bedarf durch einen veränderten Kontext geben, der zu einer
Evolution anregt.