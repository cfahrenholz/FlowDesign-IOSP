<!-- Page 1 of 13 -->


PLANUNG Sleepy Hollow
SLEEPY-HOLLOW-ARCHITEKTUR, TEIL 3
Endspurt
Das Finale ist erreicht! Und es zeigt: Slicing, IODA und Sleepy Hollow erweisen sich gerade
in der Kombination als ideal, um Agilität und Clean Code einen Boost zu verleihen.
Steht der Entwurf erst einmal, siehe [1] und [2], ist die ment); sie definieren die Ziellinie, die erreicht werden muss.
Implementation eigentlich langweilig. Das war wieder Wenn sie grün sind, ist der Body „reif“ für eine Auslieferung.
einmal meine Erfahrung bei der Umsetzung dieses Projekts. Akzeptanztests sind High-Level-Integrationstests. Sie kön-
Welche Puzzleteile gebraucht werden, war klar. Sie mussten nen deshalb nicht detailliert sein; ihre Pfadabdeckung ist ge-
„nur“ noch generiert und zusammengesteckt werden. Das ring. Sie sollen aber auch nicht prüfen, ob an jede Eventuali-
war mit ChatGPT als Helfer
simpel.
Zur Erinnerung das Szenario
in Kurzform: Eine Anwendung
soll helfen, Aufwände in Pro-
jekten zu schätzen. Schätzun-
gen sollen durch alle Teammit-
glieder getrennt vorgenommen
und dann zu einer Gesamt-
schätzung verrechnet werden.
Schätzungen sind jedoch nicht
absolut (zum Beispiel „Issue X
schätze ich auf 8 SP“), sondern
relativ (zum Beispiel „Issue Y
wird aufwendiger als X“ – ach-
ten Sie auf den Komparativ!).
Ein PO legt eine Sitzung mit zu
schätzenden Issues an. Dann
ordnen die Teammitglieder (die
Crowd) jedes für sich die Issues
in der Reihenfolge absteigen-
der Aufwände. Schließlich zeigt
die Anwendung dem PO die
„durchschnittliche“ Gesamt-
ordnung der Issues.
Die Anforderungsanalyse mit Grobstruktur des Softwaresystems mit drei Workern (Bild 1)
Slicing hatte dafür eine grobe
Struktur ergeben, bestehend
aus zwei Applikationen mit drei Workern, siehe Bild 1. Darin tät gedacht ist, sondern ob alle Module korrekt miteinander
finden die Interaktionen der Rollen PO und Crowd in den je- verbunden sind.
weiligen Applikationen über insgesamt fünf Entry-Point- Gerade auf der Ebene der Akzeptanztests lasse ich deshalb
Funktionen statt. In Bild 2 sind diese in Interfaces zusammen- gern Szenarios ablaufen, die mehrere Entry Points und wo-
gefasst, die gemäß dem Sleepy-Hollow-Architekturmuster möglich sogar mehrere Prozessoren überspannen. Sie sollen
„Prozessoren“ genannt werden. Diese Prozessoren sind die eine realistische Bedienung des Softwaresystems simulieren.
Module in der Sleepy-Hollow-Architektur, die die eigentliche In dieser Bedienung fehlt vor allem der Head, die Benut-
Verhaltensherstellung durch den Body verbergen. Dort kön- zerschnittstelle. Provider, das heißt Ressourcenzugriffe, sind
nen Akzeptanztests angesetzt werden, die unabhängig von allerdings nur von Fall zu Fall durch Surrogate ersetzt;
allen UI-Technologien sind (Bild 3). eigentlich möchte ich Akzeptanztests so nah an der Realität
Und sobald die Akzeptanztests stehen, kann mit der Imple- wie möglich. Als Beispiel ein Testszenario, in dem beide Pro-
mentation des Bodys begonnen werden (Test-First Develop- zessoren aus Bild 2 auf den Prüfstand kommen: ▶
www.dotnetpro.de 1.2025 35
003355--004477__SSlleeeeppyyHHoollllooww__1133__SSeeiitteenn__eeaa..iinndddd 3355 2266..1111..2244 1144::4444


---


<!-- Page 2 of 13 -->


PLANUNG Sleepy Hollow
Plan versus Realität
Neue Sitzung publizieren.
• Starten ohne SessionID. So weit der Stand nach dem vorangegangenen Artikel. Ihn
• Publizieren einer Session mit der Beschreibung „B“ hatte ich nach mehreren Wochen Pause als Ausgangspunkt
und den Einträgen „X“, „Y“, „Z“. Es wird eine Ses- für diesen Artikel vorgefunden. Das habe ich als unmittelbar
sionID geliefert. angenehm empfunden. Nach wenigen Minuten hatte ich
• Aktualisieren der Session in der Erwartung, dass die wieder einen Überblick und wusste, was zu tun ist, um das
Einträge „X“, „Y“, „Z“ in der Reihenfolge geliefert Softwaresystem zu implementieren. Ein Architekturmuster
werden. im Hinterkopf zu haben, eine Architektur zu sehen, die dem
Sitzung individuell das erste Mal ordnen. Muster folgt, und diese Architektur auch noch visualisiert zu
• Starten mit einer SessionID. Es werden Beschreibung haben, ist sehr hilfreich. Darin liegt alles buchstäblich vor mir
„B“ und die Einträge [{0, „X“}, {1, „Y“}, {2, „Z“}] ge- ausgebreitet, was dann reihum „abzuarbeiten“ ist. Das ist wie
liefert. eine Checkliste, in der ich Modul für Modul abhaken kann.
• Einreichen der individuellen Ordnung [2,1,0]. Als Erstes habe ich mir einen Plan für die Implementierung
Sitzung individuell das erste Mal durch einen weiteren Cli- gemacht (Bild 4). Der war sehr simpel in Form und Inhalt. Es
ent ordnen lassen. ging darin auch nicht um Präzision und Letztendgültigkeit,
• Starten mit einer SessionID. Es werden Beschreibung sondern um eine erste Fokussierung meiner Gedanken. Da-
„B“ und die Einträge [{0, „X“}, {1, „Y“}, {2, „Z“}] ge- mit habe ich mich auf die Aufgabe eingeschwungen. Dass ich
liefert. ihn einhalten würde, war nicht beabsichtigt, auch wenn das
• Einreichen der individuellen Ordnung [0, 2, 1]. angesichts seines hohen Abstraktionsniveaus nicht so schwer
Starten einer existierenden Sitzung und Aktualisieren nach gewesen wäre. Wie das Sprichwort sagt: „Der Plan ist nichts,
individuellen Ordnungen. die Planung ist alles.“ Er verliert schnell in der Hitze der Im-
• Starten mit SessionID; es werden Beschreibung „B“ plementierung seine Gültigkeit – und dennoch fühle ich mich
und die Einträge „X“, „Y“, „Z“ geliefert. durch ihn unterstützt. Er ist mir ein Handlauf, an den ich je-
• Aktualisieren der Session. Die Erwartung ist, dass sich derzeit zurückkommen kann, wenn ich mich unsicher fühle.
die Ordnung gegenüber der ursprünglichen verändert „Was ist als Nächstes dran? Ach ja, jetzt Phase X, Punkt Y.“
hat. Sie soll nun „Z“, „X“, „Y“ lauten. Und wenn ich mich nicht unsicher fühle, dann mache ich
einfach ohne Plan weiter. Auch die Architektur ist ja ein Plan,
Stichwort Checkliste. Fertig bin ich, wenn alle Module imple-
mentiert und getestet sind.
Insofern ist der Plan wirklich vor allem während des Schrei-
bens eine Hilfe „zum Einschwingen“ auf die Aufgabe. Seine
Form (hier: Textdatei) ist für mich unwichtig. Ich will einfach
nur reibungslos meine Gedanken notieren und einmal vor mir
sehen können.
Die Realität sah selbstverständlich anders aus. Weil ich al-
les mit ChatGPT in einem Chat umgesetzt habe, gibt es so-
gar eine Chronologie der Ereignisse. GitHub-Commit-Mes-
sages dokumentieren nur, was man erinnert, das getan wur-
de. Wenn man denn irgendwann mal den Code eincheckt.
Wenn man drandenkt, ausführliche Commit-Messages zu
schreiben.
Im Chat mit der KI hingegen sehe ich nicht nur Ergebnis-
se, sondern Intentionen und Friktionen. Sie liefern mir eine
Dokumentation meiner Entscheidungen und sogar solcher
der KI (Bild 5). Im Chat kann ich „den Hergang der Ereignis-
se“ verfolgen und über meine Irrungen und Wirrungen re-
flektieren. Er ist ein Dokument für Deliberate Practice [3] und
gehört zusammen mit dem Code ins Repository.
Ich ziehe deshalb auch immer noch das „Pair Program-
ming“ mit ChatGPT dem Einsatz von KI in meiner IDE vor. Es
ist zwar bequemer, die KI direkt am Code, am Kontext zu ha-
ben; ihren Einsatz verweigere ich nicht. Doch der Wechsel
zwischen ChatGPT oder Claude und IDE inklusive Kopieren
von Code, Dokumentation meines Gedanken- und Imple-
mentationsflusses und der Möglichkeit, Kontexte mit neuen
Die Entry Points des Softwaresystems auf ihren Sleey-Hollow- Chats auch immer wieder neu zu gestalten, ohne sie zu ver-
Prozessor-Interfaces (Bild 2) lieren, fühlt sich derzeit noch vorteilhaft an.
36 1.2025 www.dotnetpro.de
003355--004477__SSlleeeeppyyHHoollllooww__1133__SSeeiitteenn__eeaa..iinndddd 3366 2266..1111..2244 1144::4444


---


<!-- Page 3 of 13 -->


PLANUNG Sleepy Hollow
2. A nforderungen präzise und mehr
oder weniger in Beispielen formu-
lieren (Testfälle).
3. S chnittstellen aus den Anforde-
rungen ableiten als Ansatzpunkte
für die Testfälle.
Das sind meine NI-Leistungen, be-
vor ich KI-Leistungen in Anspruch
nehmen kann. KI ist sehr gut in der
Umsetzung gut formulierter Anfor-
derungen von begrenztem Scope.
Sie nimmt mir nervige und fehler-
trächtige Detailarbeit ab. Dafür
muss ich jedoch Vorarbeit leisten.
Requirements-First Development
bedeutet, dass ich bewältigbare An-
Sleepy-Hollow-Architektur des forderungshorizonte abstecke:
Softwaresystems (Bild 3) Die Anforderungen dürfen nur so
umfangreich sein, dass ich sie hin-
reichend präzise formulieren kann.
Vielleicht ändere ich meine Meinung, wenn die Integratio- Mir müssen beispielhafte Paare von (Input, erwartetem
nen noch besser werden (die Cursor-IDE macht schon mehr Output), also Beispiele für die Anforderungen, klar sein, be-
Spaß als frühere Ansätze) oder KI-Agentensysteme wie De- ziehungsweise sie müssen für die KI ableitbar sein.
vin mir erlauben, weniger kleinschrittig vorzugehen. Einst- Die Umsetzung muss skizzierbar sein, beziehungsweise die
weilen aber bleibe ich bei meinem hybriden Vorgehen. KI muss sie aus den Aufgaben und Regeln selbst ableiten
können.
Test-First auf 10 000 Meter Flughöhe
Natürlich habe ich meinen Plan am Anfang noch eingehal- Angesichts meiner menschlichen Neigung zu Unvollständig-
ten. Ich habe mit den Prozessoren und ihren Akzeptanztests keit, Unklarheit und Unrichtigkeit bin ich recht bescheiden,
begonnen. ChatGPT hat mir nach Vorlage der Interfaces und was den Scope angeht, für den ich die KI um Umsetzung bit-
der simplen Aufforderung „Ich brauche eine öffentliche Klas- te. Doppelt bescheiden bin ich, wenn ich in Anschlag bringe,
se, die das Interface implementiert“ lauffähigen Code für bei- wie unbewusst, unverständig, unterwürfig und unausgewo-
de Klassen mit Dummydaten generiert. gen generative KI immer noch ist. Wir beide sind kein idea-
Anschließend habe ich um die Implementation des obigen les Paar für die Programmierung, wo es auf Passgenauigkeit,
Akzeptanztest-Szenarios unter Nutzung dieser Klassen ge- Präzision und Korrektheit ankommt. Aber mit etwas Metho-
beten. Die Beschreibung habe ich eins zu eins in den Chat de klappt es doch: ▶
gesetzt (Bild 6). Das Ergebnis war lauffähiger Testcode.
Natürlich hat ChatGPT davon profitiert, dass ich das Sze-
nario schon recht formal beschrieben habe. Aber ich musste
mich keiner Spezialsprache bedienen; meine Formulierun-
gen sind auch für einen PO verständlich.
Damit war das grundsätzliche Paar (Test, Implementie-
rung) vorhanden. Und auch wenn ich den Test als Zweites ha-
be generieren lassen, nenne ich es Test-First Development.
Die zu testenden Funktionen haben ja noch keinen realen In-
halt; sie sind lediglich formal korrekt. Sobald ich sie also aus-
fülle, sagt mir der schon vorhandene Test, ob ich auf dem rich-
tigen Weg bin.
Test-First Development im Rahmen von Requirements-
First Development: Denn die Tests sind das Ergebnis eines
ausführlichen Anforderungsanalyseprozesses (Slicing). Auf
ihn muss ich mich vor allem konzentrieren, wenn ich von KI
bei der Implementation profitieren will.
1. Anforderungen verstehen und vollständig definieren. Da-
mit meine ich die Aufgaben, die der Code erledigen soll,
und die Regeln, denen er folgen soll. Ein erster grober Plan für die Umsetzung (Bild 4)
www.dotnetpro.de 1.2025 37
003355--004477__SSlleeeeppyyHHoollllooww__1133__SSeeiitteenn__eeaa..iinndddd 3377 2266..1111..2244 1144::4444


---


<!-- Page 4 of 13 -->


PLANUNG Sleepy Hollow
Prompt für die Generierung des Akzeptanztests (Bild 6)
Für das Management der ClientID sind zwei Implementationen vorteilhaft;
eine Dummy-Variante für Tests macht es möglich, verschiedene Clients im
selben Prozess zu starten (Bild 7)
Kleinschrittiges Vorgehen ist zwingend. Endlich! Inkre-
mentell iterativ kommen wir zusammen ans Ziel.
Clean Code ist zwingend. Endlich! Wenn ich sauber ent-
werfe, das heißt modularisiere (Prinzipien dafür sind zum
Beispiel SRP, SoC, OCP, DIP/IoC), und Test-first arbeite,
kann ich mir und der KI vertrauen, auch wenn ich den Code
überwiegend nicht selbst geschrieben habe.
Generative KI ist die Killerapplikation für Agilität und vor al-
Der komplette lem Clean Code Development. Wer sich bisher um beides he-
Chat mit Chat- rumgedrückt hat, kommt daran nicht mehr vorbei, wenn er
GPT für die Im- mit KI produktiver werden will.
plementation Zurück zum Code: ChatGPT ist folgsam, denkt aber nicht
des Entwurfs selbst mit. Deshalb enthält der Test noch eine Lücke, die mir
(Bild 5) schon bei der ersten Formulierung im vorherigen Artikel auf-
38 1.2025 www.dotnetpro.de
003355--004477__SSlleeeeppyyHHoollllooww__1133__SSeeiitteenn__eeaa..iinndddd 3388 2266..1111..2244 1144::4444


| Prompt
Für das
eine Du
selben
Der komplette
Chat mit Chat-
GPT für die Im-
plementation
des Entwurfs
(Bild 5) |  |  |
| --- | --- | --- |



|  |  |
| --- | --- |



---


<!-- Page 5 of 13 -->


PLANUNG Sleepy Hollow
und dem standen lauffähige
Implementationen der Pro-
zessoren gegenüber. Der
Body des Softwaresystems
war zu erkennen und auf
dem Prüfstand. Jetzt ging es
darum, ihn mit Leben zu fül-
len – ein Modul nach dem
anderen (Bild 8).
Das Repository
In Bild 8 sind die Provider für
Sitzungen und für Ordnun-
gen von deren Items durch
die Teammitglieder ge-
Konkrete Reihenfolge der trennt. Bei der Umsetzung
Implementation der Module im Body: Die Realität jenseits des Plans (Bild 8) kam mir das zu kleinteilig
vor; deshalb habe ich die
Zugriffsfunktionen für bei-
gefallen war: Es findet keine explizite Identifikation der Be- de in einem Repository-Interface zusammenfassen lassen.
teiligten statt. In Bild 3 ist zwar ein ClientID-Provider zu sehen, Aber wie bin ich zu diesem Interface gekommen? Ich habe
doch der kommt im Testszenario nicht explizit vor. Es wird „Flow-Design für Arme“ betrieben (Bild 9):
schlicht angenommen, dass die Sitzung der zu ordnenden Für jede Entry-Point-Funktion in den Prozessoren habe ich
Items von einem anderen Client angelegt wird als denen, die mir überlegt, welche Schritte nacheinander ausgeführt ▶
sie anschließend ordnen.
Was in der natürlichsprachlichen Formulie-
rung des Testszenarios noch durchging, muss
spätestens im Testcode eindeutig und konkret
gemacht werden. Wie sollen sich PO, Teammit-
glied 1 und Teammitglied 2 unterscheiden? Sie
laufen im Test alle im selben Prozess im selben
Verzeichnis. Eine Unterscheidung, wie ultimativ
geplant durch lokale Speicherung einer einma-
lig generierten ClientID, ist nicht konfliktfrei
möglich. Hier bin ich erstmalig vom Plan abge-
wichen. Ich musste dafür eine Lösung finden.
Als erste Idee habe ich den Prozessoren einen
Konstruktur mitgeben lassen, dem ich eine Cli-
entID übergebe. Aber das war natürlich Mist. Es
widersprach dem Entwurf, in dem ja schon ein
Provider dafür vorgesehen war. Doch erst etwas
später habe ich das geradegezogen und eine
Dummy-Implementation eines UserManage-
ment-Interface übergeben, das die ClientID
nicht aus einem lokalen persistenten Speicher
liest, sondern in-Memory hält (Bild 7).
Die Konstruktoren, die zuerst eine ClientID di-
rekt und später eine IUserManagement-Imple-
mentation akzeptieren, habe ich generieren las-
sen. Doch die Injektion im Test habe ich von
Hand angepasst. Es schien mir schneller und un-
gefährlicher, als den ganzen Akzeptanztest neu
generieren zu lassen. Das ist einer der wenigen
manuellen Eingriffe in den Code.
Auf dieser hohen Flughöhe war damit die An-
wendung „fertig“. Das Big Picture war in einem Phase 2 des Plans, Entwurf der Prozesse hinter den Entry Points mit
Akzeptanztest formal ausführbar beschrieben, „Flow-Design für Arme“ (Bild 9)
www.dotnetpro.de 1.2025 39
003355--004477__SSlleeeeppyyHHoollllooww__1133__SSeeiitteenn__eeaa..iinndddd 3399 2266..1111..2244 1144::4444


---


<!-- Page 6 of 13 -->


PLANUNG Sleepy Hollow
auf unterschiedlichen Abstraktionsniveaus über
der Logik liegen. Es entsteht eine Hierarchie von
Domain Specific Languages (DSL). Das wird auch
Stratified Design genannt [7].
Genau betrachtet, habe ich hier sogar Phase 2
und 3 meines Plans vermischt. Vertikal sehen Sie
den Entwurf der Datenflüsse, der Verarbeitungs-
prozesse gemäß Phase 2. Horizontal habe ich dazu
allerdings schon Module beigefügt. In den Daten-
flüssen benutze ich Kürzel, die ich erst später in ei-
ner Legende ausschreibe.
Diese Notation macht mich sehr schnell. Zwar ist
der Entwurf nicht visuell, doch das Datenflusspara-
digma ist so simpel und bewusst so eingeschränkt,
dass viele Verarbeitungsprozesse sich textuell ohne
Aufwand und auch übersichtlich beschreiben las-
sen. Mit einem Texteditor bin ich flink in der Ände-
Aus der Datenflussbeschreibung der Entry Points abgeleitete Interfaces für rung, wenn mir etwas nicht gefallen sollte.
Provider und Domänenlogik (Bild 10) Falls mir der Sinn danach steht, unterstützt mich
ChatGPT auch bei einer Visualisierung. Bild 11 zeigt
ein simples Mermaid-Diagramm, das ich aus der
werden müssen. Die habe ich nicht gezeichnet, wie im Skizze für POProc.update() in Bild 9 und der Interfacedefini-
Flow-Design [4] sonst üblich, sondern schlicht untereinan- tion habe generieren lassen. Mit etwas mehr Mühe werden
der notiert. Meine freiwillige Selbstbeschränkung dabei: die Darstellungen auch hübscher. Probieren Sie einfach ver-
Ich benutze keine Kontrollstrukturen. schiedene GPTs aus; es gibt viele für UML und BPMN. Der
Und dann habe ich die Schritte mit Modulnamen annotiert. umgekehrte Weg funktioniert übrigens auch: Sie können ei-
Das folgt auch im visuellen Flow-Design erst nach der De- nen Datenfluss oder ein Strukturdiagramm zeichnen und
finition des Datenflusses, also des Verarbeitungsprozesses. ChatGPT zur Übersetzung in Text geben; dieser kann natür-
Funktionen sind primär für die Verhaltenserzeugung, Mo- lichsprachlich das Diagramm beschreiben oder eine pro-
dule sekundär. Erst muss ich mir klar darüber sein, was pas- grammiersprachliche Umsetzung sein. Ich wähle mal den ei-
sieren soll, dann darüber, wer dafür verantwortlich sein soll. nen, mal den anderen Weg, je nachdem, wie umfangreich
oder schwierig die Entwurfslage ist. „Zum Beweis“ in Bild 12
Im Kontext des Chats war diese verbale Skizze völlig ausrei-
chend, damit ChatGPT sinnige Interfaces ableiten konnte
(Bild 10). Dass ich nicht hundertprozentig chronologisch be-
richte, wie der Hergang der Entwicklung war, können Sie da-
ran ablesen, dass erst hier das Interface für das Management
der ClientIDs auftaucht, obwohl ich es oben bei den Akzep-
tanztests schon erwähnt habe. Mein Plan war mit der Reali-
tät kollidiert. Für die Darstellung hier erlaube ich mir jedoch,
die Dinge etwas zu glätten, um Ihnen zu erleichtern, der Ent-
wicklung zu folgen.
Die Prozessoren sind Integrationen gemäß dem Integration
Operation Segregation Principle (IOSP) [5], das der IODA-Ar-
chitektur zugrunde liegt [6], auf der wiederum das Sleepy-
Hollow-Architekturmuster aufbaut. In Integrationen kommt
keine Logik vor; es werden nur Funktionen meiner eigenen
Codebasis aufgerufen (und es wird mit Datenstrukturen um-
gegangen). Theoretisch und erst einmal jedenfalls. Für die
Generierung der Interfaces kommt mir das zugute, denn Nachträgliche
dank dieser Reduktion ist das, was in einem Entry Point pas- Visualisierung
sieren soll, häufig durch eine simple Liste von Schritten be- eines Datenflusses:
schreibbar, in der jeder von ihnen nur einen Funktionsaufruf ChatGPT hat das
darstellt. Durch das IOSP werde ich angeleitet, mir selbst eine Diagramm nach dem
„Programmiersprache“ zu definieren, die aus für mich be- textuellen Entwurf
quemen Funktionen besteht. Oder genauer: Ich werde sogar als Mermaid-Code
ermuntert, mehrere „Programmiersprachen“ zu erfinden, die generiert (Bild 11)
40 1.2025 www.dotnetpro.de
003355--004477__SSlleeeeppyyHHoollllooww__1133__SSeeiitteenn__eeaa..iinndddd 4400 2266..1111..2244 1144::4455


---


<!-- Page 7 of 13 -->


PLANUNG Sleepy Hollow
Aus einem visu-
ellen Entwurf
generierter Code
für Interfaces und
Implementation
der Funktion,
d eren Datenfluss
er darstellt
(Bild 12)
der Datenfluss für POProc.update() jetzt zuerst als Diagramm, Das war jedoch eher ein Nebeneffekt. Ich war sogar ein
aus dem ChatGPT Interfaces und die Implementation der In- bisschen überrascht über diese Umsicht von ChatGPT. So war
tegration in der Methode ableitet. nun sogar schon Phase 4 meines Plans angerissen. Statt strikt
Nicht nur hat ChatGPT nach meiner Aufforderung in Bild 9 „bottom-up“ vorzugehen, gab es schon eine Implementation
Interfaces generiert, es hat auch sofort die Implementation „at the top“. Aber warum nicht?
der Prozessoren angepasst! Die waren im Kontext noch vor- An einer Stelle blieb ChatGPT dabei allerdings hinter mei-
handen und ChatGPT hat korrekt erkannt, dass meine Skiz- nen Erwartungen zurück. Meine Formulierung zum Laden al-
ze den vorhandenen Dummy-Code „überschreibt“. Dabei ler Ordnungen hat die KI in eine Schleife mit fest verdrahte-
wird folgerichtig zum Beispiel in update() auf die in start() ge- ten ClientIDs übersetzt (Bild 14). Statt einer speziellen Funk-
ladene Session zugegriffen (Bild 13). tion auf dem Repository wurde Logik generiert. So hatte ich
mir das nicht gedacht.
Da musste ich „nachprompten“ und explizit um eine
Funktion nach meinem Geschmack bitten. Anschlie-
ßend musste auch noch der PO-Prozessor aktualisiert
werden, damit er die Funktion tatsächlich nutzt. Daran
hatte ChatGPT nicht gedacht; aus seiner Sicht war dort
update() ja okay.
Bevor die Implementation des Repositorys dran war,
habe ich einen Abstecher zur SessionID gemacht, die
ich einfach halten wollte. Bisher war ich mit irgendei-
nem einzigartigen String zufrieden. Angesichts der Im-
plementation des PO-Prozessors, die überraschend
aufgetaucht war, stand mir jedoch der Sinn danach,
hier kurz nachzubessern. Eine GUID kann sich ja nie-
mand merken. Stattdessen habe ich mir eine zuf ällige
sechsstellige Buchstaben-Zahlen-Kombination wie
„ABC123“ gewünscht. Dass es dabei Kollisonen gibt,
ist nicht auszuschließen, aber genügend unwahr-
scheinlich.
Im generierten Code passt alles zusammen, auch über Funktions- Danach war das IRepository-Interface dran. Ich habe
grenzen hinweg (Bild 13) nur knapp beschrieben, dass ich mir die Persistenz ▶
www.dotnetpro.de 1.2025 41
003355--004477__SSlleeeeppyyHHoollllooww__1133__SSeeiitteenn__eeaa..iinndddd 4411 2266..1111..2244 1144::4455


---


<!-- Page 8 of 13 -->


PLANUNG Sleepy Hollow
bisschen nervig, ist durch einen eigenen, auf
Type script für Deno zugeschnittenen GPT auch
besser geworden. Nur manchmal stolpert
ChatGPT noch.
Die Domänenlogik
Die Domänenlogik war als Nächstes dran. Die
Provider für die Persistenz und die ClientIDs
waren implementiert. Nun konnte ich mich dem
Kern des Softwaresystems widmen.
Nein, so muss es nicht sein. Gerade weil ich
nach IOSP/IODA implementiere und explizit
ChatGPT hat mich missverstanden (Bild 14) entwerfe, ist die Implementationsreihenfolge
weitgehend egal. Ich muss nicht durch Schich-
ten von unten nach oben implementieren, um
in JSON-Dateien mit einem bestimmten Namensschema vor- Unabhängiges vor Abhängigem zu realisieren. Wenn ich wei-
stelle – und ChatGPT hat mir eine Implementation inklusive ter oben von „bottom-up“ gesprochen habe, dann meine ich
Tests geschrieben. Bild 15 zeigt meinen Prompt und einen vor allem, zuerst alle Operationen und ihre Klassen zu reali-
Ausschnitt aus dem generierten Code. Gut hat mir bei den sieren. In Operationen steckt Logik, sie müssen eng getestet
Tests gefallen, dass sie nicht nur funktional sind, sondern werden. Das sind die Grundbausteine des Softwaresystems.
auch aufräumen. Sie stellen sicher, dass mit reinem Tisch be- Sie bilden die DSL mit der niedrigsten Abstraktionsstufe. Auf
gonnen und geendet wird. ihnen baut alles andere auf.
Da die Funktionen des Repositorys komplementär sind – sie Durch diese Brille betrachtet sind Repository, UserManage-
schreiben und lesen –, kommen die Tests auch ohne Code- ment und DomainLogic auf Augenhöhe. Sie kennen sich
dopplungen aus. In ihnen selbst muss nicht auch noch Persis- nicht, sind nicht voneinander abhängig. Ich kann sie also in
tenzcode stehen. beliebiger Reihenfolge implementieren.
Ich habe Typescript für die Implementation benutzt. Dafür Erst dort, wo sie integriert werden – hier: in den Prozesso-
favorisiere ich die Deno Runtime. Leider hat ChatGPT (mehr ren –, sollten sie (oder zumindest Surrogate) zuerst vorhan-
als Claude) immer mal wieder Schwierigkeiten, dafür die den sein, damit die Codierung der Integrationen nicht in Lü-
richtigen Funktionen für den Dateizugriff zu importieren. cken läuft. Wie die Prozessoren gezeigt haben, sind das zwar
Deshalb musste ich noch zweimal „nachprompten“, um für keine Lücken zur Übersetzungszeit, weil alle Operationen
alle Operationen die passenden Bibliotheksfunktionen an dort über Interfaces schon bekannt sind. Einen grünen Ak-
den Start zu bringen. Aber ich kenne das schon … Es ist ein zeptanztest gibt es dennoch bisher nicht.
ChatGPT generiert Productions mit zugehörigen
Tests (Bild 15)
42 1.2025 www.dotnetpro.de
003355--004477__SSlleeeeppyyHHoollllooww__1133__SSeeiitteenn__eeaa..iinndddd 4422 2266..1111..2244 1144::4455


---


<!-- Page 9 of 13 -->


PLANUNG Sleepy Hollow
immer nach der Codierung aus der Erinnerung he-
raus geschrieben. Auch hier fehlte fast immer die
entscheidende Information: „Wie bin ich eigentlich
auf diesen Code gekommen?“ Mit KI bekommen
wir nun einen Einblick in bisher Verborgenes. Ich
glaube, das ist eine sehr gute Sache, die vor allem
nichts extra kostet.
Bild 17 zeigt die Domänenlogik mit einem Aus-
schnitt aus den Tests. Die waren viel umfangreicher
als ihr Testsubjekt. Allerdings fehlte ein Sonderfall:
Was ist, wenn es noch keine Ordnungen gibt, die
verrechnet werden könnten? Für den Fall musste ich
„nachprompten“, für die Domänenlogik und einen
zugehörigen Test. Ich denke allerdings, das hätte
ich vermeiden können, wenn ich in meinem ersten
Prompt „strenger“ gewesen wäre und aufgefordert
hätte, gleich auf Edge Cases zu achten.
Im Prompt habe ich mir bewusst keine Gedanken
Die KI gestattet intentionale Programmierung (Bild 16) darüber gemacht, wie wohl eine Implementation ▶
Beim Prompt für die Domänenlogik fällt auf, dass
anders als vorher das Interface den kleinsten Teil
ausmacht. Vor allem erkläre ich im Prompt, was die
Domänenlogik tun soll. Das formuliere ich jedoch
nicht imperativ, sondern intentional. Ich beschrei-
be Effekte und unterlege sie mit Beispieldaten
(Bild 16). Ich mache das Was klar – das Wie überlas-
se ich der KI. Wie sie das skizzierte Verhalten algo-
rithmisch mit Logik herstellt, will ich mir ja gerade
nicht überlegen. Dafür habe ich die KI als „Junior
Programmer“; sie soll mir diese lästige Detailarbeit
abnehmen. Ich konzentriere mich darauf, dass es
diese Funktion gibt, dass sie etwas Bestimmtes in
einem größeren Rahmen leistet.
Intentionale Programmierung wie hier gezeigt ist
informell. Kontrollstrukturen sind selten oder sehr
umgangssprachlich. Auch die Reihenfolge der Dar-
stellung ist recht frei. Ich profitiere mehr von klarer
Gliederung als die KI, würde ich sagen. Vor allem
wenn ich den Chat mit der KI aufzeichne und da-
mit eine Dokumenta tion parallel zum Code gene-
riere, lohnt sich jedoch ein bisschen Mühe bei der
Formulierung. Mir scheint, dass hier durch das not-
wendig textuelle, oft natürlichsprachliche Promp-
ten der KI erstmalig in der Geschichte der Soft- Die Domänenlogik mit einigen Testfällen (Bild 17)
wareentwicklung erstens Dokumentation freiwillig
geschrieben wird und zweitens diese Dokumenta-
tion sogar Informationen enthält, die früher nie do-
kumentiert wurden. Neu ist nämlich die Beschrei-
bung von Anforderungen vor der Codegenerierung
in realistischer Weise.
Spezifikationen wurden bisher zwar vor der Co-
dierung geschrieben, doch sie dienten nicht unmit-
telbar der Codierung, sondern wurden vorher noch Die Struktur des
von Entwicklern übersetzt. Kommentare im Code Workers, der das Repository
oder andere Dokumentation andererseits wurden als Service anbietet (Bild 18)
www.dotnetpro.de 1.2025 43
003355--004477__SSlleeeeppyyHHoollllooww__1133__SSeeiitteenn__eeaa..iinndddd 4433 2266..1111..2244 1144::4455


---


<!-- Page 10 of 13 -->


PLANUNG Sleepy Hollow
aussehen könnte. Ich war dazu versucht –
doch ich habe der Versuchung widerstan-
den. Die KI sollte mich überraschen. Das
Ergebnis hat mich gefreut. Über eine Map
zu gehen und deren Inhalt am Ende zu sor-
tieren, finde ich leicht verständlich.
Akzeptanztest grün
Wenn ich mich richtig erinnere, waren die
Akzeptanztests nach Implementation der
Domänenlogik tatsächlich grün. Das Chat-
Protokoll enthält dazu keine direkte Infor-
mationen. Aber wenn ich mir anschaue,
wie es danach weitergeht, sehe ich keine
Prompts, die noch etwas in den Providern
oder der Domänenlogik oder den Prozes-
soren als Integrationen geradeziehen.
Damit war die grundsätzliche Idee für
die Lösung des Problems der relativen
Schätzung validiert. Ein realistisches Sze-
nario lief fehlerfrei durch. Nur die Client-
IDs kamen noch nicht aus einer Datei. Ich
würde also sagen: Zeit zum Feiern! Ausschnitte aus dem HTTP-Kontrakt für den Repository-Service und der Provider-
Implementation, die Clients zur Kommunikation mit ihm benutzen (Bild 19)
Ein Repository-Service
Nach dem Akzeptanztest ist vor dem Ein-
satz. Dafür waren Worker nötig, also eigenständige Prozesse. Provider ist trivial, weil er je Interface-Methode nur einen
Den Anfang sollte das Backend machen, ein Server für das simplen fetch-Aufruf kapselt.
Repository.
Das Repository selbst gab es schon ge-
testet. Nun musste es noch in einem Ser-
vice gehostet werden. Dafür war Folgen-
des nötig (Bild 18):
Ein Controller, der Endpunkte für die In-
terface-Methoden des Repositorys an-
bietet.
Der Server, der den Controller zugäng-
lich macht und einen Prozess für den
Service aufspannt.
Ein Provider, der aussieht wie ein Repo-
sitory, aber in Wirklichkeit die Endpunk-
te des Service aufruft.
Provider und Controller sind ein Modul-
Paar. Der Kontrakt zwischen ihnen besteht
in HTTP-Aufrufen über bestimmte Adres-
sen mit bestimmten Parametern und Pay-
loads. Für die Implementation von Server
und Controller habe ich mir das Frame-
work Oak gewünscht, das oft mit Deno
eingesetzt wird.
Zunächst habe ich ChatGPT gebeten,
Vorschläge für Endpunkte auf Basis des
IRepository-Interfaces zu machen. Das Er-
gebnis hat mir gut gefallen; also habe ich
gleich einen Provider dafür schreiben las-
sen, ein RemoteRepository (Bild 19). Dieser Auschnitt aus dem Oak-basierten Controller/Server (Bild 20)
44 1.2025 www.dotnetpro.de
003355--004477__SSlleeeeppyyHHoollllooww__1133__SSeeiitteenn__eeaa..iinndddd 4444 2266..1111..2244 1144::4455


---


<!-- Page 11 of 13 -->


PLANUNG Sleepy Hollow
Herausfordernder ha-
be ich mir die Implemen-
tation des Controllers/
Servers vorgestellt. Doch
wie Bild 20 zeigt, war das
ebenfalls eine Kleinig-
keit. Nur der Zugriff auf
die JSON-Payload eines
Requests hat einen Mo-
ment lang Pro bleme ge-
macht. Bis ich auf con-
text.request.body.json()
statt context.request.bo-
dy({ type: ”json” }).value
gekommen bin, haben
wir ein paar Runden dre-
hen müssen. Bei so ei-
nem Framework, das ich
nicht gut kenne, frage
ich lieber ChatGPT, be-
vor ich selbst darin rum-
stochere. Doch am Ende Die Frontend-Worker greifen auf den Repository-Worker zu, um Daten gemeinsam zu speichern (Bild 21)
wusste es Intellisense
besser als ChatGPT.
Die Client-Worker
Um den Server zu testen, habe ich mir CURL-Testfälle ge-
nerieren lassen, die ich nach Insomnia übertragen habe. Da- Mit laufendem Repository-Service war ich auf der Zielgera-
bei ging es wieder nicht darum, festzustellen, ob die Opera- den. Jetzt waren nur noch die Frontends übrig, das heißt die
tionen im Repository funktionieren, sondern ob die Integra- Worker, mit denen User interagieren (Bild 21).
tion korrekt ist und das Oak-Framework korrekt benutzt Für die Frontends war im Grunde aber nur noch das UI zu
wird. Diese Tests müssen also nicht ständig automatisch aus- generieren. Die Prozessoren waren schon fertig und getestet.
geführt werden. Ich erwarte nicht, dass sich am Controller be- Es blieb nur die Frage: Wie sieht das jeweilige UI konkret aus,
ziehungsweise dem Protokoll immer wieder etwas ändert. und wie werden daraus die Prozessoren aufgerufen? Laut
Auf separate Tests für das RemoteRepository habe ich ver- Sleepy-Hollow-Architekturmuster wäre es ideal, wenn die
zichtet. Seine Implementation habe ich durch Inaugenschein- Struktur wie in Bild 22 aussähe: Das UI ist ein sauberes Ope-
nahme geprüft; sie ist ja trivial. Wenn es dort einen Fehler rationsmodul auf Augenhöhe mit Providern und Domänenlo-
gibt, stelle ich das auch schnell fest, weil dann die Integrat ion gik. Auf diese Weise ließe es sich sogar gegen ein Prozessor-
mit dem Service scheitert. Surrogat testen. ▶
Ideale Frontend- Etwas unsaubere
Architektur (Bild 22) reale Frontend-
Architektur. Das
UI ist abhängig vom
Prozessor (Bild 23)
www.dotnetpro.de 1.2025 45
003355--004477__SSlleeeeppyyHHoollllooww__1133__SSeeiitteenn__eeaa..iinndddd 4455 2266..1111..2244 1144::4455


---


<!-- Page 12 of 13 -->


PLANUNG Sleepy Hollow
Doch ich will gestehen, ich war schwach. Ich
wollte schneller ein Ergebnis sehen. Deshalb habe
ich mich für eine Abkürzung entschieden (Bild 23).
Hier ist das UI ein Hybrid gemäß IOSP: Es enthält
Logik und ruft gleichzeitig den Prozessor auf. Nicht
ganz sauber – aber bei dieser Größenordnung auch
nicht so schlimm, finde ich. Mir schwebte nicht vor,
das UI noch einmal separat zu testen – ich wollte
gleich voll mit der Nutzung loslegen.
Ich empfinde das hier als lässliche Sünde, weil
die Schnittstelle des Prozessors überschaubar und
fixiert ist. Durch Slicing war klar, wie sie aussehen
musste. Ich kaschiere sie jetzt nur noch mit einer
dünnen Schicht Benutzerschnittstelle. Dafür habe
ich wieder intentional gepromptet (Bild 24). Ganz
einfach wollte ich es halten:
Entweder es wird eine neue Session gestartet.
Oder eine existierende Session wird beobachtet.
Der Kommandozeilenparameter stellt den Modus
ein. Das ist noch simpler, als ich am Ende des Sli-
cings gedacht hatte. Es bleibt natürlich bei einem Intentionaler Prompt für das UI des PO (Bild 24)
Konsolen-UI. Bild 25 zeigt es in
Aktion:
Rechts läuft der Repository-
Service und protokolliert, wie
er aufgerufen wurde.
Links wird der PO-Client
zweimal gestartet: Beim ers-
ten Mal ohne SessionID, um
eine neue Session anzulegen.
Beim zweiten Mal mit der ID
der vorher publizierten Sessi-
on, um die aktuelle Gesamt-
ordnung anzuzeigen – in die-
Der PO-Client in Aktion (Bild 25) sem Fall ist seit der Publika-
tion noch keine Ordnung aus
der Crowd eingereicht wor-
den. Für ein Update der Ge-
samtordnungsanzeige startet
der PO den Client einfach ein
weiteres Mal.
Das main-Modul des PO-Front-
ends wurde mit dem Prompt in
Bild 24 in einem Rutsch gene-
riert. Da musste ich nichts
„nachprompten“. In meinem
Typescript-GPT ist hinterlegt,
dass für Interaktionen das CLI-
Framework Cliffy benutzt wer-
den soll. Damit kann Input ganz
leicht sowohl von der Komman-
dozeile als auch von der Kon-
UI-Handler für den Fall, dass keine SessionID auf der Kommandozeile angegeben wurde (Bild 26) sole gelesen werden.
46 1.2025 www.dotnetpro.de
003355--004477__SSlleeeeppyyHHoollllooww__1133__SSeeiitteenn__eeaa..iinndddd 4466 2266..1111..2244 1144::4455


---


<!-- Page 13 of 13 -->


PLANUNG Sleepy Hollow
schon vorhanden. Controller
und RemoteRepository-Provi-
der waren quasi nur Formsa-
che; ChatGPT hat es mir leicht
gemacht, diesen Boilerplate-
Code zu schreiben.
Mit ChatGPT bekommt mei-
ne frühere Einsicht „Ist der Ent-
Der Crowd-Client in wurf erst mal gemacht, ist die
Aktion (Bild 27) Implementation langweilig“
noch einmal neue Bedeutung.
Sie bleibt in weiten Teilen lang-
weilig, doch weil ChatGPT viel
Bild 26 zeigt Ihnen, wie die UI-Logik, die vom Cliffy-Frame- Arbeit abnimmt, ist es nicht so schlimm. Nerviger Kleinkram
work abhängig ist, einen Aufruf beim Prozessor umpolstert. wird von ChatGPT generiert. Und ChatGPT macht diese Pha-
Aber die UI-Logik ist so geradlinig, dass ich darin kein Pro- se zu einem weniger einsamen Geschäft, weil ich dabei „mit
blem gesehen habe. jemandem rede“. In dieser Weise dialogisch zu entwickeln ist
Mein Prompt für das Crowd-Frontend war genauso inten- eine qualitative Veränderung der Programmierung, finde ich.
tional. Allerdings habe ich dort einen technischen Kniff ein- Das macht Spaß, es erleichtert mich. Ich fühle mich nie allein
gebaut: Wenn der Client mit dem Parameter --clientID ge- gelassen. Vor allem kann ich mich auf das Wesentliche kon-
startet wird, kann eine ClientID angegeben werden, sodass zentrieren. Das ist der Zweck, die Absicht hinter einer Soft-
keine in einer Datei gespeichert wird. So lassen sich mehre- ware. Was ist intendiert? Das kann ich vielfach genau so
re Clients bei Test im selben Verzeichnis starten. Fehlt der Pa- weitergeben. Lediglich den Scope muss ich meiner Unvoll-
rameter, wird der persistente UserManager benutzt. kommenheit bei der Formulierung von Anforderungen und
Bild 27 zeigt den Crowd-Client in Aktion mit dem Reposito- ChatGPTs begrenzter „Intelligenz“ und seinen Kontextkennt-
ry-Service. Hervorhebenswert ist hier nur, wie auf der Konso- nissen anpassen.
le die Ordnung verändert wird. Dafür habe ich eine simple Agilität und Clean Code bekommen einen Boost. Slicing,
Syntax gewählt, bei der zuerst die Positionsnummer des zu IODA und Sleepy Hollow sind für gerade in dieser Konstella-
„verschiebenden“ Items und dann die des „Zielitems“ ge- tion der Zusammenarbeit extrem hilfreich. ◾
nannt wird. Das „Quellitem“ drückt das „Zielitem“ nach oben.
Das ist mein „Drag-and-drop für Arme“. Mit einem Web-UI [1] Ralf Westphal, Den Kopf vom Körper trennen,
würde das natürlich schöner funktionieren – und es würde den dotnetpro 11/2024, Seite 46 ff.,
Prozessor nicht beeinflussen. Es ist eine Sache rein des UI. www.dotnetpro.de/A2411SleepyHollow
[2] Ralf Westphal, Ich packe meinen Koffer …,
Fertig!
dotnetpro 12/2024, Seite 30 ff.,
Nach 100 Seiten Chat mit ChatGPT war das Softwaresystem www.dotnetpro.de/A2412SleepyHollow
implementiert. Das hört sich viel und langwierig an, war es [3] The Ultimate Deliberate Practice Guide: How to Be the
aber nicht. Ich habe in mehreren Sitzungen über ein paar Ta- Best, www.dotnetpro.de/SL2501SleepyHollow1
ge hinweg daran gearbeitet. Zu jedem Zeitpunkt fühlte ich [4] Ralf Westphal, Softwareentwurf mit Flow-Design,
mich jedoch gut orientiert. Die Tests gaben mir wie üblich die www.dotnetpro.de/SL2501SleepyHollow2
Sicherheit, dass existierender Code noch stabil war oder dass [5] Ralf Westphal, IOSP 2.0,
über einige Zeit noch etwas fehlte, weil der Akzeptanztest www.dotnetpro.de/SL2501SleepyHollow3
noch nicht grün war. Außerdem konnte ich mich im Chat über [6] Ralf Westphal, IODA Architecture,
den bisherigen Verlauf der Ereignisse informieren. www.dotnetpro.de/SL2501SleepyHollow4
Die Prozessoren haben mich lange vom UI ferngehalten. [7] Ralf Westphal, Stratified Design over Layered Design,
Ich konnte die Software im Grunde fertigstellen, ohne inter- www.dotnetpro.de/SL2501SleepyHollow5
aktiv werden zu müssen. Und als der Akzeptanztest lief,
konnte ich mich rein auf das UI konzent rieren.
Einen Moment lang war ich unsicher, ob ich die Verteilung Ralf Westphal
mit dem Repository-Worker wirklich implementieren sollte. ist Trainer, Berater und Mitgründer der Clean
Für eine Demonstration des Sleepy-Hollow-Architekturmus- Code Developer Initiative (https://clean-code-
ters war das eigentlich nicht nötig. Ihn hatte ich vor allem im developer.de). Seine Schwerpunkte sind dauer-
Slicing „provoziert“, um die Zerlegungsebene der Worker haft hohe Produktivität für die Softwareent-
einzuführen. Doch mit der Entscheidung für Oak als MVC- wicklung und zukunftsfähige Teamorganisation.
Framework und der Unterstützung von ChatGPT war der Ser- https://ralfw.de
vice kein Problem. Das Wesentliche war ja mit einem davon
dnpCode A2501SleepyHollow
unabhängig realisierten und getesteten Repository auch
www.dotnetpro.de 1.2025 47
003355--004477__SSlleeeeppyyHHoollllooww__1133__SSeeiitteenn__eeaa..iinndddd 4477 2266..1111..2244 1144::4455