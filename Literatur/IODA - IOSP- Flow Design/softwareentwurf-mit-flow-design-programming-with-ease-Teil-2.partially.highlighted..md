<!-- Page 1 of 584 -->



---


<!-- Page 2 of 584 -->


Softwareentwurf mit Flow-Design
Programming with Ease - Teil 2
Ralf Westphal
Dieses Buch wird verkauft unter
http://leanpub.com/softwareentwurf-mit-flow-design
Diese Version wurde veröffentlicht am 2021-04-16
Dies ist ein Leanpub-Buch. Leanpub bietet Autoren und Verlagen, mit
Hilfe von Lean-Publishing, neue Möglichkeiten des Publizierens. Lean
Publishing bedeutet die wiederholte Veröffentlichung neuer
Beta-Versionen eines eBooks unter der Zuhilfenahme schlanker
Werkzeuge. Das Feedback der Erstleser hilft dem Autor bei der
Finalisierung und der anschließenden Vermarktung des Buches. Lean
Publishing unterstützt den Autor darin ein Buch zu schreiben, das auch
gelesen wird.
© 2020 - 2021 Ralf Westphal


---


<!-- Page 3 of 584 -->


Ebenfalls von Ralf Westphal
Test-first Codierung
Software Anforderungsanalyse mit Slicing
Die IODA Architektur im Vergleich


---


<!-- Page 4 of 584 -->


Inhaltsverzeichnis
Zum Geleit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
Programming with Ease . . . . . . . . . . . . . . . . . . . . . . 5
Das Softwareuniversum . . . . . . . . . . . . . . . . . . . . . . 9
Einleitung . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
Anforderungskategorien . . . . . . . . . . . . . . . . . . . . . . 12
It’s the productivity, stupid! . . . . . . . . . . . . . . . . . . . . 14
Produktivitätskiller . . . . . . . . . . . . . . . . . . . . . . . . . 16
Fehlende Korrekheit . . . . . . . . . . . . . . . . . . . . . . 18
Fehlender Wert . . . . . . . . . . . . . . . . . . . . . . . . . 20
Fehlende Ordnung . . . . . . . . . . . . . . . . . . . . . . . 22
Zusammenfassung . . . . . . . . . . . . . . . . . . . . . . . . . 25
Die Methode
. . . . . . . . . . . . . . . . . . . . . . . . 29
01 - Die Anforderung-Logik Lücke . . . . . . . . . . . . . . . . . 30
Logik - Der Stoff aus dem Verhalten entsteht . . . . . . . . . . . 30
Funktionalität . . . . . . . . . . . . . . . . . . . . . . . . . . 33
EffizienzI-EffizienzdurchAlgorithmenundDatenstrukturen 34
Effizienz II - Effizienz durch Verteilung . . . . . . . . . . . . 35
Zusammenfassung . . . . . . . . . . . . . . . . . . . . . . . 37
Von den Anforderungen zur Logik . . . . . . . . . . . . . . . . 38
Logik schwer definierbar . . . . . . . . . . . . . . . . . . . . 38
Die Phasen der Programmierung . . . . . . . . . . . . . . . 43
Zusammenfassung . . . . . . . . . . . . . . . . . . . . . . . 48
Übungsaufgaben . . . . . . . . . . . . . . . . . . . . . . . . . . 50


---


<!-- Page 5 of 584 -->


INHALTSVERZEICHNIS
02 - Entwurf im Überblick . . . . . . . . . . . . . . . . . . . . . . 53
Den Entwurf abstecken . . . . . . . . . . . . . . . . . . . . . . 53
Hierarchie der Lösungen . . . . . . . . . . . . . . . . . . . . 55
Von der Kunst lernen . . . . . . . . . . . . . . . . . . . . . . 57
Entwerfen ist fachgerecht . . . . . . . . . . . . . . . . . . . 59
Entwerfen ist agil . . . . . . . . . . . . . . . . . . . . . . . . 60
1. Der Lösungsansatz . . . . . . . . . . . . . . . . . . . . . . . . 62
2. Das Modell . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
Modellarten . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
Abstraktion . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
Zusammenfassung . . . . . . . . . . . . . . . . . . . . . . . . . 84
Übungsaufgaben . . . . . . . . . . . . . . . . . . . . . . . . . . 86
Aufgabe - Lösungsansatz finden . . . . . . . . . . . . . . . . 86
03 - Radikale Objektorientierung . . . . . . . . . . . . . . . . . . 89
Die Welt bestehend aus Objekten? . . . . . . . . . . . . . . . . . 90
Der Ursprung der Objektorientierung . . . . . . . . . . . . . . . 93
Wer hat’s erfunden? . . . . . . . . . . . . . . . . . . . . . . 94
Die zentrale Analogie der radikalen Objektorientierung . . . 95
Principle of Mutual Oblivion (PoMO) . . . . . . . . . . . . . . . 100
Unabhängigkeit . . . . . . . . . . . . . . . . . . . . . . . . . 102
Geschlossenheit . . . . . . . . . . . . . . . . . . . . . . . . 102
Unidirektionalität . . . . . . . . . . . . . . . . . . . . . . . 103
Ein Prinzip als Destillat . . . . . . . . . . . . . . . . . . . . 105
Implementationsidee . . . . . . . . . . . . . . . . . . . . . . 107
Integration Operation Segregation Principle (IOSP) . . . . . . . 114
Objekte verbinden als Verantwortlichkeit . . . . . . . . . . . 117
Ein Prinzip als Destillat . . . . . . . . . . . . . . . . . . . . 120
Implementationsidee . . . . . . . . . . . . . . . . . . . . . . 121
Philosophischer Exkurs . . . . . . . . . . . . . . . . . . . . . . . 126
Übungsaufgaben . . . . . . . . . . . . . . . . . . . . . . . . . . 137
Aufgabe - Mit PoMO/IOSP implementieren . . . . . . . . . 137
04 - Flow-Design mit 1-dimensionalen Datenflüssen . . . . . . . 139
0-dimensionale Datenflüsse . . . . . . . . . . . . . . . . . . . . 141
Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
Implementation . . . . . . . . . . . . . . . . . . . . . . . . . 147
1-dimensionale Datenflüsse . . . . . . . . . . . . . . . . . . . . 148
Der Datenfluss als Scope . . . . . . . . . . . . . . . . . . . . 151
Fließende Mengen . . . . . . . . . . . . . . . . . . . . . . . 157


---


<!-- Page 6 of 584 -->


INHALTSVERZEICHNIS
Implementation . . . . . . . . . . . . . . . . . . . . . . . . . 159
Übungsaufgaben . . . . . . . . . . . . . . . . . . . . . . . . . . 162
05 - Flow-Design mit 2-dimensionalen Datenflüssen . . . . . . . 166
Abstraktion durch Komposition . . . . . . . . . . . . . . . . . . 169
Stratified Design . . . . . . . . . . . . . . . . . . . . . . . . 170
2-dimensionale Datenflüsse . . . . . . . . . . . . . . . . . . 174
Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 182
Datenflüsse als aufgemotzte Abhängigkeitsdiagramme . . . 184
n:1 Übersetzungen . . . . . . . . . . . . . . . . . . . . . . . 199
Rekursion . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201
Reflexion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 204
Übungsaufgaben . . . . . . . . . . . . . . . . . . . . . . . . . . 206
06 - Flow-Design mit modularisierten Datenflüssen . . . . . . . 211
Abstraktion durch Aggregation . . . . . . . . . . . . . . . . . . 212
Physisch kategorisieren mit dem Dateisystem . . . . . . . . 220
Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221
Abhängigkeiten . . . . . . . . . . . . . . . . . . . . . . . . . 223
Orthogonale Containerdimension . . . . . . . . . . . . . . . 230
Die Modul-Hierarchie . . . . . . . . . . . . . . . . . . . . . . . 234
Klasse - Abhängigkeiten mit Kontrakten zähmen . . . . . . 236
Namensraum - Kontraktkollisionen vermeiden . . . . . . . . 248
Bibliothek - Wiederverwendbarkeit ermöglichen . . . . . . . 248
Paket - Abhängigkeiten stabilisieren . . . . . . . . . . . . . 250
Komponente - Die Arbeitsteilung befördern . . . . . . . . . 252
Service - Module plattformneutral machen . . . . . . . . . . 255
Wave - Softwareevolution zur Laufzeit . . . . . . . . . . . . 257
Die Modul-Hierarchie im Überblick . . . . . . . . . . . . . . 258
Datenflüsse modularisieren . . . . . . . . . . . . . . . . . . . . 260
Notation & Implementation I - Funktionen . . . . . . . . . . 261
Notation & Implementation II - Daten . . . . . . . . . . . . 267
Modularisierungsbeispiel . . . . . . . . . . . . . . . . . . . 270
Reflexion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278
Übungsaufgaben . . . . . . . . . . . . . . . . . . . . . . . . . . 281
07 - Flow-Design mit 3-dimensionalen Datenflüssen . . . . . . . 285
Die wahren Übersetzungsverhältnisse . . . . . . . . . . . . . . . 286
Streams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 290
Einsatzgebiete für Streams . . . . . . . . . . . . . . . . . . . 293


---


<!-- Page 7 of 584 -->


INHALTSVERZEICHNIS
Implementation . . . . . . . . . . . . . . . . . . . . . . . . . . . 302
Continuation . . . . . . . . . . . . . . . . . . . . . . . . . . 303
Iterator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 314
Fallunterscheidung in der Integration . . . . . . . . . . . . . 316
Polymorphie . . . . . . . . . . . . . . . . . . . . . . . . . . 324
Warteschlange . . . . . . . . . . . . . . . . . . . . . . . . . 326
Reflexion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 335
Übungsaufgaben . . . . . . . . . . . . . . . . . . . . . . . . . . 338
08 - Die IODA Architektur . . . . . . . . . . . . . . . . . . . . . . 341
Die Softwarezelle . . . . . . . . . . . . . . . . . . . . . . . . . . 343
System vs. Umwelt . . . . . . . . . . . . . . . . . . . . . . . 346
“Kleiderbügelarchitektur” . . . . . . . . . . . . . . . . . . . 351
Die Membran . . . . . . . . . . . . . . . . . . . . . . . . . . 354
“Griechische Architekturen” . . . . . . . . . . . . . . . . . . 370
Der Kern . . . . . . . . . . . . . . . . . . . . . . . . . . . . 374
“Vitruvianische Architektur” . . . . . . . . . . . . . . . . . 381
The Missing Concern: Integration . . . . . . . . . . . . . . . . . 382
IOSP in der Architektur . . . . . . . . . . . . . . . . . . . . 385
Interactors . . . . . . . . . . . . . . . . . . . . . . . . . . . 386
Processors . . . . . . . . . . . . . . . . . . . . . . . . . . . . 392
IODA: All together now! . . . . . . . . . . . . . . . . . . . . 394
Übungsaufgaben . . . . . . . . . . . . . . . . . . . . . . . . . . 397
09 - Finale im Softwareuniversum . . . . . . . . . . . . . . . . . . 400
Der Explizite Entwurf ist nötig . . . . . . . . . . . . . . . . . . 405
Der Entwurf ist deklarativ . . . . . . . . . . . . . . . . . . . . . 406
Das Modell beschreibt Funktionen in Beziehungen . . . . . . . . 408
Flow-Design im 4-dimensionalen Raum . . . . . . . . . . . . . . 411
Orientierungshilfe für die Softwareentwicklung . . . . . . . 416
Anhang - Musterlösungen
. . . . . . . . . . .420
Musterlösung: 01 - Die Anforderung-Logik Lücke . . . . . . . . . 422
Aufgabe 1 - Erklären . . . . . . . . . . . . . . . . . . . . . . . . 422
Vom Nutzen der Modellierung für die Programmierung (ELI5) 423
Reflexion . . . . . . . . . . . . . . . . . . . . . . . . . . . . 425
Aufgabe 2 - Modellieren . . . . . . . . . . . . . . . . . . . . . . 426
Lösungsansatz . . . . . . . . . . . . . . . . . . . . . . . . . 427


---


<!-- Page 8 of 584 -->


INHALTSVERZEICHNIS
Modell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 428
Reflexion . . . . . . . . . . . . . . . . . . . . . . . . . . . . 432
Musterlösung: 02 - Entwurf im Überblick . . . . . . . . . . . . . . 434
Aufgabe - Lösungsansatz finden . . . . . . . . . . . . . . . . . . 434
Lösungsansatz für die Domänenlogik . . . . . . . . . . . . . 436
Reflexion . . . . . . . . . . . . . . . . . . . . . . . . . . . . 442
Musterlösung: 03 - Radikale Objektorientierung . . . . . . . . . . 444
Aufgabe - Mit PoMO/IOSP implementieren . . . . . . . . . . . . 444
Modellskizze . . . . . . . . . . . . . . . . . . . . . . . . . . 445
Codierung der Integration . . . . . . . . . . . . . . . . . . . 445
Codierung der Operationen . . . . . . . . . . . . . . . . . . 450
Reflexion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 456
Musterlösung: 04 - Flow-Design mit 1-dimensionalen Daten-
flüssen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 458
Aufgabe 1 - Modellieren und implementieren . . . . . . . . . . . 458
Lösungsansatz verfeinern: Prä-Modell . . . . . . . . . . . . 459
Modell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 460
Implementation . . . . . . . . . . . . . . . . . . . . . . . . . 461
Aufgabe 2 - Reverse modeling . . . . . . . . . . . . . . . . . . . 463
Aufgabe 3 - Lösen, modellieren, implementieren . . . . . . . . . 468
Lösungsansatz . . . . . . . . . . . . . . . . . . . . . . . . . 468
Modell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 470
Codierung . . . . . . . . . . . . . . . . . . . . . . . . . . . 473
Reflexion . . . . . . . . . . . . . . . . . . . . . . . . . . . . 475
Musterlösung: 05 - Flow-Design mit 2-dimensionalen Daten-
flüssen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 477
Aufgabe 1 - Implementation eines Modells . . . . . . . . . . . . 477
Reflexion . . . . . . . . . . . . . . . . . . . . . . . . . . . . 480
Aufgabe 2 - Die Dimensionalität eines Modells erhöhen . . . . . 480
Reflexion . . . . . . . . . . . . . . . . . . . . . . . . . . . . 484
Aufgabe 3 - Anforderungen umsetzen mit 2-dimensionalem
Modell . . . . . . . . . . . . . . . . . . . . . . . . . . . . 485
Verstehen . . . . . . . . . . . . . . . . . . . . . . . . . . . . 486
Lösen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 487
Modellieren . . . . . . . . . . . . . . . . . . . . . . . . . . . 488
Codieren . . . . . . . . . . . . . . . . . . . . . . . . . . . . 491


---


<!-- Page 9 of 584 -->


INHALTSVERZEICHNIS
Reflexion . . . . . . . . . . . . . . . . . . . . . . . . . . . . 494
Musterlösung:06-Flow-DesignmitmodularisiertenDatenflüs-
sen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 496
Aufgabe 1 - Datenfluss modularisieren . . . . . . . . . . . . . . 496
Schrittweise Modularisierung . . . . . . . . . . . . . . . . . 496
Klassendiagramm . . . . . . . . . . . . . . . . . . . . . . . 498
Bibibliotheken . . . . . . . . . . . . . . . . . . . . . . . . . 499
Aufgabe 2 - Game of Life . . . . . . . . . . . . . . . . . . . . . 501
Lösungsansatz . . . . . . . . . . . . . . . . . . . . . . . . . 501
Modellierung . . . . . . . . . . . . . . . . . . . . . . . . . . 502
Reflexion . . . . . . . . . . . . . . . . . . . . . . . . . . . . 512
Musterlösung: 07 - Flow-Design mit 3-dimensionalen Daten-
flüssen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 515
Aufgabe 1 - Tic-Tac-Toe . . . . . . . . . . . . . . . . . . . . . . 515
Lösungsansatz . . . . . . . . . . . . . . . . . . . . . . . . . 516
Modell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 520
Implementation . . . . . . . . . . . . . . . . . . . . . . . . . 534
Reflexion . . . . . . . . . . . . . . . . . . . . . . . . . . . . 545
Musterlösung: 08 - Die IODA Architektur . . . . . . . . . . . . . 548
Aufgabe 1 - Umbau nach IODA . . . . . . . . . . . . . . . . . . 549
Abhängigkeiten zeigen den Abstraktionsgradienten hinab . . 555
Aufgabe 2 - Enturf nach IODA inkl. Implementation . . . . . . . 560
Anforderungsanalyse . . . . . . . . . . . . . . . . . . . . . 560
Lösungsansatz . . . . . . . . . . . . . . . . . . . . . . . . . 562
Modell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 563
Implementation . . . . . . . . . . . . . . . . . . . . . . . . . 567
Reflexion . . . . . . . . . . . . . . . . . . . . . . . . . . . . 573


---


<!-- Page 10 of 584 -->


Zum Geleit
Hallo, lieber Leser! Mein Name ist Ralf Westphal und ich bin dein Guide
beiderErkundungdesThemaSoftwareentwurfmitFlow-Design.Mirliegt
es als ein zentraler Aspekt für saubere, nachhaltige Programmierung sehr
am Herzen. Deshalb habe ich mich nach Jahren des Denkens, Tüftelns,
Anwendens, Diskutierens und Unterrichtens entschieden, meine Sicht
darauf einmal in einem Buch zusammenzufassen. Das, was vorher über
viele Blog-Artikel und Konferenzvorträge verteilt und nur unvollständig
nachlesbar manifestiert war, habe ich nun gesammelt und mit Übungsauf-
gaben versehen. Ich hoffe, damit gebe ich dir einen soliden Handlauf für
das Selbststudium.
Gleichzeitig ist dieses Buch wie die anderen in der Reihe Programming
with Ease aber auch Grundlage für meine interaktiven Trainings. Infor-
mationen zu denen findest du auf meiner Homepage: https://ralfw.de/
Und wer bin ich, dass ich mir zugetraut habe, dieses Buch zu schreiben?
• Seit 1986 bin ich selbstständig in der Softwarebranche tätig. Von
1988 bis 1998 als Co-Geschäftsführer einer Entwicklungsfirma für
Standardsoftware in einer Handwerksbranche.
• 1998 habe ich mich dann mehr meiner Leidenschaft “Forschung
und Entwicklung” hingegeben, indem ich Chefredakteur der VB-
Fachzeitschrift BasicPro geworden bin (bis 2001). Mir lag es am
Herzen, über spannende Softwaretechnologien zu berichten und
andere dabei anzuleiten. Seit Anfang der 1980er hatte ich immer
mal wieder in Fachmagazinen etwas beigetragen, doch nun sollte
“das Weitersagen” mein Beruf werden.
• Ab 2000 war ich viele Jahre sehr in der Microsoft-Community
unterwegs als sog. Regional Director und dann Most Valued Pro-
fessional. Ich habe auf vielen Konferenzen in Deutschland und den
USA gesprochen und auch Entwicklerveranstaltungen mit organi-
siert. Gleichzeitig habe ich weiter über Technologien und zuneh-
mend Softwarearchitekturthemen geschrieben und Projektberatun-
gen und Trainings durchgeführt.


---


<!-- Page 11 of 584 -->


ZumGeleit 2
• 2008 schließlich war das Jahr, in dem Stefan Lieser und ich an-
gefangen haben, eine deutsche Clean Code Community aufzubau-
en. Angefangen haben wir mit einem Wiki - https://clean-code-
developer.de/ -, in dem wir Prinzipien und Praktiken für saubere
Programmierung weiterentwickelt um die Basis eines Wertesys-
temsdokumentierthaben.IndenFolgejahrenhabenwirvieleClean
Code Developer Trainings gemacht und die Grundlagen dafür
zusammengetragen, was du in diesem Buch liest. Wir haben uns
intensiv und kritisch mit dem Thema Clean Code auseinanderge-
setzt.
• Irgendwann vielleicht ab 2018 schien mir dann der Begriff “Clean
Code” zwar etabliert, doch nicht mehr ausreichend, um das zu
beschreiben, wohin sich mein Denken entwickelt hatte. Aus der
Clean Code Praxis der Jahre davor hatte sich schon Flow-Design
herausgeschält als eigenständiger Ansatz zum Entwurf von sau-
berem Code - siehe auch das gleichnamige Buch in dieser Reihe
-, d.h. einem Denkwerkzeug für die Entwicklungsarbeit vor der
eigentlichen Codierung. Doch auch dieser Begriff war noch nicht
umfassend genug. Zu dem, worum es seit 2008 gegangen war -
nämlich einer nachhaltigen Softwareentwicklung - gehört einfach
noch mehr.
• 2020 schließlich habe ich mich entschieden, die drei Säulen, die sich
für nachhaltige Softwareentwicklung als notwendig und tragend
bewehrt hatten, unter dem Titel Programming with Ease zusam-
menzufassen und in einer Buchreihe zu dokumentieren.
Du siehst, mein Weg hat sich vom Anwender von Softwaretechnologien
über den Autor, der ihre Anwendung beschreibt, und den Trainer, der den
Entwurf ihrer Anwendung vermittelt, an einen Punkt geschlängelt, wo
ichnunmotivierenmöchtebeiderganzenAnwendungdieNachhaltigkeit
nicht zu vergessen.
Weil Nachhaltigkeit so wichtig ist und aus verschiedenen Gründe sehr an
grundlegenden Überzeugungen und Gewohnheiten der Softwareentwick-
lung und ihres Management rührt, erlaube ich mir auch den persönlichen
Ton, in dem ich dich hier schon anspreche. Der mag für dich in einem
Buch ungewohnt sein und eher zu Blog-Artikeln passen, doch mir liegt
das Thema so am Herzen, dass ich glaube, mit einer direkteren, weniger
gestelzten Ansprache es besser rüberzubringen.


---


<!-- Page 12 of 584 -->


ZumGeleit 3
Dazu kommt, dass ich damit von Anfang den Eindruck verwischen
möchte, es handle sich hier um letzte Weisheiten, absolute Wahrheiten
undobjektiveFakten.Nein,leiderkannichalldasnichtbietenunderlaube
mir sogar die Behauptung, kein Autor, den du zum Thema liest, kann das,
egal wie sein Name lauten oder sein Schreibstil sein mag.
Mehr als “informierte Erfahrungen im Fluss” kann ich dir nicht bieten.
Was du hier lesen wirst, ist ein Schnappschuss meines Denkens. Deshalb
habe ich auch lange gezögert, überhaupt ein Buch darüber zu schreiben;
das Format suggeriert ein größeres Gewicht des Inhalts, als er verdient.
Doch jetzt scheint mir ein Plateau in meinem Erkenntnisgewinnungspro-
zess erreicht, der eine solch umfängliche Aufzeichnung doch rechtfertigt.
Wenn ich dir damit helfen kann, in deinem Denken weiterzukommen,
freue ich mich. Nur um Weiterkommen, nicht um Ankommen geht es.
Ich wünsche dir Erkenntnisgewinn und auch Spaß bei der Lektüre!
-Ralf Westphal


---


<!-- Page 13 of 584 -->


Motivation
Der Softwareentwicklung fehlt etwas. Was fehlt, ist eine Form von Klar-
heit und vor allem Gelassenheit. So ist zumindest mein Gefühl, wenn ich
Softwareentwickler in meinen Clean Code Trainings oder auch an ihrem
Arbeitsplatz beobachte.
Wo Klarheit und Gelassenheit sind, da ist der Tritt sicher, da ist die
Zuverlässigkeit hoch, da stimmt die Qualität von vornherein umfassend
und die Stimmung ist entspannt. Leider scheint mir das aber nicht die
AtmosphäreindenmeistenSoftwareentwicklungsteamszusein.Oderwie
empfindest du es in deinem Team?
Stattdessen herrscht oft Verwirrung angesichts dessen, was der Kunde
will, es sind die Backlogs voll mit Bugs und das sprichwörtliche “What
the fuck?!” ist ständig hinter den Monitor-Triptychons im Team Room zu
hören (oder zumindest auf den Gesichtern der Entwickelnden zu lesen).
Was mögen die Gründe dafür sein? Es gibt sicher viele. Ein ganz grund-
legender scheint mir jedoch dieser: Die Softwareentwicklung ist ins
Ungleichgewicht gekommen. Sie erfüllt nicht in gleicher Weise sys-
tematisch und kompetent alle Anforderungen des Auftraggebers. Sie
starrtaufdieeinenundlässtdabeieinenblindenFleckfürdieanderen
entstehen. Das führt früher oder später zu einem für den Auftraggeber
sehr spürbaren Qualitätsdefizit, dessen Ausgleich schwerer und schwerer
wird. Das Kind ist tief im Brunnen. Es fehlt einfach an Nachhaltigkeit.
Gelassenheit ist in solcher Situation nicht mehr möglich, wenn Klarheit
über so lange Zeit so eklatant gefehlt hat. Programmierung mit Leichtig-
keit sieht anders aus.
Mehr Technologie, mehr Infrastruktur ist darauf keine Antwort. Vielmehr
ist - horribile dictu! - ein Kulturwandel nötig. Ohne grundsätzliches
Umdenken geht es nicht. Die Grundhaltung ist zu verändern: Es braucht
einBewusstseindafür,dassauchsoetwasimmaterielleswieSoftware,
Nachhaltigkeit braucht.


---


<!-- Page 14 of 584 -->


Motivation 5
Wenn in deinem Team schon agil gearbeitet wird, hast du eine Ahnung,
was Kultur und Kulturwandel bedeutet. Doch leider ist Agilität nicht
genug für nachhaltige Softwareentwicklung. Sie ist zwar notwendig für
die Nachhaltigkeit, die ich meine, aber nicht hinreichend.
Wie wichtig Nachhaltigkeit ist, weiß zwar schon lange jeder Koch und
jeder Chirurg - doch die Softwareentwicklung hinkt leider noch hinterher.
Die oberste Priorität haben bei Ersteren Sauberkeit und Hygiene; ohne
sie sind Erfolge nur von kurzer Dauer. Wer eine Küche am Ende des
Tages mit dreckigem Geschirr und voller Abfall zurücklässt, beschädigt
die Grundlage für die Arbeit morgen. Wer heute Operationsbesteck nicht
sterilisiert und am Ende einer Operation nicht zählt, riskiert Komplikatio-
nenmorgen.SauberkeitundHygienesindderRahmen,indemdasKochen
und chirurgische Eingriffe stattfinden.
Ich bin überzeugt, dass für die Softwareentwicklung ein Nachhaltigkeits-
rahmen erst noch solide aufgespannt werden muss. Korrektheit und
Ordnung sind noch nicht in gleicher Weise als Grundanforderungen
in der Softwareentwicklung anerkannt wie Sauberkeit und Hygiene
in anderen Branchen. Das ist die fehlende Klarheit, die die Entwicklung
von Gelassenheit verhindert.
Diese Situation verbessern zu helfen, ist mein Anliegen. Ich möchte dir
helfen, klarer und gelassener zu programmieren. Weniger Stress durch
mehrNachhaltigkeitfürdeineSoftwareentwicklungistmeinZiel.Wiedas
erreicht werden kann, damit habe ich mich in den vergangenen 15 Jahren
intensiv auseinandergesetzt. Ich hoffe, du empfindest das, was ich hier
nun “an einem Ort” zusammentrage, als Hilfe in deinem Entwickleralltag.
-Ralf Westphal, 2020, Bansko (BG) / Hamburg (DE)
Programming with Ease
Nachhaltigere Softwareentwicklung in Klarheit und Gelassenheit umfasst
für mich mehr, als ich dir in diesem Buch vorstellen kann. Mit ein paar
Tipps&Tricks ist es nicht getan. Es geht durchaus ans Eingemachte: an
deine Glaubenssätze und Gewohnheiten.
DievielfachfehlendeNachhaltigkeitinderSoftwareentwicklungisteinso
tiefliegendesProblem,dasseinigeAnstrengungennötigsind,dieSituation


---


<!-- Page 15 of 584 -->


Motivation 6
zu ändern. Du wirst Zeit brauchen, anders wahrzunehmen, zu denken
und dann zu handeln. Dein Team wird Zeit brauchen, denn in der
Zusammenarbeit muss sich einiges ändern. Und schließlich wird sich
sogar dein Management und dein Auftraggeber ebenfalls ändern müssen
in den Erwartungen an dich und dein Team.
Das klingt nach einigem Aufwand, oder? Ja, stimmt. Leider kann ich dir
den nicht ersparen. Das Wurzelproblem von “schwer wartbarer Software”
liegt zu tief, als dass es dafür eine schnelle Lösung gäbe. Wenn du aber
dran bleibst, dann bin ich gewiss, dass sich die Mühe lohnt.
Vermitteln möchte ich dir - und deinem Team - Programming with Ease
als umfassende Herangehensweise an die Softwareentwicklung, die dich
abholt bei der Konfrontation mit Anforderungen und begleitet bis zur
Ablieferung von hochqualitativem Code.
UmmoderneTechnologienundtechnischeFeinheitengehtesnicht.React,
NoSql,GraphQL,Docker,Kubernetes,Kafka…alldasistdarinkeinThema.
Oder wenn, dann nur indirekt in Form von Prinzipien und Konzepten, die
dir helfen sollen, solche Technologien einzuordnen.
StattdessengehtesumPrinzipienundPraktikenderSoftwareentwicklung.
Das hört sich zwar nach “theoretischem Kram” an, doch sei gewiss,
mir ist es sehr, sehr wichtig, dass die Theorie in der Praxis gegründet
ist. Theoretische Überlegungen müssen zu praktisch hilfreichen Effekten
führen. Deshalb kann ich es dir nicht früh genug mit auf den Weg geben:
Welche Empfehlungen du auch immer hier lesen magst, egal wie sehr
ich sie begründe, sie stehen nie höher als der Zweck. Wenn du in einer
bestimmten Situation also meinst, einem Zweck nachhaltig besser dienen
zu können, als durch Befolgung einer Empfehlung… dann - by all means -
weiche von der Empfehlung ab. Allerdings: Du solltest schon wissen, was
dudatust.HabealsoeinebelastbareBegründungparat-wennschonnicht
mir gegenüber, dann aber für deine Teamkollegen.
Das Gesamtthema Programming with Ease ist also umfangreich. Wie ich
es dir nahebringe, habe ich lange überlegt. Am Ende habe ich mich dann
für 3 Bücher entschieden, die 1+3 Themenblöcke behandeln.
Test-first Codierung ist der erste Themenblock, auch wenn Codierung
die letzte Hürde ist, die du in der Programmierung nehmen musst. Den-
noch macht dieses Buch den Anfang in der Trilogie, weil es thema-
tisch dir als Entwickler wahrscheinlich am nächsten liegt. Codierung ist


---


<!-- Page 16 of 584 -->


Motivation 7
praktisch, Codierung wahrlich unausweichlich, Codierung hat technisch-
technologischen Reiz. Ich hoffe, dort kann ich dich am besten abholen,
wenn es schon so ans Eingemachte geht.
Im ersten Band geht es darum, dass Codierung aus meiner Sicht eben
ausschließlich test-first stattfinden sollte. Das zu akzeptieren und dann
auch zu leben, ist die erste Herausforderung auf dem Weg zu nachhaltiger
Programmierung. Ich hoffe, dass ich dir die Gründe dafür im ersten
Band ausführlich genug darlegen und dir diese Praxis mit verschiedenen
Problemlösungsansätzen auch schmackhaft machen kann.
Softwareentwurf mit Flow-Design ist der zweite Themenblock, auch
wenn Entwurf als Planung von Code der Codierung vorausgehen sollte.
Weil “Planung” sich für dich aber vielleicht nicht so attraktiv anhört,
wollte ich das Thema nicht im ersten Band der Reihe behandeln, auch
wenn ich es für das wichtigste der drei Themen halte.
Ja, tatsächlich, ich hänge dem Glauben an, dass wir in der Program-
mierung mehr denken sollten. Mehr denken vor dem Codieren, ist der
Nachhaltigkeit absolut zuträglich. Nicht, dass nicht gedacht würde - doch
mein Eindruck ist, dass gewisse Themen dabei unberücksichtigt bleiben.
Es wird z.B. viel über den rechten Einsatz von Technologien und Infra-
struktur nachgedacht. Es wird auch viel über Agilität nachgedacht oder
über DevOps. Und das ist alles gut und richtig. Doch es bleibt ein blinder
Fleck. Um den dreht es sich bei Programming with Ease im Allgemeinen
und bei Flow-Design im Speziellen: das ist die visuelle Modellierung von
Softwarelösungen.
Der letzte Themenblock unter dem Bogen, den Programming with Ease
spannt,istdanndieSoftwareAnforderungsanalysemitSlicing.Damit
gehe ich noch einen Schritt vor den Entwurf und möchte dir empfehlen,
AnforderungendurcheinespezielleEntwicklerbrillezubetrachten.Durch
die Brille der Agilität siehst du Anforderungen als User Stories, Story-
boards, Epics oder gar Event Storms. Auch das ist alles wunderbar. Du
sollst davon nichts aufgeben. Doch in meiner Erfahrung ist auch durch
diese Brille etwas nicht sichtbar, das dir das Programmiererleben aber
leichter machen würde.
Der agilen Herangehensweise fehlt eine gewisse technische Sicht. Das
findeichganzverständlich,allemaldasichinzwischenScrumundKanban
als Vorgehensmodelle etabliert haben und von XP nur noch wenig zu


---


<!-- Page 17 of 584 -->


Motivation 8
hören ist.¹ Damit haben die “Softwarelaien” gewonnen, so dass Anfor-
derungen von ihnen definiert werden, wie es für sie nachvollziehbar ist.
Das soll natürlich auch so sein - nur darf eine Sichtweise, die dir als
Programmierer dient, deshalb nicht vernachlässigt werden. Das scheint
mir jedoch der Fall, so dass nachfolgende Phasen in der Programmierung
dir schwerer fallen als nötig.
Insgesamt wird durch die Dominanz der “Softwarelaien” sogar man-
gelnder Qualität und Unzuverlässigkeit Vorschub geleistet. Ja, du liest
richtig: Real existierende Agilität führt durchaus noch zu suboptimalen
Ergebnissen.Daswirdauchnichtbesser,wenndudieZähnenochtieferin
das agile Manifest schlägst. Es braucht einfach verschiedene Perspektiven.
Agilitätistdieeine.Das,wasich dirinProgrammingwithEase vermitteln
will, ist eine zweite.
Codierung, Entwurf, Anforderungsanalyse sind die drei großen Themen-
blöcke in Programming with Ease. Damit verrate ich dir noch nicht zuviel
an dieser Stelle. Ausführlicher begründet wird das in einem kleineren,
übergreifenden Themenblock. Den umfasst die Einleitung und das erste
Kapitel. Beides inklusive dieser Motivation wiederhole ich in allen Bü-
chern, um dir zu ermöglichen, sie doch in einer anderen Reihenfolge zu
lesen, als der hier vorgestellten. Zwar habe ich mir bei der Ordnung etwas
gedacht - doch auch dafür gilt: zu eng solltest du das nicht sehen.
Einleitung und erstes Kapitel liefern den Hintergrund, vor dem ich die
anderen Themen entfalte. Sie werden zuerst ganz grob in einem Zusam-
menhangentwickelt,damitduweißt,wiesiemiteinanderverbundensind.
Danach kommt die blockweise Vertiefung, bei der du diesen Hintergrund
im Hinterkopf haben solltest.
Insgesamt ergibt sich hoffentlich für dich ein Gesamtrahmen, in dem du
dich gut aufgehoben fühlst. Einfach(er) soll dir die Programmierung ja
werden.
¹Vielleicht kann man Software Craftsmanship als einen Arm der Entwicklung von
XP verstehen. Der andere ist dann z.B. Scrum. Damit wären zwei Belange getrennt, die
XP ursprünglich in XP vereint waren. Software Craftsmanship würde in dem Fall für die
technischeSeitevonXPstehen.EinblinderFleckbliebejedochausmeinerSicht.InXPwie
in Software Craftsmanship findet sich schlicht zu wenig Methode. Beide sind Sammlungen
von Bausteinen, zwischen denen kein roter Faden gespannt ist, an dem du dich konkret
voranarbeitenkönntest.Umgenaudengehtesmiraber.


---


<!-- Page 18 of 584 -->


Motivation 9
Das Softwareuniversum
WennProgrammingwithEaseeinBogenist,denichüberdeinenSoftware-
entwicklungsprozess spannen möchte, also ein Bogen in der Zeit, dann ist
das Softwareuniversum der dazugehörige Raum für Softwarestrukturen
In diesem Raum spielt sich für mich alle Softwareentwicklung ab. Darin
bewegst du dich mal langsamer mal schneller, mal in die eine Richtung,
mal in die andere.
Allerdings ist der Raum des Softwareuniversums kein dreidimensionaler,
sondern ein vierdimensionaler. Er besteht aus vier Dimensionen, die
jede Logik auf eine andere Weise in Container fassen und zu Strukturen
verbinden.
Was Logik ist, verrate ich dir in der Einleitung. An dieser Stelle nur soviel:
sie ist die Essenz von Software. Dass du Logik in hoher Qualität schreibst,
ist für den Kunden von höchster Wichtigkeit, denn sie bestimmt das
Softwareverhalten. Du kannst sie also nicht einfach “hinklieren”, sondern
musst sie sorgfältig schneiden und verpacken.
1. Zunächstmusstdudas,wasdieLogikleistensoll,inmöglichstfeine
Anforderungsscheiben schneiden beim Slicing. Darum geht es im
dritten Band von Programming with Ease.
2. Dannmusstdudirüberlegen,wieduvorallemfunktionaleAnforde-
rungen mit Logik so erfüllst, dass du sicher sein kannst, dass deine
Lösung korrekt ist. Du musst dabei aus unzähligen fremden und
eigenen Bausteinen Kompositionen herstellen, die du testen kannst.
Das geschiehtmitFunktionen undist Themades erstenBandesund
auch des zweiten Bandes.
3. Um nicht den Überblick über deine Komposite zu verlieren, teilst
du sie in zweckvolle Gruppen auf mehreren Ebenen ein, die Zusam-
mengehöriges aggregieren und von anderem entkoppeln; das sind
die Module deiner Software. Darum geht es vor allem im zweiten
Band, aber auch schon im ersten.
4. Undschließlichmusstdudichleidernocheinigennicht-funktionalen
Anforderungen widmen, die du auch mit sorgfältiger Komposition
von Logik nicht lösen kannst. Es bleibt dir nichts anderes übrig, als
Logik auf verschiedene Hosts zu verteilen. Darum geht es vor allem
im zweiten Band, aber auch im dritten.


---


<!-- Page 19 of 584 -->


Motivation 10
Zweck des Softwareuniversums ist es, die Strukturelemente, die du im
Grunde schon aus deiner Programmierpraxis kennst - Beispielsweise
Klasse, Thread, Service, Message, Funktion -, in einen Zusammenhang
zu stellen. Sie bekommen alle einen klaren Zweck im Hinblick auf die
umfassenden Anforderungen des Auftraggebers. Vor allem möchte ich dir
jedoch zeigen, welche Rolle sie spielen in Bezug auf die Nachhaltigkeit.
Die vier Dimensionen des Softwareuniversums sind für mich:
• Delivery: Logik in Scheiben (slices) unterschiedlicher Dicke ge-
schnitten für die iterativ-inkrementelle Lieferung an den Kunden.
• Composition:LogikzuFunktionenzusammengestellt,umfunktio-
nale wie nicht-funktionale Anforderungen zu erfüllen.
• Decoupling: Funktionen zu Modulen (z.B. Klassen) aggregiert, um
Ordnung in die Vielfalt zu bringen. Testbarkeit und Wandelbarbeit
sind der Gewinn.
• Distribution: Funktionen verteilt auf Hosts (z.B. Threads) und
entkoppelt über asynchrone Kommunikation um weitere nicht-
funktionale Anforderungen zu erfüllen.
GrobeSkizzedesSoftwareuniversums


---


<!-- Page 20 of 584 -->


Motivation 11
Jede Zeile Logik, jeder Tropfen Essenz deiner Software, lässt sich im
Softwareuniversum als Punkt im vierdimensionalen Raum verorten, da
Logik immer gleichzeitig Teil einer Funktion in einem Modul in einem
Host in einem Slice ist.
Das muss dir im Moment abstrakt vorkommen. Es fehlen ja auch noch
viele Definitionen von Begriffen. Dennoch wollte ich dir das Softwareuni-
versum als Ausblick nicht vorenthalten. Als ich es das erste Mal erblickt
habe, war es für mich ein wenig wie beim Overview Effect²: Ich konnte
nun von außen überblicken, wovon ich vorher immer nur Teile gesehen
hatte. Das hat mein Verständnis von Softwareentwicklung grundlegend
verändert.
Deshalb gehören die Bände von Programming with Ease zu einer umfas-
senderen Reihe, die alle “im Softwareuniversum spielen”.
²https://en.wikipedia.org/wiki/Overview_effect


---


<!-- Page 21 of 584 -->


Einleitung
Bevor ich dir konkrete “Tipps&Tricks” für die nachhaltige Softwareent-
wicklung gebe, möchte ich dir ein big picture skizzieren. Zu oft habe ich
gehört und gelesen, dass einzelne Prinzipien und Praktiken empfohlen
werden, ohne einen Kontext, ohne eine “Herleitung”. Bei aller Richtigkeit
dieser Empfehlungen werden sie dann aber leicht missverstanden oder
eben eingesetzt, wenn der Kontext nicht passt. Das führt zu Frustration.
Die möchte ich dir ersparen, so weit es mir möglich ist.
Es ist schwer genug, all das in Worte, auch noch lineare zu fassen, was ich
dirvermittelnwillfürnachhaltigeSoftwareentwicklung.Eswirdmirauch
nur bruckstückhaft gelingen. Dass du mich missverstehst, ist für mich
vorhersehbar und unvermeidbar. Doch ich will mich bemühen, das zu
minimieren. Und eine auf der Hand liegende Maßnahme dafür ist, dass
ich etwas aushole, um einen Rahmen aufzuspannen, in dem das konkrete
Thema dieses Buches und der anderen der Reihe eingehängt werden kann.
Deshalb: Halte einen Moment durch, bis es an das eigentlichen Thema
dieses Bandes. Keine Sorge, du wirst davon genug zu sehen bekommen.
Und nun gehts los. Wo sonst als am Anfang jedes Softwareprojektes, bei
den Anforderungen:
Anforderungskategorien
Softwareentwicklung hat Anforderungen in drei Kategorien zu erfüllen,
um ihr Geld wert zu sein:
• Zunächst muss Softwareentwicklung funktionierende Software lie-
fern. Auftraggeber haben funktionale Anforderungen an Soft-
ware, die sie erfüllt sehen wollen. Nur dann hat die Funktionalität
von Software hohe Qualität. Das ist so natürlich, dass es kaum der
Rede wert ist - dennoch müssen wir da noch genauer hinschauen,
auch wenn ich denke, mit diesen Anforderungen bist du bestens
vertraut. Sie treiben dir genug Schweiß auf die Stirn.


---


<!-- Page 22 of 584 -->


Einleitung 13
• Funktionalität allein ist allerdings nicht genug - auch das ist dir
klar - und noch nicht einmal der Grund für die Beauftragung von
Softwareentwicklung. Software soll vor allem nicht-funktionale
Anforderungen erfüllen! Sie soll Funktionalität besser (Kompa-
rativ!) anbieten als die Alternative (z.B. bisherige Software oder
Handarbeit). Software soll z.B. schneller oder einfacher oder ska-
lierbarer oder sicherer funktionieren als die Alternative. Dann hat
die Effizienz³ von Software hohe Qualität. Das ist ebenso natürlich,
dass es kaum der Rede wert ist - aber diese Anforderungen bereiten
dir womöglich noch mehr Kopfschmerzen als die funktionalen.
Funktionale und nicht-funktionale Anforderungen zusammen sind Ver-
haltensanforderungen an Software. Der Auftraggeber kann durch Aus-
führung der Software überprüfen, ob die geforderte Qualität hergestellt
wurde. Dieser Oberbegriff ist wichtig, wie du im Weiteren sehen wirst.
Vielleicht überraschend für dich, sehe ich Korrektheit darin noch nicht
subsummiert. Korrektheit ist keine explizite weitere Anforderung an
Software, sondern ist impliziet in der Erwartung, dass spezifizierte Anfor-
derungen tatsächlich durch gelieferte Software erfüllt werden. Software
ist also in dem Maße korrekt, in dem sie die Spezifikation erfüllt.
Mach dir an dieser Stelle keinen Kopf über den Begriff Spezifikation.
Ich will damit keine Norm heraufbeschwören, sondern verstehe darunter
lediglich eine irgendwie gearbeitet Liste von gewünschten Eigenschaften.
ObdieaufeinerServiettestehenoderineinem500seitigenBuchgebunden
sind,isteinerlei.DerKundekannzurLaufzeitdieseListeabhakenundden
Erfüllungsgrad seiner Wünsche messen. Korrektheit liegt vor, wenn der
Erfüllungsgrad 100% ist. Fehlt allerdings ein Wunsch in der Spezifikation
und ist deshalb nicht implementiert, ist das Verhalten der Software nicht
inkorrekt, selbst wenn der Kunde bei der Überprüfung das Verhalten
vermisst.
³Effizienz habe ich als Begriff für die nicht-funktionalen Anforderungen wie Perfor-
mance, Skalierbarkeit, Benutzerfreundlichkeit, Sicherheit usw. gewählt, um sie kurz und
knapp unter einer Kategorie zusammenzufassen. Die Benennung ist nicht perfekt, aber ich
finde sie erstmal gut genug. Dem Kunden geht es um Funktionalität und Effizienz bei der
Software.Klingtdochsinnig,oder?


---


<!-- Page 23 of 584 -->


Einleitung 14
It’s the productivity, stupid!
Über die Verhaltensanforderungen hinaus hat der Auftraggeber noch eine
weitere Anforderung, die jedoch selten ausdrücklich formuliert oder gar
vertraglich festgehalten wird. Das ist nun ein ganz wesentlicher Punkt;
passauf,dennesgehtumdichunddeinTeam!HierkommtdieMotivation
für Agilität und Clean Code Development:
• Die Softwareentwicklung soll stets zügig funktionale wie nicht-
funktionale Anforderungen erfüllen. Auftraggeber haben also auch
noch einen Anspruch an die Produktivität der Softwareentwick-
lung.
Verhaltensanforderungen werden unmittelbar durch Code erfüllt. Die
Produktivitätsanforderung hingegen ist eine an die herstellende Or-
ganisation.
Wie Funktionalität mittels Code hergestellt wird, ist eine Sache von
Programmiersprachen, Bibliotheken und Frameworks. Diese Fähigkeit
ist die primäre, die du als Softwareentwickelnde(r) erwirbst und stetig
verfeinerst.
Wie Effizienzen mittels Code hergestellt werden, ist ebenfalls zunächst
eine Sache von Programmiersprachen, Bibliotheken und Frameworks.
Diese Fähigkeit wird gewöhnlich später erworben, ist letztlich jedoch die,
auf die sich viele Entwickelnde konzentrieren. Bücher wie “Algorithmen
und Datenstrukturen” beschäftigen sich mit diesem Thema.
Nicht immer jedoch lässt sich damit das geforderte Qualitätsniveau schon
erreichen. Performance oder Skalierbarkeit brauchen oft Unterstützung
durch Verteilung von Code zur Laufzeit auf verschiedene Threads im
selben Betriebssystemprozess oder in verschiedenen oder gar auf mehre-
ren Rechnern oder in unterschiedlichen Netzwerken. Damit beschäftigt
sich traditionell die Softwarearchitektur. Hier warten große Herausfor-
derungen! Hier kannst du der Held so mancher Infrastrukturtechnologie
werden.
Doch selbst wenn du gut dabei bist in der Herstellung von Funktionalität
und Effizienz, kann es leicht sein, dass der Auftraggeber nicht mit dir
zufrieden ist. Wie kann das sein? Du bist vielleicht einfach zu langsam.


---


<!-- Page 24 of 584 -->


Einleitung 15
Perfekte Verhaltensqualitäten lieferst du, nur leider zu spät. Potenziert
wird das, wenn du auch noch unzuverlässig bist, d.h. die Lieferung bis
zu einer Frist versprichst und dann doch nicht lieferst.
FürdenAuftraggebergibtesalsozwei“Laufzeiten”:dieSoftware-Laufzeit
und die Team-Laufzeit. An beide hat er Anforderungen. Die Software
soll performen, das Team aber auch. Letzteres setzt der Auftraggeber
allerdingsmehroderwenigervoraus.DafürschreibterkeineSpezifikation.
Er glaubt einfach, dass du professionell arbeitest. Dazu gehört für ihn,
dass du stets “flott dabei bist” und dir kein Bein stellst. Leider ist das oft
nicht der Fall. Softwareentwicklung fällt immer wieder über die eigenen
Füße; sie merkt sozusagen nicht, dass sie mit zusammengebundenen
Schnürsenkeln läuft.
Aber wie kann das sein? Ich denke, dafür gibt es viele Gründe. Neben
historischen, sozusagen systemimmanenten gibt es jedoch einen immer
wieder ganz akuten: Druck. Die Softwareentwicklung wird vom Auf-
traggeber oft sehr mit Deadlines unter Druck gesetzt (und lässt sich
auch unter Druck setzen), so dass sie meint, nie Zeit zu haben, die
Schnürsenkel ordentlich zu binden. Lieber stolpert sie dahin, stets willig,
dem Kunden Verhaltensanforderungen grob zu erfüllen, als dass sie sich
“sauber aufstellt” und “fit hält”.


---


<!-- Page 25 of 584 -->


Einleitung 16
WasderAuftraggeberwill:DieKategorienderAnforderungen
Produktivitätskiller
Der Auftraggeber der Softwareentwicklung schaut gewöhnlich vor allem
auf die Erfüllung von Verhaltensanforderungen. Das ist für ihn am ein-
fachsten. Das merkst du jedes Mal, wenn Abnahme ist. Darum drehen
sich dann die Diskussionen. Über den Herstellungsprozess, wie es zum
präsentierten Verhalten gekommen ist, wird nicht diskutiert. Jedenfalls
nicht direkt. Dafür fehlt ja eine Spezifikation. Was aber eben nicht heißt,
dass der Kunde zur Team-Performance keine Meinung hätte.
Hohe Produktivität von dir und deinem Team wird einfach vorausgesetzt.
Wie die Erfahrung jedoch zeigt, ist es eine naive Erwartung, dass hohe
Produktivität nach einem vielleicht anfänglich guten Start “einfach so”
erhalten bliebe. Die Produktivitätskurve sink vielmehr relativ schnell auf
einen bedauerlich niedrigen Wert. Hier eine typische Darstellung der
Entwicklung (Quelle⁴):
⁴https://blogs.sap.com/2018/05/02/introducing-agile-software-engineering-in-
development/


---


<!-- Page 26 of 584 -->


Einleitung 17
Produktiv sind Entwickelnde nicht einfach, weil sie gerade codieren. Nur
weil du dich gestresst fühlst beim Programmieren, performst du nicht
automatisch im Sinne des Auftraggebers. Das mag enttäuschend klingen,
ist aber die Realität. Solange es da ein Missverständnis zwischen dir und
dem Auftraggeber gibt, sind Konflikte unvermeidlich.
Nicht jede geschriebene/veränderte Codezeile trägt zur Produktivität bei,
wie der Auftraggeber sie sich wünscht. Produktiv ist die Softwareent-
wicklung nur, wenn sie neue Anforderungen erfüllt, d.h. an Features
arbeitet. Das kann durch Codierung geschehen oder durch andere, vorge-
lagerte Tätigkeiten.
Je öfter du Features lieferst, d.h. Erweiterungen, Verbesserungen - keine
Bug Fixes (!) - und die auch noch korrekt lieferst, desto produktiver bist
du aus Sicht des Auftraggebers.
Wenn du also auch die (unausgesprochenen) Anforderungen des Auf-
traggebers an deine Produktivität erfüllen willst, tust du gut daran, alles
was dabei hinderlich sein könnte, zu vermeiden. Wenn du während des
Kochens eines Abendessens merkst, dass dir eine Zutat fehlt und du
losrennst, um sie zu kaufen, bricht deine Produktivität ja auch ein. Dito,
wenn du mit dem Kochen beginnen willst und findest die Spüle voll mit
dreckigen Töpfen. Dito, wenn du dich zum Date fertigmachen willst und
feststellen musst, dass deine beste Hose noch in der Wäsche ist. Wann
immer also etwas fehlt, das du brauchst, um zu tun, was du eigentlich tun
willst, stehst du einem Produktivitätskiller gegenüber.
Vorausgesetzt,dassdutechnischundfachlichkompetentbist-auchdaran


---


<!-- Page 27 of 584 -->


Einleitung 18
hat ein Auftraggeber Interesse -, sehe ich vor allem drei Produktivitätskil-
ler, die du ausschalten musst:
Fehlende Korrekheit
Die Softwareentwicklung kann sehr geschäftig codieren, ohne produktiv
zu sein. Das ist immer der Fall, wenn sie Bug Fixing betreibt.
Bugs sind Inkorrektheiten, d.h. Qualitätsmängel durch
Nichterfüllung der Spezifikation.
BugszufixenistNacharbeit(re-work).NacharbeitoderAusbesserungvon
Defekten ist eine der Verschwendungsarten in der Lean “Philosophie”⁵.
Aus Sicht des Kunden vertust du deine Zeit mit Dingen, die schon lange
hätten erledigt sein sollen. Statt Bugs zu fixen, wäre es dem Auftraggeber
lieber, dass du schon wieder an neuem Verhalten arbeitest.
Jede Stunde, die du mit Bug Fixing verbringst, fehlt dir für die Feature-
Produktion.DasBugFixingzubegrenzen,selbstwennnochBugsbekannt
sind, ist daher eine notwendige Maßnahme, um produktiv zu bleiben⁶.
Besser jedoch, wenn die Softwareentwicklung gar nicht erst in diese Ver-
legenheit kommt. Warum nicht Bugs von vornherein einfach vermeiden?
Fehlende Korrektheit ist der Produktivitätskiller #1.
Um die Produktivitätsanforderung des Kunden zu erfüllen, muss Korrekt-
heit die oberste Priorität haben.[^klarheitsprämisse]
[^klarheitsprämisse]: Prämisse hierbei ist, dass klar ist, welches Verhalten
die Software überhaupt haben soll. Korrektheit meine ich nur auf das,
was klar spezifiziert ist. Wo Klarheit fehlt - allemal unwissentlich -,
⁵http://www.lean-production-expert.de/lean-production/7-verschwendungsarten.
html
⁶Siehedazuz.B.Zero-BugSoftwareDevelopment


---


<!-- Page 28 of 584 -->


Einleitung 19
sind überraschende Qualitätsmängelunvermeidbar. Das sind dann jedoch
keine Inkorrektheiten.
Korrektheit ergibt sich allerdings nicht einfach, sondern muss systema-
tisch hergestellt und erhalten werden.
• ZunächstistbeiderFeature-Produktion(undauchbeimBugFixing)
Korrektheit in Form von Reife zu erreichen. Zu jedem Zeitpunkt
bzw. spätestens vor Präsentation/Auslieferung eines Softwarestan-
des musst du prüfen, ob deine Software schon korrekt ist gem.
der Spezifikation. Haben deine Anstrengungen zur Herstellung
gewünschter Qualitäten schon ausreichenden Erfolg gehabt? Wenn
du keine Differenz mehr siehst zwischen spezifiziertem und realem
Verhalten, dann ist dein Code reif für die Präsentation beim Auf-
traggeber.
• Darüber hinaus ist allerdings stets sicherzustellen, dass bei der
Feature-ProduktionvorhererreichteKorrektheitnichtzerstörtwird.
Es darf keine Regression stattfinden, d.h. kein Rückfall auf ein
früheres, niedrigeres Korrektheitsniveau. Der Auftraggeber erwar-
tet Stabilität der Software in Bezug auf die Korrektheit. Während
der Veränderung von Code bzw. spätestens vor Präsentation/Aus-
lieferung eines Softwarestandes musst du deshalb immer wieder
überprüfen, ob deine Software noch korrekt ist gem. der Spezifikati-
on. “Verschlimmbesserung” ist eines der größten Risiken in der
Softwareentwicklung.
Maßnahmen für die Korrektheit umfassen z.B. den Abnahmetest, eine
Beta-Test-Phase,dieBeschäftigungvonTestern,dieDefinitioneinesDone-
Zustands inkl. Akzeptanzkriterien, automatisierte Tests, eine Continuous
Build/Integration Pipeline oder die Codierung nach Test-Driven Develop-
ment (TDD).
Produktivität braucht Sorgfalt. Es sind “die Dinge richtig zu tun”. So wird
landläufig auch Effizienz beschrieben. Man weiß, was zu tun ist - und tut
es dann auch so, wie es getan werden sollte. Die Verhaltensanforderungen
sind klar, die Softwareentwickelnden sind kompetent, das Ergebnis ist
korrekte Software. So sollte es zumindest sein. Das ist die Erwartung des
Auftraggebers. Doch so einfach ist es nicht…


---


<!-- Page 29 of 584 -->


Einleitung 20
Überlege selbst, welche der obigen (oder auch weiteren) Maßnahmen in
deinemTeamverlässlichgetroffenwerden,umhoheKorrektheitzuliefern
und zu erhalten.
Fehlender Wert
Aberwas,wenndieSoftwareentwicklungnichtweiß,waszutunist?Was,
wenn Unklarheit herrscht? Die Voraussetzung dafür, “die Dinge richtig zu
tun” ist, dass man überhaupt “die richtigen Dinge tut”. So wird landläufig
Effektivität beschrieben. Effektivität kann es nur geben, wenn Klarheit
herrscht.
SolangedieSoftwareentwicklungaberimUnklarendarüberist,wasgenau
die Verhaltensanforderung ist oder solange der Auftraggeber selbst sich
noch nicht ganz klar darüber ist, wie für ihn hohe Verhaltensqualität
aussieht, kann Codeproduktion nicht effektiv sein. Und ohne Effektivität
keine Produktivität.
Leider ist das der natürliche Zustand von Softwareprojekten:
• Der Auftraggeber hat eine nur unvollständige Vorstellung davon,
was er braucht.
• Der Auftraggeber kann seine Vorstellungen nur unvollständig for-
mulieren.
• Die Softwareentwicklung versteht die formulierten Anforderungen
nur unvollständig.
• Die Softwareentwicklung setzt ihr Verständnis der Anforderungen
nur unvollständig um.
• Der Auftraggeber hat in der Zeit von der Spezifikation bis zur
Abnahme ihrer Umsetzung⁷ seine Meinung geändert; seine Anfor-
derungen sehen nun anders aus. Selbst eine korrekte Umsetzung
⁷Der Begriff Spezifikation mag sich für dich hier schwergewichtig anhören. Wo bleibt
da die Agilität? Aber ich meine ihn ganz neutral. Er soll einfach nur ausdrücken, dass
ein Auftraggeber in unmissverständlicher Weise irgendwie beschrieben hat, welche Ver-
haltensanforderungen der Code, den du entwickelst, erfüllen soll. “Irgendwie” bedeutet,
dass ich nicht suggerieren will, in welcher Sprache, mit welchem Medium, in welchem
Umfang eine Spezifikation vorliegt. Ebensowenig will ich mitschwingen lassen, wie häufig
der Auftraggeber eine Spezifikation vorlegt oder ihre Umsetzung prüfen will; das kann alle
paar Wochen sein oder jeden Tag. Iterativ-inkrementelles Vorgehen ist für mich mit dem
Begriffalsoabsolutvereinbar.


---


<!-- Page 30 of 584 -->


Einleitung 21
derursprünglichenSpezifikationpasstdahernurunvollständigzum
neuen Stand der Bedürfnisse des Auftraggebers.
Das ist die Erkenntnis der Agilität in der 1990ern gewesen, die zur Min-
destforderungeinesiterativ-inkrementellenSoftwareentwicklungspro-
zesses geführt hat.
Als Produktivitätskiller hatte sich herausgestellt, dass immer wieder über-
raschend bei der Abnahme von Software nicht der erwartete Wert ge-
liefert wurde. Selbst spezifikationsgemäße Lieferung hatte nicht die im
praktischen Einsatz erforderlichen Nutzen.⁸
Das Missverständnis von Auftraggebern und Softwareentwicklung bis in
die 1990er war (und ist leider auch heute noch in einigen Projekten), dass
Verhaltensanforderungen sich in einem mehr oder weniger länglichen
Prozess einmalig vor Beginn der Umsetzung festzurren lassen könnten
(Stichwort “Wasserfall”).
Diese Vorstellung hat zu Spezifikationen geführt, die große, unvermutete
Missweisungen enthielten, die in Software gegossen große negative Über-
raschungen ausgelöst haben. Umfangreiche Nacharbeiten waren nötig,
nicht wegen Inkorrektheit, sondern wegen Wertlosigkeit. Auch korrekt
implementierte Spezifikationen haben zum Lieferzeitpunkt nichts oder zu
wenig genützt.
Dem hat die Agilität eine Desillusionierung entgegen gesetzt. Nicht noch
bessere, umfangreichere, längere Anforderungsanalyse soll die Produk-
tivität steigern, sondern das Gegenteil: eine radikale Verkürzung bei
gleichzeitiger Vervielfachung von Analyse, Spezifikation und Umsetzung.
In der Agilität gibt es weiterhin eine Spezifikation und insofern eine
Erwartung an hohe Korrektheit (Stichwort “Definition of Done”). Doch
es wird nicht mehr angenommen, dass diese Spezifikation schon “die
letzte Wahrheit” sei. Stattdessen soll die Softwareentwicklung bestrebt
sein, nur schmale Ausschnitte eines Gesamtverhaltens zu spezifizieren
(auch Inkremente genannt), die zügig umgesetzt werden können, um
⁸WertistalsonichteinfachgleichhochqualitativeSoftware.ZumWertgehörtnatürlich,
dassSoftwarehoheQualitäthat,d.h.derSpezifikationmöglichstgenauentspricht.Darüber
hinaus muss diese hohe Qualität allerdings auch noch nützlich sein in dem Moment, wo
siegeliefertwird.Darausergibtsich,dassQualitätsproduktionundWertproduktionzweizu
unterscheidendeProzessebraucht.FürErsterenbistdualsSoftwareentwicklerzuständig,für
Letzerenz.B.inScrumaberderProductOwner!


---


<!-- Page 31 of 584 -->


Einleitung 22
vom Auftraggeber Feedback zu bekommen. Wert kann man sich nur
schrittweise annähern, nicht, weil Auftraggeber oder Softwareentwick-
lung inkompetent sind, sondern weil es in der Natur der Sache komplexer
Anforderungenliegt;daistkeingeradlinigerWegzuhohemWertsichtbar.
Manbekämpftbeimiterativ-inkrementellenVorgehendieIneffektivi-
tät dadurch, dass man ihr den Zahn der Überraschung zieht.Denn nur
die Überraschung macht aus mangelndem Wert frustrierende Nacharbeit.
Ist mangelnder Wert jedoch zu erwarten, ja, geradezu die Norm, dann
ist die nächste Iteration keine Nacharbeit, keine Verschwendung, sondern
ein erwartetes Inkrement und insofern produktiv - auch wenn man gern
schneller vorangehen würde.
Softwareentwicklung wie Auftraggeber hegen beim agilem Vorgehen
nicht mehr den Glauben, dass wertvolle Software “in einem Rutsch”
entstehen kann. Vielmehr muss man sich hohem Wert experimentierend
mit hochqualitativen Inkrementen annähern. Das ist keine Last, das ist
eine Tugend, weil unvermeidbar.
Wie steht es mit diesem Verständnis in deinem Team? Geht ihr iterativ-
inkrementell vor? Versteht der Auftraggeber die Vorläufigkeit seiner An-
forderungen und eurer Lösungen?
Fehlende Ordnung
Auch wenn fehlende Korrektheit der naheliegende und greifbare Produk-
tivitätskillerist,gingihmgeschichtlichfehlenderWertinderBewusstwer-
dung der Softwareentwicklung voraus, denke ich.
Nicht genau zu wissen, was der Auftraggeber wirklich will, was für ihn
Wert darstellt, für das Geld, das er auszugeben bereit ist, war zunächst
ein größeres Problem. Erst als eine Verbesserung des Vorgehensmodells in
den 1990ern hier mehr Klarheit gebracht hatte und dadurch die Zahl der
Softwarelieferungen zur Feedback-Generierung, die potenziell inkorrekt
sein konnten, gestiegen war, trat der Produktivitätskiller Inkorrektheit
deutlich(er) zutage. Beleg ist aus meiner Sicht dafür die späte Erfindung
automatisierter Tests. Erst Ende der 1990er bekam das Thema breite
Sichtbarkeit.
Wenn man weiß, was das Richtige ist (Wert), lohnt es, das auch richtig zu
tun (Korrektheit). Wenn man es kann.


---


<!-- Page 32 of 584 -->


Einleitung 23
UnddastecktschließlichderdritteProduktivitätskiller,denichdirvorstel-
len möchte: die Unordnung. Solange du nicht bewusst darauf achtest,
OrdnungimCodeherzustellen,hastduesimmerschwer,dasRichtige
auch richtig zu tun.
Für langfristig hohe Produktivität muss das Richtige or-
dentlich richtig getan werden.
Code, der sich mit jedem neuen Feature, mit jedem Bug Fix weniger leicht
verändern lässt, wird zum Morast, in dem deine Softwareentwicklung
alsbald steckenbleibt. Oder wenn nicht steckenbleibt, dann zumindest
nur noch schwerfällig vorankommt. Das ist nicht, was Auftraggeber sich
wünschen.
CodeisteineRessource,mitundanderSoftwareentwicklungarbeitet.
Wie andere Ressourcen kann sie pfleglich behandelt werden - oder
man treibt an ihr Raubbau. Ohne weitere Maßnahmen geschieht Letzte-
res.
Für den Auftraggeber sind Inkorrektheit und Wertarmut von Code noch
vergleichsweise leicht zu spüren. Beide zeigen sich als mangelnde Quali-
täten im Verhalten.
Unordnung jedoch entzieht sich der direkten und zeitnahen Wahrneh-
mung des Auftraggebers. Deshalb hat sie Gelegenheit, sich hinter der
Fassade des Verhaltens aufzubauen. Wenn sie dann indirekt über deutlich
sinkende Produktivität auch für den Auftraggeber spürbar wird, ist es
jedoch eigentlich schon zu spät. Deshalb musst du ständig ein Auge auf
die Ordnung haben!
Wenn du die Ordnung zu lange hast schleifen lassen, sind die nöti-
gen “Aufräumarbeiten” meist zu umfangreich, als dass sie sich rechnen
würden. Und sie ließen sich auch kaum dem Kunden gegenüber ver-
heimlichen. Also schleppt sich die Softwareentwicklung weiter durch
den selbst verschuldeten Sumpf. Denn selbst verschuldet ist er, da der
Kunde sich Unordnung nicht gewünscht hat. Sie ist mangels Bewusstsein
und/odermangelsFähigkeitund/oderwiderbesserenWissens“aufBefehl”
(Ignoranz)und/oderinnaivemGlaubenanbaldigeKorrektur(sogenannte
Technische Schuld) entstanden.


---


<!-- Page 33 of 584 -->


Einleitung 24
Nicht, dass fehlende Ordnung eine neue Ursache für Produktivitäsabnah-
me wäre. Sie wurde schon in den 1960ern oder gar früher identifiziert.
Auch die Strukturierte Programmierung (structured programming⁹) ist
aus dieser Erkenntnis entstanden. Man könnte wohl auch sagen, dass
Objektorientierung von ihr ursprünglich inspiriert war. Ebenso das struc-
tured design¹⁰ und der Begriff des Moduls.
Wer mit Code zu tun hat, erwartet, ordentlichen Code vorzufinden,
d.h. Code, der nicht unnötig behindert, ihn zu verstehen (“easy to
reason about”), und der nicht unnötig behindert, ihn zu verändern.
Denn darum geht es letztlich ja immer: Code wird nur betrachtet, um ihn
neuen Anforderungen anzupassen oder zu korrigieren. Dass du Code aus
SpaßamprasselndenKaminfeuerstudierst,passiertwahrscheinlichselten,
oder?
Nach Jahrzehnten des mehr oder weniger latenten Bewusstseins der
Branche, dass Ordnung eine Qualität ist, auf die es ebenfalls zu achten
giltbeiderSoftwareentwicklung,hatdannimJahr2008derBegriff Clean
Code dem Thema neue Sichtbarkeit und Konkretheit gegeben.
Dass Robert C. Martin von sauberem Code und nicht von ordentlichem
spricht, mag dem von Martin Fowler im Zusammenhang mit dessen Buch
Refactoring geprägten Begriff code smell geschuldet sein. Was sauber ist,
riecht nicht.
DochletztlichistSauberkeitalsBildzuschwachfürdienötigeEigenschaft,
die Code haben muss, um deine Softwareentwicklung nicht schwerfällig
zu machen. Was sauber ist, kann immer noch unordentlich, d.h. unüber-
schaubar bis zu Unbrauchbarkeit sein.
Wenn du dir jetzt allerdings Ordnung vorstellst, denkst du sehr wahr-
scheinlich nicht nur an Sauberkeit als Selbstzweck, sondern auch noch
an Eignung für weitere Nutzung. Sauberkeit schützt vor Schaden.
Ordnung hat als Zweck Befähigung!
⁹https://en.wikipedia.org/wiki/Structured_programming
¹⁰https://www.amazon.de/Structured-Design-Fundamentals-Discipline-Programme/
dp/0138544719


---


<!-- Page 34 of 584 -->


Einleitung 25
Und genau darum geht es, wenn ich hier von ordentlichem Code, von
Ordnung im Code spreche. Code soll ordentlich sein, um zu zügiger
Veränderung zu befähigen.
Zusammenfassung
Auftraggeber wollen Software, die umfassend tut, was sie tun soll; sie soll
funktional und effizient sein. Diese Qualitäten sollst du in der Software-
entwicklung stets zügig liefern; du sollst produktiv sein und bleiben.
UnglücklicherweiseistschondieHerstellungvonfunktionalemundeffizi-
entem Code eine Sache, die sehr komplex ist. Ich denke, davon kannst du
ein Lied singen. Sich mit all den Technologien und Produkten und Ansät-
zen auszukennen, die zur Herstellung von funktionalem und effizientem
Code zur Verfügung stehen, ist eine Kunst für sich.
Und nun soll die Herstellung von Code, der hochqualitatives Verhalten
zeigt, auch noch stets zügig stattfinden, obwohl dieser Code ständigen
Änderungen unterliegt und die Anforderungen an ihn notorisch unklar
sind? Das steigert die Komplexität der Softwareentwicklung erheblich!
Wie es für die Herstellung von Verhaltensanforderungen Werkzeuge gibt,
so gibt es zum Glück aber auch Werkzeuge, die dir helfen, hohe Produkti-
vität zu produzieren.
• Agilität
• Automatisierte Tests
• Prinzipien und Praktiken des Clean Code Development


---


<!-- Page 35 of 584 -->


Einleitung 26
VoraussetzungenfürProduktivität
Du musst diese Werkzeuge kennen und auch einsetzen. Sie sind nicht neu,
sie sind womöglich noch nicht einmal schwierig zu beherrschen - doch
sie haben eines gemeinsam: sie gehen ans Eingemachte. Damit du sie
konsequent benutzt, musst du eine passende Grundhaltung entwickeln;
die Kultur der Softwareentwicklung in deinem Team und darüber hinaus
muss darauf ausgerichtet sein. Das braucht Zeit.
Die Agilität hat es inszwischen geschafft, breit ins Bewusstsein (oder
zumindest auf die Lippen) der Branche zu dringen. Auf die eine oder an-
dere Weise wird also in vielen Softwareentwicklungsteams versucht, die
Wertproduktion hoch zu halten durch iterativ-inkrementelles Vorgehen.
Mit der Korrektheit und der Ordnung hingegen, steht es weniger gut. Das
liegt daran, dass das eine vom anderen abhängig ist: ohne Ordnung ist es
schwer, Korrektheit zuverlässig und nachvollziehbar herzustellen und zu
überprüfen. Aber gerade die Ordnung hat es in sich. Nicht umsonst ist sie
geschichtlich der letzte Produktivitätskiller, für den breites Bewusstsein
geschaffen werden musste.
So verständlich es war, dass der Fokus von der Steigerung der Produk-
tivität in Bezug auf den Wert von Software (in den 1990er Jahren) zur
Steigerung der Produktivität durch Erhöhung der Korrektheit (in den


---


<!-- Page 36 of 584 -->


Einleitung 27
2000er Jahren) gewandert ist - so ist es andererseits auch verständlich,
dass die Produktivitätssteigerung dann gegen eine gläserne Decke stoßen
musste.ErstdurcheinenweiterenWechseldesFokushinzurOrdnung(in
den 2010er Jahren) kann nämlich die Behinderung aus dem Weg geräumt
werden, die mehr Korrektheit und auch zügigerer Wertherstellung im
Wege stand.
Dauerhaft hohe Produktivität braucht…
• eine Organisation, die ihr höchste Priorität zuweist, um langfristig
wettbewerbsfähig zu bleiben,
• ein Verständnis dafür, was Ordnung im Code bedeutet, wie er stets
wandlungsfähig gehalten werden kann,
• den Willen zur Produktion von stabil korrektem Code, um die
Kapazität für die Erweiterung von Code maximal zu halten,
• den Mut, nur auf der Basis von unzweideutigen Spezifikationen
Code zu produzieren
• und schließlich die Einsicht, dass Unklarheit und Volatilität ständi-
ge Begleiter der Softwareentwicklung sein werden, so dass Vorläu-
figkeit auf allen Ebenen akzeptiert werden muss.
Leider ist es in der Softwareentwicklung so, wie es der Buddha für das
Leben konstatiert hat:
“Frische Milch braucht Zeit zum Sauerwerden, / Unheilsames
Handeln braucht Zeit zum Reifen, / So schwelen im Toren die
Folgen seines Handelns, / Wie unter der Asche verborgene
glühende Kohlen.”, Dhammapada - Die Weisheitslehren des
Buddha, Munish B. Schiekel
Die negativen Auswirkungen deines heutigen Handelns zeigen sich nicht
immer sofort. Sie wachsen unsichtbar und schleichend an – bis du sie
irgendwann und oft zu spät deutlich spürst.
Deshalb ist es wichtig, die Produktivität als im Grunde höchstes Gut,
als wichtigste Anforderung zu verstehen und die Softwareentwick-
lung dahingehend zu organisieren. Das ist nachhaltige Softwareent-
wicklung. Zuerst und unverbrüchlich soll Produktivität geliefert werden,
dann erst Funktionalität, dann Effizienz.


---


<!-- Page 37 of 584 -->


Einleitung 28
Maßnahmen zur korrekten Wertproduktion in Ordnung müssen einen
Rahmen aufspannen, in dem konkrete funktionale und nicht-funktionale
Anforderungen umgesetzt werden. Derzeit geschieht es vielfach noch
umgekehrt: Verhaltensanforderungen werden “irgendwie” realisiert und
insbesondere Korrektheit und Ordnung sind nachrangig.
Alles, was ich dir im Folgenden präsentiere, darfst du vor diesem Hinter-
grundverstehen.IchmöchtedireinmethodischesRahmenwerkvorstellen,
mit dem du systematisch für höhere Korrektheit und Ordnung in deinem
Code sorgen kannst. Mich treibt die eigene leidvolle Erfahrung an, dass
darauf einfach zu wenig und zu spät geachtet wird. Mir ist das früher
auch oft passiert - weil ich es nicht besser wusste. Dir möchte ich diese
Erfahrungersparen.DirmöchteicheineGuidelineandieHandgeben,mit
der du während der Codierung deinen Weg zur Korrektheit und Ordnung
findest.KeineAngstmehrvordemblinkendenCursor,derdichauffordert,
vor allem Funktionalität zu produzieren. Mit ein bisschen System, gutem
Willen und Übung wirst du es schaffen, Funktionalität und dauherhaft
hohe (oder zumindest höhere) Produktivität herzustellen.


---


<!-- Page 38 of 584 -->


Die Methode


---


<!-- Page 39 of 584 -->


01 - Die Anforderung-Logik
Lücke
Um die Softwareentwicklung vom Kopf auf die Füße zu stellen, d.h. ihr
einen Rahmen für Nachhaltigkeit zu geben, ist es hilfreich, wenn wir ihr
Produkt genauer betrachten. Woraus bestehen “die Maschinen”, die du in
der Softwareentwicklung produzierst, von denen sich der Auftraggeber so
viel Hilfe verspricht?
Logik - Der Stoff aus dem Verhalten
entsteht
Die offensichtlichen Anforderungen des Auftraggebers sind die Verhal-
tensanforderungen an Software. Verhalten wird durch Code hergestellt -
aber nicht der gesamte Code ist dafür verantwortlich.
Hier als Beispiel eine Software, die eine Datei als Hex Dump ausgeben soll
wie in diesem Bild dargestellt (Quelle: C# von Kopf bis Fuß¹¹):
¹¹https://www.amazon.de/gp/product/B06XDVW33W


---


<!-- Page 40 of 584 -->


01-DieAnforderung-LogikLücke 31
Der C#-Code dafür sieht im Ausschnitt so aus:
1 using System;
2 using System.IO;
3 using System.Text;
4
5 namespace hexdump
6 {
7 // source: "C# von Kopf bis Fuß"
8 class MainClass
9 {
10 public static void Main (string[] args)
11 {
12 if (args.Length != 1) {
13 Console.Error.WriteLine ("Usage: hexdump <dateiname>");
14 Environment.Exit (1);
15 }
16
17 if (!File.Exists(args[0])) {
18 Console.Error.WriteLine("No such file: {0}", args[0]);
19 Environment.Exit(2);
20 }
21
22 using (var input = File.OpenRead (args [0])) {
23 int position = 0;
24 var buffer = new byte[16];
25
26 while (position < input.Length) {
27 var charsRead = input.Read (buffer, 0, buffer.Length);
28 if (charsRead > 0) {
29 Console.Write ("{0}: ", string.Format ("{0:x4}", position));
30 position += charsRead;
31
32 for (int i = 0; i < 16; i++) {
33 if (i < charsRead) {
34 var hex = string.Format ("{0:x2}", buffer [i]);
35 Console.Write (hex + " ");
36 } else {
37 Console.Write (" ");
38 }
39 ...
Erkennst du, welche Zeilen des Code verhaltensrelevant sind? Die Verän-
derung welcher Zeilen würde für einen Anwender unmittelbar spürbar


---


<!-- Page 41 of 584 -->


01-DieAnforderung-LogikLücke 32
sein?
Könnte using System gelöscht werden, ohne dass sich das Programm-
verhalten ändert?¹² Nein, das Programmverhalten würde sich nicht än-
dern.
Sind die Leerzeilen oder der Kommentar relevant für das Programmver-
halten? Nein.
Spürt ein Anwender, ob es die Funktion Main() gibt? Nein.¹³
Aber wenn eine Zeile mit Console.Error.WriteLine(...) fehlen
würde, dann würde der Anwender das (in manchen Fällen) bemerken.
OderwenndieZeileif (i < charsRead)fehlenwürdeoderdarindas
< durch ein > ersetzt würde, dann würde das zu einem anderen Verhalten
des Programms führen.
Code ist also nicht gleich Code. Mancher Code/manche Codezeilen sind
für das Verhalten relevant, manche nicht.
Die für das Verhalten relevanten Codezeilen stellen die
Logik von Software dar.¹⁴
Logik besteht aus
• Transformationen/Operatoren, z.B. <, ++, args.Length
• Kontrollstrukturen, z.B. if-else, for, try-catch
• I/O-bzw.allgemeinerAPI-Calls,z.B.Console.Write(),File.OpenRead()
¹²Vorausgesetzt die dadurch syntaktischen/semantischen Probleme im Quellcode wür-
dendurchweitereEingriffekompensiert.
¹³Dass Main() in C# nötig ist, um ein Programm ausführbar zu machen, ist unwe-
sentlich. In anderen Programmiersprachen sind keine Klassen wie MainClass und keine
MethodewieMain()nötig,umeinProgramm(übersetzenund)laufenzulassen.
¹⁴So nenne ich diesen Teil des Code jedenfalls im Weiteren, weil ich keinen anderen
Namendafürkenne.Wenndueinenbesserenweißtodereinenschonetablierten,dannlass
ihnmichwissen.Statementsfindeichzuwenig,weildamitimGrundeallesgemeintist,was
in C# (und anderen Sprachen) mit einem ; abgeschlossen wird. Dazu gehört, wie du bald
lesenwirst,aberauchCode,derkeineLogikist.


---


<!-- Page 42 of 584 -->


01-DieAnforderung-LogikLücke 33
Wenn nun das für Auftraggeber so wichtige Verhalten - Funktionalität
+ Effizienz - nur durch Logik hergestellt wird, stellt sich die Frage, was
der übrige Code für Zweck hat. Welche Anforderungen hilft er erfüllen?
Warum solltest du irgendetwas anderes codieren als Logik?
Nicht-Logik Code dient der Herstellung von Produktivität.
Einige Beispiele:
• Namespaces reduzieren das Rauschen im Code, das lange Namen
mit redundanten Anteilen verursachen. Sie erhöhen die Ordnung.
• Leerzeilen strukturieren den Code vertikal, indem sie unterschied-
liche inhaltliche Kohäsion anzeigen. Sie erhöhen die Ordnung.
• Funktionen “komponieren” Logik zu Funktionseinheiten, die As-
pekte eines Verhaltens unter einem Namen zusammenfassen. Sie
erhöhen die Ordnung und die Testbarkeit.
• Klassen aggregieren Funktionen (und Daten) und stellen damit
zweckvolle Einheiten zusammen. Sie erhöhen die Ordnung.
Funktionalität
Die erste Kunst bei der Herstellung (oder Entwicklung) von Logik ist,
sie so zu wählen, dass sie die gewünschte Funktionalität hat. Das lernst
du auf alle Fälle in jedem Buch einer Programmiersprache oder einem
Programmierkurs.
Logik, die die Zahlen in einem Array summiert, sieht dann z.B. so aus:
1 static int Sum(int[] numbers) {
2 var sum = 0;
3 foreach(var n in numbers)
4 sum += n;
5 return sum;
6 }
Logik, die die Zahlen in einem Array sortiert, sieht hingegen z.B. so aus:


---


<!-- Page 43 of 584 -->


01-DieAnforderung-LogikLücke 34
1 // Quelle: https://www.geeksforgeeks.org/bubble-sort/
2 static void BubbleSort(int []arr)
3 {
4 int n = arr.Length;
5 for (int i = 0; i < n - 1; i++)
6 for (int j = 0; j < n - i - 1; j++)
7 if (arr[j] > arr[j + 1])
8 {
9 int temp = arr[j];
10 arr[j] = arr[j + 1];
11 arr[j + 1] = temp;
12 }
13 }
Welche Logik-Bausteine du aus den von deiner Programmiersprachen,
deinen Bibliotheken und Frameworks angebotenen auswählst und wie du
sieinBeziehungsetzt,machtdenUnterschied,obdaseineoderdasandere
Verhalten entsteht.
Auch Code, der nur aus Logik besteht, hat insofern eine Struktur. Im
BubbleSort-Beispiel ist die augenfällig durch die Schachtelung der Kon-
trollstrukturen.
Effizienz I - Effizienz durch Algorithmen und
Datenstrukturen
Logik so zu strukturieren, dass sie die gewünschte Funktionalität hat,
ist jedoch nicht alles. Sie soll auch z.B. performant sein. Logik über die
Funktionalität hinaus auch noch mit Effizienzen auszustatten, ist die
zweite Kunst, die du lernen musst, wenn du programmieren willst.
HiereinBeispieldafür,wieandersLogikaussehenkann,nurweilsiemehr
Effizienz bieten soll. Bubblesort ist ein bekanntermaßen imperformanter
Sortieralgorithmus. Radixsort soll diesen Makel beseitigen:¹⁵
¹⁵Die Funktionalität ist dieselbe, die Logik-Struktur ist aber eine völlig andere, weil an-
dereEffizenzanforderungenerfülltwerden.Docheskommtnochschlimmer:Sogardieselbe
Funktionalität mit denselben Effizienzanforderungen kann zu sehr unterschiedlicher Logik
führen. Unter anderem das macht es dir so schwierig, aus Logik herauszulesen, welches
Verhaltensieeigentlicherzeugt.


---


<!-- Page 44 of 584 -->


01-DieAnforderung-LogikLücke 35
1 // Quelle: https://www.geeksforgeeks.org/radix-sort/
2 static void Radixsort(int[] arr, int n)
3 {
4 int mx = arr[0];
5 for (int i = 1; i < n; i++)
6 if (arr[i] > mx)
7 mx = arr[i];
8
9 for (int exp = 1; mx/exp > 0; exp *= 10)
10 {
11 int[] output = new int[n];
12
13 int i;
14 int[] count = new int[10];
15
16 for(i = 0; i < 10; i++)
17 count[i] = 0;
18
19 for (i = 0; i < n; i++)
20 count[ (arr[i]/exp)%10 ]++;
21
22 for (i = 1; i < 10; i++)
23 count[i] += count[i - 1];
24
25 for (i = n - 1; i >= 0; i--)
26 {
27 output[count[ (arr[i]/exp)%10 ] - 1] = arr[i];
28 count[ (arr[i]/exp)%10 ]--;
29 }
30
31 for (i = 0; i < n; i++)
32 arr[i] = output[i];
33 }
34 }
Logik (und zugehörige Datenstrukturen) für Effizienz-Anforderungen
passend zu wählen, erfordert also mehr als die Kenntnis von Logik-
Bausteinen. Dass du dir z.B. der algorithmischen Komplexität¹⁶ deiner
Logik bewusst bist, gehört dazu, wenn du mit Logik den Auftraggeber
umfassend erfreuen willst. Es kommt auf die Auswahl und Zusammen-
stellung der Logik-Bausteine an, auf ihre Komposition.
Effizienz II - Effizienz durch Verteilung
PerformanceundSkalierbarkeitoderauchandereEffizienzanforderungen
lassen sich allerdings nicht immer allein durch Auswahl und Anordnug
von Logik erfüllen. Dann ist zusätzlich Verteilung gefragt, d.h. die Aus-
führung von Logik verteilt auf mehrere Threads.
Als simples Beispiel mag die Sortierung von zwei Arrays dienen. Eine
Lösung nur mit Logik kann das auch mit dem schnelleren Algorithmus
nur sequenziell bewerkstelligen:
¹⁶https://www.bigocheatsheet.com/


---


<!-- Page 45 of 584 -->


01-DieAnforderung-LogikLücke 36
1 Radixsort(arr1, arr1.Length);
2 Radixsort(arr2, arr2.Length);
Die Gesamtlaufzeit ist dann die Summe der Laufzeiten der einzelnen
Aufrufe der Funktion, die die Sortierlogik kapselt.
Wenn die Sortierung jedoch parallel, d.h. auf zwei Threads (verschiedener
Prozessorkerne) stattfinden kann…
1 var t1 = Task.Factory.StartNew(() => Radixsort(arr1, arr1.Length));
2 var t2 = Task.Factory.StartNew(() => Radixsort(arr2, arr2.Length));
3 Task.WaitAll(new[] {t1, t2});
…dannentsprichtdieGesamtlaufzeit(ungefähr)nurderdesFunktionsauf-
rufs, der länger gebraucht hat.
Logik mit mehr Effizienz auszustatten durch Verteilung ist traditionell ein
Teil der Disziplin Softwarearchitektur. Sie kannst du als die dritte Kunst
der Softwareentwicklung ansehen.
Hierarchie der Hosts
Softwarearchitektur verteilt Logik, indem sie sie in Hosts ausführt. So
nenne ich geschachtelte Laufzeit-Kontexte/Container, die mit mehr oder
weniger Infrastruktur aufgesetzt, betrieben und in Verbindung gebracht
werden.
• Thread: Multithreading ist der erste Schritt, um Latenz zu ver-
bergen oder zu verringern oder den Durchsatz zu erhöhen. Die
Kommunikation schon zwischen Logik auf verschiedenen Threads
ist aber nicht mehr direkt, d.h. langsamer als die zwischen Logik
auf demselben Thread. Vorsicht ist geboten, wenn Threads auf die
selben Daten zugreifen.
• Process: Logik parallel in verschiedenen Betriebssystemprozessen
zu betreiben, entkoppelt sie stärker, was zur Robustheit beiträgt.
Dass es keinen gemeinsamen Hauptspeicher mehr gibt, reduziert
das Risiko von Fehlern. Allerdings ist die Kommunikation deutlich
aufwändiger zwischen Prozessen.


---


<!-- Page 46 of 584 -->


01-DieAnforderung-LogikLücke 37
• Machine: Logik in mehreren Threads verteilt auf mehrere Prozesse
auf verschiedenen (physischen oder virtuellen) Maschinen auszu-
führen, ermöglicht ein scale-out oder auch die Ansiedelung von
Logik näher an Ressourcen. Allerdings ist die Kommunikation zwi-
schen Maschinen noch langsamer als zwischen Prozessen, so dass
sehr auf Häufigkeit und Granularität der Nachrichtenübermittlung
geachtet werden muss.
• Network: Logik auf Maschinen in verschiedenen Netzwerken zu
verteilen, ist allemal unvermeidbar, wenn Speicher- und Prozessor-
ressourcen flexibel genutzt werden sollen (Stichwort “Cloud Com-
puting”). Der Nutzen bei der Skalierbarkeit ist mit den Gefahren
für die Sicherheit abzuwägen. Und die Kommunikationsgeschwin-
digkeit sinkt abermals.
Effizienz durch Verteilung steigern zu müssen, ist oft unvermeidbar.
Simpel ist das jedoch nicht. Die Zahl der hilfreichen Technologien nimmt
jeden Tag zu und erfordert von dir ein fleißiges Studium, wenn du mithal-
ten willst. Vorsicht ist dennoch weiterhin ganz grundsätzlich gegenüber
den fallacies of distributed computing¹⁷ geboten.
Im Weiteren spielen Hosts als Container für Logik jedoch keine größere
Rolle mehr. Die Darstellungen hier drehen sich nicht um die Herstellung
von Effizienzen, sondern vor allem um die Qualitäten Wert, Korrektheit
und Ordnung für die Anforderung Produktivität. Du wirst es mit Struk-
turen zu tun bekommen, aber nur vergleichsweise wenigen Strukturen
bestehend aus mehreren Hosts.
Zusammenfassung
Logik und ihre Verteilung ist das, was für den Auftraggeber unmittelbar
spürbar ist. Mit Logik und Verteilung Verhalten herzustellen, sind die
grundlegenden Künste der Programmierung. In ihnen können Software-
entwickelnde ständig reifen; für sie werden ständig neue Paradigmen,
Technologien und Produkte entwickelt.
Logik und Verteilung in hoher Qualität herzustellen, ist auch bei guten
Spezifikationen ein komplexes Unterfangen. Umso naheliegender sollte es
sein, dass du diese Transformation systematisch betreibst.
¹⁷https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing


---


<!-- Page 47 of 584 -->


01-DieAnforderung-LogikLücke 38
Von den Anforderungen zur Logik
Angesichts des großen, bewussten und verständlichen Bedarfs an Soft-
wareverhalten, den Auftraggeber haben, ist es kein Wunder, dass sie
großen Druck auf die Logik-Produktion ausüben. Du sollst möglichst
schnell Features mit Logik umsetzen - alles andere ist dem Kunden wenn
schonnichtegal,danndochmeistensnurwenigbewusst.Aufallesandere
achtet er insofern wenig oder kann es sogar nicht einmal beurteilen.
Logik schwer definierbar
Doch leider “ergibt sich” Logik nicht “einfach so”. Sie liegt nicht auf der
Hand.FunktionaleundeffizienteLogikzufinden,istfürdichauchmitviel
Erfahrung eine komplexe Angelegenheit. Schon eine sehr simple Aufgabe
macht das deutlich:
Iteration 1: Hello, World!
SchreibeeinProgramm,dassaufderConsole“Hello,World!”ausgibt.
Das Ergebnis soll von der Ausgabe her so aussehen:
EineBeispielausgabealsSpezifikation
Welche Logik ist dafür nötig?
Diese Frage wirst du für deine Programmiersprache sicher aus dem Stand
beantworten können. In C# sieht sie so aus:¹⁸
¹⁸Für weitere 599 Programmiersprachen kannst du dir hier die Antworten anschauen.
AberAchtung:VieleenthaltennichtnurLogik,sondernauchsprachnotwendiges“Rauschen”
drumherum.


---


<!-- Page 48 of 584 -->


01-DieAnforderung-LogikLücke 39
1 Console.WriteLine("Hello, World!");
Das Programm selbst ist umfangreicher, weil noch eine Klasse und eine
Funktion “als Verpackung” erforderlich sind, aber die reine Logik ist so
trivial.
Auf zur nächsten Iteration:
Iteration 2: Persönliche Begrüßung
Das Programm aus Iteration 1 soll erweitert werden. Der Auftragge-
ber sagt dir:
“Bitte bauen Sie das Programm so um, dass User dem Programm
ihren Namen mitteilen, um damit persönlich begrüßt zu werden.
AnwenderinJaninewirdnichtmehrmit“Hello,World!”,sondernmit
“Hello, Janine!” begrüßt. Kriegen Sie das hin?”
Welche Logik brauchst du dafür?
Auch diese Frage wirst du wahrscheinlich aus dem Stand beantworten
können,wennauchvielleichtmiteinwenigUnsicherheit,wofürsolchein-
fache Problemstellungen gut sein sollen. Ein Verhalten wie das Folgende
zu erzeugen, ist nun wirklich kein Hexenwerk:
Natürlich ist das keine große Herausforderung an deine Kunst, Logik für
Funktionalität zu finden.
Aber was, wenn dieses Verhalten nicht den Qualitätsanforderungen in
puncto Benutzbarkeit entspricht? Das stellt der Auftraggeber fest, wenn
du ihm deine neue Lösung vorstellst. Eine Anwenderin kann zwar dem
Programm den Namen “mitteilen”, muss dazu aber wissen, dass das auf
der Kommandozeile zu geschehen hat. Das hatte der Auftraggeber nicht
im Sinn mit seiner obigen Spezifikation; wie selbstverständlich hatte er


---


<!-- Page 49 of 584 -->


01-DieAnforderung-LogikLücke 40
gedacht,dasseineAnwenderinnatürlichnachihremNamengefragt wird,
um ihn dann mitzuteilen.¹⁹
“Gedacht” hatte sich der Auftraggeber ein solches Verhalten:
DaspasstgenausozurverbalenSpezifikation.DieLogikdafürsiehtjedoch
ganz anders aus als für die erste Implementation!
1 // Variante 1
2 Console.WriteLine("Hello, {0}!", args[0]);
3
4 // Variante 2
5 Console.Write("Name: ");
6 var name = Console.ReadLine();
7 Console.WriteLine($"Hello, {name}!");
Und damit ist die Lösung immer noch nicht in trockenen Tüchern! Denn
wasgeschieht,wenneinAnwenderkeinenNameneingibtundnurENTER
drückt? Dann passiert dies bei Variante 2:
Ist das ein erwünschtes Verhalten aus Sicht des Auftraggebers? Nein.
Der hatte sich bei der Formulierung “mitteilen … kann” gedacht, dass
ohne Name weiterhin mit “Hello, World!” begrüßt wird. Es gilt aller-
dings: “Gedacht ist nicht gemacht!” Auftraggeber müssen mehr, als sich
Anforderungen denken oder darauf vertrauen, dass du “als Fachmann”
schon weißt, was gemeint sein könnte. Sieh durch den Honig durch,
den dir solche Formulierungen um den Bart schmieren: “Sie haben doch
Erfahrung. Sie wissen doch, wie man das macht und was ich meine.” Nein,
¹⁹Ichhabedichhiereinwenighereingelegt.IndererstenIterationwardieBildschirmaus-
gabe die Spezifikation. In der zweiten eine rein verbale, auf die ich sofort einen Screenshot
habefolgenlassen.Derhatdirvielleichtsuggeriert,dassdasdarinzusehendeVerhaltendas
spezifizierteist.Abermitnichten!EswarschoneineInterpretationderverbalenSpezifikation.
Du siehst, es ist so eine Sache mit den Anforderungen. Welche gelten, wann liegen sie vor,
welcheFormsolltensiehaben,damitduihnenvertrauenkannst?Dazuspätermehr.


---


<!-- Page 50 of 584 -->


01-DieAnforderung-LogikLücke 41
weiß du nicht! Du kannst dir zwar eine Menge denken - nur bedeutet das
nicht, dass es dasselbe ist, wie sich der Auftraggeber denkt oder was ihm
am Ende gefällt, was Wert darstellt. Wenn du hörst “Sie als Fachmann”,
ist Gefahr im Verzug! Dann musst du die Anstrengungen verdoppeln, den
Kunden aus der Unklarheit zu locken - oder ihm ganz klar sagen, dass du
nur Vorläufiges programmieren kannst.
Eine oder drei oder auch fünf Zeilen Logik zu finden, ist in diesem
Szenario nicht das Problem. Doch schon bei dieser Größenordnung fehlt
es eben an Klarheit, was überhaupt Wert für den Auftraggeber darstellt.
Mit iterativem Vorgehen lässt sich der Schaden jedoch begrenzen. Wenn
du dem Auftraggeber nicht vorgaukelst, dass du seine Wünsche direkt
umsetzenkannst,sondernFeedback-Schleifenbenötigst,führenKontraste
zwischenWunschundLieferungnichtzuKonflikten,sondernzuInforma-
tionen. Motto: “Gut, dass wir darüber gesprochen haben!”
Nach zwei Iterationen kann die Lösung dann so aussehen:
Und die Logik hat dir natürlich keine Probleme gemacht. Wenn klar ist,
was gewünscht ist, ergibt sie sich quasi von selbst und sieht z.B. so aus:
1 Console.Write("Name: ");
2 var name = Console.ReadLine();
3 if (string.IsNullOrWhiteSpace(name)) name = "World";
4 Console.WriteLine($"Hello, {name}!");
Vielmehr war es der Kunde mit der unklaren Spezifikation, der zu einem
Umweg geführt hat. Garbage in, garbage out: Das gilt auch bei der
Softwareentwicklung.
Iteration 3: Party time!
Das Programm aus Iteration 2 soll nun abermals erweitert werden,
um zur Begrüßung auf Partys eingesetzt zu werden. Der Auftragge-


---


<!-- Page 51 of 584 -->


01-DieAnforderung-LogikLücke 42
ber sagt dir:
“IchbinVeranstaltervon2-3PartysproWoche,dievon50-100Gästen
besucht werden. Solche Partys veranstalte ich in 20-25 Wochen pro
Jahr in den nächsten 1-2 Jahren. Die neue Version des Programms
möchte ich auf meinem Laptop am Eingang der Partys laufen lassen.
JederGastsolldarinseinenNameneingebenundpersönlichbegrüßt
werden. Wenn z.B. Roger das erste Mal eine dieser Partys besucht,
wirdermit“Hello,Roger!”begrüßt.KommterzumzweitenMal,heißt
es aber “Welcome back, Roger!” Ab dem dritten Besuch lautet die
Begrüßung “Hello my good friend, Roger!”. Und ist Roger schließlich
das 25. Mal auf einer Party, ist einmalig der Zusatz auszugeben
“Congrats! You are now a platinum guest!
Ich erwarte, dass ich während der Nutzungsdauer des Programms
immer denselben Laptop verwende. Der wird vor Party-Beginn hoch-
gefahren, das Programm wird einmalig gestartet für den Abend und
am Ende mit CTRL-C beendet. Eine Internetverbindung besteht am
Veranstaltungsort leider nicht verlässlich.
Können Sie das Programm in dieser Weise erweitern?”
Was nun? Sind die Anforderungen wieder unklar? Eher nicht. Es ließen
sich zwar noch ein paar Fragen stellen, wie sich das Programm verhal-
ten soll, wenn verschiedene Gäste denselben Namen haben. Doch diese
Restunklarheit ist bei dieser Iteration nicht das Problem. Vertrau mir.
Bei dieser Iteration liegt vielmehr die Logik selbst bei klaren Anforderun-
gennichtmehraufderHand.SiemagamEnde10oder20Zeilenumfassen
- viel wäre das allerdings immer noch nicht. Dennoch wirst du bei dieser
Iteration eine deutlich größere Unsicherheit verspüren. Du siehst keinen
geraden Weg mehr zur Logik; sie springt dir nicht vor dein geistiges Auge.
Deine Gedanken kreisen… du kannst jetzt nicht einfach codieren, sondern
musst zuerst nachdenken.
Die Funktionalität selbst stellt jetzt schon ein Problem dar, obwohl das
Szenario immer noch trivial ist. Und deshalb wird auch die Korrektheit
relevant.Dennwounklarist,welcheLogikdiepassendeist,istsehrschnell
auch unklar, ob die ausgewählte tatsächlich die Anforderungen erfüllt.


---


<!-- Page 52 of 584 -->


01-DieAnforderung-LogikLücke 43
Darüber hinaus aber kommst du nicht mehr ohne Ordnung im Code
aus. Deine kreisenden Gedanken suchen nicht nur die Logik für das
Verhalten, sondern auch nach einer ordentlichen Struktur, in der du die
Logik aufhängen kannst, um deine eigene Lösung zu verstehen.²⁰
Diese Struktur wird jedoch nicht durch die Logik gebildet, es geht also
nicht um den Algorithmus. Vielmehr geht es um einen Rahmen um Logik
herum, also um Nicht-Logik Code. Wenn du dabei an Funktionen und
Klassen (oder allgemeiner: Module) denkst, hast du die richtige Intuition.
Die Phasen der Programmierung
Zwischen den Anforderungen des Auftraggebers und der Logik, die
zumindest die spürbaren Verhaltensanforderungen erfüllt, klafft eine ge-
waltige Lücke: die Anforderung-Logik Lücke. Schon in sehr simplen
Szenarien wie dem vorgestellten liegt Logik nicht auf der Hand, sondern
will gewissenhaft erarbeitet werden.
Wie die Iterationen des Beispiels zeigen sollten, geschieht das in drei
Phasen, die strickt aufeinander folgen. Immer. Auch bei dir. Selbst, wenn
du das nicht wahrnimmst oder nicht glaubst. Und auch wenn sie iterativ,
also mehrfach durchlaufen werden, tut das dem Vorhandensein und der
Reihenfolge der Phasen keinen Abbruch.
1. Phase: Analyse
Konfrontiert mit Anforderungen ist die Softwareentwicklung aufgerufen,
zunächst eine für sie relevante Analyse zu machen. Diese Analyse hat als
Ziel, Verständnis zu erzeugen. Nur wenn du wirklich verstanden hast,
solltest du dich auf den Pfad der Code-Entwicklung machen. Ansonsten
ist zu befürchten, dass das Resultat keinen Wert hat und/oder inkorrekt
ist.
²⁰Ich habe das Experiment genügend oft live mit Entwicklergruppen gemacht, um zu
wissen wovon ich rede. Während bei den ersten beiden Iterationen die Logik herausge-
sprudelt wird, hängen Probanden dieses Experiments bei Iteration 3 und “stammeln sich
etwaszusammen”.SiekönnendieLogiknicht“herunterbeten”,sonderndrehengedankliche
Schleifen auf unterschiedlichen Ebenen. Meistens wollen sie mir etwas auf dem Level von
PseudocodeerzählenodernennenmirGliederungspunkte.KonkreteLogikistdasallesaber
nicht.Unddaskannauchnichtsein.DafüristselbstdiesesBeispielzugroß.EsimKopfund
geradlinigzulösen,könnennurdieallerbestenaufAnhieb-undauchdasnichtverlässlich.


---


<!-- Page 53 of 584 -->


01-DieAnforderung-LogikLücke 44
Verständnis drückt sich ausschließlich zweifelsfrei in Kön-
nen aus.
Das weiß jeder, der eine Mathematik-Prüfung (aus eigenen Kräften)
bestanden oder auch nicht bestanden hat.
Ein konkreteres Beispiel: Wer versteht, wie Fibonacci-Zahlen berechnet
werden, der kann die Folge 1, 1, 2, 3, 5, 8 beliebig fortsetzen. Der weiß,
welche Zahl auf 8 folgt, der weiß, welche Zahl auf 21 folgt; der weiß auch,
ob 35 eine Fibonacci-Zahl ist oder nicht.
Der unzweideutige formale Ausdruck von Verständnis besteht deshalb in
“Beispielaufgaben” für dich als Entwickler bzw. für die von dir zu entwi-
ckelnde Software. Nur Software, die diese “Beispielaufgaben” fehlerfrei
löst, kann als anforderungskonform und korrekt akzeptiert werden.
Vorgelegt werden die “Beispielaufgaben” natürlich in Form von automa-
tisierten Testfällen. Andernfalls ist nicht zu erwarten, dass sie verlässlich
und nachvollziehbar und personenunabhängig überprüft werden.
Wenn Produktivität nicht durch Inkorrektheit behindert
werden soll, muss Software auf Reife und Stabilität stets
automatisiert mit relevanter Codeabdeckung getestet wer-
den.
Automatisierte Tests sind die erste Bastion im Kampf gegen den
Morast der schleichend wachsenden Unwandelbarkeit, der deine Pro-
duktivität in die Knie zwingt.
Der automatisierte Test hat allerdings eine Voraussetzung: Es muss auch
klar sein, wie ein Test “an Logik angelegt” werden kann. Wie bekommt
der Test Zugang zur zu testenden Logik? Das geschieht vor allem durch
Aufruf von Funktionen.
Das gewünschte Verhalten wird durch mindestens eine
FunktioninseinerGänzerepräsentiert(API-Funktion).Die
FunktionoderandereunterhalbihrimAufrufbaumenthal-
ten die Logik, die im Test getriggert wird.


---


<!-- Page 54 of 584 -->


01-DieAnforderung-LogikLücke 45
Verständnis als Resultat der Analyse drückt sich aus in einer Reihe
von Tupeln der Form (Testfall, Funktion).
Für das Beispiel der Fibonacci-Zahlen könnte das so aussehen:
• Funktion: int[] Fib(int n)
• Testfälle:
– Input: n=0, erwartetes Resultat: []
– Input: n=1, erwartetes Resultat: [1]
– Input: n=4, erwartetes Resultat: [1,1,2,3,]
Daraus folgt:
Softwareentwicklung, die nachhaltige Produktivität ernst
nimmt als Anforderung, ist grundsätzlich test-first Pro-
grammierung.
Das Ergebnis der Analyse sind Akzeptanztests für die zu entwickelnde
Logik. Ohne Erfüllung ihrer Akzeptanztests ist Logik nicht reif; Akzep-
tanztests sind die Reifetests “an der Außenhaut” von Software. Und ohne
unausgesetzte Erfüllung bisheriger Akzeptanztests ist Logik nicht stabil.
Beides ist inakzeptabel im Sinne dauerhaft hoher Produktivität.
Der zweiten Iteration des obigen Programms fehlte es an formalem,
dokumentiertem Verständnis. Deshalb ist die Entwicklung in die falsche
Richtung gelaufen und hat auch noch den Eindruck der Inkorrektheit
gemacht.
2. Phase: Entwurf
Die dritte Iteration im Beispiel hat natürlich auch noch unter einem
Mangel an dokumentiertem Verständnis gelitten. Darüber hinaus waren
die Anforderungen aber so umfangreich, dass sich auch gutes Verständnis
nicht mehr “einfach so” in Logik hat umsetzen lassen.
Das Nachdenken über Code vor der Codierung in der IDE, das die dritte
Iteration erzwungen hat, ist das, was ich Design oder Entwurf nenne.
DiesePhaseistdiezentraleProvokationderSoftwareentwicklung,scheint


---


<!-- Page 55 of 584 -->


01-DieAnforderung-LogikLücke 46
mir. Ihr müssen sich alle Entwickelnden stellen, hier ist echte Kreativität
gefragt. Und hier gibt es den größten Widerstand seit Anfang der 2000er.
Entwurf scheint überflüssig, hinderlich, verlangsamend. Meine Erkennt-
nis ist allerdings gegenteilig: Ich sehe, dass die Produktivität leidet, weil
Entwicklungsteams einen Entwurf vernachlässigen.
Im Entwurf wird eine Lösung für das Problem gefunden,
das die Anforderungen aufwerfen. Das ist allerdings nur
eine konzeptionelle Lösung, ein Lösungsansatz. Der mani-
festiert sich in Code erst in der nächsten Phase.
Entwurf findet immer statt. Du kannst ihn sehr bewusst oder ganz
unbewusst durchführen. Erfolgt er bewusst, ist er allerdings noch nicht
notwendig auch systematisch. Deshalb lässt die Ordnung der “entworfe-
nen” Strukturen oft zu wünschen übrig.
Entwurf ist per definitionem deklarativ.
Das heißt, im Entwurf steht keine Logik zur Verfügung. Entwurf liefert
keine Algorithmen, sondern plant ein Modell.
Das Modell als Ergebnis des Entwurfs besteht aus einer Reihe von Funk-
tionen die in Tupeln der Form (Funktion1, Funktion2, Beziehungen) ver-
bunden sind.
BeispielhafteBeziehungenzwischenFunktionenfundgdesModellssind:
• f ruft g auf (Abhängigkeit)
• g folgt auf f (Sequenz)
• f spezialisiert g (Vererbung)
• fundghabeninhaltlichetwasgemeinsam(sieverfolgendenselben
Zweck)
• f und g benutzen gemeinsamen Zustand


---


<!-- Page 56 of 584 -->


01-DieAnforderung-LogikLücke 47
Das mag abstrakt klingen und Modelle müssen auch nicht in Form
von 3-spaltigen Excel-Blättern geliefert werden. Ein Klassendiagramm,
ein Datenfluss, eine Zustandsmaschine… das und mehr sind hilfreiche
Ausdrucksformen für Modelle - die sich allerdings alle auf die obige sehr
allgemeine Definition zurückführen lassen.
Zentral beim Entwurf eines Modells ist, dass es ganz bewusst von kon-
kretem Code abstrahiert. Die Feinheiten einer Programmiersprache oder
eines Framework und der Detailreichtum von Logik stehen nicht zur
Verfügung. Der Lösungsansatz ist “mit einfacheren Mitteln” zu finden.
Diese freiwillige Selbstbeschränkung hat mehrere Gründe:
• Weniger Details erlauben eine schnellere Lösungsfindung - auf
hohem Abstraktionsnivau in Form eines Durchstichs.
• Eine deklarative Lösung erlaubt die einfachere visuelle Darstellung
und damit Kommunikation zwischen Teammitgliedern. Mentale
Modelle lassen sich externalisieren.
• Visuelle, abstrakte Lösungsansätze lassen sich in größerer Vielfalt
gegenüberstellen, was der Findung besserer Lösungen dient.
• Einen Lösungsansatz zu finden erfordert andere geistige Aktivität/-
Fähigkeit als die Codierung eines Lösungsansatzes. Die explizite
Modellierung vor einer Codierung dient mithin der Entzerrung des
Entwicklungsprozesses; es wird ermüdendes, verlangsamendes und
fehlerträchtiges Multitasking vermieden.
Ein bewusster und systematischer Entwurf stellt ein Modell her,
das nicht nur die Lösung der Verhaltensanforderungen repräsentiert,
sondern auch noch der Forderung nach Ordnung genügt.
Wo die Analyse eine Bastion gegen Wertarmut und Inkorrektheit ist, da
ist der Entwurf eine Bastion gegen Unordnung.
3. Phase: Codierung
DieCodierungschließlichsetztdenEntwurfuminCode.Duübersetztein
ModellmiteinerProgrammierspracheinFunktionen,diedumitkonkreter
Logik ausfüllst.


---


<!-- Page 57 of 584 -->


01-DieAnforderung-LogikLücke 48
Ist das Modell gut, kann dieser Phase durchaus eine gewisse Langeweile
anhaften.DasProblemistja(theoretisch)gelöst.DieSpannungistrausaus
denAnforderungen.InsofernistmeinZielmitProgrammingwithEase,dir
die Codierung etwas zu verleiden. Du sollst sie am Ende als mechanische
Arbeit auffassen, bei der nur noch relativ wenig Kreativität nötig ist. Ok,
vielleicht übertreibe ich ein wenig, aber so ungefähr stelle ich mir das vor,
weil ich es selbst so erfahren habe. Je leichter ich mir die Programmierung
gemacht habe, desto unspannender wurde die Codierung.
Nachlässigkeit darf sich deshalb jedoch nicht einschleichen. Die Codie-
rung hat ihre eigenen Probleme, die noch gelöst werden wollen. Hier
schlägt die Stunde des Handwerkers, der seine Technologien beherrscht.
Das Ergebnis der Codierung ist - wie sollte es anders sein - Code. Aber
nicht irgendein Code, sondern Code, der erstens der Ordnung des Modells
folgt und zweitens in den Detail-Ebenen unterhalb des Modells ebenfalls
Ordnung walten lässt.
Darüber hinaus ist die Codierung die Phase, in der du die automatisierten
Prüfungen der Korrektheit implementierst.
Codierung stellt Produktionscode und Testcode paarweise
test-first her.
OrdnungundKorrektheitdürfenbeiderCodierungaufdenletztenMetern
nicht kompromittiert werden. Das ist kein kleines Kunststück unter dem
üblicherweise herrschenden Druck von Lieferterminen.
Zusammenfassung
Die Übersetzung von Anforderungen in Code ist eine komplexe Tätigkeit,
die nur systematisch verlässlich alle Qualitäten herstellt: Wert in Form
von Funktionalität + Effizienz, Korrektheit und Ordnung.
Die minimale Systematik, die ich dir mit Programming with Ease insge-
samt vermitteln will, besteht darin, für gegebene Anforderungen eine für
dich als Entwickler relevante Analyse durchzuführen, die nachvollzieh-
bares Verständnis nicht nur dokumentiert, sondern auch automatisiert
überprüfbar macht.


---


<!-- Page 58 of 584 -->


01-DieAnforderung-LogikLücke 49
Ausgehend von diesem Verständnis wird dann im nächsten Schritt ein
Lösungsansatz modelliert, der von den Feinheiten der Codierung bewusst
abstrahiert für mehr Überblick, bessere Kommunizierbarkeit und größere
Flexibilität.
Erst nach diesen Vorarbeiten kann alles bereit sein, um das zu tun, was
man gemeinhin als die vordringliche Aufgabe von Softwareentwicklung
sieht: die Codierung.
EineBrückeüberdieAnforderung-LogikLücke
Analyse → Entwurf → Codierung (AEC): Dieser Prozess ist unver-
brüchlich, gar unvermeidbar. Daran glaube ich fest; das zu verstehen, hat
mir die Softwareentwicklung erheblich erleichtert.
Dasbedeutetjedochnicht,dassSoftwareentwicklungdeshalb“imWasser-
fall”odernachBDUF(BigDesignUp-Front)verlaufenmüsste.DiePhasen
AEC können beliebig häufig und beliebig schnell durchlaufen werden. Sie
sollten lediglich dem Umfang und Schwierigkeitsgrad der anliegenden
Anforderungen entsprechen.
Auf diese Weise wird die Lücke zwischen Anforderungen und Code
systematisch und nachvollziehbar und teamfähig überwunden.


---


<!-- Page 59 of 584 -->


01-DieAnforderung-LogikLücke 50
Übungsaufgaben
ÜbungmachtdenMeister!Deshalbgibteszu(fast)jedemKapitelÜbungs-
aufgaben, die du in deiner Geschwindigkeit lösen kannst. Kein Druck,
keine Anprüche, die andere dabei an dich haben könnten. Mach es dir
gemütlich damit.
Zu allen Übungsaufgaben findest du im Anhang auch Musterlösungen.
Mit denen möchte ich dir das Selbststudium erleichtern; versuche also
nicht zu luschern, während du die Übungsaufgaben löst. Und bitte ver-
stehe die Musterlösungen auch nicht als Abkürzung, mit denen du dir die
eigene Lösung der Übungsaufgaben (er)sparst.
Wenn du wirklich, wirklich daran interessiert bist, zu lernen, d.h. deine
Gewohnheiten zu verändern, dann brauchst du eigene Praxis. Du musst
nach dem Lesen etwas tun mit dem Gelesenen. Gern kannst du natürlich
die Anwendung in deinem Projektalltag versuchen; früher oder später
musst du diesen Sprung ja ohnehin machen. Aber erstens sind die Pro-
bleme in deinem Projektalltag weniger überschaubar, so dass dir weniger
klar ist, wie und wo mit dem Transfer des Gelesenen du anfangen kannst.
Zweitens wirst du durch Anwendung des Neuen erstmal langsamer,
weil du noch unsicher bist; das kann dir schnell scheele Blicke von den
Kollegen einbringen und du fällst in alte Gewohnheiten zurück. Drittens
kann ich dir keinerlei Feedback geben, noch nicht einmal in Form einer
monologischen Musterlösung. Feedback ist aber extrem wichtig, wenn du
eine neue Fähigkeit erwirbst.
Deshalb empfehle ich dir sehr, die Übungen zu machen als erste Anwen-
dung des Lernstoffs “in einer Sandkiste”. Die Aufgaben sind überschaubar,
keiner redet dir rein und macht druck und mit den Musterlösungen
bekommst du zumindest eine gewisse Form von Feedback bzw. Kontrast
zum Nachdenken.
Um deine Lösungen der Übungsaufgaben zu dokumentieren, lege für dich
ein Git-Repository an, in dem du all deine Arbeitsergebnisse speicherst.
Committe häufig und vergiss am Ende das Push nicht.²¹
²¹Wenn du noch nicht so viel mit Git gearbeitet hast, kannst du einen der bequemen
visuellenGit-Clientsbenutzenwiez.B.denkostenlosenvonGitHub.EineÜbersichtfindest
duhier.


---


<!-- Page 60 of 584 -->


01-DieAnforderung-LogikLücke 51
Ein Git-Repository ist das unterste und einfachste Sicherheitsnetz, das du
für deine Programmierung spannen kannst. Never code without it.²²
Reflexionsaufgabe
Bitte formuliere eine Frage oder eine Erkenntnis zum Kapiteltext.
• Wo bist du gedanklich hängengeblieben, was ist dir unklar,
was passt für dich irgendwie nicht zusammen, wozu würdest
du dir noch etwas mehr Erklärung wünschen? Steht irgendet-
waszudeinerbisherigenPraxisimWiderspruchunddufragst
dich, warum du etwas ändern solltest?
• Oder: Wann hast du einen Aha-Moment gehabt, was ist
diralsbemerkenswert,spannend,ausprobierenswertaufgefal-
len? Hat irgendetwas “in dir Klick gemacht”, weil dir nun ein
Zusammenhang aufgegangen ist? Oder verstehst du jetzt aus
deiner bisherigen Praxis irgendetwas besser?
Am besten formulierst du Frage bzw. Erkenntnis schriftlich. Indem
du deine Gedanken aufschreibst, wirst du dir ihrer bewusster. Bei
einer Frage kommst du dadurch vielleicht schon einer Antwort aus
dir selbst heraus näher. Bei einer Erkenntnis fällt dir vielleicht schon
etwas ein, das du ab jetzt anders machen kannst.
Aufgabe 1 - Erklären
Beschreibe mit min. 500 bis max. 1000 Worten den Nutzen eines ex-
pliztenEntwurfsbzw.derModellierungfürdieSoftwareentwicklung.
Warum sollte man selbst bei hohem Verständnis der Anforderungen
nicht sofort loslegen mit der Codierung, sondern zuerst nachdenken
und modellieren?
²²Aber nicht nur den Codeanteil deiner Lösungen solltest du in Repository legen. Alle
Artefakte sind es wert, aufbewahrt zu werden. Vielleicht schreibst du Analysen in einem
.txt/.docx Dokument auf oder machst eine Zeichnung in Visio oder hast eine Skizze auf
Papier(diedufotografierenkannst),danncommittealldasebenfalls.Soschaffstdudireine
DokumentationderkomplettenLösungsentwicklung.


---


<!-- Page 61 of 584 -->


01-DieAnforderung-LogikLücke 52
Versuche dich an einer ganz einfachen Erklärung im Stile von ELI5:
Explain it like I’m 5 years old.
https://www.dictionary.com/e/slang/eli5/
Aufgabe 2 - Modellieren
Auf der Basis des bisher Gesagten und deinem Verständnis von dem,
was Entwurf ausmacht, entwickle ein Modell für die Iteration 3 des
Hello-World Problems: Gäste sollen auf Partys begrüßt werden. Wie
kann ein Lösungsansatz aussehen, ohne dass du auch nur eine Zeile
Code schreibst. Halte also auch Abstand vom üblichen Pseudocode!
Erinneredich,dasseinModelldeklarativist.Logikstehtdirnichtzur
Verfügung - und trotzdem soll mit einem Modell der Lösungsansatz
beschrieben werden. Einem anderen Entwickler, dem du ein Modell
zeigst, soll die Codierung deutlich leichter fallen, als ohne Modell.
EinerseitssolldasModelldieLösungbeschreiben,alsoschonkonkret
sein.AndererseitsjedochsolldasModellnichtzukonkretsein.Essoll
Abstand von Details halten, die erst in der Codierung ausgefleischt
werden. Ein Modell ist mithin eine abstrakte Lösung.
Wie könnte die für das Hello-World Problem aussehen? Was sollte
darin beschrieben sein - und was sollte ausgelassen werden?
Versuche dich einmal daran mit deinen bisherigen Erfahrungen mit
Softwareentwürfen. Oder vielleicht hast du von anderen schonmal
gehört, wie die soetwas angehen.
Keine Angst, dass du diese Aufgabe “falsch” lösen könntest. Es geht
nicht darum, sie in bestimmter Weise zu erfüllen, also auf “das eine
richtige” Modell zu kommen. Diese Aufgabe soll dich schlicht auf
andere Weise als die erste zu einer aktiven Auseinandersetzung mit
dem Entwurfsbegriff anregen.


---


<!-- Page 62 of 584 -->


02 - Entwurf im Überblick
Im Entwurf wird die Umsetzung vorweggenommen. Er stellt die Lösung
des Problems dar, ohne “es zu tun”. Er entwickelt nur eine Vorstellung
davon, wie die geforderte Leistung durch Software erbracht werden
könnte.
Bevor ich dir konkret erkläre, wie ich meine, dass du sehr leichtgewichtig
entwerfen solltest und warum genau so in einer bestimmten Weise,
möchte ich dir ausführlich darstellen, was ich grundsätzlich damit meine
und was das soll.
In Kapitel 01 habe ich schon versucht, den Entwurf als unverbrüchliche
Phase jeder Softwareentwicklung herauszuarbeiten. Du kommst aus mei-
ner Sicht sowieso nicht um ihn herum, auch wenn du der Meinung bist,
ihn nicht zu brauchen. Doch lass uns noch einen genauere Blick darauf
werden, was das ist, der Entwurf.
Den Entwurf abstecken
Mit ein paar Aussagepflöcken stecke ich das Thema Entwurf mal grob ab.
Dasistabstrakt,aberkeineSorge,duwirstspäternochgenügendkonkrete
Entwürfe sehen.
1. EinEntwurfstelltdieLösungeinesProblemsdar,d.h.ererfülltdie
Anforderungen des Auftraggebers.
2. Entwurf ist allerdings nicht die eigentliche Sache, die der Auftrag-
geber will. Wie auch immer ein Entwurf aussieht, es ist also kein
Code,eristnichtausführbar.DaswidersprächederDefinitionvon
Entwurf.
3. Ein Entwurf ist nur eine Beschreibung der eigentlichen Sache,
insofern ist seine Lösung nur theoretisch/konzeptionell. Nicht jede
Beschreibung der eigentlichen Sache ist jedoch ein Entwurf. Damit
eine Beschreibung ein Entwurf ist, muss sie vor der Herstellung
der Sache angefertigt worden sein. Eine Beschreibung der eigentli-
chen Sache nach der Herstellung ist eine Dokumentation.


---


<!-- Page 63 of 584 -->


02-EntwurfimÜberblick 54
4. Ein Entwurf als Beschreibung dessen, was Code leisten soll, bevor
dieser Code geschrieben wird, hat den Zweck, die Codierung deut-
lich zu erleichtern, wenn nicht gar, sie überhaupt zu ermöglichen.
5. Der Preis für die Erleichterung der Codierung darf allerdings nicht
zu hoch sein. Es ist ein gutes Verhältnis zwischen Entwurfs- und
Codierungsaufwand zu finden, das den Gesamtaufwand der Soft-
wareherstellung reduziert. Indem Entwurf und Codierung zusam-
menkommen, soll Energie frei werden, die vorher gebunden war
in “roundtrips” (aka Debugging, Testsitzungen, Iterationen).
6. Um eine Lösung zu sein, die vor der Codierung entwickelt werden
kann, diese erleichtert und selbst nicht zu aufwändig ist, muss ein
Entwurf auf einer deutlich höheren Abstraktionsebene stattfin-
den, als die Codierung. Er darf nicht durch Details der Codierung
behindert werden; er sollte weniger Komplexität als der spätere
Code aufweisen.
7. Die höhere Abstraktion darf jedoch nicht dazu führen, dass der Ent-
wurfabhebt.Ermussalsogleichzeitigkonkretundaussagekräftig
sein.
8. Leichtgewichtigkeit ist ein Kennzeichen für hilfreiche Entwurfs-
werkzeuge, denn sonst werden sie nicht benutzt, wenn der Druck,
mit der Codierung zu beginnen, groß ist.
9. Und schließlich muss ein Entwurf durch die Realität der Codierung
informiert sein und sich geradlinig in Code übersetzen lassen. Es
braucht also Bezugspunkte im Entwurf für den Code.
EntwurfundImplementationsollen“nichtüberlappen”unddieImplemen-
tation soll den Entwurf “spiegeln”.
• Der Entwurf löst das Problem, nur nicht genauso wie der Code.
• Und der Code lässt erkennen, dass er aus dem Entwurf abgeleitet
wurde, d.h. Verbindungen zwischen ihm und den Entwurfsmitteln
sind klar.
MitdemEntwurferarbeitestdueineZielvorstellungfürdenCode,d.h.die
lauffähige Lösung.


---


<!-- Page 64 of 584 -->


02-EntwurfimÜberblick 55
Hierarchie der Lösungen
Nun gibt es die Sichtweise, dass Code selbst schon ein Entwurf (engl.
design) sei.²³ Denn der Code, den du in C# oder Java oder JavaScript
schreibst, ist ja nicht das, was am Ende ausgeführt wird und tatsächlich
das Problem des Kunden löst.
Dein Hochsprachencode wird übersetzt in Maschinencode. Das kann man
als eine Form von Produktion ansehen. Und Produktion basiert auf einem
Plan, einem Entwurf. Ein Haus wird nach einem Plan hergestellt, einen
IKEA-Schrank baust du nach einem Plan auf.
In der materiellen Weltist die Produktion so sichtbar und aufwändig, dass
ein vorheriger Entwurf zwingend ist und auffällt. Bei der Softwareent-
wicklung ist die Produktion hingegen so unsichtbar und schnell, dass sie
nicht auffällt - und man die Codierung für die Produktion halten könnte.
Ich mag mich diesem Verständnis jedoch nicht recht anschließen. Oder
wenn ich mich ihm anschließe, dann finde ich die Aussage nicht hilfreich.
Ob Code nun ein Entwurf ist oder nicht, ändert nichts an der Tatsache,
dass er selbst unabhängig von jeder Kategorie sehr schwer zu schreiben
und zu verstehen ist.
Wenn Code eine Form von Design darstellt, dann ist eben dieses Design
sorgfältig zu produzieren. Dann muss ein Entwurf sogar vor diesem
Design stattfinden.
Bei einer gegebenen manifesten Lösung, sei das Maschinencode oder
Hochsprachencode, ist ein Entwurf das, was der Lösung vorhergeht
und sie auf einem höheren Abstraktionsniveau vorwegnimmt. Lösungen
existieren mithin nicht nur in einer Form, sondern in einer Hierarchie.
Lösungen gibt es auf vielen unterschiedlichen Abstraktionsebenen. So
kann des einen manifeste Lösung des anderen theoretische sein, also
“nur” ihr Entwurf. Aus dieser Perspektive betrachtet sehe ich mindestens
folgende Abstraktionsniveaus:
1. Maschinencode ist die manifeste Lösung, das Produkt? Dann ist
Hochsprachencode der Entwurf.
²³vgl. Code as Design: Three Essays by Jack W. Reeves,
https://www.developerdotstar.com/mag/articles/PDF/DevDotStar_Reeves_CodeAsDe-
sign.pdf


---


<!-- Page 65 of 584 -->


02-EntwurfimÜberblick 56
2. Hochsprachencode ist die manifeste Lösung, das Produkt? Dann ist
ein Modell dessen Entwurf.
3. EinModellistdieLösung,dasProduk?DannisteinLösungsansatz
dessen Entwurf.
4. Ein Lösungsansatz ist die Lösung, das Produkt? Dann ist eine
“Produktidee” dessen Entwurf.
Mit Maschinencode bist du wahrscheinlich nicht vertraut. Das macht
nichts, denn ich will ja nicht die Umwandlung von Hochsprachencode
in ihn behandeln. Auch wenn ich es früher immer gern schreiben wollte,
ist dies kein Buch über Compilerbau.
Mit Hochsprachencode bist du vertraut. Den will ich dir deshalb ebenfalls
nichterklären.DiesistkeineEinführungindieProgrammierung.Aberdie
Übersetzung von Entwurf - genauer: Modell - in Hochsprachencode, das
ist eine andere Sache, den werde ich dir ausführlich vorstellen.
Entwurf, wie ich ihn hier verstehe, führt zu Hochsprachencode und
erfolgtaufzweiEbenen:zuerstinFormeinesinformellenLösungsansatzes
für eine “Produktidee”, dann in Form einer formalen Modellierung des
Lösungsansatzes.
Die “Produktidee” - also letztlich das, was Anforderungen des Auftragge-
bers beschreiben - lasse ich ebenfalls aus in diesem Band. Wie du zu den
Voraussetzungen für einen Entwurf von Hochsprachencode kommst, ist
Thema des dritten Buches der Reihe Programming with Ease.
Nur soviel an dieser Stelle: Auch die Anforderungen beschreiben die Lö-
sung.AllerdingsistdieserEntwurfsoabstrakt,soweitvonderCodeebene
entfernt, dass man “das entwerfende Element” darin im Grunde nicht
erkennt. Anforderungen sind mehr ein “Wunschkonzert”. Dennoch, wenn
du genau hinschaust, befinden sich Anforderungen in dem von den neun
obigen Pflöcken abgesteckten Gebiet. Lediglich Punkt 9, die geradlinige
Übersetzbarkeit in Code, erfüllen sie nicht.²⁴
²⁴Ja,sogardenPunkt8,dieLeichtgewichtigkeit,würdeichihnenzugestehen.Darumhat
sich die Agilität sehr bemüht. Die Möglichkeit der Leichtgewichtigkeit ist ein Resultat des
iterativ-inkrementellenVorgehens.


---


<!-- Page 66 of 584 -->


02-EntwurfimÜberblick 57
DerEntwurfsprozess-odersogardiemehrerenEntwurfsschrittehinabdie
Abstraktionshierarchie - kannst du als Schärfung verstehen. Ein zunächst
grobes Bild, ein Wunschbild, wird schärfer, detailreicher, klarer mit jeder
Phase. Wie dir die 3. Iteration des Hello-World Beispiels in Kapitel 01
gezeigt hat, ist ein Sprung vom Wunsch zum Hochsprachencode nicht
möglich. Du musst dich heranarbeiten. Du musst dir erst ein grobes Bild
machen, das du nach und nach verfeinerst.
Von der Kunst lernen
In der bildenden Kunst werden Skizzen und Kompositionen angefertigt,
bevor der Künstler sich an die Schaffung des eigentlichen Werkes macht.
Hier ein Beispiel dafür aus meiner Zeichenmappe aus Jugendjahren:


---


<!-- Page 67 of 584 -->


02-EntwurfimÜberblick 58
VondergrobenIdeezumfinalenWerkinvierEntwurfsschritten
• Am Anfang stand nur eine Idee: Ich wollte die Endlichkeit des
menschlichen Lebens darstellen. Eine Sanduhr war mir dazu gleich
vor Augen. “Bild mit Sanduhr und Mensch” war also meine Anfor-
derung.
• Davon ausgehend habe ich zuerst recht pauschale Entwürfe ge-
macht. Die haben die Komposition geklärt, also die Grobstruktur
des Werkes. Anfänglich hatte ich nur die Idee einer Sanduhr in
einer Hand. Erst im zweiten Schritt kam die menschliche Gestalt
dazu. Die war also noch nicht Bestandteil der ursprünglichen
Anforderungen, sondern hat sich ergeben.
• Im dritten Schritt ist die Sanduhr auf die Hand gewandert, die nun
auch schon etwas detaillierter ausgearbeitet ist. Auch dieser Schritt
war nicht vorherzusehen, sondern ein Ergebnis dessen, dass ich
mir die Idee vorher mit den beiden anderen Entwürfen vor Augen
geführt hatte.
• Das vierte Bild ist eine Detailstudie. Der Entwurf konzentriert
sich auf eine genauere Ausarbeitung nur der Sanduhr mit der
menschlichen Figur. Dort habe ich wohl noch Unsicherheit gespürt
und wollte mich vergewissern.
• Im finalen Werk spiegeln sich die Entwürfe deutlich - aber es sind
auch Abweichungen zu erkennen. Die Handhaltung ist nochmal
leicht anders und die Form der Sanduhr hat sich verändert. Wenn
ich mich recht erinnere, hatte ich bei der Ausarbeitung gemerkt,


---


<!-- Page 68 of 584 -->


02-EntwurfimÜberblick 59
dass ich meine linke Hand, die mir Modell stand, besser so mit dem
Stundenglas halten konnte. Außerdem hatte das konkrete Glas, das
ich hielt, diese Eiform.
DieEntwürfewarenschnellgemachtundabstrakt.Dennoch-odergerade
deshalb - konnte ich mich mit ihnen zügig an die letzte Variante der
Lösung heranarbeiten, das Modell. Die Übersetzung in das endgültige
Werk hat dann deutlich länger gedauert und musste das Modell nochmal
der Realität der Umsetzung anpassen.
Meine Erfahrungen mit der Zeichnenkunst sagen mir: ohne Entwurf geht
esnicht.EinnichttrivialesWerkentstehtnichtohneeineerklecklicheZahl
von Entwürfen, die auf unterschiedlichen Abstraktionsniveaus liegen und
sogar unterschiedliche Ausschnitte behandeln.
Entwerfen ist fachgerecht
Das kreative Werk als manifeste Lösung braucht einen iterativen Prozess.
In dem wird eine Vorstellung als Skizze externalisiert, um dann in der
Betrachtung zurück zu wirken auf die Vorstellung.
Vorstellungen so greifbar wie möglich vor sich zu stellen, um sie von allen
Seiten auf ihre Wirkung (Lösungstauglichkeit) zu überprüfen, ist für mich
genauso natürlich wie zwingend. Weniger geht nicht in einem kreativen
Prozess. Wer versucht, das Kunstwerk lediglich im Kopf kurz anzudenken,
um es dann sogleich in seiner finalen Form zu produzieren, wird viel
Verschwendung betreiben.²⁵ Beim Zeichnen besteht sie aus Zeit und ist
erkennbar am Verbrauch von Papier und Stiften.
Bei der Programmierung besteht die Verschwendung auch aus Zeit, aber
erzeugt leider keinen Materialverbrauch. Das macht es so verführerisch,
²⁵Nicht zu entwerfen und sofort zu produzieren, gibt es allerdings auch. Das ist eine
eigeneKunst.DienenntmanImprovisation,würdeichsagen.OhnePlanunggeht’sgleichins
Tun. Im Theater gibt es dafür z.B. eine eigene Kategorie: das Improvisationstheater (Impro-
Theater). Schauspieler im Impro-Theater zu sein, ist eine ganz andere Herausforderung als
Schauspieler in einem normalen Stück zu sein. Im normalen Stück gibt es ein Theaterstück
als “Entwurf”, das durch die Aufführung “produziert” wird. Beim Impro-Theater gibt es
das nicht. Es wird ohne Entwurfsschritt eine Idee aus dem Publikum sofort in Handlung
umgesetzt.DasisteineganzeigeneKunstmitihremeigenenReizundihreneigenenGrenzen.
Ein Äquivalent in der Softwareentwicklung könnte vielleicht das Prototyping sein. Das hat
seinenNutzenundReizundauchseineGrenzen.


---


<!-- Page 69 of 584 -->


02-EntwurfimÜberblick 60
glaube ich, den Entwurf zu überspringen. Verschwendung ist von pro-
duktiver Arbeit oberflächlich schwer zu unterscheiden. Erkennbar ist
Verschwendung primär an Inkorrektheit und Unordnung und sekundär
an Verzögerungen und Frustrationsäußerungen.
Nach 40 Jahren Programmierung bin ich der festen Meinung: Wer auf
einen expliziten und auch noch visuellen Entwurf vor der Produk-
tion von Hochsprachencode verzichtet, der handelt fahrlässig und
verschwendet das Geld seiner Auftraggebers. Vor dem Codieren zu
entwerfen, ist für mich ein Grundbaustein fachgerechter Arbeit als
Softwareentwickler. Und ebenso gehört zur fachgerechten Arbeit die
test-first Codierung, wie im ersten Band der Reihe ausgeführt.
Entwerfen ist agil
Dass der explizite Entwurf seit Aufkommen der Agilität zunehmend in
Verruf geraten ist, ist ein Übelstand, den ich nicht genug bedauern kann.
Und wo das im Namen der Agilität geschehen ist, halte ich es für ein
grobes Missverständnis der Agilität.
“Working software over comprehensive documentation” im Agilen Mani-
fest²⁶ ist keine Aufforderung, auf Entwurf zu verzichten. Ausdrücklich ist
ja documentation genannt, nicht design. Wie oben definiert, ist Entwurf
jedoch keine Dokumentation, wenn auch “lediglich” eine Beschreibung
und keine working software.
Undnur,weilesheißt“respondingtochangeoverfollowingaplan”,istdas
keineAufforderungjeglichesPlanenseinzulassen.Danndürfteesjaauch
kein Spring Planning in Scrum geben. Ein Entwurf ist ein Plan im Sinne
einer Gestaltungsidee für einen zukünftigen Zustand der Welt. Er drückt
den Glauben aus, “Ja, so wird es wohl funktionieren!” Doch deshalb ist
ein Entwurf nicht unumstößlich. Meine Skizzen oben im Vergleich zum
finalen Werk beweisen es: Nur, weil das Werk anders ist als die Skizzen,
sind die nicht unnötig gewesen. Die Abweichung vom Plan, den Skizzen
darstellen, ist selbstverständlich erlaubt, wenn bei der Ausführung neue
²⁶https://agilemanifesto.org/


---


<!-- Page 70 of 584 -->


02-EntwurfimÜberblick 61
Erkenntnis auftauchen.²⁷
Ein Entwurf steht einem “deliver working software frequently” aus den
12 Prinzipien des Agilen Manifests²⁸ ebenfalls nicht im Wege. Im Gegen-
teil! Durch Entwurf wird der Code korrekter und ordentlicher und also
wandelbarer.
Und ein visueller Entwurf, wie ich ihn dir nahelegen werde, ich ein Beför-
derer des Prinzips “the most efficient and effective method of conveying
information to and within a development team is face-to-face conversa-
tion.” Wenn du eine Lösungsidee hast und kannst die nicht anders als
in Code ausdrücken, dann lässt sie sich nur sehr schwer kommunizieren
und diskutieren. Ohne Entwurf reduzierst du die Chance auf face-to-face
conversation.
Schließlich: Wie willst du als agiler Programmierer dem Prinzip “Simpli-
city - the art of maximizing the amount of work not done - is essential”
dienen, ohne einen Entwurf? Nur mit einem Entwurf kannst du nämlich
überhaupt über Arbeit sprechen, bevor du sie tust. Sobald du an der IDE
sitzt und Code tippst, steigerst du den amount of work. Besser, du klärst
vorher ein paar Alternativen ab und diskutierst mit deinen Kollegen.
Dafür brauchst du allerdings eine klare und anfassbare Vorstellung von
deiner Lösung vor deren Implementation. Zu der kommst du in zwei
Schritten:
²⁷Der Zweck von Planung ist, Überblick zu gewinnen und zu entzerren. Eine Form
von Multitasking soll vermieden werden. Wenn ich eine Aufgabenliste abarbeite, die ich
mir gestern für heute zusammengestellt habe, profitiert meine Konzentration davon, dass
ich mich nicht mehr frage, “Was soll ich als nächstes tun?” Die Frage habe ich gestern
beantwortet, als ich dafür in einem “speziellen Bewusstseinszustand” war. Gestern war ich
kreativ, gestern hatte ich Überblick. Heute will ich nicht mehr kreativ sein, sondern Dinge
nur erledigen. Dazu brauche ich einen anderen “Bewusstseinszustand”. Falls ich jedoch auf
einHindernisstoße,kannichauchvomPlanabweichen.NeueInformationendürfen,sollen,
müssen den Plan verändern können. Hätte ich die Informationen gestern gehabt, hätte ich
denPlanvonvornhereinandersgestaltet.DasHindernisreißtmichheutezwarausmeinem
“Bewusstseinszustand”derAbarbeitung-aberwassoll’s?Lässtsichnichtändern.Ichmache
dasbestedaraus,indemichkurzwiederindenPlanungsmodusgehe.
²⁸https://agilemanifesto.org/principles.html


---


<!-- Page 71 of 584 -->


02-EntwurfimÜberblick 62
1. Der Lösungsansatz
In den Entwurf gehst du, wenn du die Anforderungen verstanden hast.
Vorher hast du einfach nicht genügend Grundlage, auf der du eine Lösung
aufbauen könntest.
Hier ein Beispiel für Anforderungen die das Kriterium auf Kapitel 01
erfüllen: Es liegen Beispiele vor und eine Funktionssignatur ist gegeben.
Eine Liste von ganzen Zahlen soll in eine Ordnung gebracht werden,
bei der für jede Zahl am Listenplatz mit Index i (kurz: z[i]) gilt:
z[i-1] <= z[i] <= z[i+1].
Funktion:
• int[] Ordnen(int[] zahlen)
Beispiele:
• [1,5,2,9,8,4]-> [1,2,4,5,8,9]
• []-> []
Duerkennstnatürlichsofort,dasmit“ordnen”hiergemeintist“sortieren”:
Die Zahlen sollen aufsteigend sortiert werden.
Schon diese Klassifikation der Anforderungen ist ein erster Schritt in
Richtung Lösung. Jetzt kannst du nämlich in der Literatur nachschlagen,
wie man das macht. Andere haben das Problem schon vor dir gelöst.
Du müsstest nicht einmal selbst entwerfen, sondern womöglich nur eine
Lösung abschreiben. Oder noch besser: deine Programmiersprache oder
Standardbibliothek der Programmiersprache bieten bereits eine fertige
Sortierfunktion.
“Ah, das Problem lässt sich durch Sortieriung lösen!” würde ich als erste
Erkenntnis im Sinne eines Lösungsansatzes in diesem Fall zählen.
AberderÜbunghalberwillichdavonabsehen,dassesschonLösungenfür


---


<!-- Page 72 of 584 -->


02-EntwurfimÜberblick 63
das Sortieren gibt. Das Problem ist nämlich gut geeignet, um zu erklären,
was ein Lösungsansatz ist.
Du könntest natürlich jetzt jedes weitere Nachdenken in den Wind schla-
gen und mit classical TDD in die Tasten greifen. Inkrementell könntest du
versuchen, direkt eine Lösung zu codieren. Das ist bestimmt möglich. Die
Testfälle könnten z.B. wie folgt schrittweise schwieriger werden:
1. []-> [] // Akzeptanztest und natürlicher Startpunkt
2. [3]-> [3]
3. [1,3]-> [1,3]
4. [3,1]-> [1,3]
5. [3,1,4]-> [1,3,4]
6. [3,4,1]-> [1,3,4]
7. [1,5,2,9,8,4]-> [1,2,4,5,8,9] // finaler Akzeptanztest
DieZunahmedesSchwierigkeitsgradesderTestssiehtplausibelaus.Ohne
weitere Lösungsidee kannst du dir da jedoch nicht sicher sein. Das ist ein
Grund, warum ich zwar sehr für test-first Codierung bin, doch nur mit
einem vorherigen Entwurf.
Wenndueinmalversuchstzuvergessen,wasduallesschonüberSortieral-
gorithmen weißt, was würdest du nach Studium der Anforderungen tun?
Nein, nicht codieren, sondern im Kopf oder auf einem Stück Papier.
Jetzt ist womöglich die größte Kreativität in der Softwareentwicklung
gefragt. Ich halte diese Phase jedenfalls für ihren Kern. Dafür sind
Millonen Menschen Softwareentwickelnde geworden! Das ist der Teil, wo
du an einem Problem knobeln kannst. Wer knifflige Probleme liebt, der ist
im Entwurf bei der (Er)Findung eines Lösungsansatzes genau richtig.
Ich glaube, selbst dieses Problem löst du nicht im Kopf. Du musst deine
Vorstellungen vor dir manifestieren. Blatt und Stift reichen dafür aus.
Beim Lösungsansatz gelten keine Regeln. Alles ist erlaubt, was dich dem
Ergebnisnäherbringt.DasistechteFreistil-Softwareentwicklung.Inallen
weiterenPhasenmusstduirgendwelchenRegelnundFormalismenfolgen.
Genieße also die Freiheit in diesem Moment!
Wie kannst du das Problem auf einem Blatt Papier angehen? Hier ist mal
ein Vorschlag:


---


<!-- Page 73 of 584 -->


02-EntwurfimÜberblick 64
LösungsskizzefürdieSortierung
Ist das formal? Nein. Verstehst du, was ich damit meine? Wahrscheinlich
nicht. Kenne ich jetzt die Lösung? Ja! Und nur das zählt.
Ich habe mit einer Notation mit graphischen Elementen und Konventio-
nen, die ich mir spontan ausgedacht habe, eine Darstellung geschaffen,
die es mir erlaubte, meine ganz grobe Lösungsidee aus meinem Kopf aufs
Blatt zu bekommen. Du siehst eine Lösung als Skizze.
Es hätte aber auch anders aussehen können. Über die folgende Darstel-
lungsart bin ich im Internet gestolpert, als ich für das Buch recherchiert
habe:
Hier wird die zu sortierende Liste als Matrix dargestellt, bei der in der ver-
tikalen die Werte an der jeweiligen Position aufgetragen sind. Dadurch ist
die schrittweise Herstellung der gewünschten Ordnung visuell sehr schön
nachvollziehbar. Der gelbe Wert in einem Bild i ist im Bild i+1 einfach
mit dem bis dahin letzten im blau markierten Listenabschnitt vertauscht


---


<!-- Page 74 of 584 -->


02-EntwurfimÜberblick 65
worden (rot). So formen die Punkte von Bild zu Bild zunehmend eine
aufsteigende Linie.²⁹
Beim Lösungsansatz geht es nur um das Verfahren. Solange das plausibel
wird, konkret und erklärbar(er) ist, ist das Ziel dieser Entwurfsphase
erreicht.
Wenn du mit einem Problem konfrontiert bist, kann es sein, dass du es
sofort lösen kannst. Das ist der Fall bei der vorliegenden Aufgabe. Du
kannst natürlich eine Liste von Zahlen sortieren.
Nur, weil du das kannst, kannst du es aber noch lange nicht auch noch
erklären. Wie geht das mit dem Sortieren? Wie gehst du vor? Was ist
dein Verfahren, deine Herangehensweise, deine Methode, dein Ansatz?
In der ersten Phase des Entwurfs findest du nicht nur heraus, ob du “es”
kannst oder “irgendwie weißt wie es geht”. Nein, du musst dein Können
und Wissen vermitteln können. Erste Herausforderung: Kannst du es dir
selbst erklären? Zweite Herausforderung: Kannst du es anderen erklären?
In dieser Phase bist du im Grunde Erfinder. Du brauchst dafür kein
wirres Haar, keine Brille und auch kein chaotisches Arbeitszimmer. Du
bist Erfinder qua Aufgabe, die lautet: Finde eine Lösung, die du erklären
kannst.
Deine Erfindung bezieht sich auf die anliegende funktionale oder nicht-
funktionale Aufgabe. Im Beispiel ist es zunächst nur die funktionale, eine
Listeüberhauptzusortieren.Siebesonderseffizientzusortieren,warnicht
gefragt.³⁰
²⁹DerLösungsansatz“erfindet”übrigensdenSortieralgorithmusSelectionSort.Denhabe
ich hier gewählt, weil er so naheliegend ist. Ohne mich an Selection Sort konkret erinnert
zu haben, fiel mir dieser Ansatz einfach ein. Wenn dir ein anderer eingefallen ist, ist das
natürlichebensogut.Nur,wiehättestdudeinenLösungsansatzdargestellt?
³⁰Um auch noch eine besonders effiziente (hier: performante) Lösung zu finden, musst
du wahrscheinlich mehrere Lösungsansätze entwickeln und vergleichen. Nimm dir also zu
Anfang nicht zu viel vor: Finde zunächst einen funktionalen Lösungsansatz. Erst wenn du
den hast, suche nach weiteren mit besseren Effizienzcharakteristika. Das zu trennen, fällt
vielen Entwicklern schwer. Sie wollen gleich die optimale Lösung. Doch damit stehen sie
sich selbst im Wege. Das halte ich für ein Rezept für Frust und Verzögerung. Außerdem
verschenkt soviel Vorsatz die Chance auf kleinere Iterationen. Wenn der Auftraggeber eine
funktionale und effiziente Lösung will, dann biete ihm an, zunächst nur eine funktionale
zu liefern. Dann kann er schonmal überprüfen, ob das seinen Wünschen entspricht. Falls
nämlichnicht,hastdukeinenOptimierungsaufwandverschwendet.Undsollteallesoksein,
fängst du dann mit der Optimierung an - oder der Auftraggeber entscheidet, dass mehr
Effizienz doch nicht nötig ist, da er nun gesehen hat, was eine “nur” funktionale Lösung
schonbietet.AuchdannhastdukeinenOptimierungsaufwandverschwendet.


---


<!-- Page 75 of 584 -->


02-EntwurfimÜberblick 66
Ich kann mir vorstellen, dass diese “Lösungsansatzdenke” für dich noch
ein bisschen abstrakt ist. Deshalb ein weiteres Beispiel, bevor es an die
nächste Entwurfsphase geht:
Party time again!
“IchbinVeranstaltervon2-3PartysproWoche,dievon50-100Gästen
besucht werden. Solche Partys veranstalte ich in 20-25 Wochen pro
Jahr in den nächsten 1-2 Jahren. Die neue Version des Programms
möchte ich auf meinem Laptop am Eingang der Partys laufen lassen.
JederGastsolldarinseinenNameneingebenundpersönlichbegrüßt
werden. Wenn z.B. Roger das erste Mal eine dieser Partys besucht,
wirdermit“Hello,Roger!”begrüßt.KommterzumzweitenMal,heißt
es aber “Welcome back, Roger!” Ab dem dritten Besuch lautet die
Begrüßung “Hello my good friend, Roger!”. Und ist Roger schließlich
das 25. Mal auf einer Party, ist einmalig der Zusatz auszugeben
“Congrats! You are now a platinum guest!
Ich erwarte, dass ich während der Nutzungsdauer des Programms
immer denselben Laptop verwende. Der wird vor Party-Beginn hoch-
gefahren, das Programm wird einmalig gestartet für den Abend und
am Ende mit CTRL-C beendet. Eine Internetverbindung besteht am
Veranstaltungsort leider nicht verlässlich.
Können Sie das Programm in dieser Weise erweitern?”
Das ist wieder die 3. Iteration des Hello-World Programms. Schon diese
Anforderungen umzusetzen war ja schwierig, solange ein Entwurf fehlt,
wie ich versucht habe, in Kapitel 01 zu vermitteln. Wie könnte der jetzt
also aussehen, um die Umsetzung zu vereinfachen? Oder genauer: Wie
könnte sogar zunächst nur ein Lösungsansatz aussehen?
Für mich beginnt der Lösungansatz oft mit einer Sammlung dessen, was
gebraucht wird. Welche “Komponenten” sind nötig? Was für Funkti-
onseinheiten sind klar ersichtlich? Welche Subprobleme müssen gelöst
werden? Im konkreten Fall gehört für mich dann auch dazu, welchem
Ansatz die Persistenz folgen soll.


---


<!-- Page 76 of 584 -->


02-EntwurfimÜberblick 67
Auf der linken Seite siehst du ein Gedächtnisstütze. Ich habe die Benut-
zerschnittstelle skizziert, um mir währenddessen das Problem nochmal
zu vergegenwärtigen. Natürlich ist die Benutzerschnittstelle schon Teil
der Anforderungsdefinition, die du mit dem Auftraggeber zusammen
erarbeitest. Doch zur Fokussierung auf den Entwurf ist es nicht schlecht,
die Oberfläche dessen, was nun zu entwerfen ist, zu wiederholen und ggf.
in ein anderes Format zu bringen, das dir als Entwickler taugt.
Rechts oben eine Liste der Funktionsbereiche. Aus den Anforderungen
und der Vorstellung, wie die Bedienung des Programms sich anfühlen
könnte, habe ich abgeleitet, was mindestens getan werden muss innerhalb
des Programms. Dafür reicht erstmal eine Spiegelstrichliste ohne weitere
Ordnung. Die ist sozusagen ein brain dump dessen, was dir so einfällt.
Achte nicht auf Abstraktionsniveaus oder Beziehungen zwischen diesen
Funktionsbereichen. Mir ist eingefallen:
• IrgendwiemussderNameerfragtwerden.Dasisteine“Kompetenz”,
die im Programm ausgebildet werden muss. Die kann z.B. leere
Namen abweisen und erneut auffordern, wenn das gewollt sein
sollte.
• Irgendwie muss dann auch die Liste der Gäste geführt werden, in
der gezählt wird bzw. aus der abgelesen werden kann, wie oft ein
Gast (identifiziert über seinen Namen) schon da war.


---


<!-- Page 77 of 584 -->


02-EntwurfimÜberblick 68
• Und irgendwie muss der Name inkl. seiner Besuchszahl in eine
konkrete Begrüßung überführt werden, die dann angezeigt wird.
Jenachdem, wie oft der Gast schon da war, wird hier entschieden,
mit welcher Formel er begrüßt wird.
Weniger geht nicht, finde ich. Diese Funktionsbereiche stechen für mich
als eigenständig heraus.
Zum Abschluss dann noch eine Idee, wie die Gästeliste über die Laufzeit
des Programms hinaus persistent gemacht werden könnte. Mir scheint,
dass dafür eine simple Textdatei im CSV-Format ausreicht. Zu jedem
Namen wird darin vermerkt, wie oft der Gast schon da war. Kommt der
Gast wieder, wird sein Besuchszähler erhöht.
Vielleicht hast du eine ähnliche Idee gehabt für einen Lösungsansatz,
vielleicht auch nicht. Wichtig ist nicht, dass er genau so aussieht wie mei-
ner, sonder dass es überhaupt einen gibt. Jeder Lösungsansatz auf einem
Blatt Papier (oder in einer iPad-App wie Notability oder GoodNotes) ist
besser als keiner. Denn mit jedem aufgezeichneten, d.h. externalisierten,
explizierten und visualisierten Lösungsansatz bist erstens du dir selbst
klarer über die Lösung geworden und zweitens kannst du jetzt anfangen,
den Lösungsansatz mit anderen zu diskutieren. Wenn du mit Kollegen das
Problemangehst,dannhastdudieLösungaufeinemMedium,dasihrteilt.
Darauf könnt ihr beide schauen, daran könnt ihr beide arbeiten.
Aber auch wenn ich sage, dass es für den Lösungsansatz keine spezielle
Form gibt, weil du möglichst frei sein sollst, deiner Kreativität Raum zu
geben, gibt es Grenzen der Nützlichkeit. Hier ein Bild aus einem Clean
Code Workshop. Diesen Lösungsansatz hatte ein Team am Whiteboard
zurückgelassen, als es sich an die Codierung gemacht hat. Bei aller
Offenheit für persönlichen Stil und individuelle Darstellungen ist mir das
dann doch zu wenig.


---


<!-- Page 78 of 584 -->


02-EntwurfimÜberblick 69
Also: Beim Lösungsansatz geht eine Menge. Mach dir keinen Kopf, “es
richtig zu tun”. Wichtiger ist, dass du es überhaupt versuchst und einen
Ausgangspunkt für den nächsten Entwurfsschritt schaffst. Doch achte
darauf, dass ein substanzieller Bezug zum Problem zu sehen ist. Nur dann
kann sich ein gemeinsames Modell entwickeln, weil alle von demselben
Bild ausgehen. Ansonsten hängen nur Worte in der Luft, unsichtbar und
flüchtig. Auf die kannst du ungleich schwerer Bezug nehmen. Deren
Interpretation geht schnell auseinander.
Ein zu Papier gebrachter, expliziter Lösungsansatz hilft dir auch zu
iterieren.SeinichtmitdererstenIdeezufrieden.Wenndusievordirsiehst
(oder auch nur versuchst, sie vor dich hinzustellen), kann es sein, dass du
erstmalig merkst,dass dieIdee doch nochnicht sogut ist.Schwierigkeiten
in der Visualisierung im Speziellen oder Erklärung mit Worten im Allge-
meinen sind ein gutes Signal für dich, weiter darüber nachzudenken. Und
so kann es sein, dass du auf einen neuen Lösungsansatz kommst - den du
selbstverständlich ebenfalls zu Papier bringst. Hier ein Beispiel für eine
Revision der Persistenzidee für das Hello-World Beispiel:


---


<!-- Page 79 of 584 -->


02-EntwurfimÜberblick 70
DieFunktionsbereichehabensichnichtverändert.DochdasPersistenzfor-
matgefälltmirnichtmehr.WarumdieNamenzusammenmitBesuchszäh-
lernspeichern?DannmussdieGästelisteimmerkomplettneugeschrieben
werden,wenneseineTextdateiist,obwohlsichnureinWertveränderthat.
Oder ich müsste zu einer echten Datenbank greifen, die einen gezielten
Zugriff auf nur einen Datensatz bietet. Oder ich müsste die Namen statt
in einer Datei auf viele verteilen, die ich getrennt aktualisieren kann.
Vieleinfacherscheintmirjedoch,beieinerDateizubleiben,andieNamen
allerdigs nur angehängt werden. Jeder Name taucht darin dann so häufig
auf, wie der Gast auf einer Party war. Das kann jederzeit gezählt werden.
Diesen Ansatz nenne ich Event Store, weil jeder Besuch ein Ereignis ist,
dasminimalmitdemBesuchernamendokumentiertwird.Dasisteintotal
flexibler Ansatz, der ohne Schema auskommt.³¹
Wie auch immer der Ansatz aussieht, das Wesentliche ist, überhaupt
Klarheit über deine Lösungsidee zu bekommen. Versuche Anforderungen
³¹Dass der Ansatz nicht genügend skaliert, auch wenn es tausende, gar zehntausende
Besucher gibt, ist nicht zu fürchten. Festplatten und Prozessoren sind schnell genug, um
selbstfürjedenBesuchereinesolcheDateikomplettzuladen(wasnichteinmalseinmüsste).
Aber falls du das bezweifeln solltest, probiere es schnell aus. In wenigen Zeilen kannst du
deine Hypothese mit einer spike solution überprüfen. Schließe einen Lösungsansatz, der
Vorteile hat (hier: Flexibilität), nicht aufgrund nur eines Gefühls aus, dass die Nachteile
überwiegenkönnten.MacheliebereinExperiment.


---


<!-- Page 80 of 584 -->


02-EntwurfimÜberblick 71
nicht sofort in Code umzusetzen. Versuche nicht einmal, eine Lösung
für die Anforderungen sofort mit einem formalen Modell zu beschreiben.
Nein, nimm dir die Zeit, die Lösung “im Freistil” zu erarbeiten. Deiner
Kreativität sollen dabei keine Grenzen gesetzt werden. Dadurch wird der
Lösungsansatz sehr wahrscheinlich auch schon ganz natürlich deklarativ.
Betrachte in ihm Verhalten und/oder Daten, wie du magst. Wie es dir
taugt, um Klarheit zu bekommen. “Ah, ja, so kann es gehen!” sollst du am
Ende ausrufen. Dann bist du bereit für den nächsten Schritt.
Lediglich auf Papier musst³² du deinen Lösungsansatz früher oder später
bringen. Das ist ein erster Test, ob er etwas taugt. Denn wenn du ihn nicht
mal “im Freistil” auf Papier beschreiben kannst, wie willst du das später
im Korsett des Codes schaffen?
2. Das Modell
Der Lösungsansatz ist notwendig, aber nicht hinreichend als Entwurf.
Mit ihm hast du zwar eine Lösung erarbeitet, die kannst du nur nicht
geradlinig in Code übersetzen. Damit kommen wir zum Modell: Das
Modell ist die Lösung in solchermaßen formalisierter Form, dass dir
danach die Codierung der Lösung leicht(er) von der Hand geht.
Jede Phase im Softwareentwicklungsprozess, den ich dir im Rahmen von
ProgrammingwithEaseempfehle,hateinensehrkonkreten,engenZweck:
1. Die Anforderungsanalyse baut bei dir Verständnis für ihr Problem
in einer Form auf, die konkret und testbar ist. Das Ergebnis sind
Funktionen mit zugehörigen Testfällen.
2. Der Entwurf findet eine Lösung für das Problem, das du nach der
Analyse verstanden hast. Das Ergebnis ist ein Modell.
1. Zunächst erarbeitest du die Lösung in Form eines Lösungsan-
satzes. Das ist informell, sehr abstrakt, möglichst visuell und
“auf Papier”.
³²Naja, du “musst” nicht. Aber ich lege es dir sehr, sehr ans Herz. Die Vorteile eines
solchenAusdruckssindzuvielfältig,alsdasdusieindenWindschlagensolltest.AmAnfang
mag es dir schwerfallen. Mit der Übung wird es dann leichter. Am Ende kannst du dir eine
Programmierungohne“verbildlichte”Lösungsansätzenichtmehrvorstellen.


---


<!-- Page 81 of 584 -->


02-EntwurfimÜberblick 72
2. Anschließend konkretisierst und formalisierst du den Lö-
sungsansatz. Das Abstraktionsniveau sinkt etwas, die Lösung
wird feiner ausgearbeitet, dennoch ist das resultierende Mo-
dell deklarativ und “codefrei”.
3. Die Codierung übersetzt die entworfene Lösung in Hochsprachen-
code. Das Ergebnis sind Produktions- und Testcode.
1. In der Codierung schreibst du zuerst einen Test, um dir eine
Latte aufzulegen, über die du springen willst. Mit test-first
vergisst du nicht, Tests zu schreiben, und du weißt sofort,
wann du fertig bist mit dem Produktionscode.
2. Der Produktionscode ist die Übersetzung des Modells in eine
Form, die dem Kunden am Ende nutzt. Die Funktionen und
Beziehungen aus dem Modell übersetzt du in Code. Anschlie-
ßendfüllstdudieFunktionenmitLogikan,sodasstatsächlich
Verhalten hergestellt wird. Das ist nun die imperative Lösung
des Problems, das die Anforderungen aufgeworfen haben.
3. Immer wieder refaktorisierst du Produktions- und durchaus
auch Testcode, um das, was trotz eines guten Modells und ge-
radliniger Übersetzung unsauber geworden ist, wieder in eine
zukunftsfähige Ordnung zu bringen. Das passiert immer mal
wieder und ist nicht schlimm. Gelegentlich weichst du auch
vom Modell ab, weil du in der Codierung neue Erkenntnisse
gewinnst.
Für gegebene Anforderungen ist das mehr oder weniger ein Wasserfall.
Du durchschreitest diese Phasen von 1. bis 3.3. in dieser Reihenfolge.
Theoretisch jedenfalls, denn praktisch gibt es darin Schleifen bzw. Rück-
wärtsschritte: Du gehst von der Modellierung zurück zum Lösungsansatz,
weil du bei der Konkretisierung bemerkst, dass irgendetwas noch fehlt.
Du gehst womöglich vom Lösungsansatz zurück zur Anforderungsana-
lyse und sprichst mit dem Auftraggeber, weil du bemerkst, dass dir
irgendetwas noch unklar ist. Du “drehst dich im Kreis” innerhalb der
CodierungwährendderÜbersetzungeinesModells;dasgehstduFunktion
für Funktion mit 3.1, 3.2 und 3.3 an.
Der Wasserfall ist also entschärft. Keine Sorge, du musst keinen “Agili-
tätseid” brechen. Außerdem gilt der Wasserfall nur für die anliegenden
Anforderungen. Es gibt keine Not, alle Anforderungen erst komplett zu
analysieren. Du kannst einen beliebig kleinen Ausschnitt wählen. Manch-
mal rauschst du den Wasserfall in vier Stunden herunter, manchmal in


---


<!-- Page 82 of 584 -->


02-EntwurfimÜberblick 73
einem Tag, manchmal in zwei Tagen. Länger sollte es zumindest für
Entwurf+Codierungnichtdauern.Ichglaubefestdaran,dassInkremente
nicht mehr als 16 Stunden für die Umsetzung brauchen sollten, d.h. z.B.
von heute 9:00 Uhr bis morgen 17:00 Uhr.³³
Modellarten
Das Modell formalisiert den Lösungsansatz. Es konkretisiert, was der Lö-
sungsansatz mehr oder weniger grob angedacht hat. Was bisher vielleicht
nur verschwommen zu sehen war, muss nun geklärt werden. Das betrifft
beideSeitenjederLösung:dasVerhaltenunddieDaten.Esgibtdaherzwei
Arten von Modellen:
• Das Verhaltensmodell beschreibt, was getan werden muss, um das
Problem zur Laufzeit zu lösen.
• Das Datenmodell beschreibt, mit welchen Daten etwas getan wer-
den muss.
Software weißt insofern eine grundsätzliche Dualität auf. Verhalten und
Daten sind deren gegenüberstehende Seiten und ergeben zusammen das
Ganze. Ohne Daten kein Verhalten, ohne Verhalten keine Daten.
Allerdings hat einer dieser Aspekte für mich Priorität: das Verhalten.
Dafür wird Software gemacht! Eine Problemlösung besteht immer in
³³Eine solche Arbeitsweise nennen ich spinning und habe den gleichnamigen Workout
im Fitness-Studio im Sinn. Dass in 16 Stunden nicht unbedingt Wert für den Auftraggeber
hergestellt werden kann, ist mir klar. Doch das ist auch nicht der Zweck, so kleiner Inkre-
mente. Nach 16 Stunden soll vielmehr eine Umsetzung vorliegen, zu der der Auftraggeber
“nur”Feedbackgebenkann.DuwillstalsProgrammierereinfachnichtlängeralszweiTage
im Ungewissen sein, ob das, woran du arbeitest in die richtige Richtung geht. Und auch
der Auftraggeber sollte nicht länger im Unklaren sein, ob du ihn verstanden hast bzw. ob
er überhaupt in Auftrag gegeben hat, was er wirklich braucht. Aus mehreren Feedback-
Inkrementen setzt sich dann ein Wert-Inkrement zusammen. Wann Wert für den Kunden
entsteht, ist nicht dein Job zu beurteilen. Mit jeder Umsetzung produzierst du lediglich
Qualitätscode in jeder Hinsicht in Bezug auf die dir vorliegenden Anforderungen. Das ist
wirklichalles.Dochdasistschwieriggenug.BelastedichalsonichtnochmitderWertfrage.


---


<!-- Page 83 of 584 -->


02-EntwurfimÜberblick 74
Verhalten, das Daten transformiert.³⁴
Datenmodelle
Die mainstream Objektorientierung wie auch lange Jahrzehnte sehr be-
grenzter Hauptspeicher und daraus folgend eine Wichtigkeit von Daten-
banksystemen haben aus meiner Sicht viele Softwareteams dazu verleitet,
zuerstundvorallemüberDatenmodellenachzudenken.FürdiesenAspekt
hatEntwurfeinegewisseAkzeptanzundSichtbarkeitbehalten.Ichnehme
an, dass auch du schon z.B. von Entity-Relationship (ER)-Modellen³⁵
gehört hast:
³⁴Oder sogar noch genauer: Software wird für größere Effizienz entwickelt. Mit genü-
gend Ressourcen wie Zeit oder Menschen können die Probleme, die Software löst, auch
ohne Software gelöst werden. Es geht also nicht primär um Funktionalität. Auftraggeber
versprechensichvonSoftwarevielmehr,dasssieeffizienteristalssoftwareloseAlternativen.
Der Effizienzgewinn kann in performanterer Funktionalität liegen oder in benutzerfreund-
licherer oder sicherer usw. Es geht um den Komparativ erkenntlich am “-er” der Effizienz-
Adjektive. Manchmal scheint es zwar auszureichen, nur eine Funktionalität in Software zu
gießen,umsieschlichtjederzeitfürAnwenderverfügbarzuhaben.Aberauchdamitisteine
Effizienzgemeint.
³⁵https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model


---


<!-- Page 84 of 584 -->


02-EntwurfimÜberblick 75
BeispielfüreinEntity-RelationshipDatenmodellausWikipedia
DieseDarstellungist“nur”einModell,weilsiekeinCodeist.Wedersiehst
du programmiersprachliche Anweisungen, um eine solche Datenstruktur
in einer Datenbank herzustellen, noch siehst du Klassen, die sie in-
memory darstellen könnten, noch ist überhaupt klar, wie die einzelnen
Elemente des Modells implementiert werden.³⁶
Oder hier ein anderes Datenmodell von einer Seite³⁷, die UML (Unified
Modelling Language)³⁸ Klassendiagramme vorstellt:
³⁶Die Implementierung des ER-Modells könnte mittels eines RDBMS oder auch einer
Dokumentendatenbank geschehen. Dass und welche Relationen existieren, erzwingt kein
RDBMS,auchwenndaslangedieersteWahlgewesenseinmag.
³⁷https://datamodelprototype.wordpress.com/2014/01/30/uml-modeling-class-
diagrams/
³⁸https://en.wikipedia.org/wiki/Unified_Modeling_Language


---


<!-- Page 85 of 584 -->


02-EntwurfimÜberblick 76
EinKlassendiagrammalsDatenmodell
Bei Datenmodellen geht es darum, Datenelemente zu benennen, Daten
zusammenzufassen und Zusammenfassungen in Beziehung zu stellen.
Diese Daten tun nichts, vielmehr wird mit ihnen etwas getan. Das ist die
Aufgabe von Verhalten.
Im weiteren werde ich nicht viel zu konkreten Datenmodellierungsansät-
zen sagen. Ich entwerfe und benutze Datenmodelle einfach in der einen
oder anderen Form. Datenmodellnotationen sind bei aller Unterschied-
lichkeit der Darstellungen doch so einfach und naheliegend und weit
verbreitet,dassichmirweitereAusführungenerspare.Ichbingewiss,dass
du mit der Datenmodellierung keine Schwierigkeiten haben wirst, wenn
du erstmal weißt, um welche Daten es bei einer Lösung geht.
Das allerdings ist wiederum innerhalb der Lösungsfindung ein Problem,
mit dem wir uns befassen wollen. Zu oft wird nämlich für meinen
Geschmack eine vorzeitige Optimierung im Hinblick auf das Datenmo-
dell vorgenommen. Das Datenmodell wird gesetzt und daran muss sich
dann das Verhalten anlagern. Für mich steht auf diese Weise jedoch die
Entwurfswelt auf dem Kopf!
Verhaltensmodelle
Wiegesagt,PrioritäthatfürmichdasVerhaltensmodell.ImVerhaltensmo-
dell wird beschrieben, was passieren soll. Man könnte sagen: Verhaltens-
modelledrehensichumVerben,DatenmodelleumSubstantive.Funktions-
einheitenwerdenbenannt,zusammengefasstundZusammenfassungenin
Beziehung gesetzt. Diese Funktionseinheiten tun etwas mit Daten.


---


<!-- Page 86 of 584 -->


02-EntwurfimÜberblick 77
Vielleicht fällt dir sogar eine Art Verhaltensmodell ein: lange Zeit war das
Flowchart³⁹ sehr beliebt.
EinFlowchartnachWikipediaalsVerhaltensmodell
Das sieht konkreter aus als die bisherigen Lösungsansätze, oder? Das
kannst du “runterprogrammieren”, oder?
Ich halte das aber für kein nützliches Modell. Es abstrahiert für meinen
Geschmack zu wenig von den Mitteln einer Hochsprache. Ein Flowchart
stellt einen Kontrollfluss dar wie Hochsprachencode. Es enthält Fallunter-
scheidungen und vor allem auch Schleifen wie Hochsprachencode. Diese
Art der Darstellung von Verhalten bietet schlicht keine Skalierbarkeit.
Du kannst damit keine größeren Lösungen beschreiben: das resultierende
Diagramm ist dann genauso wenig verständlich wie Hochsprachencode.
Flowcharst stammen aus einer Zeit vor der Strukturierten Programmie-
rung⁴⁰. In ihnen sind beliebige Verzweigungen (lies: Sprünge) erlaubt. Es
gibt keine wirklich beschränkende Syntax. Sie sind mithin wenig hilfreich
inderPraxis-auchwennsiehierunddabeisehrbegrenzterFunktionalität
³⁹https://en.wikipedia.org/wiki/Flowchart
⁴⁰https://de.wikipedia.org/wiki/Strukturierte_Programmierung


---


<!-- Page 87 of 584 -->


02-EntwurfimÜberblick 78
mal zum Einsatz kommen können.
Für mich gibt es zwei Kategorien von Lösungen: algorithmische und
prozessurale. Algorithmische Lösungen bewegen sich sehr nah an den
Mitteln der Strukturierten Programmierung von Programmiersprachen.
Du bist versucht, sie mit Pseudocode oder Flowcharts zu modellieren. Der
Lösungsansatz für das Sortierproblem fällt in diese Kategorie.
Als Beispiel für Pseudocode die obige Lösung für die Behandlung einer
nicht funktionierenden Lampe:
1 If lamp is plugged in then
2 if bulb is burned out then
3 replace bulb
4 else
5 repair lamp
6 end if
7 else
8 plug in lamp
9 end if
Den Code verstehst du, auch wenn er zu keiner speziellen Program-
miersprache gehört. Er ist eine Verallgemeinerung dessen, was in vielen
Sprache an Mitteln vorhanden ist. Deshalb lässt er sich schnell hinschrei-
ben; du musst auf keine syntaktischen/semantischen Feinheiten achten.
Hauptsache er liest sich flüssig.⁴¹
Algorithmische Lösungen sind am Ende aber die unkritischen. Sie müssen
gefunden werden, klar. Doch ihr Umfang ist gewöhnlich vergleichsweise
klein.Ichsagemaletwasflapsig:DerCodereinalgorithmischerLösungen
passt handschriftlich auf eine DIN A4 Seite. Das ist kein Umfang, der
für langfristig hohe Produktivität eine große Hürde darstellt. Solange
die Logik für eine algorithmische Lösung fokussiert in einer Funktion
steht und keine funktionalen Abhängigkeiten bestehen, wirst du dir ein
Verständnis erarbeiten können. Debugging hilft im Zweifelsfall.
Natürlich ist das eine Vereinfachung. Mir gehts hier aber um das big
picture. Wenn du auf einen “algorithmischen Kern” in einem Problem
gestoßen bist, dann modelliere mit einem Flowchart. Nur vermute ich,
dass du zu früh gewiss bist, dass ein Problem schon algorithmisch ist.
⁴¹Allerdings:Schaugenauhin!Hättestduesliebergehabt,dieLösungzuerstalsPseudo-
code oder zuerst als Flowchart präsentiert zu bekommen? Ich finde eine visuelle Lösung in
denmeistenFällenbesserzuüberblicken.Sieistzweidimensional,wasFallunterscheidungen
undSchleifenzugutekommt.ImtextuellenPseudocodemussalleslinearisiertwerden.


---


<!-- Page 88 of 584 -->


02-EntwurfimÜberblick 79
Du machst es dir damit zu schwer, ein Modell (oder später den Code) zu
finden.
Ich glaube, dass die meisten Probleme zuerst und vor allem prozessuale
Lösungen brauchen. In denen findest du dann keine Fallunterscheidun-
gen oder Schleifen, sondern lediglich Funktionsaufrufe. Die stehen für
SchritteineinemProzess,derdasgewünschteVerhaltenerzeugtdurchdie
Transformation von Eingabedaten in Ausgabedaten unter Verwendung
von Zustand und Ressourcen.
Auch ein Verhaltensmodell: ein Datenflussmodell für die allgemeine Funktionsweise von
Software-Funktionseinheiten
AlgorithmischeModellesindschonsehrnahamWie.ProzessualeModelle
hingegen zeigen vor allem das Was. Hier als Beispiel ein UML Sequenz-
diagramm aus Wikipedia⁴²:
⁴²https://en.wikipedia.org/wiki/Sequence_diagram


---


<!-- Page 89 of 584 -->


02-EntwurfimÜberblick 80
EinSequenzdiagrammalsVerhaltensmodell
Die durchgezogenen Pfeile stellen “Funktionsaufrufe” dar. Im Bild ruft
also der Computer den Server mehrfach auf im Rahmen der Lösung
des Problems “check mail”.⁴³
Das ist ein deutlich abstrakteres Verhaltensmodell als ein Flowchart. Hier
geht es nicht um einzelne Anweisungen, sondern lediglich um die zu
erledigendenSchritte.WiegenaueinSchrittwiesendUnsentEmailsein
⁴³Ich sage hier so kühn, dass es sich um Funktionsaufrufe handelt. Vielleicht liest du
jedoch lediglich Datenflüsse heraus: da fließen einfach Nachrichten zwischen Computer
und Server. Diese Interpretation ist für mich auch ok. Nur frage ich dich: Wie werden
denn diese Nachrichten verarbeitet? Von Logik! Und wo findest du diese Logik? Eingefasst
in Funktionen. Das ist die Coderealität: Am Ende erzeugt Logik das Verhalten - hier z.B.
Transformation einer newEmail-Nachricht in eineresponse-Nachricht - und diese Logik
steckt besserfür sichinbzw.hintergenaueinerFunktion,um klaridenfizierbar zusein mit
ihrerVerantwortlichkeit.


---


<!-- Page 90 of 584 -->


02-EntwurfimÜberblick 81
Teilverhalten erzeugt, ist unterhalb des Radars dieses Modells. Die Logik
dafürwürdestduineinertest-first Codierungfinden.Sieistganzbewusst
kein Bestandteil des Entwurfs.
Allerdings: Solange du in der Modellierung noch das Gefühl hast, dass so
eine Funktionseinheit wie der Block für sendUnsentEmail zu groß ist,
um in der Codierung zügig mit Logik gefüllt zu werden, solange solltest
du mit dem Modell noch nicht zufrieden sein. Aber dazu später mehr.
Im Verhaltensmodell liegt der Fokus auf dem Was. Deshalb werde ich
dir im Weiteren keine Flowcharts oder Pseudocode nahelegen. In beiden
steckt für mich zuviel Wie. Aber auch das Sequenzdiagramm werde ich
nicht weiter verwenden. Es skaliert ebenfalls nicht, wenn die Prozess-
schritte zu vielen “Akteuren” angehören (im Beispiel z.B. Computer).
Dennoch geben Sequenzdiagramme einen ersten Eindruck davon, wie ein
Verhaltensmodell grundsätzlich aussieht.
Abstraktion
Verhaltensmodelle und Datenmodelle beschreiben die zwei Seiten von
Software: Verarbeitung und Material. Das kann in ganz vielfältiger Weise
geschehen. Die obigen Modelle sind sollen dafür nur Beispiele sein, um
dir das Thema Modellierung etwas fasslicher zu machen.
Wenn du dir einen Eindruck von der Bandbreite an Modellierungsansätze
verschaffen willst, dann schau dir z.B. Bücher wie UML Distilled von
Martin Fowler⁴⁴ oder Modellierung: Grundlagen und formale Methoden
von Uwe Kastens⁴⁵ an. Du wirst erstaunt sein, wie vielfältig du Lösungen
ohne Code beschreiben kannst; oder manchmal auch nur Lösungsansätze,
denn einige Modellierungsmethoden ordne ich eher der vorgelagerten
Phase zu.
Egal aber, welchen Ansatz du insbesondere für die im Weiteren fokus-
sierte Verhaltensmodellierung wählen solltest, solltest du eines nicht aus
den Augen verlieren: die Umsetzung in Code. Beim Blick auf einen
Modellierungs- oder allgemeiner Entwurfsansatz frage ich mich immer:
⁴⁴UML Distilled: A Brief Guide to the Standard Object Modeling Language, Martin
Fowler,Addison-Wesley,ISBN978-0321193681
⁴⁵Modellierung: Grundlagen und formale Methoden, Uwe Kastens, Carl Hanser Verlag,
ISBN978-3446454644


---


<!-- Page 91 of 584 -->


02-EntwurfimÜberblick 82
“Und wo sind die Funktionen?” Denn die Funktionen sind die Container
für die Logik. Und die Logik ist das, was das Verhalten erzeugt und so
schwierig korrekt hinzubekommen ist. Und um sie korrekt zu erschaffen
und auch zu erhalten, ist ein test-first Vorgehen bei der Codiernung nötig.
Und dafür wiederum sind Funktionen als Ansatzpunkte zwingend.⁴⁶
Was du als und wie du in der Entwurfsphase die Lösung findest, am Ende
musstdusieineinemModellformalisiertformulieren,dasglasklarmacht,
welcheFunktionenmitwelchenVerantwortlichkeitenderCodeaufweisen
muss.
Diese funktionalen Atome, die alle ihren Beitrag leisten zum Gesamt-
verhalten, dürfen aber natürlich nicht “einfach herumliegen”. Vielmehr
müssen sie in Beziehung gesetzt werden, um ein Zusammenspiel zu
erreichen. Im Sequenzdiagramm oben ist das der Fall:
• Funktionen wie sendUnsentEmail oder deleteOldEmail sind
Verhaltensatome.
• Pfeile zwischen den “Akteuren” Computer und Server setzen
Funktionen in Beziehung, hier: checkEmail mit z.B. sendUnsen-
tEmail; erstere ruft letztere auf.
Und die “Akteure” selbst setzen Funktionen ebenfalls in Beziehung. Sie
fassen sie zusammen, hier: in Server sind sendUnsentEmail und
deleteOldEmail vereint.
Modelle als konkrete, formalisierte Lösungen und Ausgangspunkte für
deinen Code müssen damit mindestens Folgendes leisten:
• Atomisieren: Die noch zu findende Logik mit Funktionen, d.h.
Verhaltensatomen repräsentieren.
• Komponieren: Funktionen mit ihren Teilverhalten zu größerem
Verhalten zusammenfassen. Aus Verschiedenem wird etwas Neues.
• Aggregieren: Funktionen thematisch zusammenfassen. Aus Ähnli-
chem wird etwas Größeres.
⁴⁶SiehedazudenerstenBanddieserReihe:Test-firstCodierung


---


<!-- Page 92 of 584 -->


02-EntwurfimÜberblick 83
Dass Modelle außerdem auch noch die Daten, die die Funktionen verar-
beiten, beschreiben müssen, ist selbstverständlich. Wie gesagt, das halte
ich jedoch für ein vergleichsweise kleines Problem und sekundär. Wenn
du von der mainstream Objektorientierung geprägt sein solltest, mag dir
das merkwürdig erscheinen, doch versuche einmal deine Skepsis für die
folgenden Seiten auf Urlaub zu schicken.
Atomisieren, komponieren und aggregieren sind für mich Abstraktions-
leistungen. Für Details, Einzelteile, Feinheiten werden Begriffe gefunden,
mit denen es sich leichter umgehen lässt. Und das kann dann sogar auf
beliebig vielen Ebenen stattfinden.
Das Ergebnis ist ein Abstraktionsbaum mit beliebiger Tiefe für Komposite
und Aggregate.
Ohne einen solchen Baum in zwei Dimensionen - Komposition und
Aggregation - bekommen wir wachsende Lösungen einfach nicht in den
Griff, glaube ich. Er existiert am Ende de facto im Code – fragt sich nur,


---


<!-- Page 93 of 584 -->


02-EntwurfimÜberblick 84
wieeszuihmgekommenist.Wardas“Zufall”,“hatessichergeben”?Oder
hast du ihn bewusst entworfen? Ich plädiere für Letzteres.
Plane deine Abstraktionen. Plane sie vor allem nicht allein, sondern ge-
meinsam mit deinen Entwicklerkollegen. Strebe nicht nur nach collective
code ownership⁴⁷, wie es einmal im eXtreme Programming heißt. Ich
meine, es muss auch ein collective design ownership geben. Ihr müsst alle
zusammenhinterdenAbstraktionenstehen,diedieLösungrepräsentieren
und formen.
Die soziale Dimension eines Entwurfs ist nicht zu verachten. Er ist ein
Werkzeug für’s Denken wie für’s Kommunizieren. Deshalb ist es auch
nicht so wichtig, dass ein Entwurf “für sich selbst stehen kann”. Lege
deinen Lösungsansatz oder auch dein Modell nicht einfach jemandem zur
Weiterverarbeitung stumm vor. Beide sind bei allem Detailreichtum “nur”
Gesprächsanlässe.EntwürfemüssenfürdieWeiterverarbeitungmitErklä-
rungen übergeben werden. Am besten geschieht das im Dialog, zur Not
schriftlich oder per Video. Je mehr Interaktionsmöglichkeit zwischen dem
Empfänger deines Entwurfs und dir, desto besser. Denn der Empfänger
wird Fragen haben. Er muss Fragen haben, weil du nie alles, was dir zu
einerLösungimKopfherumgeht,vollständigineinemEntwurffesthalten
kannst.
Zusammenfassung
Im Entwurf findest du zuerst eine Lösung und formalisierst sie dann
abstrakt.Fürmichgiltdabei:Behaviorfirst,datasecond.Wasdasbedeutet,
wirst du in den folgenden Kapiteln sehen.
Während du in der Lösungsfindung noch sehr frei bist, was den visuellen
Ausdruck angeht - und visuell sollte er sein! -, engt die das Modell jedoch
ganz bewusst sein. Seine Abstraktionen sollten so gestaltet sein, dass du
sie leicht in Codestrukturen übersetzten kannst.
EsgibteineVielzahlanModellierungswerkzeugen.Manchemachenesdir
schwerer, andere leichter, diese Forderungen zu erfüllen. In den folgenden
Kapiteln stelle ich dir den Ansatz vor, von dem ich meine, dass er für dich
⁴⁷https://explainagile.com/agile/xp-extreme-programming/practices/collective-code-
ownership/


---


<!-- Page 94 of 584 -->


02-EntwurfimÜberblick 85
derersteseinsollte,durchdessenBrilleduaufeineLösungschaust,umsie
zuformalisieren.Nichtdereinzige,aberdererste,deinDefault.Eristbreit
einsetzbar und leichtgewichtig, wie ich dir hoffentlich vermitteln kann.
Andere Ansätze hab gerne auch in deinem Entwurfsköcher – doch gerade
um deine Lösungen in groben Strichen zu skizzieren für “das Ausmalen”
in der Codierung, halte ich das Flow-Design, wie ich es nenne, für ideal.


---


<!-- Page 95 of 584 -->


02-EntwurfimÜberblick 86
Übungsaufgaben
Reflexionsaufgabe
Bitte formuliere eine Frage oder eine Erkenntnis zum Kapiteltext.
• Wo bist du gedanklich hängengeblieben, was ist dir unklar,
was passt für dich irgendwie nicht zusammen, wozu würdest
du dir noch etwas mehr Erklärung wünschen? Steht irgendet-
waszudeinerbisherigenPraxisimWiderspruchunddufragst
dich, warum du etwas ändern solltest?
• Oder: Wann hast du einen Aha-Moment gehabt, was ist
diralsbemerkenswert,spannend,ausprobierenswertaufgefal-
len? Hat irgendetwas “in dir Klick gemacht”, weil dir nun ein
Zusammenhang aufgegangen ist? Oder verstehst du jetzt aus
deiner bisherigen Praxis irgendetwas besser?
Am besten formulierst du Frage bzw. Erkenntnis schriftlich. Indem
du deine Gedanken aufschreibst, wirst du dir ihrer bewusster. Bei
einer Frage kommst du dadurch vielleicht schon einer Antwort aus
dir selbst heraus näher. Bei einer Erkenntnis fällt dir vielleicht schon
etwas ein, das du ab jetzt anders machen kannst.
Aufgabe - Lösungsansatz finden
Die SARS-CoV-2 Pandemie 2020 hat vielleicht das Interesse für Statis-
tik in der Bevölkerung nicht erhöht, doch zumindest haben jetzt mehr
Menschen von Begriffen wie Sensitivität und Spezifizität gehört und dass
ein positives Testergebnis auf SARS-CoV-2 Infektion weder notwendig
eine Erkrankung bedeutet, noch zwingend korrekt ist. Aus diesem An-
lass folgende Aufgabe, der so genannte Bedingte Wahrscheinlichkeiten
zugrundeliegen. Das ist Mathematik, die nicht jedem jenseits der 4. Klas-
se Spaß gemacht hat, doch es ist keine höhere Mathematik und lässt
sich mit ein bisschen googlen zu dem Begriff gut erkunden; mehr als
Grundrechenarten sind nicht nötig. Dass du dich mal mit Bedingten


---


<!-- Page 96 of 584 -->


02-EntwurfimÜberblick 87
Wahrscheinlichkeiten auseinandersetzt, ist ein Gewinn fürs Leben. Da bin
ich gewiss.
Entwickle bitte nur einen Lösungsansatz für folgende Anforderungen.
Der Auftraggeber wünscht ein Programm, mit dem Anwender be-
stimmenkönnen,wiehochdieWahrscheinlichkeiteinerErkrankung
bei einem positiven Testergebnis ist.
Ein Beispiel aus der Literatur:
EinProzentderFrauen,diesichregelmäßigeinerMam-
mogrphie unterziehen, haben Brustkrebs. In 80% der
Fälle ergibt sich für Frauen mit Tumoren in der Brust
einpositiverBefund.In9,6%derFällezeigtsichjedoch
auch bei gesunden Frauen ein positiver Befund.
Wie wahrscheinlich ist es nun, dass eine Frau mit positivem Test-
ergebnis auch tatsächlich Brustkrebs hat?
Nur etwas 15% der Ärzte, denen diese Frage mit den Angaben
vorgelegtwurde,konntensiekorrektbeantworten.Daslegteinerseits
weitere Ausbildung nahe, aber auch Unterstützung durch Software
kann helfen.
Das Programm soll auf einer Datenbank basieren, die Prävalenzen
für Diagnosen enthält, aber auch Sensitivität und Spezifizität zu-
gehöriger Tests. Beispiel für einen Eintrag in Bezug auf das obige
Mammographie-Szenario:
1 Test: Mammographie
2 Diagnose: Brustkrebs
3 Prävalenz: 0,01
4 Sensitivität: 0,8
5 Spezifizität: 0,904
Der Anwender sucht nach Test oder Diagnose und gibt an, ob
der Test positiv oder negativ ist. Das Programm gibt daraufhin die
Wahrscheinlichkeit aus, dass das Testergebnis tatsächlich korrekt ist.
Beispiel für das obige Szenario:


---


<!-- Page 97 of 584 -->


02-EntwurfimÜberblick 88
1 $ ergebnischeck.exe mammographie positiv
2 Die Wahrscheinlichkeit für eine korrekte positive Diagnose von 'Brustkrebs' ist: 0,078.
3 Nur bei ca. 8 von 100 getesteten Personen ist die Aussage des Tests korrekt.
4 $
Ward Casscells, B.S., et al.; Interpretation by
Physicians of Clinical Laboratory Results, 1978,
https://www.nejm.org/doi/full/10.1056/NEJM197811022991808
Weder Modell, noch Codierung sind nötig. Mach dir also nicht zu viel
Arbeit. Überlege, was hier wirklich “entwurfswürdig” nur in Bezug auf
einen Lösungsansatz ist. Konzentriere deinen Lösungsansatz darauf. Sei
so visuell wie möglich. Anhand deines Lösungsansatzes solltest du die
Lösung jemand anderem leicht erklären können.


---


<!-- Page 98 of 584 -->


03 - Radikale
Objektorientierung
Die Wahrscheinlichkeit ist groß, dass du deinen Code in einer objekt-
orientierten Programmiersprache schreibst. Der TIOBE Index⁴⁸ listet im
SeptemberunterdenTop10Programmiersprachen6objektorientierte,die
ca. 40% der Popularität aller Sprachen auf sich versammeln.
Seit Ende der 1980er hat das Paradigma der Objektorientierung (OO) aus-
gehend von C++ immer weiter Eingang in Programmiersprachen gefun-
den. War es vorher eher von akademischem Interesse, ist das Paradigma
seitdem zum Mainstream geworden. Für mich dauerte die Hochphase
dieser Entwicklung von ca. 1995 bis 2015 - ist nun also schon einige Zeit
vorüber.⁴⁹
Natürlich gibt es noch Unmengen an Code in OO-Sprachen und die
Objektorientierung ist auch nicht tot. Ihr Dominanzanspruch jedoch
ist gebrochen. Die Zukunft gehört meinem Empfinden nach hybriden
Sprachen, die Objektorientierte Programmierung (OOP) mit Funktionaler
Programmierung(FP)verbindenundweiterefrischeIdeendazugeben.F#,
⁴⁸https://www.tiobe.com/tiobe-index/
⁴⁹Auch wenn C++ bereits 1985 kommerziell verfügbar war, hat es noch einige Jahre
gedauert,bismitdiesemWerkzeuggenügendErfahrungengesammeltwordenwaren,damit
ein breites Publikum daraus auch Nutzen ziehen konnte. Den Beginn dieser Phase stellt
für mich die Veröffentlichung des Buches Design Patterns: Elements of Resuable Object-
OrientedSoftwaredar.MitderVeröffentlichungvonJavaimJahr1995nahmdieVerbreitung
anschließend weitere Fahrt auf. Für mich hat dann nicht C++ die Objektorientierung
populärgemacht,sondernJavaalsballastarme,pragmatischeAlternative.Darausunddarum
herum haben sich anschließend weitere objektorientierte Sprachen wie C#, Ruby, Python
entwickelt - doch Java führt diese Riege immer noch mit Abstand an. Gleichzeitig zeigt
mirnunJavaaberauch,seitwanndieObjektorientierunganFührungsrolleundBedeutung
einbüßt. Das ist seit 2015 mit dem Release 8 der Fall, in dem Java Streams eingeführt
hat, die ein nicht zu übersehendes Konstrukt aus der Funktionalen Programmierung sind.
Wenn das nun Einzug in eine, nein, in die objektorientierte Sprache schlechthin hält,
dann scheint mir das Paradigma ausgereizt. Spätestens 2015 ist also aus meiner Sicht die
Dämmerung der Objektorientierung unübersehbar angebrochen. Und die Geschwindigkeit
mit der sich weitere Elemente der Funktionalen Programmierung in C#, C++, Java und
anderenobjektorientiertenSprachen“einnisten”,machtdasjedenTagdeutlicher.


---


<!-- Page 99 of 584 -->


03-RadikaleObjektorientierung 90
Go oder Rust gehören für mich in die Riege der Sprachen, die den OOP-
Mainstream transzendieren.
DochauchdieOO-SprachenselbstsindnochnichtamEnde.Insbesondere
C# entwickelt sich organisch mit FP-Konstrukten weiter; meine Vermu-
tung ist, dass C# das Beste aus F# so weit assimiliert, dass immer weniger
Motivation bestehen wird, die Sprache zu wechseln, um die Vorteile der
FP zu ernten.
Was haben nun aber OOP oder auch FP mit dem Softwareentwurf zu tun?
Ichwürdesagen:aufunterschiedlicheWeiseeineMenge.DerSoftwareent-
wurf ist eng verknüpft mit der Objektorientierung und seine Zukunft liegt
meiner Meinung nach in der Nähe der Funktionalen Programmierung.
Die Welt bestehend aus Objekten?
Vor der Objektorientierung war Software “einfach nur abstrakt”. Was
hatten Maschinencode, Assembler-Sprachen oder auch strukturierte Spra-
chen wie C oder Pascal mit der Welt zu tun? Code war in der Welt
so wenig zu finden wie mathematische Formeln. Nicht umsonst war
die Programmierung etwas für Nerds, die weltfern in einem Keller bei
Pizza und Cola vor sich hinwerkelten. Oder so ähnlich war die laienhafte
Vorstellung von Softwareentwicklung.⁵⁰
ÜberJahrzehntestanddieProgrammierungderMathematiknahe.Großes
Abstraktionsvermögen sei gefragt, so hieß es, wenn man den Computer
unter Kontrolle bringen wolle.
Und dann kam die Objektorientierung! Ihre Verheißung war, die Pro-
grammierung endlich aus den Höhen der Abstraktion in die Niederungen
des Konkreten, des Greifbaren herunterzuholen. Besteht die Welt um
uns herum nicht aus Objekten? Bestehen Maschinen nicht aus Objekten?
Autos fahren über Straßen und bleiben an Ampeln stehen; im Auto
arbeiten Motor, Kurbelwelle, Räder, Achsen, Lenkrad usw. usf. zusammen.
Objekte,wohinmanschaut!UndistSoftwareamEndenichtauchnureine
⁵⁰Zumindest entwickelte sich ein solches Bild ab Mitte der 1970er, als Computer so
erschwinglichwurden,dassjedermansichdamitauchzuhausebeschäftigenkonnte.Vorher
wardasikonischeBildwohleherdaseinesWissenschaftlersoderIngenieurs,deranteuren,
großen Maschinen im weißen Hemd oder gar noch im Laborkittel mysteriöse Handlungen
vollführte.SpäterwardieikonischeKleidungehereinbekleckertesT-Shirt.


---


<!-- Page 100 of 584 -->


03-RadikaleObjektorientierung 91
Maschine, wenn auch eine virtuelle, die ebenfalls am besten aus Objekten
bestehen sollte?
Soweit die Implementationssicht. Aus ihr leitet sich allerdings auch eine
Analysehaltung ab: Sollten Probleme nicht daraufhin untersucht werden,
welche Objekte darin eine Rolle spielen? Macht die Objektorientierung es
nicht einfacher, Anforderungen zu verstehen und dann auch umzusetzen,
weil die programmiersprachlichen Mittel näher an die realen, materielle
Welt herangerückt sind?
Nicht jedoch allein die OOP verhieß eine Revolution der Softwareent-
wicklung. Die Objekteorientierung trat im Triumvirat auf: OOA (Ob-
jekorientiere Analyse), OOD (Objektorientiertes Design) - zusammen
OOAD genannt⁵¹ mit OOP zusammen sollte die Softwareentwicklung in
eine neue Ära katapultieren. Und im Schlepptau folgte dann die UML
(Unified Modeling Language)⁵² ebenfalls ab Mitte der 1990er, um diesen
Vorstellungen auch angemessen visuellen Ausdruck verleihen zu können.
Ich kann mir erinnern, wie aufgeregt ich 1989/1990 war, als ich das
erste Mal mit C++-Compilern arbeiten konnte. Sogar nach London bin
ich geflogen zu einem C++-Workshop, um diesen Quantensprung in der
Programmierung erleben zu dürfen, noch bevor ich selbst einen C++-
Compiler auf meinem Rechner einsetzen konnte. Mit C hatte ich einige
Jahre Erfahrung; doch C++ versprach so viel mehr durch die Objektorien-
tierung.
Ja, so war das damals. Eine aufregende, verheißungsvolle Zeit. Objekt-
orientierung schien das, worauf die Programmierwelt gewartet hatte, um
endlichdurcheineProduktivitätsbarrierezubrechenundmehrMenschen
an die Codierung heranzuführen.
Die Rettung kam dann jedoch für mich persönlich aus einer ganz anderen
Richtung. An C++ habe ich mich ohne viel Erfolg abgemüht. Java war
danach nur ein kurzer Hoffnungsblitz. Viel pragmatischer, viel hilfreicher
war eine ganz andere Sprache für mein damaliges Business. Wir hatten
keine Zeit, uns in Theorie zu ergehen, sondern mussten unsere Kunden
bedienen. Das war viel einfacher möglich mit Visual Basic. Mehr als
10 Jahre war diese Sprache für mich synonym mit Produktivität und
⁵¹https://de.wikipedia.org/wiki/Objektorientierte_Analyse_und_Design
⁵²https://en.wikipedia.org/wiki/Unified_Modeling_Language


---


<!-- Page 101 of 584 -->


03-RadikaleObjektorientierung 92
Konkretheit - auch und weil sie eben nicht sauber dem Paradigma der
aufstrebenden mainstream Objektorientierung entsprach.
Dieser Kontrast zwischen dem Ideal und dem Pragmatismus, dem An-
spruch und der Realität hat mich seitdem geprägt, denke ich. Damals im
Jahr 1990 als ich in einem Projekt in Italien in einem schlecht gelüfteten
Großraumbüro saß und versuchte, mit der Objektorientierung und C++
Anforderungen umzusetzen und gnadenlos scheiterte, wurde der Same
gesät für das Buch, was du jetzt liest. Damals ist in mir eine Spannung
entstanden,die mich all die Jahrzehnte nicht verlassenhat. Es ist die Span-
nung zwischem den Ambitionen des Paradigmas der Objektorientierung,
wie sie im entstehenden Mainstream verstanden wurde, und dem, was in
konkreten Projekten daraus dann geworden ist.
Die Objektorientierung - genauer: einzelne Features von OOP-Sprachen -
finde ich selbstverständlich hilfreich; auf sie möchte ich nicht verzichten.
Doch die Objektorientierung, wie sie damals vermittelt wurde und auch
noch heute durch die Köpfe spukt, halte ich für nicht weniger als fehl-
geleitet und kontraproduktiv. Für die Zwecke der Softwareentwicklung
die Welt primär als bestehend aus Objekten zu verstehen, weist für mich
in die falsche Richtung bei der Entwicklung von Software. Denn in der
Entwicklung von Software beginnt der kreative Prozess quasi im Nichts.
Es gibt keine Objekte. Die sind vielmehr Abstraktionen am Ende der
Entwicklung. Sie an den Anfang zu stellen, ist für mich eine vorzeitige
Optimierung, die einschnürt und inflexibel macht in einer Phase, wo
Flexibilität das Wichtigste ist.
Vielleicht hast du bemerkt, dass ich die Objektorientierung qualifiziert
habe mit “mainstream”. Das ist mir wichtig, denn die Objektorientierung,
die sich seit Mitte der 1980er ausgebreitet hat, halte für eine begrenzte,
vereinfachte, gar verirrte Entwicklung des ursprünglichen Begriffs. Wann
dieDegenrationdesBegriffseingesetzthat,weißichnicht.Washeuteaber
in den Köpfen der meisten Entwickler zu finden ist, entspricht nicht der
ursprünglichen Idee. Die finde ich nämlich sehr wertvoll und will sie dir
gleich ausführlich vorstellen.
Dass die Welt im Allgemeinen und softwaretechnische Problemlösungen
imBesonderenausObjekten,alsoDingenbestehe,dieeszufindenbzw.zu
bauen gilt, glaube ich nicht. Nur in sehr, sehr begrenztem Umfang habe
ich Software gesehen, wo dieser Gedanken irgendetwas besser gemacht
hätte.


---


<!-- Page 102 of 584 -->


03-RadikaleObjektorientierung 93
Nein, die Wiederverwendbarkeit, die die Prozession zur Krönung der
Objektorientierung als herrschendes Paradigma vor sich hergetragen hat,
ist keine Errungenschaft der Objektorientierung. Wiederverwendbarkeit
hat es lange vor der OOP mit anderen Sprachen schon gegeben.
Und auch die Vererbung als charakteristisches Feature der OOP sehe
ich nicht als Gewinn. Nicht umsonst wurde sie schon 1995 mit Java
deutlich eingeschränkt gegenüber C++ und seitdem auch nicht wieder
in ursprünglicher Form in anderen Sprachen implementiert, wenn ich es
recht sehe.
Die mainstream Objektorientierung hat den Anspruch gehabt, Software-
lösungen deutlich leichter denken und implementieren zu können, also
beim Softwareentwurf zu helfen. Diesem Anspruch ist sie allerdings nur
begrenzt gerecht geworden. Dass die UML weitgehend nicht genutzt
wird von Entwicklern für den Entwurf, ist für mich ein zusätzliches
Symptom für ein Defizit der mainstream Objektorientierung. Es existiert
eine Spannung zwischen Anspruch und Realität. Immer noch.
DieseSpannungmöchteichfürdichauflösen.DieObjektorientierunghilft
beim Softwareentwurf. Nur ist es nicht die mainstream Objektorientie-
rung. Die Welt besteht nicht zuvörderst aus Objekten! Das, “was die Welt
im Innersten zusammenhält”, ist Kommunikation. Um Softwarelösungen
vordenken zu können, muss der Fokus vom Objekt auf die Beziehung
wechseln.
Der Ursprung der Objektorientierung
Wenn du bei Wikipedia “Objektorientierung”⁵³ nachschlägst, dann findet
sich in dem Beitrag keine Erwähnung des Ursprungs des Begriffs. Weder
wird sein “Erfinder” genannt, noch das Jahr, in dem der Begriff geprägt
wurde. Und schon gar nicht wird das Wichtigste näher erläutert, was
seinen “Erfinder” überhaupt angetrieben hat, ihn zu prägen. Das alles
finde ich sehr bezeichnend für die spätere Entwicklung. Es ist für mich
kein Wunder, dass die Objektorientierung so un- oder missverstanden,
⁵³https://de.wikipedia.org/wiki/Objektorientierung


---


<!-- Page 103 of 584 -->


03-RadikaleObjektorientierung 94
keinen günstigeren Einfluss auf den Softwareentwurf genommen hat.⁵⁴
Weil ich das Potenzial in der ursprünglichen Vorstellung von Objektori-
entierung für sehr groß halte, möchte ich diesem Missstand hier abhelfen.
Ich möchte dir eine radikale Objektorientierung vorstellen und der main-
stream Objektorientierung gegenüberstellen.
• Radikal nenne ich sie, weil sie zurück an die Wurzel des Begriffs
geht; lat. radix bedeutet Wurzel (Pons⁵⁵).
• Außerdem ist sie für mich radikal, weil sie sich “mit Rücksichtslo-
sigkeit und Härte” (Duden⁵⁶) gegen überkommene atrophierte, fehl-
geleitete Vorstellungen der mainstream Objektorientierung stellt.
Wer hat’s erfunden?
“Erfinder” des Begriffs Objektorientierung (object-orientation) war Alan
Kay⁵⁷, ein viel geehrter Pionier moderner Softwareentwicklung. Seinem
breiten Background als Musiker und Mathematiker und Molekularbiologe
und Informatiker schreibe ich zu, dass er intuitiv auf ein faszinierendes
Konzept gestoßen war. In einem Email-Thread⁵⁸ erinnert er sich so:
“It was probably in 1967 when someone asked me what I was
doing, and I said: ‘It’s object-oriented programming’.”
⁵⁴Vielleichtwidersprichstdumirhier.IstdennnichtvielGutesmitOO-Sprachenindie
Programmierwelt gekommen? Sind wir heute nicht produktiver als vor 30-40 Jahren? Hilft
denn nicht auch die Vorstellung von Objekten beim Entwurf von Software? Ja, durchaus.
Da ist etwas dran. Ich will das nicht ganz abtun. Wie gesagt, verzichten möchte ich nicht
auf die OO-Features in Hochsprachen wie C# oder Java oder C++ oder Ruby, auch wenn
sie durchaus inkonsistent untereinander und mit der ursprünglichen Idee implementiert
sind.Allerdingswageichzubezweifeln,dasssgeradedeshalbdieProduktivitätheutedaist,
wo sie ist. Das halte ich eher für einen Effekt gestiegener Rechnerleistungen. IDEs machen
uns heute produktiv. Oder das Internet als Quelle von Informationen und Bibliotheken und
Paketmanager. Die Konzepte der mainstream Objektorientierung hingegen haben für mich
nureinenrelativkleinenEffekt.Objectsfirst istnichtderallesbeschleunigendeGedankebei
derUmsetzungvonAnforderungeninCode.
⁵⁵https://de.pons.com/%C3%BCbersetzung/latein-deutsch/radix
⁵⁶https://www.duden.de/rechtschreibung/radikal
⁵⁷https://de.wikipedia.org/wiki/Alan_Kay
⁵⁸http://userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en


---


<!-- Page 104 of 584 -->


03-RadikaleObjektorientierung 95
Die Objektorientierung ist also knapp 20 Jahre älter als C++. Der Begriff
wurde knapp nach den ersten Schritten in die Strukturierte Programmie-
rung⁵⁹ geprägt - und war damit wahrscheinlich seiner Zeit voraus.
Das, was Alan Kay sich vorgestellt hatte, war für Entwickler, die noch
gefangenwareninSpaghetti-Code,zufortgeschritten.BisMitteder1980er
mussten sie zuerst die Logik in den Griff bekommen mit den Mitteln
der Strukturierten Programmierung. Dann konnten sie sich langsam um
“höhere Strukturen” kümmern. Die Modularisierung im Allgemeinen war
noch in den Kinderschuhen.
Alan Kay hat dann versucht, mit der Sprache SmallTalk⁶⁰, seiner Idee
eine konkrete, nutzbare Form zu geben. Aber auch wenn diese Sprache
BeachtungundFreundegefundenundaucheinigenEinflussausgeübthat,
hat sie es allerdings nie in den Mainstream geschafft. Die Popularisierung
des Begriffs, wenn auch nicht wirklich des dahinter stehenden Konzepts,
ist C++ und Java zu verdanken, würde ich sagen. So wie das Konzept
war auch SmallTalk seiner Zeit voraus als integrierte Metaprogrammier-
plattform. Oder beides war zu weit weg von der Erfahrungswelt der
meisten damaligen Entwickler, die mit Assembler, Fortran, Cobol, C,
Pascal oder Basic versuchten, Problemlösungen zu implementieren. Die
imperative, zuerst unstrukturierte, dann strukturierte Programmierung
war zu dominant. “Kontrollflussdenke” herrschte vor - und war so ganz
anders als das, was Alan Kay im Sinn hatte.
Die zentrale Analogie der radikalen
Objektorientierung
Was hatte Alan Kay im Sinne mit dem Begriff “Objektorientierung”? Er
drückt das so aus⁶¹:
“I thought of objects being like biological cells and/or indivi-
dualcomputersonanetwork,onlyabletocommunicatewith
messages […]”
⁵⁹https://de.wikipedia.org/wiki/Strukturierte_Programmierung
⁶⁰https://en.wikipedia.org/wiki/Smalltalk
⁶¹http://userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en


---


<!-- Page 105 of 584 -->


03-RadikaleObjektorientierung 96
Passt diese Analogie zu dem, was du in deinem Projektalltag an so
genanntem objektorientierten Code siehst? Fühlen sich für dich deine
Objekte wie “biologische Zellen” an? Kommunizieren deine Objekte nur
mit “Nachrichten”?
Für Alan Kay waren Objekte soetwas wie Organismen, also autonome
“Entitäten”, wie in diesem Bild einer motorischen Endplatte⁶², bei der
Nervenzelle und Muskelzelle aufeinander treffen:⁶³
Denkst du in dieser Weise über deine Objekte nach? Empfindest du die
sprachlichen Mittel in C++ oder Java oder C# als diesem Bild entspre-
chend?
Nach meiner eigenen Erfahrung und den Reaktionen von Entwicklern,
denen ich diese ursprüngliche Idee von Alan Kay vorgestellt habe, glaube
ich, dass dir das sehr fremd und weit von deiner Coderealität entfernt
vorkommt.
Das halte ich auch für kein Wunder. Denn die zentrale Idee ist irgendwo
auf dem Weg von Alan Kays Kopf zu dem, wie heute Objektorientierung
⁶²https://de.wikipedia.org/wiki/Motorische_Endplatte
⁶³Bildquelle:DoctorJana,CCBY4.0


---


<!-- Page 106 of 584 -->


03-RadikaleObjektorientierung 97
vermittelt wird, verloren gegangen.
Und was ist die zentrale Idee? Alan Kay sagt⁶⁴:
“The big idea is ‘messaging’ […]”
und er sagt⁶⁵
“[objects are] only able to communicate with messages […]
messaging came at the very beginning […]”
Messaging, d.h. die Kommunikation mittels Nachrichten, war für Alan
Kay das Erste, das Wichtigste, der Kern von Objektorientierung. Dass
das missverstanden wurde und der Mainstream sich auf die Objekte
fokussierte, ist ihm dann irgendwann selbst aufgestoßen⁶⁶:
“I’m sorry that I long ago coined the term ‘objects’ for this
topic because it gets many people to focus on the lesser idea.”
Es geht eben nicht um die Objekte in der Objektorientierung, sondern
umdieNachrichten,alsoumdieKommunikationzwischen“irgendetwas”,
dasAlanKayunterUmgehungdesüberstrapaziertenBegriffs hiereinfach
“Modul” nennt⁶⁷:
“Thekeyinmakinggreatandgrowablesystemsismuchmore
to design how its modules communicate […]”
Und so definiert er objektorientierte Programmierung⁶⁸ am Ende sogar
ohne Objekte als:
”[…] only messaging, local retention and protection and hi-
ding of state-process, and extreme late-binding of all things.”
⁶⁴http://lists.squeakfoundation.org/pipermail/squeak-dev/1998-October/017019.html
⁶⁵http://userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en
⁶⁶http://lists.squeakfoundation.org/pipermail/squeak-dev/1998-October/017019.html
⁶⁷http://lists.squeakfoundation.org/pipermail/squeak-dev/1998-October/017019.html
⁶⁸http://userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en


---


<!-- Page 107 of 584 -->


03-RadikaleObjektorientierung 98
Sind C++, Java, C# insofern objektorientierte Programmiersprachen? Nur
bedingt, würde ich sagen.
• Kapselung von Daten (Zustand) - “local retention and protection
and hiding of state-process” - ist ein Kinderspiel gerade bei streng
typisierten Sprachen. Objekte instanziiert aus Klassen können alle
verschiedenen Zustand haben, der nach außen nicht sichtbar ist.
• Auf “extreme late-binding of all things” sind viele Sprachen nicht
ausgelegt. Im Gegenteil: die vorherrschende strenge Typisierung
macht es schwer, zur Laufzeit flexibel zu entscheiden, welche
Objekte miteinander kommunizieren sollen. Interfaces sind um-
ständlich, dynamische Programmierung ist gar nicht oder nur um-
ständlicher möglich. Ruby, Python oder JavaScript sind in dem
Sinne objektorientierter.
• Benutzen nun aber die Objekte, die in C++, Java oder JavaScript
Programmen instanziiert werden, “only messaging” zur Kommu-
nikation? Ich behaupte: Nein, gerade das tun sie nicht. Objekte
rufen auf anderen Funktionen auf. Dabei übergeben sie Daten als
Parameter und bekommen Daten als Resultate zurück. Das ist für
mich nicht einfach Messaging, wie Alan Kay es sich gedacht hatte.
Seine Motivation hinter der Objektorientierung drückt Alan Kay so aus⁶⁹:
“Iwantedtogetridofdata.[and]Irealizedthatthecell/whole-
computer metaphor would get rid of data, […]”
Ist das auch deine Motivation, warum du eine objektorientierte Sprache
benutzt?ErreichstdudasZiel“getridofdata” indeinemCode?Daswage
ich zu bezweifeln. Denn die Kernidee von Alan Kay ist ja untergegangen:
Messaging.
Das macht die Wurzel der Objektorientierung so radikal für mich: der
Fokus auf die Nachrichten. Die Welt wird eben nicht zuerst in Objekte
unterteilt, die halt irgendwie von einander abhängen. Stattdessen geht es
zuerst um Kommunikation. Damit ist der Fokus auf dem, was passiert -
entweder schon passiert ist oder noch passieren soll. Das Tun steht im
Vordergrund, nicht das Haben.
⁶⁹http://userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en


---


<!-- Page 108 of 584 -->


03-RadikaleObjektorientierung 99
Für mich ist das eine um 180° gedrehte Weltsicht im Verhältnis zur main-
streamObjektorientierung. DiekonzentriertsichvorallemumdasHaben:
Objekte sind die, die Daten haben. Deshalb springen viele Entwickler bei
der Anforderungsanalyse so schnell auf Datenstrukturen an. Sie suchen
förmlich die Datenstrukturen, um dann darauf Funktionen zu verteilen.
IchzieheausAlanKaysursprünglicherIdeejedocheinenanderenSchluss.
Ich möchte dir aus seiner Zellenanalogie abgeleitet nahelegen, dich zuerst
auf das Verhalten zu konzentrieren:
1. Was muss getan werden? Am Anfang stehen Nachrichten.
2. Wer kann das tun? Dann geht es um Objekte.
3. Wer sollte welche Daten haben? Und erst zum Schluss geht es
darum, welchen Zustand Objekte haben sollten.
Keine Angst, nur weil die radikale Objektorientierung dein Weltbild
vielleicht auf den Kopf stellt, ist nicht alles falsch, was die mainstream
Objektorientierung hervorgebracht hat. Klassen, Objekte, Funktionen, In-
terfaces,Vererbung…alldasbleibtdirerhalten.Allerdingsplädiereichfür
einen anderen Umgang damit.
Und dieser andere Umgang mit deiner objektorientierten Programmier-
sprache ist gegründet in einer anderen Vorstellung von Software. Der
Codierung geht also ein Konzept voraus. Damit sind wir beim Entwurf.
Die radikale Objektorientierung ist mir so wichtig, weil sie das Denken
und damit die Lösungsfindung und -beschreibung beeinflusst. Für dich
mag OOP ein Thema der Codierung sein; für mich ist OOP viel mehr und
dem weit vorgelagert. Es geht um eine Grundhaltung. Dass sich zur OOP
nochOOAundOODgesellthaben,istfürmichnichtverwunderlich.Alles
andere wäre auch zu kurz gesprungen. Insofern hältst du hier sogar ein
OOD-Buch der anderen Art in den Händen.
Aber ich will den Begriff Objekt gar nicht so strapazieren. Wenn es
für dich das ist, was durch die Instanziierung einer Klasse entsteht und
dessen Daten zur Laufzeit auf dem Heap liegen, statt auf dem Stack,
dann soll es mir recht sein. Es ist halt ein Laufzeitcontainer mit einer
bestimmten Verantwortlichkeit und einem gewissen Zustand. Wofür du
so ein technisches Ding in deinen Lösungen benutzen kannst, wirst du
schon sehen.


---


<!-- Page 109 of 584 -->


03-RadikaleObjektorientierung 100
Vor diesem praktischen Teil muss ich dich aber leider noch einen Moment
mit etwas “Theorie” belästigen. Alan Kay hat zwar mit seinem Bild
der kommunizierenden biologischen Zellen eine wunderbare Analogie
gezeichnet – doch was bedeutet die in der Praxis? Was ist das von ihm
aufs Podest gestellte Messaging konkret?
Principle of Mutual Oblivion (PoMO)
Alan Kay schwebte eine fundamentale Struktur von Software vor, in
der “geschlossene” Einheiten gemeinsam operieren durch Austausch von
Nachrichten. Körperzellen oder Computer in einem Netzwerk sind gut
fassliche Bilder dafür - aber bevor wir damit etwas bei der Programmie-
runganfangenkönnen,müssenwirdavonabstrahieren.WashatAlanKay
uns also ganz allgemein mit seinem Konzept sagen wollen?
Ich vereinfache dafür mal das obige Bild der motorischen Endplatte
radikal unter Nutzung von Alan Kays Begriffen:
• Es geht um ein Objekt für die Nervenzelle
• und ein weiteres Objekt für die Muskelzelle
• zwischen denen die Moleküle des Neurotransmitters Acetylcholin
(ACh) als Nachrichten fließen.


---


<!-- Page 110 of 584 -->


03-RadikaleObjektorientierung 101
SchemaderObjektorientierung
Damit sind wir raus aus der schwammigen, feuchten, komplexen Biologie
und drin in der klaren, harten und einfachen Programmierung. Oder so
ähnlich. Jedenfalls sehen zwei Ellipsen (oder Kreise oder Rechtecke) und
ein Pfeil dazwischen nicht mehr so verwirrend aus, würde ich sagen.
Lass das Bild auf dich wirken. Diese Darstellung halte ich wirklich für
die völlig legtime Vereinfachung dessen, worum es Alan Kay in seiner
Analogie ging. Ja, so einfach hatte er sich das gedacht. Zumindest sieht
es einfach aus. Leider ist es das aber nicht wirklich. Der Teufel steckt im
Detail bzw. in den Auslassungen.
Details und Auslassungengibt es, weilmanches für Alan Kaywahrschein-
lich ganz selbstverständlich war. Immerhin war er zunächst einmal Mole-
kularbiologe und Mathematiker. Da hat er sich vielleicht nicht vorstellen
können, was geplagte Programmierer eben nicht für selbstverständlich
halten. Lass mich deshalb versuchen, das vereinfachte Bild für dich zu
deuten.


---


<!-- Page 111 of 584 -->


03-RadikaleObjektorientierung 102
Unabhängigkeit
AufderHandsolltevorallemliegen,dassObjektegedachtsindals“Dinge”,
die eine gewisse Unabhängigkeit haben. Biologische Zellen “leben vor
sich hin”, Computer “werkeln vor sich hin”. Sie alle sind eigenständig
“lebensfähige” Einheiten. Das bedeutet, sie haben die Kontrolle über sich;
die Kontrolle bleibt bei ihnen. Und so sollte es auch bei Alan Kays
Objekten sein.
Dem üblichen, real existierenden Objekt instanziiert aus einer Klasse in
deiner Programmiersprache geht allerdings diese Unabhängigkeit ab, weil
es nur etwas tun kann, wenn der Kontrollfluss explizit dorthin läuft. Die
Kontrolle ist immer nur bei einem Objekt zur Zeit.
Anders ist es bei Aktoren⁷⁰ oder Betriebssystemprozessen. Die operieren
grundsätzlich unabhängig voneinander auf ihren Ressourcen, weil sie
parallel ausgeführt werden.⁷¹
Doch auch wenn heute üblichen Objekte technisch nicht die volle Un-
abhängigkeit haben, hatte Alan Kay es so gedacht. Das sollten wir im
Hinterkopf behalten.
Geschlossenheit
Ebenfalls noch recht offensichtlich im Bild ist, dass jede biologische Zelle
für sich einen “Gebietsanspruch stellt”. Sie ist ein räumliches Gebilde,
das mit einer Membran einen Innenraum von der Umwelt trennt. Die
Membran regelt Zu- und Abfluss von Ressourcen und schützt den Kern.
Was in der Zelle passiert, wie sie strukturiert ist, ist von außen nicht sicht-
barbar. Ist geschlossen vor neugierigen Blicken und zeigt nur insgesamt
ein Verhalten in Form von Reaktionen auf Reize.
So dachte es Alan Kay auch für Objekte. Er hat sie als Kapseln verstanden,
die ihr Innenleben verschlossen halten. Lediglich im Nachrichtenaus-
tausch zeigen sie Verhalten.
Wenn Alan Kay sagt
⁷⁰https://en.wikipedia.org/wiki/Actor_model
⁷¹ObtatsächlichparallelaufmehrerenKernenbzw.Prozessorenodernurpseudoparallel
durchMultithreading,spielthierkeineRolle.


---


<!-- Page 112 of 584 -->


03-RadikaleObjektorientierung 103
“I wanted to get rid of data.”
dann meinte er genau diese Geschlossenheit. Sie sollte entkoppeln. Die
Details von Datenstrukturen sollten nicht weithin in Logik bekannt sein,
sondern lediglich innerhalb eines sehr überschaubaren Rahmens, d.h. in
einem Objekt, das für sie verantwortlich ist.
In dieser Hinsicht hat die mainstream Objektorientierung nach meinem
Empfinden ihren ersten Fehler bei der Interpretration von Alan Kays
radikaler Idee begangen. Das ist über die Jahrzehnte nicht unentdeckt ge-
blieben, es hat Kritik gegeben, geändert wurde die vorherrschende Praxis
jedoch nicht, würde ich sagen. Das Problem real existierender Objekte
ist die geringe Kapselung: In Java sind es getter- und setter-Methoden,
in C# sind es property-Methoden die es so leicht machen, Objektzustand
zu publizieren. Oder Felder/Attribute von Objekten werden einfach auf
public gesetzt.
Genau damit wollte Alan Kay aber aufräumen. Das gab es schon in
den 1960ern: Datenstrukturen, auf deren “Innereien” beliebig zugegriffen
werden konnte. Mit den Mitteln der Objektorientierung in C++, Java usw.
konnten diese Datenstrukturen dann lediglich auch noch mit Funktionali-
tätaufgeladenwerden.Datenstrukturensollten“Nachrichtenverarbeiten”
können - mussten dafür aber ihre sonstige Form nicht aufgeben. Damit
waren Harpyien geschaffen, die durch eine co-location von Daten und
Logik zunächst attraktiv aussahen - sich am Ende jedoch als gefährliche
Mischwesen entpuppten, die die Kopplung eher steigerten, denn verrin-
gerten.
Die Möglichkeit zur Benutzung von Interfaces ändert an dem grundlegen-
den Missverständnis nichts. Im Mainstream werden Objekte nicht als so
fundamental geschlossen gedacht, wie sie ursprünglich gemeint waren.
Unidirektionalität
DasfürihnWichtigste,dasMessaging hatAlanKayleideramwenigstens
erklärt. Vielleicht war es für ihn so selbstverständlich, so naheliegend?
Ich weiß nicht. Jedenfalls liegt hier für mich das größte Miss- oder
Unverständnis der mainstream Objektorientierung. Sie hat nicht wirklich
annehmen können, was die Analogie vermittelt.


---


<!-- Page 113 of 584 -->


03-RadikaleObjektorientierung 104
Die Objekte dominieren im Bild. Das Messaging wird nur durch einen
kurzenPfeildargestellt.Wassolldaranschonwichtigoderbesonderssein?
Kein Wunder, dass das Messaging abgetan wird.
In der UML wird der Pfeil für vor allem für Abhängigkeiten verwendet.
Seitdem ist er aus meiner Sicht vergiftet. Er bedeutet “Ich brauche dich!”
(oder zumindest “Ich kenne dich!”). Doch nichts weiter könnte von der
biologischen Realität entfernt sein, die Alan Kays Idee Pate gestanden hat.
Indem dem Pfeil diese Bedeutung gegeben wurde, hat er aufkeimendes
Verständnis schnell getötet.
Schau nochmal das Schemabild oben an: Ist es korrekt, dass die Ner-
venzelle die Muskelzelle braucht? Oder ist es vielleicht korrekt, dass
die Muskelzelle die Nervenzelle braucht? Oder noch einfacher: Haben
Nervenzelle bzw. Muskelzelle auch nur Kenntnis von einander?
Die Antwort auf all diese Fragen ist für mich ein entschiedenes Nein!
Die biologischen Zellen kennen einander nicht, brauchen einander nicht
(direkt), sie interessieren sich nicht füreinander. Sie leben sozusagen
selbstvergessen vor sich hin innerhalb eines “Nachrichtenstroms” aus Mo-
lekülen/Reizen, die auf sie einströmen und die sie andererseits aussenden.
Das ist für mich der Kern vom Kern der Objektorientierung.
Der Pfeil im Bild ist tatsächlich “nur” als Pfeil gemeint. Er beschreibt die
Fließrichtung für Nachrichten zwischen den Zellen: Acetylcholin fließt
von der Nervenzelle zur Muskelzelle. Die Nervenzelle setzt ACh unter
bestimmten Umständen frei, die mit den auf sie einströmenden Reizen
und ihrem Zustand zu tun haben. Und wenn das ACh auf die Muskelzelle
als Reiz trifft, reagiert die entsprechend und in Abhängigkeit von ihrem
Zustand.
DasMessaging,dasAlanKaymeint,istalsoeineganzklarunidirektionale
Verbindung zwischen Objekten!
EsgibtzwischenbiologischenZellenkeineRequest/Response-Beziehungen.
EsgibtzwischenbiologischenZellenkeineCommand-and-Control-Abhängigkeiten.
Das ist die radikale Botschaft der Objektorientierung von Alan Kay.
In allen weiteren Bildern von mir in diesem Buch wirst du deshalb Pfeile
nurmitdieserBedeutungsehen:Nachrichten(allgemeiner:Daten)fließen
unidirektional von einer Funktionseinheit zu einer anderen.


---


<!-- Page 114 of 584 -->


03-RadikaleObjektorientierung 105
UmAbhängigkeitenauszudrücken,d.h.Strukturbeziehungen,benutzeich
ein anderes Verbindungssymbol: den Strich mit einem Punkt am Ende.
Ein Prinzip als Destillat
Es ist wahr:
“The big idea is ‘messaging’ […]”
Messaging bedeutet unidirektional fließende Nachrichten. Messaging in
Anlehnung an biologische Zellen bedeutet sogar, dass Objekte einander
nicht kennen.
NervenzellenundMuskelzellenarbeiten unzweideutigzusammen,wie du
beim Lesen bemerkst, da sich deine Augen mühelos über den Text bewe-
gen. Nur wissen sie deshalb nichts voneinander. Das ist der Wahnsinn der
radikalen Objektorientierung! Kein Wunder, dass the big idea nicht mit
Hurra! aufgegriffen wurde.
Wenn wir Alan Kays Idee aber ernst nehmen, dann ist genau das das
fundamentale Organisationsprinzip von objektorientierter Software. Ich
habe es das
Principle of Mutual Oblivion (PoMO)


---


<!-- Page 115 of 584 -->


03-RadikaleObjektorientierung 106
genannt.⁷²
Objekte als die Akteure, die Funktionseinheiten innerhalb von Software
haben alle ihre Aufgabe. Wie sie die erfüllen, verbergen sie vor anderen
Objekten; sie kapseln ihre Logik und ihre Daten (Zustand).
Zusammenarbeit zwischen Objekten entsteht, indem Objekte Daten “ab-
sondern und absorbieren”. Das mag dir etwas drastisch klingen, aber ich
formuliere es bewusst so, um die Entkopplung zwischen Objekten zu
betonen.
ObjekteabsorbierenDatenausihrerUmgebung,wennsiedazubereitsind.
Dann sind diese Daten Nachrichten, also Daten, die ein Objekt zu einem
Verhaltenmotivieren.Insofern passtNachricht zurDefinition des Begriffs
Information von Gregory Bateson⁷³:
“[Information is] a difference which makes a difference”
Objekte sind Informationsverarbeiter.
Dass Alan Kay sagt, “I wanted to get rid of data”, kann damit nicht
pauschal stimmen. Er meinte eine bestimmte Art von Daten: globalen
Zustand,d.h.weithinsichtbareDaten,diezuunübersehbarenKopplungen
führen.
Indem er jedoch Messaging in den Kern der Objektorientierung stellt,
wettet er sogar auf Daten, nur eben eine andere Art. Nachrichten sind
flüchtig und nur von lokaler Bedeutung. Sie sind weniger koppelnd als
Zustand. Nichtsdestotrotz muss über sie aber natürlich Einigung erzielt
werden: Wenn ein Objekt bestimmte Nachrichten versteht, dann bilden
die sein Vokabular, das anderen Objekten bekannt sein muss. Objekte,
die Nachrichten formulieren können nicht irgendetwas “absondern”; sie
müssen sich dem Vokabular von Objekten anpassen, die Nachrichten
“absorbieren”. Nachrichten stellen also eine gemeinsame Sprache dar
⁷²Ein Engländer sagte mal zu mir, dass oblivion wohl besser obliviousness hieße. Den
Hinweishabeichgernangenommen-nurwardadieursprünglicheFormulierungschonso
langeinGebrauch,dassichmichschwergetanhabe,siezukorrigieren.UnddieAbkürzung
PoMO wäre ohnehin nicht von einer Anpassung betroffen. Aber wenn du willst, merke dir
Principle of Mutual Obliviousness. Egal, welche Worte wir benutzen, wir wollen vor allem
dasselbemeinen.
⁷³https://en.wikipedia.org/wiki/Gregory_Bateson


---


<!-- Page 116 of 584 -->


03-RadikaleObjektorientierung 107
zwischen kooperierenden Objekten, selbst wenn die sich konkret nicht
kennen.
“Absondern” und “absorbieren” habe ich geschrieben, auch wenn du
vielleicht “senden” und “empfangen” erwartet hast. Um die Radikalität
des PoMO zu betonen, finde ich “absondern” bessern, weil in dem Begriff
keine andere Partei impliziert ist. Würde ich “senden” schreiben, würdest
du sofort an einen Empfänger denken. Und wenn du an einen Empfänger
denkst, dann fragst du dich, wer es konkret ist und wie ein Objekt genau
an ein anderes Nachrichten schickt. Dass dieser Reflex eintritt, möchte
ich aber vermeiden. Du würdest dir damit die Eleganz von Alan Kays
Analogie kaputtmachen.
IndenüblichenOO-SprachenkommunizierenObjektenichtmittelsSend()
undReceive()miteinander;daswenigerverfänglicheEmit()/Absorb()-
Paar fehlt aber auch. Die üblichen Objekte rufen vielmehr direkt Me-
thoden aufeinander auf; sie kennen einander also. Und diese Methoden
sind auch noch Funktionen, die ein Resultat an das aufrufende Objekt
zurückliefern. Das ist die allgegenwärtige Manifestation des Miss- bzw.
Unverständnisses von Alan Kays Idee.
In deinem OO-Code gibt es kein Messaging. Deine Objekte kennen einan-
der. Ihre Datenverbindungen sind nicht unidirektional. Sie setzen mithin
diestrukturierteProgrammierungnurmitetwasaufgemotzenMittelnfort.
Dein mainstream OO-Code verstößt gegen das erste Prinzip der radikalen
Objektorientierung, das PoMO.
Implementationsidee
“Ja, wie soll denn das aber funktionieren mit dem Messaging?” magst du
dich nun fragen. “Wie kann man Objekte nach PoMO entkoppeln?” Diese
Frage muss ich natürlich beantworten, sonst ist das ganze nur weltfremde
Theorie.
Als erstes müssen wir genauer hinschauen, was es denn bedeutet, dass
ein Objekt abhängig ist von einem anderen. Wie würde Unkenntnis, gar
Ignoranz gegenüber anderen Objekten aussehen?
Bei Objekten wie bei biologischen Zellen geht es erstmal darum, was
ihre Aufgabe ist. Das eine Objekt mag für eine Berechnung zuständig
sein, das andere für die Persistenz. Beide Objekte erfüllen ihre Aufgaben


---


<!-- Page 117 of 584 -->


03-RadikaleObjektorientierung 108
ausschließlich mittels Logik. Erinnerst du dich noch an deren Definition
aus dem Kapitel 1?
Logik ist das, was ein Objekt ausmacht. Die läuft innerhalb des Raumes
ab, den die Membran des Interface eines Objektes aufspannt. So wie
die chemischen Prozesse innerhalb einer biologischen Zelle hinter der
Zellmembran ablaufen. Ob und wie Logik Zustand hält oder nicht, ist von
außen nicht zu sehen. Oder genauer: Es ist nicht direkt zu sehen; denn
indirekt lässt sich am Verhalten eines Objektes ablesen, ob es auf Zustand
zurückgreift.
Lass es mich konkret machen mit dem Hello-World Szenario. Laut Lö-
sungsansatz aus Kapitel 2 gibt es darin eine Verantwortlichkeit zum
Führen einer (persistenten) Gästeliste. Das klingt doch nach einer guten
Aufgabe für ein Objekt, oder? Alle Details dessen, wie eine Gästeliste
geführt wird, kapselt das Objekt; kein anderes Objekt soll davon erfahren
oder gar sich davon abhängig machen.
Damit ist ein Objekt definiert. Aber welche Daten ist es bereit, zu “absor-
bieren”,welcheNachrichtensollesverstehen?Mirscheintsinnvoll,dass…
• auf einer Gästeliste Namen registriert werden können
• und dass die Gästeliste nach den registrierten Namen befragt wer-
den kann. Da es eine “intelligente” Gästeliste in einem Hello-World-
Programm ist, liefert sie als Antwort nicht nur die Namen, sondern
auch gleich die Häufigkeiten, mit denen sie registriert wurden.⁷⁴
Die Logik für diese Verantwortlichkeit im Rahmen des zweiten Lösungs-
ansatzes kann mit C# so aussehen:
⁷⁴Ob eine persistente Gästeliste so intelligent sein sollte, lässt sich diskutieren. Ist die
Zählung von Besuchshäufigkeiten nicht vielleicht doch eine Sache der Domänenlogik?
Dann würde die Gästeliste lediglich eine rohe Liste der Namen “absondern” müssen.
Andere Objekte würden freier darin sein, was sie damit machen. Die Gästeliste wäre
“wiederverwendbarer”!Eigentlichwürdeichauchdahintendieren,dieGästeliste“dümmer”
zu machen und nicht Häufigkeiten liefern zu lassen. Doch dann wäre sie für die hiesigen
Erklärungen vielleicht ein bisschen sehr armselig. Durch die Häufigkeiten braucht sie
etwas mehr Logik. Sie wird plastischer. Das ist mir gerade wichtiger als eine perfekte
Verantwortlichkeitsallokation.


---


<!-- Page 118 of 584 -->


03-RadikaleObjektorientierung 109
1 // Namen registrieren
2 File.AppendAllLines("gästeliste.txt", new[]{name});
1 // Registrierte Namen mit Häufigkeiten liefern
2 var namen = File.ReadAllLines("gästeliste.txt");
3 var namensgruppen = namen.OrderBy(x => x)
4 .GroupBy(x => x);
5 var häufigkeiten = namensgruppen.Select(x => (x.Key, x.Count()))
6 .ToArray();
Die Gästeliste wird persistent in einer Datei mit Namen gästelis-
te.txt geführt, in der Zeile für Zeile der Name eines Besuchers in der
Reihenfolge des Eintreffens steht.
Wie kann ein radikales Objekt diese Logik nun kapseln? Wie kann es
Nachrichten ganz PoMO-konform “absorbieren” und “absondern”, also
von außen gesehen reagieren, d.h. Verhalten zeigen? Hier mein erster
Vorschlag:
1 class Gästeliste
2 {
3 public class EingehendeNachricht {}
4 public class Registrieren : EingehendeNachricht
5 { public string Name; };
6 public class Laden : EingehendeNachricht { };
7
8 public class AusgehendeNachricht {}
9 public class Besuche : AusgehendeNachricht
10 { public (string Name,int Häufigkeit)[] Häufigkeiten; }
11
12
13 public event Action<AusgehendeNachricht> Absondern;
14
15
16 public void Absorbieren(EingehendeNachricht nachricht) {
17 switch (nachricht) {
18 case Registrieren r:
19 File.AppendAllLines("gästeliste.txt", new[]{r.Name});
20 break;
21
22 case Laden l:
23 var namen = File.ReadAllLines("gästeliste.txt");
24 var namensgruppen = namen.OrderBy(x => x)
25 .GroupBy(x => x);
26 var häufigkeiten = namensgruppen.Select(x => (x.Key, x.Count()))
27 .ToArray();
28
29 var b = new Besuche {
30 Häufigkeiten = häufigkeiten
31 };
32 Absondern(b);
33 break;
34 }
35 }
36 }
Findest du darin die Logik? Gut! Aber das ist der uninteressante Teil am
Objekt. Interessant ist, wie es Nachrichten empfängt: durch eine Methode.


---


<!-- Page 119 of 584 -->


03-RadikaleObjektorientierung 110
Das Objekt reagiert auf eine Nachricht durch Aufruf der MethodeAbsor-
bieren().
Das ist grundsätzlich konform mit der mainstream Objektorientierung.
Allerdings weiche ich insofern vom Üblichen ab, als dass es eben nur eine
Methode gibt. Eine Methode empfängt alle Nachrichten, die das Objekt
versteht. Welche das sind, definiert die Klassenhierarchie unterhalb Ein-
gehenteNachricht{}.DasObjektistalsostrengtypisiert.Latebinding,
wie es sich Alan Kay gewünscht hat, kennt es nicht.⁷⁵
Durch diese Gestaltung der Oberfläche des Objektes wird glasklar, dass
Nachrichten Datenstrukturen sind die zwei Facetten haben:
• Nachrichten haben eine Bedeutung. Erstens sollen sie von anderen
Objekten als relevant erkannt werden können, zweitens sollen
sie dann etwas Spezifisches bewirken. Das geschieht im Beispiel
über den Datentyp. Dass Objekte relevante Nachrichten darstellen,
erkennt das Objekt verlässlich an ihrem Basistyp Eingehende-
Nachricht{}.AlleanderenObjektewürdenabgewiesen,genauer:
nicht einmal vom Compiler zugelassen. Was genau dann zu tun
ist, leitet das Objekt vom konkreten Nachrichtentyp ab. Es reagiert
anders auf Registrieren{} als auf Laden{}.
• Nachrichten tragen Daten. Sobald das Objekt die konkrete Nach-
richterkannthat,hatesaucheineErwartungdaran,wasdarannoch
für eine payload hängt. Manchmal ist die leer wie bei Laden{},
meistens hängen aber wohl Daten daran, die zu verarbeiten sind.
Das Objekt kann damit seinen Zustand verändern oder sie einfach
nur transformieren.
Noch bemerkenswerter jedoch ist der Umgang mit “abgesonderten” Nach-
richten! Darin zeigt sich das PoMO besonders deutlich: das Objekt darf
ja nicht wissen, wer mit einer “abgesonderten” Nachricht etwas anfängt.
Es kennt weder die Objekte, die Nachrichten “absondern”, die es mit
⁷⁵Über die Wichtigkeit von late binding als Kriterium für die Objektorientierung lässt
sich trefflich streiten, würde ich sagen. Es gibt gute Gründe dafür - aber auch gute
Gründedagegen.MancheHochsprachensetzendarauf,anderewidersetzensich.Ichtendiere
immer noch zu typsicherem late binding mittels Vererbungshierarchie oder Interface-
Implementation. Erst zur Laufzeit ist klar, von welchem Typ die absorbierte Nachricht ist
- allerdings kann dieser nur aus einer fixen Menge stammen. Auf diese Weise wird eine
KlassevonLaufzeitfehlernausgeschlossen.DasempfindeichalshilfreicheBeschränkungin
denmeistenFällen.


---


<!-- Page 120 of 584 -->


03-RadikaleObjektorientierung 111
Absorbieren() aufnimmt. Das liegt in der Natur von Funktionsaufru-
fen; es ist unbekannt, wer der Aufrufer einer Funktion ist. Noch kennt
es aber Objekte, die an seinen “abgesonderten” Nachrichten interessiert
sind. Denn das ist nicht einmal verlässlich ein Objekt, das eine “absorbier-
te” Nachricht “abgesondert” hat. Es gibt keine direkte request-response-
Beziehung zwischen “Absonderer” und “Absorbierer” (landläufig: Sender
und Empfänger oder Produzent und Konsument).
Ein Objekt das eine Laden{}-Nachricht “absondert”, tut eben nur das in
demMoment.Wenndarüberhinausnochgespanntdaraufist,waseswohl
für Besucherhäufigkeiten geben mag, dann muss es sich bereit machen,
Besuche{} zu “absorbieren”. Ob und wann eine solche Nachricht aber
eintrifft, ist völlig unsicher!
Ohje, jetzt ist es raus. Die radikale Objektorientierung kennt nur asyn-
chrone Kommunikation. Es gibt im Konzept keine (von Alan Kay benann-
te) synchrone Kommunikation in dem Sinn, dass ein Objekt, das eine
Nachricht “absondert” auf das Eintreffen einer anderen, daraus folgenden
Nachricht wartet. Das kann es zwar tun, wenn es will, nur ist das
nicht “der Urzustand” von Objekten. Wenn man Objekte biologischen
Zellen ähnlich denkt, dann ist synchrone Kommunikatoin ein no-go. Eine
Nervenzelle stößt kein ACh aus, um daraufhin zu warten, dass eine Mus-
kelzelle reagiert (die sie ohnehin nicht kennt) oder von irgendwoher ein
anderen Signal eintritt. Biologische Zellen reagieren einfach auf das, was
sie reizt. Objekte reagieren einfach auf Nachrichten die eintreffen, wenn
sie sie verstehen. Dabei ist es grundsätzlich uninteressant, warum die
Nachrichten eintreffen; sie liegen einfach zur Verarbeitung an. Allerdings
ist ein Objekt dann frei festzustellen, dass es gerade nicht bereit ist, eine
bestimmte Nachricht angemessen zu verarbeiten. Doch das ist schon ein
Detail, mit dem ich dich hier gar nicht belasten will.
Entscheidend ist hier in Bezug auf die Implementation des PoMO, dass
die “Absonderung” einer Nachricht getrennt ist von der “Absorption”. Die
einzigeMethodedesObjekts,dieseineOberflächedefiniert,diesozusagen
sein Universalrezeptor für alle Nachrichten ist, die es versteht, liefert
nie ein Resultat. Wer auch immer sie aufrufen mag, bekommt keine
Rückmeldung darüber, was das Objekt mit einer “absorbierten” Nachricht
tut. Und das ist gut so. Das ist ganz PoMO. Logik, die eine Nachricht
produziert und “absondert”, kann, soll, darf nicht warten, was damit
passiert.


---


<!-- Page 121 of 584 -->


03-RadikaleObjektorientierung 112
Wenn eine “absorbierte” Nachricht zu einer Reaktion über eine Zustands-
änderung hinaus führt, dann wird eine Nachricht als Reaktion über
einen Event “abgesondert”, hier: Absondern(). Technisch ist das ein
Funktionszeiger mit einer konkreten Signatur.
Diesem Funktionszeiger kann jeder, der an “abgesonderten” Nachrichten
des Objektes interessiert ist, eine Funktions zur “Absorption” zuweisen,
d.h. einen Event-Handler.
Hier eine Beispielnutzung des Objektes. Zunächst sind da nur Regis-
trieren{}-Nachrichten zu absorbieren:
1 var db = new Gästeliste();
2
3 db.Absorbieren(new Gästeliste.Registrieren{Name="Bob"});
4 db.Absorbieren(new Gästeliste.Registrieren{Name="Janine"});
5 db.Absorbieren(new Gästeliste.Registrieren{Name="Bob"});
Doch dann folgt eine Laden{}-Nachricht:
1 db.Absondern += besuche =>
2 Console.WriteLine(string.Join(",",
3 (besuche as Gästeliste.Besuche)
4 .Häufigkeiten.Select(x => $"{x.Name}({x.Häufigkeit})")));
5
6 db.Absorbieren(new Gästeliste.Laden());
Weilder,derdieLaden{}-Nachricht“absondert”-hierkonkreter:sendet-
aber auch an der zu erwartenden Reaktion mit der Nachricht Besuche{}
interessiert ist, wird vorher ein Event-Handler registiert. In diesem Fall
listet der nur die Namenshäufigkeiten auf der Konsole.
Kennt das Objekt db die Quelle der “absorbierten” Nachrichten? Nein!
Kennt es die Senke für seine “abgesonderten” Nachrichten? Nein! Kann
ein Betrachter von außen sehen, wie das Objekt seiner Verantwortlichkeit
nachkommt, ob es Zustand hat? Nein! Verläuft der Nachrichtenfluss
unidirektional? Ja!
So sieht radikale Objektorientierung in einer ersten Näherung mit main-
stream OO-Sprachen aus. Sie lässt sich implementieren. Das ist gut zu
wissen, oder? Denn nur, wenn sich Alan Kays Idee auch umsetzen lässt,
kann sie praktisch ihren Nutzen entfalten.
Allerdings, so wirst du wahrscheinlich denken, ist das noch etwas um-
ständlich.SinddieganzenNachrichtenklassennichteinOverhead?Ja,das


---


<!-- Page 122 of 584 -->


03-RadikaleObjektorientierung 113
sind sie wohl in den meisten Fällen. An einer Stelle halte ich sie zwar für
sehr wichtig, um eine konkrete Grenze zu ziehen, wie du später sehen
wirst, doch im Allgemeinen darfst du gern das Optimierungspotenzial
deiner Programmiersprache ausnutzen und zur Nachrichtenverarbeitung
spezifische Methoden definieren. Damit würde die Klasse für Gästelisten-
Objekte z.B. so aussehen:
1 class Gästeliste_optimiert
2 {
3 public event Action<(string Name,int Häufigkeit)[]> Häufigkeiten;
4
5
6 public void Registrieren(string name) {
7 File.AppendAllLines("gästeliste.txt", new[]{name});
8 }
9
10 public void Laden() {
11 var namen = File.ReadAllLines("gästeliste.txt");
12 var namensgruppen = namen.OrderBy(x => x)
13 .GroupBy(x => x);
14 var häufigkeiten = namensgruppen.Select(x => (x.Key, x.Count()))
15 .ToArray();
16 Häufigkeiten(häufigkeiten);
17 }
18 }
Ich höre dein Aufatmen. Du siehst, auch radikale Objektorientierung
besteht nicht immer auf radikalem Anderssein. Die Kombination aus
Methodenname und Parameterliste stellt einen simplen Weg dar, um
Nachrichten zu beschreiben, die ein Objekt versteht. So findest du es
auch in der OOP-Literatur erwähnt, wenn darin der Begriff Messaging
auftaucht. Aber Achtung: Zum Messaging gehört mehr! Auch mit “richti-
gen” Methoden wie in diesem Beispiel will das PoMO eingehaltenwerden.
Deshalb liefert Laden() auch hier kein Resultat. Die als Reaktion auf
diese Nachricht “abzusondernde” mit den Besuchshäufigkeiten verlässt
ein Gästelisten-Objekt immer noch über einen Event: Häufigkeiten().
Der ist jetzt allerdings auch konkreter Formuliert mit einer Signatur, die
einen eigenen Nachrichtendatentyp überflüssig macht.
Wahrscheinlich runzelst du immer noch die Stirn, ob das denn alles so
seine Richtigkeit hat. Das kann ich verstehen. Der Code sieht noch anders
aus als das, was du gewohnt bist. Doch das muss er auch, wenn du
etwas anderes bewirken willst als in der Vergangenheit. Die Andersheit
ist kein Selbstzweck. Sie soll vielmehr das Unterstützen, was Alan Kay
weiland 1967 im Hinterkopf hatte: Evolvierbarkeit. Code sollte leichter zu
verändernsein.Codesollteauchleichterzuverstehensein.DieTestbarkeit
mag ihm noch nicht so bewusst gewesen sein, doch auch die sollte


---


<!-- Page 123 of 584 -->


03-RadikaleObjektorientierung 114
gesteigert werden. Und tatsächlich wird das mit dieser Implementation
erreicht. Sie entkoppelt und sie erzeugt Kohäsion.
Ohne Methoden, die ein Resultat liefern, gibt es keinen Zugriff mehr auf
Zustand in einem Objekt. Die Daten sind damit verschwunden, wie Alan
Kay es wollte. Das Objekt ist eine echte Kapsel für Zustand und Logik.
Und auch Quelle und Senke für Nachrichten sind entkoppelt. Woher eine
Laden{}-Nachricht kommt, muss nicht dasselbe Objekt sein, dass eine
Besuche{}-Nachricht verarbeitet. Und auch die Zeitpunkte zwischen
“Absonderung” der einen Nachricht und “Absorption” der anderen kön-
nen andere sein. Spürst du die Flexibilität, die dadurch entsteht?
Dennochversteheich,wenndunochnichtganzzufriedenbist.ZumGlück
enthält die radikale Objektorientierung ein weiteres Geheimnis, das es zu
lüften gilt.
Integration Operation Segregation
Principle (IOSP)
Alan Kay hat nicht deutlich darauf hingewiesen, dass Messaging aus-
schließlich unidirektionale Kommunikation bedeuten kann - zumindest,
wenn er die Zellenanalogie ernst meint. Wahrscheinlich war das für ihn
zu selbstverständlich.
Er hat allerdings ebenfalls versäumt, auf einen zweiten Umstand hin-
zuweisen, der ebenfalls ganz selbstverständlich und offensichtlich ist -
und dennoch deshalb übersehen worden ist. In der Zellenanalogie steckt
wahrlich ein Geheimnis, über das sich Menschen sogar Tausende von
Jahren die Köpfe eingeschlagen haben. Auch wenn wir es nicht für die
Menschheit im Allgemeinen lüften können, so können wir es aber zum
Glück für die Softwareentwicklung im Speziellen.
Um die das Geheimnis spürbar zu machen, hier zunächst der Rest einer
Implementation des Hello-World Programms unter Berücksichtigung von
PoMO.
Das Objekt für die Gästeliste zunächst in einer noch etwas weiter opti-
mierten Version:


---


<!-- Page 124 of 584 -->


03-RadikaleObjektorientierung 115
1 class Gästeliste_optimiert_v2
2 {
3 public void Registrieren(string name) {
4 File.AppendAllLines("gästeliste.txt", new[]{name});
5 }
6
7 public void Laden(Action<(string Name,int Häufigkeit)[]> Häufigkeiten) {
8 var namen = File.ReadAllLines("gästeliste.txt");
9 var namensgruppen = namen.OrderBy(x => x)
10 .GroupBy(x => x);
11 var häufigkeiten = namensgruppen.Select(x => (x.Key, x.Count()))
12 .ToArray();
13 Häufigkeiten(häufigkeiten);
14 }
15 }
Der Event ist verschwunden! Stattdessen hat Laden() einen Parameter:
einen Funktionszeiger für die “abzusondernde” Nachricht, die über die
Besuchshäufigkeiten informiert.
Der Mechanismus für die “Absonderung” ist im Grunde derselbe: ein
Funktionszeiger statt eines Funktionsresultats. Quelle der “absorbierten”
Nachricht und Senke der “abzusondernden” sind weiterhin entkoppelt.
Das ist gut. Allerdings ist nun klar, dass der Empfang der Nachricht
zum Laden zur Erzeugung einer Nachricht mit Häufigkeiten führt. Dieser
Zusammenhang war vorher nicht zwingend.
TechnischwirdderUmgangmitdemObjektabernuneinwenigeinfacher.
Dafür mag der Preis gering sein, dass ein- und ausgehende Nachricht über
die Signatur miteinander in Bezug gesetzt sind.
AlsnächstesdieBenutzerschnittstelle,dienachdenNamenfragtundauch
am Ende die Begrüßung ausgibt:
1 class Benutzerschnittstelle
2 {
3 public event Action<string> Name;
4
5 public void NamenErfragen() {
6 while (true) {
7 Console.Write("Name: ");
8 var name = Console.ReadLine();
9 Name(name);
10 }
11 }
12
13 public void Begrüßen(string begrüßung) { ... }
14 }
Hier habe ich mich entschieden, bei einem Event für die “abzusondernde”
Nachricht zu bleiben. Das hat keinen sehr tiefen Sinn, sondern soll hier
vor allem etwas Variantenreichtum bei der Implementation nach PoMO
demonstrieren.


---


<!-- Page 125 of 584 -->


03-RadikaleObjektorientierung 116
Du erkennst das Muster: Nachrichten, die ein Objekt “absorbieren” soll,
weil es sie versteht und verarbeiten soll, werden in void-Methoden
übersetzt. Und Nachrichten, die ein Objekt “absondern” soll, werden in
Funktionszeiger übersetzt; entweder sind das Events oder Parameter einer
“Absorbtionsmethode”.
Dito beim letzten Objekt, das ich der Lösung spendiere:
1 class Domäne
2 {
3 public void BegrüßungErmitteln(string name,
4 (string Name, int Häufigkeit)[] besuche,
5 Action<string> begrüßung) {
6 ...
7 begrüßung(text);
8 }
9 }
Auch fließen Nachrichten wieder über einen Funktionszeiger als Para-
meter aus. Das hat den Nachteil einer Verbindung zwischen ein- und
ausfließenden Nachrichten, doch es hat eben auch einen Vorteil bei der
Nutzung des Objektes. Auf diese Weise kann es in ganz unterschiedlichen
Zusammenhängen genutzt werden, in denen ganz verschiedene Konsu-
mentendie“abgesonderten”Nachrichten“absorbieren”.Dasistmiteinem
Event eher nicht praktikabel.
Aber lass dich von so einem Implementationsdetail erstmal nicht ver-
schrecken.DieBenutzungvonFunktionszeigernwirddichwahrscheinlich
schon genug irritieren, da muss ich nicht auch noch über deren Varianten
schwadronieren.
Dass den weiteren Objekten Logik fehlt, übersieh einfach. Die Logik ist
nicht wichtig für das Geheimnis der radikalen Objektorientierung, um
das es hier geht. Dafür sind lediglich die Objekte mit ihren Oberflächen
wichtig!
• Welche Objekte gibt es?
• Welche Nachrichten verstehen/erzeugen sie?
Die Zahl der Objekte entspricht der der Klassen. Und die Zahl der
Nachrichten entspricht der der Pfeile zwischen den Objekten. Dort, wo
einePfeilspitzeaufeinObjekttrifft,findetsichinderImplementationeine
“absorbierende” Methode. Dort, wo ein Pfeil aus einem Objekt austritt,
findet sich in der Implementation ein “absondernder” Funktionszeiger.


---


<!-- Page 126 of 584 -->


03-RadikaleObjektorientierung 117
Lass dich nicht verwirren durch den Pfeil für den Namen, der von der
Benutzerschnittstelle zur Domäne geht. Der steht nicht für eine weite-
re Nachricht, sondern für eine mehrfache Verwendung des Namens in
der payload von Nachrichten. Er gehört einmal zur Registrieren()-
Nachricht und einmal zur BegrüßungErmitteln()-Nachricht.
Ja, so ist das mit den Objekten, wenn die Daten echt fließen. Positiv ist die
Kapselung von Details in den Objekten. Doch die Verbindungen zwischen
den Objekten sind nun erstmal recht frei. Solange eine “abgesonderte”
Nachricht (oder auch nur Daten einer Nachricht) irgendwo anders passen,
können sie dort auch “absorbiert” werden. Einer Muskelzelle ist es ja
ebenfalls egal, woher das ACh kommt, das sie gerade reizt. Sie nimmt,
was sich ihr präsentiert: von einer Nervenzelle wie von einer Pipette, falls
sie in einer Petrischale liegen sollte.
Und damit rücken wir an das Geheimnis heran. Hiding in plain sight
könnte man sagen: das Geheimnis, die von Alan Kay nicht beantwortete
Frage steht im vorherigen Bild wieder vor dir.
Objekte verbinden als Verantwortlichkeit
Das Geheimnis biologischen Zellen ist: Wer bringt eigentlich Nervenzelle
und Muskelzelle zusammen, dass sie gemeinsam (mit Millionen anderer


---


<!-- Page 127 of 584 -->


03-RadikaleObjektorientierung 118
Zellen)einlebendesGanzesbilden?IstdaseinGottundwennja,welcher?
Oder ist das schlicht Evolution?
Auf das Schemabild bezogen: Wer zieht eigentlich die Pfeile zwischen
Objekten? Und wie werden die Verbindungen zwischen den Objekten im
Code hergestellt?
Letztere Frage kann ich ganz leicht beantworten:
1 var ui = new Benutzerschnittstelle();
2 var dom = new Domäne();
3 var db = new Gästeliste_optimiert_v2();
4
5 ui.Name += name => {
6 db.Registrieren(name);
7 db.Laden(
8 besuche => {
9 dom.BegrüßungErmitteln(name, besuche,
10 ui.Begrüßen);
11 });
12 };
13
14 ui.NamenErfragen();
Keine Sorge, das funktioniert. Störe dich bitte im Moment nicht daran,
dass das irgendwie merkwürdig aussieht. Das liegt am reichlichen Ge-
brauch von Funktionszeigern. Der ist aber nicht wichtig, auch wenn es dir
im Moment so erscheinen mag. Die Funktionszeiger sind nur ein Mittel,
mit dem ich ganz leicht und ohne weitere Erklärungen das PoMO erfüllen
konnte.
Funktionszeiger als Mittel der sauberen Programmierung sind aus meiner
Sicht zwar unverzichtbar. Doch wann und wo genau, erkläre ich dir
später. Im obigen Fall wären sie nicht wirklich nötig. Sie sind nur ein
vorübergehendes Überbleibsel aus dem vorherigen Abschnitt.
Worauf ich deinen Blick lenken will, ist etwas anderes. Und das ist
wahrlich genauso wichtig für Alan Kays Idee wie das Messaging, würde
ich sagen.
ImSinneeinesEntwurfsmussirgendwerdaraufkommen,welcheObjekte
es geben sollte und welche Nachrichten zwischen ihnen fließen. Irgend-
wer stellt also mit Pfeilen Verbindungen zwischen Objekten her. Ok, nicht
irgendwer, sondern du als Entwickler einer Lösung. Du bist sozusagen
ein intelligent designer, der Objekte erschafft und in Beziehung setzt. Sie
erschaffen sich nicht selbst und sie kennen einander auch nicht, so dass
sie sich nicht zu “Teams” zusammenfinden können.


---


<!-- Page 128 of 584 -->


03-RadikaleObjektorientierung 119
WährendduNachrichtenundObjekteentwirfst,triffstduEntscheidungen
darüber, wie sie am besten in Verbindung stehen. Wenn die Objekte
laut PoMO nicht wissen, mit wem sie zusammenarbeiten, dann muss
dieses Wissen an anderer Stelle manifestiert sein. In einem Entwurfsbild
geschieht das durch Pfeile für den Nachrichtenfluss. Ein Pfeil verbindet
das “absondernde” mit dem “absorbierenden” Objekt, Quelle mit Senke.
Und wie ist das im Code? Wie wird der Pfeil übersetzt? Ein Objekt
wird in den Beispielen zur Klasse. Der Austrittspunkt eines Pfeils, der
“Absonderungspunkt” einer Nachricht wird zu einem Funktionszeiger.
Der Eintrittspunkt eines Pfeils, der “Absorptionspunkt” einer Nachricht
wird zu einer Methode. Aber die Linie des Pfeils, dass er von einem
bestimmten Quell-Objekt zu einem bestimmten Senke-Objekt “schießt”,
wie wird das übersetzt?
Im vorstehenden Codebeispiel geschieht das durch die Zuweisung einer
“absorbierenden” Methode an einen “absondernden” Funktionszeiger, z.B.
1 dom.BegrüßungErmitteln(name, besuche,
2 ui.Begrüßen);
Die Methode ui.Begrüßen() “absorbiert” den Begrüßungstext, den das
Objekt dom über den Funktionszeiger Action<string> begrüßung
“absondert”.
Objektebeschreibensichvollständigselbst,könntemansagen.Duschaust
auf eine Klasse, die ein Objekt des Entwurfs manifestiert und siehst alles:
die Nachrichten, die sie akzeptiert, die Nachrichten, die sie emitiert, das
Wie ihres Verhaltens (die Logik) und auch ihre Zustandsdatenstruktur,
falls es eine gibt.
Die Beschreibung der Verbindungen zwischen Objekten kann qua PoMO
natürlich nicht Sache der Objekte sein. Dazu braucht es eine weitere
Instanz.Dieistausschließlichdafürverantwortlich,dieNachrichtenflüsse
zwischen Objekten herzustellen. Du hast dich als intelligent designer für
gewisse Verbindungen entschieden; diese Entscheidungen sind im Code
durchzusetzen. Das ist im Sinne des Single Responsibility Principle (SPR)
eine ganz eigene Verantwortlichkeit. Dafür braucht es mithin eine eigene
Funktionseinheit. Das kann nicht Sache der Objekte selbst sein.
Oder anders ausgedrückt: Wenn schon laut PoMO Objekte von einander
nichts wissen dürfen, dann dürfen sie nicht plötzlich zum Aufbau von
Nachrichtenkanälen doch wieder von einander wissen.


---


<!-- Page 129 of 584 -->


03-RadikaleObjektorientierung 120
Es darf keine funktionalen Abhängigkeiten zwischen Objekten geben.
Ein Objekt darf nicht wissentlich einem bestimmten anderen eine Nach-
richt schicken. Es darf die Logik im einen Objekt nicht wissentlich eine
Funktion in einem anderen aufrufen.
Von welchen Objekten welche Nachrichten an welche anderen fließen,
d.h. welche Objekte am Ende welche anderen aufrufen, muss von einer
anderen Instanz bestimmt werden. Das steckt für mich zwingend in Alan
Kays Idee und Analogie. Wenn du Messaging konsequent denkst, dann
geht es nicht anders. Messaging führt zu funktionaler Unabhängigkeit.
Ein Prinzip als Destillat
DasPoMOdefiniertdiegrundsätzlicheNaturvon“Objektnetzwerken”.Es
braucht jedoch ein zweites Prinzip, um zu definieren, wie Objekte mittels
Nachrichtenverbindungen konkret verwoben werden. Das nenne ich das
Integration Operation Segregation Principle (IOSP)
• Operation ist das, was Objekte tun. Oder genauer: das, wie Objekte
etwas tun, also die Logik.
• Integration ist das, wie Objekte verbunden sind. Es integriert, wer
festlegt, welches Objekte welche Nachrichten an welches andere
sendet.
DasIOSPgebietet,dassdiesebeidenVerantwortlichkeitennichtvermischt
werden sollen. Wer Verhalten erzeugt mit Logik, der darf nicht auch noch
Objekte verbinden. Mit Logik darf also keine Kenntnis vermischt werden,
wie konkrete Objekte in Beziehung stehen.
InEntwurfsdiagrammenistdasgarkeinProblem.DieKästchenimobigen
Bild stehen für Operationen, sie kapseln Logik. Die Pfeile im obigen Bild
stehen für Integration, sie verbinden Objekte. Unterschiedliche visuelle
Ausdrucksmittel für unterschiedliche Verantwortlichkeiten. Das ist ein-
fach.
Doch wie kann diese natürliche Unterscheidung im Modell übersetzt
werden in Code?


---


<!-- Page 130 of 584 -->


03-RadikaleObjektorientierung 121
Implementationsidee
Wie das obige Beispiel der Verbindung der Hello-World-Objekte zu einem
lauffähigen Ganzen zeigt, kann die Übersetzung von Integration ganz
einfach sein: sie findet in einer Funktion statt. Im Beispiel ist das Main():
1 static void Main(string[] args) {
2 var ui = new Benutzerschnittstelle();
3 ...
4 ui.NamenErfragen();
5 }
Main()ist ausschließlich für die Integration zuständig. Sie ist eine In-
tegrationsfunktion. Deshalb findest du in ihr keine Logik. Main() tut
nichts selbst im Hinblick auf die Verhaltensherstellung im Programm. Die
Funktion sorgt lediglich dafür, dass alle dazu nötigen Objekte erzeugt
und entwurfsgemäß verbunden sind. Dazu steck sie entweder Nachrich-
tenquellen und -senken zusammen oder ruft nachrichtenverarbeitende
Methoden auf.
Umgekehrt ist die folgende “absorbierende” Funktion eine Operation. Sie
enthält ausschließlich Logik und verbindet keine Objekte.
1 public void Laden(Action<(string Name,int Häufigkeit)[]> Häufigkeiten) {
2 var namen = File.ReadAllLines("gästeliste.txt");
3 var namensgruppen = namen.OrderBy(x => x)
4 .GroupBy(x => x);
5 var häufigkeiten = namensgruppen.Select(x => (x.Key, x.Count()))
6 .ToArray();
7 Häufigkeiten(häufigkeiten);
8 }
Laden() weiß nicht, von welchem anderen Objekt die Aufforderung
kommt, zu reagieren. Und die Funktion Laden() weiß auch nicht, an
welches andere Objekt die Nachricht über die Besuchshäufigkeiten geht,
die sie erzeugt. Der Funktionszeiger Häufigkeiten() macht darüber
keine Aussage. Er ist ein Platzhalter für eine beliebige Senke.
Lediglich Main() als Integration kennt die Zusammenhänge:


---


<!-- Page 131 of 584 -->


03-RadikaleObjektorientierung 122
1 db.Laden(
2 besuche => {
3 dom.BegrüßungErmitteln(name, besuche,
4 ui.Begrüßen);
5 });
In der Integration siehst du, dass die “abgesonderte” Nachricht an die
Domäne fließt. db, d.h. das Objekt zur Gästeliste, das die Laden()-
Nachricht verarbeitet, “is oblivious to that”.
Aus Alan Kays Analogie folgt für mich ganz klar das IOSP. Und aus dem
IOSP folgt, dass Funktionen entweder reine Integrationen sein sollen und
keineLogikenthalten-oderFunktionensollenreineOperationenseinund
ausschließlich Logik enthalten.
Die Übersetzung des radikal objektorientierten Modells oben folgt dem
IOSP.
Allerdings tut es das zu umständlich.
Funktionszeiger zur “Absonderung” von Nachrichten, sind zwar univer-
sell - doch letztlich sind sie für die meisten Fälle zu kompliziert bzw. zu
gewöhnungsbedürftig. Wenn du PoMO und IOSP durchdenkst, kommst
du darauf, dass der radikalen Objektorientierung auch mit Funktionsre-
sultaten gedient werden kann.
Tatsächlich ist nicht das Funktionsresultat das Problem. Darin steckt
kein Widerspruch zu den Prinzipien der radikalen Objektorientierung. Es
kommt vielmehr darauf an, wer was mit einem Funktionsresultat tut!
Wenn eine Funktion in einer Integration aufgerufen wird, die keine Logik
enthält und also mit einem Funktionsresultat nichts tut, dann ist das
keine funktionale Abhängigkeit! Die aufgerufene Funktion weiß immer
noch nicht, wer sie aufruft. Und sie weiß auch nicht, wer mit dem
Funktionsresultat als “abgesonderter” Nachricht etwas tut. Dem PoMO ist
gedient auch mit einem Funktionsresultat. Dem IOSP kann auch gedient
sein mit einem Funktionsresultat.
Es steht Methoden mit Resultat also nichts im Wege, um Nachrichten
zu “absorbieren” und auch “abzusondern”. Ich hoffe, das ist eine gute
Nachricht für dich.
Welchen Unterschied das macht wieder am Beispiel des Hello-World-
Programms. Zuerst die in dieser Hinsicht optimierte Version der Gäste-
liste:


---


<!-- Page 132 of 584 -->


03-RadikaleObjektorientierung 123
1 class Gästeliste_optimiert_v3
2 {
3 public void Registrieren(string name) {
4 File.AppendAllLines("gästeliste.txt", new[]{name});
5 }
6
7 public (string Name,int Häufigkeit)[] Laden() {
8 var namen = File.ReadAllLines("gästeliste.txt");
9 var namensgruppen = namen.OrderBy(x => x)
10 .GroupBy(x => x);
11 return namensgruppen.Select(x => (x.Key, x.Count()))
12 .ToArray();
13 }
14 }
Das sieht aus, wie du es erwartet hättest und gewohnt bist, oder? Metho-
den, wie sie sein sollen.
Genauso endlich in der Domäne:
1 class Domäne
2 {
3 public string BegrüßungErmitteln(string name,
4 (string Name, int Häufigkeit)[] besuche) {
5 ...
6 var text = ...;
7 return text;
8 }
9 }
Und zu deiner endgültigen Beruhigung noch die Integration. Ohne den
“Zwang” zu Funktionszeigern zur Einhaltung von PoMO sieht das doch
sehr verträglich aus, oder? So kann radikale Objektorientierung Spaß
machen.
1 class Program
2 {
3 static void Main(string[] args) {
4 var ui = new Benutzerschnittstelle();
5 var dom = new Domäne();
6 var db = new Gästeliste_optimiert_v3();
7
8 ui.NamenErfragen(
9 name => {
10 db.Registrieren(name);
11 var häufigkeiten = db.Laden();
12 var begrüßung = dom.BegrüßungErmitteln(name, häufigkeiten);
13 ui.Begrüßen(begrüßung);
14 });
15 }
16 }
Nur an einer Stelle “schiebt” ein Funktionszeiger noch Nachrichten aus
einem Objekt heraus, bei der Benutzerschnittstelle{}. Der Grund
dafür: Es ist unklar, wieviele Nachrichten “abgesondert” werden als
Reaktion auf die “absorbierte” Nachricht NamenErfragen(). Mit einem


---


<!-- Page 133 of 584 -->


03-RadikaleObjektorientierung 124
einmaligen Funktionsresultat wäre dieses 1:n-Verhältnis zwischen Input
und Output nicht implementierbar. Aber dazu später noch ausführlicher.
An dieser Stelle siehst du vor allem Objekte integriert in Form einer
Sequenz von Funktionsaufrufen. Einfacher kann Messaging nicht mehr
werden:
1 db.Registrieren(name);
2 var häufigkeiten = db.Laden();
3 var begrüßung = dom.BegrüßungErmitteln(name, häufigkeiten);
4 ui.Begrüßen(begrüßung);
Warum nicht gleich so? Weil ich die Prinzipien für dich schrittweise
entwickelnwollte.Das,wasdirmainstreamOO-Sprachenbieten,istnicht
schlecht. Nein, es ist sogar sehr gut. Du hast mit ihnen scharfe Messer in
der Hand. Deshalb musst du aufpassen, dass du dich nicht schneidest. Am
besten beachtest du also ein paar Grundregeln für den Umgang mit schar-
fen Messern. Die OO-Sprachmittel “irgendwie” einzusetzen, wie du es aus
der Strukturierten Programmierung gewohnt bist, ist zu wenig. Es fehlen
die Regeln für die Objektorientierung, die radikale Objektorientierung.
Mit PoMO und IOSP liefere ich sehr klare Prinzipien, die im Umgang
mit den OO-Sprachmitteln eingehalten werden sollten, um überhaupt
wirklich OOP zu betreiben, wie es der Erfinder gemeint hatte.
Kurz nachdem Alan Kay den Begriff der Objektorientierung geprägt
hatte, wurde von Edgar Dijkstra 1968 das goto als höchst scharfes Messer
entlarvt und gefordert, es mit Regeln zu entschärfen; für ihn galt: Go To
Statement Considered Harmful⁷⁶. Daraus ist die Strukturierte Program-
mierung entstanden, in der es im Grunde kein goto mehr gibt. Oder wann
hast du zuletzt diese Anweisung benutzt?
Was Alan Kay vorher getan hatte - ohne es zu sagen oder vielleicht gar
zu ahnen - war, die funktionalen Abhängigkeiten als scharfe Messer zu
entlarven. Nur verklausuliert hat er allerdings für Regeln plädiert, sie zu
entschärfen. Aus dem Begriff Messaging wurde das leider nicht heraus-
gelesen - sondern mit der mainstream Objektorientierung im Grunde nur
noch schlimmer gemacht. Ich möchte diesem Übelstand abhelfen und for-
muliere in Anlehnung an Dijkstra: Functional Dependencies Considered
Harmful⁷⁷.
⁷⁶https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf
⁷⁷https://ralfw.de/2019/07/functional-dependencies-considered-harmful/


---


<!-- Page 134 of 584 -->


03-RadikaleObjektorientierung 125
Ganz allgemein: Programmiersprachen sind Werkzeuge. Die können Gu-
tes tun oder auch Schaden anrichten. Nicht alles, was mit ihnen möglich
ist, sollte deshalb einfach getan werden. Wir brauchen sinnige Begrenzun-
gen.
Konkret: Wir müssen etwas tun, um uns nicht ständig mit funktionalen
Abhängigkeiten ins eigene Fleisch zu schneiden. Auf PoMO und insbeson-
dere IOSP zu achten, ist meine dringende Empfehlung dafür. Unsere OO-
Sprachen stehen gerade nicht zur Disposition; wir können ihre Features
nichtzügiganpassen.WirmüssenmitihrenMittelleben,imGutenwieim
Schlechten.DeshalbmüssenwirinunserenKöpfenetwasverändern.Dein
Bewusstsein möchte ich schärfen für den Schaden, der durch funktionale
Abhängigkeiten entsteht. Mit der radikalen Objektorientierung möchte
ich dir ein Mindset an die Hand geben, nein, wohl eher in deinen Kopf
einprägen, das dich schon in der Lösungsfindung, also weit vor der
Codierung, auf Abstand hält zu funktionalen Abhängigkeiten. Was mich
dabei so zuversichtlich macht ist, dass die Idee schon so alt ist.⁷⁸
Alles,wasfolgt,sollalsoimKonzeptfreivonfunktionalenAbhängigkeiten
sein und auch in der Implementierung. Funktionale Abhängigkeiten sind
hinderlich; sie verschlechtern die Testbarkeit und Verständlichkeit. Sie
sind auch gänzlich unnötig. Hier und da kannst du sie als vorsichtige
und lokale Optimierungen einsetzen. Doch sei dir immer bewusst, dass
du dabei ein scharfes Messer schwingst.
⁷⁸Alan Kay hat die richtige Intuition gehabt, nur war sein Bild nicht klar genug.
Biologische Zellen, Messaging… das war zu weit weg von der noch goto-verhafteten
Programmierung Ende der 1960er. Auch die Funktionale Programmierung hat im Grunde
dieselbeIdeegehabt-unddassogareinJahrzehntodergarlängervorAlanKay.Auchsiehat
sichbisherjaabernichtdurchgesetzt.AllerdingsgewinntsieanRaumindenletztenJahren:
Haskell, Scala, Clojure, F# sind keine Sprachen im Elfenbeinturm. Und indem Elemente
der Funktionalen Programmierung in OO-Sprachen Einzug halten, wird die Möglichkeit
beflügelt, ohne funktionale Abhängigkeiten zu entwickeln. Ich finde, das ist eine sehr gute
Entwicklung, der C# vorreitet und Java hinterher trottet. Schade, dass der Umweg um die
50 Jahre gedauert hat. Doch vielleicht ist das kein Wunder. Über viele Erkenntnisse müssen
ein oder zwei Generationen vergehen, bis sie wirklich Fuß fassen können. Mir scheint nun
aber die Zeit reif für Messaging. Es ist hohe Zeit für radikale Objektorientierung und die
Gelegenheitistgünstig.AndersalsfürActor-ProgrammierungoderMicroservicesmusstdu
auchkeineneuenTechnologienlernenundeinführen.PoMO/IOSPkannstduschonmorgen
indeinemCodeleben,wennduwillst.Zuerstliesabermalweiter.FürdenEntwurfwillich
dirnocheinpaarpraktischeRatschlägemitgeben.


---


<!-- Page 135 of 584 -->


03-RadikaleObjektorientierung 126
Philosophischer Exkurs
DiemainstreamObjektorientierungistmiteinemgroßenAnspruchaufge-
treten:dieProduktivitätsolltesteigendurchWiederverwendung,dieWelt
sollte sich leicht im Code abbilden lassen durch Objekte. Nach meinem
Empfinden hat sie diesen Anspruch bei weitem nicht so erfüllt, wie es
sich ihre Proponenten seit den 1990er gewünscht haben. Wie kommt das?
Ich habe eine Erklärung gefunden, die mir einiges plausibel macht: Soft-
ware ist missverstanden worden als Maschine und wurde dann nicht
einmal wie eine Maschine konstruiert.
Wenn der Mainstream die Objektorientierung wirklich, wirklich ernst
genommen hätte, dann hätte etwas daraus werden können mit der Abbil-
dung der Welt in Software in Form von Objekten. Als Beispiel fallen mir
elektronische Schaltungen wie diese “Astabile Kippstufe (Multivibrator)
als Wechselblinker”⁷⁹ ein:
EchteObjekteineinemflüssigenZusammenspielimplementiereneineProblemlösung
⁷⁹https://www.bastelnmitelektronik.de/basteleien-ger%C3%A4te-und-schaltungen/
weitere-schaltungen-ger%C3%A4te-und-basteleien/wechselblinker-astabile-kippstufe/


---


<!-- Page 136 of 584 -->


03-RadikaleObjektorientierung 127
Hier siehst du nicht nur die Objekte, du kannst sie fühlen, anfassen. Jedes
Bauteil leistet seinen Beitrag zum Gesamtverhalten. Das ist eine kleine
“elektronische Maschine”.
Nicht nur ist diese Manifestation ein schönes Beispiel für das Zusam-
menspiel von Objekten - jedes Bauteil kapselt seinen Zustand (ganz
offensichtlich z.B. bei einem Kondensator), jedes Bauteil verbirgt seine
Funktionsdetails und reagiert nur auf Nachrichten (hier: Elektronen) -, es
gibtdafürsogareineetabliertevisuelleModellsprache.DieselbeSchaltung
als Entwurf:
EntwurfeineProblemlösungbestehendausechtenObjekten
Jedes Objekt ist hier sogar mit einem eigenen Symbol repräsentiert. Die
Verbindungen sind ganz deutlich, während sie im Schaltungsaufbau nicht
mehr so gut nachvollziehbar sind.
Das ist für mich gelebte radikale Objektorientierung! Elektronische Schal-
tungen folgen PoMO und IOSP. Die Bauteile stellen die Objekte dar, sie
leisten etwas, sie operieren. Und die Drähte zwischen den Bauteilen bzw.
geätzte Leiterbahnen inklusive Platine integrieren diese Objekte.
Mit elektrischen und elektronischen Schaltungen gab es schon Erfahrung
bevor die ersten Computer gebaut wurden. Im Zuge der Weiterentwick-


---


<!-- Page 137 of 584 -->


03-RadikaleObjektorientierung 128
lung der Hardware von Computern wurde die Erfahrung massiv aus-
gebaut. Aus Computern basiert aus Releais wurde solche mit Röhren,
dann Transitoren, dann integrierten Schaltkreisen. Warum hat man sich
nicht an dieser vor Augen stehenden “Objektorientierung” in der Soft-
wareentwicklung orientiert? Es wäre so einfach, ja, im wahrsten Sinn
des Wortes so naheliegend gewesen? Spätestens als Alan Kay dann seine
Analogie formuliert hat, in der ja nicht nur biologische Zellen, sondern
sogar “computers on a network” vorkamen, hätte man doch aufhorchen
können.
Doch das geschah nicht. Auch seit 1985 mit C++ und dann 1995 mit
Java hat es kein wirkliches Umdenken in Richtung echter Objektorientie-
rung gegeben. Ein anderes “Meta-Modell” von Software herrschte in den
Köpfen vor. Software war eben nicht gedacht als Maschine, weder eine
elektronische, noch eine Maschine. Selbst wenn man es vielleicht Kindern
und interessierten Verwandten so erklärt hat, wurde diese Vorstellung
nicht gelebt.
Das ist für mich der Grund, warum die Objektorientierung nicht wirklich
zu einer Objektorientierung geführt hat. Alan Kay war auf dem richtigen
Weg, nur war seine Analogie mit biologischen Zellen vielleicht etwas
“outspaced”. Hätte er auf elektronische Schaltungen verwiesen, wäre
vielleicht alles anders gekommen. Aber er hat nicht gesagt:
“I thought of objects being like components on an electronic
cirquit board, only able to communicate with messages ins-
tead of electrons.”
Ichglaube,damit wäreviel mehrviel klarergewesen.Aberdie Geschichte
ist anders verlaufen…
Doch gegen welche Vorstellung hat die radikale Objektorientierung es
nicht geschafft sich durchzusetzen? War war das “Meta-Modell” für
Software?
Ich glaube, dass Software nicht Maschinen, sondern Organisationen nach-
empfunden wurde: “Und der Mensch schuf Software ihm zum Bilde, zum
Bilde seiner Organisationen schuf er sie; und schuf eine Befehls- und
Kontrollhierarchie.”⁸⁰
⁸⁰Freinach1.Moses1.27derLutherbibel1912


---


<!-- Page 138 of 584 -->


03-RadikaleObjektorientierung 129
Das ist der Grund, warum funktionale Abhängigkeiten vorherrschen. Das
ist auch der Grund, warum sich Software so schwer verändern lässt, wie
Unternehmen.
Eine Befehls- und Kontrollhierarchie (command-and-control (manage-
ment)) ist nach Wikipedia⁸¹ u.a. gekennzeichnet durch:
• Top-down Hierarchie, d.h. oben finden Entscheidungen statt, die
nach unten durchgereicht werden.
• Entscheidungenfindennichtdortstatt,wodieArbeitgeleistetwird;
dafür müssen Informationen von unten nach oben fließen, d.h.
untere Ebenen arbeiten oberen zu.
• Die Organisation ist unterteilt in Silos (Abteilungen), die möglichst
wenig miteinander zu tun haben. Silos fassen Mitarbeiter nach
Ähnlichkeit zusammen.
• Höhere Hierarchieebenen weisen untere an und kontrollieren die
Ausführung.
Übersetzt in die Sprache der radikalen Objektorientierung bedeutet das:
Befehls- und Kontrollorganisationen verstoßen massiv gegen PoMO und
IOSP. Sie sind sozusagen die Antithese zur radikalen Objektorientierung,
weil sie auf funktionaler Abhängigkeit beruhen.
Wenn du auf dieses Schemabild eines Organigramms⁸²⁸³ schaust, dann
solltest du eine unheimliche Ähnlichkeit mit Klassenhierarchien in OO-
Programmen wahrnehmen.
⁸¹https://en.wikipedia.org/wiki/Command_and_control_%28management%29
⁸²https://de.wikipedia.org/wiki/Organigramm
⁸³Bildquelle:Sprenger,CCBY-SA3.0


---


<!-- Page 139 of 584 -->


03-RadikaleObjektorientierung 130
Am Ende ist die auch nicht zu vermeiden; Software muss hierarchische
organisiert sein. Doch die Frage ist, was die Verantwortlichkeit der Hier-
archieebenen ist. In der mainstream Objektorientierung gibt es da keinen
Unterschied.AufjederEbenewirdgeleistet,operiert,Logikausgeführt.Im
Extremfall ist das als Micromanagement⁸⁴ spürbar; dann ist auch wirklich
jedem “Untergebenen” klar, dass eine höhere Ebene zur Aufgabe einer
daruter liegenden aktiv beitragen will.
Dass es zu Micromanagement überhaupt kommen kann, liegt aus meiner
Sicht daran, dass höhere Ebenen den Anspruch haben, etwas von dem
zu verstehen, was weiter unten passiert. Das ist kein Wunder, wenn
MitarbeiteraufhöhererEbenevonuntenüberdieKarriereleiternachoben
aufgestiegen sind. Sie lassen nicht einfach ihre Fachkenntnis unter sich
zurück. Immerhin sind sie doch als besonders gute Fachleute nach oben
berufen worden. Warum sollten sie dann nicht erstens aktiv kontrollieren,
was unten passiert, und zweitens auch noch mitarbeiten, insbesondere,
wenn es unten schief läuft?
Und genau so ist Software aufgebaut. Allerdings wächst sie eher von oben
nachuntendurchRefaktorisierung.HierdreitypischeEntwicklungsschrit-
te für ein Hello-World Programm.
Das könnte die erste Version sein, die im Versuch-und-Irrtum-Modus
heruntergehackt wurde. Eine Klasse, eine Methode, die komplette Logik
darin enthalten:
⁸⁴https://en.wikipedia.org/wiki/Micromanagement


---


<!-- Page 140 of 584 -->


03-RadikaleObjektorientierung 131
1 class Program
2 {
3 static void Main(string[] args) {
4 while (true) {
5 Console.Write("Name: ");
6 var name = Console.ReadLine();
7 File.AppendAllLines("gästeliste.txt", new[]{name});
8 var namen = File.ReadAllLines("gästeliste.txt");
9 var namensgruppen = namen.OrderBy(x => x).GroupBy(x => x);
10 var besuche = namensgruppen.Select(x => (Name:x.Key, Häufigkeit:x.Count()));
11 var häufigkeit = besuche.First(x => x.Name == name).Häufigkeit;
12 // vereinfachte Logik für die Bestimmung der Begrüßung:
13 var begrüßung = $"Hello, {name}! Number of visits: {häufigkeit}";
14 Console.WriteLine(begrüßung);
15 }
16 }
17 }
Das funktioniert und ist für diese Problemgröße auch kein Problem. Den-
noch kann jemand, der später daran arbeitet auf den Gedanken kommen,
eseinwenigsaubererzumachen,umzumBeispieleinenBereichderLogik
testen zu können. Der führt zum Beispiel eine “Geschäftslogik” ein:
1 class Program
2 {
3 static void Main(string[] args) {
4 var dom = new Geschäftslogik();
5
6 while (true) {
7 ...
8 var begrüßung = dom.BegrüßungErmitteln(name, besuche);
9 Console.WriteLine(begrüßung);
10 }
11 }
12 }
13
14
15 class Geschäftslogik
16 {
17 public string BegrüßungErmitteln(string name,
18 IEnumerable<(string Name, int Häufigkeit)> besuche) {
19 var häufigkeit = besuche.First(x => x.Name == name).Häufigkeit;
20 return $"Hello, {name}! Number of visits: {häufigkeit}";
21 }
22 }
Jetzt delegiert Main() einen Teil seiner bisherigen Verantwortlichkeit an
dieGeschäftslogik.Dassiehtganznatürlichaus-aberisteinProblem,weil
die Methode nun zwei Verantwortlichkeiten hat: sie operiert weiterhin,
integriert aber auch. Main() lässt es sich nicht nehmen, aktiv mit Logik
an der Herstellung des Gesamtergebnisses beteiligt zu sein.
Diese Form von halbherziger Auslagerung setzt sich in üblichen Codeba-
sen beliebig tief fort. Als nächstes ist vielleicht die Persistenz dran. Dafür
wird eine zweite “Abteilung” gegründet die mit der Geschäftslogik nichts
zu tun hat - und Program behält in Main() weiterhin die Zügel in der


---


<!-- Page 141 of 584 -->


03-RadikaleObjektorientierung 132
Hand. Main() definiert, wie nach den Namen gefragt wird und wie das
Ergebnis angezeigt wird, das es bei anderen in Auftrag gibt.
Doch nicht nur Main() behält die Zügel in der Hand und kontrolliert
mit eigener Logik weiter. Der Prozess der teilweisen Auslagerung von
Logik in die Tiefe kann sich auf jeder Ebene fortsetzen. Im Beispiel ist
ja die Ermittlung der Begrüßung noch ein Platzhalter. Warum dafür
nicht endlich die richtige Logik entwickeln? Am besten, in einer eigenen
Funktion in einer eigenen Klasse mit sehr spezifischer Verantwortlichkeit,
an die BegrüßungErmitteln() delegieren kann:
1 class Geschäftslogik
2 {
3 public string BegrüßungErmitteln(string name,
4 IEnumerable<(string Name, int Häufigkeit)> besuche) {
5 var templates = new Templates();
6
7 var häufigkeit = besuche.First(x => x.Name == name).Häufigkeit;
8 return string.Format(templates[häufigkeit], name);
9 }
10 }
11
12
13 class Templates
14 {
15 public string this[int häufigkeit] {
16 get {
17 // Annäherung an die volle Funktionalität
18 switch (häufigkeit) {
19 case 1: return "Hello, {0}!";
20 case 2: return "Welcome back, {0}!";
21 default: return "Hello my good friend, {0}!";
22 }
23 }
24 }
25 }
Merkst du, wie das “Organigramm” des Codes von oben nach unten
wächst. Wenn auf einer Ebene zu viel Logik ist, dann wird ein Teill davon
nach unten gedrückt. Eine Funktion wird extrahiert und vielleicht wird
sogar eine neue Klasse extrahiert. In jedem Fall aber bleibt Logik auf
der Ebene zurück, von der nach unten gedrückt wurde. Die Entwicklung
gleicht der in einem Unternehmen, wo ein Mitarbeiter sich überlastet
fühlt und Teile seiner Arbeit (Logik) wegdrückt zu anderen, die ihm
zuarbeitensollen.MeistenswerdennurTeiledereigenenArbeitinsolcher
Weise ausgelagert. Es bleibt also genügend Arbeit bei dem, der wegdrückt;
der will ja weiterhin seine Nützlichkeit durch eigene Arbeit für das
Unternehmen deutlich machen. Der Glaube: Es wäre zu wenig übrig,
wenn alles weggedrückt würde und nur noch Koordination (Integration)
übrig bliebe.


---


<!-- Page 142 of 584 -->


03-RadikaleObjektorientierung 133
Was aber noch schlimmer ist im Code: Wo Logik ist, kommt schnell
weitere Logik hinzu. Denn es ist leichter, zu bestehender Logik einfach
weitere für neue Anforderungen hinzuzusetzen, als sich zu überlegen, wie
die Struktur bestehend aus Funktionen und Klassen insgesamt verändern
ließe. Entwurf ist schwieriger, als Logik zu addieren. Das Ergebnis sind
Funktionen, die wachsen und wachsen und wachsen. Ab und an wird aus
ihnen etwas extrahiert, d.h. in tiefere Hierarchieebenen runtergedrückt.
Doch für jede Zeile, die ausgelagert wird, kommen gern mehrere hinzu.
Das ist der Grund, warum du Funktionen mit 100, 500, 5000 Zeilen findest.
Auch die mainstream Objektorientierung hat kein Maß gefunden dafür,
was eine Funktion, was ein Objekt an Logik enthalten sollte. Um Logik
geht es weiterhin. Sie leistet das, was der Kunde will. Mit der mainstream
Objektorientierung ist nur eine Idee in die Welt gekommen, wie man die
Zahl der Orte, auf die Logik verteilt, erhöhen kann. Ein System dafür gibt
es aber nicht. Oder wenn, dann wird es massiv seit 30 Jahren ignoriert.
Es fehlen Prinzipien und Regeln zur Begrenzung Verantwortlichkeit von
Funktionen und Klassen.
In Unternehmenshierarchien gibt es den Begriff Machtfülle. Damit wird
beschrieben, wie weitreichend die Eingriffsmöglichkeiten eines Mitarbei-
ters insbesondere in die Aktivitäten unter ihm angesiedelter Ebenen ist.
Das Ideal ist, viel Macht zu haben. Dafür gibt es viel Gehalt. Dann ist man
weit oben im Organigramm angesiedelt.
Demistauchgrundsätzlichnichtsentgegenzusetzen,wenndennsteigende
Machtfülle mit einem Loslassen einherginge. Je weiter oben im Organi-
gramm eine Position ist, desto weniger darf sie sich in die Operation unter
ihr einmischen. Wer oben im Organigramm operativ tätig bleibt, d.h. im
Tagesgeschäftentscheidend,derbehindertdieHerstellungvonWertdurch
die Operation. Er ist schlichtweg ein Flaschenhals.Management attention
ist laut Engpasstheorie⁸⁵ der ultimative Engpass.
Erste Aufgabe eines Managers ist es also, sich auf die Integration zu
beschränken. Seine Aufgabe ist es eben nicht, daran beteiligt zu sein, was
unter ihm hergestellt wird. Sein Fokus ist allein die Ermöglichung dieser
Herstellung. Er ist derjenige, der tiefer hängende Ebenen integriert zu
einem Prozess, in dem die Arbeitsergebnisse behinderungsfrei fließen.
Dass eine Prozessorientierung statt einer Abteilungsorientierung bessere
⁸⁵https://de.wikipedia.org/wiki/Theory_of_Constraints


---


<!-- Page 143 of 584 -->


03-RadikaleObjektorientierung 134
ErgebnissebringtfürUnternehnen,istderManagementlehreschonlänger
nicht entgangen. Doch in Unternehmen gilt old habits die hard. Die
command-and-control Denke ist Tausende Jahre alt, hat bis vor vielleicht
50 Jahren auch noch annehmbare Ergebnisse erzielt und ist tief in den
TraditonenundGlaubenssätzenderGesellschaftverwurzelt.Daslässtsich
nichteinfachumwerfen,nurweildieWeltindenletzten30Jahrensostark
an Komplexität zugenommen hat.
Dass Software nach dem Bilde menschlicher Organisationen geformt
wurde,scheintmirgenausoklarwieunvermeidlich.DerComputerwurde
immer als Befehlsempfänger dargestellt. Damit war er der bessere Mit-
arbeiter im Sinne der überkommenen Vorstellung zur Unternehmensor-
ganisation. Das hat sich in der Struktur von Software niedergeschlagen.
Ist nicht der Programmierer wie ein Manager, der seinen Untergebenen
sagen muss, was sie wann tun sollen? Weiß der Programmierer es nicht
am besten und muss nun nur noch dafür sorgen, dass die Verhaltensher-
stellung kontrolliert geschieht? Dafür setzt er Statthalter ein: Klassen und
Funktionen.
Woher die Klassen mit ihren Funktionen kommen, sei dahingestellt. In
jedem Fall folgen sie dem “Meta-Modell”, dass sie eine Hierarchie bilden,
in der oben es besser weiß als unten und jederzeit daran beteiligt bleiben
darf, das Verhalten mittels Logik herzustellen.
Woher sollte auch eine andere Vorstellung kommen? Im Sinne eine
Kommandoausführung gab es keine anderen Beispiele, als die moderne
Programmierung mit Hochsprachen ab den 1950ern erfunden wurde.
Programmierer waren eingebettet in streng hierarchisch strukturierte
Unternehmen. Sie selbst waren Befehlsempfänger und waren beauftragt,
“virtuelle Untermehmen” zu bauen. Wie hätten sie auf die Idee kommen
können, dass deren Strukturen anders aussehen sollten, als die realer
Unternehmen?Oderumgekehrt:WiesolltensieaufdieIdeekommen,dass
reale Unternehmen anders strukturiert sein sollten, als sie waren?
Das war die Situation, in der Alan Kay ein radikal anderes Bild für Soft-
ware fand. Für Unternehmen ist es ihm nicht einmal eingefallen, nur für
Software. Doch in solchen kooperierenden, netzwerkartigen Strukturen
wurde nicht gearbeitet. Die in der Analogie steckenden Prinzipien PoMO
und IOSP wurden nicht gelebt - und so hat die Softwarewelt Alan Kays
Idee im Grunde nicht verstanden. Der Mainstream hat an der Spiegelung
hierarchier Unternehmensstrukturen in Software auch nach Übernahme


---


<!-- Page 144 of 584 -->


03-RadikaleObjektorientierung 135
der Objektorientierung festgehalten. Der Objektgedanke sollte als lokale
Optimierung für die Wiederverwendbarkeit helfen, produktiver zu wer-
den. Das Wurzelproblem inflexibler Softwaresysteme wurde damit aller-
dings nicht angegangen: die funktionalen Abhängigkeiten als Ausdruck
eines system-strukturellen Hangs zum Micromanagement.
Das änderte sich erst langsam, als monolithische Softwaresysteme über-
haupt aufgebrochen wurden durch Verteilung. Ihre Leistung in Bezug auf
SkalierbarkeitundPerformancekonntenurgesteigertwerden,indemman
Teile des Monolithen voneinander entkoppelte. Plötzlich hab es physisch
eigenständig laufende Funktionseinheiten, die nur durch Messaging kom-
munizieren konnten. Zwischen Threads gibt es keine request/response-
Kommunikation.
In den 1990ern hat diese Entwicklung begonnen und ist noch nicht zum
Abschluss gekommen. Actor-Frameworks und Micro-Services sind aber
Ausprägungen einer anderen Grundvorstellung von Software, die sich
weniger an der Struktur innerhalb von Unternehmen ausrichtet, sondern
eher an einem Markt oder anderen Netzwerken von Akteuren.
Dabei ist für eine bessere Organisation von Software ein solch massiver
Schritt hin zu neuer Technologie nicht nötig. Es reicht, die Vorstellung
von der Struktur zu ändern. Mit meinem hier geschilderten Verständnis
der radikalen Objektorientierung möchte ich die ein neues “Meta-Modell”
anreichen. Denke Software nicht länger als virtuelles Unternehmen nach
alter Väter Sitte. Denke Software nicht als Sammlung von Silos.
Im Vordergrund bei Software - und bei Unternehmen - sollte nicht
die Abteilung stehen, sondern der Prozess. Es geht immer noch darum,
dass für die Umwelt eine Leistung erbracht werden muss. Dafür ist ein
reibungsloses Zusammenspiel vielen Beteiligter in einem Prozess nötig,
der Wert für Benutzer herstellt. Abteilungen sind dafür sekundär. Primär
ist das, was einfach getan werden muss. Dafür sind Resultate entschei-
dend. Entlang eines Prozesses wird aus Reizen/Input unter Nutzung von
Ressourcen/Zustand eine Reaktion/Output generiert.
Dafür musst du die richtige Logik finden und zu Operationen zusammen-
fassen, die verständlich und testbar sind. Dafür musst du darüber liegend
die richtige Integration finden. Darum wird es im Weiteren gehen.
Die Softwareentwicklung hat für mich das Potenzial, die neue Leitdiziplin
der Gesellschaft zu werden. Früher waren es Religion und Militär, dann


---


<!-- Page 145 of 584 -->


03-RadikaleObjektorientierung 136
Industrie. Jetzt ist die Softwareentwicklung dran, weil sie von jeher mit
KomplexitätundderNotwendigkeitzurAnpassungihrerProdukteaneine
sich ständig wandelnde Umwelt zu tun hat.
Dieser Notwendigkeit können sich nun Unternehnen und auch die Gesell-
schaft nicht mehr entziehen. Und so kann sich der Prozess umgkehren:
Hat früher die Gesellschaft Software nach ihrem Bild von Unternehmen
geprägt, wird zukünftig Software die Gesellschaft nach ihrem Bild prägen.
DukannstTeildieserEntwicklungsein,indemduSoftwareabjetztradikal
anderes organisierst. PoMO und IOSP leiten dich dabei.


---


<!-- Page 146 of 584 -->


03-RadikaleObjektorientierung 137
Übungsaufgaben
Reflexionsaufgabe
Bitte formuliere eine Frage oder eine Erkenntnis zum Kapiteltext.
• Wo bist du gedanklich hängengeblieben, was ist dir unklar,
was passt für dich irgendwie nicht zusammen, wozu würdest
du dir noch etwas mehr Erklärung wünschen? Steht irgendet-
waszudeinerbisherigenPraxisimWiderspruchunddufragst
dich, warum du etwas ändern solltest?
• Oder: Wann hast du einen Aha-Moment gehabt, was ist
diralsbemerkenswert,spannend,ausprobierenswertaufgefal-
len? Hat irgendetwas “in dir Klick gemacht”, weil dir nun ein
Zusammenhang aufgegangen ist? Oder verstehst du jetzt aus
deiner bisherigen Praxis irgendetwas besser?
Am besten formulierst du Frage bzw. Erkenntnis schriftlich. Indem
du deine Gedanken aufschreibst, wirst du dir ihrer bewusster. Bei
einer Frage kommst du dadurch vielleicht schon einer Antwort aus
dir selbst heraus näher. Bei einer Erkenntnis fällt dir vielleicht schon
etwas ein, das du ab jetzt anders machen kannst.
Aufgabe - Mit PoMO/IOSP implementieren
DaswarjetzteineLadungTheorieundsogarPhilosophie.Aberdasmusste
leider sein. Das ist das Fundament, auf dem ich den Rest aufbauen werde.
DieradikaleObjektorientierungmitihrenPrinzipienistfürmicheinesehr
pragmatische Konkretisierung dessen, was Entwurf im Allgemeinen will:
Software eine Form geben.
Mit der radikalen Objektorientierung hat Software nun eine sehr, sehr
grundlegende Form, die wir im Weiteren erkunden werden. Sie hat
ImplikationenfürdasVorgehenbeimEntwurf,dieNotationvonModellen
und schließlich die Grobstruktur von Software, d.h. die Architektur.


---


<!-- Page 147 of 584 -->


03-RadikaleObjektorientierung 138
Bevor wir in die Modellierungspraxis aber einsteigen, eine kleine Auf-
gabe, um deine Codierungsgewohnheiten herauszufordern. Du steckst
wahrscheinlich gedanklich tief in der mainstream Objektorientierung mit
ihren unsäglichen funktionalen Abhängigkeiten.⁸⁶ Wie weit kannst du
dich aus daraus also schon befreien nach dem, was du über PoMO und
IOSP gelesen hast? Schaffst du es, aus den Codebeispielen eine eigene
Übersetzungspraxis abzuleiten, die einen Entwurf in Code überführt?
Du erinnerst dich an die Aufgabe aus Kapitel 2? Da ging es darum,
einem Patienten mit einem Testergebnis eine Auskunft zu geben,
wie belastbar dieses Ergebnis ist. Zum Beispiel: Wie hoch ist die
Wahrscheinlichkeit,dasseinpositiverTestwirklicheineErkrankung
meldet? Dazu hast du einen Lösungsansatz formuliert.
Auch und gerade weil dir ein Modell für den Lösungsansatz fehlt
- zumindest habe ich mir keines von dir gewünscht -, implemen-
tiere nun deinen Lösungsansatz unter Anwendung von PoMO und
IOSP. Bemühe dich wirklich, wirklich beide Prinzipien einzuhalten.
Vielleicht schaffst du das - vielleicht gibt es aber auch hier und da
Codeabschnitte, wo es dir schwer fällt. Es könnte sein, dass dir nicht
einfällt, wie du die Prinzipien technisch umsetzen kannst; es könnte
aber sein, dass dir eine technische Lösung einfällt, sich in dir aber
allesdagegenstreubt,weildiesokomischoderumständlichaussehen
würde.
Versuch es einfach mal und dann sprechen wir darüber. Wichtig ist
mir, dass du dich bemühst, dich auf PoMO/IOSP einzulassen. Ich
möchte deine Sinne schärfen für die Vorteile, die aus ihrer Anwen-
dung entstehen - und vielleicht auch die Grenzen ihrer Anwendung.
WasdujetztnochvoreinerImplementierungmitdeinemLösungsan-
satztust,istdirüberlassen.Vielleichtmodellierstdu“freiSchnauze”?
Das kannst du machen; Teil der Aufgabenlösung ist es nicht. Am
Ende zählt nur dein Code.
⁸⁶Das ist keine Kritik, sondern nur eine Feststellung, eine Ahnung. Du liest dies hier ja
schon aus dem Willen heraus, zukünftig etwas anders zu machen. Irgendwie hast du schon
dasGefühlgehabt,dassetwasnichtstimmenkannmitderbisherigenHerangehensweise.


---


<!-- Page 148 of 584 -->


04 - Flow-Design mit
1-dimensionalen
Datenflüssen
Jetzt wird’s formal. Tut mir leid, das kann ich dir nicht ersparen. Aber
versprochen, es wird nicht schlimm: so wenig formal wie möglich, aber
eben auch so viel wie nötig. Ohne die Präzision einer formalen Modell-
Notation wird es dir sonst schwer fallen, deine Lösungsansätze so zu
präzisieren, dass du sie leicht in Code übersetzen kannst. Ohne die
Präzision einer Notation ist auch die Kommunikation eines Modells an
andere umständlich und/oder verlustbehaftet.
Formalität empfindest du wahrscheinlich als eher begrenzend, behin-
dernd. Das kann ich verstehen. Aber in dieser Begrenzung steckt etwas
Positives; sie befreit dich auch anderersseits davon, dir über bestimmte
Dinge immer wieder Gedanken zu machen. Versuch’ doch einmal, das
Formale als Baukasten zu reframen; aus dem kannst du dich bedienen,
um etwas Schönes herzustellen.
Die Notation für Musik ist auch sehr formal, sehr genau. Dennoch (oder
gerade deshalb?) gibt es so viel wunderbare Musik, die sich dadurch
ausdrücken lässt.
Aber keine Angst, so umfangreich und kompliziert soll es hier nicht
werden. Ich möchte dir eine leichtgewichtige Notation vorstellen, die


---


<!-- Page 149 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 140
wirklich praxistauglich ist.⁸⁷
Im vorherigen Kapitel habe ich dir vermitteln wollen, dass für mich
das Meta-Modell für Software in der radikalen Objektorientierung liegt.
Sie liefert mir wirklich eine greifbare Vorstellung davon, “was Software
im Innersten zusammenhält”. Wenn Organismen aus biologischen Zellen
bestehen, dann besteht Software aus Objekten. Das ist natürlich noch
nicht alles bei Organismen und also auch nicht bei Software, doch es ist
ein Start, ein Rahmen, eine grundlegende Vorstellung.
DamitdieseVorstellunginderPraxisRelevanzbekommenkann,mussich
Software “nach ihrem Bilde” schaffen können. Ich muss sie so codieren,
vorher muss ich sie jedoch schon so entwerfen. Ich muss Lösungen als
konkrete Modelle dieses Meta-Modells visualisieren.
Mein Mittel dafür ist das, was ich Flow-Design nenne. Flow-Design ist
eine Methode, die ich zusammen mit Kollege Stefan Lieser über viele
Jahre der Beschäftigung mit Clean Code Development Prinzipien und
Praktiken entwickelt habe. Darin eingegangen ist, was sich als praktikabel
in Projekten und Trainings herauskristallisiert hat. Flow-Design ist also
keine Kopfgeburt, sondern das Ergebnis von Versuch-und-Irrtum. Die
Theorie hat seine Praxis beeinflusst - und die Praxis hat wiederum
die Theorie beeinflusst. Seinen Anfang hat Flow-Design irgendwann ab
2006 gehabt im Zusammenhang mit Microsofts Concurrent Coordination
Runtime⁸⁸ - glaube ich zumindest. Relativ stabil war es allerdings erst um
2013, als ich darüber unter dem Titel OOP as if you meant it⁸⁹ geschrieben
habe.DochauchanschließendhatsichnocheinigesanFlow-Designgetan;
immer wieder gibt es mal Verfeinerungen oder Klärungen. Flow-Design
⁸⁷Meine Notation mag dich hier und da an UML erinnern und du fragst dich dann
vielleicht, warum es nicht UML ist. Oder du findest, die Notation ist ganz anders, und
stellst dir dieselbe Frage. Meine Antwort darauf: Weil UML eben nicht praxistauglich
leichtgewichtig ist. Wäre UML praxistauglich leichtgewichtig, dann wäre UML weithin im
Praxiseinsatz beim Entwurf. Das ist aber nicht der Fall. Meine - zugegeben informellen -
Erhebungen bei Konferenzen liefern seit Jahren dasselbe Ergebnis: ca. 10% der Teilnehmer
setzenUMLein,nur5%gehendabeiüberKlassendiagrammeodermaleinSequenzdiagramm
hinaus. Wenn 90% der Entwickler UML also nicht einsetzen, dann ist UML mit seinem
Anspruchgescheitert.DieIdeedahinterwargut-dochirgendwiehatesebennichtgeklappt.
Deshalb sollten wir formale, visuelle Notationen aber nicht abtun. Auch in der UML ist ja
Nützlichesdrin.IchsehesiealsSteinbruch.Wennsiemichjedochbeengt,dannverlasseich
sie.Wennduwillst,verstehediehiesigeNotationals“UML-inspiriert”.
⁸⁸https://en.wikipedia.org/wiki/Concurrency_and_Coordination_Runtime
⁸⁹http://geekswithblogs.net/theArchitectsNapkin/archive/2013/09/08/oop-as-if-you-
meant-it.aspx


---


<!-- Page 150 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 141
ist mithin selbst ständig im Fluss. Die Stromschnelle liegen jedoch schon
seit Jahren hinter dem Ansatz. Der Fluss ist ruhig und stark. Flow-Design
ist tragfähig und beweist sich jeden Tag in der Praxis.
Du siehst, ich bin überzeugt von Flow-Design. Sonst würde ich dich dazu
ja auch nicht motivieren wollen. Das bedeutet aber nicht, dass ich Flow-
Design für allein selig machend oder für eine silver bullet halten würde.
Mit Flow-Design sind nicht alle deine Entwurfsprobleme gelöst. Allemal
musst du ja immer noch überhaupt auf eine Lösung kommen; dabei kann
ich dir quasi gar nicht helfen. Trotzdem halte ich Flow-Design für sehr,
sehr nützlich als Denkwerkzeug und auch zur Kommunikation von und
über Lösungen im Team. Mit Flow-Design kannst du Softwarelösungen
einfach plastisch machen, unabhängig davon, ob du dich Anhänger einer
Objektorientierten Programmierung oder Funktionalen Programmierung
siehst.
Nun aber genug der Vorrede! Steigen wir ein ins Flow-Design…
0-dimensionale Datenflüsse
Flow-Design basiert auf der radikalen Objektorientierung. Im Kern von
Flow-Design steht deshalb das Messaging. Und das bedeutet, Lösungen
drehen sich um den Fluss von Nachrichten, also um Datenfluss. Mit Flow-
Design modellierst du Lösungen konsequent in Form von Datenflüssen.
Datenflüsse, nicht Kontrollflüsse! Der Unterschied mag dir noch nicht
voll bewusst sein und auch nicht Relevanz haben; dennoch solltest du ihn
fühlen und verinnerlichen. Gib dir dafür ruhig etwas Zeit.
Der Einstieg in die “Datenflussdenke” ist zum Glück einfach. Wenn du
schonmal von EVA gehört hast, dann bist du gut gerüstet:
EVA: Eingabe - Verarbeitung - Ausgabe
Google Books nennt eine Ausgabe der Zeitschrift für Datenverarbeitung
aus dem Jahr 1973 als erste Quelle, in der das EVA-Prinzip erwähnt ist.
Aber ich vermute, das Prinzip ist älter. Es ist ja auch so naheliegend und
einfach.
• Da ist ein “Informationsverarbeiter”,


---


<!-- Page 151 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 142
• der wird “gefüttert” mit einer Eingabe und
• produziert daraufhin eine Ausgabe.
Die Eingabe fließt in die Verarbeitung und die Ausgabe fließt aus der
Verarbeitung heraus. Das kann man so visualisieren:
Im Flow-Design heißt die Verarbeitung ganz allgemein Funktionseinheit:
• Die Verarbeitung steht für eine Funktion(alität), die sich ein Auf-
traggeber direkt oder indirekt wünscht.
• Sie wird ultimativ von einer programmiersprachlichen Funktion
erbracht.
• Aber das Symbol für die Verarbeitung ist nicht (immer) gleichzuset-
zen mit einer Funktion.
Flow-Design beginnt mit diesem simplen Zusammenhang: Daten fließen
in eine Funktionseinheit, die sie in andere Daten transformiert, die aus ihr
herausfließen. So ist es immer und überall in Software, im Kleinen wie im
Großen.DieFunktionaleProgrammierungsingtdirgerneinLieddavon.⁹⁰
Eine solche Funktionseinheit verstehe ich als Punkt, ein Verarbeitungs-
punkt in einem Modell, d.h. als 0-dimensionales Konstrukt wie einen
⁹⁰WasduinderAbbildungsiehst,isteigentlicheinereineFunktion(purefunction).Ohne
weitereZusätzeistzuerwarten,dassfürgleicheEingabeimmerdieselbeAusgabeerarbeitet
wird.


---


<!-- Page 152 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 143
mathematischen Punkt. Eine ganze Software kann durch einen solchen
Punkt repräsentiert werden oder nur eine von Millionen Funktionen in
einer Software.
Wie passt das mit der radikalen Objektorientierung zusammen? Was ist
eine Funktionseinheit in Bezug auf sie, ist sie ein Objekt? Ich würde
gern sagen, die Funktionseinheit sei ein Objekt. In einer frühen Form des
Flow-Design war das auch tatsächlich der Fall. Letztlich hat sich jedoch
herausgestellt, dass das nicht nötig ist; allemal nicht, wenn man daraus
ableitet, dass jede Funktionseinheit des Modells zu einer Klasse im Code
wird.
Eine Funktionseinheit ist zumindest kein Objekt im Sinne der mainstream
Objektorientierung. Im Sinne der radikalen Objektorientierung ist sie al-
lerdings “das Ding”, das etwas tut und mit anderen über einen Datenfluss
in Verbindung steht. Das hört sich doch irgendwie wie “Objekt” an, oder?
So ganz kann das aber nicht stimmen, weil das, was da fließt, (meistens)
keine vollständigen Nachrichten sind, sondern nur payloads von Nach-
richten. Denn die Funktionseinheiten selbst stehen im Grunde für Nach-
richten. Ein “echtes” Objekt als Funktionseinheit würde anders aussehen.
Ich stelle mal zwei Varianten gegenüber:
Flow-Designarbeitet(meistens)mitden“runden”Funktionseinheitenwie
Registrieren und Laden links. Sie sind auf eine Verantwortlichkeit
fokussiert. Das SRP lässt grüßen. Die “kastenförmige” Funktionseinheit
hingegen tut mehr und lässt den Verarbeitungsprozess in größeren Model-
len verschwimmen. Auch wenn die Gästeliste als “Objekt” plausibler
erscheint, ist sie nicht praktisch. Alan Kay mag sich soetwas zwar vorge-


---


<!-- Page 153 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 144
stellt haben - ein Objekt, das verschiedene Nachrichten verarbeiten kann
-, doch entwerfen lässt sich damit nicht vorteilhaft, wie du bald feststellen
wirst.
Was sind also die “elliptischen” Funktionseinheiten? Nimm sie einfach
als… abstrakte Funktionseinheiten, ohne sie sofort auf ein programmier-
sprachliches Konstrukt übersetzen zu wollen. Sie leisten etwas im Daten-
fluss.SiekapselnDetails.DasistdasWesentliche.IhrNameistProgramm.
Er beschreibt ihre Funktionalität kurz und knapp.
Notation
Die Notation für den Grundbaustein des Flow-Design ist simpel, aber
nicht beliebig.
• Die Funktionseinheit wird üblicherweise als Ellipse oder Kreis
dargestellt, um sie von Klassen zu unterscheiden.
• Einfließende Daten, die Eingabe, werden durch einen Pfeil symbo-
lisiert, der auf die Funktionseinheit zeigt.
• Ausfließende Daten, die Ausgabe, werden ebenfalls durch einen
Pfeil symbolisiert, der nun von der Funktionseinheit weg zeigt.
• Welche Daten ein- bzw. ausfließen, wird am Pfeil in Klammern
notiert. Immer! Selbst wenn keine Daten fließen, sondern nur
sozusagen “ein Signal”, sollen Klammern am Pfeil notiert sein. Der
Sinn hinter diesem Gebot: Nur wenn Klammern am Pfeil stehen, ist
klar,dassdu dirGedankendarübergemachthast,wasfließt. Fehlen
die Klammern, ist es unklar, ob du dir Gedanken gemacht hast oder
nichts fließen soll.
Beispiel:


---


<!-- Page 154 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 145
• Bestehen fließende Daten aus mehreren Teilen - hier z.B. a und b
bei der Eingabe -, dann werden die innerhalb der Klammer durch
Komma getrennt aufgeführt.
Funktionseinheiten mit Seiteneffekten
Eine Funktionseinheit braucht immer eine Eingabe, produziert jedoch
nichtimmerDateneineAusgabe,wiedirobenvielleichtschonaufgefallen
ist. Ohne Eingabedaten gäbe es keinen “Reiz”, der eine Funktionseinheit
zur (Aufnahme der) Verarbeitung veranlässt. Das Resultat der Verarbei-
tung kann jedoch in etwas anderem bestehen als Ausgabedaten, die dann
weiterfließen.
Wenn eine Funktionseinheit keine Ausgabe, also keine hinausfließenden
Daten produzieren muss, was macht sie dann aber mit der Eingabe? Sie
soll ja nicht nur Wärme durch Prozessoraktivität erzeugen.
Funktionseinheiten - oder “radikale Objekte” - kapseln nicht nur ihre
Logik, sondern auch ihren Zustand. Einfließende Daten können also auch
schlicht auf Zustand einwirken, ohne in ausfließende Daten transformiert
zu werden.
Verallgemeinertbedeutetdas:FunktionseinheitenkönnenvonRessourcen
abhängig sein. Diese Abhängigkeit verbergen sie vor ihrer Umwelt, doch
sie existiert nichtsdestotrotz und sollten auch im Modell visualisiert
werden können. Das sieht dann so aus:


---


<!-- Page 155 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 146
• Die Abhängigkeit von einer Ressource - das kann Speicher oder
andere Hardware sein - wird nicht mit einem Pfeil symbolisiert,
sondern mit einer “Abhängigkeitslinie”: der Punkt am Ende zeigt
an, dass sich die Funktionseinheit an der Ressource “befestigt hat”;
sie braucht die Ressource, sie hält sie fest, sie kontrolliert sie.
• Daten können entlang der Abhängigkeitsbeziehung grundsätzlich
in beide Richtungen fließen (das symbolisieren die Pfeile an der
“Abhängigkeitslinie”). Manchmal ist allerdings eine Richtung vor-
herrschend. Die Details der Kommunikation mit einer Ressource
sind gewöhnlich nicht Bestandteil eines Flow-Design Modells. Die
Pfeile an der “Abhängigkeitslinie” machen aber insbesondere dann
Sinn, wenn eine Richtung betont werden soll.
Durch Abhängigkeiten quer zum Datenfluss können Funktionseinheiten
Seiteneffekte erzeugen. Im Sinne der Funktionalen Programmierung wer-
den sie dadurch “unrein”: dieselben Eingabedaten können zu unterschied-
lichen Ausgabedaten führen. Flow-Design sieht das allerdings nicht als
Problem an. Es ist vielmehr die Natur der Dinge, ja geradezu der Zweck
von Software. Software soll Seiteneffekte haben. Ohne Seiteneffekte gibt
es keine spürbaren Ergebnisse für Anwender.
Allerdings anerkennt Flow-Design, dass es schwerer ist, Funktionsein-
heiten mit Seiteneffekten zu testen. Deshalb sollten Seiteneffekte bzw.


---


<!-- Page 156 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 147
Abhängigkeiten von Ressourcen im Model kenntlich gemacht werden. So
lassen sich frühzeitig Maßnahmen treffen, um sie einzuhegen. Wie du
später sehen wirst, geben solche Abhängigkeiten wichtige Hinweise für
die Modularisierung.
Implementation
Die Übersetzungsregel für Funktionseinheiten will ich zunächst pauschal
und einfach halten. Überhaupt in Datenflüssen zu denken und eine solche
Notation zu benutzen, ist für dich wahrscheinlich Umgewöhnung genug.
Deshalb lautet die Regel:
• Funktionseinheiten werden zu Funktionen im Code
• Die Eingabe wird zu Parametern der Funktion. Sollten keine Daten
fließen und die Datenklammer auf dem Pfeil leer sein, dann hat die
Funktion keine Parameter.
• Die Ausgabe wird zum Funktionsresultat. Sollten keine Daten flie-
ßen und die Datenklammer auf dem Pfeil leer sein, dann ist es eine
void-Funktion. Das ist auch der Fall, wenn es keinen Ausgabe-Pfeil
gibt wie bei Registrieren oben.
Beispiele:
1 int Addieren(int a, int b) {...}
2
3 void Registrieren(string name) {...}
4
5 Besuche Laden() {...}
Dass Registrieren() wie auch übrigens Laden() abhängig von einer
Ressource sind, ist den Funktionen selbst nicht anzusehen. Die Abhängig-
keit ist ein Implementationsdetail.
Im Augenblick bekümmere dich auch nicht darum, welcher Klasse die
Funktionen angehören. Um die Modularisierung kümmern wir uns später.
An dieser Stelle nimm einfach nur mit: Funktionseinheiten werden zu
Funktionen. Fertig. Daten fließen als Parameter hinein und als Funktions-
resultate ‘raus. Das ist alles.
So einfach kann Flow-Design sein!


---


<!-- Page 157 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 148
“Kringel”⁹¹, Pfeil, Klammern: das ist das Wesentliche der Flow-Design
Notation.⁹²
1-dimensionale Datenflüsse
Konzeptionell sind 0-dimensionale Datenflüsse wichtig. Sie sind die Bau-
steine, aus denen Flow-Designs zusammengesetzt werden; deshalb habe
ichsieandenAnfanggestelltundihreElementeerklärt.Praktischrelevant
sind sie für sich genommen aber eher nicht. Welches Problem kannst du
durch nur eine Funktionseinheit lösen? Es braucht also eine Möglichkeit,
0-dimensionale Datenflüsse zu “höherdimensionalen” zu verbinden. Der
erste Schritt dazu sind - wie könnte es anders sein - 1-dimensionale
Datenflüsse.
InderMathematikistdieLinie1-dimensional.Siebestehtaus0-dimensionalen
Punktenbzw.verbindet0-dimensionalePunkte.ImFlow-DesignistdieSe-
quenz das 1-dimensionale Konstrukt: Funktionseinheiten werden einfach
“hintereinander geschaltet”. Als Illustration ein Beispiel aus dem Hello-
World Szenario:
Jetzt wird ein Verarbeitungsprozess sichtbar: Eingabedaten durchlaufen
mehrere Verarbeitungsschritte, bis die endgültige Ausgabe hergestellt ist.
⁹¹ObdudieFormfüreineFunktionseinheitKringel,Blase,bubble,Ellipse,Kreisnennst,
istegal.ImModellstehtsieeinfachfüretwasAbstraktes,dasverarbeitet.DieDetails,allemal
die Logik, sind dir nicht bekannt, wenn du sie malst. Sie sollen auch unwichtig sein für das
Verständnis der Verantwortlichkeit einer Funktionseinheit. Zwar heißt es “Bubbles don’t
crash” und deshalb muss auch die Übersetzung von Flow-Design Modellen einfach sein,
damit du sie schnell verifizieren kannst. Deshalb musst du trotzdem nicht alles über eine
Funktionseinheitwissen,wenndusiemalst.
⁹²Ok, fast. Ein bisschen mehr ist schon nötig, um wirklich aussagekräftige Modelle
zeichnen zu können, doch diese drei Elemente sind das Fundament. Selbst die Ressourcen-
abhängigkeit muss nicht absolut zwingend im Modell auftauchen oder genau so dargestellt
werden. Überhaupt geht es nicht um “genau so”, also die Syntax, sondern um die Semantik.
Dassdaetwasfließtundtransformiertwird,istderKern;dasgilteszuvisualisieren.


---


<!-- Page 158 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 149
InsolcherWeisekannstduFunktionseinheiten“verdrahten”,wennsievon
ihrenEingabe-bzw.Ausgabedatenherzusammenpassen.DieAusgabeder
einen Funktionseinheit wird zur Eingabe einer anderen.
WenndichdasaneineelektronischePlatineerinnert,kannichdassehrgut
verstehen.DenBegriff“Verdrahtung”benutzeichbewusst.Obensiehstdu
also eine “Reihenschaltung”.⁹³
Das Wichtigste an dieser Darstellung, besser: Denkweise ist:
• Es handelt sich um einen Datenfluss, keinen Kontrollfluss. Daten
fließen: Ausgaben werden zu Eingaben; Kontrolle fließt nicht. Die
Kontrolle bleibt ganz fundamental in den Funktionseinheiten! Das
bedeutet, alle Funktionseinheiten haben gleichzeitig die Kontrolle.
In der radikalen Objektorientierung gibt es also im Grunde nur
Parallelverarbeitung. Die ist nicht einmal betonenswert, weil sie
⁹³Wenndudarausschließt,dassesaucheine“Parallelschaltung”gebenmüsste,liegstdu
richtig.Dochdazuerstspätermehr,wennduetwasÜbunghastmitdemFlow-Design.


---


<!-- Page 159 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 150
in der Analogie mit den biologischen Zellen tief drin steckt. Jede
Zelle lebt für sich, ist autonom. Dasselbe gilt für die Computer
in einem Netzwerk, auf die Alan Kay auch anspielt; sie arbeiten
alle selbstständig. Für ihn sind Objekte also “Dinger”, die autonom
sind. Sie reagieren auf Nachrichten in Parallelität. Wie lange sie
nach einem Reiz durch eine Nachricht aktiv bleiben, ist ihre Sache.
Sie können also Ausgaben erzeugen und damit andere Objekte
anstoßen - und trotzdem mit irgendetwas weitermachen.⁹⁴ Diese
Sichtweise musst du im Hinterkopf haben! Sie macht dich freier,
Lösungen zu modellieren, auch wenn du diese Freiheit nicht immer
brauchst. Mehr dazu bei 3-dimensionalen Datenflüssen.
• Im Datenfluss gibt es keine Schleifen! Die Daten fließen immer
nur in eine Richtung. Diese Einschränkung ist wichtig, um die
Deklarativität von Datenflussmodellen zu betonen. Du bist sehr
wahrscheinlich versucht, Lösungen in Form von Schleifen, gar
ineinander geschachtelten Schleifen zu denken. Das ist imperatives
Denken. Damit bewegst du dich sehr nah, zu nah an der Implemen-
tation. Du verlierst doch damit im Detail. Das belastet dich unnötig
im Entwurf; du wirst langsam. Zwar könntest du eine Schleife in
einem Flow-Design Diagramm zeichnen - doch du würdest dir
damit keinen Gefallen tun.⁹⁵ Vergiss für die Modellierung also
Schleifen
Wie ein Datenfluss fließt, ob horizontal, vertikal, von links nach rechts
oder rechts nach links, mänandrierend… das ist alles nicht wichtig; achte
nur darauf, dass die Flussrichtung leicht zu verfolgen ist; die Pfeile weisen
⁹⁴Die Nähe zum Actor Model ist nicht zu leugnen. Alan Kay hat auch mal gesagt -
wenn ich mich recht erinnere; leider finde ich die Quelle nicht mehr -, dass er vielleicht
Objekte zu “klein”, zu feingranular gedacht hat. Seiner Idee würden eigentlich Actors ganz
gutentsprechen.
⁹⁵Denk an Flip-Flops als elektronische Schaltung oder den Multivibrator im vorher-
gehenden Kapitel. Darin wird der Output eines Bauteils zu einem Input für ein anderes
Bauteil,daseinenOutputerzeugt,derwiederzumInputfürdaserstewird.Dasistdeutlich
schwieriger zu verstehen als eine Reihenschaltung. Oder denke an eine Rückkopplung
zwischenLautsprecherundMikrofon:dortsorgtdieAusgabedesLautsprechersalsEingabe
für das Mikrofon, das ihn speist, zu einem unangenehmen Ergebnis. Schleifen machen
dir das Verständnis von Datenflüssen (oder auch Kontrollflüssen) ganz schnell kaputt. Die
FunktionaleProgrammierungistnichtumsonstauchbekanntals“schleifenlos”.


---


<!-- Page 160 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 151
ja aber den Weg. Allerdings: Eine Schleife sollte nicht darin sein.⁹⁶
Der Datenfluss als Scope
Im obigen Beispiel einer “Reihenschaltung” siehst du ein Datum zweimal
auftauchen: name; es ist der Input für heraussuchen und Begrüßung
bestimmen. Das ist plausibel, denn beide Funktionseinheiten brauchen
den Namen:
• heraussuchen sucht den Eintrag zu einem Namen aus der Gäste-
liste heraus.
⁹⁶Ganz selten gibt es mal eine Gelegenheit von diesem Gebot abzuweichen. Das ist
vor allem der Fall, wenn deine Funktionseinheiten nicht einzelne Verantwortlichkeiten
darstellen, sondern Bündel. Wenn du vorsichtig bist, kann eine Schleife hier und da etwas
vereinfachen.Einstweilenwürdeichjedochsagen:Don’ttrythisathome!


---


<!-- Page 161 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 152
• Begrüßung bestimmen baut aus dem Namen und der Zahl der
Besuche des Gastes eine passende Begrüßung, z.B. "Hello my
good friend, Bob!"
AndenInputsderFunktionseinheitengibtesnichtsauszusetzen.Aberwas
ist mit den Outputs? Muss heraussuchen den Namen in seine Ausgabe
einschließen? Im Beispiel fließt der name sowohl in heraussuchen
hinein wie heraus. Im zweiten Bild, wo die Funktionseinheiten für sich
stehen und mit den blauen Linien verbunden sind, ist das ganz deutlich
zu sehen.
Im Sinne einer Vollständigkeit kann man sicher sagen, dass der Zugriff
auf die Gästeliste einen ganzen Datensatz liefern sollte, der aus Name
und Besuchsanzahl besteht. Die Bezeichnung heraussuchen für die
Funktionseinheit legt das nahe.
Doch dass es die gibt und keine andere, ist ja eine Entscheidung, die auch
anders ausfallen könnte. Wenn im aktuellen Modell heraussuchen auf
die persistente Gästeliste zugreift, in der Namen und Besuchsanzahlen als
Tupel stehen und womöglich sogar nach dem Namen indiziert sind, dann
suggeriert das Datenmodell eine solche Funktionseinheit.
Wenn der Lösungsansatz jedoch darin bestünde, die Namen in einem
Event Store zu speichern, dann würden die Prozessschritte anders ausse-
hen. Aus dem Zugriff auf die Datenbank würden keine Tupel kommen,
sondern vielleicht nur die Einträge, die zum Namen passen.
Wie kann jetzt die Eingabeanforderung von Begrüßung bestimmen
erfüllt werden? zählen hat den Namen nicht direkt als Input, könnte ihn


---


<!-- Page 162 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 153
allerdingsausderListebestimmen(fallsdienichtleerist);einverlässlicher
Output des Namens ist nicht möglich. Aber sollte zählen überhaupt
einen Namen liefern, passt das zur Verantwortlichkeit? Ich denke, nicht.
Jede Verantwortlichkeit soll fokussiert sein und nach PoMO nicht an eine
mögliche Umgebung denken. Eine Funktionseinheit ist zunächst immer
für sich als 0-dimensionales Element im Flow-Design. Eingabe, Ausgabe
und Zustand sollen sich nur nach ihrer Verantwortlichkeit richten, die ihr
Name knapp beschreibt.
• Besuche laden soll lediglich alle Besuche aus dem Event Store
laden. Das ist eine mehr oder weniger lange Liste. Heute stehen
in der nur Namen, morgen könnten in der aber auch noch andere
besuchsrelevante Informationen stehen, wie z.B. die Veranstaltung
oder das Besuchsdatum.
• zählen soll nur die Zahl der Einträge in einer Liste von Besuchen
bestimmen. Das ist heute trivial, kann morgen mit weiteren Infor-
mationen aber schon etwas aufwändiger sein.
Begrüßung bestimmen ist am Ergebnis von zählen interessiert. Dar-
über hinaus braucht die Funktionseinheit allerdings den Namen. Wie
kommt der zu ihr? Er ist am Anfang vorhanden als Input in den Daten-
fluss bei Besuche laden. Von dort könnte er weitergeleitet werden an
die downstream stehende Funktionseinheit Begrüßung bestimmen. Im
folgenden Bild geschieht das mit einem Split und einem Join:


---


<!-- Page 163 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 154
Der Split zweigt einen “Nebenfluss” mit einer Untermenge der anliegen-
den Daten ab als Input für eine spätere Funktionseinheit - und das Join
führt mehrere Datenflüsse zusammen. Ich denke, das verstehst du intuitiv
und ist dir auch schon in anderen Notationen begegnet.⁹⁷
name an zählen in dieser Weise vorbei zu leiten, ist möglich. Manchmal
machen Split und insbesondere Join guten Sinn in einem Datenfluss
- doch für den hiesigen Fall ist das zu kompliziert. Die grundsätzliche
Einfachheit des Prozesses wird dadurch verrauscht. So viele Linien sind
für den kleinen Zweck unangemessen.
Einerseits lege ich dir die Analogie mit den elektronischen Leiterplatten
nahe. Die passt auch zu dem Bild mitSplit und Join. Andererseits hat jede
Analogie ihre Grenzen. Eine solche ist hier erreicht. Deshalb will ich auf
eine andere wechseln: den Block in Programmiersprachen.
Jeder Datenfluss ist ein Block. Er bildet damit einen Scope in dem “Dinge”
⁹⁷Auf semantische Feinheiten beim Join möchte ich an dieser Stelle verzichten. Genau
genommen stellt sich die Frage, wann diese Standard-Funktionseinheit “feuert”: bei jeder
Veränderung eines Input-Wertes oder nur wenn sich beide verändert haben? In manchen
DatenflüssenistsolcheUnterscheidunginteressant,meistensjedochnicht.Deshalbwillich
dichhiernichtmitNotationsideenbeschweren,mitdenendasausgedrücktwerdenkönnte.


---


<!-- Page 164 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 155
- hier: fließende Daten - einfach bekannt und überall sichtbar/verwendbar
sind. In dieser Weise verstanden, kann das Modell viel einfacher aussehen:
LinkskommtdernameindenScopedesDatenflusses.Erwirdbenutztvon
Besuche laden, steht aber weiterhin zur Verfügung im Scope. Deshalb
kann er später ein weiteres Mal als Eingabe für Begrüßung bestimmen
benutzt werden.
Aus zählen fließt nur n als Anzahl der Besuche heraus. Um aus diesem
Output on the fly oder besser in the flow einen anderen Input zu machen,
habe ich einfach dahinter ein Pipe-Symbol (|) gesetzt. Das trennt die
Ausgabedaten von den weiterfließenden Eingabedaten.
Hier die Syntax zuerst etwas ausführlicher mit zwei Pfeilen für eine
Verbindung zwischen Funktionseinheiten und dann vereinfacht.


---


<!-- Page 165 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 156
Manchmal benutze ich die erste Syntax, weil sie mir etwas besser erlaubt,
beim zeichnen zu denken. Ich kann mit dem Output einer Funktionsein-
heit abschließen - und dann mit einem neuen Pfeil daran den Input für die
nächste Funktionseinheit anschließen.
Merke:Alles,wasineinenDatenflusshineinfließtoderdarinerzeugtwird,
ist ab dem Punkt downstream verfügbar. Allerdings solltest du deshalb
nicht die Namen für die Daten - z.B. a, b, c, d als Variablen ansehen.
Es sind schlicht benannte Daten. In Datenflüssen gibt es keine mutable
data. Es gibt einfach nur Daten, die fließen und “zufällig” einen Namen
haben, um im Fluss etwas zu bedeuten. Im Messaging gibt es ebenfalls
kein Konzept von mutability für das, was fließt. Allerdings könnten
Objekte Zustand haben; als Abhängigkeit ist der ja aber gekapselt und
ein Implementationsdetail. Auf die “Verdrahtung” der Funktionseinheiten
hat er keinen Einfluss.
Wenn die Bedeutug offensichtlich ist z.B. aufgrund des Namens einer
Funktionseinheit,könnendiefließendenDatenauchlediglichdurchihren
Typ repräsentiert werden:


---


<!-- Page 166 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 157
Fließende Mengen
Zwischen den Funktionseinheiten fließen “Datenblöcke”. Wie die struktu-
riert sind, ist im Grunde nicht wichtig für die Funktionsweise des Flusses.
Wenn du ihnen einen “sprechenden Namen” gibst, ist dir klar, worum es
sich handelt.
Manchmal ist es dann aber doch interessant, die Struktur der fließenden
Daten offenzulegen. Das kann aus Bequemlichkeit sein, weil du für die
Zusammenfassung von Daten keinen guten Namen findest. In Addieren
fließen zwei ganze Zahlen hinein; weiter oben habe ich sie a und b
genannt. Die sind als Tupel auf dem Fluss-Pfeil notiert, entweder mit
Namen oder mit Datentypen. Aber wie könnte die Bezeichnung für beide
zusammen lauten? “Summanden” wäre korrekt, aber auch etwas gestelzt.
Deshalb finde ich das Tupel bequemer. Sollten dessen Elementanzahl
jedoch wachsen, dann würde ich mir mehr Mühe mit der Namensfindung
geben.
Ein Beispiel anderer Art sind die besuche oben. Die Bezeichnung ist ein
Plural, es handelt sich also um eine Menge. Aber eine Menge von was?
Hier wäre vielleicht interessant, den Typ zu erfahren. Außerdem wäre es
vielleicht leichter ersichtlich, dass es sich um eine Menge handelt, wenn
das mit der Notation ausgedrückt werden könnte. Beides ist möglich:


---


<!-- Page 167 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 158


---


<!-- Page 168 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 159
Mit einem Sternchen * innerhalb der Klammer für die fließenden Daten
direktaneinemDatumkannstduausdrücken,dassessichumeineMenge
handelt. Statt eines Plurals benutzt du dann natürlich den Singular: aus
besuche wird besuch*.⁹⁸ Das Sternchen steht für 0 oder mehrmalige
WiederholungeinesDatenelementeswiebeiRegulärenAusdrücken⁹⁹.Wo
string* steht, können also 0 oder ganz viele Zeichenketten herausflie-
ßen. Beachte: Auch die leere Menge ist immer noch eine Menge.
Wie du fließende Mengen beschreibst, ist dir überlassen. Mache es mit
dem Plural oder mit dem Sternchen oder einem konkreten Datentypen.
Das Sternchen hat jedoch mehrere Vorteile:
• Es macht die Menge im Datenfluss sehr deutlich erkennbar.
• Esistabstrakt.DumusstdichfürdasModellnochnichtentscheiden,
ob sich um ein Feld, eine Liste oder einen Iterator handelt. Das
Wichtigste ist: es gibt nicht nur ein Ausgabe-Element, sondern eine
beliebig große Menge. Darauf muss die folgende Funktionseinheit
eingestellt sein.
Du wirst merken, dass im Sternchen viel Kraft liegt. Es ist das Mittel, um
in Datenflüssen ohne Schleifen auszukommen. Datenflüsse sind Mengen-
verarbeitungsprozesse. Es fließen nicht Einzelstücke hindurch, sondern
ganzoftMengen.AufdieseWeisewerdendeinebisherigengeschachtelten
Schleifen “linearisiert”.
Implementation
Die Implementation von 1-dimensionalen Datenflüssen ist trivial. Wenn
0-dimensionale Datenflüsse, also einzelne Funktionseinheiten zu Funktio-
nen werden, dann werden 1-dimensionale Datenflüsse zu Sequenzen von
Funktionsaufrufen.
Die Übersetzung dieses Datenflusses
⁹⁸Alternativ kannst du auch den vollständigen Typ hinschreiben, wie du ihn in dei-
ner Programmiersprache angeben würdest, z.B. string[] oder IEnumerable<string>.
DochdaswürdeichnurinAusnahmefällentun.
⁹⁹https://en.wikipedia.org/wiki/Regular_expression


---


<!-- Page 169 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 160
besteht mithin aus zwei Teilen. Da sind zuerst die Funktionseinheiten für
sich genommen:
1 string[] BesucheLaden(string name) {...}
2
3 int Zählen(string[] besuche) {...}
4
5 string BegrüßungBestimmen(string name, int n) {...}
6
7 void Begrüßen(string begrüßung) {...}
Und dann der übersetzte Fluss, die “Reihenschaltung” der Funktionsein-
heiten:
1 var besuche = BesucheLaden(name); // woher der Name kommt, sei dahingestellt
2 var n = Zählen(besuche);
3 var begrüßung = BegrüßungBestimmen(name, n);
4 Begrüßen(begrüßung);
Das war’s. Fertig ist die Transformation des Flow-Design Modells in eine
Hochsprache.
Diese Form kommt dir aus Kapitel 3 sicher bekannt vor: es handelt sich
um eine Integration. Was auch sonst? Integrationen stecken Objekte zu


---


<!-- Page 170 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 161
Messaging-Netzwerken zusammen.¹⁰⁰
Bitte beachte hier:
• Die“Wiederverwendung”vonnameimScopedesDatenflusseswar
ganz einfach.
• DasSternchenfürdieMengewurdealsFeldinterpretiert.Solltesich
das irgendwann als Nachteil für die Implementation herausstellen,
kann die geändert werden, ohne dass dadurch das Modell “falsch”
würde.
• Die Namenskonventionen in deiner Programmiersprache geben dir
sicherlich vor, wie Funktionen und Variablen zu benennen sind. In
C# werden Funktionen/Methoden z.B. groß geschrieben. Im Modell
hingegen bist du frei(er).
Nun habe ich oben die Natur der Datenflüsse betont, die da ist, dass
die Kontrolle überall zugleich ist. Diese Eigenschaft geht bei dieser Über-
setzung in eine Sequenz von Funktionsaufrufen verloren. Jetzt ist die
Kommunikation zwischen den Funktionseinheiten synchron: mit jedem
Output wandert die Kontrolle zur nächsten Funktion(seinheit), die ihn als
Input verarbeitet. Das Modell ist in dieser Hinsicht offener, unbestimmter.
Nach meiner Erfahrung stört diese Reduktion jedoch nicht. Die im Da-
tenfluss inhärente Parallelität ist als Potenzial wunderbar - in der Praxis
allerdings nur selten nötig. Deshalb kannst du in der Praxis als default
die Übersetzung eines 1-dimensionalen Datenflusses in eine Sequenz von
Funktionsaufrufen annehmen. Das passt schon.
Und wenn es nicht passt, dann übersetzt du eben anders. Am Modell
ändert das oft nur vergleichsweise wenig. Mit Datenflüssen wirst du
in dieser Hinsicht nicht bevormundet. Sie bieten dir gleich mehr, als
du eigentlich brauchst. Das ist gut. Meistens lehnst du das Angebot ab.
Manchmal nimmst du es an - und sorgst dann selbst da, wo es nötig ist,
für Synchronisation. Ansonsten ist die Synchronisation implizit.
¹⁰⁰Warum ich die Nutzung von temporären Variablen vorziehe, statt geschachtelter
Aufrufe, habe ich dir schon im vorherigen Kapitel gesagt. Ab jetzt ist die Übersetzung, wie
du sie hier siehst, deshalb “kanonisch”. Ich kann dir nur empfehlen, nicht an temporären
Variablen oder Codetextzeilen sparen zu wollen. Die Verständlichkeit ist besser so wie
hier gezeigt. Es gibt für mich dazu nur zwei Ausnahmen: die eine betrifft Zugriffe auf
Datenstrukturen und die andere die Nutzung vonfluent interfacesbzw. “Fluss-Operatoren”
wie|>oder>>inF#oderanderenSprachen.DafürfolgenhierunddaBeispieleimweiteren
Text.


---


<!-- Page 171 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 162
Übungsaufgaben
Reflexionsaufgabe
Bitte formuliere eine Frage oder eine Erkenntnis zum Kapiteltext.
• Wo bist du gedanklich hängengeblieben, was ist dir unklar,
was passt für dich irgendwie nicht zusammen, wozu würdest
du dir noch etwas mehr Erklärung wünschen? Steht irgendet-
waszudeinerbisherigenPraxisimWiderspruchunddufragst
dich, warum du etwas ändern solltest?
• Oder: Wann hast du einen Aha-Moment gehabt, was ist
diralsbemerkenswert,spannend,ausprobierenswertaufgefal-
len? Hat irgendetwas “in dir Klick gemacht”, weil dir nun ein
Zusammenhang aufgegangen ist? Oder verstehst du jetzt aus
deiner bisherigen Praxis irgendetwas besser?
Am besten formulierst du Frage bzw. Erkenntnis schriftlich. Indem
du deine Gedanken aufschreibst, wirst du dir ihrer bewusster. Bei
einer Frage kommst du dadurch vielleicht schon einer Antwort aus
dir selbst heraus näher. Bei einer Erkenntnis fällt dir vielleicht schon
etwas ein, das du ab jetzt anders machen kannst.
Aufgabe 1 - Modellieren und implemen-
tieren
1. Modelliere mit Flow-Design (d)einen Lösungsansatz für das
Hello-World-Problem in der Iteration 3 wie in Kapitel 1 be-
schrieben.Achtung:JeProgrammaufrufwirdnurnacheinem
Namen gefragt! Das Programm endet, wenn für den Namen
die Begrüßung angezeigt wurde. Beispiel:
1 $ hello-world.exe
2 Name: Bob
3 Welcome back, Bob!
4 $


---


<!-- Page 172 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 163
2. Übersetze dein Modell in Code der Hochsprache deiner Wahl.
DasResultatsolllauffähigsein,umdasModellzuverifizieren.
Aufgabe 2 - Reverse modeling
Leite aus dem Code der Musterlösung von Kapitel 3 zum Problem
der Bedingten Wahrscheinlichkeiten bei den Testergebnissen einen
1-dimensionalen Datenfluss ab, der alle Aufrufe von Funktionen
enthält, die der Code selbst definiert.
Aufgabe 3 - Lösen, modellieren, imple-
mentieren
Szenario
Entwickle ein Programm, das den Text in simplen Textdateien um-
formatiert,sodassdieLängenderTextzeileneingewissesMaximum
nicht überschreiten.
Beispielaufruf des Programms:
1 $ umbruch märchen.txt 25 > märchen-umgebrochen.txt
2 $
Das Programm verarbeitet den Text in der Datei, die im ersten
Parameter angegeben ist. Der zweite Parameter gibt die maximale
Länge der Zeilen des umformatierten Textes vor. Der umformatierte
Text wird auf der Console ausgeben und im Beispiel mit > in die
Datei märchen-umgebrochen.txt umgeleitet; nur deshalb ist er
nicht zu sehen.
Dateiinhalt von märchen.txt:


---


<!-- Page 173 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 164
1 Vor einem großen Walde wohnte ein armer Holzhacker mit seiner
2 Frau und seinen
3 zwei
4 Kindern; das Bübchen hieß
5
6 Hänsel und das Mädchen
7 Gretel.
Erwarteter Dateiinhalt von märchen-umgebrochen.txt:
1 Vor einem großen Walde
2 wohnte ein armer
3 Holzhacker mit seiner
4 Frau und seinen zwei
5 Kindern; das Bübchen hieß
6 Hänsel und das Mädchen
7 Gretel.
Beachte:
• Whitespace der Quelle wird nicht erhalten im Umbruch.
• Satzzeichen an einem Wort gehören zum Wort.
Sollte ein Wort allein länger als die maximale Zeilenlänge sein, wird
es einfach abgeschnitten und in Teilen umgebrochen. Beispiel:
Dateiinhalt text-mit-langem-wort.txt:
1 Er trug seine Dampfschifffahrtskapitänsmütze mit Stolz.
Der Umbruch mit einer maximalen Zeilenlänge von 9 Zeichen soll
zu diesem Ergebnis führen:
1 Er trug
2 seine
3 Dampfschi
4 fffahrtsk
5 apitänsmü
6 tze mit
7 Stolz.
TODO
1. FindeeinenLösungsansatz.FormulieredenmitwenigenWor-
ten und/oder informell visuell.
2. Modelliere deine Lösung mit einem 1-dimensionalen Daten-
fluss.
3. Übersetze dein Modell in eine Hochsprache und bringe das
Programm zum Laufen.


---


<!-- Page 174 of 584 -->


04-Flow-Designmit1-dimensionalenDatenflüssen 165
Mach dir keinen Kopf um technische Details wie Text-Encoding
oder Fehlerfälle wie nichtvorhandene Datei oder negative maximale
Zeilenlänge. Es geht nicht darum, dass das Programm in einem
App Store verkauft wird und supportarm bei Millionen Nutzern
läuft. Du sollst eine Gewohnheit für die Schritte Lösen, Modellieren,
Übersetzen bekommen.


---


<!-- Page 175 of 584 -->


05 - Flow-Design mit
2-dimensionalen
Datenflüssen
EineFunktionseinheitabstrahiertdavon,konkretwieeineVerantwortlich-
keiterfüllt wird. Weder ist die Logikzu sehen im Modell, noch ist klar,mit
welchem technischen Mechanismus das Verhalten angestoßen wird. Nur
das Paradigma ist klar: Daten rein, Daten raus, d.h. Daten durchfließen
eine Funktionseinheit wie Wasser einen Durchlauferhitzer.
Eine “Reihenschaltung” von Funktionseinheiten, also ein mehrschrittiger
Datenfluss abstrahiert davon, wie Funktionseinheiten miteinander ver-
bunden sind, um im Verein eine Aufgabe bewältigen. Nur das Paradigma
ist klar: Daten fließen downstream von Funktionseinheit zu Funktionsein-
heit wie Wasser über Stromschnellen eines Bergflusses.
Mit Flow-Design möchte ich also dein Denken aus den Niederungen der
Implementationsdetails auf die Kuppe eines Hügels bringen, von wo aus
du über den Nebel blicken kannst.¹⁰¹
¹⁰¹FotovonRicardoGomezAngelbeiUnsplash


---


<!-- Page 176 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 167
Ultimativ kommst du nur von Kuppe zu Kuppe in solch einer Landschaft,
wenn du dich in den Nebel hinunter begibst. Irgendwann musst du dich
den Details stellen. Doch für einen Überblick, das big picture, die grobe
Planung eines Weges von hier nach dort ist es eine gute Sache, sich nicht
mit Kleinigkeiten zu belasten.
Dieser Gedanke steckt letztlich auch hinter der Erfolgsgeschichte der
Hochsprachen. Zuerst waren Röhren und Relais, die von Hand verdrahtet
werden mussten, um einen Computer auf ein bestimmtes Verhalten ein-
zustellen. Der Computer physisch verändert; es wurde quasi ein anderer
daraus, um andere Anforderungen zu erfüllen.
Dann kamen Programme in Form von Maschinencode, die der Computer
in immer gleicher physischer Konfiguration abarbeiten konnte. Selbst
wenn die auf Lochkarten präsentiert werden mussten, war das schon eine
Abstraktion von den Hardwaredetails.
Und dann kamen Programme in Hochsprachen. Die Programmierung
erfolgt zuerst immer noch über Lochkarten, doch die Notation änderte
sich drastisch: statt mit Zahlen (Maschinencode) und “stichwortartigem”
Text (Assembler) konnten Anweisungen nun in immer besser lesbarem
Text gegeben werden: Fortran, Cobol, Lisp, Algol, C, Basic, Pascal… Nicht
nur die Hardware war unsichtbar, auch ihre feingranularen Befehle.
Allerdings:DiegrundlegendeVerarbeitungsarchitekturschienimmernoch
durch. Programme beschrieben und beschreiben die Verhaltensherstel-
lung mit Kontrollflüssen auf einem stackbasiertem Prozessor. Von den
FeinheitenderRegisterallokationwirdzwarabstrahiert-manchmalsogar
über zwei Ebenen hinweg: in der Hochsprache und in der darunter liegen-
den Zwischensprache, die womöglich erst zur Laufzeit in Maschinencode
übersetzt wird -, doch Befehl folgt immer noch auf Befehl wie zu Zeiten
der Maschinencode-Programmierung. Kontrollstrukturen der Strukturier-
ten Programmierung haben mit dem Spaghetticode ungezügelter Sprünge
mittels goto aufgeräumt, doch tiefe Schachtelungen und lange Sequenzen
von Kontrollstrukturen sind trotzdem noch schwer verständlich und feh-
lerträchtig.
Dass das so ist in den Niederungen der Programmierung, lässt sich so
schnellnichtändern,denkeich.WennwirdieFlexibilitätbehaltenwollen,
die uns Logik bietet, dann müssen wir mit diesen Zuständen leben.
Was wir allerdings tun können ist, diese Zustände zu begrenzen. Das


---


<!-- Page 177 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 168
ist der Antrieb hinter Flow-Design. Die Komplexität, die mit Logik auf
der Basis einer Stackmaschine inklusive Allokation von globalen Daten
auf einem Heap entsteht, muss auf überschaubare Einheiten begrenzt
werden. Garbage Collection war in dieser Hinsicht ein Schritt voran
wie die Strukturierte Programmierung; freiwillige Selbstbeschränkung in
dem, was Entwickler noch selbst entscheiden sollen, hat geholfen, die
Codekomplexität deutlich zu reduzieren. Doch auch jetzt noch passiert zu
viel in einzelnen Methoden. Es gibt kein Halten bei der Anreicherung von
MethodenmitLogik.Wozuerst20Zeilensind,kommenschnell30weitere
hinzu, dann 50, dann 150 - und am Ende sind es 1378 Zeilen Logik in einer
Methode plus eine Menge Aufrufe von anderen Funktionen dazwischen
(aka Funktionale Abhängigkeiten).
Das ist ein Übelstand, dem die weitergehende Freiwillige Selbstkontrolle
des Flow-Design mit IOSP entgegenwirken will. Das geschieht durch Än-
derung des Paradigmas. Im Flow-Design Modell ist keine Stackmaschine
mehr zu sehen. Im Flow-Design Modell geht es auch nicht mehr um
Kontrollfluss. Stattdessen fließen Daten zwischen kontinuierlich “arbei-
tenden” oder “wartenden” Funktionseinheiten, die darauf in verantwor-
tungsvoller Weise reagieren.
Im Datenfluss gibt es keine globalen Daten, allemal keine impliziten.
Funktionseinheiten greifen nicht einfach hierhin und dorthin, um sich
Daten zu beschaffen oder zu speichern. Ihre Arbeit findet (vor allem) auf
den Daten statt, die in die hineinfließen. Und sollte das nicht genug sein,
dann können explizit Daten als Ressourcen dazugestellt werden. Die sind
im Modell deutlich zu erkennen und (potenziell) gleichzeitige Zugriffe
lassen sich frühzeitig entschärfen.
Modellierung mit Datenflüssen ist insofern für mich sozusagen next level
programming. Die Funktionale Programmierung will das gleich konkret
machen mit Code; Flow-Design begnügt sich hingegen zunächst mit Kon-
zeptionellem - das dann von dir in Hochsprachencode für Kontrollfluss-
Stackmachine mit Heap übersetzt wird.¹⁰²
¹⁰²Solltest du deshalb vielleicht besser gleich auf eine Funktionale Programmiersprache
wechseln? Tu das gern - aber für die meisten Entwickler einer OO-Sprache ist das unrea-
listisch. Manche kriegen die Kurve von Java nach Kotlin, wenige schwenken von C# nach
F#. Clojure, Scala, Haskell sind alle wunderbar auf ihre Art - doch der Umstieg in größeren
Projektenistsehrschwer.Deshalbistesmirwichtig,direinEntwurfswerkzeugandieHand
zu geben, dass dich im Denken auf ein höheres Level hebt und dessen Modelle du dann
in mainstream OO-Hochsprachencode übersetzen kannst. Mit manchen Sprachen geht das
natürlichbesser,mitanderenschlechter.ZumindestistaberdeinDenkenbefreit.


---


<!-- Page 178 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 169
Abstraktion durch Komposition
Die Abstraktion der Datenflüsse nenne ich Komposition. Komposition ist
gekennzeichnet dadurch, dass Verschiedenes zu etwas Neuem zusammen-
gesetzt wird.
Hier ein Beispiel aus der Musterlösung zum Textumbruch-Problem:
1 private static void Ausgeben(IEnumerable<string> zeilen) {
2 foreach(var z in zeilen)
3 Console.WriteLine(z);
4 }
Die Operation Ausgeben() “komponiert” aus einer foreach-Schleife
und dem API-Aufruf Console.WriteLine() ein Ganzes, das es vorher
nicht gab. Dieses Ganze tut etwas Neues, das viel spezifischer ist, als das,
was die darin zusammengefassten Logik-Bausteine tun.
DerZweckvonKompositionistdieHerstellungvonBequemlichkeit.Kom-
positionenfassenDetailszusammen,umdiedudichnichtmehrkümmern
musst,wenndueinZielerreichenwillst.DubenutztdieKompositionstatt
der einzelnen Bausteine und bist damit produktiver.
Dasselbe gilt für Integrationen. Sie “komponieren” zwar nichts Neues aus
Logik, sondern aus anderen Funktionseinheiten, doch das Ergebnis ist
dasselbe: eine Funktionseinheit die spezieller ist und einfacher zu nutzen.
1 static void Main(string[] args) {
2 var (dateiname, maxZeilenlänge) = Analysieren(args);
3 var text = Laden(dateiname);
4 var worte = Zerlegen(text);
5 worte = Zerschneiden(worte, maxZeilenlänge);
6 var zeilen = Zusammensetzen(worte, maxZeilenlänge);
7 Ausgeben(zeilen);
8 }
Wie schwierig wäre es gewesen, das Verhalten von Main() aus einzelnen
Logik-Bausteinen zusammenzusetzen? Wie viel leichter ist es, einige
Operationen zu nutzen!
Die Geschichte der Zivilisation ist eine Geschichte der Kompositionen,
würde ich sagen. Wenn du heute ein Auto öffnest mit der Fernbedienung
und dann darin nur noch einen Start-Knopf drückst und dann nur noch


---


<!-- Page 179 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 170
Gas und Bremse betätigst, dann ist das eine Bequemlichkeit, die durch
unzählige aufeinander aufbauende Kompositionen ermöglicht wird.
Vor 100 Jahren musste ein Autofahrer sich viel mehr mit Details seiner
Maschine auseinandersetzen als heute - und hat noch nicht einmal diesel-
be Leistung bekommen können. Dasselbe gilt in der Programmierung. So
produktiv wie du heute bist, waren Entwickler vor 50 Jahren nicht. Ihnen
fehlteesanAbstraktionen,genauer:anKompositionen.EineMethodewie
File.ReadAllLines() gab es nicht einmal vor 20 Jahren in der ersten
Version von C#, geschweige denn dass es automatische Speicherverwal-
tung des Heap in C gab. Visual Basic 1.0 mit seinem visuellen Designer
für Benutzerschnittstellen hat Millionen Entwicklern die Beschäftigung
mit den Details des Windows Grafik-API erspart.
Stratified Design
Die Geschichte der Produktivitätssteigerung unserer Branche ist für mich
eine Geschichte der Abstraktion durch Komposition. Verschiedenes, Kom-
plementäres wurde zusammengefasst, um diese Details hinter einer Fas-
sade zu bedienen. Abstraktionen von Abstraktionen über Abstraktionen:
daraus wird Produktivität gemacht.
Und nun schau in deine Projekte. Wie steht es da mit der Produktivität?
Ich kenne keines, bei dem die Produktivität mit der Zeit gestiegen ist. Wie
kommt das? Die Produktivität unserer Branche nimmt mit jedem Jahr zu
- die in den Projekten der Branche nimmt mit jedem Jahr ab. Ist das nicht
merkwürdig?
Ich denke, es gibt dafür mehrere Gründe. Einer davon ist jedoch ein Man-
gel an Abstraktion. Es fehlt das Denken in konsequenten Kompositionen.
Nicht, dass dazu nicht aufgerufen worden wäre. Abelson und Sussman
haben schon 1987 in ihrem Paper “Lisp: A Language for Stratified De-
sign”¹⁰³ beschrieben, wie Abstraktionen mittels Sprachen hergestellt wer-
den können. Alan Kay schlägt in dieselbe Kerbe in seinem 2011 Vortrag
“Programming and Scaling”¹⁰⁴: Wer die Problemlösung mit Programmier-
sprachen einfacher machen will, der sollte eine Programmiersprache auf
¹⁰³https://dspace.mit.edu/bitstream/handle/1721.1/6064/AIM-986.pdf
¹⁰⁴https://www.tele-task.de/lecture/video/2772/


---


<!-- Page 180 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 171
hohem Abstraktionsniveau anbieten. Allerdings: Je höher das Abstrakti-
onsniveau, desto spezifischer die Sprache, desto enger das Anwendungs-
gebiet.
Heutige Hochsprachen haben also im Grunde ein sehr niedriges Abstrak-
tionsniveau, auch wenn es höher ist als das von Maschinencode. Mit
Hochsprachen lassen sich alle möglichen Probleme lösen. Eine Buchhal-
tungssoftware wie ein online Spiel oder ein Compiler lassen sich in Java
oder C# oder Python programmieren.
Sollst du nun aber für mehr Produktivität in deinem Projekt eine eigene
Sprache erfinden, eine Domain Specific Language (DSL)¹⁰⁵? Ja und Nein.
Nein insofern, als dass du keine eigene Sprache mit Syntax, Semantik,
Notation und Compiler erfinden sollst. Das lohnt sich schlicht nicht für
Domänen/Anwendungen/Projekte, in denen du nur einmal tätig bist oder
solange dir die Konzepte und Zusammenhänge darin nicht klar bzw.
ständigimFlusssind.EineSprachezudefinieren,ist“schlimmer”alseinen
API zu definieren: Du musst so viele Entscheidungen für die Zukunft
treffen, dass dir ganz schwindelig wird. Das ist den Besten vorbehalten
in vergleichsweise stabilen und klaren Szenarien.
Andererseits aber auch Ja insofern, als dass du ein Vokabular erfinden
sollst, das du bei gegebener Syntax, Semantik, Notation deiner Hochspra-
che benutzen kannst. Syntaktische und semantische Abstraktionen sind
etwas für sehr, sehr spezielle Fälle; ein domänenspezifisches Vokabular,
mit dem du eine Domäne beschreibst, und das du dann auf einer höheren
EbenwiederumzusammenfasstzunochabstrakteremVokabularusw.usf.,
das ist etwas für jede Software.
Diese Art der Abstraktion ist allerdings etwas anderes als die “mit Objek-
ten”.DiemainstreamObjektorientierungwollteauchproduktivermachen.
Das ist aber knapp daneben gegangen, würde ich sagen, weil man Kom-
position nicht konsequent auf Verhalten angewendet hat.
Das ändert nun Flow-Design. Die Grundlage dafür ist das IOSP. Mit
IOSP kannst du konsequent eine Abstraktionstreppe hinaufsteigen. Du
schichtest Kompositionen auf Kompositionen auf Kompositionen wie
Gesteinsschichten¹⁰⁶ oder Schichten zivilisatorischer Überreste bei einer
¹⁰⁵https://en.wikipedia.org/wiki/Domain-specific_language
¹⁰⁶DasBildzeigtklassischeKreidestein-SchichtenaufZypern;Quelle:Wikipedia-Artikel
zuStratum.


---


<!-- Page 181 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 172
archäologischen Ausgrabungsstätte.
Merriam-Webster¹⁰⁷ definiert stratum wie folgt:
one of a series of layers, levels, or gradations in an ordered
system
Und genau das meinen Abelson/Sussman und Alan Kay: ein geordnetes
System aus Schichten, deren Abstraktionsgrad einem Gradienten folgt. Je
höher die Schicht, das Stratum, desto höher der Abstraktionsgrad.
Wie entsteht soetwas nun aber mit IOSP? Die Musterlösung zum Textum-
bruch ist ein erstes Beispiel: sie besteht aus drei Strata. Auf jedem dieser
Abstraktionsniveaus ist die Lösung vollständig.
Das höchste Stratum ist das, in dem die Problemlösung mit nur einer
“Vokabel” beschrieben wird. Etwas verkürzt sieht das so aus:
1 umbruch.Program.Main(string[] args)
¹⁰⁷https://www.merriam-webster.com/dictionary/stratum


---


<!-- Page 182 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 173
Es reicht der Aufruf einer Funktion, um einen Text umzubrechen. Das ist
bequem, oder? Ein Benutzer muss dafür den Lösungsansatz nicht kennen.
Das darunter liegende Stratum besteht aus “Vokabular”, das vielfältigerist
und deshalb noch zu einem Ganzen komponiert werden muss.
1 var (dateiname, maxZeilenlänge) = Analysieren(args);
2 var text = Laden(dateiname);
3 var worte = Zerlegen(text);
4 worte = Zerschneiden(worte, maxZeilenlänge);
5 var zeilen = Zusammensetzen(worte, maxZeilenlänge);
6 Ausgeben(zeilen);
Während umbruch.Program.Main() hochgradig spezifisch ist, sind
Zerlegen() oder Zusammensetzen() schon weniger spezifisch.
Und schließlich das niedrigste, tiefste Stratum: die reine Logik. Diese
Komposition aus sehr unspezifischen “Vokabeln” leistet dasselbe, wie die
darüber liegenden. Der Vorteil: alle Details liegen vor dir. Der Nachteil:
alle Details liegen vor dir.
1 var dateiname = args[0];
2 var maxZeilenlänge = int.Parse(args[1]);
3 var text = File.ReadAllText(dateiname);
4 var worte = text.Split(new[] {' ', '\t', '\n', '\r'},
5 StringSplitOptions.RemoveEmptyEntries);
6 worte = worte.SelectMany(wort => {
7 var wortteile = new List<string>();
8 while (wort.Length > maxZeilenlänge) {
9 wortteile.Add(wort.Substring(0, maxZeilenlänge));
10 wort = wort.Substring(maxZeilenlänge, wort.Length - maxZeilenlänge);
11 }
12 if (wort.Length > 0) wortteile.Add(wort);
13 return wortteile;
14 }).ToArray();
15 var verbleibendeWorte = new List<string>(worte);
16 var zeilen = new List<string>();
17 while (verbleibendeWorte.Count() > 0) {
18 var zeile = "";
19 while (verbleibendeWorte.Count() > 0) {
20 var tempZeile = zeile + (zeile.Length > 0 ? " " : "")
21 + verbleibendeWorte[0];
22 if (tempZeile.Length > maxZeilenlänge)
23 break;
24 zeile = tempZeile;
25 verbleibendeWorte.RemoveAt(0);
26 }
27 zeilen.Add(zeile);
28 }
29 foreach(var z in zeilen)
30 Console.WriteLine(z);
So wichtig Details sind für die korrekte Ausführung, sie stehen dir beim
Verständnis schnell im Wege. Würdest du lediglich mit einem Programm


---


<!-- Page 183 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 174
auf diesem Abstraktionsniveau konfrontiert, dann wärest du sehr, sehr
unproduktiv.
Um deine Produktivität zu steigern, ist es also vorteilhaft, konsequent
saubere Abstraktionen einzuziehen. Bei gegebener, notwendiger Logik
lautet die Frage also: Wie können diese sehr allgemeinen “Vokabeln” zu-
sammengefasst werden zu spezifischeren? Denn spezifischere “Vokabeln”
sind aussagekräftiger, sprechender - und das ist ein Vorteil fürs Verständis
wie für den Aufbau noch höherer Strata.
Oder eben umgekehrt beim Entwurf: Während des Entwurfs kennst du
noch keine Logik. Du arbeitest dich von oben nach unten durch die Strata.
Während sie in der Natur und in der Zivilisation von unten nach oben
wachsen, entwirfst du sie (meistens) von oben nach unten. Du fragst dich
angesichts eines Problems bzw. eines Aspekts deines Lösungsansatzes:
“Welche Vokabeln könnten mir helfen, möglichst knapp auszudrücken,
was ich hier erreichen will?”
Beim Textumbruch stand anfänglich im Raum das Gesamtproblem. Für
seineLösunggabesschoneineForm:umbruch.Program.Main(string[]
args). Die war impliziert. Das war die gegebene DSL auf höchstem
Niveau. Also stellte sich die Frage: Wie lautet die DSL auf einem etwas
niedrigeren Abstraktionsniveau? Mit welchen “Verben” kann das Verhal-
ten, das von Main() erwartet wird, ausgedrückt werden? Verben, die im
Rahmen von Syntax und Semantik der Hochsprache C# benutzt werden
können; das sind Funktionen.
Und so weiter und so fort.
2-dimensionale Datenflüsse
Eine Funktionseinheit habe ich als 0-dimensional bezeichnet. Eine “Rei-
henschaltung”vonFunktionseinheitenstelleneinen1-dimensionalenFluss


---


<!-- Page 184 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 175
dar. Wenn ich nun die Komposition aber verallgemeinere, dann entstehen
2-dimensionale Datenflüsse: sie haben eine Breite in Flussrichtung und
eine Tiefe orthogonal dazu in Richtung der Integrationshierarchie.
Integrationen “komponieren” also nicht nur aus Operationen etwas Grö-
ßeres, sondern auch aus anderen Integrationen. Einer Integration ist es
einerlei,welcherArtdieFunktionseinheitensind,diesieintegrieren.Einer
Funktionseinheit ist von außen nicht anzusehen, ob sie eine Operation
oder Integration ist; aus das gehört zur Kapselung von Details.
An der Spitze eines 2-dimensionalen Datenflusses steht immer eine In-
tegration. Sie repräsentiert die Gesamtleistung, die durch eine Daten-
flusshierarchie erbracht werden soll. Sie ist verantwortlich für einen
Ausschnitt aus den Anforderungen, für den ein Akzeptanztest existieren
soll.¹⁰⁸
Die geschweifte Klammer im vorherigen Bild ist nur ein Symbol, um
die Integration auszudrücken. Sie zeigt an, dass die darüber liegende
Funktionseinheit die darunter liegend geklammerten “verdrahtet”, wie es
die Pfeile zwischen ihnen anzeigen. Wenn du willst, kannst du das auch
aufandereWeiseanzeigen.IchpersönlichziehedenBogenmiteinerLinie
darüber vor, weil der sich leicht zeichnen lässt und damit Datenflüsse
auch über größere Entfernungen auf einem Blatt an ihre Integration
¹⁰⁸Erinnere dich an Kapitel 1. Dort habe ich den Input für den Entwurf als eine Liste
von Funktionen beschrieben. So weit soll die Anforderungsanalyse gehen, dass du einzelne
Funktionssignaturen erkennst, die Interaktionswünsche des Benutzers befriedigen. Jede
Funktion steht für eine Nachricht, die von außen auf das Softwaresystem trifft, verarbeitet
werdenmussundeineNachrichtalsAntwortgeneriert.MehrdazuineinemspäterenKapitel.


---


<!-- Page 185 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 176
angeschlossen werden können. Ein Dreieck hingegen ist manchmal die
einfachste Form, wenn du nicht mit der Hand, sondern einem Tool wie
Powerpoint malst, weil du das Modell ordentlicher haben willst.
In den bisherigen Beispielen hat es ganz natürlich immer nur eine solche
Wurzel gegeben. Die wurde durch die Funktion Main() implementiert,
die sofort Operationen integriert hat. Wie du aus Anforderungen auf die
vielenWurzelnfürdieDatenflüssekommst,dieeineSoftwareausmachen,
ist eine Sache der Anforderungsanalyse; mein Ansatz dafür ist Slicing.
Damit will ich die in diesem Band jedoch nicht belasten. Die Wurzeln für
die Entwurfsszenarien hier gebe ich vor oder sie liegen wirklich auf der
Hand. Du kannst aber schonmal anfangen, dir Software als Versammlung
von Datenflusshierarchien vorzustellen, die unabhängig nebeneinander
“hängen” wie Kleiderbügel im Schrank.¹⁰⁹
¹⁰⁹Am Ende sind die Hierarchien natürlich nicht unabhängig voneinander. Sie teilen
sichFunktionseinheiten,dieFunktionseinheitenteilensichZustand.UndFunktionseinheiten
gehören zu denselben Modulen. Das ändert für mich jedoch am grundlegenden Bild nichts:
Die Interaktion mit Benutzern findet in Datenfluss-Prozessen statt. Das ist eine Sichtweise,
zu der auch Unternehmen heute immer mehr übergehen; nichts anderes bedeutet letztlich
Kundenorientierung. Sie orientieren sich weg vom Abteilungsfokus, der zu Silodenken
führt, hin zu einem Prozessfokus, bei dem der Kunde am Anfang und am Ende einer
Wertschöpfungskettesteht.


---


<!-- Page 186 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 177
Am Boden einer Datenflusshierarchie finden sich ausschließlich - du
kannst es dir denken - Operationen. In einer Datenflusshierarchie ist die
Logik also konsequent nach unten gesunken.
Es gibt keine Beschränkung der Tiefe oder Länge eines 2-dimensionalen
Datenflusses. Eine Integration aber aus mehr als 5-7 Funktionseinheiten
zu “komponieren”, ist eher ungewöhnlich. 3-5 Funktionseinheiten sind
optimal, weil du die gut überblicken kannst. Ob und wie sie zusam-
men plausibel die Integration ausmachen, braucht dann keine großartige
Analyse. Wenn also mal ein 1-dimensionaler Datenfluss unter seiner
Integration zu sehr wachsen sollte, überlegst du dir einfach, wie du
darineinigeFunktionseinheitenzusammenfassenkannst,umsiemiteiner
weiteren Integration “tiefer zu legen”.


---


<!-- Page 187 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 178
Datenflüsse wachsen also ganz natürlich zunächst in der Länge und dann
in der Tiefe. Manchmal passiert aber auch das Gegenteil: dann ersetzt du
eine Integration durch die bisher integrierten Funktionseinheiten.
Die Refaktorisierungen extract und inline gibt es also auch im Flow-
Design. Strukturen wollen halt “atmen”: sie wollen sich differenzieren/-
entfalten/auseinandergehen-unddannwollensiesichwiederzusammen-
ziehen.
Dank des IOSP ist das ganz einfach. Integrationen lassen sich wunderbar
refaktorisieren, weil sie eben keine “verquarzte” Logik enthalten und
schleifenfrei sind.
Aus Operationen werden Integrationen
Anders ist das bei Operationen. Die zu refaktorisieren, kann schon ein
Problem sein. Mit dem IOSP bekommst du dafür jedoch einen glasklaren
Maßstab. Ich nenne das refactor to IOSP. Mehr dazu findest du in meinem
Band Test-first Codierung. Hier nur so viel dazu:
Wenn du aus einer Operation etwas Logik auslagern willst, weil sie dir zu
komplexwird,dannmusstdunachIOSPdiekompletteLogik“tieferlegen”.
Aus der Operation muss eine Integration werden! Hier ein Beispiel:
Am Anfang mag eine Lösung für das Textumbruch-Problem aus einer
Operation bestehen:


---


<!-- Page 188 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 179
1 public static void Main(string[] args) {
2 var dateiname = args[0];
3 var maxZeilenlänge = int.Parse(args[1]);
4 var text = File.ReadAllText(dateiname);
5 var worte = text.Split(new[] {' ', '\t', '\n', '\r'},
6 StringSplitOptions.RemoveEmptyEntries);
7 worte = worte.SelectMany(wort => {
8 var wortteile = new List<string>();
9 while (wort.Length > maxZeilenlänge) {
10 wortteile.Add(wort.Substring(0, maxZeilenlänge));
11 wort = wort.Substring(maxZeilenlänge, wort.Length - maxZeilenlänge);
12 }
13 if (wort.Length > 0) wortteile.Add(wort);
14 return wortteile;
15 }).ToArray();
16 var verbleibendeWorte = new List<string>(worte);
17 var zeilen = new List<string>();
18 while (verbleibendeWorte.Count() > 0) {
19 var zeile = "";
20 while (verbleibendeWorte.Count() > 0) {
21 var tempZeile = zeile + (zeile.Length > 0 ? " " : "")
22 + verbleibendeWorte[0];
23 if (tempZeile.Length > maxZeilenlänge)
24 break;
25 zeile = tempZeile;
26 verbleibendeWorte.RemoveAt(0);
27 }
28 zeilen.Add(zeile);
29 }
30 foreach(var z in zeilen)
31 Console.WriteLine(z);
32 }
Dasistunübersichtlichunddudenkstdir,dassdumaleinenwichtigenTeil
herauslösen könntest in eine eigene Funktion, z.B. das Zusammensetzen
der neuen Zeilen:
1 public static void Main(string[] args) {
2 var dateiname = args[0];
3 var maxZeilenlänge = int.Parse(args[1]);
4 var text = File.ReadAllText(dateiname);
5 var worte = text.Split(new[] {' ', '\t', '\n', '\r'},
6 StringSplitOptions.RemoveEmptyEntries);
7 worte = worte.SelectMany(wort => {
8 var wortteile = new List<string>();
9 while (wort.Length > maxZeilenlänge) {
10 wortteile.Add(wort.Substring(0, maxZeilenlänge));
11 wort = wort.Substring(maxZeilenlänge, wort.Length - maxZeilenlänge);
12 }
13 if (wort.Length > 0) wortteile.Add(wort);
14 return wortteile;
15 }).ToArray();
16
17 var zeilen = Zusammensetzen(worte, maxZeilenlänge);
18
19 foreach(var z in zeilen)
20 Console.WriteLine(z);
21 }
22
23
24 private static IEnumerable<string> Zusammensetzen(IEnumerable<string> worte,
25 int maxZeilenlänge) {
26 var verbleibendeWorte = new List<string>(worte);
27 var zeilen = new List<string>();
28 while (verbleibendeWorte.Count() > 0) {
29 var zeile = "";
30 while (verbleibendeWorte.Count() > 0) {


---


<!-- Page 189 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 180
31 var tempZeile = zeile + (zeile.Length > 0 ? " " : "")
32 + verbleibendeWorte[0];
33 if (tempZeile.Length > maxZeilenlänge)
34 break;
35 zeile = tempZeile;
36 verbleibendeWorte.RemoveAt(0);
37 }
38 zeilen.Add(zeile);
39 }
40 }
Das ist eine super Idee! Nur leider ist jetzt dem IOSP nicht mehr Genüge
getan in Main(). Das darf nicht sein. Main() enthält jetzt offensichtlich
zwei Abstraktionslevel, ein Widerspruch auch zum SLA. Also muss auch
die restliche Logik dort “nach unten gedrückt werden”. Wie du sie dafür
in Operationen einteilst, ist dir überlassen. Im einfachsten Fall entstehen
nurzweiweitereFunktionen:einefürdieLogikvorderausgelagertenund
eine für die Logik dahinter.
1 public static void Main(string[] args) {
2 var (worte, maxZeilenlänge) = Beschaffen(args);
3 var zeilen = Zusammensetzen(worte, maxZeilenlänge);
4 Ausgaben(zeilen);
5 }
6
7 private static IEnumerable<string> Zusammensetzen(IEnumerable<string> worte,
8 int maxZeilenlänge) {
9 ...
10 }
11
12 private (IEnumerable<string> worte, int maxZeilenlänge) Beschaffen(string[] args) {
13 var dateiname = args[0];
14 var maxZeilenlänge = int.Parse(args[1]);
15 var text = File.ReadAllText(dateiname);
16 var worte = text.Split(new[] {' ', '\t', '\n', '\r'},
17 StringSplitOptions.RemoveEmptyEntries);
18 worte = worte.SelectMany(wort => {
19 var wortteile = new List<string>();
20 while (wort.Length > maxZeilenlänge) {
21 wortteile.Add(wort.Substring(0, maxZeilenlänge));
22 wort = wort.Substring(maxZeilenlänge, wort.Length - maxZeilenlänge);
23 }
24 if (wort.Length > 0) wortteile.Add(wort);
25 return wortteile;
26 }).ToArray();
27
28 return (worte, maxZeilenlänge);
29 }
30
31 private static void Ausgeben(IEnumerable<string> zeilen) {
32 foreach(var z in zeilen)
33 Console.WriteLine(z);
34 }
Ob dieser Schnitt durch die Logik allerdings ein guter ist…? Ausgeben()
sieht plausibel aus. Beschaffen() hingegen fühlt sich nicht so gut an.
Warum sollten Worte und die maximale Zeilenlänge zusammen beschafft
werden? Die Resultatsstruktur deutet auf eine Vermischung von Verant-
wortlichkeiten hin.


---


<!-- Page 190 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 181
Welche Schnitte durch die Logik besser wären, überlasse ich dir zur Über-
legung als Fingerübung. Hier wollte ich dir nur zeigen, was zu geschehen
hat, wenn du aus einer Operation anfängst, Logik zu extrahieren. Dann
greift das IOSP und aus der Operation wird eine Integration.
Integrationen wie Operationen sind beide Kompositionen. Extraktion und
Inlining sind im Rahmen des IOSP also völlig normal. Ob das noch
im Entwurf im Datenfluss-Modell geschieht oder dir erst während der
Implementation auffällt, ist einerlei.
Wenn dir allerdings eine Extraktion von Logik schwer fällt, dann liegt
die Ursache dafür oft in verschmierten Verantwortlichkeiten - du findest
hier und da und dort verteilt über die Logik in der Operation dieselbe
Verantwortlichkeit - und Schleifen, allemal geschachtelten. Nimm das
dann bitte nicht als Argument gegen das IOSP, sondern als Symptom
der schlechten Evolvierbarkeit und Testbarkeit des Codes. Das IOSP ist
sozusagen nur der Sensor, mit dem du solche Unsauberkeit aufspürst.
Don’t shoot the messenger!
AlsBeispielfüreineOperation,dieschwernachIOSPzurefaktorisierenist,
der Textumbruch mal etwas anders. Auf solche Logik kommt man, wenn
man nicht durch das IOSP durch einen Entwurf geleitet wird, sondern
gleich mit der Codierung beginnt:¹¹⁰
1 static void Main(string[] args) {
2 var dateiname = args[0];
3 var maxZeilenlänge = int.Parse(args[1]);
4 var text = File.ReadAllText(dateiname);
5 var worte = text.Split(new[] {' ', '\t', '\n', '\r'},
6 StringSplitOptions.RemoveEmptyEntries);
7 var verbleibendeWorte = new List<string>(worte);
8 while (verbleibendeWorte.Count() > 0) {
9 var zeile = "";
10 while (verbleibendeWorte.Count() > 0) {
11 if (verbleibendeWorte[0].Length > maxZeilenlänge) {
12 var kopf = verbleibendeWorte[0].Substring(0, maxZeilenlänge);
13 verbleibendeWorte[0] = verbleibendeWorte[0].Substring(
14 maxZeilenlänge,
15 verbleibendeWorte[0].Length - maxZeilenlänge\
16 );
17 verbleibendeWorte.Insert(0, kopf);
18 }
19 var tempZeile = zeile + (zeile.Length > 0 ? " " : "")
20 + verbleibendeWorte[0];
21 if (tempZeile.Length > maxZeilenlänge)
¹¹⁰Wahrscheinlich würde einecode-first Lösung sogar noch unsauberer aussehen, insbe-
sondereineinerSprachemitwenigerAbstraktionenoderwennAbstraktionennichtbekannt
sind.IchkannmirdasfürdieseLösungabernichtmehrvorstellen,weilichzuderLogikvon
der anderen Seite her gekommen bin. Was du im Beispiel siehst, ist nur mein Versuch, eine
eigentlichsaubereLösung“zuverdrecken”.


---


<!-- Page 191 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 182
22 break;
23 zeile = tempZeile;
24 verbleibendeWorte.RemoveAt(0);
25 }
26 Console.WriteLine(zeile);
27 }
28 }
In den Zeilen 2 bis 6 ist noch kein Unterschied festzustellen. Doch danach
geht es bunt durcheinander. Die äußere while-Schleife ist eigentlich für
den Zeilenzusammenbau zuständig, doch darin findet sich auch die das
Zerschneiden von Worten und die Ausgabe auf der Konsole. Das ist sehr
unglücklich - und doch leider so normal.
Sag selbst: Wenn du mit einer Funktion konfrontiert wirst, die einen
TextumbruchwieindenAnforderungenbeschriebenleistet,wenndualso
dasersteMalauf Main()stößt,möchtestdudanndieobigeVersionsehen
oder die folgende?
1 static void Main(string[] args) {
2 var (dateiname, maxZeilenlänge) = Analysieren(args);
3 var text = Laden(dateiname);
4 var worte = Zerlegen(text);
5 worte = Zerschneiden(worte, maxZeilenlänge);
6 var zeilen = Zusammensetzen(worte, maxZeilenlänge);
7 Ausgeben(zeilen);
8 }
Diese Frage kannst du dir für jedes Problem stellen. Wie soll der Code
aussehen,derdieLösungdarstellt?MöchtestduliebereinenHaufenLogik
sehen oder ein Gemisch aus Logik und ein paar Funktionsaufrufen? Oder
möchtest du eine Integration sehen?
Was ist lesbarer für dich? Was ist übersichtlicher? Was lässt sich besser
refaktorisieren? Wo lässt sich Logik am Ende besser testen?
Ich hoffe, deine Antwort ist inzwischen ein Ja. Vielleicht noch etwas zag-
haft, weil du dein Glück nicht fassen kannst, ein Strukturierungsprinzip
gefunden zu haben, das solche Ordnung liefert, dennoch schon ein Ja.
Gern darf das kräftiger und lauter werden, mit etwas Zagen kann ich aber
auch leben. Wir sind ja erst bei Kapitel 5.
Notation
Integrationen wie Operationen sind Kompositionen. Sie bauen etwas
Neues, Größeres aus Teilen zusammen. Das, was sie zusammenbauen


---


<!-- Page 192 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 183
ist Verhalten, Funktionalität, eine Transformation von Eingabedaten in
Ausgabedaten (ggf. mit Seiteneffekten).
Komposition findet genau genommen jedoch nur von unten nach oben
statt. Von oben nach unten findet Dekomposition statt. Wie kommst du
auf die Teile, die zu einem Ganzen zusammengesetzt werden? Sind die
schon vorhanden? Das ist bei Operationen der Fall. Die Logik, die dort
“zusammengebaut”wird,istdurchProgrammiersprache,Bibliothekenund
Frameworks gegeben. Sie wird zwar noch etwas parametrisiert, doch die
Teile sind schon fertig. Eine Operation als Komposition entsteht insofern
durch Synthese.
Bei Integrationen hingegen ist es oft (vielleicht sogar meistens?) anders
herum: Du kennst das Äußere einer Funktionseinheit, du weißt auch,
dass sie keine Operation, sondern eine Integration sein soll. Doch welches
“Vokabular” brauchst du, um ihren Prozess zu beschreiben? Wenn es das
noch nicht gibt, dann musst du zuerst Analyse betreiben; du musst das
durch die Funktionseinheit repräsentierte Problem “auseinandernehmen”.
Du musst Teilprobleme identifizieren, deren Lösungen zusammen das
Ausgangsproblem lösen. Das ist Dekomposition. Und wenn du das mehr-
fach tust angefangen von einer Wurzelintegration für das Gesamtproblem
“nach unten” durch viele Ebenen der Integration, dann ist das rekursive
Dekomposition oder stepwise refinement.
Stepwise refinement ist eine ehrwürdige Methode. Niklaus Wirth hat
den Begriff 1971 in seinem Paper “Program Development by Stepwise
Refinement¹¹¹” geprägt:
“Ineachstep,oneorseveralinstructionsofthegivenprogram
are decomposed into more detailed instructions. This succes-
sivedecompositionorrefinementofspecificationsterminates
when all instructions are expressed in terms of an underlying
computer or programming language, and must therefore
be guided by the facilities available on that computer or
language.”
“Instructions” kannst du durch “Funktionseinheiten” ersetzen und “terms
of an underlying computer or programming language” steht für “Lo-
gik”. Die schrittweise Verfeinerung zerlegt zunächst Integrationen in
¹¹¹https://john.cs.olemiss.edu/~dwilkins/Seminar/S05/wirth.pdf


---


<!-- Page 193 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 184
Integrationen und Operationen, bis alle Blätter der Zerlegungshierarchie
Operationen sind. Das ist die Modellierungsphase. In der anschließenden
Codierungsphase zerlegt die schrittweise Verfeinerung dann die Operatio-
nen in Logik-Anweisungen.
Allerdings gibt es ein entscheidenden Unterschied zwischen der Dekom-
positionzuWirthsZeitenunddem,wasichdirhiervermittelnwill:Wirth
kannte das IOSP nicht. In Wirths Paper findest du daher eine Pascal-
Pseudocode void-Funktion wie diese:
1 procedure Trycolumn(j) ;
2 begin integer i; i : = 0;
3 repeat i : = i+ 1 ; testsquare;
4 if safe then
5 begin setqueen; x[j] := i;
6 if j < 8 then Trycolumn (j+ 1) ;
7 if not safe then removequeen
8 end
9 until safe or (i = 8)
10 end
DasistkeineIntegration,dasistkeineOperation-dennochistWirthdamit
zufrieden. Ich wäre es nicht. Das ist für mich nicht sauber. Das folgt nicht
IOSPundistdeshalbnichtleichttestbar,ganzabgesehenvondergeringen
Verständlichkeit.
Die rekursive Dekomposition bzw. die schrittweise Verfeinerung sind
weiterhin eine zentrale Analyse- und Problemlösungstechnik - allerdings
nur mit einem Upgrade. Stepwise refinement 2.0 berücksichtigt IOSP und
PoMO. Stepwise refinement hat als Resultat ein Datenfluss-Modell.¹¹²
Datenflüsse als aufgemotzte
Abhängigkeitsdiagramme
Das, was durch eine rekursive Dekomposition zunächst entsteht, ist “nur”
ein Problembaum: ein großes Problem wird zerlegt in kleinere Probleme
¹¹²Zumindest der Rahmen des Modells sollte ein Datenfluss-Modell sein. Du kannst
stattdessen und darüber hinaus natürlich auch in andererweise modellieren, z.B. mit Zu-
standsautomaten. Allerdings glaube ich erstens, dass du mit Flow-Design beginnen solltest
undsehrweitkommst;meistensbrauchstdukeinenanderenModellierungsansatz.Zweitens
bleibe ich dabei: Egal, welchen Modellierungsansatz du wählst, das Ergebnis muss Klarheit
in Bezug auf die zu codierenden Funktionen sein, die selbstverständlich wieder dem IOSP
folgen müssen und wahrscheinlich Operationen sein werden, weil darüber Liegendes eben
imModellierungsansatzausgedrücktist.


---


<!-- Page 194 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 185
und jedes kleinere Problem wird wiederum zerlegt in noch kleinere
Probleme. Das könnte man mit echter Schachtelung visualisieren:
Doch das wird schnell unhandlich; damit lässt sich nicht genügend Tiefe
darstellen und Verbindungen sind über “Containergrenzen” hinweg auch
schwierig. Also ist ein Baum die bessere Darstellung:
“Problembaum” klingt nicht so gut, oder? Ein Problem ist schon genug;


---


<!-- Page 195 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 186
wer will da einen ganzen Baum von Problemen haben? Der Problembaum
kann allerdings als Lösungsbaum reframet werden: Jedes Mal, wenn du
ein Problem vollständig in kleinere Probleme (Teilprobleme) zerlegst, hast
du für das Problem eine Lösung gefunden. Das Schlüsselwort ist vollstän-
dig. In der Programmierung bedeutet das: Die Lösungen der Teilprobleme
stehen für die gesamte Logik, die zur Lösung des Ausgangsproblems nötig
ist. Denn um nichts anderes geht es, wenn du ein Problem lösen sollst:
Du sollst die Logik finden. Oder allgemeiner ausgedrückt: Du sollst eine
passendeKompositionausgegebeneBausteinenfinden.WelcheBausteine
werden gebraucht? Wie sind die Bausteine zu konfigurieren? Und wie
sind die Bausteine dann “zu verdrahten”? Für jedes Teilproblem musst
du nur lediglich annehmen, dass du auch dafür eine Lösung finden wirst.
EntwederdurchweiterevollständigeZerlegungoderirgendwanninForm
von Logik. Du folgst einfach nur systematisch und “reihenweise” dem
mañana Prinzip¹¹³:
“Mañana is the Spanish word for tomorrow. […] When —
during implementation of a method — you wish you had a
certain support method, write your code as if you had it and
implement the method later.”¹¹⁴
Eine vollständige rekursive Dekomposition ist also eine, bei der das IOSP
Treiber für die Zerlegung ist. Du zerlegst ein Problem so lange, dass du
gewiss oder zumindest zuversichtlich bist, dass zur endgültigen Lösungen
lediglich noch ein bisschen triviale Integration der Lösungen für die
Teilprobleme nötig ist.
Zunächst ist ein Zerlegungsbaum¹¹⁵ nur eine Abhängigkeitshierarchie.
Größere Probleme bestehen aus kleineren, umfassendere Lösungen sind
abhängig von Teillösungen. Beachte bitte, dass ich deshalb im folgenden
¹¹³http://www.cs.cornell.edu/courses/JavaAndDS/files/manana.pdf
¹¹⁴“Method” musst du hier natürlich zunächst allgemein als Problem verstehen. Und
“supportmethod”isteinTeilproblem,dessenLösungdueinfachannimmst.Ergänzendwürde
ichsogarnochdazusetzen:FallsdirkeinknackigerNamefürdasTeilproblemeinfällt,dann
schreibst du einfach einen Platzhalter hin. X ist genauso gut wie Y oder Noch keine
Ahnung oder Restproblem. Zu oft sollte dir das während der Zerlegung eines Problems
zwar nicht passieren, denn wenn dessen Teilprobleme nur X, Y, Z heißen, ist auch nicht so
viel gewonnen. Aber ich denke, du verstehst, was ich meine. Ab und an entgehst du mit
einemPlatzhaltereinerBlockade.
¹¹⁵Zerlegungsbaum scheint mir der neutrale Begriff oberhalb von Problembaum und
Lösungsbaumzusein.


---


<!-- Page 196 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 187
Diagramm das Symbol für die Abhängigkeitsbeziehung benutze und die
Beziehung von oben nach unten verläuft, also vom Ganzen zum Teil:
So ein Abhängigkeitsdiagramm ist dir sicher schonmal über den Weg ge-
laufen.EinFunktionsbaumistnichtsanderes.HiereinerfürdieTextumbruch-
Musterlösung. Darin sind alle Funktionen in ihrer Aufrufhierarchie gelis-
tet - allerdings hat die Reihenfolge keine Bedeutung:
Wenn der Zerlegungsbaum jedoch vollständig ist, dann kannst du daraus


---


<!-- Page 197 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 188
einen 2-dimensionalen Datenfluss machen.¹¹⁶ Der Bogen unterhalb einer
Integration zeigt einerseits Abhängigkeit an und andererseits Organisati-
on in einem Fluss. Ein 2-dimensionaler Datenfluss ist insofern ein “aufge-
motztes” Abhängigkeitsdiagramm.¹¹⁷ Er gibt dir mehr Informationen:
1. Welche Abhängigkeiten existieren?
2. Und welche “Zusammenarbeitsbeziehungen” zwischen den Abhän-
gigkeiten existieren?
Insofern ist eine Integration mehr als die Summe ihrer Teile. Auch wenn
sie keine Logik enthält, kennt sie ihre Teile nicht nur, sondern addiert
dazu noch eine Ordnung. Dass das eine Teil mit einem anderen in
gewisser Weise “verdrahtet” ist, ist ein Zusatz gegenüber einem reinen
Zerlegungsbaum.
Integration ist eine eigene Leistung. Wenn ein Problem in Teilprobleme
vollständig zerlegt ist, ist es genau genommen also noch nicht gelöst.
Es bleibt herauszufinden, wie die Lösungen der Teilprobleme am Ende
zusammenspielen müssen. Die wahrhaft vollständige Zerlegung eines
Problems sieht daher so aus:
¹¹⁶Ein Zerlegungsbaum ist sichtbar irgendwie nicht vollständig, wenn es eine 1:1-
Zerlegung gibt wie z.B. bei Zusammensetzen() und Zusammensetzen()'. Wenn eine
Funktionseinheitinnureineanderezerlegtwird,dannkanneskeinenFlussgeben.Esmuss
alsonochirgendetwas“Spannendes”passierenaufderoberenEbene.ImBeispielistdasdie
“Vorbereitung”derRekursiondurchzusätzlicheParameter.DasistzwarkeineLogik,aberes
isthervorhebenswert.InanderenFällenkannessichumLogikhandeln,wieduuntensehen
wirst.
¹¹⁷In einem Zerlegungsbaum ist jedes Teil auch nur einmal gelistet. In einem Datenfluss
hingegenkönnenTeileauchmehrmalsvorkommen,wennsieinderVerarbeitungmehrfach
gebrauchtwerden.


---


<!-- Page 198 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 189
Doch das Restproblem der Integration der Lösungen der Teilprobleme ist
trivial. Und falls nicht, dann hast du wahrscheinlich einige nicht triviale
Teilproblemenochnichtidentifiziert.MachmitderDekompositionweiter!
Und am Ende löst du das “Restproblem: Intgeration”, indem du es nicht
einfach wie die anderen Teilproblem unter das Ausgangsproblem hängst
unddaraufwartet,dassdirdazuetwasbeiderCodierungeinfällt-sondern
du “bringst die Teilprobleme in Fluss”. Weg von den Abhängigkeiten, hin
zum Datenfluss.
Zeit für ein Beispiel:
Einen Diamanten wachsen lassen
Ein Programm soll einen ASCII-Diamanten folgender Form ausge-
ben:
1 $ diamant C
2 A
3 B B
4 C C
5 B B
6 A
7 $
Gegeben ist als Kommandozeilenparameter ein Buchstabe, der die
Breite des Diamanten definiert. Der Diamant besteht aus Schichten,
die mit einem Buchstaben bezeichnet sind, bei A beginnen und
bis zum gegebenen Buchstaben fortschreiten. Die Schichtenbreite
variiert mit ihrem Buchstaben.
QuellederAufgabe:https://codingdojo.org/kata/Diamond/


---


<!-- Page 199 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 190
Das ist natürlich wieder mal ein von der Domäne her triviales Szenario.
Die “in Auftrag gegebene” Funktion aus der Anforderungsanalyse liegt
auch auf der Hand: Main(); es handelt sich ja um ein Programm, das
nur eine Interaktion mit dem Benutzer beherrscht. Ich denke, es gibt kein
Verständnisproblem und wir können gleich in den Entwurf springen.
So überschaubar das Problem aber auch ist, ein Gedanke sollte an den
Lösungsansatz verschwendet werden. Worin könnte der bestehen? Die
Domäne ist so klein, da möchtest du sicherlich einfach loslegen und ein
paar Schleifen codieren, damit die Sache vom Tisch ist. Klar, das kann
man schon so machen - nur geht’s hier um die Übung von Flow-Design.
Also halten wir uns zurück. Gehen wir die Sache im Kleinen sauber
systematisch an; wenn wir das können, können wir es auch im Großen.
Zurückhaltung und genaues Hinschauen ist die Grundlage.
Also, der Lösungsansatz: Wie kann der Aussehen? Für mich besteht er le-
diglichinderEntscheidung,denDiamanteninzweiSchrittenaufzubauen:
1. Die verschiedenen Schichten werden generiert.
2. Die Schichten werden zu einem Diamanten aufeinander gelegt.
Der Lösungsansatz konzentriert sich auf die Domäne. Und der Lösungsan-
satzwehrtsichbewusstgegendenReflex,denDiamantenaufbaualseinen
“monolithischen Algorihtmus” zu verstehen. Denn wo Algorithmus drauf
steht, ist schnell Unverständlichkeit drin. Wo Algorithmus draufsteht,
da gibt es kein Halten, was Kontrollstrukturen angeht; Testbarkeit und
Refaktorisierbarkeit werden dadurch erschwert.
Jetzt zum Modell.
Zuerst eine Dekomposition der Probleme. Alles beginnt mit dem Gesamt-
problem,derkomplettenAufgabe.EswirddurcheineFunktionseinheitan
der Wurzel repräsentiert und später durch Main() im Code gelöst.
• Main()


---


<!-- Page 200 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 191
Welche Teilprobleme kann ich darin erkennen? Als erstes fällt mir die
gesamte Domäne ein:
• Wachsen(): ein Diamant soll um einen Buchstaben “wachsen”.
Daraus folgen dann allerdings zwei Teilprobleme, die die Domäne einrah-
men, wenn ich eine vollständige Zerlegung will:
• Präsentieren(): der Diamant muss “präsentiert werden”
• Finden(): und der Buchstabe als Samen für das Diamantenwach-
sum muss ermittelt werden.


---


<!-- Page 201 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 192
IstdamitdieDekompositionabgeschlossen?Nein.MeinLösungsansatzist
noch nicht sichtbar. Beim Wachstum gibt es Teilprobleme:
• Generieren(): Wie oben schon beschrieben, sollen die Schichten
des Diamanten zuerst gebildet werden.
• Pressen(): Und dann werden die Schichten zu einem ganzen
Diamanten “gepresst”.


---


<!-- Page 202 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 193
Mehr braucht es nicht, um das Wachstumsproblem zu lösen. Die Zerle-
gung halte ich für vollständig.
Ist jetzt endlich die Dekomposition abgeschlossen? Angesichts dessen,
dass es sich um eine Übungsaufgabe handelt, kannst du dir denken, dass
die Antwort Nein ist. Ich möchte mir dir ja die Dekomposition üben. Du
sollst deinen Blick dafür schärfen, denn ein stepwise refinement 2.0 liefert
dir eine optimale Ausgangsposition für die Codierung. Testbarkeit und
Verständlichkeit sind sofort hoch; Refaktorisierung nicht mehr nötig.
Bei gegebenen Schichten, scheint mir das Pressen tatsächlich nun trivial.
Doch die Generierung kann noch eine weitere Zerlegung vertragen:
• Aufspannen(): Für jede Schicht muss aus einem Buchstaben eine
ganze Schicht hergestellt werden.
• Aufschichten(): Und welche Schichten gibt es überhaupt? Aus-
gehend von einem Buchstaben gilt es Aufbau und Umfang des
Diamanten festzulegen.
Jetzt erst bin ich zufrieden. Eine weitere Zerlegung muss nicht sein. Ich
traue mir zu, alle Blätter mit Logik zu füllen. Die Blätter sind rot gefärbt,


---


<!-- Page 203 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 194
weilichdamitandeutenwill,dassdortLogik-“Gefahr”lauert.Dieanderen
Knoten im Baum sind grün, weil Integration “gefahrlos” ist.
“Gefährlich” ist für mich eine Komposition, bei der das Risiko groß ist,
einen Fehler zu machen. Wo das der Fall ist, muss ich vorsichtig vorgehen,
ambestentest-first beiderCodierung.AberdasistindiesemBandjanicht
das Thema.
DerZerlegungsbaumisteinersterSchrittfürsModell.Ichseheschon,wel-
che Funktionen später gebraucht werden. Aber ihre Signaturen sind noch
nicht klar. Ich kenne ihre Beziehungen im Sinne der Eingabe-Ausgabe-
Transformation noch nicht. Zur vertikalen Dimension 2-dimensionaler
Datenflüssemussjetztnochdiehorizontalekommen:die1-dimensionalen
Datenflüsse, die von den abhängigen Funktionseinheiten integriert wer-
den.
Jetzt muss ich nur noch für jede Integration die Reihenfolge der Verar-
beitungsschritte festlegen und die fließenden Daten identifizieren. Das
Modell in zwei Schritten aufzubauen, finde ich sehr entspannend. Ich
muss mich nicht sofort um den korrekten Datenfluss kümmern, sondern
kann mich erstmal auf die Dekomposition konzentrieren:
1. Dekomposition, Analyse, Zerlegungsbaum: Probleme in Teilpro-
bleme zerlegen, den Abhängigkeitsbaum vom Wurzelproblem her
wachsen lassen bis zu den Operationen.
2. Komposition, Synthese, Datenflüsse: Die Teillösungen zu ganzen
Lösungen integrieren. Das geschieht tendenziell von den Blättern
zur Wurzel hin.


---


<!-- Page 204 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 195
Mir zu überlegen, wie genau die identifizierten Funktionseinheiten als
Lösungen für Teilprobleme “zusammenspielen”, ist wirklich eine ganz
eigene Aufgabe. Selbst wenn du dir über die Funktionseinheiten klar bist,
magst du noch rätseln, welche Daten fließen sollten. In diesem Szenario
habe ich an zwei Stellen gegrübelt:
• Was soll aus Finden() herausfließen? Soll der Buchstabe von der
Kommandozeile durchgereicht werden? Oder soll er übersetzt wer-
den in einen numerischen Wert, der z.B. die Anzahl der Schichten
angibt? Am Ende habe ich mich für die Beibehaltung des Buch-
stabens entschieden, weil der nicht nur in der Eingabe, sondern
auch der Ausgabe auftaucht. Ich zähle ihn zu domänenrelevanten
Daten.¹¹⁸
• Was ist das Ergebnis von Aufspannen()? Wieviel Arbeit wird
dort schon geleistet? Für mich ist die Funktionseinheit der Kern
im Kern der Anwendung. Dort wird der Rahmen des Diamanten
¹¹⁸Das ist auch der Einfachheit des Szenarios und der Übungssituation hier geschuldet.
In “richtigen” Anwendungen wäre ich damit vorsichtiger. Daten vom Anwender “einfach
so” in die Domäne zu schleifen, kann gefährlich sein, weil es den Anwendungskern an die
Benutzerschnittstellebindet.


---


<!-- Page 205 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 196
hergestellt. Aufschichten() füllt den nur noch aus. Deshalb
fließen aus Aufspannen() keine primitiven Daten, sondern ein
Tupel, das eine Schicht beschreibt, eine Schichtendefinition.
Sie gibt an, wieviele Zeichen eine Schicht umfassen soll ( breite)
und mit welchem Buchstaben sie zu versehen ist ( kennung). Dass
die Schichten in der Anforderungsbeschreibung von A bis C und
dann wieder bis A wachsen und schrumpfen, wie sie das tun, das
steckt in Aufspannen().
Bei der “Verflüssigung” eines Zerlegungsbaums können sich gerade we-
gen dieser Überlegungen zu den Nachrichten zwischen den Funktions-
einheiten auch nochmal Veränderungen ergeben. Der Antrieb für den
Zerlegungsbaum ist ein trennender; der Antrieb für den Datenfluss ist
ein verbindender. Diese Kräfte müssen in Balance gebracht werden.
Das ist gelebtes SRP: Die einen Entscheidungen wollen zu einer anderen
Zeit getroffen werden als die anderen. Wir müssen damit nicht andere
Personen betrauen; es reicht, wenn wir uns Zeit nehmen und durch Pha-
sen mit unterschiedlichem Fokus gehen. Die übliche Herangehensweise
versucht unter Druck zu viele verschiedene Entscheidungen auf einmal
zu treffen; das Mindset wird nicht wirklich gewechselt. Man liest kurz die
Anforderungen und setzt sich dann schon an den Code. Das entspricht
allerdings nicht der Komplexität der Sache.¹¹⁹
Und nun? Ist das eine Lösung, die funktionieren würde, wenn sie imple-
mentiert würde? Die Frage stellt sich immer nach dem Entwurf. Eine
gewisse Unsicherheit bleibt, doch mit Erfahrung wirst du die sehr klein
bekommen. Oder du wirst leicht die Bereiche im Entwurf benennen
können, die dir noch Bauschmerzen machen; dann kannst du sie mit einer
spike solution¹²⁰ näher beleuchten, um deine Unsicherheit auszuräumen.
Ob mein Modell für die Diamantenpressung etwas taugt, wirst du selbst
herausfinden. Das wird eine der Übungsaufgaben zu diesem Kapitel sein.
¹¹⁹Ich weiß, ganz so stürmisch gehst du natürlich nicht vor. Du machst dir Gedanken.
Du überstürzt nichts. Niemals! Und dennoch… Irgendwie kommt es ja dazu, dass der Code
eineFormbekommt,diedirnunProblememacht.DuliestdiesesBuch.Irgendetwasistalso
schiefgelaufenbeideinembedachtenAnsatz.MeineVermutung:Duüberstürztzwarnichts
- aber die Differenzierung ist dennoch nicht fein genug. Du hast immer wieder zu viel auf
einmal gewollt. Und das ist ja auch kein Wunder, wenn dir eine Deadline im Nacken sitzt.
Aber es hilft nichts: Die Dinge müssen eben richtig getan werden. Sonst kommt zu wenig
dauerhafte Qualität heraus. Differenzierung beim Tun gehört für mich dazu, richtig zu tun
inderSoftwareentwicklung.
¹²⁰http://www.extremeprogramming.org/rules/spike.html


---


<!-- Page 206 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 197
Konsistenz
AmobigenModelllässtsicheinGrundsatzdesFlow-Designsschönerken-
nen: Be consistent! Achte darauf, dass deine 2-dimensionalen Datenflüsse
konsistentsind,wasEin-undAusgabenaufdenunterschiedlichenEbenen
angeht:
• Das, was in eine Integration hineinfließt, muss auch in den Daten-
fluss, den sie definiert, hineinfließen.
• Das, was aus einer Integration hinausfließt, muss auch aus dem
Datenfluss, den sie definiert, hinausfließen.
Im folgenden Bild ist durch die pinken Kreise verbunden, was überein-
stimmen muss:
• args fließt in Main hinein und deshalb auch in die erste Funkti-
onseinheit, die Main integriert. Irgendwo muss args ja verarbeitet
werden. Die Verarbeitung findet immer durch eine Operation statt.
• Die größe fließt sogar über mehrere Ebenen final in Aufspannen
hinein.
• diamant wird von Pressen erzeugt, fließt aber erst im Stratum
darüber aus Wachsen nach Präsentieren.


---


<!-- Page 207 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 198
• UndauchderFall,dasseskeinenOutput,musskonsistentbehandelt
werden.WennMainnichtsproduziert,danndarfauchamEndedes
darin integrierten Datenflusses nichts herausfließen; Präsentie-
ren hat keinen Output.
AchteaufdieKonsistenzdeinerDatenflüsse;nimmsienichtaufdieleichte
Schulter.DufällstsonstausdeinerKonzentrationwährendderCodierung
raus,weilduspätestensdortbemerkst,dassdiretwasfehltfüreineflüssige
Umsetzung.
Strukturierte Daten
Dass fließende Daten immer am Fluss-Pfeil zu notieren sind, habe ich dir
schon eingeschärft. Dass du sie mit Name und/oder Typ notieren kannst,
habe ich dir auch schon gezeigt. Aber ist dir auch aufgefallen, dass ich
bisher alle Namen für fließende Daten klein geschrieben hatte? Das war
kein Zufall!
Die Konvention bei der Datenflussmodellierung im Flow-Design ist, dass
die Namen von fließenden Daten klein geschrieben werden, solange ihr
Typ offensichtlich oder explizit angegeben ist. Beispiele im obigen Bild
sind args (Typ ist bekannt) oder größe (Typ ist genannt).
Bei Schichtendef liegt der Fall nun anders. Den Namen habe ich groß
geschrieben, weil es sich hier um einen selbst definierten Typ handelt. Die
Großschreibung soll das hervorheben und daran erinnern, den Typ auch
im Modell zu definieren. Das kann direkt am (ersten) Verwendungsort sei
wie im Beispiel oder irgendwo “in Sichtweite”.


---


<!-- Page 208 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 199
Für die Beschreibung eines solchen Typs gibt es keine besondere Notation.
Stelle die Struktur einfach irgendwie dar, z.B. als Tupel wie im Beispiel
oder als Spiegelstrichliste:
1 Schichtendef
2 - breite:int // wieviele Zeichen soll eine Schicht umfassen;
3 // erstes und letztes sind die Kennung
4 - kennung:char // A..Z
Trau dich, eigene Typen zu definieren! Allzu leicht versucht man, mit
primitivenDatentypenauszukommen.DochdasverschenktamEndeeine
Chance für die Zuordnung von Logik.
Und vergiss nicht, die Typdefinition mit in das Modell aufzunehmen.
Nur wenn du dir sofort darüber Gedanken machst, bekommt der Fluss
auch die richtige Form. Nachrichten und “Verdrahtung” beeinflussen sich
gegenseitig.
n:1 Übersetzungen
Den Datenfluss wirst du einfach implementieren können. Kein Problem.
Dennochmöchteichihnnutzen,umdirnocheineFeinheitnahezubringen.
In dir nagt sicher die Frage, ob denn wirklich, wirklich nie Logik in einer
Integration stehen darf. Die platte Antwort habe ich dir schon geben:
Ja, nie, niemals darf Logik in einer Integration stehen. Und das ist auch
technisch hinzukriegen.
Nur,weilestechnischmachbarist,bedeutetdasjedochnicht,dassesauch
technischimmergetanwerdensollte.Wiegesagt:HöheralsdiePrinzipien
sind die zu erreichenden Ziele. Wenn Testbarkeit und Verständlichkeit
nicht kompromittiert werden, kann auch mal etwas Logik in einer Inte-
gration stehen. Dass eine Perle in einer Auster wächst, ist ja auch einer
Verunreinigungzuverdanken.ManchmalentstehtalsodiebessereLösung
durch ein bisschen Unsauberkeit.
Im Datenfluss gibt es dafür noch kein Beispiel, aber eine Chance. Die
steckt besonders in Aufschichten. Die Funktionseinheit ist ein typi-
sches Beispiel für etwas, das ich n:1 Übersetzung nenne: Es kommen n
Schichtendef-Tupel an, aber es gibt nur 1 immer gleiche Transformati-
on für alle, die dafür sorgt, dass n Schichten am Ende hinausfließen.


---


<!-- Page 209 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 200
Das Wesentliche an Aufschichten passiert also nicht für n Datenele-
mente, sondern nur für 1. Es wäre gut, das im Modell deutlich zu machen.
Das kannst du auf verschiedene Weise tun:
Wie du es darstellst, ist letztlich egal. Das Modell soll dich in der Kom-
munikation mit anderen und als Plan für die Codierung nur deutlich in
dieser Hinsicht sein. Am Ende ist es eine Übungssache, eine Sache der
Konvention im Team und auch des Kontextes.
Die Übersetzung sieht aber im Grunde immer gleich aus: ein bisschen
Logik¹²¹ in der Integration, das Wesentliche extrahiert; das Extrakt ist
dann gut testbar. In diesem Fall so:
1 IEnumerable<string> Aufschichten(IEnumerable<Schichtendef> schichtendefinitionen) {
2 var schichten = new List<string>();
3 foreach(var sd in schichtendefinitionen)
4 schichten.Add(SchichtGenerieren(sd));
5 return schichten:
6 }
7
8 string SchichtGenerieren(Schichtendef schichtendefinition) {
9 ...
10 }
Das ist mehr als in C# für Aufschichten() nötig ist, aber ich wollte
die Logik in der Funktion besonders dick auftragen. Denn: Solche Logik
ist ok. Sie ist völlig unkritisch, weil sie musterhaft ist und du gerade mit
foreach nichts falsch machen kannst. Das versteht jeder auf den ersten
Blick und muss nicht getestet werden.
Noch kürzer wäre natürlich
¹²¹Logik in der Integration ist gelegentlich ok, macht sich jedoch durchaus durch Inkon-
sistenz im Datenfluss bemerkbar. In diesem Fall fließt auf der integrierenden Ebene z.B.x*
inAhinein,aberaufderdarunterhängendenEbeneistesnurx.Wiekanndassein?Dieses
Kunststück vollbringt eben Logik in der Integration. Die ist nicht sichtbar, hat aber einen
Effekt.Ichnennesiedeshalbdarklogic:weildusiespürst,ohnesiezusehen.Siestecktnicht
indenBlätternderHierarchie,sondernistverborgenirgendwoindarüberliegendenKnoten,
wosieeineKraftausübt.Wiedarkmatter imUniversum.


---


<!-- Page 210 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 201
1 return schichtendefinitionen.Select(SchichtGenerieren);
Doch soetwas mag dir nicht in deiner Sprache zur Verfügung stehen.
Macht aber nichts, denn auch die obige ausführlichere Logik ist eine
“lässliche Sünde”.
Es gibt auch andere Fälle, in denen eine Integration eine solche triviale
Schleife enthalten kann. Mach dir nichts draus und tue es einfach. Die
Zerlegung im Diagramm ist dann zwar nicht wirklich vollständig - aber
da musst du nicht päpstlicher sein als der Papst. Manchmal gehst du auch
mit gutem Gewissen über eine rote Ampel.¹²²
Rekursion
Im Grunde ist es dasselbe bei einer Rekursion. Schau dir nochmal den
Code für das Zusammensetzen neuer Zeilen beim Textumbruch-Beispiel
an:
1 private static IEnumerable<string> Zusammensetzen(IEnumerable<string> worte,
2 int maxZeilenlänge) {
3 return Zusammensetzen(new List<string>(worte), new List<string>());
4
5 IEnumerable<string> Zusammensetzen(List<string> verbleibendeWorte,
6 List<string> zeilen) {
7 if (verbleibendeWorte.Count == 0) return zeilen;
8
9 var zeile = "";
10 while (verbleibendeWorte.Count > 0) {
11 var tempZeile = zeile + (zeile.Length > 0 ? " " : "")
12 + verbleibendeWorte[0];
13 if (tempZeile.Length > maxZeilenlänge)
14 break;
15
16 zeile = tempZeile;
17 verbleibendeWorte.RemoveAt(0);
18 }
19 zeilen.Add(zeile);
20
21 return Zusammensetzen(verbleibendeWorte, zeilen);
22 }
23 }
Zeile 3 ist nicht wirklich Logik. Dort wird lediglich ein Parameter hinzu-
gefügt. Die äußere Funktion Zusammensetzen() ist also eine saubere
¹²²Eine ausführlichere Begründung findest du in einem Blog-Artikel von mir: Kontroll-
strukturen in der Integration. Der beschreibt auch, wann Fallunterscheidungen “erlaubt”
sind. Nimm das nur bitte nicht als Freibrief, die keine Gedanken mehr über den Datenfluss
und das IOSP zu machen. Erst ein ordentlicher Datenfluss, der auf vollständige Zerle-
gung aus ist. Dann vielleicht eine kleine Optimierung für die Codierung, indem du eine
Kontrollstruktur in die Integration einstreust. Gelegenheit dazu werden dir 3-dimensionale
Datenflüssegeben.


---


<!-- Page 211 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 202
Integration. Bei der inneren Funktion - Zusammensetzen' im Zerle-
gungsbaum oben - ist das aber anders. Sie enthält vor allem Logik - und
dann ganz am Ende noch einen Funktionsaufruf, die Rekursion. Das ist
nicht sauber.
Besser würde es, wenn der Löwenanteil der Logik für den Zusammenbau
einer Zeile nochmal extrahiert würde: NächsteZeileZusammenset-
zen() wäre nun eine waschechte Operation.¹²³
1 private static IEnumerable<string> Zusammensetzen(IEnumerable<string> worte,
2 int maxZeilenlänge) {
3 return Zusammensetzen_rec(new List<string>(worte), new List<string>());
4
5
6 IEnumerable<string> Zusammensetzen_rec(List<string> verbleibendeWorte,
7 List<string> zeilen) {
8 if (verbleibendeWorte.Count == 0) return zeilen;
9 NächsteZeileZusammensetzen(verbleibendeWorte, zeilen);
10 return Zusammensetzen_rec(verbleibendeWorte, zeilen);
11 }
12
13
14 void NächsteZeileZusammensetzen(List<string> verbleibendeWorte,
15 List<string> zeilen) {
16 var zeile = "";
17 while (verbleibendeWorte.Count > 0) {
18 var tempZeile = zeile + (zeile.Length > 0 ? " " : "")
19 + verbleibendeWorte[0];
20 if (tempZeile.Length > maxZeilenlänge)
21 break;
22
23 zeile = tempZeile;
24 verbleibendeWorte.RemoveAt(0);
25 }
26 zeilen.Add(zeile);
27 }
28 }
Doch letztlich wäre die innere Funktion Zusammensetzen_rec() im-
mer noch unsauber. Das if darin ist ein Widerspruch zum IOSP.
Istdasaberwirklichschlimm?Nein.DieLogikisttrivial,alsoverständlich
und nicht testwürdig. Am Anfang der rekursiven Methode wird die
Abbruchbedingung geprüft; das ist musterhaft. Wirklich spannend (oder
kritisch) ist das, was zwischem dem und dem rekursiven Aufruf passiert.
¹²³Ich innere, rekursive Funktion versehe ich jetzt mal mit dem Suffix_rec, um sie von
deräußeren,sichtbarenzuunterscheiden.InF#gibtessogareinSchlüsselwort,mitdemman
rekursiveFunktionenkennzeichnenmuss:rec.Daserschienmirzuerstüberflüssig,weiles
inanderenSprachenfehlt;dochirgendwanndachteich,dassesgarkeineschlechteIdeeist,
einesolcheEntscheidungexplizitimCodezumachen.DerunbedarfteLeseristdanngleich
vorgewarnt.


---


<!-- Page 212 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 203
Das ist nun herausgezogen und für sich testbar. Wunderbar.¹²⁴
WiewürdenunaberdasModellfüreinesolcheImplementationaussehen?
Lässt sich das darstellen, also planen? Hier ein Vorschlag:
• Die “selbstbezügliche” Abhängigkeit steht für den rekursiven Auf-
ruf.
• Und der fehlende Output bei NächsteZeileZusammensetzen
deutetdaraufhin,dasseswohleinenSeiteneffektgebenmuss.Sonst
würde die Funktionseinheit keinen Sinn machen.
• maxZeilenlänge fließt hier in die untergeordneten Funktionsein-
heiten, weil die Nutzung einer closure im Code nur eine Optimie-
rung darstellt.
Schön ist etwas anderes. Es geht auch noch ein bisschen schöner, wenn
du erstmal 3-dimensionale Datenflüsse kennengelernt hast. Doch für den
Moment soll das reichen. Du kannst damit Rekursionen modellieren.
¹²⁴ObeseineguteIdeeist,ListenhineinzureichenundinderFunktionzuverändern,also
vonaußengesehenmitmutable Objektenzuarbeiten,seidahingestellt.InderFunktionalen
Programmierung wäre das ein no go. Solange OO-Sprachen das aber nicht leichter machen
und breit Tupel als Rückgabewerte anbieten, kannst du im Einzelfall so arbeiten, denke
ich. NächsteZeileZusammensetzen() ist keine pure function, doch der Seiteneffekt ist
überschaubarundgewollt.


---


<!-- Page 213 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 204
Reflexion
2-dimensionale Datenflüsse sind etwas ganz Natürliches. Kein Datenfluss
ohneIntegration;irgendwermussaucheinen1-dimensionalenDatenfluss
“verdrahten”. Damit ist die Integration im Modell. Warum dann nicht Un-
termengen von Datenflüssen wiederum durch eine Integration ersetzen?
Das geht in beliebiger Tiefe und ist das Mittel, um eine steigende Zahl von
Operationen in den Griff zu bekommen im Hinblick auf die Komposition.
Wie tief so ein Integrationsbaum dann ist, kannst du dir überlegen.
Setze einfach für jede Integration fünf Funktionseinheiten an, die darin
verbunden werden.
Auf der 0-ten Ebene gibt es 1 Funktionseinheit als Wurzel.
1. Auf der ersten Ebene gibt es 5 Funktionseinheiten.
2. Auf der zweiten Ebene kann es 5x5=25 Funktionseinheiten geben.
3. Auf der dritten Ebene kann es 25x5=5x5x5=125 Funktionseinheiten
geben.
Aufdern-tenEbenegibtesalso5^nFunktionseinheiten.Wennndieletzte
Ebene bezeichnet, sind das die Operationen.
Bei gegebener Zahl von Operationen, kannst du natürlich auch die not-
wendige Tiefe des Baumes 2-dimensionalen Datenflusses berechnen, das
ist der Logarithmus zur Basis 5. Bei 1300 Operationen wäre es die Tiefe
z.B. 4 bis 5.¹²⁵
Das ist ein bisschen theoretisch, denn du wirst kein Modell mit 1300
Operationen “am Stück” entwerfen. Du braucht kein Tool, um so einen
Datenfluss zu zeichnen. Wenn ein System zur Verarbeitung einer In-
teraktion des Benutzers am Ende so viele Operationen enthalten sollte,
dann hast du es aus größeren Bauteilen aufgebaut. Das bedeutet, dass
die Operationen - allgemeiner: Blätter - eines Baumes die Wurzeln eines
anderenseinkönnen.AmEndebedeutetdassogar,dassOperationeneines
Datenflusses Integrationen eines anderen aufrufen können. Es ist alles
eine Frage, wo der Horizont für Logik liegt. Was ist bei der Lösung eines
Problems jenseits des Horizonts der Implementation? Das ist Logik, das
¹²⁵HilfefürsolcherArtBerechnunggibtsz.B.hier:https://rechneronline.de/logarithmus/


---


<!-- Page 214 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 205
ist Funktionalität, die getestet ist und nicht verstanden werden muss im
Detail. Sie liegt verpackt in einer Black Box vor.
Aber hier greife ich schon vor auf das Thema Modularisierung. Für
wachsende Datenflüsse ist das erste Mittel zu ihrer Beherrschung die
Integration über mehrere Strata.¹²⁶ Bau dir Sprachen aus Sprachen aus
Sprachen, eine Hierarchie von Vokabular, das immer spezifischer wird:
GenerierenistspezifischeralsAufspannenundAufschichteninder
Domäne der Diamantenpressung. Und nur darum geht es, um Vokabular
für deine Domäne. Das soll dir von unten nach oben die Dinge einfacher
machenbisschließlichanderSpitzederDatenflusshierarchiedasgesamte
Verhalten mit einem “Zauberwort” gewünscht werden kann. Main sollte
vielleicht besser Abrakadabra heißen.
Take away: Mit Hierarchie werden wachsende Mengen (oder auch Kom-
pliziertheit, gar Komplexität) handhabbar. Behalte das im Hinterkopf…
In Unternehmen mag weniger Hierarchie die Zukunft sein. Bei Software
ist es aus meiner Sicht mehr. Mehr “gute” Hierarchie. Und “gut” ist - du
kannst es dir denken -, wenn die Hierarchie PoMO und IOSP folgt.
¹²⁶Siehe zu Strata auch meinen Blog-Artikel Stratified Design over Layered Design.
Bottom line: Strata sind echte Abstraktionen, architekturelle Schichten nicht. Denn Abhän-
gigkeiten sollten nur in Richtung des Abstraktionsgefälles zeigen. Das tun sie bei einer
Schichtenarchitekturnicht.


---


<!-- Page 215 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 206
Übungsaufgaben
Reflexionsaufgabe
Bitte formuliere eine Frage oder eine Erkenntnis zum Kapiteltext.
• Wo bist du gedanklich hängengeblieben, was ist dir unklar,
was passt für dich irgendwie nicht zusammen, wozu würdest
du dir noch etwas mehr Erklärung wünschen? Steht irgendet-
waszudeinerbisherigenPraxisimWiderspruchunddufragst
dich, warum du etwas ändern solltest?
• Oder: Wann hast du einen Aha-Moment gehabt, was ist
diralsbemerkenswert,spannend,ausprobierenswertaufgefal-
len? Hat irgendetwas “in dir Klick gemacht”, weil dir nun ein
Zusammenhang aufgegangen ist? Oder verstehst du jetzt aus
deiner bisherigen Praxis irgendetwas besser?
Am besten formulierst du Frage bzw. Erkenntnis schriftlich. Indem
du deine Gedanken aufschreibst, wirst du dir ihrer bewusster. Bei
einer Frage kommst du dadurch vielleicht schon einer Antwort aus
dir selbst heraus näher. Bei einer Erkenntnis fällt dir vielleicht schon
etwas ein, das du ab jetzt anders machen kannst.
Aufgabe 1 - Implementation eines Mo-
dells
Implementiere das Modell für die Anwendung, mit der man einen
Diamantenwachsenlassenkann.AlleFunktionenkönnenweiterhin
zu einer Klasse gehören.


---


<!-- Page 216 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 207
Aufgabe 2 - Die Dimensionalität eines Mo-
dells erhöhen
Du erinnerst dich an dieses Modell für das Testproblem?


---


<!-- Page 217 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 208
Das ist ein 1-dimensionaler Datenfluss, über dem lediglich Main
steht für seine Integration; das ist vernachlässigbar. Deine Aufgabe
jetzt: Mache aus diesem Datenfluss einen wahrlich 2-dimensionalen.
Überlege also, welche Funktionseinheiten unter weiteren Integra-
tionen zusammengefasst und extrahiert werden könnten. Wie viele
Ebene kannst du (halbwegs) sinnvoll denken? Falls du eine der
Operationen umwandelnmöchtestin eineIntegration,weildudarin
noch Teilprobleme siehst, tue das auch gerne.
Aufgabe 3 - Anforderungen umsetzen mit
2-dimensionalem Modell
SchreibeeinProgramm,dassdieNettozeilenindenQuellcode-Dateien
in einem Verzeichnisbaum zählt.
DieNettozeilensinddieZeilen,dienichtausschließlichKommentar-
zeilen und keine Leerzeilen sind. Beispiele auf der Basis von Java/C#
Kommentarsyntax:
1 z = x + y;
2 a = 2 * a; // verdoppeln
3 // Ein Funktionsaufruf:


---


<!-- Page 218 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 209
4 zeilen = File.ReadAllLines("hello.txt");
5 /* Ein Gedicht:
6 Im Herbst da fall'n vom Baum die Blätter.
7 Donnerwetter!
8 */
9
10 worte = zeilen.SelectMany(SplitLine); /* Es werden als Worte alle
11 Zeichenfolgen angesehen,
12 die durch Whitespace getrennt sind.*/ Console.WriteLine(worte.Count());
13 // ENDE
In diesem Codeausschnitt gibt es 5 Nettozeilen: 1, 2, 4, 10, 12
• Zeile 2 ist eine Nettozeile, weil sie neben dem einzeiligen
Kommentar non-whitespace Zeichen enthält.
• Zeile 9 ist keine Nettozeile, weil sie nur aus whitespace
Zeichen bestejt
• Zeile10isteineNettozeile,weilderKommentarerstnachnon-
whitespace Zeichen beginnt.
• Zeile 12 ist eine Nettozeile, weil nach dem Kommentarende
non-whitespace Zeichen stehen.
• Zeile 13 ist keine Nettozeile, weil vor dem Kommentar nur
whitespace Zeichen stehen.
Für mehrzeilige Kommentare zwischen /* und */ kannst du anneh-
men:
• dass sie nicht geschachtelt vorkommen,
• dass keine Kommentarzeichen innerhalb von Kommentaren
vorkommen,
• dasssienie mehrfachineinerZeilebeginnenund/oderenden,
• dass keine Kommentarzeichen innerhalb von Zeichenketten-
definitionen vorkommen.
Der Aufruf des Programms soll so geschehen:
1 $ loccount src
2 932 Nettozeilen gefunden in 16 Dateien
3 $
Der Kommandozeilenparameter bezeichnet die Wurzel eines Ver-
zeichnisbaumes, in dessen ganzer Tiefe nach Quellcodedateien ge-
sucht wird. Quellcodedateien sind Dateien mit der Endung, wie zu


---


<!-- Page 219 of 584 -->


05-Flow-Designmit2-dimensionalenDatenflüssen 210
deiner Programmiersprache passt. Für mich wäre es .cs für C#-
Dateien, für dich vielleicht .java oder .py.
TODOs
1. Entwickle einen Lösungsansatz
2. ModellieredeinenLösungsansatzmiteinem2-dimensionalen
Datenfluss
3. Codiere dein Modell
Die Behandlung von mehrzeiligen Kommentaren soll insgesamt hier
nicht zu einer Kunst ausarten; denn wenn du das vollständig machen willst,
wirstdunichtfertig.MehrzeiligeKommentaresindaberauchinvereinfachter
Form noch Herausforderung genug; sie haben ihren Sinn in dieser Aufgabe.
Kümmeredichumsie,aberversenkenichtzuvielZeitbeiihnen.


---


<!-- Page 220 of 584 -->


06 - Flow-Design mit
modularisierten
Datenflüssen
Datenflüsse spannen einen Ordnung auf. Funktionseinheiten werden in
eine funktionale Beziehung zueinander gesetzt. Zusammenarbeit entsteht.
Eigentlich sind auch nicht mehr als 1-dimensionale Datenflüsse nötig.
Alles, was getan werden muss pro Interaktion mit einem Anwender, kann
darin in Operationen gekapselt und “verdrahtet” werden.
Aber, ach!, solche “Reihenschaltungen” werden alsbald unübersichtlich.
Nach 5, 7, 12 Operationen “in Reihe”, verlierst du den Überblick. Wo
passiert was? Wie ist der Hergang der Verhaltensproduktion? Wo kannst
du welche Logik erwarten?
Um Übersicht zu behalten, fasst du also Abschnitte 1-dimensionaler Da-
tenflüsse zusammen; du ziehst weitere Integrationen ein. Die verändern
das Verhalten nicht für den Anwender, aber sie bringen dir als Entwickler
etwas.
UnddannwachsendieDatenflüsseweiter.DieeinzelnenDatenflüsseneh-
men an Operationen zu und brauchen deshalb auch mehr Integrationen.
Außerdem kommen weitere Interaktionen mit den Anwendern hinzu und
erhöhendamitdieAnzahlderDatenflüsse.Aus12Operationenwerden25,
75,150,987usw.-vondensieordnendenIntegrationenganzzuschweigen.
Wie willst du da noch durchsteigen? Das ist ein zentrales Problem der
Softwareentwicklung. In unseren “Codemaschinen” kommen so schnell
so viele “Bauteile” zusammen, dass wir ein Problem mit dem Überblick
haben. Wenn du schon in der Küche Mühe hast, Ordnung zu bewahren,
wie schwer ist das im Code? Integrationen sind bei weitem nicht genug.
Es braucht Ordnungsmittel, die darüber hinausgehen.
Dafür sind Module da. Module sind Ordnungsmittel für Funktionen.


---


<!-- Page 221 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 212
Abstraktion durch Aggregation
Integrationen und Operationen sind Kompositionen. Als Kompositionen
sind sie Abstraktionen: Sie fassen Verschiedenartiges unter einem Dach
zusammen.
LocCounter integriert drei Funktionseinheiten zu einer Gesamtfunktio-
nalität, die nun unter dem Namen LocCounter zur Verfügung steht.
Wer Nettocodezeilen zählen will, muss sich nicht mehr mit den Details
auseinandersetzen, sondern kann das Programm LocCounter nutzen.
Dasisttotaleinfach.Vieleinfacher,alsselbstParsen,Verarbeitenund
Anzeigen in der richtigen Reihenfolge zu nutzen. Das wäre ja möglich,
wenn das eigenständige Programme wären:
1 $ Parsen src | Verarbeiten | Anzeigen
2 932 Nettozeilen gefunden in 16 Dateien
3 $
Zu parsen ist etwas ganz anderes als im Sinne der Codezeilenzählung zu
verarbeiten; zu verarbeiten ist etwas ganz anderes als anzuzeigen; und
auch anzuzeigen ist etwas ganz anderes als zu parsen.
Schon unter Unix war es möglich, sich selbst aus kleinsten, ganz ver-
schiedenen Programmen Verarbeitungsprozesse auf der Kommandozeile
zusammenzusetzen. Das war ein Teil der Attraktivität von Unix. Insofern
würdeichsagen,dassUnixderVorreitervonserviceorientiertenArchitek-
turen war. Die heutigen Microservices tragen die Idee nur ins Web - und
machen es dabei noch nicht so einfach wie Unix.
AberwillstduwirklichdieobigeKommandozeileimmerwiederhinschrei-
ben, um Quellcodedateien auszuwerten? Nein, du willst es bequemer


---


<!-- Page 222 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 213
haben. Deshalb schreibst du ein Programm, das diese Teile integriert.
Unter Unix könnte das ein Bash-Script loccounter.sh sein, das die
Kommandozeile enthält. Oder es könnte eben auch ein C#, Java, Python
Programm sein, in dem Funktionen, die parsen, verarbeiten und anzeigen
integriert werden.
Egal, mit welcher Plattform du arbeitest, ob du Programme oder Funktio-
nen integrierst, du “komponierst” aus verschiedenen Funktionseinheiten
etwas Neues. Die verschiedenen Funktionseinheiten sind sozusagen kom-
plementär. Sie ergänzen einander zu einem Ganzen. Dass sie verschieden
sind, ist essenziell. Zusammengefasst bieten sie in ihrer Verschiedenheit
etwas Bequemeres und Verständlicheres auf höherer Ebene.
Composition rulez!
Unsere zivilisatorischen Errungenschaften, unseren Fortschritt verdanken
wir Kompositionen.
Komposition bringt Bequemlichkeit. Aber Übersichtlichkeit bringt sie
nicht. Das ist auch eigentlich nicht ihr Zweck. Sie soll Nutzen herstellen,
nicht Ordnung.
Denk an ein Kinderzimmer oder an die Küche. Wie wird da Ordnung
hergestellt? Findest du in einer Küche je einen Teller mit Messer, Gabel,
Löffel und einem Glas nebeneinander? Findest du im Kinderzimmer je
eine Hose, zwei (gleichfarbige) Socken, ein T-Shirt beieinander? Nein. Das
ist nicht unsere Vorstellung von Ordnung.
Einen Teller mit Messer, Gabel, Löffel und Glas findest du auf einem
gedeckten Tisch. Das ist sogar die Definition von gedecktem Tisch. An
einen gedeckten Tisch kann man sich setzen und essen. Alles ist bereit für
die Nutzung. Das ist bequem. Ein gedeckter Tisch ist eine Komposition;
und wenn das Essen noch schmeckt, ist er ein Gedicht. Das erwarten wir
in einem Restaurant und bezahlen dafür.
Unsere Vorstellung von Ordnung in einer Küche oder im Kinderzimmer
istabereineandere.DorterwartenwirkeineKomposition,sondernAggre-
gation. Wir erwarten, dass gleichartige Dinge zusammengefasst werden.
Abstraktion erfolgt hier nach Ähnlichkeit, nicht nach Unterschiedlichkeit.
Als Beispiel eine Tüte mir Süßigkeiten:


---


<!-- Page 223 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 214
Die Tüte ist eine Komposition. Sie bietet dir in handlicher Form einen
vielfältigen Genuss. Das ist das Versprechen von Haribos Color-Rado
Mischung.
Wenn du die Tüte auskippst, kullert dir allerdings Chaos entgegen. Was
in Summe gut schmeckt, ist auf einem Haufen unübersichtlich. Wenn du
zumBeispielamliebstenGummibärchenausderMischungisst,dannhast
du es schwer, die zu finden. Dito, wenn du am liebsten Lakritz magst.


---


<!-- Page 224 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 215
Umgezieltaufdaszuzugreifen,wasduhabenwillst,istKompositionnicht
die passende Abstraktion. Dafür willst du eine Aggregation haben, in der
die Dinge nach Ähnlichkeit zusammengefasst sind. Hier ein Beispiel:


---


<!-- Page 225 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 216
Die Gummiteile sind hier zusammengefasst nach grundsätzlicher “Art”:
es gibt “Gummiteile”, Lakritz - und eine Mischung aus “Gummiteil” und
Lakritz, die Fledermaus. Wer kein Lakritz mag, wie ich, der freut sich über
solcheAggregationen.IndieserOrdnungmussichnichtlangesuchen,um
ein Teil zu finden, das ich mag.
Ordnung liegt allerdings im Auge des Betrachters bzw. Ordners. Der
bestimmt, was die Ordnungskriterien sind. Es gibt für die Color-Rado Mi-
schungkeineabsolute,perfekte,alleinseligmachendeOrdnung.Vielmehr
bestimmt der Zweck die Ordnung. Wenn ich grobe Geschmacksklassen
bequem bedienen will, dann ist die obige Ordnung hilfreich. Wenn ich
hingegen eher einen betrachtenden Ästheten befriedigen will, dann könn-
te die folgende Ordnung mehr Zustimmung finden:


---


<!-- Page 226 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 217
Hier sind die Teile nach Farbe aggregiert. Egal, welchen Geschmack sie
haben, egal, welche Konsistenz sie haben, auf einem Haufen liegen die
TeilenuraufgrundihrerFarbe.Dasistgenauso“richtig”,wiedievorherige
Ordnung. Es wird einfach ein anderer Zweck verfolgt.
Aber es geht auch noch anders. Erkennst du, was hier das Ordnungskrite-
rium ist?


---


<!-- Page 227 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 218
Was ich dir mit diesen Variationen von Ordnungen deutlich machen will:
Die Ordnung entsteht durch Zusammenfassung von Ähnlichem. Was das
Kriteriumist,seidahingestellt.InjedemFallkannmandenTeilenansehen,
ob sie es erfüllen. Jedes für sich kann der einen Aggregation oder der
andere zugeordnet werden.
Bei Kompositionen liegt die Zugehörigkeit nicht im einzelnen Element,
sondern in den Beziehungen der Elemente zueinander. Parsen muss
zu Verarbeiten muss zu Anzeigen passen im Sinne eines Ganzen.
Im letzten Aggregationsbeispiel muss jedoch nur das eine Teil zu einer
Aggregation passen und das nächste Teil ebenfalls usw.
Kompositionen sind Operationen und Integrationen. Aggregationen hin-
gegen sind Kategorien. In den Bildern sind Color-Rado Teile also unter-
schiedlich kategorisiert. Dadurch sind Ordnungen für bestimmte Zwecke
entstanden.
In einer Küche sind die Dinge auch in dieser Weise kategorisiert. Du
findest alle Messer zusammen und alle Gabeln und alle Löffel und alle
Teller.UndGabeln,Messer,Löffelsindnochmalzusammengefasstineiner
Besteckschubalde, die getrennt ist vom Regal, auf dem die Teller stehen.
Und die Teller stehen näher bei den Müsli-Schalen als bei den Gabeln.


---


<!-- Page 228 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 219
Du fühlst es vielleicht schon: Kategorien können Hierarchien bilden! Um
Ordnung in viele Dinge zu bekommen, bilde ich Kategorien. Denen ordne
ich die Dinge zu (oder unter). Wenn es aber mehr und mehr Kategorien
gibt, dann verliere ich auch bei denen den Überblick. Also kategorisiere
ich Kategorien. Usw. usf. in beliebiger Tiefe.
Küche selbst ist eine Kategorie. Die fällt unter die Oberkategorie Funkti-
onsbereiche oder so.
• Küche
– Besteck
* Gabel
* Löffel
* Messer
– Geschirr
* Teller
* Schale
* Tasse
– Kochgeschirr
* …
• Kinderzimmer
– …
Innerhalb der Küche gibt es dann Werkzeugkategorien wie Besteck oder
Tassen,diemehroderwenigerumfassendsind.DukannstaufjederEbene
weitere Kategorien daneben stellen, z.B. Glas bei Geschirr, oder Unterka-
tegorien bilden, z.B. zwischen Teelöffel und Esslöffel unterscheiden. Oder
Teelöffel und Kuchengabeln unter Kuchenbesteck zusammenfassen unter
Besteck.
Kompositionen bilden eine Hierarchie, denn nur so bekommt man die
wachsende Menge an Bauteilen in den Griff, um neue Höhen in der
Bequemlichkeit zu erklimmen. Und Aggregationen bilden ebenfalls eine
Hierarchie, um neue Höhen in der Ordnung zu erklimmen.
Aber wofür solche Ordnung? Wofür das Ähnliche zusammenfassen? Ich
denke, es gibt mindestens zwei Gründe:


---


<!-- Page 229 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 220
• Vor allem willst du kategoriale Ordnung für die nächste Kompo-
sition. Wenn du wieder mal etwas Neues “komponieren” musst,
dann willst du schnell einen Überblick darüber bekommen, welche
Bauteile dir zur Verfügung stehen. Beispiel Opernbesuch: Wenn
du in die Oper gehst, dann willst du auf einen Blick sehen, was
deine Kleidungsoptionen sind. Was steht zur Auswahl in Bezug auf
Anzug/Kleid,Schuhe,Schmuckusw.DugehstdieKategoriendurch,
die zu einer Abendgarderobe (ebenfalls eine Kategorie!) gehören
und schaust, was dazu im Schrank ist.
• Aber du willst auch kategoriale Ordnung, um Optimierungen
vornehmenzukönnen.Wenndudas,waszueinerKategoriegehört,
vordirsiehst,kannstdufeststellen,wasdaistoderwasfehltoderob
es Dopplungen gibt. Du kannst z.B. feststellen, dass manche deiner
Töpfe auf einem Induktionsherd funktionieren, aber andere nicht.
DaskanndieKaufentscheidungfürdennächstenHerdbeeinflussen
- oder für weitere Töpfe.
Die Zahl der Funktionen in deiner Anwendung wächst ständig. Neue
Anforderungen wollen erfüllt werden. Du brauchst also ein Mittel, um
Ordnung in die Funktionen zu bringen. Du musst sie kategorisieren
können.
Physisch kategorisieren mit dem Dateisystem
Nun könntest du denken, dass die Kategorisierung doch eigentlich ganz
einfachist.DieKategorienbildeneineHierarchieundaufdeinemRechner
gibt es ein altbewährtes Mittel, um Hierarchien aufzubauen: das Datei-
system. Warum also nicht einfach Funktionen, die zu einer Kategorie
gehören, in einer Datei zusammenfassen? Warum nicht Dateien, die zu
einer höheren Kategorie gehören, in einem Verzeichnis zusammenfassen?
Warum nicht Verzeichnisse, die zu einer noch höheren Kategorie gehören,
wiederum in einem Verzeichnis zusammenfassen?
Das ist tatsächlich keine schlechte Idee. Behalte das im Hinterkopf. Du
wirstdieseFormderphysischenKategorisierungbrauchenkönnen.Damit
würdest du deine Funktionsmenge auf eine Menge Datei- und Verzeich-
nishaufen verteilen, um den Überblick zu behalten - doch ansonsten wäre
nichts gewonnen. Letztlich wäre es egal, in welcher Datei in welchem Ver-
zeichnis eine Funktion definiert wäre. Alle Funktionen wären in gleicher
Weise verfügbar, d.h. in Integrationen einsetzbar.


---


<!-- Page 230 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 221
Wäre das schlimm? Das wäre besser als nichts. Du könntest schon für
die bisherigen Übungsaufgaben überlegen, auf welche Quellcodedateien
die Funktionen verteilt werden könnten. Was wären Kriterien für die
Ähnlichkeit?¹²⁷
Wenn du aber genauer hinschaust, ist diese Gleichmacherei zu pauschal.
Auch wenn Funktionen nach einem Kriterium ähnlich sind - z.B. haben
einige Funktionen mit dem Datenbankzugriff zu tun -, bedeutet das nicht,
dass sie alle gleich “wichtig” sind. Nicht alle sollten von allen anderen
Funktionen in anderen Dateien aus genutzt werden können. Manche
Funktionen sind wichtiger und haben eine andere Reichweite als andere.
Um diese zusätzliche Unterscheidung abzubilden, braucht es mehr als
physische Kategorien mittels Dateien und Verzeichnissen. Es braucht
Unterstützung vom Compiler. Es braucht Syntax und Semantik.
Module
Du willst Funktionen nicht nur kategorisieren, also überhaupt “in Töpfen
zusammenfassen”, sondern auch noch innerhalb der Kategorien “gewich-
ten”. Manche Funktionen sind wichtiger als andere; manche Funktionen
sind besonders stellvertretend für eine Kategorie, andere sind nur not-
wendige Details, die jenseits einer Kategorie eigentlich keine Bedeutung
haben.
Kategorien sollen also Kapseln sein, die eine spürbare Oberfläche haben,
über die man sie nutzen kann - und gleichzeitig haben sie ein Innenleben,
das privat ist.
Wenn du 1000 Funktionen hast, dann fallen die vielleicht in 50 Kategorien.
Solange die Kategorien aber nicht kapseln können, sind für 1 Funktion in
einerKapselimmernoch999anderegrundsätzlichsichtbarundpotenziell
relevant.AuchmitKategorienistdaseinegroßeZahl,umbeidernächsten
KompositiondierichtigeFunktionzufinden.WennaberproKategorienur
vielleicht im Durschnitt 8 Funktionen wichtig wären… dann wären für 1
¹²⁷Dass das nicht in allen Programmiersprachen so funktioniert, sei in diesem Moment
vernachlässigt. In C# oder Java kann ich nicht einfach ein paar Funktionen in eine Datei
packenundvonFunktioneninanderenDateienausnutzen.AlleFunktionenmüssenineiner
Klassedefiniertsein.


---


<!-- Page 231 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 222
Funktion in einer Kategorie aus anderen lediglich 392 Funktionen noch
relevant und sichtbar. Das wäre eine erhebliche Reduktion!
Module sind für mich nun die strukturellen und syntaktischen Einheiten,
die eine solche Reduktion erlauben.
Module fassen Funktionen einer Kategorie zusammen und erlauben
es,diesegegenüberanderenModulenzuverbergenoderzuveröffent-
lichen. Module sind Container für Funktionen mit einem Kontrakt.
Der Kontrakt besteht aus den sichtbaren Funktionen.¹²⁸
Kontrakt nenne ich die Menge der Veröffentlichungen, weil sie ein Ver-
sprechen darstellen. An das Öffentliche können sich nämlich andere
Module binden. Sobald das geschieht, sobald Abhängigkeiten aufgebaut
sind zu Veröffentlichungen, musst du bei der Veränderung des veröffent-
lichenden Moduls vorsichtig werden. Jede Änderung gefährdet potenziell
alle abhängigen Module.
¹²⁸Warum Kontrakt und nicht Interface? Im allgemeinen Sprachgebraucht mag man
KontraktundInterfacesynonymverwerden.DaesinProgrammiersprachenaberSprachkon-
strukte gibt, die Interface genannt werden, möchte ich hier einen etwas unverbrauchteren
Begriff benutzen. Außerdem betont Kontrakt für mich mehr, das worum es geht: eine
Verpflichtung. Die Begriffe Interface und Schnittstelle beschreiben nur die Funktion. Mit
KontraktzieleichmehraufdieBedeutung.


---


<!-- Page 232 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 223
Syntaktische Container für Funktionen nenne ich Module, weil sie un-
abhängig von physischen wie Datei oder Verzeichnis definiert werden
können. In manchen Sprachen mögen sie zusammenfallen, in anderen
können mehrere Module jedoch z.B. in derselben Datei definiert sein,
in wieder anderen kann sich dasselbe Modul womöglich über mehrere
Dateien erstrecken.
Abhängigkeiten
Da sind die wieder, die Abhängigkeiten. Die kennst du schon von den
Funktionseinheiten der Datenflüsse: funktionale Abhängigkeiten sind zu
vermeiden, aber Abhängigkeiten allgemein lassen sich nicht vermeiden.
Abhängigkeiten sind nötig, wenn wir Bequemlichkeit und Überblick
durch Hierarchie gewinnen wollen. Integrationen sind also bewusst und
unvermeidbar abhängig von dem, was sie integrieren.
Wenn nun Funktionseinheiten in verschiedenen Modulen aggregiert wer-
den, passiert es zwangsläufig, dass Funktionseinheiten im einen Modul
von Funktionseinheiten in anderen Modulen abhängig wird. Übertragen
auf die umschließenden Module bedeutet das, dass diese Module indirekt
voneinander abhängig werden. Doch das ist eben nur eine Abstraktion; in
Wirklichkeit sind es die Funktionseinheiten in den Modulen.


---


<!-- Page 233 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 224
Abhängigkeiten haben nun zwei Seiten: die abhängige und die unabhän-
gige, von der die abhängige abhängig ist.
Abhängig zu sein, ist zunächst mal keine schöne Sache, nicht in deinem
persönlichen Leben und auch nicht in der Softwareentwicklung. Wer
abhängig ist, muss mit reduzierten Freiheitsgraden auskommen. Wer
abhängig ist, ist anfällig dafür, unter Veränderungen dessen zu leiden,
von dem er abhängig ist. Wer abhängig vom monatlichen Gehaltseingang
in voller Höhe auf dem Konto ist, hat ein Problem, wenn Kurzarbeit
angeordnet wird oder er sogar entlassen wird. Wer abhängig von Nikotin
ist, hat ein Problem, wenn sich die Zigarettenschachtel unerwartet als leer
entpuppt, wenn der Drang zu einer Zigarettenpause steigt.
Manche Abhängigkeitsverhältnisse kann man recht gut kontrollieren, z.B.
indem man darauf achtet, immer rechtzeitig eine volleZigarettenpackung
zu kaufen. Deshalb steckt in Hotelzimmern auch stets eine zweite Toi-
lettenpapierrolle neben der Toilette. Andere Abhängigkeiten lassen sich
nur schwer oder gar nicht kontrollieren, z.B. die vom Gehaltseingang;


---


<!-- Page 234 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 225
da kann man höchstens etwas auf grundsätzlicherer Ebene tun, indem
man z.B. ein frugales Leben führt oder Ersparnisse hat oder ein breites
Kompetenzspektrum für größere Arbeitsmarktattraktivität.
Abhängigkeitenlassensichnichtgrundsätzlichvermeiden.Aberdukannst
mit ihnen bewusst umgehen auf beiden Seiten des Abhängigkeitsverhält-
nisses. Lass uns einen genaueren Blick darauf werfen. Dafür will ich
dem Unabhängigen aber einen anderen Namen geben. Das Unabhängi-
ge ist nämlich nicht wirklich frei, wie man meinen könnte. In vielen
Verhältnissen steht das Unabhängige nämlich in einer Pflicht. Indem es
sich angeboten hat für eine Abhängigkeit, hat es Verantwortung für das
Abhängige übernommen. Das beste Beispiel dafür sind Eltern: Kinder
sind abhängig von ihren Eltern, die Eltern sind aber nicht abhängig von
ihren Kindern; Eltern sind unabhängig. Allerdings: Eltern haben eine
Verantwortung für das Wohlergehen ihrer Kinder. Das gehört dazu, wenn
man sich für Kinder entscheidet. Eltern gehen also eine Verpflichtung ein,
ihren Kindern in deren Abhängigkeit zur Verfügung zu stehen. Damit
schränken Eltern ihre grundsätzliche Freiheit ein.
Abhängigkeit und Verpflichtung kommen immer dann zusammen, wenn
es einen Kontrakt zwischen der abhängigen und der unabhängigen Partei
gibt. Man kann auch von Berechtigtem und Verpflichtetem sprechen.
Bei Kaufverträgen ist so ein Verhältnis sogar bidirektional: der Käufer
hat nach Vertragsabschluss ein Recht auf die Ware, zu deren Lieferung
der Verkäufer verpflichtet ist. Umgekehrt hat der Verkäufer ein Recht auf
Bezahlung, zu deren Leistung der Käufer verpflichtet ist.


---


<!-- Page 235 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 226
Zwischen Funktionseinheiten in der Software ist das Verhältnis zum
Glück simpler; es ist immer nur unidirektional.
Trotzdem gilt es vorsichtig zu sein auf beiden Seiten der Abhängigkeit.
Denn auch hier könnte man sagen: Die Dosis macht das Gift.
Services stabilisieren
Zunächst eine wachsende Anzahl von Abhängigkeiten - einem wach-
senden fan-in, die ein grundsätzlich Unabhängiges zugelassen hat. Das
Unabhängige leistet etwas für die vielen Abhängigen, es stellt also einen
Service dar.


---


<!-- Page 236 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 227
Du könntest denken, das sei kein Problem für das Unabhängige, weil
es ja unabhängig ist. In der Realität ist das aber nicht der Fall, weil es
sich bei den Abhängigkeiten um Kontrakte handelt. Der Service hat ein
Versprechen in den Raum gestellt und viele nun Abhängige haben ihn
damiternstgenommen.DievielenAbhängigensindjetztseineClientsund
bauen darauf, dass der Service sein Versprechen auch in Zukunft einhält.
Das Problem für einen Service in vielen Verpflichtungen ist, dass er nun
große Verantwortung trägt. Er muss sich um Stabilität bemühen in Bezug
auf existierende Kontrakte, wann immer Veränderungen in ihm anstehen.
Je größer der fan-in und auch je unbekannter die Kontraktpartner, desto
größer die Stabilitätspflicht. Das macht das Dilemma von öffentlichen
APIs aus: Sie sollen sich einerseits weiterentwickeln, andererseits gibt
es womöglich eine riesige und dazu unbekannte Zahl von Clients, die
darauf bauen. Wie APIs Veränderung ohne Pflichtverletzung aufgebaut
und versioniert werden können, ist deshalb immer wieder Thema in der
Literatur.
Um den Problemen eines großen fan-in¹²⁹ aus dem Weg zu gehen, kannst
du einen Service bewusst ab einem gewissen Punkt einfrieren. Und wenn
du das nicht selbst tust, passiert das ohnehin früher oder später; große
Verpflichtungen führen zu großer Vorsicht die sich in Bewegungsreduk-
tion ausdrückt. Verknöcherung und Atrophie kommen hier zusammen.
Also überlege dir, ob du den Stier nicht bei den Hörnern packst. Statt
ewiger immer schmerzvollerer und unbefriedigenderer Veränderung als
Schrecken ohne Ende besser ein Ende mit Schrecken.
Ich ahne, dass dir dieser Vorschlag nicht gefällt. Du kannst dir nicht
¹²⁹Du könntest fan-in sogar mit “Fangemeinde” übersetzen. Denn Fans z.B. einer Band
erwarten von ihr auch Konstanz in dem, was sie bei Auftritten oder in neuen Alben liefert.
Dass eine Band, ein Künstler mit einer großen Fangemeinde drastisch den Stil ändert, ist
auchdeshalbeherselten.DerbisherigeErfolgwürdeaufsSpielgesetzt.


---


<!-- Page 237 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 228
vorstellen,dassdasgeht.DabeipassiertdasmitjedemGeschirr-Set:Esgibt
nur eine begrenzte Nachkaufgarantie. Man muss nur wollen. Ressourcen
können nicht für alle Angebote ewig vorgehalten werden.
Aber ich schlage dir noch eine andere Strategie vor: reduziere die Wahr-
scheinlichkeit, dass überhaupt eine Änderung notwendig wird.¹³⁰
Jeweniger“Angriffsfläche”einServicefürVeränderungsgründehat,desto
höher seine natürliche Stabilität und einen desto größeren fan-in kann er
verantwortungsvoll bedienen.
Darauf zielt z.B. das Dependency-Inversion Principle (DIP)¹³¹ ab, das am
häufigsten zitiert wird mit:
“Details (concrete implementations) should depend on abs-
tractions.”
DieAnnahmedahinter:EineAbstraktion,dieUnterschiedeimAbstrahier-
ten ausgleicht, d.h. Details verbirgt bzw. übertüncht, ist von Natur aus sta-
biler als all ihre Elemente. Konkret wird das immer wieder übersetzt mit
Abhängigkeiten von Interfaces statt von sie implementierenden Klassen.
Doch auch das IOSP ist ein hilfreiches Prinzip in dieser Hinsicht. Hättest
dudasgedacht?Dennwaspassiert,wennduindeinerCodebasisdasIOSP
beachtest? Erstens wandert die Logik in die Blätter, zweitens werden die
Funktionen sehr klein.
Logik ist das, was besonders anfällig für Veränderung ist: darin stecken
oft Fehler; sie muss oft für neue Features angepasst werden. Wo aber
wenig Logik “auf einem Haufen liegt”, ist die Wahrscheinlichkeit gering,
dass etwas daran verändert werden muss bzw. dass die Veränderung
tiefgreifend ist.
In Bezug auf ihre “Fans” gilt das auch für Integrationen. Sie sind klein und
“ausstrahlende” Veränderungen sind unwahrscheinlich. Außerdem bieten
sich mit Integrationen auf jeder Ebene Möglichkeiten, Instabilitäten ge-
genüber ihren Clients zu kompensieren, wenn von ihren Services welche
“ausstrahlen” sollten.
¹³⁰GenaugenommenistEinfrierensogarnureinSonderfalldieserallgemeinenStrategie.
¹³¹https://en.wikipedia.org/wiki/Dependency_inversion_principle


---


<!-- Page 238 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 229
Mit dem IOSP kommst du also zu Funktionseinheiten an der Basis, von
denen zwar viele andere potenziell abhängig sein können, die jedoch ver-
gleichsweise wenig Angriffsfläche für Veränderungen bieten. Integratio-
nen und Operationen in einer IOSP-Funktionshierarchie sind viel stabiler
als die üblichen hybriden Funktionen von 100, 300, 1500 Zeilen Länge.
Wenn also schon Abhängigkeiten unvermeidbar sind, dann bitte in einer
IOSP-Hierarchie.
Clients immunisieren
Die Abhängigen von Services sind ihre Clients. Für sie besteht das Risiko
von wachsendem fan-out an Abhängigkeiten:
Über jede Abhängigkeit kann eine Instabilität eines Service auf den Client
einwirken und ihn zu einer Veränderung zwingen. Ein Prinzip, das dem
entgegenwirken will, ist z.B. das Interface Segregation Principle (ISP)¹³²:
“[N]o client should be forced to depend on methods it does
not use. ISP splits interfaces that are very large into smaller
and more specific ones so that clients will only have to know
about the methods that are of interest to them.”
Es reduziert die Abhängigkeiten durch ein Angebot spezifischerer Ser-
vices; Clients können sich für maßgeschneiderte Leistungen entschei-
den, statt sich von umfassenden abhängig zu machen. Das reduziert
die Wahrscheinlichkeit, dass in ihrem Nutzungsausschnitt eines Service
¹³²https://en.wikipedia.org/wiki/Interface_segregation_principle


---


<!-- Page 239 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 230
eine Instabilität auftauch. Ihr Service mag instabil sein - aber in für sie
irrelevanten Bereichen.¹³³
Das IOSP hilft auch hier. Mit Integrationen lassen sich für alle möglichen
Szenarien spezifische Funktionseinheiten “komponieren”. Das tun Ope-
rationen ohnehin, das tun aber auch Integrationen. Die sind “so billig”
(allemal in ihrer Form als Sequenz von Funktionsaufrufen), dass du dir für
jeden Zweck eine maßgeschneiderte Integration zusammenstellen kannst,
statt im Client ein breites Service-Interface selbst zu nutzen.
Aber was wird durch eine Service-Instabilität denn eigentlich bedroht?
Es ist vor allem wieder Logik. Wenn Logik in einem Client von Logik
in einem Service abhängig ist, also eine funktionale Abhängigkeit be-
steht, dann ist wirklich Gefahr im Verzug. Die Logik im Client existiert
in prekären Verhältnissen, weil sie ständig bedroht ist durch mögliche
Instabilitäten ihrer Services.
Dem gehst du ebenfalls mit dem IOSP aus dem Wege. Darin gibt es keine
funktionalen Abhängigkeiten mehr; das Risiko für eine Integration, durch
eine Veränderung in einem Service beeinträchtigt zu werden, ist deutlich
geringer als bei einer hybriden, funktional abhängigen Funktion.
Orthogonale Containerdimension
Module fassen Funktionen zusammen; sie abstrahieren von deren Un-
terschieden im Hinblick auf ein Kriterium; sie aggregieren Funktionen
unter einem neuen Begriff. Aber sie bilden nicht nur Namensräume,
sondern definieren Kontrakte. Sie machen damit Versprechen über ein
Leistungsangebot, das von anderen Modulen angenommen werden kann.
Es entstehen direkt kontraktuelle Abhängigkeiten zwischen Funktionen
verschiedener Module. Die Abhängigkeiten der Module voneinander hin-
gegen sind nur indirekt.
Was damit entsteht ist eine weitere, zu den 2-dimensionalen Datenflüssen
orthogonale Dimension:
¹³³Module selbst mit ihren Kontrakten, also der Menge öffentlicher Funktionen, sind die
Grundlagebzw.derallgemeineFalldesISP.IndemduüberhauptFunktionenineinemModul
und nicht nur einem Namensraum versammelst und lediglich einige öffentlich machst,
definierstdueinerstesInterface,dessenUmfanggeringeristalsdieMengeallerFunktionen.
Das ist das default Interface eines Moduls. Das ISP baut darauf auf, indem es vorschlägt
selbsteinModul-InterfacenochfürunterschiedlicheZweckeweitereinzuschränken.


---


<!-- Page 240 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 231
Komposition und Aggregation sind die zwei wesentlichen Dimensionen,
in denen du Logik organisierst.
Aber wozu Aggregation? Komposition hebt Funktionalität auf immer
höhere Ebenen; sie stellt Bequemlichkeit her. Was leistet demgegenüber
Aggregation? Abstraktion ist irgendwie immer eine gute Sache, doch
wozu diese Form der Abstraktion in Bezug auf Ähnlichkeit?
Es geht um Kontrolle. Das ist wie mit Abteilungen in Unternehmen.
Angestellte sind zunächst und vor allem in Abteilungen organisiert in
Unternehmen, um sie zu kontrollieren. Man behält sie besser im Blick,
man kann sie besser in eine Richtung lenken. Hier ein typisches Bild aus
dem Film The Apartment¹³⁴, als Abteilungen noch besser sichtbar waren:
¹³⁴https://youtu.be/x356ll3hTxg


---


<!-- Page 241 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 232
Alle Angestellten mit ähnlicher Tätigkeit sind in einem Großraumbüro
aggregiert. Und am Kopf des Raumes sitzt der Bürovorsteher oder sogar
Abteilungsleiter. Der hat den Überblick. Und das Organigramm¹³⁵ gibt
den Überblick über die “Kontrollstrukturen” und ist insofern selbst eine
“Kontrollstruktur”:¹³⁶
Die Hierarchie der Aggregationen im Unternehmen sieht z.B. so aus:
• Unternehmen
– Unternehmensbereich
* Abteilung
¹³⁵https://de.wikipedia.org/wiki/Organigramm
¹³⁶Bildquelle:Sprenger,CCBY-SA3.0


---


<!-- Page 242 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 233
· Gruppe¹³⁷
Die Aggregationen als Kategorien dienen nicht der Herstellung von
Ergebnissen. Das geschieht in Prozessen quer zu den Kategorien. Daten-
flusshierarchien repräsentieren Herstellungsprozesse. Module wie Abtei-
lungen sind vielmehr die Verantwortlichkeitsstrukturenfür grundlegende,
prozessübergreifende Aspekte im Rahmen einer Software bzw. eines
Unternehmens.
In Abteilungen hat man ähnliche Kenntnisse - Verkaufsabteilung, Mar-
ketingabteilung, Entwicklungsabteilung, Buchhaltung usw. -, erfüllt also
denselben “Daseinszweck”. Außerdem teilt man sich Ressourcen, die für
die Erfüllung des Zwecks nötig sind, z.B. braucht die eine Abteilung
einen Abteilungsdrucker, die andere aber einen Abteilungsscanner und
die Dritte Werkbänke. Insofern haben Abteilung auch den Zweck der
BündelungvonRessourcen.EffizienzistdieTriebfederhinterAbteilungen
- und auch Modulen.
AufderanderenSeiteistdieTriebfederhinterDatenflüssenEffektivität.Es
soll das Richtige getan werden, das, was für den Anwender Wert darstellt.
Datenflüsse sind Wertschöpfungsketten über Module hinweg.
Im Flow-Design wird Code als organisiert in einer Matrix aufgefasst:
Datenflusshierarchieund Modulhierarchie zusammen stellen die Gesamt-
ordnung her.
¹³⁷Eine Gruppe innerhalb einer Abteilung ist übrigens nicht zu verwechseln mit einem
Team. Ein Team ist eine cross-funktionale oder besser cross-kategoriale Einheit, die einen
Prozess repräsentiert. Das hat für die Softwareentwicklung die Agilität erreicht: Sie hat
deutlich gemacht, dass Entwicklung nicht effizient und effektiv genug voranschreitet,
wenn ständig Abteilungsgrenzen zu überwinden sind. Ein agiles Team ist deshalb eine
KompositionausMenschen,dieganzunterschiedlicheRollenspielen/Fähigkeitenhaben.


---


<!-- Page 243 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 234
Zu jeder Funktion(seinheit) lässt sich also fragen: In welchem Modul ist
sie defininiert und zu welchen Datenflüssen gehört sie. Welchem Zweck
dient sie und wo erfüllt sie diesen in Prozessen?
Die Modul-Hierarchie
Die Funktionseinheiten, die du in Datenflüssen wertschöpfend “kompo-
nierst” kannst du also in Modulen zusammenfassen. Das ist grundsätzlich
sehr schön, stößt aber schnell an seine Grenzen, wenn das nur auf einer
Ebene geschehen kann. Über wie viele Funktionen kannst du mit einem
Modul “die Kontrolle behalten”, also einen Überblick haben und die Res-
sourcennutzung optimieren? Sind das 5, 10, 25, 50 oder 100 Funktionen?
Egal wie viele, es sind immer viel, viel weniger als die Gesamtzahl deiner
Funktionen. Du wirst also mit wachsender Funktionenzahl auch eine
wachsende Modulzahl bekommen. Dann stellt sich die Frage: Über wie
viele Module kannst du eigentlich den Überblick behalten?


---


<!-- Page 244 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 235
Woraus das hinausläuft, hast du schon im Organigramm gesehen: Bei
steigender Zahl von Funktionseinheiten brauchst du eine Hierarchie von
“Kontrollstrukturen”oderKategorien.DubrauchsteineModul-Hierarchie.
Und diese Modul-Hierarchie ist am besten eine physische. Das Dateisys-
tem macht es vor: Dateien liegen physisch in Verzeichnissen, die physisch
in Verzeichnissen liegen usw. Mit einer geschachtelten Gliederung lässt
sich das hier im Text veranschaulichen:
• /Wurzelverzeichnis
– Unterverzeichnis1/
* Unterverzeichnis1.1/
· Datei1
* Datei2
– Unterverzeichnis2/
* Datei3
ImDateisystemkannstduVerzeichnisseöffnenundschließenimExplorer
(Windows)/Finder (macOS). Was du nicht sehen willst, “klappst du weg”.
So kannst du dich gut auf einen Kategorienzweig konzentrieren. Du
behältst auch den Überblick, weil du alle Unterebenen schließen kannst
und dann nur den direkten Inhalt eines Verzeichnisses siehst.
Unschön wäre es, wenn eine solche Hierarchie nur logisch wäre, wenn
also alle Hierarchieelemente physisch auf derselben Ebene lägen und man
ihren Inhalt analysieren müsste, um die Hierarchie zu (re)konstruieren.
Hat die folgende List dieselbe wie die vorstehende oder eine andere? Wie
lange brauchst du, um das zu erkennen?
• A/, parent:B/
• X, parent:F/
• F/, parent:A/
• S/, parent:B/
• Y, parent:S/
• B/, parent:
• Z, parent:A/


---


<!-- Page 245 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 236
Das Wurzelverzeichnis wäre hier z.B. nur als solches zu erkennen, weil es
keinen Verweis auf ein parent-Verzeichnis hat.
Um Code ausreichend modularisieren zu können, braucht es also eine
möglichst physische Hierarchie. Falls die dann nicht tief genug ist, um
Überblick zu bewahren zu könnnen - was zu erwarten ist, wenn Zehntau-
sende und mehr Funktionen zu organisieren sind -, muss darüber hinaus
noch logisch hierarchisiert werden. Das ist dann suboptimal, aber nicht
zu ändern.¹³⁸
Klasse - Abhängigkeiten mit Kontrakten zähmen
In der Objektorientierung stellen Klassen die unterste Ebene der Modul-
Hierarchie dar. In Klassen fasst du Funktionen direkt zusammen und
versiehst sie mit einer Sichtbarkeit (public, private oder sogar noch
differenzierter). Klassen bieten damit Leistungen im Rahmen eines Kon-
trakts an.
WennichfürdieNettocodezeilenzählungKlassensuchenwürde,indenen
ich Funktionen aggregieren will, würde ich z.B. auf Benutzerschnitt-
stelle{} kommen:
¹³⁸Das Verzeichnissystem ist zwar eine physische Hierarchie mit beliebiger Tiefe, bietet
fürsichgenommenaberkeineModularisierungsfeatures.EsmussalsoetwasinderProgram-
miersprachehinzukommen.


---


<!-- Page 246 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 237
1 class Benutzerschnittstelle {
2 public static string Parsen(string[] args) {...}
3
4 public static void Anzeigen(int nDateien, int mNettozeilen) {...}
5 }
Unddasistesfastschon,wassichüberdieModulebeneKlasse sagenlässt;
du bist mit ihr schon intim vertraut und kannst gar nicht ohne.¹³⁹ Sie ist
derunmittelbaresyntaktischeContainerfürFunktionen.Klassenspannen
einen Namensraum auf; sie geben Funktionen damit einen Kontext. Sie
machen es aber auch möglich, öffentliche Funktionen mit privaten zu
unterfüttern. Es kann eine interne Funktionshierarchie geben, die sich
beliebig verändern kann, ohne dass Abhängige es bemerken müssen.
Refactoring hinter der Fassade der öffentlichen Methoden ist jederzeit
möglich. Das default Interface entkoppelt die Umwelt von den Details
einer Klasse.
Hierarchische Modularisierung mit Klassen
Du wirst mich über Vererbung nur wenig schreiben sehen. Vererbung
ist ein Detail der Objektorientierung, dass ich für stark überbewertet
halte. Für den radikal objektorientierten Softwareentwurf halte ich sie
für nur wenig relevant. Sie hat ihren Platz, doch der ist für mich eher
am Rande der Bühne. In der Mitte stehen IOSP und PoMO und eine
physische Modulhierarchie. Und eine strickte Trennung von Daten- und
Serviceklassen.
Üblicherweise versteht man unter einer Klassenhierarchie eine Verer-
bungshierarchie. Die meine ich jedoch nicht, wenn ich hier Klassen in
einer Hierarchie anordne. Ich möchte dir vielmehr nahelegen, Klassen-
definitionen zu schachteln, wenn deine Programmiersprache das zulässt.
Definiere Klassen in Klassen:
¹³⁹In manchen OO-Sprachen kannst du technisch/syntaktisch ohne, aber das wirst du
nursehrseltennutzen,denkeich.DaswärejaprozeduraleProgrammierungundganz,ganz
gruselig. Oder? In anderen Sprachen gibt es keine Klassen, also keine “Vorlagen”, die sich
instanziieren lassen, aber immer noch syntaktische Container mit einem Kontrakt. In OO-
SprachenistdasÄquivalenteinestatische Klasse.


---


<!-- Page 247 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 238
1 class Parent {
2 class Child {
3 class Grandchild {
4 ...
5 }
6 ...
7 }
8 ...
9 }
Nutze diese Möglichkeit, um den Namensraum oder Container, in dem
Klassen existieren, nicht “vollzumüllen”. Durch physische Schachtelung
von Klassen kannst du auch ihre Sichtbarkeit begrenzen. Du verringerst
das Risiko “unabsichtlicher” Abhängigkeiten.
Die physische Schachtelung hat allerdings einen Nachteil für die Testbar-
keit. Du kommst an Methoden in geschachtelten Klassen nicht so leicht
ran, wenn sie sauber hinter Kontrakten verborgen sein sollen. Wenn du
mit Gerüsttests arbeitest wie in Test-first Codierung beschrieben, stört
dich das nicht so sehr - dennoch stehen beschränkte Sichtbarkeiten geziel-
ten Tests im Wege. Hier musst du abwägen, wie wichtig permanente Tests
sind im Vergleich zu einer verständlicheren Struktur. Das hängt von der
konkreten Codesituation ab. Ich möchte dir nur vermitteln, geschachtelte
Klassen nicht pauschal als Strukturierungsmittel auszuschließen.
Eventuell kannst du dir zumindest mit Namensräume und/oder Ansiede-
lung von Klassen in Dateien in verschiedenen Verzeichnisebenen helfen.
Sei kreativ bei der Strukturierung!
Kriterien für die Aggregation mit Klassen
Und wann solltest du Funktion(seinheit)en in Klassen zusammenfassen?
Was gilt als Gemeinsamkeiten? Meine Empfehlung: Suche möglichst
formale Kriterien und versuche, auf dein Bauchgefühl erst zum Schluss
zu hören. Formale Kriterien sind solche, bei denen du “an der Form” von
Funktionen erkennen kannst, ob sie ihnen genügen; du musst dann nicht
verstehen, was sie tun, sondern nur sehen, dass es ein “texttuelles” Muster
gibt.
• API: Ein sehr einfaches, formales Kriterium ist ein API, den ver-
schiedene Funktionen benutzen. Wenn Read() und Write() bei-
de mit dem MySql-API arbeiten oder beide die Konsole ansteuern,
dann gehören sie in dieselbe Klasse.


---


<!-- Page 248 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 239
• Zustand: Ebenfalls sehr einfach und formal ist es, die Funktionen
zusammenzufassen, die mit denselben in-memory Daten umgehen.
Push() und Pop() bei einem Stack sind dafür ein Beispiel: Beide
arbeiten auf derselben Datenstruktur, deren genaue Form sie vor
Clients verbergen. Sie definieren zusammen einen Abstrakten Da-
tentyp (ADT), weil man den realen nicht sieht.
• Integration: Wenn Funktion A() die Funktionen B() und C()
aufruft, ist das gut sichtbar und kann nahelegen, dass alle in einer
Klasse zusammengefasst werden. Vielleicht können B() und C()
dann sogar private gesetzt werden; das wäre ein Gewinn für die
Übersichtlichkeit.
Manchmal ist aber auch das Gegenteil der Fall. Wenn B() und C()
schon den Klassen S{} und T{} angehören, dann mag es besser
sein, A() in eine dritte Klasse zu legen, weil weder der einen, noch
der anderen schon existierenden Klasse die Integration der jeweils
anderen aufgebürdet werden sollte.
• Verantwortlichkeit: Nicht so einfach und nicht formal ist die
Aggregation nach Verantwortlichkeit, also nach dem SRP. Dafür
musst du die Anforderungen und den Code gut verstehen. Welche
Entscheidungen stehen hinter Funktionen, so dass ihre Zusammen-
fassung lohnt - ohne dass du das schon an API- oder Zustands-
Nutzung ablesen kannst? Ein Beispiel könnte das Mapping von
Datensein:WenndiePersistenzDateninderStrukturS{}anliefert
bzw. speichert, die Domäne aber mit Struktur T{} arbeiten will,
dann ist ein Mapping zwischen S{} und T{} nötig. S{} muss in
T{} und T{} in S{} gewandelt werden. Das geschieht z.B. mit
zwei Mapping-Funktionen. Die brauchen keinen API und haben
keinen Zustand, dennoch gehören sie aufgrund ihrer Verantwort-
lichkeit in eine Klasse. Die Klasse ist dann verantwortlich dafür, die
Entscheidung, dass Persistenz und Domäne mit unterschiedlichen
Datenstrukturen arbeiten, durchzusetzen.
• Aspekt: Aspekte sind für mich sehr allgemein und ganz grundle-
gendnichtvermischbareZwecke,z.B.Frontendvs,Backend,Testvs.
Produktion, Kern vs. Peripherie, Technik vs. Domäne, Monitoring
vs. Produktion, auch Integration vs. Operation, Verhalten vs. Daten.
Was zu einem Aspekt gehört, sollte zusammengefasst und von
anderen Aspekten getrennt werden. Dafür musst du aber natürlich
inhaltlich analysieren und auch dein Bauchgefühl mal walten las-
sen. Das betrifft auch Integration vs. Operation; beide sollten nicht


---


<!-- Page 249 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 240
zu pauschal getrennt werden; es gibt aber Gelegenheiten, wo genau
ihr Aspektunterschied eine Grenze zieht zwischen Funktionen und
sie auf verschiedene Klassen verteilt.
API und Zustand sind Kriterien, die unter gemeinsame Ressourcennut-
zung fallen. Ob die Ressource ein Hauptspeicherbereich ist oder durch
einen API repräsentiert wird, ist einerlei.
An dieser Stelle sind die Kriterien abstrakt für dich, glaube ich. Aber in
weiteren Modellen wirst du dafür Beispiele sehen.
Klassen als Datenstrukturen
Nun spreche ich die ganze Zeit von Funktionen, die mit Klassen zusam-
mengefasstwerdensollen.WasistdennabermitdenDaten?SindObjekte
alsInstanzenvonKlassennichtKombinationenausMethodenundDaten?
Hier sehe ich leider eines der größen Probleme der mainstream Objekt-
orientierung. Es wurde nicht genug darauf geachtet, diese beiden Aspekte
sauber zu trennen. Zu schnell wurde im Sinne eines naiven Weltverständ-
nisses Funktionalität mit Daten verschweißt. Hier ein repräsentatives
Beispiel¹⁴⁰, wie du Tausende im Internet findest:
¹⁴⁰https://www.tutorialspoint.com/system_analysis_and_design/system_analysis_and_
design_object_oriented_approach.htm


---


<!-- Page 250 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 241
“Employee” als Klassenname legt die Versammlung von Daten darunter
nahe. Und so ist es auch: Objekte der Klasse stehen für Angestellte mit
je eigenen Namen und Adressen. Damit fällt die Klasse Employee{} in
die Kategorie Datenstruktur oder Datenklasse. Eine Datenklasse steht
für Daten, eine Datenklasse ist Daten. Ihre Aufgabe ist es, die Daten
in gewisser Weise zu strukturieren. Hier wird z.B. eine Name mit einer
Adresse zusammengefasst, aber das Einstellungsdatum ist nicht dabei.
Und die Adresse besteht vielleicht aus weiteren Daten wie Straße und
Ort, die in Employee{} jedoch nicht direkt zu finden sind; dafür gibt es
vielleichteineeigeneDatenklasseAddress{}.DieAnordnungvonDaten
nebeneinander bzw. in der Tiefe, einzeln oder in Mengen, definiert eine
Datenstruktur.
Doch die Klasse Employee{} ist nicht nur eine Datenstruktur. Sie hat
eine zweite Verantwortlichkeit. Die werden repräsentiert durch ihre Me-
thoden wie Delete Employee() usw. Und damit beginnt der Grusel
der mainstream Objektorientierung! Das halte ich für einen Widerspruch
zum SRP und auch zum Separation of Concerns (SoC) Prinzip. Ganz naiv
gedacht, mag es irgendwie plausibel klingen, Daten und Operationen auf
Datenzusammenzufassen.Dochwenndugenauhinschaust,dannmüssen


---


<!-- Page 251 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 242
sich dir Fragen stellen wie:
• Warum sollte ein Objekt, das für einen Angestellten steht, einen
weiteren hinzufügen? Wozu hinzufügen? Warum also Add Em-
ployee()?
• Warum sollte ein Objekt sich selbst löschen? Warum die Methode
Delete Employee()?
Hier wird also nicht nur Funktionalität mit Datenstruktur vermischt, hier
werden auch noch einzelne Daten mit Datenmengen vermischt. Das ist
schlimm.
Damit dir das nicht passiert, empfehle ich ausdrücklich, dass die Daten-
klassen und Serviceklassen oder Verhaltensklassen voneinander trennst.
Klassen sind entweder Daten (Datenklassen) oder haben Daten (Service-
klassen).
Serviceklassen haben Daten insofern, als dass ihre Leistung auf Daten zu-
rückgreifenmuss.¹⁴¹EsistnichtihrHauptzweck,Datenzuhalten,sondern
das ist “zufällig” nötig. Diese Daten werden dann auch nicht nach außen
sichtbar gemacht. Sie sind Implementationsdetails. Serviceklassen haben
keine oder nur in Ausnahmefällen sichtbare Attributes/Properties/Fields.
ImDatenflusssiehstduDatenanzweiStellen:imFlussund“imStillstand”
als Abhängigkeiten (Zustand) von Funktionseinheiten. Integrationen in-
teressieren sich dafür eigentlich nicht selbst, sondern nur Operationen. In
ihnen ist die Logik, die die Daten transformiert.
¹⁴¹Ob diese Daten in-memory liegen oder aus einer Ressource beschafft werden müssen,
seidahingestellt.EineDatenbankklasseistalsoeineServiceklasseundkeineDatenstruktur.


---


<!-- Page 252 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 243
Operationen mit ihrer Logik sind also auf die eine oder andere Weise
abhängig von Datenstrukturen.
Um damit nicht gegen das IOSP zu verstoßen, dürfen Datenstrukturen
keine Logik enthalten. Sonst wären Operationen ja funktional abhängig
von der Logik in Datenstrukturen von denen sie abhängig sind.
DasIOSPsorgtalsodafür,dassDatenstrukturennichtauchnochmitLogik
aufgeladen werden. Eine Klasse wie Employee{} ist nach IOSP nicht
möglich.
Leider sind Klassen in OO-Sprachen die Mittel, um sowohl Funktionen
zu aggregieren zu umfassenderen Services, wie auch Daten zu bündeln
zu Datenstrukturen.¹⁴² Das Risiko ist damit hoch für dich, dass du die
Grenzziehungmalnichtsoguthinbekommst.Aberzumindestbistdujetzt
sensibilisiert.
¹⁴²Interessanterweise sind Serviceklassen in Bezug auf ihre Funktionen Aggregationen,
aber Datenklassen sind in Bezug auf ihre Daten Kompositionen. Eine Datenklasse fasst ja
Unterschiedliches zusammen, z.B. Name und Address zu Employee{} . Ein Angestellter
ist etwas Neues, etwas, das man bequemer handhaben kann, als einen Namen und eine
Adresseseparat.


---


<!-- Page 253 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 244
Abstrakte Datentypen
Dürfen denn Datenklassen wirklich gar keine Methoden haben? Wirklich
keine einzige? Eigentlich ja - und die Funktionale Programmierung kann
ja wunderbar damit leben. Andererseits wäre es schade, die Mittel der Ob-
jektorientierung für Daten so in den Wind zu schlagen. Ich finde es schon
sehr bequem, Methoden und Daten in einer Klasse zusammenzubringen.
Nur eben mit Bedacht.
Aus meiner Sicht gibt es daher drei Bedingungen für Logik in Methoden
von Datenklassen:
• Keine API-Aufrufe: Wer mit Datenklassen umgeht, muss nicht
gewärtigen,dassihreObjekteplötzlichheftigaufRessourcenzugrei-
fen. Das wäre überraschend und schlecht für die Verständlichkeit,
vor allem würde es aber die Operationen, die solche Datenobjekte
nutzen, schwer zu testen machen. Ganz zu schweigen davon, dass
dann auch die Datenklassen nochmal einen zusätzlichen Testauf-
wandbräuchten,derihreEntwicklungverzögern.Dasistabernicht
ratsam, weil Datenklassen zu Schnittstellen gehören; die sollten
zügig definiert sein, um die Arbeitsorganisation im Team zu verbes-
sern. Und schließlich: Datenklassen haben einen potenziell hohen
fan-in. Den können sie jedoch nicht verantwortungsvoll mit großer
Stabilität bedienen, wenn in ihnen Logik haust.
• Konsistenzsicherstellung: Logik in Datenstrukturen darf der Si-
cherstellungderKonsistenzderDatendienen.WenneinEmployee{}
nur mit einem Namen instanziiert werden darf, dann kann das
Logik im Konstruktor prüfen. Allerdings beschränkt sich die Kon-
sistenzsicherstellung auf die Struktur der Daten. Ob ein Name für
den Angestellten Sinn macht, liegt nicht in der Verantwortung der
Datenstrukturlogik zu prüfen.
• Datenzugriff: Außerdem darf die Logik in einer Datenstruktur
dem Zugriff auf die Daten dienen. Das tut sie z.B. mit Push()
und Pop() in einem Stack{}. Ein anderes Beispiel wäre die
Enumeration der Knoten in einem Baum in dept-first Reihenfolge.
Navigation in den Daten sowie CRUD-Operationen sind für mich
ok auf Datenstrukturen.
Wenn die Logik in einer Datenstrukturklasse also der Definition eines
Abstrakten Datentypen dient, dann sei es so. Zuerst ist da vielleicht nur


---


<!-- Page 254 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 245
eine Liste als primitiver Datentyp. Aber mit einer Datenklasse machst du
daraus eine stets sortierte Liste. Das passt.
Kriterien für instanziierbare Klassen
Datenklassen müssen instanziiert werden. Serviceklassen können instan-
ziiert werden. Können, müssen aber nicht. Wann aber sollten nun Ser-
viceklassen instanziiert werden? Oder wann kannst du statische Klassen
einsetzen?
Auch eine statische Klasse oder statische Methode kann ja wunderbare
Leistungen auf Daten in einem Fluss erbringen. Allerdings sind statische
Methoden/Klassen schon lange in Ungnade gefallen. Der Grund: Sie
verringern die Testbarkeit. Denn Abhängigkeiten zu statischen Methoden
lassen sich nicht mit Polymorphie zur Laufzeit ersetzen. Statische Klassen
erlauben keine Interfaces, auf denen DIP/IoC aufbauen.¹⁴³
Wennduaberwillst,hastduhiereinzweitesKriteriumfürinstanziierbare
Klassen: die Option, darauf ein explizites Interface definieren zu können.
Das erste Kriterium war Datenklasse. Das zweite ist Polymorphie via
Interface.
Polymorphie für bessere Testbarkeit über einen Austausch durch ein Sur-
rogatistüberalldorteinThema,woTestsbehindertwerdenwürden,wenn
ein Objekt “im Original” benutzt werden müsste. Das ist leicht der Fall
bei Klassen, die auf Ressourcen zugreifen (z.B. Datenbank, Drucker, Zeit),
also periphere Klassen. Mehr dazu im Kapitel über die IODA Architektur.
Ressourcen bzw. Seiteneffekte legen nahe, eine Klasse instanziierbar zu
machen.
EbensowirstduServiceklasseninstanziierbarmachen,wennsiein-memory
Zustandhaben.SiesinddannnochkeineDatenklassen,abersiebrauchen
eben doch welche über Nachrichtenverarbeitungen hinweg. Dazu zähle
ich auch die Konfigurierbarkeit. Mache Klassen stehen einem Test schon
weniger im Wege, wenn sie “nur” konfigurierbar sind; es braucht noch
¹⁴³Wenn du Funktionszeiger zur Verfügung hast, kann dir das zu einem Teil egal sein.
In der Funktionalen Programmierung gibt es ja auch keine Interfaces und niemand klagt
darüber. Aber Funktionszeiger sind in der OOP etwas Besonderes; da gibt es bei vielen
Entwicklern nicht so viel Erfahrung. Die Unterstützung dafür in OO-Sprachen ist auch
unterschiedlich: in C# gut, in Java nicht so gut. Mehr zum Thema Testen mit DIP/IoC und
SurrogatenimBandTest-firstCodierung.


---


<!-- Page 255 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 246
gar kein Interface für volle Austauschbarkeit; vielmehr reicht es, die
Instanziierung zu parametrieren.
Ein typisches Beispiel für mich ist in dieser Hinsich eine Datenbank-
zugriffsklasse. Solch ein Service kann für einen Test entschärft werden,
wenn er mit einem config string initialisiert werden kann, der im Test
auf diese Datenquelle weist und in Produktion auf eine andere. Du willst
so eine Serviceklasse womöglich gar nicht vollständig im Test ersetzen;
ein Interface wäre überkandidelt. Allerdings möchtest du im Test eine
spezielleDatenquelleverwenden.DasistübereineKonfigurationmöglich,
die für jeden Test individuell ist; in jedem Test wird wieder ein Objekt der
Datenbankzugriffsklasse erzeugt und frisch konfiguriert.
Sobald du anfängst mit der Polymorphie, also Interfaces einsetzt und zur
Laufzeit unterschiedliche Instanzen benutzen willst, kommst du schnell
auf Inversion of Control (IoC), d.h. die Konfiguration von Klassen mit
Serviceobjekten. Insofern stecken instanziierbare Klassen andere an, wo
immer ihre Objekte injiziert werden sollen.
Und was ist nun mit statischen Klassen? Die sind für mich der default.
Ja, genau! Ich wünsche mir zuerst, dass eine Klasse statisch ist - und
dann kann es sein, dass ich einem der genannten Kriterien nachgeben
muss. Schade, denn ich finde statische Klassen einfacher zu verstehen
und auch zu testen: Die muss ich nicht instanziieren, die muss ich nicht
konfigurieren, da gibt es keine Interfaces, da gibt’s keine komischen
Abhängigkeiten zu ersetzen. Das finde ich alles super. Und wenn einige
hardcore mainstream OO Apologeten abfällig meinen, statische Funktio-
nen “seien böse”, weil sie doch für prozedurales Denken stünden, was ja
nun gar nicht mehr ginge… dann wünsche ich einen guten Tag und gehe
wieder mit IOSP und PoMO an die Arbeit.
static ist ein Werkzeug. Man muss es eben einsetzen können. Wenn
die Welt nur noch voller Nägel ist, passt dieser Schraubendreher nicht
mehr. Ist schon klar. Doch für mich ist die Lösungswelt bunter. Statische
Methoden haben darin ihren Platz genauso wie instanziierbare Klassen
und Funktionszeiger. Für mich zählt, wie ich ein auf bestimmten Prin-
zipien beruhendes Modell am besten in Code übersetzen kann, um den
verständlich und testbar zu halten. Dazu tragen statische Methoden und
Klassen bei.
EsgibtdanämlichzumBeispieleinMuster:ServiceklasseninderDomäne,
im Kern können oft statisch bleiben. Das ist der Fall, weil es ja explizite


---


<!-- Page 256 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 247
Integrationen darüber gibt und die Serviceklassen frei von Abhängig-
keiten von Ressourcen bleiben können. Sei auch hier gespannt auf das
IODA-Kapitel. Das Muster nennt sich functional core, imperative shell¹⁴⁴:
im Kern bleiben Klassen statisch und folgen mehr der Funktionalen
Programmierung, drumherum jedoch in der Peripherie kommen jedoch
instanziierbare Klassen aus den oben genannten Gründen zum Einsatz.
Explizite Interfaces für Klassen
Interfaces sind keine Module. Module haben Interfaces. Interfaces sind
eine Form für den Kontrakt eines Moduls. Die bekannteste Form ist eine
explizite Interface-Definition wie z.B.¹⁴⁵
1 interface IStack {
2 void Push(object element);
3 object Pop();
4 }
Wenn eine Klasse ein Interface implementiert, also seinen Kontrakt be-
dient, sind die Interface-Methoden für Clients des Interface nutzbar und
alle anderen nicht. Ein Interface ist mithin eine Fokussierungshilfe. Es
bietet einen view auf die öffentlichen Methoden einer Klasse.
Außerdem abstrahiert das Interface insofern, als das es alle Klassen unter
sich subsummiert im Sinne einer Aggregation, die es implementieren.
Dadurch entsteht in OO-Sprachen Polymorphie: einem Client ist es letzt-
lich egal, welcher Klasse ein Objekt angehört, solange es das Interface
implementiert, auf das er baut. Alan Kay hatte sich “extreme late binding”
gewünschtfürdieNachrichtenbehandlung,ummaximalePolymorphiezu
ermöglichen; das liefern Interfaces nun aber gerade nicht. Im Gegenteil,
mit ihnen musst du dich früh festlegen, welche Objekte welche Nach-
richten “verstehen”. Doch das hat auch seine guten Seiten: Typsicherheit
und damit die Möglichkeit, Fehler schon zur Übersetzungszeit zu finden.
Manche Sprachen pfeifen darauf, aber in C++, C# und Java ist es halt so.
¹⁴⁴https://www.destroyallsoftware.com/screencasts/catalog/functional-core-imperative-
shell
¹⁴⁵Ich mag den Präfix “I” für Interfaces. Klassen mit einem “C” zu beginnen, würde mir
nicht einfallen. Dafür sind Klassen viel zu häufig und zu sehr im Mittelpunkt; bei ihren
NamenmöchteichRauschenvermeiden.DochbeieinemInterfacefindeichdas“I”hilfreich
zur Unterscheidung eines Interface-Typs von einer Klasse. Es trägt nicht stark auf und gibt
mirKlarheit.DieseKonventionvonC#wünscheichanderenSprachen.Oderduübernimmst
sieeinfachfürdeineProjekte.Warumnicht?


---


<!-- Page 257 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 248
ExpliziteInterfaceshelfenderModularisierungindemsieVielgestaltigkeit
ermöglichen, sind jedoch selbst keine Module.
Namensraum - Kontraktkollisionen vermeiden
Namensräume beherbergen Datentypen (z.B. Klassen und Interfaces).
Eigentlich zähle ich Namensräume jedoch im Allgemeinen nicht zu den
Modulen. Sie sind für mich vor allem syntactic sugar, um Namen einfa-
cher differenzieren zu können.
In Sprachen, wo Namensräume allerdings ermöglichen (z.B. Java Packa-
ges), die Sichtbarkeit ihrer Elemente einzuschränken, kannst du sie zu
den Modulen rechnen. Sie definieren dann simple Kontrakte - addieren
jedochnichtsEntscheidendeszuModulenhinzu.Siesindreinsyntaktische
ModuleauftextuellerEbene;dukönntestimGrundedieselbenEffektemit
geschachtelten Klassen erzielen.
Bibliothek - Wiederverwendbarkeit ermöglichen
Einen wesentlichen Schritt über Klassen hinaus gehen Bibliotheken. Sie
sind für mich die wesentliche nächste Ebene in der Modul-Hierarchie.
Bibliotheken beherbergen Datentypen (z.B. Klassen) und definieren einen
Kontrakt über deren Sichtbarkeit. Wesentlich ist jedoch, dass sie ihre
Elemente in Form einer Black Box anbieten. Bibliotheken verlassen das
Reich des Quellcodes. Sie sind ausführbare Container.


---


<!-- Page 258 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 249
Damit bringen Bibliotheken Wiederverwendbarkeit in die Modulhier-
archie. Nicht Klassen sind die Meilensteine der Wiederverwendbarkeit,
wie es die mainstream Objektorientierung glaubt, sondern Bibliotheken.
Und mit Bibliotheken wurde schon Wiederverwendbarkeit lange vor der
Objektorientierung erreicht.
Solange Quellcode eines Service für den Entwickler eines Clients sichtbar
ist, würde ich nicht wirklich von Wiederverwendbarkeit sprechen. Im
Zweifelsfall würde der Entwickler des Clients nämlich den Service zu
seinen Gunsten anpassen. Das ist noch der Fall, wenn dir Code in Form
von Klassen oder Namensräumen vorliegt.
Erst wenn man dir Code lediglich als Bibliothek aushändigt, beginnt
die Wiederverwendbarkeit. Dann hast du keine Möglichkeit des Eingriffs
in den Service-Code. Du kannst nicht hinter die Fassade des Kontrakts
der Bibliothek schauen. Alle Implementationsdetails sind dir physisch
verborgen.
Das ist ein wichtiger Schritt nach vorne bei der Modularisierung. Damit
kommt die Softwareentwicklung anderen Disziplinen näher, die aus fixen
Bauteilen Neues zusammensetzt.
Leidersind BibliothekeninnerhalbvonProjektenunterbewertetals Mittel
zur Modularisierung, finde ich. Fremde Bibliotheken werden gern angezo-
gen, um sich selbst Entwicklungsaufwand zu sparen - doch der eigene
Code wird nur vergleichsweise schwach in Bibliotheken gekapseln.


---


<!-- Page 259 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 250
Paket - Abhängigkeiten stabilisieren
SobaldBibliothekenvonunbekanntvielenClientsbenutztwerden,kommt
es besonders auf Stabilität an. Bei Auslieferung wollen Clients sicher sein,
mit den Bibliotheken ausgeliefert zu werden, gegen die sie entwickelt
wurden. Nur weil eine Bibliothek aber einen syntaktischen Kontrakt
erfüllt - also gewisse Klassen mit gewissen Methoden veröffentlicht -
und erfolgreich zur Laufzeit geladen und gebunden werden kann, heißt
das nicht, dass sie auch der entspricht, gegen die compiliert wurde. Das
Verhalten hinter der Fassade des Kontraktes könnte sich verändert haben;
die Semantik könnte eine andere sein.
Mit dieser Unsicherheit räumen Pakete auf. Pakete enthalten eine oder
mehrereBibliothekenundfixierendieseKonstellationinderZeitmiteiner
Versionsnummer. Ein Paket mit einem grundsätzlich gleichen Service
kann auf diese Weise mehrfach existieren.
Und nicht nur dokumentiert die Versionsnummer eines Paketes dessen
Entwicklung, sie sorgt auch dafür, dass Pakete in Abhängigkeitsbäumen
insgesamt stets in der korrekten Konstellation vorliegen. Wenn Pakete
andere referenzieren, dann immer inklusive deren Versionsnummer.
Pakete sorgen mithin für größere Stabilität in modularisierter Software.
Clients können sicher sein, dass ihre Services den Erwartungen entspre-
chen, die sie zum Zeitpunkt des Eingehens der Abhängigkeit erfüllten.
Auch Pakete halte ich für unterbewertet innerhalb von Projekten. Gerne
zieht man fremde Pakete an - doch für die Modularisierung des eigenen
Codes werden sie vergleichsweise selten genutzt.


---


<!-- Page 260 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 251
Paket-Funktionen als Logik
Oben ist Logik wie folgt definiert:
• Transformationen/Operatoren, z.B. <, ++, args.Length
• Kontrollstrukturen, z.B. if-else, for, try-catch
• I/O-bzw.allgemeinerAPI-Calls,z.B.Console.Write(),File.OpenRead()
Dasistsehrdetailliertundnichtfalsch.FürgrößereSoftwaresystemekann
esjedochamEndeetwasunpraktischwerden.Deshalbformuliereichjetzt
nochmal etwas allgemeiner:
Logik besteht aus Kontrollstrukturen und Aufrufen von Pake-
ten.
Die entscheidende Neuerung ist, dass Transformationen und API-Calls
zusammengefasst sind zu Funktionen, die in anderen Paketen als dem
definiert sind, an dem du jeweils gerade arbeitest. Damit ist all das
Verhalten Logik, für das dir kein Quellcode vorliegt. Versionierte Black
Boxes enthalten also stets Logik. Ob die Black Box die Standardbibliothek
deiner Programmiersprache ist oder eine 3rd Party Bibliothek oder der
Compiler dir mit einem Operator syntactic sugar anbietet, um einen
Funktionsaufruf zu verbergen, das ist einerleid. Aber vor allem ist ab
jetzt auch einerlei, ob die aufgerufene Funktion von dir/deinem Team
geschrieben wurde. Solange ihr eure Funktionen in Pakete verpackt und
damit die Quellen am Nutzungsort unzugänglich macht, solange könnt
ihr auch eure eigenen Funktionen in Operationen aufrufen.
Ist das eine Erleichterung? Ich hoffe, doch. Aber sie musste eben bis hier
warten, weil die Modularisierung noch nicht eingeführt war.
Pakete sind also die Container, in denen Strata definiert werden. Strebe
danach, eure Abstraktionen in Form eines höher und höher steigenden
Vokabulars in Pakete zu verpacken.¹⁴⁶ Du verfolgst damit dieselbe Stra-
tegie, der die ganze Branche notwendig als Markt folgt. Das ist technisch
¹⁴⁶Apropos Abstraktion: Wenn du deine eigenen Funktionen aus anderen Paketen als
Logik ansiehst, dann musst du schauen, dass das SLA nicht zu leicht verletzt wird. Wenn
dudichindeinenPaketenStratumfürStratumundSpracheebenefürSprachebeneindeiner
“DSL” nach oben arbeitest, dann vergrößerst du auch den Abstand zu Funktionen aus 3rd
PartyPaketenbzw.Operatoren.TendenziellwirstdualsoweiterobeninAbstraktionenauch
inOperationenwenigerKontrollstrukturenundOperatorenusw.einsetzenwollen.


---


<!-- Page 261 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 252
nichtschwer-dochdumusstdenMuthaben,KlassenundFunktionenund
damit Logik in Paketen zu fixieren. Das kostet Organisationsaufwand, das
braucht womöglich Arbeitsteilung, dafür musst du einen Entwurf haben.
Doch als Preis winken Funktionen, die du in Logik noch höherer Ebene
benutzen darfst. Mit Paketen schaffst du dir stabile eigene Abstraktions-
ebenen.
Komponente - Die Arbeitsteilung befördern
Komponenten bestehen aus mindestens zwei Arten von Paketen. Die eine
definiert den Kontrakt der Komponente, die andere eine Implementation
des Kontrakts.
PaketmitKontrakt1.0.0undPaketmitdessenImplementation1.3.0
Komponenten sind die Module, die nicht nur eine Separierung von Kon-
trakt und Implementation erzwingen, sondern den Kontrakt auch phy-
sisch unabhängig als Black Box neben die Implementation stellen. Kon-
trakt und Implementation sind natürlich plattformspezifisch, da sie als
Pakete vorliegen. Dennoch geht diese Strukturierung deutlich über die
Paarung eines expliziten Interface mit einer Klasse hinaus. Der physisch
separate Kontrakt, der in einem oder mehreren Paketen vorliegt, kann
nämlich unabhängig von der Implementation Clients zur Verfügung ge-
stellt werden.
Solange explizites Interface und implementierende Klasse noch in dersel-
ben Bibliothek vorliegen, ist zwar etwas gewonnen für die Entkopplung
zwischen Clients und Service.


---


<!-- Page 262 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 253
Dennoch muss zuerst der Service mit seinem Interface in einer Bibliothek
vorliegen, bevor ein Client dagegen entwickelt werden kann.
Wenn der Kontrakt jedoch physisch separat in einer Bibliothek vorliegt
(oder noch besser: in einem Paket, damit es auch keine Missverständnisse
gibt)…


---


<!-- Page 263 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 254
…dann kann die Entwicklung auf beiden Seiten des Kontrakts gleichzeitig
erfolgen:
Mit Komponenten wird eine Arbeitsteilung im Team möglich, die an bei-


---


<!-- Page 264 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 255
denEndeneinesDurchstichsgleichzeitigarbeitenkann.Fürinkrementelle
Entwicklung ist das ein großer Gewinn.
Allerdings kommen auch Komponenten nur selten innerhalb von Projek-
ten zum Einsatz. Meine Vermutung: das ist eine Folge fehlenden syste-
matischen Entwurfs. Denn ohne einen Entwurf, der Module sorgfältig
herausarbeitet, sind Kontrakte vor der Codierung unbekannt. Sie können
also nicht zuerst definiert werden, um dann auf beiden Seiten parallel zu
arbeiten.
Dasistsehrschade,dennwannimmerichmitTeamskomponentenbasiert
arbeitsteilig arbeite, ist die Überraschung am Ende groß, dass das ersten
so reibungslos funktioniert und zweitens auch noch entspannt. Denn wer
auf seiner Seite des Kontrakts arbeitet, kann sich ganz auf seine Arbeit
konzentrieren. Der Kontrakt ist der einzige Bezugspunkt. Ein ständiger
Austausch mit anderen Entwicklern nicht nötig. Und die Black Box, in
der der Kontrakt kommt, widersteht der Versuchung, doch noch schnell
nebenbei etwas daran zu verändern. Die Stabilität ist deutlich erhöht.¹⁴⁷
Service - Module plattformneutral machen
Komponenten trennen den Kontrakt von der Implementation. Und Ser-
vices machen den Kontrakt plattformneutral.
Services bestehen aus mehreren Modulen mit einem plattformneutralen
Kontrakt. Das bedeutet, der Kontrakt liegt nicht als Bibliothek oder Quell-
code Interface vor, sondern in irgendeiner anderen Form. Der Kontrakt
eines Service könnte in einer XML-Datei beschrieben sein oder in einem
RFC-Textdokument wie z.B. das SMTP-Protokoll¹⁴⁸.
¹⁴⁷Natürlich sind Komponentenkontrakte nicht in Stein gemeißelt. Sie können während
der Entwicklung auf beiden Seiten in Frage gestellt werden. Doch dann ist ein expliziter
AustauschübergewünschteVeränderungennötig.EskommtnichtzuAlleingängen,dienur
zu unangenehmen Überraschungen führen können. Es gibt eine Zeit für die Definition von
Kontrakten, und es gibt eine Zeit für ihre Nutzen. Komponentenorientierung trennt diese
Aspekte und die Phasen ihrer Entwicklung sorgfältig. Ein erster Schritt ist - wie gesagt -
mit expliziten Interfaces (oder abstrakten Basisklassen) gemacht; der wahre Vorteil solcher
AbstraktionkommtjedocherstmitKomponentenzumTragen.
¹⁴⁸https://tools.ietf.org/html/rfc821


---


<!-- Page 265 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 256
EinplattformneutralerKontraktkanninjederProgrammierspracheimple-
mentiertwerden.Dasbedeutet,aufbeidenSeiteneinesplattformneutralen
Kontrakts, beim nutzenden Client wie beim implementierenden Service
können unterschiedliche Plattformen am Start sein.
Damitdasmöglichist,müssenServicesineinemeigenenProzessgetrennt
von Clients laufen. Die Plattformneutralität der separaten Kontrakte
erzwingt also die Laufzeit-Autonomie der Implementationen.
Dasistnatürlichnichtneu.SchonUnixcommandlineutilitieswarennach
dieser Definition Service-Module:
1 ls | grep ".md" | wc -l
ls und grep und wc sind separate Programme und laufen in eigenen Pro-
zessen, wenn diese Kommandozeile ausgeführt wird. Sie kennen einander
nicht - das PoMO lässt grüßen - und basieren lediglich auf einem ganz
einfach Kontrakt: ihr Input kommt von der Konsole (stdin) und ihr Out-
put geht auf die Konsole (stdout). In welcher Programmiersprache diese
Utilitiesgeschriebensind,istegal.Siearbeitenproblemloszusammen.Und
du könntest eine weitere Utility schreiben, die auch diesem Kontrakt folgt.
Service-Orientierung ist also nichts, was wirklich neu ist. Micro-Services
sind lediglich die moderne Variante eines alten Konzepts.


---


<!-- Page 266 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 257
Wave - Softwareevolution zur Laufzeit
UndwelchesModulfasstvieleServiceszusammen?IchnennedieseEbene
der Hierarchie Wave. Für mich bildet der Zusammenschluss von vielen
Services, bei denen manche öffentlich an der Peripherie sind und andere
im inneren des Moduls verborgen eine Art stehender Welle: Die ange-
botene Leistung wird beständig erbracht, es gibt keine Pause - doch die
Instanzen der einzelnen Services oder auch ihre Organisation hinter der
Kontrakt-Fassade könnens ich jederzeit und zur Laufzeit ändern. Durch
eine stehende Welle in einem Fluss fließt ständig Wasser, die Form bleibt
dennoch erhalten. Dito bei einer Wave bestehend aus Service-Modulen.
Mit einer Wave wird Software zur Laufzeit evolvierbar. Auf darunter
liegenden Modul-Ebenen muss die Nutzung pausieren, um von einer
neuen Service-Version zu profitieren. Bei einer Wave ist genau das nicht
mehr der Fall.


---


<!-- Page 267 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 258
Die Modul-Hierarchie im Überblick
Wie du siehst, stehst du einer wachsenden Zahl von Funktionen nicht
machtlos gegenüber. Es gibt eine Reihe pragmatischer, ordnender Mittel,
die Modul-Hierarchie.
In ihr können zuerst Funktionen und dann Module physisch geschachtelt
werden - unter Optimierung der jeweils entstehenden Oberfläche. Mit
KontraktenkannstdudasVerhältniszwischenöffentlicherBühneundver-
borgenem Schnürboden so einstellen, dass eine gute Mischung zwischen
Leistungsangebot plus Testbarkeit und Entkopplung entsteht.
Je weiter oben in der Modul-Hierarchie du dich bewegst, desto größer die
Anforderungen an Werkzeuge, Infrastruktur und Arbeitsorganisation. Du
kannst deshalb leichter über Klassen entscheiden als über Services. Das
tust du auch schon jeden Tag - doch ich möchte dich motivieren, dich
etwas mehr “nach oben zu orientieren”.
Auch wenn es aufwändiger wird, mit Modulen umzugehen, je höher die
Hierarchie hinauf du dich aggregierend begibst, der Lohn der Mühe ist
eine wachsende Übersicht über dein “Rohmaterial”, die Funktionen. Die
Zahl der Funktionen, die ein Modul praktikabel enthalten kann, steigt mit
jeder Ebene deutlich. Bei Klassen mögen es vielleicht nur 10 oder 20 sein,
bei Services reden wir von Tausenden.


---


<!-- Page 268 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 259
Meiner Erfahrung nach, bewegen sich zu viele Projekte zu weit unten in
der Modulhierarchie. Sie versuchen vor allem mit Klassen zu modulari-
sieren. Da stößt dann die physische Hierarchie schnell an ihre Grenzen.
Das Resultat sind dann Codebasen, in denen zu viele Funktionen zu
weit sichtbar sind; das führt zu unnötigen Abhängigkeiten, die wiederum
unnötige Stabilitätsforderungen nach sich ziehen. Kurz: Zu niederstufige
Modularisierung leistet Inflexibilität Vorschub und senkt somit die Pro-
duktivität.
Beziehe in deine Entwurfsentscheidungen also öfter physische Schachte-
lungen von Klassen mit ein, vor allem jedoch nutze viel öfter Pakete und
Komponenten.
• Pakete lege ich dir ans Herz, weil du Black Boxes in stabilen
Verhältnissen benutzen willst. Bibliotheken waren früher ok, aber


---


<!-- Page 269 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 260
heute sind sie es nicht mehr. Allemal nicht mehr, wenn du in einem
Team arbeitest.
• Komponenten lege ich dir ans Herz, weil du mit ihnen dein Team
besser nutzt. Statt gleichzeitig an vielen Features zu arbeiten und
sich dabei ins Gehege zu kommen - Merge-Konflikte lauern überall
-, arbeitet lieber am selben Feature, aber an verschiedenen Stellen
in der Codebasis entlang des Durchstichs vom Frontend bis zum
Backend.
Auch wenn heute serviceorientierte Architekturen der letzte Schrei sind,
rate ich dir nicht unbedingt zu ihnen. Sie haben ihren Platz und Con-
tainer sind cool - doch in dieser Weise massiv verteilte Anwendungen
haben einen hohen Preis. Ein solider Monolith oder vielleicht eine simple
Verteilung auf Client und Server sind in vielerlei Hinsicht einfacher zu
handhaben - müssen deshalb aber nicht weniger modular sein.
Wenn du mehr Modularität haben willst, erhebe dich zunächst über die
Klassen hinauf in die Welt der Black Boxes. Eine gute komponentenorien-
tierte Architektur ziehe ich jeden Tag einer schlechten serviceorientierten
vor.
Datenflüsse modularisieren
Puh, das war jetzt ein Ausflug in die Welt der Module. Lieber wäre mir
eine engere Verzahnung mit Datenflüssen und gleichzeitiger Anwendung
gewesen. Doch in diesem Buch will ich mich auf “Datenflussdenke”
konzentrieren und nicht auf die Modularisierung mit dem dahinter lau-
ernden großen Thema Architektur. Deshalb habe ich dir Module nur als
Konzept erklärt und vor allem im Überblick vorgestellt. Die Anwendung
im Weiteren wird sich auf Klassen und Bibliotheken beschränken.
Größere Strukturen werden zwar noch im Rahmen des Kapitels um die
IODA Architektur thematisiert, doch der Aufhänger werden auch dort
Datenflüsse sein.
Selbst wenn die meisten Modularisierungsebenen hier theoretisch und
abstrakt bleiben werden, wirst du aber etwas für die Organisation von
SoftwarezurÜbersichtlichkeitmitnehmen.Allermeistensbewegstdudich
in deinen Projekten ohnehin auf Ebene von Klassen und Bibliotheken.


---


<!-- Page 270 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 261
Module in Datenflussmodelle einzuziehen, ist von der Notation her ein-
fach. Es gibt auch verschiedene Möglichkeiten, zwischen denen du nach
Geschmack und Eignung im konkreten Fall wählen kannst.
Notation & Implementation I - Funktionen
Der Fokus beim Flow-Design liegt auf dem Verhalten. Es ist wahrlich
ein Behavior-Driven Design Ansatz - der trotz des ableitbaren Akronyms
nichts mit BDD (Behavior-Driven Development) gemein hat. Das, was
zuerst zu modularisieren ist, sind deshalb die Funktionseinheiten.
Das geschieht durch simple visuelle Zusammenfassung: kästle die Funkti-
onseinheiten, die zum selben Modul gehören sollen, einfach ein.
Module, die weiter auseinander liegende Funktionseinheiten aggregieren,
müssen dabei nicht in einem Stück gezeichnet werden. Du erkennst die
Zusammengehörigkeit verschiedener Teile ja am Namen und/oder z.B. an
einer Farbe.
Genauso funktioniert es zeichnerisch in 2-dimensionalen Datenflüssen:


---


<!-- Page 271 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 262
Die so eingezeichneten Module werden zu Klassen im Code. Wie du
diese Klassen dann zu Modulen auf höherer Ebene zusammenfasst, ist im
Grunde unabhängig vom Datenfluss. Den gibt es zwar immer noch, nur
ist kein Prozess mehr zu erkennen, wenn du Datenflusspfeile zwischen
Modulen einzeichnest. Es entstehen Schleifen, die verhindern, dass du
klar den Hergang einer Transformation von Input zu Output erkennen
kannst.¹⁴⁹
Interessanter als die Datenflüsse werden bei der Modularisierung dann
¹⁴⁹In dieser Darstellung müssen auch Pfeile eingezeichnet werden, die Datenfluss mit
Funktionseinheitennichtzusehensind:DatenflüssevonderIntegrationzurerstenintegrier-
ten Funktionseinheit und zurück zur Integration von der letzten integrierten. Sonst wären
Moduleunverbunden,indenenFunktionseinheitenausanderenintegriertwerden.


---


<!-- Page 272 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 263
die Abhängigkeiten zwischen den Modulen. Damit kommst du von der
Verhaltensdarstellung zur Strukturdarstellung.
Und mit dieser Perspektive arbeitest du dich dann die Modul-Hierarchie
hoch:


---


<!-- Page 273 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 264
Modularisierungsrichtung
Weil Flow-Design verhaltensorientiert ist, stehen Datenflüsse, d.h. Pro-
zesse mit ihren Funktionseinheiten im Mittelpunkt - und nicht Module.
Das ist im Gegensatz zur mainstream Objektorientierung; dort findet der
Einstieg oft/meistens über die Module in Form von Klassen statt.
DieseHerangehensweisehalteichfürfehlgeleitetundeineUrsachefürdie
Unwandelbarkeit von vielen Codebasen heute. Mit Klassen zu beginnen,
ist eine Form von vorzeitiger Optimierung. Man meint schon am Anfang,
wissen zu können, welche Aggregationen am Ende nützlich sein werden.
Aber woher sollte man das wissen? Aggregationen fassen nach Ähnlich-
keit zusammen. Doch welche Ähnlichkeiten sind am Anfang sichtbar?
Keine. Es gibt nichts, das ähnlich oder verschieden sein könnte.
UnddassDatenstrukturenAggregationenfürFunktionseinheitenausFlüs-
sen sein sollten, habe ich oben schon weitgehend ausgeschlossen. Fängt


---


<!-- Page 274 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 265
manmitdenenjedochan,dannistdasBestrebenganznatürlich,möglichst
viel darauf zu vereinen. Mainstream OO-Codebasen sind deshalb aus
meinerSichtzuwenigmodularisiert;esgibtzuwenigeKlassenunddaraus
folgend auch zu wenige Bibliotheken usw.
Ich bin ein Verfechter der “Mustererkennung”, statt der a priori Definition
von Modulen.¹⁵⁰ Deshalb ist mein hauptsächliches Vorgehen bei der
Modularisierung bottom-up: Ich starte die Modularisierung bei den Ope-
rationen und arbeite mich von dort nach oben durch den 2-dimensionalen
Datenfluss.
Dabei fange ich mit der am einfachsten zu klassifizierenden Operation
an. Sobald die einer Klasse angehört, kann ich bei der nächsten Operation
überlegen, ob sie derselben oder einer anderen Klasse angehören sollte.
Und sobald ich zwei Klassen habe, kann ich bei der nächsten Operation
überlegen, ob sie der einen oder anderen oder einer dritten Klasse angehö-
ren sollte. Usw. usf. von den Operationen zur Wurzel des Datenflusses.
Die Frage, ob sie dieser oder jener oder einer neuen Klasse angehören
¹⁵⁰Natürlich liegen manchmal Module auf der Hand. Das wirst du spätestens im Kapitel
zur IODA Architektur selbst von mir hören. Aufs Ganze gerechnet sind das jedoch wenige.
Deshalb ist Flow-Design noch nicht Modul-getrieben. In mancher Hinsicht musst du
dich aber eben auch nicht dümmer stellen, als du in der Entwurfssituation bist. Es gibt
musterhafte Entwicklungen in der Softwareentwicklung; aus denen kann man schon auf
gewissenaheliegende,garwiederkehrendeModuleschließen.


---


<!-- Page 275 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 266
sollte, stelle ich genauso einer Integration. Die Integrationen kommen
allerdings meistens erst nach den Operationen dran. Nur in manchen
Fällen ist es schon früher klar, dass eine Integration einer bestimmten
Klasse angehören sollte.
EbensoistesinmanchenFällenauchmöglich,top-down beiderModulari-
sierung vorzugehen. Bei einer Integration kann sich aufdrängen wohin sie
gehört und dann vermerke ich das auch sofort - und behalte mir natürlich
vor, diese Entscheidung später zu revidieren.
Die Modularisierung ist letztlich ein Jo-Jo-Vorgehen, dessen Amplitude
schnell abnimmt. Was du von unten kommend klassifiziert hast, prüfe
von oben kommend auf Sinnhaftigkeit und umgekehrt. Das ist wie beim
Bettenmachen: Dort beginnst du an einer Seite, die Bettdecke glatt zu
ziehen, gehst auf die andere Seite und glättest dort, dann wieder zurück
und nachbesser und nochmal von der anderen Seite. Jedenfalls geht mir
das so. Ich brauche 2-3 Runden ums Bett, wenn es wirklich ordentlich sein
soll.
Modularisierungskriterien
Und was sind die Überlegungen, nach denen du Funktionseinheiten zur
selben oder zu einer anderen Klasse rechnen solltest? Im Abschnitt Kri-


---


<!-- Page 276 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 267
terien für die Aggregation mit Klassen habe ich sie dir im Grunde schon
genannt, aber ich wiederhole sie aus einem etwas anderen Blickwinkel
hier nochmal:
• Wenn du bei zwei Operationen feststellst, dass sie mit demselben
API umgehen, dann fasse sie im selben Modul zusammen. Beispiele
dafür:Dateisystemzugriff,Benutzerinteraktion,TCP-Kommunikation.
Ob über den API auf eine Hardware-Ressource zugegriffen wird
oder er lediglich eine Abstraktion von Logik darstellt (z.B. Ver-
schlüsselung), ist für die Zusammenfassung unerheblich.
Umgekehrt solltest du Funktionseinheiten, die nicht denselben API
benutzen, auch nicht aggregieren.
Solche Klassen wirst du eher nicht statisch machen, da ihr Service
oft (für Tests) konfiguriert werden muss und/oder Polymorphie
gewünscht ist.
• Wenn zwei Operationen auf denselben in-memory Zustand zu-
greifen, fasse sie ebenfalls zu einer Klasse zusammen. Dann wird
daraus später auch ein Objekt.
• Funktionseinheiten, die “thematisch” zusammengehören - sei es
wegen Verantwortlichkeit oder Aspekt -, fasse auch zusammen
in derselben Klasse. Dieses Kriterium ist jedoch vergleichsweise
schwach, weil du es nicht formal am Datenfluss überprüfen kannst;
du musst den Datenfluss dafür verstehen.
• Und schließlich gibt es noch einen speziellen Fall bei Integrationen:
Wenn eine Integration ausschließlich Funktionseinheiten der-
selbenKlasseintegriert,dannsolltesieselbstebenfallsdieserKlas-
se angehören. Sie wandert damit wahrscheinlich in den Kontrakt
der Klasse und die integrierten Funktionseinheiten können oft aus
ihm herausgehalten werden. Gerade für dieses Muster ist es vorteil-
haft, wenn du bottom-up bei der Modularisierung vorgehst.¹⁵¹
Notation & Implementation II - Daten
Die Modularisierung der Daten hat zwei Aspekte:
¹⁵¹Dieses Muster ist sehr mächtig! Mit ihm kannst du nicht nur Erkenntnisse für eine
gute Modularisierung gewinnen, sondern auch für gute Datenflüsse. Es hat Kraft, Funk-
tionseinheiten zusammenzufassen und zu trennen. Manchmal wirst du deinen Datenfluss
überdenken, um diesem Muster dienen zu können. Der Gewinn, der dadurch entsteht ist
eine Verringerung der Oberfläche eines Moduls, weil du integrierte Funktionseinheiten aus
demKontraktrausdrückenkannst.


---


<!-- Page 277 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 268
• Aggregation von Daten in einem Modul
• Zuordnung von Funktionen zu Daten
Ich fasse das gern unter einem Begriff zusammen, der der Verhaltensori-
entierung im Flow-Design ein Gegengewicht gegenüberstellt:
Wider die Primitive Obsession
Die primitive obsession¹⁵² schleicht sich leider schnell ein, wenn du sehr
fokussiert auf den Prozess bist. Du suchst die Funktionseinheiten, die
etwas tun, und lässt zwischen ihnen nur die nötigen Daten fließen: hier
einFeld,dorteineHashmap,daeinTupel.Dasfunktioniertauchalles-nur
wunderst du dich irgendwann darüber, dass deine Service-Klassen stark
anwachsen. Wohin dann mit den Methoden?
Das Wurzelproblem dahinter ist, dass bei zu ausgeprägter “Datenfluss-
denke” Datenklassen nicht so schnell auf den Schirm treten und am
Ende gar unter den Tisch fallen. Wo die mainstream Objektorientierung
Datenstrukturen zu stark auflädt mit Logik, kann es dir zu Beginn der
Beschäftigung mit der radikalen Objektorientierung passieren, dass du
nichteinmalansiedenkst.DasistauchnichtgutundwirdmitdemBegriff
der primitive obsession bezeichnet: Du verschenkst Chancen auf sinnige
eigene Datentypen, an die sich dann auch Logik anlagern darf im zweiten
Schritt.
Wenn du dann zwar Datenklassen definierst, aber “vergisst”, relevante
Logik darin zu versammeln, dann kann es zum anemic domain model¹⁵³
kommen. Die Datenstrukturen sind zwar schön strukturiert, nur sind sie
“blutleer”, d.h. ohne Logik.
Flow-Design mag sich so darstellen, als dass es keinen Wert auf “gut
ausgestattete” Datenstrukturen legen würde. Doch das Gegenteil ist der
Fall. Wogegen ich mich allerdings wende, ist die vorzeitige Definition
und überreiche Ausstattung von Datenstrukturen. Zuerst der Datenfluss
und primitive fließende Daten - und dann mal schauen, was sich für
Muster zeigen. Sehe ich Muster in Datenkonstellationen oder in der
¹⁵²http://wiki.c2.com/?PrimitiveObsession
¹⁵³https://www.martinfowler.com/bliki/AnemicDomainModel.html


---


<!-- Page 278 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 269
Transformation von Daten, dann kann ich nur raten, die in Datenstruk-
turen auch auszudrücken. Entscheidungen und Erkenntnisse “sind zu
modularisieren”: das ist der Kern des SRP.
Für Klassen muss es einen Bedarf geben. Den Bedarf stellen Funktions-
einheiten dar, die etwas gemein haben. Den Bedarf stellen auch Daten
dar, die “sich ergänzen” und von einer Komposition in einer Datenklasse
profitieren.
Danach suche ich zuerst in den fließenden Daten: gibt es Tupel, die besser
unter einem Namen zusammengefasst würden? Beispiel: Wenn die Net-
tozeilenzählung aufgebohrt würde, dann wäre es irgendwann vorteilhaft,
den Dateinamen beim Dateiinhalt zu lassen; es könnte dafür ein Tupel
(dateiname, dateiinhalt) fließen. Aber warum nicht beides in
einer Datenklasse Datei{} zusammenfassen? Leider ist das in manchen
OO-Sprachen noch sehr “teuer”; eine Klasse in Java oder C# für diesen
Zweck zu definieren, scheint der geringe Scope, in dem sie genutzt wird,
nicht zu rechtfertigen angesichts des Aufwandes, der für Konstruktor,
getter/setter und womöglich für Vergleichbarkeit von Instanzen getrieben
werden muss. In anderen Sprachen wiederum bekommt man viel davon
“geschenkt”. Dennoch: Ich möchte dich ermuntern, öfter diesen Aufwand
zu treiben für eine aussagekräftige Modularisierung.
Manchmal lohnt sich das auch schon für nur ein Datenelement, z.B. eine
Liste. Ein eigener Datentyp gibt ihm schlicht einen Namen - und ist
anschließend Anlagerungspunkt für passende Logik.
Im zweiten Schritt kannst du schauen, ob Datenklassen etwas mit Funk-
tionalitätaufgeladenwerdenkönnen.DamitbekommstdueinenHebelan
die Hand, mit dem du Funktionseinheiten im Fluss aus anderen Klassen
herausbrechen kannst. Du entzerrst Service-Klassen, indem du Logik in
Datenklassen verschiebst.
Wenn es im Rahmen der Nettozeilenzählung eine Datei{}-Klasse gäbe,
dann wäre sie z.B. der natürlich Ansprechpartner für die Bruttozeilenzahl,
falls die für eine Auswertung nötig wäre.
Auf der Basis von Datenklassen für einzelne Elemente in einer Liste
liegt auch immer mal wieder nahe, die Liste selbst in einen eigenen
Datentyp zu fassen. Bei der Nettozeilenzählung könnte ich mir zum
Beispiel Dateien{} vorstellen, die als ADT eine Liste von relevanten


---


<!-- Page 279 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 270
Dateien zur Verfügung stellen könnte. Statt schon bei der Dateienbeschaf-
fung durch Traversierung des Verzeichnisbaum einen Filter anzusetzen,
könnten in einer Instanz von Dateien{} zunächst alle Dateien in der
Verzeichnishierarchie geliefert werden - um dann für unterschiedliche
Zwecke gefiltert zu werden, z.B.
1 var ds = new Dateisystem();
2 ...
3 var dateien = ds.DateienUnterWurzel(pfad);
4 var relevanteDateien = dateien.MitTyp("java");
5 ...
6 relevanteDateien = dateien.MitTyp("cs");
7 ...
Die MitTyp()-Methode gehört zum Aspekt “Zugriff” von Datenklassen.
Sie würde ohne weitere API-Nutzung arbeiten. Das passt für mich -
und macht es möglich, diese Logik sogar in Operationen zu nutzen!
Operationen dürfen und müssen ja von Daten abhängig sein, selbst wenn
die Funktionen mit Logik anbieten.
Modularisierungsbeispiel
Als erstes Modularisierungsbeispiel lass uns mal den 2-dimensionalen
Datenfluss zur Beurteilung der Glaubwürdigkeit der Testergebnisse an-
schauen. Hier ist mein abschließender Datenfluss aus der Musterlösung:


---


<!-- Page 280 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 271
Welche Klassen lassen sich daraus ableiten, wenn ich bottom-up vorgehe?
Eine ist klar, das ist die für Main: die Funktionseinheit gehört zu Pro-
gram{} (in C#). Aber was ist mit den Funktionseinheiten darunter?
• Ich fange mit Parse an, weil sie für mich zur schematischen
Peripherie gehört. Deshalb schlage ich sie der Klasse UI{} zu.¹⁵⁴
• Gibt es noch eine Funktionseinheit, die ich unter UI{} subsummie-
ren könnte? Ja, für mich gehört Display auch dazu. In diesem
kleinen Beispiel sind sich Parse und Display so ähnlich vom
Zweck her, dass ich sie zusammenfasse. Zwar benutzen sie nicht
denselbenAPI,dochbeidedienenderInteraktionmitdemBenutzer.
Wenn die Logik in den Funktionseinheiten anwachsen sollte im
Verlauf einer Weiterentwicklung, würde ich allerdings hier mit
verschiedenen Klassen differenzieren.
• Wozu gehört Heraussuchen? Auch dort ist ein API im Spiel:
es findet Dateizugriff statt. Das passt allerdings nicht zum UI{}.
¹⁵⁴In der Musterlösung sind Parsen und Display getrennt. Dort habe ich für die
KommandozeileeineeigeneKlassegewählt,diedieKommandozeilealsDatenstrukturreprä-
sentiert.HierwähleichmaleinenanderenWeg,umdieAlternativezuzeigen,dieindiesem
Zusammenhangnichtwirklichschlechterist.FürdieAbhängigkeitenimKlassendiagramm
ändertdasamEndenichtsgrundsätzlich.


---


<!-- Page 281 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 272
Für mich ist das eine “dorsale” Interaktion des Service, den das
Programm darstellt; sie ist “nach hinten”, vom Anwender weg
gerichtet. Die Klasse dafür ist die Testdatenbank{}.
• Gibt es weitere Operationen, die zur Testdatenbank{} gehören
könnten? Nein. Der Dateisystem-API wird nirgendwo sonst be-
nutzt. Wohin gehört also Auswerten? Ich sehe kein formales Krite-
rium, nach dem ich zuordnen könnte. Inhaltlich handelt es sich um
dieDomäne.DassdieDomänemiteinerServiceklasserepräsentiert
wird, halte ich für angemessen. Wie könnte die heißen? Mir fällt
Glaubwürdigkeitsbeurteilung{} ein.
• Nur noch Deuten ist als Operation übrig, um einer Klasse zugeord-
net zu werden. Passt sie zu einer bereits definierten? Darin findet
kein API-Zugriff statt, also scheiden Testdatenbank{} und UI{}
aus. Passt sie aber zur Domäne? Es spricht etwas dafür; die Aus-
wertung der Domäne wird dort weiterverarbeitet. Dagegen spricht
allerdings, dass die Deutung nur in spezifischen Weise stattfindet,
weil der Benutzer keine Wahrscheinlichkeiten interpretieren mag.
Sie ist also durchaus interaktionsnah. Das habe ich schon in der
Musterlösung erwogen und mich dann für den obigen Datenfluss
entschieden, indem das ausgedrückt wird, indem sie der Berech-
nung nachgeschaltet ist, ohne auf derselben Ebene wie die Anzeige
zu stehen. Diese “Zwitterstellung” könnte durch eine Serviceklasse
Mapping repräsentiert werden, denn um nichts anderes handelt es
sich. Es wird ein Ergebnis aus Zahlen in eines in Form von Text
umgeformt.
• Allerdings könnte hier auch ein Fall für eine Datenklasse vorliegen.
Deutung{} könnte mit der Auswertung instanziiert werden und
bei der Anzeige wird einfach nur auf den Inhalt in Form eines
Textes zugegriffen, dessen Formatierung Logik in der Datenklasse
vornimmt.
• Datenklassen liegen außerdem für den Test{} und die Auswer-
tung{} schon aus dem Entwurf vor. Da muss ich keine primitive
obsession überwinden. Aber könnten die eine “Bluttransfusion”
vertragen, um wenigeranaemic zu sein? Nein, ich denke nicht, dass
der Test die Auswertung zugeschlagen bekommen sollte; und ich
glaube auch nicht, dass die Auswertung als Datenstruktur für die
Deutung zuständig sein sollte. Ich lasse die Datenstrukturen also
frei von Logik. Nichtsdestotrotz stellen sie ja aber Module dar.
• Nun die Integrationen: Auch hier arbeite ich mich bottom-up vor.


---


<!-- Page 282 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 273
Zu welcher Klasse sollte Berechnen gehören? Die Funktionsein-
heit integriert zwei aus unterschiedlichen Klassen. Sollte sie der
einen oder anderen zugeschlagen werden, einer weiteren, schon
existierenden, oder eine neue Klasse eröffnen? Das ist die bisher
schwierigste Entscheidung, finde ich. Zur Testdatenbank{} ge-
hört Berechnen allerdings für mich gar nicht. Aber auch bei
derGlaubwürdigkeitsbeurteilung{}seheichdieIntegration
nicht, die damit die Domäne abhängig machen würde von der
Persistenz. Also eine dritte Klasse. Bei dieser geringen Projektgröße
würde ich allerdings keine neue aufsetzen, sondern schlicht Pro-
gram{} mit der Integration beauftragen. Bei der IODA Architektur
wirst du dafür allerdings eine eigene Verantwortlichkeit kennenler-
nen.
• Bei Beurteilen mache ich es mir jetzt einfach. Auch hier über-
nimmt Program{} die Aufgabe.
Ergänzt um die Klassen sieht die Datenflusshierarchie nun so aus:
Das ist etwas verwirrend, wenn ich es dir so vorsetze. Ich behaupte aller-
dings,dass es nichtannähernd so schlimmist, wenndu selbstschrittweise
die Module in deine Datenflussmodelle einzeichnest. Eines nach dem


---


<!-- Page 283 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 274
anderen kommt hinzu und macht ja Sinn für dich. Wenn es zu kunterbunt
durcheinandergeht dabei, nimm das als Indikator für eine suboptimale
Modularisierung. Dann solltest du vielleicht einen Schritt zurücktreten
und nochmal über den Datenfluss nachdenken.
In diesem Beispiel habe ich z.B. gestutzt bei der Modularisierung von
Deuten und Auswerten. Beide sind in verschiedenen Strata angesiedelt.
Das war in der Musterlösung ohne Module plausibel. Doch bei der
Modularisierung ergibt sich dadurch vielleicht eine Spannung. Alternativ
hätte ich Berechnen auflösen und Auswerten plus Deuten in einer
Domänenklasse zusammenfassen können. Das hätte allerdings zu einer
Integration beider Operationen geführt, um den Kontrakt der Domänen-
klasse zu verringern.
Nun lasse ich es aber so, weil ich die Idee einer Datenklasse auch nicht
schlecht finde - allemal aus didaktischen Gründen, um dir zu demonstrie-
ren, wie das Flow-Design das Denken mit seiner Visualität anregt.
Wenn du weniger Linien vorziehst, kannst du die Modularisierung auch
mit Farben verdeutlichen. Dass die Funktionseinheiten rot und grün sind,
ist ja nur bisher eine Betonung der Unterscheidung zwischen Integration
und Operation gewesen. Diese Colorierung ist eigentlich nicht nötig.
Nutze Farben lieber für die Modularisierung:


---


<!-- Page 284 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 275
Wie auch immer du Module in einem Datenfluss darstellst, es lohnt sich,
die Module auch nochmal in einem eigenen Strukturmodell herauszuzie-
hen.MiteinigerÜbungimFlow-Designwirstdudaswenigerundweniger
brauchen, weil die Modulhierarchie dir schon im Datenfluss klar sein
wird; doch allemal für den Anfang ist ein separates Strukturdiagramm
keine schlechte Sache. Sieh den Aufwand dafür als Gelegenheit zur
Reflexion über dein Modell an.
In diesem Klassendiagramm habe ich nun die Klassen ebenfalls grün


---


<!-- Page 285 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 276
bzw. rot eingefärbt, wie du es von den Funktionseinheiten im Datenfluss
her kennst. Damit will ich ihren grundsätzlichen Charakter betonen:
Manche Klassen haben vor allem die Aufgabe, zu integrieren, andere
zu operieren. Das bedeutet nicht, dass in einer integrierenden Klasse
keine Operationen stecken können. Eine integrierende Klasse kann also
Logik enthalten - doch die ist eben nicht charakteristisch. Ebenso können
operierende Klassen Integrationsmethoden enthalten. Die Frage ist, was
die grundsätzliche Aufgabe einer Klasse ist: Soll sie eher selbst einen
transformierenden Beitrag in einem Prozess darstellen oder hat sie eher
die Aufgabe, einen Prozess herzustellen?
Diagramme mit Klassen sind vor allem Strukturdiagramme; in ihnen
geht es um Abhängigkeiten. Aber du kannst natürlich auch Flüsse mit
Klassen zeichnen. Dann bekommst du etwas Ähnliches wie UML Se-
quenzdiagramme oder Kollaborationsdiagramme (zusammen stellen sie
Interaktionsdiagramme¹⁵⁵ dar). Es wird dann schwer„ mit den Pfeilen den
“Hergang der Dinge” zu verfolgen; der Prozess sticht nicht mehr heraus.
Deshalb kann eine Nummerierung der Flüsse helfen. Insgesamt finde ich
diese Darstellung jedoch wenig hilfreich und benutze sie fast nie.
Sobald du die Struktursicht eingenommen hast, fällt es dir auch leichter,
höhere Modul-Ebenen zu erklimmen. Im Datenfluss würde ich nicht über
Klassen hinausgehen. Aber der Abhängigkeitsbaum der Klassen ist die
Darstellung, in der du zu Bibliotheken oder Paketen zusammenfassen
kannst.¹⁵⁶
¹⁵⁵https://www.tutorialspoint.com/uml/uml_interaction_diagram.htm
¹⁵⁶WeiterhochdieModul-Hierarchiewillichhiernichtgehen.DasVorgehenändertsich
nichtgrundsätzlichfürPaketeausBibliothekenundKomponentenausBibliothekenusw.


---


<!-- Page 286 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 277
KlassenzuBibliothekenzusammenfassen
ResultierendeAbhängigkeitenzwischenBibliotheken


---


<!-- Page 287 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 278
Reflexion
Ohne Modularisierung geht es nicht. Aber Modularisierung ist nochmal
einganzeigenerAspektdesEntwurfs.HiergibteswiederOrdnungshierar-
chien,aberdawirdesdannauchtechnisch.Dochandersistdiewachsende
Zahl von Funktionen nicht beherrschbar.
Im praktischen Entwurf ist die Datenflussmodellierung, die ich dir hier
insbesondere vorstellen will, meist auf die Modulebenen Klasse und
Bibliothek beschränkt. Höhere Modul-Abstraktionen werden in einem
separatenEntwurfbetrachtet,deroftzur“ordentlichen”Softwarearchitek-
tur gerechnet wird. Da ist dann auch die Verteilung von Logik ein Thema.
Weil da jedoch mehr Plattformabhängigkeit und Technologiekenntnisse
ins Spiel kommen, lasse ich diese “höheren Ebenen”, den grobgranularen
Entwurfhieraußenvor.IndemTagesgeschäfthastdudamitauchweniger
zu tun. Flow-Design wie hier vorgestellt soll dir dort aber vor allem
dienen.
Aber auch ohne tiefe Modulschachtelungen erscheinen dir die Entwürfe
hier womöglich etwas durcheinander. Doch wie gesagt: das ist Absicht. In
den Handzeichnungen steckt eine gewollte Vorläufigkeit, dito im Durch-
einander.
Doch das Durcheinander ist immer nur ein Durcheinander für den, der
nicht dabei war. Wer dabei war, als ein Entwurf entwickelt wurde,
der kennt die schrittweise Entwicklung. Für den gibt es neben dem
visuellen Entwurf noch ein zusätzliches mentales Modell. Das ist nicht
vermeidbar und sollte immer einkalkuliert werden. Deshalb sind UML-
Reinzeichnungen auch so schwer “über den Zaun” zu werfen für eine
Implementierung durch bisher Unbeteiligte. In keinem Diagramm steckt
alles,waszuwissennötigistfüreineCodierung.AllemaldasWarumfehlt,
selbst wenn Was und Wie zu sehen sind.
Deshalb glaube ich daran, dass die durcheinander aussehenden Entwürfe
nur Gedächtnisstützen und Spiekzettel sind. Sie wollen durch jemanden,
der damit vertraut ist, interpretiert werden. Bei einer Übergabe sind
sie in eine Story zu verpacken. Wie bei einer Moritatentafel, die der
Bänkelsänger vorträgt, braucht es bei Entwurfszeichnungen jemanden,
der das Publikum durchführt.


---


<!-- Page 288 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 279
Insofern sind Flow-Design Entwürfe auch immer vergleichsweise klein.
Du sollst nicht tagelang an einer riesigen Wandfläche mit einem Entwurf
sitzen, bist du mal wieder etwas implementierst. Die Form selbst soll dich
zu kleineren Inkremeten anhalten.
Entwürfen sollen nur soviel Klarheit haben, dass du sie erklären und/oder
codieren kannst. Und du wirst feststellen, dass du sie noch nach Tagen,
gar Wochen verstehst - nicht trotz, sondern wegen des Durcheinanders.
Meine Theorie dazu ist, dass das Durcheinander eine Individualität hat,
quasi eine Signatur ist, die jedem Entwurf etwas verleiht, das dir gut im
Gedächtnis bleibt. Jedenfalls ist das meine Erfahrung.
Und falls es mal nicht so sein sollte und du Mühe hast, den Entwurf
zu entziffern… dann nimm das als Gelegenheit, ihn nochmal abzumalen
und dabei zu überprüfen. Ist er immer noch stimmig? Oder hast du neue
Erkenntnisse und der Entwurf sollte angepasst werden. “Unordentliche”
Entwürfe regen zu vermehrter aktiver Beschäftigung an. Das ist gewollt.
Sie sollen sich der Vorstellung, dass da etwas in Stein gemeißelt sei,
widersetzen.
Das gilt auf allen Ebenen: alles ist letztlich vorläufig. Integrationen sollen
es dir z.B. leicht machen, Verhalten durch schlichte Komposition von
Abstraktionen immer wieder neu herzustellen.
Einerseits. Denn andererseits brauchst du auch Stabilität. Die ist nicht
Sache der Datenflüsse, sondern der Module. Module sollen nicht nur
Übersicht durch Aggregation schaffen, sondern auch Stabilität durch
Grenzziehung bieten. Dass diese Grenzen nicht impraktikabel a priori
gezogen werden, ist der Beweggrund hinter dem Vorgehen von Flow-
Design: Zuerst die Flüsse, dann die Module. Denn nur wenn Flüsse
und fließende Daten bekannt sind, ist zu sehen, was wie in Prozessen
zusammenhängt, was gebraucht wird, was sich ähnlich ist und nah sein
sollte-oderwasebennichtähnlichistundsichfernseinsollte.Wostecken
Details, die es zu verbergen gilt? Wo wird Funktionalität hergestellt, die
weiterreichend gebraucht wird?
Dieses Vorgehen, das der mainstream Objektorientierung eher entgegen-
gesetzt ist, macht einen guten Teil von Flow-Design aus. Flow-Design
kennt auch die Aspekte Verhalten und Struktur; es stellt jedoch wohlbe-
gründet das Verhalten an den Anfang und ordnet ihm die Struktur nach.


---


<!-- Page 289 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 280
Ich hoffe, dass dir diese Herangehensweise so viel mehr Geradlinigkeit
bringt bei der Softwareentwicklung, wie mir.


---


<!-- Page 290 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 281
Übungsaufgaben
Reflexionsaufgabe
Bitte formuliere eine Frage oder eine Erkenntnis zum Kapiteltext.
• Wo bist du gedanklich hängengeblieben, was ist dir unklar,
was passt für dich irgendwie nicht zusammen, wozu würdest
du dir noch etwas mehr Erklärung wünschen? Steht irgendet-
waszudeinerbisherigenPraxisimWiderspruchunddufragst
dich, warum du etwas ändern solltest?
• Oder: Wann hast du einen Aha-Moment gehabt, was ist
diralsbemerkenswert,spannend,ausprobierenswertaufgefal-
len? Hat irgendetwas “in dir Klick gemacht”, weil dir nun ein
Zusammenhang aufgegangen ist? Oder verstehst du jetzt aus
deiner bisherigen Praxis irgendetwas besser?
Am besten formulierst du Frage bzw. Erkenntnis schriftlich. Indem
du deine Gedanken aufschreibst, wirst du dir ihrer bewusster. Bei
einer Frage kommst du dadurch vielleicht schon einer Antwort aus
dir selbst heraus näher. Bei einer Erkenntnis fällt dir vielleicht schon
etwas ein, das du ab jetzt anders machen kannst.
Aufgabe 1 - Datenfluss modularisieren
Modularisiere den folgenden Datenfluss zur Nettozeilenzählung wie
in der Musterlösung von Kapitel 5 vorgestellt:


---


<!-- Page 291 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 282
1. Zeichne die Klassen in den Datenfluss ein.
2. Zeichne anschließend ein reines Klassendiagramm.
3. Fasse die Klassen zu Bibliotheken zusammen.
Aufgabe 2 - Game of Life
EntwirfeinProgramm,dasdienächstenNGenerationeneinerGame-
of-Life Welt berechnet. Eine ausführliche Darstellung der Idee von
Game-of-Life findest du bei Wikipedia.
Oberfläche
Das Programm soll auf der Kommandozeile aufgerufen werden
können wie folgt:
1 $ gol 3 world.txt
2 ...
3 $
DasErgebnissindindiesemFallDateienmitdenNamenworld-1.txt,
world-2.txt, world-3.txt mit den berechneten Generation im
selben Format wie die Eingangsdatei.


---


<!-- Page 292 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 283
Für jede Generation gibt das Programm einen Punkt als Fortschritts-
indikator aus.
Dateiformat
Eingabe- und Ergebnisdateien bestehen aus Textzeilen, in denen
leere/tote Zellen durch ein . repräsentiert werden und lebendige
durch ein X. Für
wäre der Dateiinhalt
1 .....
2 .....
3 .XXX.
4 .....
5 .....
Alle Zeilen in einer Datei sind gleich lang. Die Zahl der Zeilen muss
aber nicht der Zeilenlänge entsprechen. “Welten” müssen also nicht
quadratisch sein.
TODOs
Entwirf “nach den Regelen der Kunst” des Flow-Design. Was gehört
dazu? Hier zur Erinnerung:
1. Lösungsansatz
2. Modellieren
1. Zerlegungsbaum
2. 2-dimensionaler Datenfluss
3. Modularisierung
1. KlassenzuerstindenDatenflusseinzeichnen,dann
als Strukturdiagramm.
2. BibliothekenalsStrukturdiagrammmitihrenKlas-
sen.


---


<!-- Page 293 of 584 -->


06-Flow-DesignmitmodularisiertenDatenflüssen 284
Und wenn du danach noch Lust haben solltest… dann kannst du
deinen Entwurf natürlich auch codieren, um zu sehen, ob deine
Bubbles crashen oder die Lösung Hand und Fuß hat.
https://en.wikipedia.org/wiki/Conway’s_Game_of_Life
Schön wäre es, wenn die Punkte während der Herstellung der Genera-
tionen ausgegegeben würden. Wenn es aber einfacher ist, die erst hinterher
auszugeben,dannistauchdasok.


---


<!-- Page 294 of 584 -->


07 - Flow-Design mit
3-dimensionalen
Datenflüssen
Mit2-dimensionalen,hierarchischenDatenflüssenkannstduschonskalie-
ren. Integrationen und dazu noch Module sind treffliche Ordnungsmittel,
um auch bei wachsender Zahl von Funktionseinheiten den Überblick zu
behalten. Also keine Angst, dass dir die durch IOSP und PoMO kleiner
werdenden Funktionseinheiten über den Kopf wachsen.
Dennoch lassen die Datenflüsse noch etwas vermissen. Es fehlt ihn eine
gewisse Natürlichkeit. Die hierarchische Linearität ist etwas “ßteif”, wie
man in Hamburg sagen würde. Da ist kein Raum für “Ausbrüche”, für
Nebenflüsse, kurz für parallele Geschehen. Bisher haben die Datenflüsse
nur einen Hauptarm, der aus der “Reihenschaltung” der Operationen
bestünde, wenn es denn keine Hierarchie gäbe, die das verschleiert.
Reale Flüsse jedoch, die fließen mal auseinander, mal zusammen, mal
spaltet sich ein Seitenarm ab, um sich später wieder mit dem Hauptarm
zu verbinden. In der Natur hat das mit dem Terrain zu tun, durch das
das Wasser fließt. Es besteht eine Co-Evolution zwischen Fluss und
Geographie: Zuerst führt der Boden das Wasser, dann formt das Wasser
den Boden und so verändert sich auch wieder der Wasserfluss.
Bei Datenflüssen sind es die Anforderungen, die den Flusslauf formen.
Und manchmal wäre da vorteilhaft, wenn der Flusslauf sich auch zu ihrer
Erfüllung teilen könnte. Zum Glück geht das und ist zeichnerisch ganz
einfach und naheliegend. Bei der Implementation wird es allerdings ein
wenig knifflig. Deshalb stelle ich dir mehrarmige Datenflüsse auch erst
jetzt vor. Früher waren sie für mich die 2. Dimension, aber ich habe
gemerkt, dass es motivierender und hilfreicher ist, zuerst die Hierarchie
einzuführen. Also spannen erst Datenflüsse mit mehreren Armen 3-
dimensionale Datenflüsse auf:


---


<!-- Page 295 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 286
Eine solche Darstellung sieht für dich wahrscheinlich erstmal trivial aus
und vielleicht hast du solche Datenflüsse sogar schon vermisst. Doch es
gibt einen Grund, warum ich damit gewartet habe…
Die wahren Übersetzungsverhältnisse
Lass mich reinzoomen in die Datenflüsse. Bisher hast du es mit Transfor-
mationen dieser Art zu tun gehabt:
Das bedeutet: Die Funktionseinheit erzeugt für jedes a ein b. Ob sie
zwischen eintreffenden a-Reizen auch noch aktiv ist, ist erstmal egal; sie


---


<!-- Page 296 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 287
könnte es sein, weil es sich ja um einen Datenfluss handelt, aber sie muss
es nicht. Die Darstellung symbolisiert nur ein Input-Output-Verhältnis.
Dasselbe gilt auch in diesen Beispielen:
Auf einen Reiz folgt eine Reaktion. Das ist natürlich und leicht zu verste-
hen, oder? Deshalb hast du auch bisher noch nicht den Eindruck gehabt,
dass es sich um “echte” Datenflüsse handelt; die Modelle konnten leicht
in Kontrollflüsse übersetzt werden. Das Mapping dafür war trivial: Jede
Funktionseinheit wurde zu einer Funktion mit dem Input als Parameter
und dem Output als Resultat.


---


<!-- Page 297 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 288
1 int f(string a) {...}
2
3 List<int> g(string[] a) {...}
4
5 string[] h(string a) {...}
So sollte es auch sein. Das ist ein guter Einstieg in eine andere Denkweise.
Ich wollte es dir leicht machen. Nichts ist falsch daran, meistens kannst
du in dieser Weise übersetzen.
Ultimativ ist diese Übersetzung jedoch begrenzend. Sie wird der Natur
des Datenflusses nicht gerecht. Die Übersetzungsverhältnisse habe ich für
dich nur zunächst vereinfact.
In Wirklichkeit wird jedoch nicht die Funktionseinheit, d.h. “der Kringel”
übersetzt. Die wahren Übersetzungsverhältnisse sind differenzierter: In-
put und Output werden getrennt übersetzt und es gibt dabei später eine
Wahl, wie du sehen wirst.


---


<!-- Page 298 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 289
• Es wird nicht “der Kringel” zu einer Funktion, sondern der Input.
Der Input definiert eine Parameterliste für eine Funktion, die theo-
retisch auch anonym sein könnte.
• Aber damit man die Input-Verarbeitung leicht anstoßen kann, be-
kommt die Funktion meist den Namen der Funktionseinheit.
Das ist schon ein bisschen anders als die bisherigen Übersetzungsver-
hältnisse; die große Abweichung besteht darin, dass der Output in ein
Funktionsresultat übersetzt werden kann, aber nicht muss.
• Der Output führt zu einem Funktionsresultat mit einem return
in der Funktion - doch das ist nur eine Möglichkeit, Output “abzu-
sondern”. Erinnere dich an das PoMO! Eine Funktionseinheit weiß
nicht, wer sie mit Input befeuert. Aber sie darf auch nicht wissen,
wer ihren Output weiterverarbeitet. Das ist mit der Übersetzung
nach Funktionsresultat + return gegeben.
Mit dieser naheliegenden Übersetzung ist das PoMO eingehalten. Al-
lerdings ist eine Übersetzung damit auch auf synchrone Datenflüsse
festgelegt. Wenn eine Funktion ein Ergebnis mit return zurückgibt, ist
sie beendet. Daten fließen hinaus, die Kontrolle ebenfalls.


---


<!-- Page 299 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 290
Wie gesagt, für viele Datenflüsse ist das ausreichen. Doch eine universelle
Lösung sieht anders aus. Die ist aber gefragt, wenn du mit mehrarmigen
Datenflüssenmodellierenwillst.DennbeimehrarmigenDatenflüssestellt
sich eine Frage:
Was bedeutet das eigentlich?
Funktionseinheit k reagiert auf Input a. Wird aber nun für jedes a ein b
und ein c generiert? Oder wird für ein a ein b oder ein c erzeugt? Oder
kann es womöglich sein, dass auf ein a weder ein b noch ein c erzeugt
werden? Diese letzte Frage hättest du auch schon in 1-dimensionalen Da-
tenflüssen stellen können: Muss für jeden Input ein Output hinausfließen
- oder kann ein Input auch “verschluckt werden”?
Mit der Übersetzung nach Rückgabewert + return sind diese Fragen
sinnlos. Erstens gibt es nur einen Rückgabewert, zweitens muss immer
genau einer geliefert werden; ein return ist zwingend erforderlich.
Sobald jedoch mehrere alternative oder “parallele” Ausgaben ins Spiel
kommen, ändert sich die Lage. Plötzlich sind diese Fragen relevant. Zum
Glück gibt es darauf im Flow-Design eine Antwort:
Streams
ZuerstsolltedieDarstellungdifferenzierterwerden.Dumusstausdrücken
können, was da jetzt eigentlich so anders ist.


---


<!-- Page 300 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 291
Wenn eine Funktionseinheit so gezeichnet wird…
…bedeutet das weiterhin: Es fließen b und c pro a immer heraus. Das
bleibt die Semantik - stellt sich nur die Frage, wie “gleichzeitig” zwei
verschiedene Output-Werte herausfließen können.
Wenn du allerdings etwas anderes ausdrücken willst, wenn du darstellen
willst, dass ein Output möglich, jedoch nicht zwingend ist, wenn du
Optionalität brauchst, dann musst du das speziell darstellen:
Hier entsteht als Reaktion von m auf a ein Strom von b-Werten. Mehrere
einzelnebfließenausmheraus.Daskönnen2,5,100.000oderauchnur1b
sein-undsogarkeinbistmöglich.Flow-DesignbezeichnetdasalsStream
im Gegensatz zu einer Liste oder Collection, wie du sie bisher kennst.
Achte auf die Feinheit in der Notation:


---


<!-- Page 301 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 292
• Bei einer Liste steht der Stern innerhalb der Klammer; es fließt
einmal etwas heraus - dafür steht die Klammer -, das besteht
allerdings aus einer Menge gleichartiger Elemente.
• Bei einem Stream steht der Stern außerhalb der Klammer! Es fließt
mehrfach das heraus, was in der Klammer steht.
Eine Funktionseinheit kann nur einen “Ausfluss” haben und darauf ihren
Output als Stream “ablassen” - oder sie kann mehrere “Ausflüsse” haben.
Oft ist damit gemeint, dass Output entweder aus dem einen oder aus dem
anderen hinausfließt. Das bedeutet, das auf dem jeweils anderen nichts
hinausfließt. Und daraus folgt, dass solche alternativen Ausgänge Ströme
erzeugen müssen; sonst ließe sich nicht kein Output generieren.


---


<!-- Page 302 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 293
Einsatzgebiete für Streams
Bisher bist du recht gut ohne Ströme nur mit Listen ausgekommen. Damit
istdieMengenbehandlungsehrschönmöglich.Sieerlaubenes,Datenflüs-
se schleifenfrei zu halten. Wann solltes du ihnen Streams vorziehen?
• Der ursprüngliche Beweggrund für Streams sind Verzweigungen.
Ohne Streams sind Verzweigungen nicht unter Einhaltung von
IOSP und PoMo möglich. Du willst erstens in einer Integration
keine Kontrollstrukturen haben müssen, um z.B. mit einem if-
else zwei Ausgänge wie oben bein zu implementieren. Außerdem
willst du auch bei mehreren Ausgängen in der Implementation der
Funktionseinheit nicht wissen, an wen downstream der Output
fließt. Das bietet ein Resultatswert mit return - aber mehrere
ganz verschiedene und alternative Ausgänge lassen sich darüber
nurschwerimplementieren.¹⁵⁷Wiedusehenwirst,verallgemeinern
Streams die PoMO-konforme Ausgabenerzeugung. Ein Rückgabe-
wert und return sind demgegenüber nur ein Sonderfall.
¹⁵⁷Mit einem union type in einer FP-Sprache wie F# “lässt sich da ‘was machen”. In
einer OO-Sprache entspricht dem eine Hierarchie von Datenklassen. Doch damit ist die
Fallunterscheidung für die Behandlung der unterschiedlichen Resultate unterschiedlichen
Typs über den einen Ausgang nur vertagt. Sie muss wohl wieder in der Integration
stattfindenmiteinerFallunterscheidung.


---


<!-- Page 303 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 294
• Ein zweiter Grund für Ströme sind sozusagen “einarmige Ver-
zweigungen”. Bei einer alternativen Verzweigung fließt auf einem
Ausgang ein Ergebnis heraus, auf den anderen aber nicht. Die
“einarmige Verzweigung” hat nur einen Ausgang - doch auf dem
muss eben nicht zwingend ein Output für einen Input herausflie-
ßen. Du kannst so eine Funktionseinheit als Drossel ansehen: Es
kann viel Input hineinfließen und nur gelegentlich lässt sie ihn
- transformiert oder nicht - durch. Wichtig ist hier zu verstehen,
dass eben für manchen Input wirklich nichts herausfließt. In einer
Drossel (oder auch einem Filter) kann dabei Zustand zum Einsatz
kommen; vielleicht werden Inputs miteinander verglichen, um zu
entscheiden, ob ein Output erzeugt werden soll.
• Listen sind sehr bequem in der Implementierung. Ich kann dir emp-
fehlen, sie Strömen vorzuziehen, wann immer es geht; lass Listen
der Default für dich sein. Manchmal allerdings stehen sie einer
effizienten Implementierung im Wege. Das ist zum Beispiel der Fall,
wenn eine Funktionseinheit eine sehr große Menge von Elementen
erzeugt, gar eine unbekannt große Menge. Ein Beispiel könnte bei
der Nettozeilenermittlung die Menge der Dateien sein. Vielleicht
handelt es sich um Hunderte oder gar Tausende? Die zuerst zu
sammeln, um sie in einer Liste en bloc weiterzuverarbeiten, könnte
großen Speicherverbrauch auf einmal nach sich ziehen. Vergleiche
die folgenden Datenflüsse im Hinblick auf Speichereffizienz und
Verständlichkeit. Der erste ist vielleicht der verständlichste, doch


---


<!-- Page 304 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 295
bei größerer Anzahl von Dateien wird er keinen Spaß machen. Der
zweite ist speichereffizient, aber auf Kosten der Verständlichkeit/-
Ordnung: die Persistenz ist auseinander gerissen, um so spät wie
möglich den Speicher für die Dateiinhalte zu brauchen. Der dritte
schließlich ist im Grunde genauso verständlich wie der erste, hat
sogar noch den Vorteil, ohne dark logic auszukommen, und ist
speichereffizient wie der zweite.
NettozeilenzählungmitListen
…mitListenundabgespaltenerDateiinhaltsbeschaffung
…undmitStreams
• Große Mengen kommen oft auch mit einer großen Latenz daher:
Es dauert einfach, bis alle Elemente beschafft sind. In einem Da-
tenfluss ist währenddessen viel Aktivität in einer Funktionseinheit


---


<!-- Page 305 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 296
und keine in denen downstream von ihr. Warum soll downstream
auf eine Liste von Elementen gewartet werden? Es könnte in
einem Datenfluss, wo die Kontrolle gleichzeitig überall sein kann,
schon downstream mit der Verarbeitung von Elementen begonnen
werden, sobald welche beschafft wurden. Die Beschaffung kann
danach parallel weitergehen, während erste Elemente schon ver-
arbeitet werden. Das ist im Grunde das Problem der Game-of-
Life Fortschrittsanzeige: Es soll schon Fortschritt sichtbar gemacht
werden, während noch an weiteren Generationen gearbeitet wird.
Deshalb musste ich die Fortschrittsausgabe “nach unten drücken”.
Mit Streams ist das anders lösbar: Jetzt kann die Fortschrittsanzeige
viel weiter oben liegen, ohne die Einzelverarbeitung von Genera-
tionen zu stören; die Abhängigkeiten zwischen den Modulen sind
dadurch entspannt.
MiteinemStreamkanndieFortschrittsausgabeausdenTiefendesDatenflussesheraufgeholt
werden.


---


<!-- Page 306 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 297
ZirkuläreAbhängigkeitenwerdendurchdenStreamvermieden.
• Die Zeit ist auch aus anderen Gründen im Spiel. Vielleicht kann
Output nur unregelmäßig oder mit ungewissem zeitlichen Abstand
produziert werden? Das ist z.B. immer der Fall bei Benutzerinterak-
tionen.EinUIwirdangezeigt,derBenutzerhatmehrereMöglichkei-
ten, einmalig oder wiederholt zu interagieren - doch wann passiert
das? Das lässt sich am besten mit Streams modellieren. Weil die
dir bisher nicht bekannt waren, war für die Beispiele auch nur eine
Interaktion nötig, die mit einem Programmlauf abgeschlossen war.
Nicht alle Anwendungen, an denen du arbeitest, sind jedoch Batch-
ProgrammeoderREST-Services,wonurjeweilseineInteraktionzur
Zeit zu betrachten ist. Nachfolgend ein Datenfluss für das Hello-
World Beispiel unter der Annahme, dass das Programm einmal
gestartet wird und dann in einer Schleife die Namen erfragt:
• Und schließlich gibt es Fälle, in denen Streams schlicht der bessere
Ausdruck für die Verarbeitung von Daten sind. Sie erlauben “das


---


<!-- Page 307 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 298
Zurückschalten” von Mengenverarbeitung mit Listen auf Einzel-
verarbeitung.EineFunktionseinheitkannals“Vereinzelungsanlage”
aufgesetzt werden. Statt einzelne Elemente tiefer in einer Daten-
flusshierarchie zu verarbeiten, schaltest du den Prozess einfach
downstream dahinter.
“Serienschaltung”stattSchachtelungmiteinenStream
Parallelverarbeitung mit Streams
EinspeziellesThemafälltnochindasReichderStreams:dieParallelverar-
beitung. Hier möchte ich nicht so tief darauf eingehen, weil es sich um ein
ThemaderVerteilungvonLogikhandelt,dasnochmaletwasganzanderes
ist als die Komposition und die Aggregation. Zwei Sichtweisen auf die
Parallelverarbeitung möchte ich dir jedoch kurz mit Skizzen vermitteln.
Da ist zum einen die asynchrone Verarbeitung “in Reihenschaltung”. Soet-
waskannz.B.beigrafischenBenutzerschnittstelleninteressantsein,damit
das UI nicht einfriert. Du verlagerst die Eingabeverarbeitung einfach in
den Hintergrund. Es gibt dann zwei Threads: einen Vordergrund-Thread


---


<!-- Page 308 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 299
fürdasUIundeinenHintergrund-ThreadfürdieVerarbeitung.DieLatenz
der Verarbeitung wird damit verborgen. Der Benutzer kann womöglich
während der Hintergrundverarbeitung weiter mit anderen Teilen des UI
interagieren.
MitFarbenkönnenThreadssehreinfachinDatenflüssendargestelltwerden.
Eine Besonderheit bei solcher Auslagerung in den Hintergrund kann
sein, dass du darauf achten musst, das Ergebnis aus dem Hintergrund-
Thread in den Vordergrund-Thread zu heben; du brauchst vielleicht eine
explizite Synchronisation. Das ist aber ein technisches Detail deines UI-
Framework.
MitDatenflüssenundStreamskannstaberauchLatenzverringern,indem
du Elemente nebenläufig verarbeitest. Dazu nochmal die Nettozeilenzäh-
lungalsBeispiel.WarumdieDateiennacheinanderverarbeiten?Wenndie
Dateianalyse länger dauern sollte, könnten auch 2, 3 oder mehr Dateien
parallel in Arbeit sein.


---


<!-- Page 309 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 300
Ein Scatter-Gather Datenfluss: Die Dateiverarbeitung wird auf mehrere Threads verteilt
(scatter); später werden die Ergebnisse der Threads gesammelt (gather) und erst bei Voll-
ständigkeitweitergeleitet.
Hier stellt sich dann eine Frage ganz offensichtlich, die ich bisher nicht
angesprochen habe: Wie wird eigentlich ein Stream-Ende mitgeteilt? Wie
weiß die downstream Verarbeitung, wann das letzte Element eingetroffen
ist?
Für manche Szenarien ist das uninteressant; ein Beispiel ist die Fort-
schrittsanzeige des Game-of-Life: Wenn keine Generation mehr gemeldet
wird, wird keine mehr gemeldet; niemand wartet darauf.
In anderen Szenarien ist es jedoch wichtig zu wissen, wann das letzte
Element eines Stroms “reingerauscht ist”; vielleicht muss dann eine ab-
schließende Transformation stattfinden. Bei Listen ist das kein Problem,
weil sie immer komplett mit allen Elementen angeliefert werden.
Zwei Ansätze liegen dafür nahe:
• Es kann das Stream-Ende durch ein explizites end-of-stream (EOS)
Element angezeigt werden.
• Oder es kann die Anzahl der zu erwartenden Elemente “nach
vorne gemeldet werden” von der Funktionseinheit, die die Anzahl
kennt.DannkanndownstreamangeeigneterStelledaraufgewartet
werden, dass eben so viele Elemente “vorbeigerauscht sind”, um
noch eine abschließende Aktivität zu entfalten.
Den zweiten Ansatz zeigt die obige nebenläufige Nettozeilenanalyse. Die


---


<!-- Page 310 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 301
Zeilenzählung kann erst die Gesamtzahl melden, wenn verlässlich alle
Dateien verarbeitet wurden.¹⁵⁸
Der erste Ansatz käme wohl eher zum Einsatz, wenn zwar die Nettozei-
lenzählung mit Streams erfolgte, aber ohne Parallelverarbeitung. Dann
könnte einfach nach der letzten Datei ein EOS-Datum durch die Verarbei-
tungfließen,woesnichtbeachtetwürde,umbeiderZählungdieFreigabe
der Nettozeilensumme zu veranlassen. Die Zählung am Ende hat dann als
Drossel fungiert.
An dieser Stelle noch ein Wort zum Übergang von Output zu Input: Wenn
eine Funktionseinheit einen Stream erzeugt, dann hat das zunächst und
meistens nur auf sie einen Einfluss. Downstream ist nichts vom Stream
zu bemerken; dort tauchen einfach nur einzelne Datenelemente auf. Die
Realität sieht also eigentlich wie folgt aus:
¹⁵⁸Im Detail muss bei der zusammenfassenden Funktionseinheit natürlich darauf gewar-
tetwerden,dassbeideInformationenvorliegen.InwelcherReihenfolgedasderFallist,lässt
sichnichtimmervorherbestimmen;deshalbsolltesierobustseinundsowohldamitzurecht
kommen, dass zuerst die zu erwartende Elementzahl bekannt ist und dann diese Anzahl
Elementeeintrifft,wieauchdamit,dassschonalleElementeeingetroffenseinkönnen,ohne
dass die Anzahl schon bekannt war; in dem Fall geht es erst weiter, wenn auch die Anzahl
vorliegt.


---


<!-- Page 311 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 302
Doch das ist umständlich zu notieren und auch selbstverständlich. Zeige
es also nicht explizit in deinen Datenflüssen an; ich mache das auch nicht.
Es ist ein Detail, von dem die Notation abstrahiert.
Das erklärt auch, warum gewöhnlich ein Stream “sich nicht fortsetzt”.
Aus g im obigen Diagramm kommt kein Stream heraus, obwohl ja in
der ersten Variante einer hineinzugehen scheint. Mit der unteren Variante
wird klar, warum: Es geht in g gar kein Stream hinein. Überhaupt gibt es
keinen “hineinfließenden” Stream; Streams sind ausschließlich eine Sache
des Output von Funktionseinheiten.
Implementation
Streams sind “das Natürlichste von der Welt” in Datenflüssen; ja, sie
machen Datenflüsse geradezu aus: Es kommen Daten bei einer Funktions-
einheit an und führen dazu, dass die beliebige viele Daten erzeugt. Die
bisherige 1:1-Beziehung war davon immer nur ein Sonderfall, ein sehr
nützlicher und weitreichender, dennoch nur ein Sonderfall.
MitStreamssindwirimGrundejetztdaangekommen,wowirbeiderradi-
kalenObjektorientierunglosgegangensind.InderAnalogievonAlanKay
- du erinnerst noch die biologischen Zellen? - war keine Beschränkung
enthalten auf “ein Input erzeugt genau einen Output”. Messaging umfasst
alle Datenflüsse, auch und gerade die, in denen Funktionseinheiten mit
verschiedenen und mehreren Nachrichten auf eine empfangene reagieren.


---


<!-- Page 312 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 303
Das bisherige war sozusagen spezielle radikale Objektorientung, jetzt
kommt die allgemeine radikale Objektorientierung.
Continuation
Ich kann es dir leider nicht ersparen, deshalb setzen ich es besser gleich an
den Anfang. Im Grunde ist es auch nur eine Wiederholung von etwas, das
du schon im Kapitel über die radikale Objektorientierung schon gesehen
hast. Die allgemeine und universelle Übersetzung für den Output von
Funktionseinheiten ist die Continuation.
Ein Modell wie dieses
kannst du nicht nur in eine Funktion mit Rückgabewert int übersetzen,
sondern genauso in eine Funktion, die ihren Output über eine Continuati-
on hinausschiebt:
1 void f(strint a, Action<int> onB) {
2 ...
3 onB(...);
4 }
Die Continuation, also der Funktionszeiger, der als zweiter Parameter
übergeben wird, ersetzt die Ergebnislieferung durch return. Indem die
Funktion die ihr übergebene Funktion onB aufruft, meldet sie an “irgend-
wen” einen Output. f ist nicht bekannt, welche Funktion sich hinter onB
verbirgt; damit ist das PoMO erfüllt wie mit return.
Um das zu betonen, sollte der Continuation-Parameter einen Namen
haben, der sich auf f bezieht. Vermeide, die Continuation mit dem zu
bezeichnen, was als nächstes geschieht:


---


<!-- Page 313 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 304
1 void f(strint a, Action<int> display) { // Widerspruch zum PoMO!
2 ...
3 display(...);
4 }
display zieht sich auf die weitere Verarbeitung des Output von f. Das
ist ein Widersprich zum PoMO; jetzt weiß f, dass (früher oder später) der
Output angezeigt werden soll. Im Grunde hat sich damit eine funktionale
Abhängigkeit in f eingeschlichen.
Gravierend ist die zum Glück noch nicht, solange du nicht einen zweiten
Fehler begehst und die Continuation mit einem Rückgabewert ausstattest:
1 void f(strint a, Func<int,bool> check) { // Widerspruch zum PoMO!
2 ...
3 if (display(...))
4 ...
5 }
Jetzt ist die funktionale Abhängigkeit unzweideutig und hinderlich. Der
Fortgang der Verarbeitung innerhalb von f ist abhängig davon, was
außerhalb passiert.
Das kannst du schon so machen… nur handelt es sich damit nicht mehr
umeinenFunktionszeigerfüreinenOutput.DasPoMOistausdemFenster
geflogen und du hast lediglich eine parameter injection für eine Funktion.
Wenn du Polymorphie brauchst, ist das ein legitimes Mittel. Für das
Messaging jedoch ist es nicht tauglich!
Also, wenn ich sage, dass Continuations die allgemeine Implementation
eines Ausgangs einer Funktionseinheit sind, dann meine ich damit Funkti-
onszeiger, die keinen Rückgabewert haben und deren Namen sich auf die
Funktion beziehen, zu deren Parameterliste sie gehören.
“Continuation” wird ein solcher Funktionszeiger dann genannt, um anzu-
zeigen, dass er dafür steht, wie es weitergeht, how processing continues.
Dieser “Programmierstil” wurde 1975 unter dem Namen Continuation-
passing style (CPS)¹⁵⁹ von eben dem Gerald Sussman mitbegründet, der
auch hinter dem stratified design steckt, das Flow-Design anstrebt.
Einen 1-dimensionalen Datenfluss wie diesen
¹⁵⁹https://en.wikipedia.org/wiki/Continuation-passing_style


---


<!-- Page 314 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 305
kannst du also so übersetzen:
1 void f(string a, Action<int> onB) {
2 ...
3 onB(...);
4 }
5
6 void g(int b, Action<bool> onC) {
7 ...
8 onC(...);
9 }
10
11 void h(bool c) { ... }
12
13 // Aufruf
14 var a = ...;
15 f(a,
16 b = g(b,
17 h));
Dass du das nicht tun würdest, ohne mit der Wimper zu zucken, verstehe
ich. Die Funktionsdefinitionen sind noch harmlos: Wo ist das Problem,
statt eines Rückgabetypen eine Continuation in die Signatur zu setzen?
Eine Continuation aufzurufen, ist auch nicht schwieriger als return zu
nutzen; es ist sogar aus dem Stand flexibler, weil mit der Continuation
mehrfach Resultate geliefert werden können.
Für die Funktionsdefinition ist CPS also ein reiner Gewinn. Genuss ohne
Reue!
Die Nutzung der Funktionen sieht dann allerdings seltsam aus. Wenn du
das ein paar Mal gemacht hast und dich an die Einrückungen gewöhnt
hast, kommt dir auch das recht gut lesbar vor… Dennoch ist die Lesbarkeit
nicht optional. Das will selbst ich eingestehen.
Aber es gibt eben Gelegenheiten, wo es sich lohnt, diesen Preis zu zahlen.
Deshalb sollst du diese Implementation kennenlernen und du solltest mit
ihr auch vertraut sein. Lass sie zu einem gleichwertigen Pfeil in deinem
Köcher werden neben Rückgabewert+ return. Es gibt keinen Grund, auf
KriegsfußmitFunktionszeigernzustehen.ImGegenteil!DieZukunftwird
dir davon ohnehin mehr bescheren - auf die eine oder andere Weise.


---


<!-- Page 315 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 306
InC#undFP-SprachensindFunktionszeigergarkeinProblem.Inanderen
Sprachen sind sie leider nicht first class citizens, Java gehört dazu, in
anderer Hinsicht auch Python. Nicht alle Sprachen machen es auch gleich
leicht, Funktionszeiger zu nutzen, wenn es sie denn schon gibt, oder die
dazu gehörenden “namenlosen” Funktionen - Lambda Funktionen - zu
definieren.LeiderverrauschtderCodeinmanchenSprachendadurch.Das
ist sehr bedauerlich, aber derzeit nicht zu ändern. Bitte lass auch das nicht
dir Continuations komplett verleiden.
Wie oben gesagt, stellen Continuations die allgemeine Übersetzung für
“Ausflüsse” von Funktionseinheiten dar. Solange du ihre verallgemeinern-
den Eigenschaften jedoch nicht brauchst, kannst du natürlich einfacher
übersetzen wie üblich:
1 int f(string a) {
2 ...
3 return ...;
4 }
5
6 bool g(int b) {
7 ...
8 return ...;
9 }
10
11 void h(bool c) { ... }
12
13 // Aufruf
14 var a = ...;
15 var b = f(a);
16 var c = g(b);
17 h(c);
Ich tue das natürlich auch, wo ich kann. Die Universalität der Continua-
tions ist kein Selbstzweck. Da es speziellere Sprachekonstrukte gibt für
häufige Szenarien, können die selbstverständlich eingesetzt werden.
Allerdings rate ich dir bei Nutzung von Rückgabewert + return davon
ab, die Aufrufe zu schachteln:
1 h(g(f(...))); // schlecht lesbar
2
3 h( // ebenfalls schlecht lesbar
4 g(
5 f(...))
6 );
Geschachtelte Funktionsaufrufe sind schlecht lesbar, weil du deine Lese-
richtung plötzlich umkehren musst: Du musst von rechts nach links bzw.
unten nach oben lesen und versuchen zu verstehen.
Auch wenn Continuations die allgemeine Übersetzung für “Ausflüsse”
sind, werden sie also nur in speziellen Fällen eingesetzt. Wo Streams im


---


<!-- Page 316 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 307
Modell stehen, da liegen Continuations nahe. Zu den Einsatzszenarien
gehören:
• verschiedene Ausgaben, Stichwort Zerlegung
• alternative Ausgaben, Stichwort Fallunterscheidung
• optionale Ausgaben, Stichwort Drossel
• vereinzelte Ausgaben, Stichwort Latenz
• umfängliche Ausgaben, Stichwort Speichereffizienz
Lass mich zwei dieser Fälle an einem kleinen Beispiel demonstrieren:
Zahlen addieren
EinProgrammsolleineReihevonZahlenaddieren,diederBenutzer
eingibt.DerBenutzerkanndieZahlenschonaufderKommandozeile
beim Programmstart mitgeben, aber er wird auch vom Programm
nach jedem Ergebnis nach einer neuen Zahlenfolge gefragt.
1 $ addieren
2 Zahlen: 1 2 39
3 42
4 Zahlen: -3 7 129 17
5 150
6 Zahlen: 1 E 4
7 *** Fehlerhafte Zahlenfolge!
8 Zahlen: 1 3 4
9 8
10 Zahlen:
11 $ addieren 1 2 39
12 42
13 Zahlen: 9 8 7
14 24
15 Zahlen:
16 $
DieZahlensindganzepositiveodernegative.InderEingabesindsie
durch Leerzeichen zu trennen. Das Programm wird durch eine leere
Eingabe beendet (oder durch Ctrl-C).
Die Domänenlogik ist trivial. Sobald erstmal die Zahlen in einer Liste
vorliegen, ist eine Summe schnell berechnet. Der Teufel steckt hier in
anderen Details:
• Die Eingabe der Zahlen erfolgt alternativ auf der Kommandozeile
vor dem Programmlauf und über eine Konsoleneingabe während
des Programmlaufs.


---


<!-- Page 317 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 308
• Die Eingabe einer unbekannt großen Menge von Zahlengruppen
kommt vereinzelt, sporadisch.
• Die Eingaben können valide oder invalide sein.
Fallunterscheidungen und Latenz spielen eine Rolle. Die gilt es im Daten-
flussmodell darzustellen:
Den Einsatz von Streams habe ich für dich hervorgehoben. Interessant ist
dabei lediglich, dass Parsen und Zahlen erfragen lange Arme haben,
auf denen nichts hinausfließt. Die habe ich hier der Vollständigkeit mo-
delliert für die Fälle, dass diese Funktionseinheiten feststellen, dass nichts
(mehr) zu tun ist. Im ersten Fall wird dadurch die ganze Verarbeitung
umflossen,damitesbeiderinteraktivenZahleneingabeweitergehenkann;
im zweiten Fall wird dadurch ein Signal an Ende geschickt, auf das das
Programm abgebrochen werden könnte (wenn es nicht ohnehin anhalten
würde, sobald die Schleife in Zahlen erfragen endet).
In den meisten Fällen würde ich diese Alternativen nicht einmal modellie-
ren. Es sind die default Verhaltensweisen. Bei Parsen fließen ja auch alle
drei Arme am Ende zusammen; auf der Integrationsebene sieht man von
ihnennichts;esgehteinfachdanachmiteinem“Signal”anInteraktive
Zahleneingabe weiter.
“Sehenswürdigkeiten” der Implementation sind zunächst zwei Methoden,
die den Output mit Streams implementieren:


---


<!-- Page 318 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 309
1 public void Zahlen_erfragen(Action<string> onEingabe, Action onEnde) {
2 while (true) {
3 Console.Write("Zahlen: ");
4 var eingabe = Console.ReadLine();
5 if (string.IsNullOrWhiteSpace(eingabe)) {
6 onEnde();
7 break;
8 }
9 onEingabe(eingabe);
10 }
11 }
Das ist eine typische Methode in einem Console-UI. Sie enthält ein
while(true)alsmessageloop,wiesiesichineinemGUIautomatischim
Hintergrund dreht. Darin werden Benutzereingaben erfragt und per Con-
tinuation nach draußen geschoben; du könntest auch sagen “publiziert”.
Wer damit weiterarbeitet, ist für das UI nicht ersichtlich.
EndlichsiehstdudamiteinBeispielfürdiewahreNaturvonDatenflüssen:
dass Funktionseinheiten darin alle gleichzeitig aktiv/voll Kontrolle sein
können. Zahlen_erfragen() läuft und läuft und läuft, während sein
Outputparalleldownstreamverarbeitetwird,d.h.Kontrollealsoauchdort
ist.¹⁶⁰
Als zweites Beispiel die Kommandozeilenanalyse:
1 public static void Parsen(string[] elemente, Action<int[]> onZahlen,
2 Action<string> onFehler,
3 Action onKeineElemente) {
4 if (elemente.Length == 0) {
5 onKeineElemente();
6 return;
7 }
8
9 try {
10 var zahlen = elemente.Select(int.Parse).ToArray();
11 onZahlen(zahlen);
12 }
13 catch {
14 onFehler("Fehlerhafte Zahlenfolge!");
15 }
16 }
¹⁶⁰Dasstimmtnatürlichnichtwirklich,weildieKontrollebeiAufrufvononEingabe()
ja hinausfließt und erst zurückkommt, wenn downstream die Verarbeitung abgeschlossen
ist. Doch das ist im Grunde ein Detail. Du kannst Zahlen_erfragen() auch abstrakter
verstehen.FürdieFunktionmachteskeinenUnterschied,obeinAufrufvononEingabe()
dieEingabenurschnellineineWarteschlangestelltundzurückkehrt,damitaufdienächsten
Zahlen gewartet werden kann; in einem anderen Thread könnte eine solche Warteschlange
abgearbeitet werden. Oder ob die Eingabe synchron sofort komplett verarbeitet wird. Die
Continuation hat hier dieselbe Kraft wie Iteratoren mit yield return in C#: der Code
sieht synchron aus, ist damiteasy to reason about, könnte aber auch in einem asynchronen
Verarbeitungsprozesseingesetztwerden.


---


<!-- Page 319 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 310
Die Operation hat drei alternative Ausgänge:
• Entweder die Kommandozeile enthält keine Zahlen, d.h. nichts
muss getan werden (onKeineElemente()).
• Oder die Kommandozeile enthält Parameter, die sich als Zahlen
interpretieren lassen. Die werden dann “hinausgeschoben” via on-
Zahlen().
• Oder die Kommandozeile enthält etwas, was sich aber nicht als
Zahlenfolge interpretieren lässt. Dann wird das via onFehler()
gemeldet.
In allen Fällen weiß das Parsen nicht, woher die Elemente kommen und
wohinseinOutputgeht.JederOutputistoptional;eswirdkeinbestimmtes
Ergebnis produziert; alle sind möglich. Dafür sind Streams/Continuations
ideal.
SoweitdieInnensichtderFunktionseinheiten,dieStreamsausgeben.Aber
wie werden sie benutzt?
1 private static UI __ui;
2
3 static void Main(string[] args) {
4 __ui = new UI();
5
6 Zahleneingabe_auf_Kommandozeile(args);
7 InteraktiveZahleneingabe();
8 }
9
10 private static void Zahleneingabe_auf_Kommandozeile(string[] args) {
11 Parser.Parsen(args,
12 onZahlen: zahlen => {
13 var summe = Mathe.Summieren(zahlen);
14 __ui.Ergebnis_anzeigen(summe);
15 },
16 onFehler: __ui.Fehler_melden,
17 onKeineElemente: () => {}
18 );
19 }
20
21 private static void InteraktiveZahleneingabe() {
22 __ui.Zahlen_erfragen(
23 onEingabe: eingabe => {
24 Parser.Parsen(eingabe,
25 onZahlen: zahlen => {
26 var summe = Mathe.Summieren(zahlen);
27 __ui.Ergebnis_anzeigen(summe);
28 },
29 onFehler: __ui.Fehler_melden
30 );
31 },
32 onEnde: () => {}
33 );
34 }


---


<!-- Page 320 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 311
Ich denke, dieser Anblick wird dich etwas verwirren. Wenn du den
Umgang mit Funktionszeigern und Lambda-Ausdrücken nicht gewohnt
bist, dann reibst du dir bestimmt ein paar Mal die Augen. “Was? Wie geht
das?”
AberesistganzkonsequentundamEndeeinfach.DeinVerständnisistnur
getrübtdurchdieGewohnheit,Funktionengeschachteltaufzurufen.Dann
ist ihre Aufrufreihenfolge ja von rechts nach links und innen nach außen.
Wenn du mit Continuations (allgemeiner: Callbacks oder Funktionszei-
gern) arbeitest, ist es umgekehrt. Du musst dich daran gewöhnen, dass
die Verhältnisse wieder normal sind: Die Integrationen mit Continuations
werden von links nach rechts, von oben nach unten, von außen nach
innen gelesen. Weil es dabei alternative Flüsse geben kann, hat sich
eine Notation bewehrt, in der Continuations eingerückt werden. Dein
Verständnis baust du also mit einem Blick von links oben nach rechts
unten auf; der Datenfluss ist diagonal.¹⁶¹
AlsBeispielZeilen22ff;siespiegelndenDatenflussdesModellswider.Der
“happy path” lautet:
1. Zahlen erfragen (22)
2. Zahleneingabe parsen (24)
3. Geparste Zahlen summieren (26)
4. Ergebnis ausgeben (27)
DiealternativenFlüssefindetduin23(Eingabegetätigt)vs.32(Programm-
ende gewünscht) und 25 (fehlerfreie Eingabe) vs 29 (fehlerhafte Eingabe).
Event-Based Components
Continuations sind universell. Als Parameter skalieren sie aber nicht so
gut, finde ich; wenn es mehr als zwei oder drei sind, dann sieht das am
Nutzungsort nicht so schön aus. Es hat zwar den Vorteil, dass du je Aufruf
unterschiedliche Continuations mitgeben kannst, doch manchmal wird
das Codebild dadurch getrübt.
¹⁶¹Die“leeren”Continuations() => {} sindnur der Vollständigkeithalbervorhanden.
In einer synchronen Abarbeitung des Datenflusses sind diese Streams eigentlich nicht
nötig; ich habe sie nur der Allgemeingültigkeit wegen drin. Bei asynchroner Abarbeitung
bräuchtestdusie.


---


<!-- Page 321 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 312
Eine Alternative zu Continuations als Parameter sind Continuations als
Felder/Attribute(inC#auchEventsgenannt).Damitwirddanneineganze
Klasse (ein Objekt) zu einer Funktionseinheit. Das habe ich früher Event-
Based Component (EBC) genannt und hat vielen Entwicklern gefallen.
Damit kamen Softwaremodelle elektronischen Schaltplänen sehr nahe.
Deshalb auch “Component” in der Bezeichnung, selbst wenn es nicht
um die Modulebene der Komponenten geht; es ging um Bauteile (engl.
component), die “verdrahtet” werden.
Das Summierungsbeispiel damit modelliert könnte so aussehen:
In der Visualisierung haben EBCs ihren Charme, finde ich. Und damals
war es ein erstern Schritt hin zu Messaging im Rahmen der mainstream
Objektorientierung. Durch den Bezug zu Events war die Unidirektionali-
tät des Nachrichtenflusses auch sofort akzeptiert.
Doch EBCs haben am Ende zu viele Nachteile. Sie sind zu schwerge-
wichtig, weil sie auch für kleine Funktionseinheiten eigentlich eine ganze
Klasse benötigen; die Aggregierbarkeit ist geringer. Es schleichen sich in
dieDiagrammeSchleifenein,wieduobensiehst.EBC-Funktionseinheiten
müssenmehrfachinstanziiertwerden,umsieinunterschiedlichenFlüssen
zu verdrahten. Und in der Übersetzung der Integration ist der Fluss viel
weniger sichtbar, auch wenn sie sehr aufgeräumt aussieht:


---


<!-- Page 322 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 313
1 static void Main(string[] args) {
2 var parser = new Parser_EBC();
3 var ui = new UI_EBC();
4 var mathe = new Mathe_EBC();
5
6 parser.OnFehler += ui.Fehler_melden;
7 parser.OnZahlen += mathe.Summieren;
8 parser.OnKeineElemente += () => { };
9
10 mathe.OnErgebnis += ui.Ergebnis_anzeigen;
11
12 ui.OnEingabe += parser.Parsen;
13
14 parser.Parsen(args);
15 ui.Zahlen_erfragen();
16 }
Ausgänge mit Eingängen der EBCs zu verbinden durch simple Zuwei-
sung der empfangenden Funktion an das Continuation-Feld/Attribut,
sieht hübsch aus. Doch wie die Daten konkret von welcher zu welcher
Funktionseinheit wann fließen, verschwimmt. Der Fokus ist auf den
Substantiven, den EBCs, nicht auf den Verben, den Funktionen.
Innerhalb einer EBC sieht es wieder sehr ordentlich aus. Der Kontrakt ist
klar:
• da sind die Funktionen, die Input entgegennehmen - und deshalb
alle void sind,
• da sind die Events, die Continuation-Felder/Attribute, über die
Output hinausfließt.
1 class Parser_EBC
2 {
3 public void Parsen(string[] elemente) {
4 if (elemente.Length == 0) {
5 OnKeineElemente();
6 return;
7 }
8
9 try {
10 var zahlen = elemente.Select(int.Parse).ToArray();
11 OnZahlen(zahlen);
12 }
13 catch {
14 OnFehler("Fehlerhafte Zahlenfolge!");
15 }
16 }
17
18 public void Parsen(string zahlen) {
19 var elemente = zahlen.Split(new[] {' ', '\t'},
20 StringSplitOptions.RemoveEmptyEntries);
21 Parsen(elemente);
22 }
23
24
25 public event Action<int[]> OnZahlen;
26 public event Action<string> OnFehler;
27 public event Action OnKeineElemente;
28 }


---


<!-- Page 323 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 314
Hier und da haben EBCs Vorteile, wenn du merkst, dass in deinen Flüssen
“Subtantive” eine Rolle spielen; das siehst du spätestens bei der Modulari-
sierung. Ein Beispiel ist immer wieder mal die Benutzerschnittstelle. Statt
dass dir eine Aktivität auf der Zunge liegt bei der Modellierung, denkst
du eher an ein Ding.
DiePraxisrelevanzvonEBCsistmeinerErfahrungnachrechtgering,doch
ich wollte dir diese Übersetzungsmöglichkeit nicht vorenthalten. In EBCs
zudenken,istkeineschlechteÜbung;vielleichtliegtdirdasauchzunächst
näher wegen der Analogie zu elektronischen Bauteilen? Probier’ es aus.
Iterator
Ok,ichhabemeineArgumentefür(undwider)ContinuationsalsÜberset-
zungen für Streams vorgetragen. Ja, ich bin der Meinung, dass Continua-
tions cool sind und überhaupt Funktionszeiger in heutigen OO-Sprachen
unterbewertet. Aber ich gebe zu, die Lernkurve kann schon steil sein;
und nicht in allen Sprachen werden Funktionszeiger in gleicher Weise
unterstützt.
In bestimmten Fällen lassen sich Streams zum Glück anders übersetzen.
Wenn es um Speicherplatzeffizienz geht, helfen z.B. Iteratoren. Als Bei-
spiel die Beschaffung der Dateien in der Nettozeilenzählung:
Das Modell definiert einen Stream als Output der Sammlungsphase; denn
wer weiß, wie viele Dateien da zusammenkommen und geladen werden
müssen; das passiert besser einzeln Datei für Datei.
Aber was anschließend? Es können einzelne Nettozeilenzahlen aus der
Analyse herausfließen; immerhin fließen in die Analyse ja auch nur
einzelne Dateien. Der Stream ist lediglich eine Sache des Output, wenn
man es genau nimmt. Dann stellt sich allerdings die Frage nach der
Kennzeichnung des Streamende (EOS).


---


<!-- Page 324 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 315
Oder… die Analyse übersetzt den Stream in eine Liste. Es kommen viele
Elemente hinein und es gehen viele hinaus. Das Verhältnis ist ja auch 1:1:
für jede Dateien wird eine Nettozeilenzahl bestimmt. Eine Liste ist auch
plausibel, oder? Bei einer Liste von Zahlen sollte kein Speicherproblem
mehr auftreten, auch wenn es sich um Millionen von ihnen handelt.
Wie es auch modelliert ist, am Ende soll nur einmal ein Gesamtergebnis
mit der Summe aller Nettozeilenzahlen und der Anzahl der Dateien
geliefert werden. Wenn die Zählung viele Daten bekommt und nicht für
jedes Datum einen Output generiert, dann ist die eine Drossel und sollte
mit eine Stream versehen werden.
Plausibel? Ich hoffe. Aber bei der Übersetzung mit Iteratoren ist das am
Ende eigentlich egal:
1 IEnumerable<string> Sammeln(string pfad) {
2 foreach(var dateiname in Directory.GetFiles(pfad, "*.cs",
3 SearchOption.AllDiretories)) {
4 var datei = new Datei(File.ReadAllLines(dateiname));
5 yield return datei;
6 }
7 }
8
9 IEnumerable<int> Analysieren(IEnumerable<Datei> dateien) {
10 foreach(var datei in dateien) {
11 yield return Bereinigen(datei.Zeilen).Count();
12 }
13 }
14
15 (int n, int m) Zählen(IEnumerable<int> nettozeilenzahlen) {
16 var _ = nettozeilenzahlen.ToArray();
17 return (_.Sum(), _.Count());
18 }
Den Funktionen ist nicht anzusehen, ob sie auf Streams oder Listen
arbeiten. Mit Iteratoren wie IEnumerable<T> lässt sich der Unterschied
kaschieren.DasProgrammiermodellmiteinemforeachistdasselbe.Die
Magie steckt bei C# in yield return. Dadurch wird dem Compiler
angezeigt, einen Zustandsautomaten zu generieren, an dem downstream
“gezogen werden kann”. Die foreach-Schleife in Zeilen 2ff wird erst
wirklich durchlaufen, wenn in Zählen() mit ToArray() am Iterator
nettozeilenzahlen gezogen wird.
Wenn das für dich neu ist und dir der Kopf schwirrt, kann ich das
verstehen. Ich will dir auch nicht wirklich im Detail erklären wie das
funktioniert,sondernesnursoweituntermauern,dassdumirglaubst,dass
es funktioniert. Das Iterator Entwurfsmuster¹⁶² ist lange etabliert. OO-
Programmiersprachenhabenesnurunterschiedlichkomfortabelgemacht,
¹⁶²https://en.wikipedia.org/wiki/Iterator_pattern


---


<!-- Page 325 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 316
es zu nutzen. Unten drunter geht es immer um dasselbe: Erst bei einem
Aufruf von next() auf einem Iterator wird auch das nächste Elemente
geliefert oder eben sogar erzeugt. “Elements on demand” könnte man
sagen. Das passt zu Streams.
Fallunterscheidung in der Integration
Wenn du über die Aufgaben, die ich dir hier gebe, hinausgehst, wirst du
ganz schnell in eine Entwurfssituation geraten, in der du eine Fallunter-
scheidung modellieren willst. Ein 3-dimensionaler Datenfluss wird dir
natürlich vorkommen; für jeden Fall lässt du darin einen Arm entstehen.
DochdannkommtdieStundederWahrheit:Wieübersetztdudas?Esdarf
doch keine Logik in der Integration stehen. Eine Bifurkation übersetzt die
intuitiv mit einem if-else, das natürlich in die Integration gehört.
Nach IOSP ist das nicht erlaubt. Du kannst das if-else stattdessen in
einer Operation nutzen, die zwei Ausgänge hat, die durch Continuations
implementiertsind.EinganztypischesBeispielistdieValidation:diekann
klappen oder fehlschlagen.¹⁶³
Die kanonische Übersetzung sieht dann so aus:
¹⁶³Achte auch das neue Detail in der Datenflussdarstellung: Port-Namen. Du kannst
Eingänge (Input-Ports) und Ausgänge (Output-Ports) an Funktionseinheiten mit Namen
versehen,umimModellklarzumachen,wann/wasdafließt.Meistensschreibeichsoeinen
Port-Namen mit einem führenden Punkt, z.B. .Valide. Port-Namen sind insbesondere in
DatenflussdiagrammenmitKlassen-EBCs-sehrhilfreich.


---


<!-- Page 326 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 317
1 void Validieren(string daten, Action<string> onValide, Action onInvalide) {
2 if (...daten...) // Logik zur Validierung der Daten
3 onValide(daten);
4 else
5 onInvalide();
6 }
7
8 // Integration
9 var x = ...;
10 Validieren(x,
11 onValide: daten => {
12 ... // Behandlung valider Daten
13 },
14 onInvalide: () => {
15 ... // Reaktion auf invalide Daten
16 });
UndschonistdieLogikinderIntegrationvermieden.Siesteckvollständig
in Validieren()und kann dort leicht getestet werden. So ist es “nicht
nur sauber, sondern rein” nach IOSP.
Doch ich verstehe, dass das eben auch umständlich ist. Und wo ist der
Schaden eines kleinen if-else in der Integration? Die könnte doch ganz
einfach so aussehen:
1 var x = ...;
2 // *** Don't try this at home! ***
3 if (...x...) // Logik zur Validierung der Daten
4 ... // Behandlung valider Daten
5 else
6 ... // Reaktion auf invalide Daten
Ja, so könnte die Integration aussehen. Doch die Logik zur Validierung
wäre hier nun gar nicht für sich testbar. Das ist für mich ein no-go. Und
die Abstraktionsebenen wechseln ja auch, wenn der Rest drumherum aus
ordentlichen Funktionsaufrufen besteht.
Nein, nein, das kann ich dir gar nicht durchgehen lassen empfehlen. Aber
es gibt eine Zwischenlösung, die ich akzeptabel finde:
1 bool IstValide(string daten)
2 => ...daten... // Logik zur Validierung der Daten
3
4 // Integration
5 var x = ...;
6 if (IstValide(x))
7 ... // Behandlung valider Daten
8 else
9 ... // Reaktion auf invalide Daten
Jetzt ist die Logik ausgelagert in eine Funktion IstValide(), in der sie
gut testbar ist und für sich verständlich ein Abstraktionsniveau bildet.


---


<!-- Page 327 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 318
DieVerallgemeinerungdieser“lässlichenSünde”ist:EineKontrollstruktur
ohne Ausdruck (Logik) kann ok sein in einer Integration. Das hast du
schon bei foreach gesehen.¹⁶⁴
Ich sage “eine” Kontrollstruktur und meine auch eine, also 1, one, un, uno,
един. Lass diese “Erlaubnis” zur Kontrollstruktur nicht dein Freibrief sein,
Integrationen damit zu pflastern. Eine Kontrollstruktur ohne Ausdruck
ist noch verständlich, übersichtlich und wahrscheinlich testunwürdig.
Sobald du aber mit mehreren, gar geschachtelten beginnst, öffnest du der
Unverständlichkeit und Testnotwendigkeit Tür und Tor. Das macht dann
keinen Spaß mehr.
Das allgemeine Problem hinter der Validation wie oben gezeigt ist die
Klassifizierung. Nichts anderes tut die Validation ja: sie klassifiziert einen
Wert als valide oder invalide. Das lässt sich einfach mit einem boolschen
Wert ausdrücken und ist oft ausreichend. Allgemeiner und oft auch
verständlicher ist jedoch die Übersetzung in eine Enumeration.
Zahlen konvertieren
Ein Programm soll Zahl ins Dezimalsystem konvertieren. Zunächst
geht es um römische, binäre und hexadezimale Zahlen. Die zu kon-
vertierende Zahl wird auf der Kommandozeile bei Programmstart
angegeben; die Ergebnisausgabe erfolgt auf der Konsole.
1 $ konvertieren MCMLXXXIV
2 1984
3 $ konvertieren 1101
4 13
5 $ konvertieren 16
6 22
7 $ konvertieren #11
8 17
9 $ konvertieren C
10 100
11 $
Zu welchem Zahlensystem die zu wandelnde Zahl gehört, ist ge-
wöhnlich an ihren Ziffern abzulesen. Falls es da jedoch wie z.B. im
Fall von 11 (binär oder hexadezimal?) oder C (römisch oder hexdezi-
mal?) eine Mehrdeutigkeit geben kann, kann hexadezimalen Zahlen
¹⁶⁴Aber ein for geht nicht, weil darin die Schleifenvariable immer Ausdrücke zur
Überprüfung und Veränderung braucht. Ebenfalls geht kein while(), weil man zu dessen
Verständnismentalstate aufbauenmuss.DasistbeieinemforeachnichtderFall.


---


<!-- Page 328 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 319
ein#vorangestelltwerden.FehltderPräfix,wirddieMehrdeutigkeit
zu Ungunsten der hexadezimalen Darstellung entschieden.
Das eigentliche Problem bei dieser Aufgabe ist natürlich die Zahlenkon-
vertierung.FürdasFlow-DesignspannenderistjedochdieKlassifizierung.
Welche Art von Zahl liegt an? Wenn das klar ist, kann die passende
Konvertierung gewählt werden.
Hier hat die Klassifizierung drei Ausgänge, auf denen die klassifizierte
Eingabe als Stream hinausfließt, weil ja nicht klar ist, wo überhaupt ein
Outputzuerwartenist.WiedasmitContinuationsübersetztwerdenkann,
ist dir inzwischen klar, denke ich. Hier ein Beispiel mit EBCs:
1 class Klassifikation
2 {
3 public void Klassifizieren(string text) {
4 else if (...)
5 OnRömisch(text);
6 else if (...)
7 OnBinär(text);
8 else
9 OnHexadezimal(text);
10 }
11
12 public event Action<string> OnRömisch;
13 public event Action<string> OnBinär;
14 public event Action<string> OnHexadezimal;
15 }
16
17 // Integration
18 var k = new Klassifikation();
19 var u = new Umwandlungen();
20 var ui = new UI();
21
22


---


<!-- Page 329 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 320
23 k.OnRömisch += u.VonRömisch;
24 k.OnBinär += u.VonBinär;
25 k.OnHexadezimal += u.VonHexadezimal;
26
27 u.OnErgebnis += ui.ErgebnisAnzeigen;
28
29
30 k.Klassifizieren(args[0]);
Das sieht gar nicht so unsauber aus, oder? Klassifikation und Umwand-
lung sind einander sehr übersichtlich zugeordnet. Das spiegelt sich auch
im Modell, wenn ich das mal mit EBCs aufsetze:
Doch wenn du es nicht so hast mit Continuations, dann geht es auch
noch anders. Die Klassifikation liefert ihr Urteil einfach als Wert einer
Enumeration - und wie es damit weitergeht, wird in der Integration
entschieden.
1 class Klassifikation
2 {
3 public enum Klassen {
4 Römisch,
5 Binär,
6 Hexadezimal
7 }
8
9 public static Klassen Klassifizieren(string text) {
10 if (...)
11 return Klassen.Römisch;
12 if (...)
13 return Klassen.Binär;
14 return Klassen.Hexadezimal;
15 }
16 }
17
18 // Integration
19 var text = args[0];
20 var zahl = Klassifikation.Klassifizieren(text) switch {
21 Klassifikation.Klassen.Römisch => Umwandlungen.VonRömisch(text),
22 Klassifikation.Klassen.Binär => Umwandlungen.VonBinär(text),
23 Klassifikation.Klassen.Hexadezimal => Umwandlungen.VonHexadezimal(text)
24 };
25 UI.ErgebnisAnzeigen(zahl);


---


<!-- Page 330 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 321
Auch nicht schlecht, oder? Obwohl hier in der Integration ein C#switch-
Ausdruck steht, also Logik, fällt die Integration nicht negativ auf. Sie ist
verständlich und testunwürdig. Die entscheidende Logik zur Klassifizie-
rung ist immer noch in der Klassifizierungsklasse.¹⁶⁵
Also: Die eine oder andere Kontrollstruktur in der Integration kann dir
den Tag versüßen, allemal wenn sie dir erspart, dich mit Continuations
abzuplagen. So ein bisschen dark logic ist schon ok. Nur halte sie gut
im Zaum. Wenn schon Kontrollstruktur, dann am besten nur ein einzige:
ein foreachoder wie hier ein switch. Auch wenn die Reihe der if-
Anweisungen einem switch entsprechen, würde ich dabei zucken.
Discriminated Unions
In dieselbe Kerbe wie die Übersetzung mit Enumerationen schlagen
Discriminated Unions¹⁶⁶, wie sie aus der Funktionalen Programmierung
bekannt sind - oder in stark vereinfachter Form schon in C existierten.
SolchekurzuniontypesgenanntenTypenerlaubenes,verschiedeneTypen
unter einem Dach zu versammeln.
Eine Enumeration wie diese
1 public enum Klassen {
2 Römisch,
3 Binär,
4 Hexadezimal
5 }
basiert auf demselben Typ - int - für alle Alternativen, greift daraus
jedoch Werte heraus, verbirgt diese hinter einem spezifischen Namen und
versammelt sie unter dem neuen Typdach Klassen. bool macht das im
Grunde auch und könnte so notiert werden:
¹⁶⁵Wenn du es genau nimmst, könntest du allerdings nun einen Widerspruch gegen das
PrinzipDon’tRepeatYourself(DRY)feststellen:EsgibtzweiKontrollstrukturen,dieimGrun-
de dasselbe tun: einmal die Reihe von Fallunterscheidungen in Klassifizieren()und
einmal das switch. In beiden gibt es dieselbe Zahl von Fällen. Das war in der Lösung mit
denContinuationsanders.
¹⁶⁶https://fsharpforfunandprofit.com/posts/discriminated-unions/


---


<!-- Page 331 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 322
1 public enum bool {
2 false,
3 true
4 }
Bei einem union type besteht die Begrenzung auf den Grundtyp int
nicht. Es kann jeder Typ sein bzw. der union type definiert einen eigenen
Grundtyp darauf Typen für dessen alternative Ausprägungen.
Als Beispiel mag eine möglicherweise fehlschlagende Transformation
dienen: Ein Text soll in eine dezimalzahl gewandelt werden. Für "42"
klappt das, für "Hallo!" klappt das nicht. Als Funktionseinheit in einem
Datenfluss sähe das so aus:
Das Problem kannst du wie immer mit Continuations lösen. Damit will
ich dich nun aber nicht wieder nerven. Alternativ kannst du es aber auch
nach einem Muster lösen, wie es z.B. der .NET Framework immer wieder
einsetzt:¹⁶⁷
¹⁶⁷Ichweiß,dassesdafüreineMethodeint.TryParse()gibt.Aberhierwollteichdir
eineImplementationzeigen,damitduselbstdasMusteranwendenkannst.


---


<!-- Page 332 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 323
1 class Zahlenwandlung
2 {
3 public static bool Umwandeln(string text, out int zahl) {
4 zahl = 0;
5 if (text.All(x => char.IsDigit(x)) is false) return false;
6
7 zahl = int.Parse(text);
8 return true;
9 }
10 }
11
12 // Integration
13 if (Zahlenwandlung.Umwandeln("42", out var zahl))
14 ...
15 else
16 ...
Das ist wieder recht sauber, wenn in den beiden Zweigen des if konse-
quent Funktionen aufgerufen werden.¹⁶⁸
Allerdings geht es mit union types noch anders. Dafür definiere ich hier
einen Typ, der sowohl für Erfolg wie Misserfolg steht. Im Erfolgsfall wird
die gewandelte Zahl zurückgegeben, im Misserfolgsfall nichts weiter.
Die unterschiedlichen Typen werden in OO-Sprachen über Vererbung
unter einem Dach vereint:
1 abstract class Ergebnis {}
2
3 class Erfolg<T> : Ergebnis {
4 public T Wert;
5 }
6
7 class Misserfolg : Ergebnis {}
Die Operation hat in diesem Fall einen Ergebnistyp, der sowohl den
umgewandelten Wert wie einen abschlägigen Bescheid transportieren
kann. Die Signatur ist einfacher als im vorhergehenden Fall mit dem sehr
sprachspezifischen out-Parameter:
¹⁶⁸In Go wird stattdessen ein anderes Muster favorisiert. Dort würde die Signatur so
lauten: (bool,int) Umwandeln(string text). Das entscheidende if müsste dann
jedoch dem Funktionsaufruf nachgeschaltet werden. Das finde ich etwas umständlicher; es
verrauschtdenCodemehralseinout-Parameter.Aberprobieresselbstausundvergleiche.


---


<!-- Page 333 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 324
1 class Zahlenwandlung
2 {
3 public static Ergebnis Umwandeln(string text) {
4 if (text.All(x => char.IsDigit(x)) is false)
5 return new Misserfolg();
6
7 var zahl = int.Parse(text);
8 return new Erfolg<int> {Wert = zahl};
9 }
10 }
Und in der Integration wird nun mittels Kontrollstruktur überprüft, wel-
cher Fall vorliegt:
1 switch (Zahlenwandlung.Umwandeln("42")) {
2 case Erfolg<int> e:
3 ...
4 break;
5 case Misserfolg _:
6 ...
7 break;
8 }
Das ist aufwändiger als mit dem out-Parameter. Das ist so aufwändig
wie mit einer Enumeration. Aber es ist allgemeingültig, weil hier die Klas-
sifikation ganz unterschiedliche und beliebig “angereicherte” Ergebnisse
liefern kann.
Wenn in den case-Fällen jetzt nur Funktionsaufrufe stattfinden, finde ich
es ok, eine Klassifikation in dieser Weise in einer Integration vorzuneh-
men.
Polymorphie
In den Beispiele zur Fallunterscheidung taucht immer wieder die Dopp-
lung auf: Zuerst die Klassifikation, dann die Auswertung der Klassifikati-
on. Das ist zwar eine gute Trennung im Sinne des SRP, führt nichtsdesto-
trotz aber eben zu mehrfachen Fallunterscheidungen. Darin kannst du ein
Konsistenzrisiko sehen und die Not für vermehrten Testaufwand.
In manchen Fällen lässt sich das jedoch umgehen. Ein Beispiel dafür ist
nochmaldieZahlenwandlung.Beiderwirdjaimmergewandelt,nureben
in unterschiedlicher Weise, je nach Zahlensystem. Oben habe ich das
Problem mit mehreren Ausgängen gelöst. Das ist ok - doch du könntest
darin das Muster sehen, dass immer im Grunde dasselbe passiert und des-
halbdasModellvereinfachen.Dannsindnichtmehrereoptionale,Stream-
basierteAusgängenötig,sonderneinAusgang,aufdemUnterschiedliches
herauskommen kann:


---


<!-- Page 334 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 325
DieKlassifikationliefertjetztnichteinfachein“Etikett”,dassdannwieder
interpretiert werden muss, sondern gleich eine Funktionseinheit, “die es
tut”. Für die ist zunächst nur eine Abstraktion interessant, z.B.
1 interface IWandeln {
2 int Wandeln(string text);
3 }
Darauf könnte eine Klassifikation abgestellt sein:
1 public static IWandeln Klassifizieren(string text) {
2 if (...)
3 return new RömischWandeln();
4 if (...)
5 return new BinärWandeln();
6 return new HexadezimalWandeln();
7 }
8
9 // Integration
10 var text = args[0];
11 var wandler = Klassifikation.Klassifizieren(text);
12 var zahl = wandler.Wandeln(text);
13 UI.ErgebnisAnzeigen(zahl);
Die verschiedenen Zahlensystemwandler implementieren einfach alle
dasselbe Interface IWandeln{}.
In diesem speziellen Fall könnte es allerdings noch etwas kompakter
aussehen, wenn nicht ein Serviceobjekt, sondern gleich ein Datenobjekt
geliefert würde:


---


<!-- Page 335 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 326
1 interface IZahl {
2 public int Wert { get; }
3 }
4
5 class RömischeZahl : IZahl
6 {
7 public RömischeZahl(string text) {
8 ... // Umwandlung
9 Wert = ...;
10 }
11
12 public int Wert { get; }
13 }
14 ...
15
16 class Klassifikation
17 {
18 public static IZahl Klassifizieren(string text) {
19 if (...)
20 return new RömischeZahl(text);
21 if (...)
22 return new BinäreZahl(text);
23 return new HexdezimaleZahl(text);
24 }
25 }
Die Integration ist dann mega knapp:
1 var zahl = Klassifikation.Klassifizieren(args[0]);
2 UI.ErgebnisAnzeigen(zahl.Wert);
Hübsch, oder? Und alles nur mit üblichen OO-Mitteln. Das wird auchcon-
ditional polymorphism genannt. Hier gibt es nur eine Fallunterscheidung!
Und ansonsten ist alles in den Klassen verpackt, die für jeden Fall stehen.
Davon profitierst du natürlich umso mehr, je umfangreicher das genutzt
wird, was da einmal bedingt instanziiert wird.
Allerdings gibt es einen Wermutstropfen: Das PoMO ist nicht so sauber
eingehalten, finde ich. Die Klassifikation weiß vermittels der konkret zu
instanziierenden Klassen darüber Bescheid, was downstream “abgeht”.
Es findet nicht nur eine Klassifikation von Input statt wie mit einer
Enumeration, sondern auch noch eine Entscheidung über das weitere
Vorgehen (im Rahmen einer Abstraktion). Das “auch noch” verweist da
für mich auf einen gewissen Widerspruch zum SRP. Doch den magst du
hinnehmen.
Warteschlange
Und zum Schluss nochmal ein kleiner Ausflug ins Reich der Verteilung.
Ich will das nur andeuten und dir damit den Impuls geben, über das


---


<!-- Page 336 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 327
Konkrete immer hinaus zu blicken auf das dahinter stehende Konzept, die
Prinzipien, die Abstraktion.
Worum geht es beim Messaging? Um den Fluss von Daten auf einem
Medium. Wie Korken auf einem Bach bewegen sich Daten von einer
Quelle zu einer Mündung. Eine Funktionseinheit setzt diese Datenkorken
auf einen Bach, eine andere Funktionseinheit, downstream, fischt sie für
sich von diesem Bach. Oder du könntest die beiden Funktionseinheiten
auch spezfisch mit ihrem eigenen Bach verbunden denken.
Das fließende Gewässer ist das Medium für den unidirektionalen Trans-
port der Produkte eines Produzenten zu einem Konsumenten.
So ein Medium war bisher auch im Spiel: der Stack.
1 var produkt = Produzieren(...);
2 Konsumieren(produkt);
DerOutputvonProduzieren()wirdinderVariablenproduktgespeichert.
Deren Speicherplatz ist von der Integration als lokale Variable auf dem
Stack allokiert. Von dort wird der Output als aktueller Parameter wieder-
um auf den Stack für Konsumieren() kopiert. Nicht anders läuft es bei
Continuations ab.
Das ist zum Glück alles durch den Compiler vor dir verborgen. Nichtsdes-
totrotz ist eben die Realität, dass ein Medium nötig ist für den Nachrich-
tenfluss zwischen “radikalen Objekten”.
AllerdingsmussdiesesMediumkeinStacksein.JedeandereDatenstruktur
ist möglich, wird dann nur nicht automatisch vom Compiler unterstützt.


---


<!-- Page 337 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 328
Der Stack ist schlicht “eingebacken” in unseren Code, weil er eine taug-
liche Abstraktion der Hardware darstellt. Prozessoren sind keine reinen
Stackmaschinen. Zunächst für eine Stackmaschine aber Zwischencode zu
erzeugen, der erst in einem weiteren Schritt für eine konkrete Hardware
optimiert wird, ist einfacher oder zumindest flexibler. Sprachen sind
Strata, die uns immer höher über die Hardwarerealität aufsteigen lassen.
Der Stack ist das Medium zur Datenweitergabe im Kontrollfluss. Die
Warteschlange (engl. queue) ist demgegenüber das Medium zur Daten-
weitergabe im Datenfluss.
Wie du siehst, kannst du Datenflüsse auch mit Stacks implementieren.
Doch damit bist du an das Paradigma gebunden, zu dem er gehört:
synchrone Programmierung. Datenflüsse sind hingegen von Natur aus
asynchron.
Der Stack ist eine LIFO-Datenstruktur. Das verbirgt der Compiler vor
dir aber. Deshalb macht es nichts, dass ein Stack den bisherigen Überset-
zungen von Datenflüssen unterliegt. Messaging hingegen basiert darauf,
dass die Nachricht, die zuerst eine Funktionseinheit verlässt, auch zuerst
downstream von einer anderen verarbeitet wird. BeimMessaging überho-
len Nachrichten einander nicht; die Produktionsreihenfolge entspricht der
Konsumptionsreihenfolge.
Dem entspricht ganz natürlich eine FIFO-Datenstruktur. Das ist eine
Warteschlage. Wäre es anders, würdest du dich in jedem Supermarkt
aufregen, wenn du kurz davor bist, dranzukommen und jemand anderes
dir vorgezogen wird.
FürdiemeistenDatenflüsse,dieduentwirfst,istdie“Unnatürlichkeit”des
Stack unerheblich. Er ist ja vor dir durch den Compiler verborgen. Doch
wenn es an die Nebenläufigkeit geht, wenn du asynchrone Datenflüsse
implementieren willst, dann musst du das Medium wechseln. Dafür gibt
es sicher auch für deine Programmiersprache Frameworks, aber ich will
dir diesen Wechsel einmal hier kurz ungeschönt “im Selbstbau” demons-
trieren; ich will dir die Queue zeigen, die den Stack ersetzt.
Das Szenario ist nochmal die Nettozeilenzahlbestimmung. Darin soll die
Analyse asnychron zur Sammlung geschehen und parallel für mehrere
Dateien. Wie du das modellieren kannst mit Streams, hast du schon
gesehen. Und mit den Farben bzw. den Bögen unter analysieren
visualisierst du sogar die Nebenläufigkeit.


---


<!-- Page 338 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 329
Aber wie implementierst du das? Ohne die Modellierungsebene zu verlas-
sen, senke ich mal das Abstraktionsniveau. Schauen wir unter die Haube,
wenn eine Warteschlange zum Einsatz kommen soll:
Hier ist das Nachrichtenmedium als Abhängigkeit explizit zu sehen:
• Das Sammeln trägt die gefundenen Dateien am Ende einer Warte-
schlage ein. Diese Eintragung ist synchron: Es geht erst weiter mit
der Sammlung, wenn der Eintrag in der Warteschlange steht. Das
istjaabereinemarginaleVeränderungeinerDatenstrukturundhält
nicht auf.
• Die Analyse entnimmt zu bearbeitende Dateien am Kopf der War-
teschlange. Die Dateien fließen also durch die Warteschlange von
der Produktion zur Konsumption. Die Konsumption ist durch die
Warteschlange von der Produktion entkoppelt; sie muss nicht so-
fort reagieren. Die Warteschlange ist ein Puffer zwischen beiden
Funktionseinheiten, in dem sich Dateien ansammeln können, falls
schneller produziert als konsumiert wird.
• Im Modell sind für die Analyse zwei Funktionseinheiten an den
Start gebracht. Beide laufen auf verschiedenen Threads; so können
sie Dateien parallel verarbeiten. Die Latenz der Analyse insgesamt
sinkt dadurch.


---


<!-- Page 339 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 330
• Am Ende fließen im Zählen alle Analyseergebnisse zusammen und
werden nach Eintreffen des letzten als Gesamtergebnis weitergege-
ben.
Das Besondere ist die explizite Datenstruktur der Queue, von der beide
Seiten des vormaligen Streams nun abhängig sind. Diese Datenstruktur
dient mehreren Threads, muss als thread-safe sein. Der eine schreibt, die
anderen lesen. Die Queue muss sicherstellen, dass dabei nichts schief geht.
Angefügt wird, wenn die Sammlung wieder eine Datei gefunden hat.
Entnommen wird, wenn eine Analyseeinheit bereit ist. Die Analyse läuft
pro Einheit also in einer Schleife ab. Sollte sie darin entnehmen wollen,
die Queue aber leer sein, dann wartet sie ab, bis wieder eine Datei zur
Verarbeitung eingetragen ist.
Die Analyseeinheiten bezeichne ich als Worker: Sie laufen für sich au-
tonom auf ihrem Thread und “lauschen” auf einem Medium auf neue
Arbeitspakete, wann immer sie ihre vorherige Arbeit erledigt haben.
Dieselbe Queue bedient hier mehrere Threads; deshalb sind es für mich
Worker und keine Actors¹⁶⁹, die jeder für sich eine eigene Queue haben,
die Mailbox.
Bevor ich dir eine Übersetzung zeige, möchte ich das obige Modell
allerdings wieder ein wenig mehr “ins Fließen bringen”. Die Queue steht
einbisschenverlorenzwischenderSammlungundderAnalyse.Konkreter
sieht es so aus:
¹⁶⁹https://www.brianstorti.com/the-actor-model/


---


<!-- Page 340 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 331
Die Klasse Backlog{} implementiert eine thread-sichere Queue, in die
der Sammler{} gefundene Dateien einstellt. Anhängen() ist hier eine
Senke, aus der nichts herausfließt, weil ja die Daten in einem Zustand
gehalten werden. Für das Sammeln ist damit seine erledigt.
Auf der anderen Seite laufen mehrere Worker vom Typ Analyse{},
die mit demselben Backlog{} wie der Sammler{} gestartet wurden.
Die Analyse beginnt allerdings nicht gleich mit ihrer Arbeit, sondern
geht in einen Wartemodus: Sie wartet darauf, dass in der Queue eine
Datei ankommt. Wenn das geschehen ist, schiebt sie die hinaus und die
Analyselogik nimmt sich ihrer an. Das ist wie üblich ein synchroner
Datenfluss - der aber durch den Thread, den Warten gestartet hat, von
der Sammlung entkoppelt ist. Du siehst, dass der grüne Thread noch bis
zum Warten läuft und dort erst der pinke beginnt. Auch der kleine Pfeil
im Kreis in Warten zeigt an, dass dort ein Thread gestartet wird.
“Im Selbstbau” gibt es beim Multithreading natürlich einiges zu bedenken.
Diese ganzen Details will ich dir aber ersparen. Wie das Backlog{}
thread-safe gemacht wird, ist hier einerlei und ohnehin egal, wenn du
für solche Dinge später ohnehin einen Framework benutzt. Interessant ist
hingegen der Einsatz dieser Datenstruktur insbesondere beim Konsumen-
ten:


---


<!-- Page 341 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 332
1 abstract class Worker<T>
2 {
3 public Worker(Backlog<T> queue) {
4 Warten(queue,
5 Verarbeiten);
6 }
7
8 private void Warten(Backlog<T> queue, Action<T> onBacklogeintrag) {
9 var th = new Thread(_ => {
10 while (true) {
11 if (queue.Entnehmen(out var backlogeintrag))
12 onBacklogeintrag(backlogeintrag);
13 else
14 break;
15 }
16 });
17 th.Start();
18 }
19
20 protected abstract void Verarbeiten(T daten);
21 }
22
23
24 class Analyse : Worker<Datei>
25 {
26 private Random _rnd = new Random();
27
28 public Analyse(Backlog<Datei> queue) : base(queue) { }
29
30
31 protected override void Verarbeiten(Datei datei) {
32 Console.WriteLine($"analysieren({datei.Daten})");
33 Thread.Sleep(_rnd.Next(200,500));
34 OnNettozeilenzahl(datei.Daten * 10);
35 }
36
37
38 public event Action<int> OnNettozeilenzahl;
39 }
In Warten() läuft die Logik ab, die versucht, einen Arbeitsauftrag aus
der Queue zu beschaffen. Der wird dann hinausgeschoben zur Verar-
beitung downstream - die spannenderweise in einer abgeleiteten Klasse
stattfindet.¹⁷⁰ Und immer so weiter im Kreis. Mit while(true) wird das
Backlog so schnell entleert, wie es das Backlog zulässt. Entnehmen()
ist allerdings synchron und blockierend: Sollte das Backlog gerade leer
sein, kehrt Entnehmen() solange nicht zurück, bis wieder ein Auftrag
eingestellt wurde.
Allerdings kann es auch sein, dass das Backlog “geschlossen wurde”; dann
kehrt Entnehmen() mit falsezurück und das Warten hat ein Ende.
Die im Hintergrund laufenden Worker können also alle indirekt beendet
werden,indemdasBacklog“geschlossenwird”.Daskönntez.B.geschehen,
¹⁷⁰Das ist kein Widerspruch gegen das PoMO! Der Nachrichtenproduzent weiß nichts
vom Nachrichtenkonsumenten. Und auch die konsumierende Routine Verarbeiten()
weiß nicht, woher ihr Input kommt. Ihre Klasse Analyse{} integriert über das Erbe von
Worker<Datei>aufModulebeneProduktionundKonsumption.


---


<!-- Page 342 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 333
wenn das Endergebnis ermittelt wurde.¹⁷¹
Die Continuation als Feld/Attribut zeigt dir an, dass die Analyse{} ein
EBC ist. Mir schien das in diesem Fall angemessen für alle Funktionsein-
heiten:
Ich finde, das ist ein sauberes “Schaltbild” für das Programm. Vereinfacht
könntest du es auch so zeichnen:
Lass dir also gern etwas einfallen, um deine Modelle ausdrucksstark zu
machen und gleichzeitig übersichtlich zu halten: Den Doppelpfeil habe
ich gerade erst für dieses Bild “erfunden”. Ich habe ihn noch nie vorher
zur Entkopplung via Queue gezeichnet. Wenn ich ihn mir aber so ansehe,
¹⁷¹Hintergrund-Threads explizit zu schließen, ist für eine saubere Programmbeendung
essenziell. Das ist eines der Details, um das du dich leider kümmern musst, wenn du in
die Parallelverarbeitung einsteigst. Ein Gewinn bei Performance oder Responsiveness als
nicht-funktionale Anforderungen kostet etwas; du bezahlst mit Aufwand für Infrastruktur-
programmierung.


---


<!-- Page 343 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 334
dann gefällt er mir ganz gut. Wenn ich ihn öfter benutze, wird sich zeigen,
ob er wirklich praxistauglich ist.
Der andere interessante Bereich des Codes ist die Integration des Flusses.
Interessant daran ist, dass es da ganz unspektakulär aussieht:¹⁷²
1 // Construction
2 var bl = new Backlog<Datei>();
3 var sammler = new Sammler(bl);
4 var workers = new[] {
5 new Analyse(bl),
6 new Analyse(bl)
7 };
8 var zähler = new Zähler();
9
10 // Binding
11 sammler.OnM += zähler.ErwartungSetzen;
12
13 workers[0].OnNettozeilenzahl += zähler.Aktualisieren;
14 workers[1].OnNettozeilenzahl += zähler.Aktualisieren;
15
16 zähler.OnErgebnis += (n, m) => { ... };
17
18 // Run
19 sammler.Sammeln(args[0]);
DieIntegrationistgeradlinigfüreineImplementationmitEBCs.Dasshier
Nebenläufigkeit im Spiel ist, ist unsichtbar. Und genau so soll es ja auch
sein. Ein ADT für das Nachrichtenmedium und die Worker-Serviceklasse
verbergen die Feinheiten. Die Mulithreading-Infrastruktur ist damit in
zweigenerischenKlassen-Backlog<T>{}undWorker<T>{}gekapselt.
Alle anderen Funktionseinheiten müssen sich nicht weiter darum küm-
mern.¹⁷³
Die Kommentare in der Integration zeigen übrigens Phasen an, die immer
wieder in Implementationen von Datenflüssen durchlaufen werden:
• Construction: Zuerst werden alle nötigen Objekte instanziiert.
• Binding: Dann werden Objekte zu Datenflüssen verbunden, sofern
das nötig ist. Das ist der Fall, wenn du EBCs einsetzt.
• Run: Schließlich wird die Verarbeitung mit einer Nachricht an die
Wurzel des Datenflusses gestartet.
¹⁷²Ich habe nur ein paar Details weggelassen, um das Programm am Laufen zu halten
bis ein Ergebnis vorliegt; nach Eintragung der letzten Datei ins Backlog durch Sammeln()
würde der Vordergrund-Thread ja aus der Methode zurückkehren und auch aus Main()
zurückfallen und das Programm damit beendet, egal ob in den Hintergrund-Threads der
Workernochgearbeitetwirdodernicht.
¹⁷³Ok,dasstimmtnichtganz.DerZähler{}istauchnochMultithreading-sensibel.Aber
auchdaskönnteichnochändern.ErfolgtjawieBacklogundWorkereinemMuster,dassich
ineineBasisklasseGatherer<T>{}herausziehenkönnte.


---


<!-- Page 344 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 335
Reflexion
3-dimensionale Datenflüsse sind natürlich und unvermeidlich. Im Modell
sind sie meistens gut verständlich; alles ist klar. Bei der Implementation
jedoch gilt es dann etwas aufzupassen. Meine länglichen Ausführungen
mögen dir das jedoch schlimmer ausgemalt haben, als es in der Praxis ist.
Mit ein wenig Übung werden 3-dimensionale Datenflüsse kein Problem
machen;dabinichsicher.DochamAnfangmagesdichverwirren,dassdu
so viele Optionen zur Übersetzung hast. Ohne Streams war die Codierung
von Funktionseinheiten so simpel. Mit Streams explodieren nun plötzlich
die Möglichkeiten.
Das kann und will ich dir nicht ersparen. Programming with Ease steht
zwar für eine Methode der Leichtgewichtigkeit und Klarheit. Deshalb ist
aber nicht alles schwarz-weiß. “Nur so und nie anders” hat Flow-Design
nicht im Programm, auch wenn es sich für dich manchmal so anhören
mag.Ja,ichbinvonIOSP/PoMOüberzeugtundsetzediePrinzipienoftals
scharfes Messer an, um Wünschenswertes von nicht Wünschenswertem
zu trennen. Dennoch gibt es Grauzonen. In denen musst du nach Augen-
maß entscheiden.
Beliebt ist da die Frage, “Wann sind denn Kontrollstrukturen in Integra-
tionen erlaubt? Alternative Flüsse mit Continuations übersetzen, ist so
umständlich; kann ich das nicht mit einer Kontrollstruktur vermeiden?”
Meine Antwort darauf: “Klar, du darfst alles machen. Weiche von den
Prinzipien ab, wie du magst. Ob das eine gute Idee ist, wird dir später
dein Schmerz mitteilen.”
Das Problem sinkender Produktivität in Projekten ist ultimativ zwar un-
vermeidbar, doch die Steilheit der Abnahme ist eine inverse Funktion der
Berücksichtigung von Prinzipien: Je mehr du Prinzipien berücksichtigst,
desto flacher die Kurve; je weniger du sie berücksichtigst, desto steiler
geht die Produktivität nach unten und die Stimmung in den Keller.
Jede einzelne Missachtung ist vielleicht nicht so schlimm. Am Ende stirbt
das Projekt dann aber a death by a thousand cuts.
Die Vielzahl der Optionen in diesem Kapitel veranschaulicht die Natur
der Softwareentwicklung sehr schön: Es geht um ständige Abwägung.
Hard and fast rules wären schön, gibt es in Teilen auch, doch über weite


---


<!-- Page 345 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 336
Strecken musst du halt den Kopf angeschaltet lassen. Meine Empfehlung
dabei ist jedoch: Im Zweifelsfall tendiere zur Berücksichtigung eines
Prinzips. Wähle den etwas langsameren, sauberen Weg - um langfristig
höhere Geschwindigkeit zu behalten.
Schreibe einen Test, halte SRP und IOSP ein, auch wenn es im Moment
etwas nervig sein mag. Dein zukünftiges Ich - oder deine Kollegen -
werden es dir danken.
Darüber hinaus kann ich auch noch raten: Verwechsle nicht Unkenntnis
mit mangelnder Eignug. Häufig begegne ich Entwicklern, die vor Conti-
nuations im Speziellen, aber auch anderen Sprachfeatures stirnrunzelnd
stehen, wenn ich sie in einer Datenflussübersetzung einsetze. Sie sagen,
das sei aber nicht wirklich besser zu verstehen, als das, wie sie selbst
übersetzt haben. Und dann stellt sich heraus, dass sie keine Erfahrung
haben mit den eingesetzten Sprachfeatures, Konzepten, Paradigmen.
In C# kann ich konkret Jahre benennen, in denen bestimmte Features
eingeführt wurden. Wenn die nach 20, 13 oder auch nur 5 Jahren nicht in
den Köpfen und Fingerspitzen eines Entwicklers angekommen sind, dann
kann ich auch nicht helfen. Tut mir leid, da bin ich jetzt etwas platt.
Nicht jedes Sprachfeature, nicht jede Bibliotheksfunktion muss dir sofort
einfallen oder auch nur gefallen. Aber es gibt bei jeder Sprache und
Plattform so Grundlegendes, das jeder Entwickler, der sich Profi nennen
will, einfach kennen und können muss.
Insofern kann ich dir nur empfehlen: Bleib am Ball! Lass dich nicht von
der Entwicklung deiner Plattform abhängen. Frage dich bei jeder neuen
Version, inwiefern dir neue Features dienen können. Oder spezifischer in
Bezug auf das Thema hier: Inwiefern können dir Features dienen, um
Modelle leichter zu übersetzen und saubereren Code zu schreiben? Im
Jahr 2020 zähle ich z.B. bei C# Features wie lokale Funktionen¹⁷⁴ oder
Pattern Matching¹⁷⁵ dazu. Und wer mehr mit Nebenläufigkeit zu tun hat,
derprofitiertsicherlichvonActor-FrameworkswieAkka(Java,C#)¹⁷⁶oder
CAF (C++)¹⁷⁷ oder proto.actor (.NET, Go, Java, Kotlin)¹⁷⁸. Aber das sind
¹⁷⁴https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-
structs/local-functions
¹⁷⁵https://docs.microsoft.com/en-us/dotnet/csharp/pattern-matching
¹⁷⁶https://akka.io/
¹⁷⁷https://actor-framework.org/
¹⁷⁸https://proto.actor/


---


<!-- Page 346 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 337
nur Beispiele. Mir geht es mehr um die Prinzipen dahinter:
• Bleib am Ball!
• Lerne in der Grauzone des ewig Vorläufigen zu arbeiten.
Das Vorläufige ist nicht nur eine Sache des Kunden, der sich nie festlegen
will auf Anforderungen und immer wieder mit neuen Ideen um die Ecke
kommt. Das Vorläufige ist auch dein Begleiter bei Entscheidungen, die du
für deine Lösungen im Entwurf triffst und dann bei der Übersetzung des
Modells in den Code.
Du kannst dich heute für eine Übersetzung eines Streams mit einem
Iteratoren entscheiden - und morgen stellst du fest, dass du dich damit
in eine Ecke gepinselt hast. So ist das Leben. Dann lass los von der ersten
Entscheidung und triff eine neue. Versuche also nicht, Entscheidungen
“für immer” zu fixieren. Das wäre so, als würdest du mit einem Herz-
schrittmacher leben, der auf eine Frequenz eingestellt ist. Ein gesundes
Herz hat vielmehr eine hohe Herzratenvariabilität (HRV)¹⁷⁹: Es kann
sich von Sekunde zu Sekunde an den Bedarf des Körpers anpassen; die
Herzfrequenz ist nicht konstant in der Minute, in der du dir vielleicht
den Puls misst; sie fluktuiert ständig. Deine aktuelle Herzfrequenz, die
du misst, ist vielmehr ein Durchschnitt.
SeialsowiedeinHerz:Seiflexibel,passedichinjederSekundedemBedarf
an. Manchmal ruft der nach einer Continuation, manchmal nach einer
Kontrollstruktur in der Integration, manchmal nach einem Iterator - und
dann verändert sich alles und es ist besser, wenn du die Entscheidungen
von gestern revidierst.
MeinfesterGlaubeist,dassdichgenaudann,wennesansRevidierengeht,
ein Denken in Modellen und ein Code, der mit IOSP/PoMO den Modellen
folgt, besser unterstützt, als das, was die mainstream Objektorientierung
dir bisher empfohlen hat.
¹⁷⁹https://de.wikipedia.org/wiki/Herzfrequenzvariabilit%C3%A4t


---


<!-- Page 347 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 338
Übungsaufgaben
Reflexionsaufgabe
Bitte formuliere eine Frage oder eine Erkenntnis zum Kapiteltext.
• Wo bist du gedanklich hängengeblieben, was ist dir unklar,
was passt für dich irgendwie nicht zusammen, wozu würdest
du dir noch etwas mehr Erklärung wünschen? Steht irgendet-
waszudeinerbisherigenPraxisimWiderspruchunddufragst
dich, warum du etwas ändern solltest?
• Oder: Wann hast du einen Aha-Moment gehabt, was ist
diralsbemerkenswert,spannend,ausprobierenswertaufgefal-
len? Hat irgendetwas “in dir Klick gemacht”, weil dir nun ein
Zusammenhang aufgegangen ist? Oder verstehst du jetzt aus
deiner bisherigen Praxis irgendetwas besser?
Am besten formulierst du Frage bzw. Erkenntnis schriftlich. Indem
du deine Gedanken aufschreibst, wirst du dir ihrer bewusster. Bei
einer Frage kommst du dadurch vielleicht schon einer Antwort aus
dir selbst heraus näher. Bei einer Erkenntnis fällt dir vielleicht schon
etwas ein, das du ab jetzt anders machen kannst.
Aufgabe 1 - Tic-Tac-Toe
Entwickle ein Programm, mit dem man auf der Konsole Tic-Tac-Toe
(TTT) spielen kann.
Beide Spieler sitzen am selben Computer und machen abwechselnd
ihre Züge. Sie platzieren ihre Spielsteine durch Angabe der Koordi-
nateeinesFeldesaufdemSpielbrett.SosähedasaufderKonsoleaus:
1 $ ttt
2 A|B|C
3 1: | |
4 -+-+-
5 2: | |
6 -+-+-


---


<!-- Page 348 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 339
7 3: | |
8 X ist am Zug: A1
9 A|B|C
10 1:X| |
11 -+-+-
12 2: | |
13 -+-+-
14 3: | |
15 O ist am Zug: B2
16 A|B|C
17 1:X| |
18 -+-+-
19 2: |O|
20 -+-+-
21 3: | |
22 X ist am Zug: B2
23 Ungültiger Zug!
24 X ist am Zug: B1
25 A|B|C
26 1:X|X|
27 -+-+-
28 2: |O|
29 -+-+-
30 3: | |
31 ...
32 A|B|C
33 1:X|X|X
34 -+-+-
35 2: |O|O
36 -+-+-
37 3: | |
38 X gewinnt!
39 $
• Das Spielbrett wird immer wieder neu und aktualisiert darge-
stellt nach jedem Zug.
• Wenn ein Zug nicht ausgeführt werden kann, z.B. weil das
Spielfeld schon belegt ist oder die Koordinaten ungültig sind
(z.B. X8), wird eine Fehlermeldung gezeigt und die Eingabe
kann wiederholt werden.
• Bei jedem Zug zeigt das Programm, welcher Spieler dran ist.
• Am Ende wird gemeldet, wer gewinnt oder ob das Spiel
unentschieden beendet wurde.
Wie du dir denken kannst, ist zu erwarten, dass im Modell Streams
vorkommen.Duwirstalsoeinen3-dimensionalenDatenflussentwer-
fen müssen.
EineImplementationdesModellsistdiesesMalwichtigerBestandteil
der Aufgabe, weil du dich entscheiden sollst, wie du die Streams
übersetzt. Wenn du aber nicht so viel Zeit hast für die Implemen-
tation,kannstduaneinerStelleeineAbkürzungeinschlagen:beider
Spielendeüberprüfung. Im Modell sollte allerdings eine vollständige
Überprüfung des Spielendes stattfinden; es gibt mehrere Gründe für
ein Spielende, die würdig sind, getrennt modelliert zu werden.
https://de.wikipedia.org/wiki/Tic-Tac-Toe


---


<!-- Page 349 of 584 -->


07-Flow-Designmit3-dimensionalenDatenflüssen 340
Wenn du magst, kannst du dem Programm auch ein GUI geben oder
es in einer Webseite realisieren. Die Konsole wähle ich nur, um es so
technologiefrei wie möglich zu machen. Wenn du aber Frontend-Profi bist,
zauberegernetwasvisuellNettes.
Beispielsweise könntest du vereinfacht annehmen, dass der Spieler
gewinnt, der als erstes das Mittelfeld B2 besetzt. Damit lässt sich dann
nicht wirklich interessant spielen, doch du kannst dein Programm interaktiv
zumindest ausprobieren, wenn du ein bisschen darauf achtest, wo du die
Spielsteinesetzt.


---


<!-- Page 350 of 584 -->


08 - Die IODA Architektur
Bisher habe ich dir Flow-Design vorgestellt als einen Ansatz, der dich bei
vergleichsweise überschaubaren Problemen zu einem Entwurf und damit
zu sauberem Code führen soll. Mit Datenflusshierarchien kannst du zwar
wachsendeVerhaltensanforderungenmodellieren,mitModulenkannstdu
die daraus resultierende wachsende Zahl an Funktionseinheiten bändigen.
Doch damit reagierst du immer nur.
Die Möglichkeit zur flexiblen Reaktion ist mir natürlich wichtig, dir
mitzugeben. Doch manchmal sind Reaktion und damit einhergehende
ad hoc Entscheidungen Verschwendung. Du musst nicht jedes Rad neu
erfinden und auch bei aller Ungewissheit der Anforderungen ist nicht
alles im Nebel. Manches ist so überraschend wie Weihnachten. Es gibt
Muster, die du anwenden kannst. Mit ein paar best practices kannst du dir
das Leben einfacher machen, um mehr Aufmerksamkeit auf das wirklich
Neuartige richten zu können.
Zu den nützlichen Mustern gehört für mich, eine grundlegende Vorstel-
lung von der Grobstruktur von Software zu haben. Was ist eigentlich das
Ganze, in dem die Daten durch Flüsse fließen?
Du hast wahrscheinlich schon von Architekturen bzw. Architekturmus-
tern wie MVC (Model-View-Controller)¹⁸⁰, Schichtenarchitektur (laye-
red architecture)¹⁸¹, Hexagonale Architektur (ports-and-adapters)¹⁸² oder
Clean Archicture¹⁸³ gehört. Sie alle haben gemeinsam, dass sie die Logik
von Software aufgeteilt in gewisse Funktionsbereiche sehen, die in gewis-
sen funktionalen Abhängigkeitsverhältnissen stehen. Architekturmuster
sind damit “Strukturnormen”, die sagen: “So soll Software modularisiert
sein.” Sie beschreiben nicht, was du beobachten kannst, sondern machen
konkrete Vorgaben, wie du “im Großen” deinen Code strukturieren sollst.
Das ist grundsätzlich eine gute Sache, auch wenn du denken magst, dass
doch jede Anwendung ganz anders und neu ist, quasi eine Schneeflocke.
¹⁸⁰https://www.w3schools.in/mvc-architecture/
¹⁸¹https://www.thinktocode.com/2018/07/05/layered-architecture/
¹⁸²https://en.wikipedia.org/wiki/Hexagonal_architecture_%28software%29
¹⁸³https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html


---


<!-- Page 351 of 584 -->


08-DieIODAArchitektur 342
UndEntwicklersindaucheigenePersönlichkeiten,ganzzuschweigenvon
den Teams, zu denen sie sich zusammenfinden; da kann man doch nicht
pauschal sagen, wie Software strukturiert werden soll.
Natürlich kann man das nicht ganz genau und die Architekturmuster
wollendasauchnicht.DiespezifischeArchitekturistganzanwendungsin-
dividuell, so wie das eine Haus diese Architektur hat und das andere eine
ganz andere; eine Schule hat eine andere Architektur als eine Villa oder
ein Theater. Robert C. Martin - der, der den Begriff Clean Code geprägt
hat und auch für die Clean Architecture steht - fordert das sogar, indem
er sagt, jede Anwendung sollte eine screaming architecture¹⁸⁴ haben, d.h.
eine, die “hinausschreit”, um was für eine Anwendung es sich handelt.
Konkrete Anwendungen brauchen eine konkrete Architektur, die ganz
konkreten Anforderungen entspricht. Ihre Struktur soll genau ihre nicht-
funktionalen Anforderungen widerspiegeln.
• Datenflüsse spiegeln die funktionalen Anforderungen
• Module spiegeln die Anforderungen an Verständlichkeit, Übersicht-
lichkeit, kurz: Ordnung
• DieVerteilungspiegeltEffizienzanforderungenanz.B.Performance,
Skalierbarkeit, Verfügbarkeit usw.
Die Kräfte, die an diesen Strukturen ziehen, sind je Anwendung ganz
individuell - und doch gibt es tried and true Ansätze, um Anwendun-
gen zu strukturieren. So wie alle Gebäude Fundament, Wände, Räume,
Dach als Strukturelemente teilen, auch wenn die Gebäudezwecke sehr
differieren,könnenundsolltenAnwendungenebenfallsStrukturelemente
in bestimmten günstigen Beziehungen teilen. Das ist die Botschaft der
Architekturmuster.
Über die Jahrzehnte wurden verschiedene solcher Empfehlungen entwi-
ckelt. Jede war eine Reaktionen auf Probleme, die man damals empfun-
den hatte. Jede sollte es Entwicklern leichter machen, ihrem Code eine
Grundstruktur zu geben, die ihn langlebiger macht, ohne ihn zu sehr
einzuschränken.
Näher will ich auf die bisherigen Architekturmuster hier gar nicht ein-
gehen. Lieber stelle ich dir ein weiteres vor, von dem ich meine, dass es
¹⁸⁴https://blog.cleancoder.com/uncle-bob/2011/09/30/Screaming-Architecture.html


---


<!-- Page 352 of 584 -->


08-DieIODAArchitektur 343
zukunftstauglicherist,weileszurradikalenObjektorientierungpasst,weil
in ihm IOPS und PoMO berücksichtigt werden.
Ich habe darüber lange nachgedacht, ob ich mich den etablierten Mustern
entgegenstelle. Wie du siehst, ist meine Entscheidung am Ende positiv
gewesen: Ja, ich glaube, die etablierten Architekturmuster leiden allesamt
an einem fundamentalen Problem, egal, wie viele Funktionsbereiche sie
differenzieren und ob sie die als Kästen oder Schalen darstellen. Ich sehe
den guten Willen dahinter, ich sehe eine Entwicklung in die richtige
Richtung-dochselbstdasderzeitneuesteMuster-dieCleanArchitecture
-, das versucht, bisherige in sich zu vereinen, überwindet nicht dieses
Problem; es bleibt in einem überkommenen Denkmuster stecken. Das
fundamentale Problem sind natürlich… funktionale Abhängigkeiten.
Aber genug davon. Wie sieht das Architekturmuster aus, mit dem ich
meine, dieses Problem zu lösen?
Die Softwarezelle
In einem Blog-Artikel im Jahr 2005¹⁸⁵ habe ich zum ersten Mal, glaube ich,
den Begriff Softwarezelle (software cell) öffentlich benutzt. Leider sind die
Bilder im Artikel über die Jahre online verloren gegangen, doch ich habe
noch etwas in einem Archiv auf meiner Festplatte gefunden. So habe ich
mir damals eine Softwarezelle vorgestellt.¹⁸⁶
¹⁸⁵https://weblogs.asp.net/ralfw/403986
¹⁸⁶Interessanterweise ist Alistair Cockburn zeitgleich auf eine ähnliche Idee mit der
Hexagonalen Architektur gekommen. Davon wusste ich aber nichts in dem Irland Urlaub,
in dem ich wild Bilder mit dreieckigen Softwarezellen in mein Notizbuch gekritzel hatte -
zumLeidwesenmeinerFreundin.EslagetwasinderArchitekturluft,dasnachVeränderung
rief.DasbisdahinvorherrschendeArchitekturmusterSchichtenarchitektur waranGrenzen
gestoßen;seineNützlichkeitließzuwünschenübrig.


---


<!-- Page 353 of 584 -->


08-DieIODAArchitektur 344
Der erste Unterschied zu dem, was vorher empfohlen wurde, war die
deutlichere Ansiedlung der Domäne in der Mitte. Ich wollte sie her-
ausstellen, ihre Wichtigkeit betonen; deshalb ist sie als “fetter” Kreis
in der Mitte immer zu sehen, während andere Funktionsbereiche beim
Herauszoomenwegfallen.EsgehtumdieDomäne-derRestist“Beiwerk”,
eben Peripherie. Die Softwarezelle gehört also zu den konzentrischen
Architekturmodellen-auchwennsiehiernochalsDreieckdargestelltwar.
Damit wollte ich es leichter machen, mehrere Softwarezellen zu einem
“Gewebe”, d.h. zu einer verteilten Anwendnung zusammenzustellen:


---


<!-- Page 354 of 584 -->


08-DieIODAArchitektur 345
Aus Dreiecken lassen sich in der Computergrafik alle Formen zusam-
mensetzen. So dachte ich, dass ein Dreieck auch für alle möglichen
“Softwareformen” ein guter Grundbaustein sein könnten.
An diesem Bild wird dann auch der hauptsächliche Unterschied zu den
vorherigen Architekturmodellen sichtbar: dass Domänenlogik in allen
Teilen einer verteilten Anwendung anzutreffen ist. Sie ist nicht nur etwas,
das in einem Application Server läuft, wie sie Anfang der 2000er von Mi-
crosoft und anderen gepusht wurden, sondern Domänenlogik ist genauso
anwesendimFrontend-Prozess(z.B.inFormvonValidationslogik)wieim
Datenbank-Prozess (z.B. in Form von Stored Procedures).
Domäne in die Mitte und Domäne überall: darum ging es zunächst bei
der Softwarezelle. Die funktionalen Abhängigkeiten zwischen den Funkti-
onsbereichen innerhalb einer solchen Softwarezelle, die jeweils für einen
Betriebssystemprozess stand, waren mir noch nicht als Problem bewusst.
Wie du im ersten Bild siehst, sind sie sogar traditionell ausgerichtet,


---


<!-- Page 355 of 584 -->


08-DieIODAArchitektur 346
während in der Hexgonalen Architektur¹⁸⁷ eine teilweise Umkehrung
stattgefunden hatte.¹⁸⁸
AlistairCockburnsursprünglicheDarstellungderHexagonalenArchitektur
System vs. Umwelt
Zu der damaligen Zeit habe ich mich mit Systemtheorie, Konstruktivis-
mus und solchen Sachen beschäftigt. Deshalb war mir ein Anliegen, als
erstesbeimeinerArchitekturideeeinedeutlicheGrenzezuziehen.Mitder
“Zeugung” einer Software entsteht eine Dualität: Wo vorher “nichts” war,
steht jetzt ein Softwaresystem einer Umwelt gegenüber.
¹⁸⁷https://web.archive.org/web/20180822100852/http://alistair.cockburn.us/Hexagonal+
architecture
¹⁸⁸Wenn ich von Umkehrung spreche, dann meine ich nur die Ausrichtung der Ab-
hängigkeitenvonAbstraktionen,d.h.dieÜbersetzungszeitabhängigkeiten.Diefunktionalen
Abhängigkeiten zur Laufzeit sind über die Jahre in allen Architekturmodellen unangetastet
geblieben.


---


<!-- Page 356 of 584 -->


08-DieIODAArchitektur 347
Eine Software ist ein System von “verzahnten” oder “verdrahteten” Funk-
tionsblöcken,diezusammeneine“Reiz-Reaktion-Maschine”darstellen.Ei-
ne Software reagiert auf Einflüsse aus der Umwelt. Sie zeigt ein Verhalten,
das sich an der Veränderung von Daten ablesen lässt.


---


<!-- Page 357 of 584 -->


08-DieIODAArchitektur 348
Jede Softwarezelle ist ein solches System. Zu seiner Umwelt gehören
Anwender, Datenbanken, Scanner, TCP-Verbindungen - und natürlich
andere Softwarezellen.


---


<!-- Page 358 of 584 -->


08-DieIODAArchitektur 349
Eine Softwarezelle steht mit all dem in Beziehung. Sie interagiert mit den
“Agenten” in ihrer Umwelt. Wenn das andere Softwarezellen sind, dann
formen sie zusammen ein System auf höherer Ebene, das wiederum eine
Softwarezelle darstellt:


---


<!-- Page 359 of 584 -->


08-DieIODAArchitektur 350
Auch wenn der Ausgangsgedanke war, dass eine Softwarezelle einem
Betriebsystemprozess als Host für Code entspricht, passt eine Software-
zelleletztlichganzallgemeinauchzuSoftwaresystemenhöhererOrdnung.
Eine Softwarezelle ist ein Holon¹⁸⁹:
“A holon (Greek¹⁹⁰: ὅλον, holon neuter form of ὅλος, holos
“whole”) is something that is simultaneously a whole and a
part.”
Und stets erinnert der Punkt/Kreis in der Mitte daran, woum es eigentlich
geht:dieDomäne.SiestehtfürdenZweck,deneineSoftwarezelleerfüllen
soll.
¹⁸⁹https://en.wikipedia.org/wiki/Holon_%28philosophy%29
¹⁹⁰https://en.wikipedia.org/wiki/Ancient_Greek


---


<!-- Page 360 of 584 -->


08-DieIODAArchitektur 351
“Kleiderbügelarchitektur”
DasseineSoftwareeinSystemdarstellt,daseinerUmweltgegenübersteht,
ist noch kein Architekturmuster. Software als selbstähnliches System auf-
zufassen, das aus autonomen Einheiten - Softwarezelle - besteht, die man
auf unterschiedlichen Ebenen identifizieren kann, ist allerdings schon
ein ganz grobes, großes Architekturmuster oder -konzept. MVC oder
Schichtenmodell, selbst N-Tier Architecture¹⁹¹ als verteilte Erweiterung
des Schichtenmodells haben nicht dieses Bild von Software.
Indem du dir Software als bestehend aus Softwarezellen vorstellst, bist
du gerüstet für die Entwicklung eines Monolithen wie auch von Mi-
croservices. Softwarezellen nach oben und nach unten keine Größenbe-
schränkung haben. Wesentlich ist ihnen die Idee der Autonomie: Jede
Softwarezelle für sich steht für ein Bündel an Prozessen, mit denen sie
auf Umweltreize reagiert - unabhängig von anderen Softwarezellen, also
auch gleichzeitig.
Die Prozesse werden angestoßen durch Input-Nachrichten aus der Um-
welt, transformieren diese Daten in einem 3-dimensionalen Datenfluss
und geben schließlich Output-Nachrichten an die Umwelt ab. Die Interak-
tion besteht darin, dass derjenige, der dein Softwaresystem reizt, gewöhn-
lich auch der ist, der an seiner Reaktion interessiert ist. Ob das Menschen
¹⁹¹https://en.wikipedia.org/wiki/Multitier_architecture


---


<!-- Page 361 of 584 -->


08-DieIODAArchitektur 352
als Benutzer sind oder Maschinen oder andere Softwaresysteme, ist dafür
unerheblich.
Weil 3-dimensionale Datenflüsse sich nach unten ausweiten, also eine Art
Dreieck bilden, und weil viele davon nebeneinander in einem Software-
system existieren, entsteht damit - finde ich - das Bild eines Schrankes, in
dem Kleiderbügel nebeneinander hängen:
Auf jedem Kleiderbügel kannst du dir dann noch ein Kleidungsstück
für einen bestimmten Zweck vorstellen: Da hängt eine Regenjacke, ein
Wintermantel,eineSmoking-Jacke,einBlousonundvielesmehrnebenein-
anderundistbereit,deineAnforderungenjenachWetterundGelegenheit
zu erfüllen.
Wenn du ein technischeres Bild vorziehst, kannst du dir auch jede Soft-
ware als Ansammlung von Batch-/Shell-Skripten vorstellen. In jeder
.bat/.sh-Datei steht dann eine Kommandozeile, in der weitere Skripte
über Pipes verbunden sind usw. Die Interaktion damit findet dann viel-
leicht nicht über ein fancy GUI statt, sondern über die Kommandozeile,
doch das ist erstmal nur ein Detail.
Alles, was über Reize durch Eingaben auf der Kommandozeile oder eine
JSON-Datenstruktur, die du auf der Konsole eintippst, hinausgeht, alles,
was hübscher ist als ein JSON-Output auf der Konsole, das ist lediglich
der Unfähigkeit (oder Unwilligkeit) der Nutzer eines Softwaresystems


---


<!-- Page 362 of 584 -->


08-DieIODAArchitektur 353
geschuldet, sich mit dem universellen Medien stdin und stdout und
JSON-Daten zufrieden zu geben.¹⁹²
TicTacToekönnteauchsogespieltwerdenundwürdedireinigeMühemit
der Benutzerschnittstelle ersparen:
1 $ ttt
2 {
3 brett: [
4 "", "", "",
5 "", "", "",
6 "", "", ""
7 ],
8 status: "X ist am Zug"
9 }
10 Deine Eingabe: { zug: { spalte: 0, zeile: 1 } }
11 {
12 brett: [
13 "", "", "",
14 "X", "", "",
15 "", "", ""
16 ],
17 status: "O ist am Zug"
18 }
19 Deine Eingabe: ...
Oder so:
1 $ ttt neu
2 {
3 brett: [
4 "", "", "",
5 "", "", "",
6 "", "", ""
7 ],
8 status: "X ist am Zug"
9 }
10 $ ttt zug A2
11 {
12 brett: [
13 "", "", "",
14 "X", "", "",
15 "", "", ""
16 ],
17 status: "O ist am Zug"
18 }
19 $
Auch deshalb setze ich den Punkt in die Mitte des Softwaresystems und
machedarauseineSoftwarezelle:DieWichtigkeitderProzessessollbetont
werden gegenüber den technologischen Feinheiten zur Interaktion. Lass
¹⁹²ObesnunJSONoderXMLoderYAMLoderCSVDatensind,dieineinSoftwaresystem
hineinfließenundherausfließen,istnichtwichtig.Mirgeht’shierumdieBetonungderReiz-
verarbeitung als zentraler Aufgabe von Softwaresystemen. Wie eine Benutzerschnittstelle
aussieht, ist demgegenüber untergeordnet; Spracheingabe, GUI oder REST ist letztlich ein
technischesDetail.


---


<!-- Page 363 of 584 -->


08-DieIODAArchitektur 354
dich also nicht durch Benutzerschnittstellenanforderungen ins Bockshorn
jagen! Natürlich sollst du die am Ende erfüllen; doch was nützt die
hübscheste Benutzerschnittstelle, wenn die darüber abgesetzten Reize
nicht mit gewünschten Reaktionen beantwortet werden, weil intern der
Prozess nicht stimmt?¹⁹³
Die Membran
“SoftwareisteinSystem,dasausProzessenbesteht”isteinersterSchrittzu
einem Architekturmuster. Allerdings unterscheidet sich das von den übli-
chen, weil es quasi um 90° gedreht ist: Die bisherigen Architekturmuster
machenkeineAussageüberProzesse,überVerhaltensherstellung,sondern
über Struktur. Sie definieren kanonische Modul-Strukturelemente und
deren Zusammenhänge - während die “Kleiderbügelarchitektur” keine
Aussage macht über Module, sondern über Datenflüsse.
Muss es denn aber entweder-oder sein? Oder ist ein sowohl-als-auch
möglich? Ja, ich glaube, das geht.
Eine erste Unterscheidung über Module, die die Funktionseinheiten der
Datenflüsse aggregieren, liegt auch sehr nahe, finde ich: Es gibt solche,
diewirklich,wirklichzumKerneinerSoftwarezellegehören,zurDomäne,
und es gibt solche die zur Peripherie gehören. Diese Unterscheidung habe
ich schon öfter benutzt; jetzt weißt du, woher sie kommt.
Die Peripherie einer Softwarezelle nenne ich Membran. Das finde ich
passend, wenn das Ganze mit Softwarezelle sich an die Biologie anlehnt.
¹⁹³Aber dazu mehr im dritten Band von Programming with Ease: Beim Slicing geht es
darum, wie du mit Anforderungen so umgehst, dass du an die Aufhänger der Kleiderbügel
kommst.DerRestistdann“nurnoch”SacheeinesordentlichenEntwurfsderenDatenflüsse.
UnddamithastdudichindiesemBandbeschäftigt.


---


<!-- Page 364 of 584 -->


08-DieIODAArchitektur 355
Aufgabe der Membran ist es, das innere der (Software)Zelle von der
Umwelt zu isolieren. Es soll ein geschützter Raum entstehen, der eine
gewisse Stabilität aufweist und in dem sich etwas entwickeln kann, ohne
von den Turbulenzen in der Umwelt ständig durchgeschüttelt zu werden.
Die Umwelt stellt vielfältige Anforderungen an Software, die Umwelt
verändert sich unabhängig von Software - und das soll nicht sofort
komplett auf die Prozesse durchschlagen. Die Membran entkoppelt die
Innenwelt von der Außenwelt.


---


<!-- Page 365 of 584 -->


08-DieIODAArchitektur 356
Die Membran ist wie ein Puffer, der Veränderungen außen in ihrem
Einfluss auf den Kern abmildert. Gleichzeitig ist die Membran eine Über-
setzungsstrecke,aufderÄußeresfürInnenverständlichgemachtwirdund
Inneres für die Umwelt.
Ventrale Interaktion: Portale
Die offensichtliche und erste Aufgabe der Membran ist es, Abhängigen
eine Softwarezelle zugänglich zu machen. Abhängig sind die “Agenten”


---


<!-- Page 366 of 584 -->


08-DieIODAArchitektur 357
in der Umwelt, die Softwarezellen für ihre Zwecke nutzen wollen, es
sind die (Be)Nutzer, die User. Ob das Menschen oder Maschinen sind,
ist weiterhin unerheblich. Benutzer fordern Softwarezellen zu Verhalten
auf. Sie reizen sie und sind gespannt auf die Reaktion. Softwarezellen sind
damit grundsätzlich Benutzern zugewandt.
Benutzer initiieren Dialoge mit Softwarezellen. Softwarezellen sind als
erstes in Interaktionen mit Benutzern eingebunden und müssen deren
Eingaben entgegennehmen, verarbeiten und schließlich Ergebnisse aus-
geben. Dafür ist Logik jenseits der Domäne nötig. Diese Logik ist Teil der
Membran - und sie ist Teil des gesamten Verarbeitungsprozesses.


---


<!-- Page 367 of 584 -->


08-DieIODAArchitektur 358
Weil diese Logik dem Benutzer zugewandt arbeitet, nenne ich diesen Teil
der Membran auch die ventrale Membran; es handelt sich um ventrale
Interaktionen.¹⁹⁴
¹⁹⁴Bildquelle: Medical gallery of Blausen Medical 2014. WikiJournal of Medicine 1 (2).
DOI:10.15347/wjm/2014.010.ISSN2002-4436.-Ownwork,CCBY3.0


---


<!-- Page 368 of 584 -->


08-DieIODAArchitektur 359
Eine Softwarezelle ist dadurch asymmetrisch strukturiert. Die Membran
umschließt den Kern zwar vollständig, doch sie ist unterschiedlich aus-
geprägt. Weil es naheliegender ist, stelle ich dir zuerst den ventralen,
benutzerzugewandten Aspekt vor.
Etwas technischer nenne ich diesen Aspekt auch Portal. Der ventrale
Teil der Membran wird konstituiert durch eines oder mehrere Porta-
le, jenachdem, wieviele Benutzer oder Benutzerrollen du unterscheiden
willst. Portale stehen für UI-Technologien (z.B. Konsole, GUI, Web, REST)
und Sichtweisen auf die Softwarezelle (z.B. Sachbearbeiter, Manager,
Buchhaltung).


---


<!-- Page 369 of 584 -->


08-DieIODAArchitektur 360
Portale sind Adapter. Sie passen Umwelt und Innenwelt aneinander
an. Dafür bestehen Adapter - wenn man genau hinschaut - aus einem
Sammler (collector, editor) und einem Projektor (projector).


---


<!-- Page 370 of 584 -->


08-DieIODAArchitektur 361
Da es ein wenig umständlich ist, so zu zeichnen, gibt es aber auch eine
verkürzteDarstellung.InderwerdenPortaledurchQuadraterepräsentiert.
Die Kreislinie deutet an, dass sich Adapter rundherum befinden; doch die
gerade wesentlichen werden eben mit einem Quadrat hervorgehoben:


---


<!-- Page 371 of 584 -->


08-DieIODAArchitektur 362
Eine Unterscheidung zwische Sammlung und Projektion ist dabei ge-
wöhnlich auch nicht nötig. Später taucht sie nochmal auf; du solltest
sie also im Hinterkopf behalten. Einen hervorhebenswerten Aspekt des
Architekturmusters stellen sie jedoch nicht dar.
Interessanter sind da schon die Abhängigkeitsverhältnisse. Bisher habe
ich Pfeile eingezeichnet für den Datenfluss zwischen Softwarezelle und
Benutzern. Die Daten fließen allerdings entlang einer Abhängigkeitsbe-
ziehung.SoftwarezelleundBenutzersindsozusagennichtaufAugenhöhe.
Vielmehr ist der Benutzer abhängig von der Softwarezelle. Er braucht sie,
nicht umgekehrt. Für ihn wurde sie geschaffen.


---


<!-- Page 372 of 584 -->


08-DieIODAArchitektur 363
An diesem Abhängigkeitsverhältnis kannst du Benutzer immer erkennen,
egal wo sie in einem Softwarezellendiagramm angeordnet sind. Das
Abhängigkeitsverhältnis geht vom Benutzer aus zur Softwarezelle und
wird dort mit einem Portal bedient. Das Portal enthält die Logik, die die
Interaktion mit dem Benutzer möglich macht.
Dorsale Interaktion: Provider
Benutzer brauchen eine Softwarezelle “zu ihrem Glück”; für sie ist eine
Softwarezelle eine Ressource, von der sie abhängig sind.
Umgekehrt brauchen aber auch Softwarezellen Ressourcen; sie sind eben-
falls abhängig von “Agenten” in der Umwelt. Softwarezellen sind selbst
Nutzer anderer Softwarezellen oder benötigen Hardware der einen oder
anderen Art, um ihre Aufgabe zu erfüllen.
Typische Ressourcen sind Dateisystem, Datenbank, TCP-Kommunikation.
AberauchderZugriffaufdieZeit,ZufallszahlenoderdieUUID-Generierung


---


<!-- Page 373 of 584 -->


08-DieIODAArchitektur 364
sind Ressourcenzugriffe¹⁹⁵, weil dabei die Hardware eine Rolle spielt.¹⁹⁶
Diese Abhängigkeiten werden in einer Softwarezelle repräsentiert und
gekapselt in Adaptern, die ich Provider nenne. Ihr “Kürzel” ist im Soft-
warezellendiagramm das Dreieck:
Adapter gehören zur Peripherie wie die Portale. Sie enthalten Logik, die
¹⁹⁵Ein Ressourcenzugriff wie auf die Systemuhr mag nicht erwähnenswert sein. Warum
solltest du dafür einen Provider aufsetzen? Es geht nicht um den Aufwand, sondern um die
Testbarkeit. Nur, wenn du Ressourcenzugriff an einem Ort kapselst, im Provider, hast du
später eine Chance, sie in Tests bei Bedarf durch ein Surrogat zu ersetzen. Siehe dazu auch
denBandTest-firstCodierung meinerReiheProgrammingwithEase.
¹⁹⁶Hardware wie Tastatur, Maus, Bildschirm fällt in die Zuständigkeit von Portalen. Für
dieBildschirmausgabeistalsokeinProvidereinzuzeichnen,sonderndieübernimmtdasselbe
Portal,dasauchdieEingabevomBenutzerliest.


---


<!-- Page 374 of 584 -->


08-DieIODAArchitektur 365
die Interaktion mit den Ressourcen vermittelt.¹⁹⁷
Das sind für mich die dorsalen Interaktionen; sie finden hinter dem
Rücken der Softwarezelle statt und müssen die Benutzer, denen sie zu-
gewandt ist, nicht wirklich interessieren.
¹⁹⁷Im vorstehenden Bild siehst du eine Softwarezelle sowohl als Benutzer wie auch als
Ressource. Das habe ich ganz bewusst so gezeichnet, denn so ist es: Softwarezellen, d.h.
SoftwareisteinerseitsDienstleister(StichwortServer)fürandereSoftwareundandererseits
ist sie deshalb auch Dienstnehmer (Stichwort Client) von anderer Software. Ob ich in
einem solchen Diagramm andere Software als Softwarezelle einzeichne oder z.B. durch ein
Hardwaresymbol repräsentiere oder gar ein Firmen-/Produkt-Logo, hängt davon ab, ob die
nutzende/benutzte Software zum Scope des Projektes gehört. Liegt sie innerhalb des Scope,
muss dein Team sie also selbst entwickeln, dann solltest du sie als Softwarezelle darstellen;
denn dann wirst du dich früher oder später mir ihrem Innenleben beschäftigen müssen. Ist
das nicht der Fall, wähle irgendein aussagekräftiges Symbol. Als Beispiel nimm hier die
“Datenbanktonne”, die für einen MongoDB Server in der lokal oder in der Cloud stehen
könnte.


---


<!-- Page 375 of 584 -->


08-DieIODAArchitektur 366
Du kannst dir die Provider als Rückgrat der Softwarezelle vorstellen.
Daran richtet sie sich auf. Ohne Unterstützung der Ressourcen kann sie
ihre Leistung nicht erbringen.
Eine Softwarezelle steht “rundherum” mit der Umwelt in Verbindung
über Adapter. Portale und Provider bilden zusammen die Membran der
Softwarezelle; sie liegen auf der Peripherie, während die Domäne im
Kern steckt. Dennoch ist die Kommunikation mit der Umwelt nicht
symmetrisch:
• Benutzer kontrollieren die Softwarezelle; die Interaktion zwischen
beiden geht von den Benutzern aus.
• Ressourcen werden von der Softwarezelle kontrolliert; die Interak-
tion zwischen beiden geht von der Softwarezelle aus.


---


<!-- Page 376 of 584 -->


08-DieIODAArchitektur 367
Deshalb die unterschiedlichen Bezeichnungen für die Adapter: Portal
vs Provider, auch wenn sie technisch dasselbe leisten: Isolation und
Übersetzung. Deshalb auch die Unterscheidung in ventrale und dorsale
Interaktion/Kommunikation. Ich finde diese Begriffe aus der Medizin
passend zu der Asymmetrie in der Software.
Adapteraufgaben
Auf einer hohen Flughöhe über einer Softwarezelle sind Adapter Black
Boxes. Ihre Aufgabe ist pauschal die Anbindung von Domäne an Umwelt
bzw. umgekehrt. Doch wenn du näher ranzoomst, dann siehst du in ihnen
Muster. Adapter haben immer wieder dieselben Aufgaben:
• Technische Kommunikation (API call): ein API muss gekapselt
werden, über den mit der Umwelt Nachrichten ausgetauscht wer-
den können. Triviale Beispiele sind Console.WriteLine() oder
File.ReadAllLines().
• Mapping: APIs liefern Daten aus der Umwelt und senden Daten an
die Umwelt in einem gewissen Format. Dieses Format ist technisch
motiviert.MitdemInnenraumeinerSoftwarezelle,garderDomäne
hat es nichts zu tun oder sollte es auch gar nicht. Zwischen API
und Innenraum muss also eine Datenformattransformation statt-
finden. Ein triviales Beispiel: aus einem Dateinamen und einem


---


<!-- Page 377 of 584 -->


08-DieIODAArchitektur 368
Text gelesen aus der Datei wird ein Datei()-Objekt für die Netto-
zeilenzählung. Etwas aufwändiger ist das Mapping ausgefallen bei
TicTacToe: aus einer Zugliste wird eine Maxtrix. Das Parsing der
Kommandozeile, was du in verschiedenen Beispielen gesehen hast,
enthält auch ein solches Mapping.
- Validation: Daten, die aus der Umwelt in eine Softwarezelle kommen,
müssen auch immer wieder mal validiert werden. Haben sie eine akzep-
table Form, sind sie also syntaktisch korrekt? Diese Prüfung findet ganz
oder zum Teil schon beim Mapping statt. Aber ist der syntaktisch korrekte
Inhalt, der in einer Domänendatenstruktur gewandelt werden konnte,
auchinhaltlich,semantischakzeptabel?Manchmalkanndaserstwährend
der Verarbeitung in der Domäne festgestellt werden. Aber manchmal
kann und sollte die Validation davon getrennt als eigener Prozessschritt
modelliert werden. Ein triviales Beispiel: bei TicTacToe wurde geprüft, ob
ein syntaktisch korrekter Zug wie (1,0) zu Zeitpunkt des Zuges auch
möglich war, d.h. zur Spielsituation passte.
Je nach Adapter wirst du diese Aufgaben unterschiedlich umfänglich
und differenziert implementieren. Im Bild siehst du sie natürlich deutlich
separiert, weil ich dir mitgeben will, sie im Hinterkopf zu haben und als
Chance zu einer Zerlegung von Problemen zu sehen. Lass sie dir eine
Analysehilfe sein: Schau mit ihnen auf ein Problem und trenne darüber
schoneinigekomplementäreTeilproblemeheraus.EinenZerlegungsbaum
zu entwickeln, fällt dir damit manchmal leichter.


---


<!-- Page 378 of 584 -->


08-DieIODAArchitektur 369
DieseAufgabenkannstdueinfach so,wie gezeigt,in Reiheschalten. Doch
welchen Modulen gehören sie an? Im einfachsten Fall sind sie Teile des
Adapters.
Wennsiejedochumfänglicherwerden,lohnensichseparateModule.Ganz
ausdifferenziert sähe das dann so aus:
API call, Mapping und Validation sind “auf Augenhöhe”, d.h. komplemen-
täreTeileeinesProzessesundwerdenüberzweiEbenenhinwegintegriert.
DerMappingAdapter{}würdeden“rohen”APIcallmiteinemMapping
dekorieren;undderValidatingAdapter{}würdedengemapptenAPI-
Zugriff noch mit einer Validation ausstatten.
Hier im Beispiel sieht das etwas überkandidelt aus. Doch wenn dein Code
wächst, ist das ein Muster, auf das du zurückgreifen kannst. Es folgt
dem Grundsatz, dass Abhängigkeiten dem Abstraktionsgradienten folgen:
höhereAbstraktionenhängenvonniedrigerenab.EinvalidierendesPortal
ist liegt höher als ein Portal, das nur rohe Daten aus der Umwelt beschafft.
Denk an stratified design! Das gilt auch im Kleinen, wenn es nur um ein
Portal oder einen Provider geht.


---


<!-- Page 379 of 584 -->


08-DieIODAArchitektur 370
“Griechische Architekturen”
Die Verarbeitungsprozesse innerhalb einer Softwarezelle “hängen nicht
in der Luft”. So suggeriert es aber die obige “Kleiderbügelarchitektur”.
Die war zwar ein guter Einstieg in die prozessorientierte Strukturierung
von Software; so hast du ein erstes Bild davon bekommen, wie es darin
aussieht. Doch jetzt möchte ich genauer werden.
Die Kleiderbügel haben den tiefen und breiten Datenfluss repräsentiert,
der die eigentliche Transformation von Benutzerdaten in Benutzerdaten
vornimmt. Der Fokus war dabei auf der Wurzel, dem Aufhänger des Klei-
derbügels, unter dem sich dieser Prozess in seinen Feinheiten ausdehnt.
Wie die Bilder mit den Providern nun aber gezeigt haben, gibt es gar nicht
dieseeineWurzel;siewarnurderRepräsentantfürdas,waszwischenden
Aspekten Sammlung und Projektion eines Portals passiert. Genauer sieht
es so aus:


---


<!-- Page 380 of 584 -->


08-DieIODAArchitektur 371
Die “Kleiderbügelarchitektur” ist also nur eine plastische erste Näherung.
So einprägsam das Bild sein mag, so sehr es für den Anfang taugt, ich
möchte es jetzt verlassen zugunsten eines anderen Bildes. Raus aus dem
Schrank, rein in die Kultur.
Schon etwas realistischer scheint mir, den Provider am Anfang und am
Ende überhaupt mit ins Bild zu nehmen. Das soll mit der “Xi Architektur”
geschehen.XiisteinBuchstabedesgriechischenAlphabets,dermitseinen
Strichen hübsch die unabhängigen Prozesse darstellen kann, die da vom
Provider über den Kern zum Provider arbeiten.
Doch das kann nur der Anfang sein. Die Verarbeitungsprozesse sind ja
auch über Provider mit der Umwelt verbunden; das sollte die Darstellung
hergeben: Nachrichten kommen aus der Umwelt (ventral), werden unter


---


<!-- Page 381 of 584 -->


08-DieIODAArchitektur 372
Zugriff auf Ressource in der Umwelt verarbeitet (dorsal) zu Nachrichten,
die wiederum an die Umwelt hinausfließen (ventral).
Adapter sind “an allen Ecken und Enden” dabei beteiligt. Der Datenfluss
des Verarbeitungsprozesses einer Interaktion ist damit innerhalb der Soft-
warezelle aufgespannt.
Aus dem Xi würde damit ein Tau:


---


<!-- Page 382 of 584 -->


08-DieIODAArchitektur 373
Doch auch das ist natürlich noch stark vereinfacht. Denn selten gibt es in
einem Prozess nur einen lesenden oder schreibenden Zugriff auf eine Res-
source; meistens sind es viele lesende und schreibende und das auch noch
im Wechsel und in Bezug auf verschiedene Ressourcen. Deshalb würde
ich mindestens von einer “Pi Architektur” sprechen, um zu beschreiben,
wie Softwarezellen mit Datenflüssen strukturiert sind:


---


<!-- Page 383 of 584 -->


08-DieIODAArchitektur 374
Software besteht zunächst einmal aus Prozessen. Diese Prozesse werden
aus der Umwelt gespeist und liefern Ergebnisse an die Umwelt. Und diese
Prozesse nutzen Ressourcen in der Umwelt, um ihre Arbeit zu erledigen.
Dass für dich diese Vorstellung von Software primär wird, möchte ich
mit all diesen Bildern erreichen. Die Bilder müssen dir gar nicht speziell
gefallen; du kannst dir gern andere, für dich passendere Bilder ausdenken;
Hauptsache sie prägen sich irgendwie bei dir ein, weil sie so anders sind,
als das, was du üblicherweise siehst. Denn die Prozesspersketive ist so
anders als das Übliche.
Und was ist das Übliche? Das Übliche ist eine reine Strukturperspektive.
Es werden nur Funktionsbereiche gezeigt, also im Grunde Module. Das
wirst du hier später auch sehen, weil mein Architekturmuster da einen
großen Unterschied macht; doch erstmal noch ein wenig weiter mit dem
Prozess-Fokus.¹⁹⁸
Der Kern
Und was passiert zwischen den Kontakten der Adapter mit der Umwelt?
Da passiert die Domäne. Die Domäne macht den Kern einer Software
¹⁹⁸Natürlich können dir schon jetzt alle oder alle bis auf einen Funktionsbereich meines
Architekturmustersklarsein.Ichverheimlichesienicht.Nurwillichsienochnichtüberdie
Prozessehinausheben.IchmöchtemitdirnochetwasmehrausPerspektivederDatenflüsse
auf“dieInnereien”vonSoftwareschauen.


---


<!-- Page 384 of 584 -->


08-DieIODAArchitektur 375
aus. Nimm als Beispiel TicTacToe: Unabhängig davon, wie die Benut-
zerschnittstelle aussieht, das Spiel wird immer gleich gespielt. Den Code
für die Domäne solltest du in einer Konsole-Anwendung oder eine Web-
Anwendung verwenden können. Oder nimm die Nettozeilenzählung:
Unabhängig davon, ob die Zählung über die Kommandozeile oder ein
GUI angestoßen wird, egal, ob das Resultat als Text auf der Konsole
oder als Grafik in einem GUI gezeigt wird, und auch einerlei, ob der
Quellcode aus dem lokalen Dateisystem oder von einem FTP-Server
kommt, den Code für die Domäne solltest du nicht ändern müssen. Die
Membran mit ihren Portalen und Providern soll all diese technischen
Feinheiten der Interaktion mit der Umwelt vor dem Kern verbergen. Der
soll isoliert ruhig in der Mitte einer Softwarezelle seinen Dienst tun, auch
wenn der Auftraggeber mal wieder eine neue Idee zur Interaktion hat.
Dass die Benutzerschnittstelle sich ändern soll, dass eine neue Ressource
anzubinden ist, sind ja keine Seltenheiten.
Domänenlogik
Die Domäne besteht zunächst einmal aus Domänenlogik. Wir haben ja
die Prozessbrille auf. Da sehen wir zuerst die Logik, die im Rahmen eines
Prozesses einen Beitrag zur Gesamttransformation der Daten leistet. Bei
TicTacToe war die am Ende im Schiedsrichter{} versammelt.


---


<!-- Page 385 of 584 -->


08-DieIODAArchitektur 376
Die Domäne umfasst die Logik, die frei ist von Gedanken an die Umwelt.
Idealerweise könntest du die Domänenlogik entwickeln, ohne Ansehen
der Umwelt. Das ist auch immer wieder der Traum der mainstream
Objektorientierung. Doch leider ist es ein Traum, ein Ideal. In der realen
Projektwelt ist das selten machbar. Der Preis für vollständig unabhängige
Modellierung der Domänenlogik besteht allzuoft in einem spürbaren
Verlust an einer oder mehrerer Effizienzen.
Damit das keine unangenehme Überraschung ist, ziehe ich eine rea-
listische Vorgehensweise vor, wie ich sie dir bisher versucht habe zu
vermitteln:
1. Entwirf deine Lösung, so dass du weit vor der Codierung alle
Einflussfaktorenberücksichtigenkannst,d.h.funktionalewienicht-
funktionale Anforderungen.
2. Entwirf deine Lösung prozessorientiert outside-in und top-down.
Lass dich treiben von den konkreten funktionalen Anforderungen;
entwirf Datenflüsse von den Enden her und dann in die Tiefe. Be-
rücksichtige dabei natürlich die nicht-funktionalen Anforderungen.


---


<!-- Page 386 of 584 -->


08-DieIODAArchitektur 377
3. Modularisiere erst, wenn du eine Masse an funktionalen Prozess-
bausteinen hast, in denen du Muster sehen kannst, die Aggregatio-
nen nahelegen.
Das ist aus meiner Sicht der beste Weg, um nicht der Illusion von der
“Astronauten-Domänenlogik” aufzusitzen, die unbeeindruckt von irdi-
schen Einflüssen im All schwebt.
Und was war die Domänenlogik bei der Nettozeilenzählung? Die stecke
imModulFilter{}.Warsiedortabersoformuliert,dasssiedieUmwelt
ignorieren konnte? Nein! Sie war bewusst auf eine Umwelt ausgelegt,
in der die Zahl der zu analysierenden Dateien “überschaubar” war. Im
ModellfindestdueineCollectionvonDateienalsInputderDomänenlogik.
In der Wahl einer Liste steckt die Entscheidung für eine bestimmte
Umwelt. Die Domänenlogik nicht als Astronaut in eine Umlaufbahn zu
schießen hatte den ganz irdischen Grund, dass sie völlig unabhängig
womöglich aufwändiger ausgefallen wäre.
Die völlige Umweltunabhängigkeit ist eine Optimierung, die sich meiner
Meinung nach nur selten lohnt. Die viel zitierte “Wiederverwendbarkeit”
beschwört sie zwar herauf - doch das kostet eben eine Menge. Die
Frage ist, ob du das Budget an Zeit und Geld hast. Ich kann dir also
nur raten, gehe vom Naheliegenden, vom Bekannten aus und spekuliere
nicht zu viel, was mehr oder weniger weit hinter dem Horizont der
aktuellen Anforderungen liegen könnte. Vertraue lieber darauf, dass du
mit sauberem Flow-Design und sauberer Übersetzung deiner Modelle
in Code eine gute Grundlage dafür legst, dass deine Software sich den
kommenden Überraschungen anpassen lässt.
Domänendaten
Zur Domänenlogik in ihren Modulen gehören auch die Domänendaten.
Zusammen bilden sie die Domäne, den Kern jeder Anwendung.


---


<!-- Page 387 of 584 -->


08-DieIODAArchitektur 378
Die gibt es immer, es fragt sich nur, inwiefern du sie sichtbar machst im
Modell in Form eigener Datentypen (Module). Von Domänendaten oder
dem Domänendatenmodell spreche ich hier vor allem in Form eigener
Domänendatentypen. Die Datei{} bei der Nettozeilenzählung oder das
Spielbrett{} sind einfache Beispiele für Domänendatenmodelle.
Domänendatenfließenund/oderstehenimDatenflussderDomänenlogik
unddurchausauchdarüberhinaus.Immersind siejedochDaten,während
Module der Domänenlogik allenfalls Domänendaten haben.


---


<!-- Page 388 of 584 -->


08-DieIODAArchitektur 379
So wie die Domänenlogik isoliert von der Umwelt sein soll durch die
Membran, so sollen auch die Domänendaten nichts mit der Umwelt zu
tun haben. Das gehört für mich zu den Grundsätzen der Softwarearchi-
tektur. Im TicTacToe Beispiel habe ich deshalb bewusst eine ganz andere
Domänendatenstruktur gewählt im Vergleich zu der, mit der das Portal
gearbeitet hat.
Hier und da musst du wohl auch bei den Domänendaten mal Kompro-
misse eingehen. “Astronauten-Datenstrukturen” sind zu teuer. Das ändert
allerdings nichts am Prinzip der Unabhängigkeit. Domänendaten sind
verzahnt mit der Domänenlogik und nicht mit der Umwelt und ihren
Repräsentanten in der Software, den Adaptern.
Zwischen Domänendaten und Domänenlogik passt also kein Blatt. Aber
zwischen Umwelt und Domänendaten passt eine Wand. Da ist eine Über-
setzung nötig. Im TicTacToe-Beispiel war dafür das Mapping zuständig.


---


<!-- Page 389 of 584 -->


08-DieIODAArchitektur 380
Das Mapping ist mal dünner und mal dicker. Immer solltest du es aber
im Blick behalten. Lieber irre mal in Richtung zu dickem Mapping als
umgekehrt. Am Ende ist der Mappingaufwand, so lästig er ist, gering im
Verhältnis zu anderer Logik.¹⁹⁹ Der Gewinn durch Entkopplung jedoch,
der ist hoch! Sei nicht bequem; lass ihn dir nicht wegen ein wenigFaulheit
durch die Lappen gehen.
Die Bezeichnung Domänenlogik suggeriert, dass nur in Modulen der
Domänenlogik, also in Serviceklassen Funktionen sein dürfen, die Logik
enthalten. Vordringlich ist das zwar so, aber nicht vollständig. Domä-
nendatentypen sind auch dazu da, Logik auf sie zu schieben. Finde den
natürlichen Ort für Logik: manchmal ist der in einem Servicemodul,
manchmal in einem Datenmodul.
Wenn du stark geprägt bist durch mainstream Objektorientierung, dann
musst dich vielleicht ein wenig anstrengen, Logik aus Datentypen zu
¹⁹⁹In trivialen Szenarien kannst du auch mal ohne Mapping leben. Denk nur daran,
wie schnell aus trivialen Szenarien dann weniger triviale und am Ende komplexe werden.
Wie oft wurden aus Case Studies, Prototypen, privaten Projekten am Ende Produkte, die
hoheFlexibilitätundhoheStabilitätaufweisenmüssen?Inzwischengibtesauchzahlreiche
Helferlein, die dir beim Mapping zur Hand gehen oder es sogar ganz übernehmen. Schau
dichbeideinerEntwicklungsplattformmalum.


---


<!-- Page 390 of 584 -->


08-DieIODAArchitektur 381
entfernen. Es ist wahrscheinlich, dass die damit überladen sind. Wenn
du stark von Funktionaler Programmierung geprägt bist - aber immer
noch so wenig, dass du bis hierher durchgehalten hast -, dann kann
dein Code, wenn du mit einer hybriden Programmiersprache arbeitest,
wahrscheinlich davon profitieren, dass du ab und an mehr Logik an
Datentypen anlagerst.
Tutmirleid,denBegriffwiedermalanzurufen,aberesisteineSacheder…
Balance.
“Vitruvianische Architektur”
Zeit für ein weiteres Architekturbild, oder? Erst die Kleiderbügel, dann
die griechischen Buchstaben und jetzt… Jetzt muss der Kern ins Daten-
flussbildeingebautwerden.DieKleiderbügelsolltennurüberhauptzeigen,
dass Software erstmal und vor allem aus Prozessen besteht; ohne Prozesse
ist sie nichts. Und die griechischen Buchstaben haben dann diese Prozesse
an die Membran “angeheftet”.
AberwassollendieProzesseleisten?DasstecktimKernderSoftwarezelle,
in der Domäne. Es geht - wie könnte es anders sein - um das, was die
Membran umschließt. Die Adapter sind sozusagen nur die Glieder einer
Software; mit ihnen greift sie in die Umwelt, holt von da und platziert
dort. Die Domäne hingegen macht den Rumpf einer Software aus; er wird
durch sie bewegt und geschützt.
Ein vollständigeres Architekturbild ist für mich daher dieses:


---


<!-- Page 391 of 584 -->


08-DieIODAArchitektur 382
Leonardo da Vincis Vitruvianischer Mensch²⁰⁰ symbolisiert für mich
darin einerseits die Wichtigkeit der Domäne, andererseits aber auch die
Notwendigleit ihrer Anbindung an die Umwelt. Auch wenn die Domäne
das ist, worum es bei Software geht, existiert sie nicht im luftleeren Raum.
Umgekehrt haben Adapter allein keinen Zweck, sondern stets nur in
Zusammenhang mit dem “Schutz” einer Domäne.
In der “Pi-Architektur” wurden die Adapter betont, in der “Vitruvia-
nischen Architektur” gibt es diese Betonung nicht mehr, sondern die
Adapter hängen mit der Domäne zusammen und umgekehrt. Es geht um
die Einheit in der Differenz der Zwecke.
The Missing Concern: Integration
“It’s the processes, stupid!” könnte ich sagen. Ja, daran glaube ich, dass es
vor allem um die Prozesse in einer Software geht - und dann erst um die
Module. Deshalb hast du in den bisherigen Architekturbildern vor allem
Datenflüsse gesehen.
²⁰⁰https://de.wikipedia.org/wiki/Vitruvianischer_Mensch


---


<!-- Page 392 of 584 -->


08-DieIODAArchitektur 383
Doch Module haben natürlich ihre Berechtigung. Ihre Aggregationen
machen es einfacher, einen Überblick zu gewinnen. Passieren müssen
die Dinge in Prozessen; doch was ist da in Prozessen verdrahtet? Welche
hauptsächlichen Funktionsbereiche gibt es? Darum dreht es sich bei den
üblichen Architekturmustern. Darauf muss auch ich eine Antwort liefern,
damit meine Architekturidee vergleichbar ist und “Empfehlungspower”
hat. Sie soll dir ja eine Erwartungshaltung vermitteln, welche Funktions-
bereiche du in deiner Software finden bzw. einrichten solltest.
Lass uns mal schauen, was wir da bisher haben in der letzten Prozess-
Architekturvariante. Ich sehe da eine Hierarchie von Funktionsberei-
chen:²⁰¹
• Softwarezelle
– 1 x Membran/Adapter
* n x Portal
* n x Provider
– 1 x Kern/Domäne
* n x Domänenlogik
* n x Domänendaten
Ob eine Softwarezelle als Service übersetzt wird oder als Wave, ob ein
PortalzueinerKlasseodereinerKomponentewird,dasistnichtsowichtig.
In jedem Fall reden wir über Module. Die bisherigen Funktionseinheiten
der Datenflüsse sind verschwunden. Wird befinden uns “in einer anderen
Dimension”.
²⁰¹IchlassedieAspektederAdaper-APIcall,Mapping,Validation-ausdieserHierarchie
heraus. Das sind Verfeinerungen, denen in anderen Architekturmustern nichts gegenüber-
steht. Du hast sie im Hinterkopf und wirst sie bei Bedarf dort hervorholen. Im big picture
sindsienichtnötig.


---


<!-- Page 393 of 584 -->


08-DieIODAArchitektur 384
In dieser Dimension geht es traditionell um Struktur. Das heißt, es geht
darum, wie die Funktionsbereiche von einander (funktional) abhängig
sind. Ich reduziere zur Beantwortung dieser Frage mal die Softwarezelle
auf ein Modul je Funktionsbereich:


---


<!-- Page 394 of 584 -->


08-DieIODAArchitektur 385
Wie sind die Funktionsbereiche von einander abhängig? Welcher braucht
und kennt welchen anderen? Was meinst du?
IOSP in der Architektur
In dem Architekturmuster, das ich dir nahelege, lautet die Antwort: die
Funktionsbereiche sind nicht von einander abhängig.
Das ist der Trick! Das macht das Muster so anders als die bisherigen.
Ob MVC, Schichtenarchitektur oder Clean Architecture: überall sind die
Funktionsbereiche nicht nur abhängig, sondern funktional abhängig. Das
ist verständlich, wenn man die Entwicklungsgeschichte der Architektur-
musterbedenkt, aber das macht es nicht besser.Wir können ihnen danken
für die Dienste, die sie geleistet haben - und dann verabschieden wir uns
von ihnen.
Funktionale Abhängigkeiten sind schlicht ein Übel. “In der Natur” gibt es
sie nicht. Sie sind menschengemacht und treten erst innerhalb menschli-
cher Organisationen auf. Doch sollten wir Software so strukturieren, wie
Organisationen, gar Unternehmen? Wie schlecht die sich re-organisieren
lassen, ist ja kein Geheimnis. Ich bin also dagegen und schlage etwas
anderes vor.


---


<!-- Page 395 of 584 -->


08-DieIODAArchitektur 386
Ist dir aufgefallen, was in den obigen Architekturbildern gefehlt hat? Ich
habe munter Datenflüsse durch die Softwarezellen gelegt und für diese
Sichtweise als die primäre plädiert. Dabei habe ich jedoch eines völlig
außen vor gelassen: die Integration.
Wer integriert denn die Datenflüsse, die sich da von Portal/Sammler über
Domäne und Provider bis zu Portal/Projektor spannen? Irgendwer muss
die Funktionseinheiten ja zu einem Fluss verbinden. Eine beispielhafte,
vereinfachte Verbindung der Funktionsbereiche als Abstraktionen ihrer
Funktionseinheiten zu einem Datenfluss könnte so aussehen:
Eingabedaten fießen vom Portal gesammelt und durch Daten aus einer
Ressource angereichert an die Domäne, die sie in ein Ergebnis transfor-
miert, das zum Teil in einer Ressource gespeichert wird und ansonsten
zur Ausgabe weiter ans Portal fließt.
Ob vor dem Ressourcenzugriff schon die Domäne im Spiel ist oder auch
noch danach, macht keinen Unterschied. Wesentlich ist die Klammerung
des ganzen Flusses durch das Portal. Es muss am Anfang stehen, weil es
sonst nichts zu verarbeiten gibt. Es muss auch am Ende stehen, weil sonst
die Verarbeitung niemandem nützt.²⁰²
Interactors
DieersteEbenederIntegrationderFunktionsbereicheziehtalleüberhaupt
zusammen. Das ist die fehlende Integration in den bisherigen Bildern.
²⁰²WieumfangreichdasPortaloderderProvideroderdieDomänegestaltetsind,istauch
unerheblich. Die Domäne kann Tausende Zeilen Logik umfassen und ein Provider nur eine
odereinPortal/ProjektorkannquasileerseinundderlesendeProviderTausendeZeilenlang.
EsgehtumeineprinzipielleVerschaltungderFunktionsbereiche.


---


<!-- Page 396 of 584 -->


08-DieIODAArchitektur 387
Jetzt sind Portal, Provider und Domäne in einer Komposition vereint.
Jetzt kann die Umwelt mit Provider und Domäne interagieren. Diese
Integration nennen ich deshalb Interactor.
Main() oder ihre Klasse Program{} wie in den bisherigen Beispielen,
ist allerdings nicht der Interactor. Bisher war das der Einfachheit halber
ok, doch wenn die Anwendungen wachsen, lohnt es sich, ein Interactor-
Modul eigens zu definieren. Sein Verantwortlichkeit ist, die Umwelt mit
der eigentlichen Verarbeitung zu verbinden.
Die Verantwortlichkeit für die Main() und Program{} konzentriert sich
dadurchaufKonstruktionundKonfigurationvonFunktionsbereichen/Ob-
jekten.


---


<!-- Page 397 of 584 -->


08-DieIODAArchitektur 388
Interactors gibt es allerdings in zwei Ausprägungen, abhängig davon, wie
die Kommunikation mit der Umwelt abläuft.
Application
Wenn ein Portal, das vom Interactor integriert wird, auf Reize von der
Umwelt wartet, nenne ich ihn Application. Bei einer Application wird das
Portal innerhalb der Integration gestartet und wartet auf eine Eingabe
von der Umwelt. Das hast du im Hello-World Beispiel gesehen, als das
Programm am Laufen geblieben ist nach Begrüßung eines Gastes für die
Begrüßung des nächsten usw.


---


<!-- Page 398 of 584 -->


08-DieIODAArchitektur 389
Aus dem UI{} fließt ein Strom von Namen; Name erfragen ist der
Sammler-Aspekt des Portals. Am anderen Ende des Datenflusses ist
Begrüßen die dazu passende schließende Klammer.
Die Application{} mit ihrer Funktionseinheit Run startet das das
UI{}, so dass anschließend das Programm eigentlich die ganze Zeit in
der Benutzerschnittstelle steht und wartet; nur, wenn dort eine Eingabe
gesammelt wurde, fließt mal etwas zur Verarbeitung heraus.
Dieses Interaktionsmuster herrscht bei Desktop-Anwendungen vor, in
denen die Anwendung gestartet wird und dann auf Benutzereingaben auf
der Konsole oder über eine graphische Benutzerschnittstelle lauscht.
Controller
Anders ist es in Web-Anwendungen. Dort wartet kein UI auf Benutzerein-
gaben. Das übernimmt vielmehr eine Infrastruktur, der Internetserver, der
den Anwendungscode hostet. Wenn der eine HTTP-Nachricht empfängt,
leitet er sie an den Anwendungscode weiter. Meist wird dort ein Control-
ler nur für die Verarbeitung dieser Nachricht instanziiert. Der muss sich
nicht mehr um TCP- oder HTTP-Feinheiten kümmern, sondern bekommt
dieNachrichtineinembesserverdaubaremFormat,vielleichtsogarschon
als simples Datenobjekt (POJO, POCO). Das ist so anders als auf dem
Desktop, dass ich diesen Interactor Controller nenne nach dem Muster,
wie es in Web-Anwendungen zum Einsatz kommt.


---


<!-- Page 399 of 584 -->


08-DieIODAArchitektur 390
Die drei Punkte unter main sollen andeuten, dass main nicht selbst
und direkt handle integriert, sondern das irgendwie in der Infrastruktur
passiert. main sorgt nur dafür, dass Controller registriert sind, um im
rechten Moment Reize aus der Umwelt zu verarbeiten.
Weil Controller nicht auf Input warten, sondern den “magisch” und
ganz im Einklang mit PoMO von irgendwoher und irgendwann geliefert
bekommen,habensieoftaucheinenOutput.SietransformierenInputvon
der Infrastruktur in Output für die Infrastruktur; die muss dann zusehen,
dass sie ihn an den richtigen Empfänger weiterleitet.
Die Rolle des Portals ist in diesem mehr auf Mapping und Validation
konzentriert. Dabei darf es auch noch zu Abhängigkeiten von der Infra-
struktur kommen, die den Controller hostet.
process hingegen weiß dann nichts mehr von einer Infrastruktur. Das
kann die Domäne sein oder… aber darauf komme ich gleich.
VorhernocheineinfacheresBeispielfüreinenController.AuchohneWeb-
oderMobile-EinsatzgibtesSzenarien,indenenderInteractoreinControl-
ler und keine Application ist. Das ist der Fall bei Konsolenanwendungen,
diekeineBenutzerschnittstellestarten,dieaufEingabenwartet.DasHello-
World Beispiel passt wieder; es muss nur die Eingabe des Namens auf
die Kommandozeile verlegt werden und bei jedem Programmlauf nur ein
Gast verarbeitet werden.


---


<!-- Page 400 of 584 -->


08-DieIODAArchitektur 391
Jetzt liest das UI{} den Namen aus der Kommandozeile; lediglich einmal
fließt also ein Name weiter zur Verarbeitung. Dass dann am Ende die
Begrüßung über die Konsole stattfindet, tut der Controller-Natur des
InteractorskeinenAbbruch.ErwirdfürdieIntegrationdesVerarbeitungs-
prozesses pro anliegende Daten instanziiert.²⁰³
Der Interactor als injection point
Indem Program{} und Interactors getrennt werden, gibt es einen klaren
Punkt für Injektionen von Laufzeitabhängigkeite (injection point): Kon-
struktion findet in main statt, dabei werden direkt oder indirekt über
RegistrierungenbeiDI-ContainernAbhängigkeiteninInteractorsinjiziert
- und so werden die besser testbar. Denn diese Abhängigkeiten - vor allem
die zu Portalen - können in Tests durch Surrogate ersetzt werden.
Indem du also bewusst eine Integrationsebene mit Interactors einziehst,
erhöhst du die Testbarkeit. Interactors können dann womöglich in un-
terschiedlichen Szenarien gehostet werden. Denn das tut Program{}
entweder direkt oder eine Infrastruktur, die dort gestartet wird indirekt.
²⁰³Ob der Controller bei on-demand Instanziierung tatsächlich nur integriert oder doch
auch konstruiert, sei dahingestellt. Inwiefern Konstruktion auch erst in Reaktion auf einen
Reizstattfindensollteodermuss,istauchvonderInfrastrukturabhängig,diedenController
hostet.


---


<!-- Page 401 of 584 -->


08-DieIODAArchitektur 392
Processors
Mit Interactors gibt es eine Verantwortlichkeitstrennung und es steigt die
Testbarkeit.Dasistwunderbar.DochdieInteractorsbleibenabhängigvon
Portalenl. Die in Tests zu ersetzen durch Surrogate mag umständlich sein.
Deshalb gibt es eine zweite kanonische Integration in dem Architektur-
muster, das ich dir hier vorstelle: die Processors.
Ein Processor integriert alles, was zwischen den Portalen passiert. Das
habe ich schon oben im allgemeinen Bild zu Controllers angedeutet mit
der Funktionseinheit process.
Der Processor integriert Domäne und Provider. Damit gibt es darin zwar
auchAbhängigkeitenzuHardware-RessourcenüberdieProvider,dochdie
sind oft weniger schwierig automatisiert zu testen als Portale oder sollten
sogar mit getestet werden im Sinne eines Integrationstests.²⁰⁴ Dabei darf
dann nur kein UI im Wege stehen. Aber das tut es ja auch nicht, weil es
schon auf der höheren Integrationsebene quasi ausgeblendet wird.
²⁰⁴Die Methoden des Processors sind nun endlich wirklich die Aufhänger der “Klei-
derbügelarchitektur”. Es sind nicht Domänenfunktionen, sondern integrierende. Denn die
KleiderbügelstehenfürmöglichstumfangreicheDatenflüsse,diedurcheineWurzelgetestet
werden können. Die Kleiderbügel “hängen an der Leine”, die zwischen Kollektor und
ProjektordesPortalsdurchdenInteractoraufgespanntwird.


---


<!-- Page 402 of 584 -->


08-DieIODAArchitektur 393
Die Modul-Hierarchie in der Architektur hat damit zwei Integrationebe-
nen:
Der Processor ist natürlich auch wieder ein injection point. Du kannst
dort mit Tests ansetzen und sicher sein, dass deine Portal-Technologien
dir nicht in die Suppe spucken. Aber du kannst auch noch, wenn du willst,
die Provider mit Surrogaten ausblenden.
Für mich ist der Processor daher der häufigste Ansatzpunkt für Akzep-
tanztests: Dort ist alles Visuelle ausgeblendet und andererseits so viel
wie möglich der eigentlichen Verarbeitung im Griff. Auf das Hello-World
Beispiel mit dem Application-Interaktor bezogen bedeutet das:


---


<!-- Page 403 of 584 -->


08-DieIODAArchitektur 394
Du siehst, wie process jetzt ganz natürlich den Datenfluss, der vom
Interactor integriert wird, vereinfacht; dort gibt es nur noch drei Schritte.
Im Grunde reduziert der Processor den Interactor auf EVA.²⁰⁵
IODA: All together now!
Damit sind alle Funktionsbereiche einer Softwarezelle versammelt. Sie
leistet ihre Arbeit mit…
• Domänenlogik
• Domänendaten
• Provider und
²⁰⁵Wenn ein Controller im Spiel ist, empfängt der Nachrichten aus der Umwelt. Die
eigentliche Nachrichtenverarbeitung findet jedoch im Processor statt. Deshalb nenne ich
den manchmal auf Message Handler und seine integrierende Funktionseinheit handle.
Lass dich also nicht verwirren, wenn es bei einem Controller-Einsatz mal zwei handle-
Funktionseinheiten gibt: einmal die des Controllers und einmal die des Processors. Beide
behandeln ja auch Nachrichten: der Controller nimmt sie recht roh entgegen und der
Processorbekommtsieschon“vorgewärmt”durchdasvorgeschaltetePortal.DerController
liegt auf einem höheren Abstraktionsniveau, weil er Nachrichten in spezifischer Form
verarbeitet; der Processor auf niedrigerem, weil er allgemeiner ist. Ihn interessiert nicht, ob
die Nachrichten über HTTP oder die Kommandozeile angeliefert wurden. Deshalb ist ein
InteractorabhängigvomProcessor.


---


<!-- Page 404 of 584 -->


08-DieIODAArchitektur 395
• Portal
Diese Funktionsbereiche kennen einander aber nicht. IOSP und PoMO
gelten auch auf Architekturebene strikt! Vielmehr gibt es darüber hinaus
explizit integrierende Funktionsbereiche auf zwei Ebenen:
• Interactor²⁰⁶
• Processor
DieIntegrationenkannstdudirals“Bindegewebe”zwischenden“eigentli-
chen” Funktionsbereichen einer Softwarezelle vorstellen. Damit wird das,
was sich nicht kennt, zusammengehalten.
Allerdings fehlt noch etwas zum großen Architekturmusterglück: die
(Domänen)Daten und die Umwelt sind bisher nicht im Bild erschienen.
Das will ich nun nachholen:
²⁰⁶Der Begriff interactor findet auch in der Clean Architecture Anwendung - aber in
anderer Weise. Ich habe lange nach einem Oberbegriff für Application und Controller
gesucht. Nichts wollte passen - und am Ende habe ich mich für Interactor entschieden.
Das war für mich insofern plausibel, als dass eben auf der Ebene die Interaktion mit den
BenutzerndurchIntegrationvonPortalundProcessorermöglichtwird.PerfektistderBegriff
nicht,aberfürmichimAugenblickgutgenug.


---


<!-- Page 405 of 584 -->


08-DieIODAArchitektur 396
Die IODA Architektur ist also nach ihren Ebenen benannt. Das Akronym
soll ausdrücken, dass sie auf dem IOSP basiert. Dazu werden allerdings
noch explizit die Daten gestellt und die Abhängigkeit zur Plattform als
Summe aller APIs, die von Operationen benutzt werden.
Wie in anderen Architekturmustern geht es hier auch um Funktionsbe-
reiche vertreten durch Module. Die bisher üblichen findest du in der
IODA Architektur wieder. Der Funktionsbereich presentation layer der
Schichtenarchitektur wird repräsentiert durch Portale. Die Adapter der
Hexagonalen Architektur werden vertreten durch Provider. Die äußere
Schalte der Clean Architecture ist zusammengefasst in den APIs. Und die
Domäne ist sogar differenzierter repräsentiert durch Domänenlogik und
Domänendaten als in anderen Architekturmustern.
Was die IODA Architektur nun aber fundamental unterscheidet, das ist
die Abwesenheit jeder Abhängigkeit zwischen den Funktionsbereichen.
Was Logik enthält, kennt einander nicht. Die üblichen Funktionsbereiche
bilden also keine Abstraktionshierarchie wie es in anderen Architektur-
mustern suggeriert wird. Sie sind auf Augenhöhe und komplementär. Sie
alle tragen ihren Teil zur Gesamtleistung bei. Doch das Gesamte wohnt
ihnen nicht selbst inne.
Das Ganze ist mehr als seine operationalen Teile. Zu ihm gehören auch
noch deren Verbindungen. Und dafür stehen die Integrationen. Die Tren-
nung der Integration von den operierenden Funktionsbereichen - ob nun
in eine oder zwei Ebenen oder gar mehr, ist egal - macht die IODA
Architektur so anders als bisherige Architekturmuster. Darin steckt die
Innovation: dass Komposition nicht den Funktionsbereichen überlassen
wird, sondern eine eigene Aufgabe ist. Komposition ist so wichtig, dass sie
nicht implizit stattfinden sollte über die Ausrichtung von Abhängigkeiten
durch Schichten oder Schalen; Komposition verdient eine eigene Reprä-
sentation orthogonal dazu. Die Verarbeitung fließt horizontal zwischen
den operierenden Funktionseinheiten; deren Komposition erfolgt vertikal.
Diese grundsätzliche Trennung ist aus meiner Sicht ein entscheidender
Ermöglicher von Flexibilität. Denn Komposition ist viel einfacher zu
ändern und zu ergänzen als Logik.
Die IODA ist die konsequente Erhebung von IOSP auf die Ebene der
Architektur.


---


<!-- Page 406 of 584 -->


08-DieIODAArchitektur 397
Übungsaufgaben
Reflexionsaufgabe
Bitte formuliere eine Frage oder eine Erkenntnis zum Kapiteltext.
• Wo bist du gedanklich hängengeblieben, was ist dir unklar,
was passt für dich irgendwie nicht zusammen, wozu würdest
du dir noch etwas mehr Erklärung wünschen? Steht irgendet-
waszudeinerbisherigenPraxisimWiderspruchunddufragst
dich, warum du etwas ändern solltest?
• Oder: Wann hast du einen Aha-Moment gehabt, was ist
diralsbemerkenswert,spannend,ausprobierenswertaufgefal-
len? Hat irgendetwas “in dir Klick gemacht”, weil dir nun ein
Zusammenhang aufgegangen ist? Oder verstehst du jetzt aus
deiner bisherigen Praxis irgendetwas besser?
Am besten formulierst du Frage bzw. Erkenntnis schriftlich. Indem
du deine Gedanken aufschreibst, wirst du dir ihrer bewusster. Bei
einer Frage kommst du dadurch vielleicht schon einer Antwort aus
dir selbst heraus näher. Bei einer Erkenntnis fällt dir vielleicht schon
etwas ein, das du ab jetzt anders machen kannst.
Aufgabe 1 - Umbau nach IODA
Blättere zurück zur Game-of-Life Musterlösung (oder zu deiner
eigenen) und baue das Modell um nach IODA. Ziehe also Interactor
und Processor Integrationen ein. Hier ein Rückblick zur Erinnerung:


---


<!-- Page 407 of 584 -->


08-DieIODAArchitektur 398
• Zeige IODA im Datenflussmodell
• Zeige IODA in einem Klassendiagramm
Ist der Interactor eine Application oder ein Controller?
Aufgabe 2 - Enturf nach IODA inkl. Imple-
mentation
Schreibe ein Programm, mit dem ein Anwender, der Spieler, Zahlen
raten kann. Pro Spiel nennt das Programm ihm einen Zahlenbereich
n..m,indemdiezuratendeZahlliegt.nwirdzufälligausdemBereich
1..50gewählt,mwirdzufälligausdemBereich10..100gewählt.Esgilt
je Spiel: n<=m-10.
Je Raterunde wird dem Spieler gesagt, ob er sich der Zahl nähert
(“wärmer”) oder sich von ihr entfernt (“kälter”) im Vergleich zur
vorhergehenden Raterunde. Außerdem weißt das Programm den
Spieler darauf hin, wenn er dieselbe Zahl nochmals eingibt.
1 $ zahlenraten
2 Rate eine Zahl zwischen 10 und 17...


---


<!-- Page 408 of 584 -->


08-DieIODAArchitektur 399
3 1. Versuch: 15
4 Nein.
5 2. Versuch: 16
6 Nein. Kälter.
7 3. Versuch: 14
8 Nein. Wärmer.
9 4. Versuch: 11
10 Nein. Wärmer.
11 5. Versuch: 15
12 Nein. Kälter. Die Zahl hattest du schon.
13 6. Versuch: 12
14 Ja! Herzlichen Glückwunsch!
15 $


---


<!-- Page 409 of 584 -->


09 - Finale im
Softwareuniversum
Entwurf ist die Kunst der konzeptionellen Lösung eines Programmier-
problems. Ihr Ausgangspunkt ist das Verständnis der Anforderungen, ihr
Zielpunkt ist das Modell einer Lösung.
Nur konzeptionell ist die Lösung des Entwurfs, weil sie noch nicht
lauffähig, noch nicht implementiert ist. Das Modell ist nicht die konkrete
Lösung, sondern nur die abstrakte, ein Plan und Rahmen für die konkrete.
Das Modell zu erfinden, halte ich für die zentrale und große kreative
Leistung in der Softwareentwicklung. Wie du es schaffst, eine Lösung zu
entwerfen, kann ich dir deshalb gar nicht genau vermitteln; es ist eben
ein kreativer Akt. Die Kapitel hier im Buch können dir deshalb leider nur
einenHandlaufbietenundeinenRahmenabstecken.Darankannstdudich
indeinerSituationentlangbewegen,darinkannstdudeinekonzeptionelle
Lösung aufspannen.
Habe ich dir dafür den besten Ansatz vorgestellt?
Für mich persönlich, ja. Es ist das mir derzeit beste Vorgehen. Ich selbst
habe davon sehr profitiert über die Jahre, da ich es entwickelt habe und
danach arbeite.
Absolut gesehen hingegen, nein. Sicher gibt es noch bessere Vorgehens-
weisen - nur leider kenne ich sie nicht.
Reflektierendes Zwischenspiel
Du solltest in Anschlag bringen, dass jedes Vorgehen in gewisser
Weisesubjektiv ist. Es ist eine Heuristik, die bei gegebenem Wissens-
undBewusstseinsstandeingenügendgutesErgebniserzielt.Ichhabe
meinen Background, du hast deinen. Auch wenn ich mich bemüht
habe, einen common ground zu definieren und darauf aufzubauen,
wirst du das, was mir total plausibel erscheint, womöglich weniger


---


<!-- Page 410 of 584 -->


09-FinaleimSoftwareuniversum 401
plausibel finden. Und das ist ok.
Ja, das möchte ich gerade in diesem Band betonen! Es ist ok, wenn
du anderer Meinung bist. Es ist sogar gut so, denn dann stellst du
womöglich mir eine Frage und dann kann ich entweder noch eine
bessere Begründung für eine Aussage finden - oder ich revidiere sie.
So entwickelt sich der Ansatz weiter.
Aber selbst wenn du mir keine Frage stellt und nur skeptisch die
Stirn runzelst bei der Lektüre, habe ich etwas Wichtiges erreicht.
Reflexion ist wichtiger als Konformität. Dieser Aspekt kommt mir
indenmeistenFach-undSachbüchernzukurz.IchwilldenAutoren
nichtunterstellen,dasssieandererAnsichtseien,docheskommtmir
zumindest so vor.
Egal also, was du liest - mein Buch oder eines von Robert C. Martin
oder Donald Knuth oder einem “Guru” der Softwareentwicklung -
, lies es mit Offenheit und Skepsis. Sei bereit für eine attraktive
Überraschung, aber behalte auch deine Distanz. Wenn du aus 300
Seiten nur 3 anregende Gedanken mitnimmst, ist das genug. Wenn
du nach 75 Seiten findest, das geht alles in die falsche Richtung und
du weißt nun umso mehr, warum du bei dem bleiben willst, was du
bis dahin getan hast, ist da auch ok. In beiden Fällen ist in dir etwas
passiert; du hast dich ein wenig verändert. Dass du dich der Lektüre
überhaupt ausgesetzt hast, ist das Wesentliche.
Damagstdueinwenden,dassmandochabernichtwirklich,wirklich
verstehen kann, wenn man nur 75 Seiten liest und auch fleißig
ausprobiert hat, was in einem Buch vermittelt wird. Das stimmt
wohl - doch ist ein Einwand auf der Basis einer Prämisse. Die lautet:
“Man muss alles wirklich, wirklich verstehen, um sich eine Meinung
zu bilden.” Dieser Prämisse folge ich jedoch nicht. Ich frage mich
vielmehr:Warum willichetwasüberhauptverstehen?Weilichmich
verändern will.
Wenn ich den Veränderungswillen jedoch als Prämisse setze, dann
ist alles ausreichend, was die Wahrscheinlichkeit erhöht, dass ich
mich verändere. Dazu reicht womöglich schon die Lektüre von nur
75 Seiten eines Fachbuches; ja, es reicht sogar die Lektüre eines
Aphorismus’ von wenigen Zeilen.
Daswirddirvielleichnochplausibler,wennicheinezweitePrämisse
dazu setze: Dass ich bei Lektüre eines Buches nur vordergründig


---


<!-- Page 411 of 584 -->


09-FinaleimSoftwareuniversum 402
eine bestimmte Veränderung in mir erzielen will; in Wirklichkeit
ist es mir egal, wie ich mich verändere. Ich kann also ein Fachbuch
lesen und meine Einstellungen zur Ehe verändern; ich kann genauso
einen Roman lesen und eine Einsicht in die Softwareentwicklung
gewinnen. Das Potenzial für Veränderung lauert überall. Sei bereit!
Und eine Veränderung hat in dir sogar stattgefunden, wenn du nach
75 ein Fachbuch beiseite legst mit der Meinung “Abwegig!” oder
“Nichts Neues unter der Sonne!”. Zwar machst du danach äußerlich
unverändert weiter in deiner Praxis - doch innerlich bist du weiter.
Duweißtjetztnämlichbesser,warumduderbisherigenPraxisfolgst.
Du hast mehr Gewissheit. Das ist nicht zu verachten.
Als Autor fällt mir das etwas schwer zu schreiben. Natürlich möchte
ich 5-Sterne Reviews meiner Schreibmühe; selbstverständlich möch-
te ich, dass du mein Buch zuende liest und “Wie geil!” ausrufst.
Doch ich will und muss realistisch sein. Dass ich das erreiche, ist
unwahrscheinlich angesichts der Menge an Büchern, die um deine
Aufmerksamkeit buhlen. Ich habe ja auch genügend Erfahrung mit
mir selbst als Leser. Wie oft habe ich das Ergebnis von viel Herzblut
eines anderen Autors nach nur einem Drittel weggelegt. Ja, 25-30%
sindofteineSchwellebeiderLektüreeinesBuches:Wennichsoweit
komme,dannwaretwasdrinfürmich,aberich“darf”esauchguten
Gewissensweglegen.Halteichlängerdurch,dannisteseinwirklich
gutes Buch. Doch deshalb muss ich es trotzdem nicht zuende lesen.
Ein nächster “Abrisspunkt” sind 66-75%. Oft denke ich, bis dahin
ist das Wichtigste gesagt; der Autor hätte auch einfach aufhören
können.
Ist das arrogant? Nein. Ich maße mir ja keine Objektivität an. Mein
Urteil ist ganz subjektiv. Für mich reicht es einfach. Ich habe dann
genug aus einem Buch gezogen. Auf zum nächsten! Es hat einfach
genügend Veränderung in mir für den Moment stattgefunden.
Für den Moment ist mir dabei ganz wichtig! Dieses Verständnis
möchte ich dir auch mitgeben. Wenn du z.B. nur die ersten 123
Seiten in diesem Buch gelesen haben solltest und dann hierhin
zum Schlusskapitel gesprungem bist, weil du dir einen Überblick
verschaffenwillst,gelangweiltwarstoderschlichtimmernurerstmal
kursorisch liest, dann ist es doch völlig ok, wenn du gleich aufhörst.
Es war genug für dich für den Moment - und irgendwann später
knüpft du vielleicht daran an. Auf die eine oder andere Weise.


---


<!-- Page 412 of 584 -->


09-FinaleimSoftwareuniversum 403
Ich bin ein großer Freund des Mottos
Ist der Schüler bereit, kommt der Lehrer.
Nicht für jede Veränderung ist die Zeit gekommen, wenn du es
meinst. Nur weil du mal zu diesem Buch gegriffen hast, weil du
denkst, du könntest doch mal etwas an deinem Kenntnisstand und
deinen Gewohnheiten beim Softwareentwurf verändern, heißt das
nicht, dass du dafür schon wirklich, wirklich bereit bist. Das mag
frustrierend sein; vielleicht denkst du, dass man dann doch aber
keine Kontrolle über seinen Fortschritt hätte, wenn man immer
auf Bereitschaft warten müsste und sich nicht willentlich zu einem
bestimmten Zeitpunkt verändern könnte. So einen Reflex würde ich
verstehen-dochfürmichpersönlichundsubjektivhatsichüberviele
Jahre herauskristallisiert, dass weniger Kontrolle und mehr Geduld
keine so schlechte Sache sind.
DasErgebnisistfürmicheinmehr“experimenteller”Lebensstil.Wie
ein Venture Capital Geber mache ich viele, sehr viele Experimente.
Jedes Buch, das ich lese, ist eines. Jedes Mal, wenn ich ein Buch zu
schreiben anfange, ist es eines. So habe ich zum Beispiel je nach
Zählung 3-6 Mal angefangen, Flow-Design so wie hier zusammen-
zufassen - und es hat nicht geklappt. Meine Diagnose: Ich war noch
nichtbereit.DeshalbwardierichtigeReaktionfürmichderAbbruch
dieser Experimente und weiter zu warten und es dann nochmal
anders zu probieren.
Geradlinigkeit steht hoch im Kurs. Sogar ich möchte dir ja mit
meinem Ansatz Programming with Ease zu mehr Geradlinigkeit
verhelfen. Doch letztlich bleibt das Leben und Lernen wohl ein
Mäandrieren, glaube ich. Zuviel Effizienzwille ist gar nicht gut.
“Umwege erhöhen die Ortskenntnis”, sagt man. Genau! Und das gilt
eben auch fürs Lernen, für die Veränderung.
Hoppla, jetz bin ich aber ins Plaudern gekommen. Das war nicht
meine Absicht, als ich die rhethorische Frage “Habe ich dir dafür
den besten Ansatz vorgestellt?” gestellt hatte. Aber so kann es gehen.
Wieder eine Schleife im Strom der fließenden Gedanken.
Also:Allesgut,wenndu(noch)keinFanvonFlow-Designgeworden
sein solltest. In dem Fall danke für deine Offenheit, es zu versuchen
unddemAnsatzeineChancezugeben.Aberwennduzumindestein


---


<!-- Page 413 of 584 -->


09-FinaleimSoftwareuniversum 404
paar schöne Aha-Momente gehabt haben solltest, freue ich mich na-
türlich doppelt. In beiden Fällen schreibe mir gern an info@ralfw.de.
Jetzt zurück zur Methode… Hier am Ende des Buches wollte ich ja
eine kleine Zusammenschau veranstalten.
Demkönnteichentgegenhalten:KanneinAutordennin300oderauch
1500 Seiten wirklich, wirklich vermitteln, was er denkt? Oder besser: Was
er denkt, glaubt, tut. Nein, das geht nicht. Das merke ich beim Schreiben
meinerArtikelundBücher;darausschließeich,dassesauchanderenAutoren
wohl so gehen wird. Bücher sind nur Ausschnitte dessen, was den Autor
mit all seinem Wissen/Können ausmacht. Bücher sind nur Momentaufnah-
men seiner Kompetenz. Das ist für mich der Grund, warum es so viele
Missverständnisse und Konflikte in unserer Branche gibt. Wir nehmen zu
schnell an, nach vollständiger Lektüre eines Fachbuches auch wirklich alles
erfahren zu haben, was es zum Thema zu sagen gibt - was der Autor weiß.
Doch das ist nicht so. Deshalb betreiben wir immer wieder Cargo Cult. “We
are going through the motions” - und dennoch bleibt das erhoffte Ergebnis
aus. Warum? Hat der Autor es uns nicht genau so vorgemacht? Nein, der
Autor weiß ja nichts über deine Situation; wäre er in selbst in ihr, hätte
er womöglich einen anderen Weg eingeschlagen. Womöglich wäre er sogar
selbst von dem abgewichen, was du in seinem Buch gelesen hast. Oder er
hätte es anders ausgelegt, anders in Zusammenhang mit anderem gesetzt,
was woanders von ihm geschrieben steht. Die Wahrscheinlichkeit, dass du
einenAutormissverstehst,istgroß.Deshalbist“wirklich,wirklichverstehen”
ebenauchnichtselbstverständlichnach300SeitenLektüre.Autorensindauch
nurMenschen und begrenztin ihrerFähigkeitzukommunizieren,was sie in
Gänzesind.WenndualsobeimeinenDarstellungendieStirnrunzelst,istdas
nur verständlich. Würden wir uns darüber unterhalten, würde ich vielleicht
sagen, “Oh, da hast du mich missverstanden” oder besser “Oh, da habe ich
michmissverständlichausgedrückt”oderwomöglichsogar“Hm,sohabeich
das noch nicht gesehen; darüber muss ich mal nachdenken. Vielleicht sollte
ichmeinenAnsatznachbessern?”
Ich versuche bei der Lektüre von Büchern der sunk cost fallacy auszu-
weichen. Wenn ich nach 25%, 50% oder 75% meine, dass ich für den Moment
genug aus einem Buch gezogen habe, dann lege ich es beiseite, ohne mich
zu schelten. Nur, weil ich das Geld ausgegeben habe und so weit gekommen
bin, muss ich nicht weiterlesen. Zur bisherigen Zeit muss ich keine weitere
investieren, wenn mir das im Moment nicht wertvoll erscheint. Vielleicht
lese ich später weiter, vielleicht auch nicht. Meine Metrik ist nicht “gelesene
Seiten”,sondern“empfundenerNutzenimVergleichzuanderenOptionen”.
Dass dieses Zwischenspiel nicht zur Methode gehört, stimmt natürlich
nicht. Ich will dir in Wirklichkeit nicht nur Flow-Design näherbringen,
sonderndichaufvielenEbenen“inFlussbringen”.FürmichistFlow-Design,
d.h. eine flow-first Sichtweise auf die Softwareentwicklung eine Frage der
Kongruenz. Nur wenn ich selbst “mich flüssig halte”, kann ich auch flüssig
in meiner Arbeit mit Datenflüssen sein. Und umgekehrt mag die Methode,
die ich vertrete ein Ergebnis meines persönlichen Strebens nach Flüssigkeit


---


<!-- Page 414 of 584 -->


09-FinaleimSoftwareuniversum 405
sein. Co-Evolution von Mensch und Methode. Wo hat das seinen Anfang
genommen? Ich weiß es nicht. Doch ich glaube fest daran, dass es bei dir
auch so ist. Auch bei dir findet Co-Evolution statt - und insofern trage ich
mitallemdazubei,wasundwieichschreibe.
Der Explizite Entwurf ist nötig
Habe ich dir den besten Ansatz für den Entwurf vorgestellt? Wenn er dir
am Ende etwas einfacher macht, dann ist er zumindest gut genug für den
Moment und für dich. Das finde ich wesentlich. Wovon würde ich mir da
am meisten Nutzen für dich versprechen?
Wenn du nur eines mitnimmst nach all der Mühe der Lektüre, dann
wünsche ich mir, dass du mitnimmst: Expliziter Entwurf ist so hilfreich,
dasseralsnötig,unumgänglich,geradezualternativlosangesehenwerden
muss.
Ob du mit Flow-Design entwirfst und allem hier Gesagten bis zum letzten
“Sternchen außerhalb der Klammer” folgst oder standard UML-Notation
benutzt,istletztlichegal.DassdudirjedochausdrücklichZeitnimmst,um
vorderCodierungdeineLösungkonzeptionellzuentwickeln,dasfindeich
ganz und gar nicht egal.
Lass dich nicht vom Sirenengesang des Codes in die IDE ziehen! Binde
dichwieOdysseusaneinemMastfestundgenieße,ohneanDetailklippen
zu zerschellen. Setze deinen Code nicht aufs Spiel durch premature
coding.ProduktionscodeisteinempfindlichesWesen;dassolltestdunicht
überanspruchen.Solangedunichtgenauweißt,waszutunist,tueesnicht
am Produktionscode. Halte dich zurück!
Ich weiß, das ist manchmal sehr schwer. Dir kribbelt es in den Fingern,
einegrobeLösungsideeschnellmalauszuprobieren-amProduktionscode.
Geh’ dann am besten eine runde um den Block; kühle dich ab. Oder trink
mit Kollegen einen Kaffee. Oder schreib’ einen Prototypen oder Spike.
Ja, manchmal hilft es zu codieren, um einer Lösung auf die Spur zu
kommen. Vielleicht hängt deine Lösung von deiner Kenntnis eines API


---


<!-- Page 415 of 584 -->


09-FinaleimSoftwareuniversum 406
ab; solange du da noch unsicher bist, bist du gedanklich blockiert. Dann
verbessere deine Kenntnis des API; probiere ihn auch schon im Hinblick
aufdasanliegendeProblemaus.Wunderbar!Nurtu’dasnichtamProduk-
tionscode.
Wenn du schließlich sicherer und/oder ruhiger geworden bist durch
risikolose Codierung, dann tritt zurück und entwerfe: Nimm ein Blatt
Papier oder dein iPad oder deinen reMarkable zur Hand und visualisiere
dein Lösungskonzept. Du bist dann schon informiert durch Code und es
fällt dir leichter, “nur” zu “malen”. Wunderbar! Wenn dir “Abreaktion von
Codierungsdrang” hilft, dann wirf die IDE an, um erstmal ein Gefühl für
einen Lösungsansatz zu bekommen. Das ist dann dein Weg in einer be-
stimmtenSituation.Nurbring’dabeidenProduktionscodenichtinGefahr.
Und überspringe anschließend den Schritt eines visuellen Entwurfs nicht.
Falle nicht dem overconfidence effect²⁰⁷ zum Opfer!
Der explizite Entwurf entschleunigt und bietet dir wertvolle Gelegenheit
zur Reflexion. Ganz zu schweigen davon, dass ein expliziter visueller
EntwurfdasWerkzeugist,umeingemeinsamesmentalesModellvonSoft-
ware in einem Team aufzubauen. Wenn du im Team Software entwickelst,
ist eine gemeinsame explizite Phase zur konzeptionellen Lösungsfindung
noch umso wichtiger. Ideen “mit Händen und Füßen” vermitteln, gar
entwickeln zu wollen, wie es oft geschieht, ist zu ausdrucksarm und zu
flüchtig.
Der Entwurf ist deklarativ
Explizit und visuell sollte also der Entwurf sein. Aber nicht jede Visuali-
sierung ist auch eine wirklich gute. Wenn du Pseudocode ans Whiteboard
schreibst, machst du ja auch etwas sichtbar, was vorher nur in deinem
Kopf war. Das meine ich mit Visualisierung allerdings nicht.
Weniger Worte, mehr graphische Elemente: darum geht es bei der Visua-
lisierung. “Boxes and lines” geht in die richtige Richtung. Doch auch das
ist noch zu wenig bzw. zu unspezifisch.
Alles, was nach Code aussieht - also auch Pseudocode -, hat im Entwurf
nichts zu suchen. Dann bringt der Entwurf schlicht nichts. Er wird zu
²⁰⁷https://en.wikipedia.org/wiki/Overconfidence_effect


---


<!-- Page 416 of 584 -->


09-FinaleimSoftwareuniversum 407
detailliert und damit zu langsam und zu umfangreich. In der kreativen
Phase der Lösungsentwicklung sollst du möglichst unbeschwert sein. Lass
dich nicht von Feinheiten einer Programmierplattform herunterziehen.
NatürlichdarfdeinEntwurfamEndenichtabgehobensein;Realitätsnähe,
Umsetzbarkeit: die sind wichtig für Entwürfe. Gleichzeitig leben sie von
einer gewissen “Entrücktheit”. Sie sind “nur” Pläne oder Karten, nicht das
Terrain.
Also hilft dir ein Entwurf nur, wenn er von der späteren Coderealität abs-
trahiert. Das tut er umso mehr, je stärker er sich auf das Was konzentriert,
denn das Wie. Logik ist das pure Wie. Ein Entwurf hingegen beschreibt
“nur”, was getan werden muss. Deshalb nenne ich den Entwurf auch eine
deklarative Lösung.
ZusammenhängesinddieSachedesEntwurfs.Dass etwasbedachtistbzw.
geschieht, ist wichtiger, als wann. Kontrollflüsse passen für mich deshalb
nicht zum Entwurf.
Ein Strukturdiagramm mit Modulen ist insofern ganz typisch für den
Entwurf. Nicht umsonst hat es gerade ein UML-Diagramm in alle (OO-
)Entwicklerköpfe geschafft: das Klassendiagramm. Wie die Module im
Diagramm zusammenhängen sollten, lasse ich hier einmal dahingestellt;
sie aber überhaupt im Entwurf zu nennen und in Zusammenhang zu
bringen, das ist zentral.
Zu wissen, dass es Funktionsbereiche gibt, und wie sie zusammenhängen,
ist allerdings nicht genug. Überhaupt stellt sich die Frage, woher der
Zusammenhang kommt. Nur, weil du entschieden hast, dass es eine
Benutzerschnittstelle und eine Domäne und Persistenz gibt, ist doch
deshalb nicht klar, dass z.B. die Benutzerschnittstelle mit der Domäne
zusammenhängt und nicht mit der Persistenz.
Die Zusammenhänge zwischen Funktionsbereichen ist vielmehr eine Fol-
ge von Kooperation. Und Kooperation ist eine Frage des Prozesses. Der
Entwurf muss also auch eine Idee vom Prozess entwickeln, in dem
Ergebnisse für die Anwendenden hergestellt werden. Wie kannst du das
in deklarativer Weise tun?
Wenn ich das Charakteristium für eine deklarative Prozessbeschreibung
aufeinWortreduzierensollte,dannwürdeichsagen:Schleifenfreiheit.No
loops! macht einen deklarativen Prozess aus.


---


<!-- Page 417 of 584 -->


09-FinaleimSoftwareuniversum 408
SchleifensindImplementationsdetails.SchleifensindFeinheitendesCodes.
Sie sind Kennzeichen eines Kontrollflusses. Sie machen Code schwer
verständlich,weilsiedenflüssigenAufbauvonVerständniszurückwerfen
und belasten. Sobald du dir Gedanken über Schleifen machen musst, bist
du beim Wie. Das, was in einer Schleife geschieht, tritt zurück hinter dem,
wie es geschieht.
Der deklarative Entwurf eines Prozesses verträgt Alternativen, aber er
verträgt keine Schleifen!
Ob du dann für den schleifenfreien Prozessentwurf kanonisches UML
benutzt, ob du das IOSP dabei einhältst… das überlasse ich dir. Ich habe
dir ausführliche meine Vorstellung einer leichtgewichtigen Notation auf-
bauend auf begründeten Prinzipien vorgestellt. Doch das ist im Speziellen
nicht so wichtig wie ein deklarativer Entwurf im Allgemeinen, egal, wie
du ihn betreibst.
Ohne Deklarativität fehlt deinem Entwurf einfach die nötige Abstraktion.
Er wird geerdet. Er will schon zu sehr den Code vorwegnehmen. Wenn
Programmierung davon profitiert, dass du auf goto verzichtest, indem du
nurnochdieMittelderStrukturiertenProgrammierungverwendest,dann
profitiert die Programmierung auch davon, dass du dich ein weiteres Mal
beschränkst: Verzichte auf die Flexibilität der Sprache, verzichte auf den
Gebraucht von Schleifen in der Verhaltensbeschreibung.²⁰⁸
Das Modell beschreibt Funktionen in
Beziehungen
Der Entwurf löst Probleme im Großen, die Codierung löst Probleme im
Kleinen: sozusagen Makro- vs Mikro-Problemlösung. Im Entwurf ist die
Lösung deklarativ und nicht lauffähig, im Code ist sie imperativ und
lauffähig.
Die Codierung leistet dabei zweierlei:
²⁰⁸DamitmeineichnichtnurineinerProzessdarstellungzurückweisendePfeile,sondern
alle Visualisierungen, die zum Verständnis die Kenntnis einer Schleife voraussetzen. Das
betrifftalsoauchdarklogicSchleifeninIntegrationen,dieimEinzelfallgarnichtsoschlimm
scheinen.


---


<!-- Page 418 of 584 -->


09-FinaleimSoftwareuniversum 409
• Codierung übersetzt das deklarative Gerüst des Entwurfs in Code-
Konstrukte.GraphischeElementedesModellswerdenzutextuellen
im Code. Das ist ein 1:1 Mapping. Soweit der einfache Teil der
Codierung.
• CodierungerfindetdarüberhinausaberauchnochdieLogik.Dasist
ebenfalls ein kreativer Akt, der nicht zu unterschätzen ist. Deshalb
ist es so wichtig, die Produktionscode-Logik test-first zu stützen.
Diese Logik braucht Container, in die sie “eingefüllt” werden kann. Ohne
Container keine gezielte Adressierung. Diese Container sind Funktionen.
Wenn also die Codierung die Logik erst erfindet, dann ist es die Aufgabe
der vorhergehenden Entwicklungsphasen, die Container für die Logik zu
definieren. Das macht auch die Deklarativität des Entwurfs aus, dass er
sich nur um Funktionen kümmert. Er beschreibt nur, welche es gibt, nicht,
wie die ihre Aufgabe erfüllen.
Wie in Kapitel 1 beschrieben, liefert die Anforderungsanalyse eine erste
sehr grobe Liste an Funktionen: Das sind die Methoden der IODA Proces-
sors; dort setzen Akzeptanztests an. Diese Funktionen sind zunächst quasi
unzusammenhängend. Jede stellt ein Inkrement aus Sicht des Anwenders
dar. Du könntest sie einfach eine nach der anderen umsetzen und dein
Programm würde für den Anwender nützlicher und nützlicher.
Diese Funktionen sind allerdings in der Realität und auch in den meisten
Beispielen hier im Buch viel zu groß, als dass dir die Logik dafür einfach
so einfallen würde. Du musst dich an sie herantasten. Das tust du im
Entwurf, indem du darin das Problem, das die initiale Funktion aus der
Analyse darstellt, konzeptionell löst. Ziel ist es, eine Liste von feineren
Funktionen zu erarbeiten, deren Aufgabe so klein ist, dass du ihre Logik
testgestützt (hoffentlich) einfach entwickeln kannst; oder vielleicht sind
die Funktionen sogar trivial und du schreibst die Logik sofort hin.²⁰⁹
“Auseinsmach’viele”istdas,wasderEntwurfleistet.Eristeinanalytisch-
synthetischer Prozess: Du zerlegst Probleme, du setzt Lösungen zusam-
men. Die primären Mittel sind dafür Funktionen, also erstmal nur Wün-
sche, dass gewisse Effekte hergestellt werden mögen.
²⁰⁹Mit“einfach”und“trivial”bezieheichmichaufeineKategorisierung,dieichimBand
Test-firstCodierung einführe.Probleme,zudenendieseBezeichnungenpassen,entsprechen
gewissenKriterien.


---


<!-- Page 419 of 584 -->


09-FinaleimSoftwareuniversum 410
Aber diese Funktionen müssen natürlich in Zusammenhänge gebracht
werden: die Prozesse. Die zentralen Beziehungen zwischen Funktionen,
die im Modell definiert sein müssen, sind daraus folgend diese:
• Welche Funktion bekommt von welcher anderen ihren Input?
• Welche Funktion stellt welche Funktion mit welcher anderen in das
Input-Output-Verhältnis?
Und “nur” aufgrund einer wachsenden Zahl von Funktionen gibt es noch
eine weitere Beziehung:
• Welche Funktion steht mit welcher anderen in einem engeren
inhaltlichen Zusammenhang?²¹⁰
Datenflüsse und Module hast du im Flow-Design als die konkreteren
Repräsentationen dieser Beziehungen kennengelernt.
Die Prinzipien IOSP und PoMO wirken auf die Beziehungen modulierend
ein. Modelle bestehend aus Funktionen und Beziehungen kann es auch
ohne diese Prinzipien geben. Mit diesen Prinzipien jedoch sehen die
Modelle anders aus.
Wenn du dann für jede initiale Funktion der Anforderungsanalyse viele
Funktionen in solchen Beziehungen er-/gefunden hast - gerne auch mit
zugehörigen Testfällen für eine test-first Codierung -, dann ist dein
expliziter Entwurf abgeschlossen. Der Codierung liegt mit dem Modell
ein Plan vor, der umgesetzt werden kann.
Dafür ist ein anderes Mindset nötig. Wer codiert ist in einem anderen
Bewusstseinszustand als wer entwirft. Deshalb ist die Trennung beider
Phasensowichtig.DieEffizienzundEffektivitätwirderhöhtdurchsolche
“Arbeitsteilung” (auch wenn du selbst in beiden Phasen tätig bist).
²¹⁰Zwischen diesen Funktionen ist die Kopplung höher: Sollte sich an einer etwas
verändern müssen, ist die Wahrscheinlichkeit hoch, dass sich auch einer anderen etwas
verändern muss. Sie teilen sozusagen Gründe für Veränderungen. Das ist der Fall, wenn sie
derselben Verantwortlichkeit angehören, d.h. zur Umsetzung derselben Entscheidung von
KundeoderEntwicklerinbeitragen.


---


<!-- Page 420 of 584 -->


09-FinaleimSoftwareuniversum 411
Flow-Design im 4-dimensionalen Raum
Das Modell liefert Funktionen als Container für Logik - und natürlich
Datenstrukturen. Für mich haben die Funktionen in Prozessen dabei
Vorrang. Ziel ist die Logik, doch ohne zerlegte Probleme repräsentiert
durch feingranulare Funktionen, kommst du nicht auf die Logik.
Softwareentwicklung dreht sich mithin vor allem um Komposition: Kom-
plementäre Logik in Operationen zusammenfassen; komplementäre Ope-
rationen - und Integrationen - in Integrationen zusammenfassen. Und
auch komplementäre Daten zu Datenstrukturen zusammenfassen.
Die Kompositionsdimension ist deshalb die für mich hauptsächliche im
Softwareuniversum, das ich schon ganz am Anfang einmal angerissen
habe.


---


<!-- Page 421 of 584 -->


09-FinaleimSoftwareuniversum 412
Zwei Fragen stellen sich angesichts dessen unmittelbar. Ich weiß gar
nicht genau, welche davon die erste ist. Letztlich ist das auch egal. Ich
beginne mal mit dieser: Woher kommt der Anlass, überhaupt auch nur
eine Funktion zu implementieren?
Die Antwort darauf ist: Anforderungsanalyse. Die Kompositionsdimen-
sion wird gespeist aus einer Analysedimension. In der geht es darum,
Wert zu schaffen durch Lieferung von Nützlichem. Das Nützliche ist
Logik. Logik steckt in Funktionen. Und damit zügig Wertegeschaffen bzw.
Feedback zu Logik gegeben werden kann, ist es wichtig, Anforderungen
in feine Scheiben zu schneiden. Die Aufgabe des Auftraggebers ist die
Definition dieser feinen Scheiben, deine ist die Umsetzung in Code. Die
SchnittstellezwischeneuchfürjedesdieserInkrementeist…eineFunktion.
Der Auftraggeber versieht sie mit Bedeutung für sich, du füllst sie direkt
oder indirekt mit Logik.
InderzweitenDimensiondesSoftwareuniversumsgehtesalsodarum,aus
den ursprünglichen gesamten umfänglichen Anforderungen solche her-
auszuschneiden, die sich dir gegenüber als Funktionen darstellen lassen.
Diesen Prozess nenne ich Slicing und auch er folgt einer Zerlegungshier-
archie: Die strebt von etwas Nebulösem ausgehend einer Funktion zu, die
eine Interaktion repräsentiert - und diese Funktion verfeinerst du dann
weiter im Entwurf zu einem hierarchischen Prozess.²¹¹
²¹¹MehrdazuimBandSoftwareAnforderungsanalysemitSlicing.


---


<!-- Page 422 of 584 -->


09-FinaleimSoftwareuniversum 413
Aus Slices folgen Datenflüsse. Das kannst du dir als eine riesige Pyrami-
de vorstellen. Riesig, wirklich riesig! An ihrem Fuß gibt es womöglich
Zehntausende Operationen. Das kann ich hier nicht darstellen. Aber ich
versuche es mal mit einem Ausschnitt:


---


<!-- Page 423 of 584 -->


09-FinaleimSoftwareuniversum 414
Die Pyramide wächst nicht gleichmäßig. Elternknoten im Zerlegungs-
baum der Slices und Integrationen haben nicht immer dieselbe Zahl von
Kindknoten. Ein System mag zerfallen in zwei Bounded Contexts, aber
ein Co-Worker Team mag nur aus einer Partition bestehen und die aus 10
Dialogen,manchedavonmitnureinerInteraktionen,anderemitachtoder
15. Und immer so weiter in die Tiefe des Baumes bis zu den Operationen
als seine Blätter.
Dir wird klar: Da kommt was zusammen. Aus einer großen Vision für
eine Software werden viele Processor-Funktionen als Wurzeln für die
Datenflüsse, die wiederum aus vielen Funktionen bestehen. Diese Menge
will bewältigt werden. Da willst du den Überblick behalten; außerdem
willst du Testbarkeit herstellen und “Verklumpungen” vermeiden. Des-
halb braucht das Softwareuniversum eine weitere Dimension, eine für
die Ordnung, die in der Entkopplung besteht. Das leisten Module als
Aggregationen für Funktionen:
Auch die benötigen eine Hierarchie - eine physische wie eine darauf
aufbauend eine logische -, um der Funktionsflut Herr zu werden. “Soft-
waremaschinen” haben nicht nur Dutzende oder Hunderte Bauteile, son-
dern Tausende, Zehntausende, gar Hunderttausende. Automotoren mit
viel weniger Teilen werden von viel größeren Teams entwickelt. Indus-
triefabriken mit vielleicht genauso vielen Teilen, werden mit noch grö-
ßeren Teams entwickelt. Die Verantwortung und kognitive Last, die auf


---


<!-- Page 424 of 584 -->


09-FinaleimSoftwareuniversum 415
Entwickelnden liegt, ist also enorm. Kleine Teams von 3 oder 7 Personen
müssen entwerfen, implementieren und über Jahre weiterentwickeln, was
woanders viel mehr Personal bekommen würde und viel statischer ist.
Es ist nicht verwunderlich, dass unsere Branche deshalb immer noch am
Lernen ist, wie das am besten zu bewerkstelligen ist.
Soweit die Dimensionen, die für die langfristig hohe Produktivität im
Hinblick auf funktionale Anforderungen nötig sind.²¹²
Damit kommst du schon sehr weit - doch die höheren Weihen der
Softwareentwicklung wirst du damit nicht erlangen. Die sind denjenigen
vorbehalten, die auch hohe Ansprüche des Kunden an nicht-funktionale
Anforderungen erfüllen; insbesondere seien hier die Spitzenperformance,
die Skalierbarkeit und neuerdings auch die Wandlungsfähigkeit zur Lauf-
zeit genannt.
Diese Anforderungen lassen sich nicht mit monolithischer Logik lösen,
sondern bedürfen der Verteilung. Logik muss auf verschiedenen Threads
und sogar “weiter entfernt” parallel laufen. Das will geplant sein. Dafür
braucht es eine weitere Container-Hierarchie orthogonal zu den bisheri-
gen. Die Verteilung von Software zu entwerfen halte ich sogar für eine
sehr spezifische Disziplin innerhalb der Softwareentwicklung, die eigene
Fähigkeiten, Methoden und Werkzeuge braucht.
Die Host-Dimension kann ich hier nur anreißen. Wichtig ist mir, dir
mitzugeben, dass es sie gibt und das dort erhebliche Probleme ganz
eigener Art auf dich warten. Zu jeder Ebene der Host-Hierarchie kannst
²¹²WieimerstenKapitelerklärt,befriedigtLogikaucheinigenicht-funktionaleAnforde-
rungen, die in den drei Dimensionen deshalb mitgedacht werden. Nur der Einfachheit der
Formulierunghalberkonzentiereichmichaufdiefunktionalen.


---


<!-- Page 425 of 584 -->


09-FinaleimSoftwareuniversum 416
du viele Bücher zu Konzepten und noch mehr zu Technologien und
Produkten studieren. Mehr als bei den anderen Dimensionen bildet die
Host-Dimension ein Reich der Hypes und Moden. Vergleichbar ist es
nur mit dem Reich der Benutzerschittstellentechnologien, das sich um
die Dialog- und Interaction-Slices entfaltet. Gerade bei den Hosts steckt
einfach viel Potenzial, für den Auftraggeber kurzfristig Wert zu schaffen
- und Geld mit Technologien und/oder Beratung zu verdienen. Wer ist
demgegenüberschonanNachhaltigkeitinteressiert,fürdiedieDatenfluss-
und Modul-Dimensionen stehen? Insofern: Schön, dass zumindest du hier
bist!
Orientierungshilfe für die Softwareentwicklung
Und was bedeutet das alles? Warum habe ich dir das Softwareuniversum
hier nochmal entfaltet? Auch wenn es so ausführlich erst hier am Ende
steht und erst im zweiten Band der Programming with Ease-Reihe, ist es
mir ganz wichtig. Es stellt für mich das big picture der Softwareentwick-
lung dar, in das ich alles einordnen kann.


---


<!-- Page 426 of 584 -->


09-FinaleimSoftwareuniversum 417
Ich kann die Geschichte der Softwareentwicklung darin nachzeichnen;
ich kann darin Trends verorten; ich kann Lücken erkennen; ich kann
beschreiben, womit wir uns hier beschäftigt haben.
Das Softwareuniversum sollte eigentlich - sage ich mal etwas unbeschei-
den - am Anfang der Ausbildung zur Softwareentwicklerin stehen. Da
wäre es der Auszubildenden natürlich sehr abstrakt; über die Zeit jedoch
würde es sich ihr erschließen. Das Softwareuniversum ist insofern auch
eine Landkarte: Wo stehe ich? Wo will ich hin? Wo gibt es Sehenswür-
digkeiten? Wo lauern Schwierigkeiten? Welchen Weg will ich durch das
nehmen? Was gibt es alles zu lernen? Diese und mehr Fragen lassen sich
damit leicht(er) beantworten.
MeinEindruckist,dassdieSoftwareentwicklunganzweierleileidet:anzu
wenig Überblick und gleichzeitig an zu wenig Differenzierung. Es wird
viel in einzelnen Ecken herumgebastelt - und der Rest ignoriert. Dann
glaubt man, in einer Ecke den heiligen Gral gefunden zu haben - aber das,
worum es beim Rest geht, leidet womöglich darunter.
Das soll nicht bedeuten, dass jeder alles ständig im Blick haben muss.


---


<!-- Page 427 of 584 -->


09-FinaleimSoftwareuniversum 418
Aber es wäre wohl gut, sich seines Ausschnitts bewusst(er) zu sein. Das
Softwareuniversum erlaubt es dir, heraus und hinein zu zoomen. Beim
Fokuswechsel ist dir das Ganze dann immer wieder bewusst; du verlierst
nicht den Kontakt zum Ganzen.
Unausgesetzter Fokus leistet Tunnelblick und Silodenken Vorschub. Ich
denke, es steht jedem Entwickler gut an, den Überblick zu behalten. Nur
so fällt auch die Nachhaltigkeit nicht durch die Ritzen. In den Medien
herrschen Vorgehen und nicht-funktionale Anforderungen vor. Die Stich-
worte sind Agilität und Architektur. Und dann geht es noch um Logik, im-
merwiederumLogik:Nämlichimmerdann,wenneseineneueBibliothek
zu entdecken gibt. “Jetzt noch einfacher verschlüsseln!”, “Endlich leichter
3D-Grafiken darstellen!”, “Programmiere deinen eigenen Chat-Bot!” - all
das sind Beispiele dafür, wie Logik-Komposition noch einfacher gestaltet
werden kann zur Erfüllung von funktionalen Anforderungen.
Im Softwareuniversum sind damit die Hotspots der Medienaufmerksam-
keit so zu verorten:
Das ist doch interessant, mal so zu sehen, oder? Interessant ist, wo die


---


<!-- Page 428 of 584 -->


09-FinaleimSoftwareuniversum 419
Hotspots sind - und wo eben keine Aufmerksamkeit ist. Diese blinden
Flecken möchte ich mit Programming with Ease mehr ausleuchten. In den
Bänden geht es deshalb um andere Bereiche im Softwareuniversum.
Alle Lücken kann ich nicht (sofort) füllen. Aber ich bemühe mich, dir eine
zusätzlichePerspektiveundebeneinbigpicture zugeben.Ichwürdemich
freuen, wenn dir das helfen würde, deine Arbeit besser zu verstehen und
deine Entwicklung in der Programmierkunst besser zu gestalten.
Ich wünsche dir viel Erfolg!


---


<!-- Page 429 of 584 -->


Anhang -
Musterlösungen
Wenn du nachhaltig Software entwickeln willst, wie ich es mir vorstelle,
dann musst du dir nicht nur ein paar Tipps&Tricks merken. Es wäre
schön, wenn es so einfach wäre - doch das reicht leider nicht. Du braucht
vielmehr Übung und Experimente und Reflexion. Immerhin gilt es, einige
Gewohnheiten abzustreifen und Glaubenssätze zu verändern. Jedenfalls
ist es mir so ergangen auf meinem Weg zu Programming with Ease.
Um dich zu einer solch aktiven Auseinandersetzung mit der Methode zu
animieren, gehören zu den Kapiteln Übungsaufgaben. Vielleicht hast du
dich an der einen oder anderen schon versucht. Das wäre super, denn
dann hast du den ersten Schritt zur erfolgreichen Veränderung und zum
Kompetenzaufbau schon getan.
Der zweite Schritt besteht anschließend in der Reflexion deiner Lösungen.
Diekannstdualleinvornehmen,indemdudichamEndezurücklehnstund
überlegst, was gut und was schlecht gelaufen ist usw. Damit bewegst du
dich jedoch nur innerhalb deiner eigenen Komfortzone. Tiefer geht deine
Reflexion, wenn du sie von einem Kontrast ausgehen lässt. Den möchte
ich dir mit den Musterlösungen in diesem Band bieten.
Meine Vorstellung davon, wie die Übungsaufgaben gelöst werden könn-
ten, weicht sehr wahrscheinlich von deiner ab. “Könnten” schreibe ich
hier bewusst statt “sollten”, weil ich nicht glaube, dass es nur eine Lösung
für die Übungsaufgaben gibt. Vielmehr gibt es eine Lösungsbandbreite,
die z.B. davon bestimmt ist, wie Schwerpunkte bei der Anwendung von
Prinzipien und Praktiken gesetzt werden. Hier und da würde ich zwar
sagen, dass es “keine zwei Meinungen geben sollte”, doch allermeistens ist
das nicht so.


---


<!-- Page 430 of 584 -->


421
Die folgenden Musterlösungen sind daher nicht die Lösungen. Sie sind
nicht “richtig” und deine “falsch”, wenn sie anders aussehen. Der Wert
meiner Musterlösungen liegt nicht in einer “Wahrheit”, die sie verkörpern,
sondern vor allem in ihrer Andersheit.
DieDifferenz zwischendeinenLösungenundmeinenMusterlösungensoll
dich noch weiter anregen, darüber nachzudenken, warum du zu deinen
gekommen bist. Hattest du etwas missverstanden oder übersehen oder
sogar in gutem Willen ergänzt? Hast du einen anderen Schwerpunkt
gesetzt?
Warum meine Musterlösungen sind, wie sie sind, erkläre ich natürlich.
Meine Entscheidungen sind (hoffentlich) alle begründet und plausibel für
dich - was jedoch nicht heißt, dass man darüber nicht diskutieren könnte.
Hätte ich mich anders entschieden, wo Entscheidungsfreiheit bestand,
wäre ich zu anderen Lösungen gekommen - die vielleicht näher an deinen
liegen würden. Der Kürze wegen biete ich dir allerdings nur jeweils eine
Musterlösung pro Übungsaufgabe - und das auch nur in einem Monolog,
wie ihn ein Buch ermöglicht.
Doch eine Musterlösung ist besser als keine, würde ich sagen. Damit
kannst du deine Reflexion schonmal anregen und tiefer in den Lernstoff
eintauchen.
Für persönlicheres, konkreteres und dialogisches Feedback stehe ich dar-
über hinaus natürlich gern zur Verfügung. Melde dich jederzeit per Email
oder schaue dir auf meiner Homepage²¹³ an, was ich dir ergänzend an
Trainings und Coaching bieten kann.
Viel Erfolg und Freude bei der Lösung der Übungsaufgaben und der
anschließenden Reflexion!
²¹³https://ralfw.de/


---


<!-- Page 431 of 584 -->


Musterlösung: 01 - Die
Anforderung-Logik Lücke
Aufgabe 1 - Erklären
Wie ist es dir ergangen mit der Aufgabe? Ich könnte es verstehen, wenn
du dich damit schwer getan hast. Erstens überhaupt “ein Essay schreiben”,
zweitens die Darstellung auch noch besonders einfach in der Sprache
halten. Das waren schon zwei ordentliche Herausforderungen und ich
würde mich wunder, wenn du weniger als 60 Minuten dafür gebrauchst
hast.
IchselbsthabefürdiefolgendeMusterlösungaucheinigeAnläufenehmen
müssen. Mit 60 Minuten war es dabei nicht getan. (Aber eine größere
erwarteteBearbeitungsdauerwollteichauchnichtinderAufgabenennen,
um dich nicht gleich abzuschrecken.)
Wie so oft, ist das Ergebnis gerade wegen der begrenzten Zeit dann
etwas länger geworden. Mit mehr Zeit wäre ja Gelegenheit, Redundanzen
herauszukürzen oder knappere, elegantere Formulierungen zu finden.
Andererseits ist eine Erklärung, die sich an Laien richtet, quasi notwendig
länglicher, weil weniger an Begriffe und Konzepten vorausgesetzt werden
kann. Man muss dann mehr mit Beispielen/Analogien arbeiten, um das
Abstrakte für sie zumindest halbwegs greifbar zu machen.
Wie dein Ergebnis am Ende aussieht, ist für den Zweck der Aufgabe
jedoch zweitrangig. Schön, wenn es gut lesbarer Text herausgekommen
ist. Wichtiger jedoch ist aus meiner Sicht das, was vor und während dem
Schreiben passiert ist.
Für eine Erklärung musstest du erstmal selbst dein Verständnis der Begrif-
fe “Entwurf” und “Modell” aufbauen und schärfen.


---


<!-- Page 432 of 584 -->


Musterlösung: 01-DieAnforderung-LogikLücke 423
Und dann musstest du für die Anforderung ELI5 dein Verständnis noch-
mal transformieren in eine laienverständliche Form. Du musstest auswäh-
len und ordnen und auch noch in Worte fassen, was dir “intuitiv klar ist”.
Um diesen Prozess ging es mir bei dieser Aufgabe. Ein Prozess, der beim
Lernen im Allgemeinen und bei der Vermittlung von Programmierkennt-
nissen im Besonderen viel zu selten durchlaufen wird, finde ich. Denn auf
dieseWeisefindetLernenvielintensiverstatt.AufdieseWeiseersteignest
du dir den Stoff nämlich wirklich an. (Zumindest gilt das für Stoff, dessen
Verständnis du nicht unmittelbar durch Tun überprüfen kannst.)
Nach dieser Vorrede hier nun erstmal mein Versuch:
Vom Nutzen der Modellierung für die
Programmierung (ELI5)
Spielst du manchmal mit einer Puppe oder mit einem Spielzeugauto oder
mit einer Dinosaurierfigur? Oder hast du womöglich sogar ein Puppen-
haus oder einen Kaufladen oder Bauernhof, die du in deinem Zimmer
aufbauen kannst zum Spielen?
Super, denn dann weißt du auch, was ein Modell ist. Eine Puppe ist ein
Modell eines Menschen, ein Kaufladen ist ein Modell eines Supermarktes,
weil Puppe und Kaufladen in vielen Dingen einem Menschen bzw. einem
Supermarkt sehr ähnlich sind - aber sie sind eben viel kleiner und es fehlt
ihnen auch in anderer Hinsicht so einiges.
Dennoch macht es Spaß, mit einer Puppe oder einem Kaufladen zu spielen,
oder? Die haben ja auch Vorteile, z.B. dass sie dir zur Verfügung stehen,
wenn du es willst. Oder ein Spielzeugauto ist viel billiger als ein echtes.
Oder eine Dinosaurierfigur gibt es überhaupt, während echte Dinosaurier
gar nicht mehr leben. Du könntest einen echten Dinosaurer nicht mal im
Zoo besuchen, während du auf einem echten Bauernhof allerdings Urlaub
mit deinen Eltern machen könntest.
Modelle gleichen dem, was sie darstellen, einerseits also sehr; wenn du
damit spielst, ist es fast so, als würdest du z.B. wirklich ein Auto haben
odereinenBauernhof.AndererseitssindModellehandlicherundgünstiger.
Dein Eltern können dir z.B. ein Spielzeugauto kaufen, aber für ein echtes
müssten sie ganz lange sparen und du müsstest auch erstmal erwachsen
werden, um es fahren zu dürfen.


---


<!-- Page 433 of 584 -->


Musterlösung: 01-DieAnforderung-LogikLücke 424
Ein Modell ist also eine tolle Sache. Du kannst mit etwas spielen, was dir
sonst nicht zugänglich wäre. Du kannst dir damit vorstellen, wie es wäre,
z.B. einen echten Bauernhof zu haben, ohne deshalb gleich umzuziehen.
Mit einer Puppe kannst du dir vorstellen, wie es wäre, ein Baby zu haben,
ohne deshalb gleich wirklich ein eigenes Kind oder auch nur ein kleines
Geschwister bekommen zu müssen. Modelle sind also total bequem und
billig.
Wenn man nun programmiert, dann baut man im Grunde eine Art
Maschine. Die besteht zu einem Teil aus einem Computer, zum anderen
Teil besteht sie aus einem Rezept, das der Computer abarbeitet, um
irgendetwas zu tun, z.B. als Roboter euren Rasen zu mähen oder beim
Spiel auf deinem Smartphone eine Figur zu bewegen. Dieses Rezept heißt
Programm oder Software.
Ein Auto ist auch eine Maschine. Für die hast du ein Modell, mit dem du
dir vorstellen kannst, wie es wäre, ein richtiges Auto zu haben.
Genauso kann man als Programmierer für eine Software-Machine, die
manbauenwill,zunächstaucherstmalnureinModellherstellen;damitist
jedoch weniger der Computer gemeint, sondern vor allem das Programm,
das er abarbeiten soll. Dieses Modell kann dann natürlich nicht das, was
die echte Software-Maschine einmal tun soll - aber es sieht ihr eben doch
ähnlich und ist viel billiger.
Mit so einem Programm-Modell hat es ein Programmierer einfacher, sich
vorzustellen, wie es wäre, wenn er die spätere Software-Maschine wirklich
hätte. Das ist total nützlich, weil es sehr, sehr schwierig und teuer ist,
richtige Software-Maschinen zu bauen.
Einen Unterschied gibt es aber zwischen einem Spielzeugauto als Modell
und einem Modell für eine Software. Das Spielzeugauto-Modell wird dem
echten Auto nachempfunden; es gibt zuerst das echte Auto und dann das
Modell. Beim Programmieren macht man es anders herum: Da baut man
zuersteinModelloderauchzweioderdrei,umdanachdasechteProgramm
dem Modell nachzuempfinden.
Auf diese Weise kann sich ein Programmierer sparen, erst eine total
komplizierte Software-Maschine zu bauen, um dann zu merken, dass sie
doch nicht so geworden ist, wie er es gerne gehabt hätte. Besser ist es, er
stellterstmalnureinModellherundbeschäftigtsichdamit,umeinGefühl
dafür zu bekommen, wie es wäre, die echte Maschine zu haben. Wenn ihm


---


<!-- Page 434 of 584 -->


Musterlösung: 01-DieAnforderung-LogikLücke 425
das nicht gefällt, macht er einfach ein neues Modell. An so einem Modell
kann er sich halt eine Menge Dinge überlegen, ohne viel Arbeit zu haben:
Wie soll die Maschine aussehen? Wie soll sie bedient werden? Aus welchen
Teilen soll die Maschine bestehen? Wie sollen die Teile zusammengesteckt
werden, damit die Maschine leicht zu bauen ist?
Natürlich möchte ein Programmierer auch mega gern mit der echten
Software-Maschine arbeiten, so wie du am liebsten in einem echten Kauf-
laden etwas kaufen oder verkaufen würdest. Wenn der Programmierer
allerdings zu früh anfängt, seine Software-Maschine zu bauen, dann hat
er sich vielleicht noch gar nicht alles ausgedacht, was dazu nötig ist. Dann
wäre es später voll schwierig, die echte Maschine umzubauen, wenn ihm
etwas Neues einfällt, was sie können soll oder wie sie etwas anstellt. Auch
deshalbisteshilfreich,dassderProgrammierersicherstmalnurmiteinem
Modell beschäftigt. Das könnte ja aus soetwas wie Knete oder Lego oder
auch nur Papier sein, damit er ganz schnell neue Ideen ausprobieren kann.
Vielleicht hast du das ja auch schon gemacht: Statt ein Spielzeugauto zu
kaufen, hast du eines aus Lego selbst gebaut. Und als es dir nicht mehr
gefallen hat, hast du es umgemodelt oder eine Rakete aus den Legosteinen
gebaut.
Genau das sollten Programmierer auch tun, wenn sie eine Software-
Maschine bauen müssen. Sobald sie dann ein schönes Modell haben,
können sie es ja “in echt” bauen. Auf diese Weise wird es auch viel leichter,
die echte Maschine zu bauen. Die Programmierer müssen sich weniger
ärgern,weilsiesichvorallemwährenddesModellbausvertanhaben,wenn
es leicht ist, etwas zu korrigieren.
Modelle machen also das Programmieren leichter und günstiger.
Reflexion
Ich fand es schwierig, eine griffige Analogie für ELI5 zu finden. Mit dem
Spielzeug bin ich dann zufrieden gewesen. Vorher hatte ich es u.a. mit
Rezepten und einem Bauplan fürs Haus probiert. Das fühlte sich für das
Sprachniveau dann letztlich aber nicht so passend an.
Natürlich ist auch dieser Text nicht wirklich für 5jährige geeignet. Wich-
tiger ist, dass er möglichst wenig Jargon enthält und versucht, den Begriff
Modell und die Vorteile des Modellierens anschaulich zu machen. Was ist


---


<!-- Page 435 of 584 -->


Musterlösung: 01-DieAnforderung-LogikLücke 426
die Absicht dahinter, wenn man sich nicht negativen Konotationen und
UML-Feuerwerk beirren lässt?
Diese Absicht kommt im Text hoffentlich gut rüber: Modelle erlauben es,
dassmansichetwasvorstellenkann,ohneesrealindenHändenzuhalten.
Man soll ohne großen Aufwand ein Gefühl für etwas bekommen.
Was an Echtheit fehlt, ersetzt die Imagination. Das ist Sinn und Zweck
von Modellen, weil sie dadurch eben viel, viel einfacher herzustellen sind
als “the real thing”. Und weil das viel, viel einfacher ist, kann man sich
mehr Modelle leisten als “real things” - bzw. es sind Veränderungen an
Modellen einfacher, schneller, günstiger als an “real things”.
Dass Modellen viele Eigenschaften des Echten fehlen, kann mithin keine
Kritik sein. Es ist vielmehr ihr Vorteil und Hauptzweck. Es geht um Abs-
traktion. Statt Echtheit und “high fidelity” bekommt man etwas anderes.
Das sind Handlichkeit, Vereinfachung, Flexibilität und Fokus. Die sind
allesamt sehr nützlich, wenn man Anforderungen in Code umsetzen soll.
Code ist so komplex, dass man sich nicht einfach auf ihn stürzen kann,
sobald man meint, die Anforderungen verstanden zu haben. Besser, du
machst dich als Programmierer mit dem, was der Code tun soll und wie
er strukturiert sein könnte, erstmal anhand von Modellen vertraut. Du
kannst dir damit einige Tränen sparen!
Aufgabe 2 - Modellieren
Beim Modellieren ist alles erlaubt - nur kein Code. Das Modell soll
einerseits halbwegs “lebensecht” sein, andererseits soll ihm Wesentliches
fehlen, um den Aufwand klein zu halten und sich nicht Details zu
verlieren. Skizze statt Gemälde, so könnte man vielleicht sagen.


---


<!-- Page 436 of 584 -->


Musterlösung: 01-DieAnforderung-LogikLücke 427
VomModellzumProduktinfünfSchritten
Lösungsansatz
Ich weiß schon, dass das Programm über die Console bedient werden soll.
Außerdem ist klar, dass das Programm irgendwie die Besucherdaten
über seine Laufzeit hinweg speichern muss. Der Auftraggeber will den
LaptopzwischendenPartiesausschalten;ausschließlichimHauptspeicher
können die Gästedaten also nicht gehalten werden.
Auf der Festplatte könnten die Daten in einer Datenbank (z.B. RDBMS
mit SQLite) gehalten werden oder sogar noch einfacher in einer Textdatei.
Eine überschlägige Rechnung ergibt, dass ca. 15.000 Besucher über all
die Jahre mit dem Programm begrüßt werden sollen. Das ist nicht zu
viel, um sehr pauschal in einer Textdatei gespeichert zu werden. Eine
1,5MB Textdatei könnte bei Programmstart in den Hauptspeicher geladen
werden.SiekönnteauchwährendderProgrammlaufzeitständigerweitert
werden, damit keine Daten bei einem Programmabsturz verlorengehen.
Wahrscheinlich könnte die Datei sogar für jeden Gast geladen werden,
ohne dass eine Performanceeinbuße zu befürchten wäre. (Das kann ich
mir als ein “Forschungsthema” für eine spike solution²¹⁴ merken, falls
später beim Modellieren eine Entscheidung davon abhängt.)
²¹⁴http://www.extremeprogramming.org/rules/spike.html


---


<!-- Page 437 of 584 -->


Musterlösung: 01-DieAnforderung-LogikLücke 428
Das Speicherformat innerhalb einer Textdatei könnte für jeden Besucher
dessen Namen und seine Besuchsanzahl festhalten.
Modell
Software hat viele Stakeholder. Deren Ansprüche an ein Modell können
sehr unterschiedlich sein. Auftraggeber bzw. Anwender möchten mit
einem Modell ein Gefühl dafür bekommen, wie sich der Umgang mit der
Software später anfühlen wird. Für Entwickler hingegen ist es vor allem
interessant, ein Gefühl dafür zu bekommen, wie die Software aufgebaut
ist und ihr Verhalten erzeugt.
Es scheint mir deshalb angemessen, nicht nur ein Modell, sondern min-
destens zwei zu bauen.
Oberfläche
Das Oberflächenmodell könnte im einfachsten Fall aus einem Text wie
dem folgenden bestehen. Der ist zwar nicht interaktiv, aber er demons-
triert das Verhalten:
1 $ helloworld.exe
2 Name: Janine
3 Hello, Janine!
4 Name: Peter
5 Welcome back, Peter!
6 Name:
7 Name: Mike
8 Hello my good friend, Mike!
9 CTRL-C
10 $
• Es ist zu sehen, dass es verschiedene Begrüßungen gibt.
• Das Layout von Abfragen, Eingaben und Ausgaben ist zu sehen.
• Ein Betrachter sieht, was passiert, wenn jemand keinen Namen
eingibt.
• Es ist klar, wie das Programm zu beenden ist.
Das vermittelt ohne jeglichen Programmieraufwand schon einen guten
Eindruck dafür, wie sich das Programm zur Laufzeit anfühlt.
In anderen Szenarien könnte die Codierung eines Prototyps für die Be-
nutzerschnittstelle angezeigt sein. Das lohnt allerdings nur, wenn dessen


---


<!-- Page 438 of 584 -->


Musterlösung: 01-DieAnforderung-LogikLücke 429
Code um Größenordnungen weniger umfangreich ist, als der später
wirklich benötigte. UI Mockup Werkzeuge aller Art haben hier auch ihren
Zweck.
Ginge es um eine graphische Benutzeroberfläche, könnte ich z.B. mit
Balsamiq Mockups ein visuelles Modell so herstellen:
Dazu hätte ein Auftraggeber sicherlich eine Meinung, könnte Feedback
geben - und all das, ohne auch nur eine Zeile Code zu schreiben.
Aber um diese Art Modelle geht es mir ja in diesem Buch nicht. Die liegen
auf der Hand.
Interna
Das Problem bei dieser Hausaufgabe ich das Modell für dich als Ent-
wickler, d.h. ein Modell für die Interna des Programms. Wie kann Code
modelliert werden, der am Ende ja nur aus Text in Dateien besteht?
Ich könnte mit Dateien beginnen. Warum nicht aufschreiben, auf welche
Dateien der Code am Ende aufgeteilt werden sollte? Technisch reicht
eine einzige, z.B. program.cs. Aber dann ist mit einem Modell nichts
gewonnen.


---


<!-- Page 439 of 584 -->


Musterlösung: 01-DieAnforderung-LogikLücke 430
Aberesgibtvielleicht“Themen”,derenCodeinunterschiedlichenDateien
liegen könnte, z.B.
• benutzerschnittstelle.cs
• datenspeicherung.cs
• program.cs
Die Ausgabe auf der Console ist etwas ganz anderes, als die Datenspei-
cherung. Die Logik dafür zu trennen, macht bestimmt Sinn. Und der Rest
passiert dann in program.cs, der Datei, die es in C# sowieso gibt, um
die Funktion Main() zu beherbergen.
Die Liste der Dateien ist ein Modell. Jemand, der die Logik schreibt, wird
dadurch schon etwas angeleitet. Etwas Entscheidendes fehlt allerdings
noch: die Verbindungen zwischen diesen Codebausteinen. Die Logik, die
auf die Dateien verteilt wird, muss ja irgendwie zur Laufzeit zusammen-
arbeiten.
Eine simple Beziehung könnte schon die Reihenfolge der Dateien in einer
Listeausdrücken.DannkönnteAusführunglautobigerListez.B.mitLogik
in benutzerschnittstelle.cs beginnen, danach geht es weiter bei
datenspeicherung.cs und schließlich in program.cs. Aber das hört
sichnichtplausibelan,oder?Näherlägees,beiprogram.cszubeginnen.
Außerdem soll wahrscheinlich Logik nicht nur einmal in benutzer-
schnittstelle.cs ausgeführt werden, nachdem z.B. etwas in pro-
gram.cs passiert ist. Deshalb ist eine Reihenfolgenbeziehung zu wenig.
Die Verbindungen zwischen der Logik in den Dateien müssen flexibler
sein.
Mit Text lassen sich Verbindungen zwischen Elementen allerdings schwer
flexibel und verständlich beschreiben. Besser ist es, das Medium zu
wechseln und visuell zu werden.


---


<!-- Page 440 of 584 -->


Musterlösung: 01-DieAnforderung-LogikLücke 431
Die Linien drücken erstmal nur aus, dass es überhaupt Beziehungen
zwischen den Dateien gibt. Allerdings kann jetzt mehrfach Logik aus
derselben Datei im Spiel sein.
Aber worin bestehen diese Beziehungen? Wenn die Abarbeitung von
Logik nicht einfach von einer Datei in die nächste fließt, sondern hin
und her, dann geht das nur über Funktionsaufrufe. Die Verbindungslinien
stehen also ganz pauschal dafür, dass Logik aus der einen Datei Logik in
einer anderen mittels einer Funktion aufruft, die ihr von dort bekannt ist.
WenndasModellhilfreichseinsoll,dannbrauchtesalsonochetwasmehr
Detail in Form von Funktionsaufrufen: Welche Datei ruft wann welche
Funktion in welcher anderen auf? Das kann z.B. so aussehen:


---


<!-- Page 441 of 584 -->


Musterlösung: 01-DieAnforderung-LogikLücke 432
Von einer Funktion ist klar, in welcher Datei sie sich befindet: Main()
steckt konventionshalber als Eintrittspunkt für das Programm in pro-
gram.cs. Welche anderen Funktionen es gibt und wie sie auf die Dateien
verteilt sind, ist dann meine Sache. Das festzulegen, ist ein Teil der
kreativen Leistung während des Entwurfs. Die Dateinamen geben ja aber
schon einen Hinweis darauf, wie ich meine, dass die Verteilung aussehen
könnte.
Was du in dem “Sequenzdiagramm” siehst, ist eine Möglichkeit der
Verteilung. Ich behaupte nicht, dass es die beste ist. Um die Güte geht
es hier nicht, sondern darum, wie ein Modell überhaupt aussehen könnte.
Nur darüber solltest du dir erstmal Gedanken machen.
Reflexion
Erfüllt das, was ich produziert habe, die Anforderungen an ein Modell?
• Ein Modell soll deklarativ sein. Das bedeutet, es beschreibt nicht
das Wie, sondern das Was. Vor allem enthält es keine Logik. Das
ist der Fall. Ich habe nicht enthüllt, wie genau die Daten dargestellt,
geladen, transformiert werden. Dass Daten geladen werden, ist zu
sehen. Wie Daten geladen werden, welche Logik dafür nötig wäre
oder sogar welches Datenformat benutzt würde, ist nicht zu sehen.
• Ein Modell soll eine Liste von Funktionen liefern, die in der
Codierung mit Logik gefüllt werden. Das ist auch der Fall. Mindes-
tens fünf Funktionen sollte der Code zu diesem Modell am Ende
aufweisen. Sogar deren Signaturen sind definiert.
• EinModellsolldieBeziehungenzwischendenFunktionendeutlich
machen.DasistauchderFall.DaistdieAggregationsbeziehung,die
beschreibt,welcheFunktionenineinerDateizusammengefasstwer-
den sollen.²¹⁵ Da ist die Abhängigkeits- oder Nutzungsbeziehung
zwischen den Funktionen: Welche Funktion ruft welche andere
auf? Da ist die Teilenbeziehung: Welche Funktionen teilen sich
Daten?²¹⁶ Das ist die Sequenzbeziehung: Welche Funktion folgt
welcher anderen in der Nutzung?
²¹⁵Der Allgemeingültigkeit über Sprachen hinweg habe ich mich auf Dateien als Aggre-
gatevonFunktionenkonzentriert.DasfunktioniertinPythonoderRubyoderJavaScriptaus
dem Stand. In C# oder Java braucht es darüber hinaus allerdings noch eine Klasse. Doch
wenndiegenausowiedieDateibenanntist,dannmachtsiedasModellnichtkomplizierter.
²¹⁶Das sind z.B. loadAllGuests() und getGreeting(), die beide mit der Gästeliste
List<(string,int)>arbeiten.


---


<!-- Page 442 of 584 -->


Musterlösung: 01-DieAnforderung-LogikLücke 433
Ob die Mittel der Darstellung für das Modell die besten sind, ob das
Modell ein Gutes ist, sei dahingestellt. Formal erfüllt das Obige jedoch die
Kriterien für ein Modell. Und ich würde sogar sagen: Selbst dieses Modell
ist besser als keines.
DieQualitätdesModellsbestehtdarin,dassesmichzwingt,mirGedanken
zumachen.IchmussmirdieSoftwarevorstellen,wennauchnursehrgrob.
Unter Kenntnis dessen, wie ein Computer funktioniert und welche Logik
mir zur Verfügung steht, kann ich im Kopf simulieren, was passieren wür-
de. Das kann ich vergleichen mit dem, was ich an Verständnis während
der Anforderungsanalyse erarbeitet habe.
Wenn dir das schwer gefallen ist, verstehe ich das gut. Auch mir ist dieses
Modell schwer gefallen. Allerdings lag das daran, dass ich versucht habe,
alles zu vergessen, was ich dir eigentlich sagen möchte über Modellierung.
Ichhabemichzurückgenommen,umnäherandeinerSituationzusein.Du
liest das Buch ja wahrscheinlich, weil du noch keine größere Erfahrung
mitdemSoftwareentwurfhast.AufwelcheIdeenkommstduda?Dashabe
ich mir versucht vorzustellen.
Deshalb auch nochmal: Es kommt hier vor allem darauf an, dass du dir
ernsthaft Mühe gegeben hast. Hast du versucht, die Definition für ein
Modell umzusetzen? Mehr ist nicht wichtig gewesen bei dieser Übung.
Denn wenn dein Modell der Definition folgt, dann bist du weiter, als ohne.
Dann hast du mehr als einen Container für Logik - aka Funktion -, was es
dir schon viel leichter macht, die Logik zu finden. Logik in kleine Happen
teilen, damit sie verständlicher und testbarer wird, ist das Ziel.
Dass ein Modell vieles ungesagt lässt, dass es die Lösung unterspezifi-
ziert, ist selbstverständlich. Das gehört zu seinem Zweck und ist kein
Kritikpunkt. Dass du modellierst, ist mithin auch nicht im Widerspruch
zu jedem Anspruch der Agilität. Nur, weil du gerade nicht in die Tasten
haust, bedeutet das nicht, dass du nicht dabei bist, Wert für den Kunden
herzustellen. Es kommt halt aufs richtige Maß an.


---


<!-- Page 443 of 584 -->


Musterlösung: 02 - Entwurf
im Überblick
Gerade bei der Lösung dieser Aufgaben geht es nicht um richtig vs. falsch.
Ich habe dir keine konkrete Methode oder Notation vorgestellt, an die
du dich halten könntest, was dann mehr oder weniger richtig anwenden
könntest. Der Wert dieser Aufgaben liegt vielmehr darin, dich vom Reflex
der Codierens zu lösen.
“Codierend Probleme lösen” ist die Spezialität von vielen Entwicklern.
Wie auch sonst sollten Probleme gelöst werden? Aber die Problemlösung
besteht nach meiner Vorstellung nie aus Code! Code implementiert die
Lösung, er manifestiert sie. Die Lösung selbst jedoch ist “immateriell”. Sie
besteht in einem Ansatz, einem Vorgehen, einem Modell.
Mit diesen Übungen, ja, mit diesem Buch möchte ich dich dahin bringen,
die Lösung zu trennen von ihrer Implementation. Indem du überhaupt
einen Lösungsansatz und ein Modell entwickelst als Antwort für die
Aufgaben, hast du im Grunde schon alles richtig gemacht. Die Übung
steckt in deinem Bemühen um Abstand vom Code.
In einem Training würde ich dich fragen: “Wie war das für dich?” Doch
auch ohne persönlichen Kontakt kannst du für dich (oder mit Kollegen)
darüber reflektieren. Was war schwierig, was war leicht, was war uner-
wartet?
Aufgabe - Lösungsansatz finden
Die erste Aufgabe ist insofern etwas ungewöhnlich, als dass du dafür
wahrscheinlich etwas Recherche betreiben musst. Nur wenige Entwickler
(oder auch Ärzte) haben im Umgang mit Bedingten Wahrscheinlichkeiten
Erfahrung. Google hilft hier allerdings schnell und die Mathematik ist
nicht kompliziert. Deshalb habe ich mir erlaubt, die Aufgabe mal so zu


---


<!-- Page 444 of 584 -->


Musterlösung: 02-EntwurfimÜberblick 435
stellen. Ein bisschen Herausforderung darf sein, finde ich. Ich hoffe, ich
konnte deinen Problemlösungsehrgeiz etwas anstacheln.
Das Problem hat drei gut sichtbare, grobe Aspekte, würde ich sagen:
• Benutzerschnittstelle (Präsentationslogik)
• Datenbank (Datenzugriffslogik)
• Berechnung (Domänenlogik)
Das klingt naheliegend, quasi wie aus dem Lehrbuch. Vielleicht fällt dir
dazu auch gleich ein Architekturmuster ein: die Schichtenarchitektur.
Damit hättest du womöglich sogar schon das halbe Modell in der Tasche.
Doch darum geht es in der Aufgabe nicht. Hier ist lediglich der Lösungs-
ansatz gefragt.
In dessen Sinn halte ich die Benutzerschnittstelle in diesem Fall für
uninteressant. Sie ist trivial und in den Anforderungen vorgegeben. Da
ist keine Kreativität mehr gefragt.
Bei der Datenbank hast du vielleicht aufgehorcht: “Ah, das ist doch
konkret! Da gibt es so viel zu bedenken.” Du möchtest dem Auftraggeber
bestimmt viele Fragen stellen.
Aber auch dieser Aspekt ist aus meiner Sicht hier relativ unspannend. Die
Interaktion mit der Datenbank ist trivial: aus ihr wird nur gelesen. Und
selbst wenn darin Tausende Einträge stünden, ließe sich der gewünschte
blitzschnell finden. Von einer Datenbank zu sprechen, ist fast schon zu
viel. Es ist einfach eine mehr oder weniger lange persistente Liste von
Datensätzen.²¹⁷
Diese Datensätze könnten z.B. in Form einer simplen CSV-Datei bei
Installation mitgeliefert werden:²¹⁸
²¹⁷Die für mich spannendste Frage wäre hier eigentlich die nach der Aktualisierung.
Wie wird einer Programminstallation in einer Arztpraxis eine neue Version der Datenbank
mitgeteilt? Bestimmt kommen jeden Tag neue Tests hinzu und manche werden obsolet
oder ändern sich in ihren Parametern. Der SARS-CoV-2 PCR-Test ist dafür ein Beispiel. So
spannenddieFrageaberauchist,sieistjenseitsderAufgabenstellung.ImrealenLebenwäre
sie sehr relevant, in der Übung nicht. Eine Aktualisierung ist nicht einmal erwähnt; also ist
sie keinen Gedanken in der Lösung wert. Die einfachste Variante einer Datenbank kann
angenommenwerden.
²¹⁸Sensitivität und Spezifizität des PCR-Tests für SARS-CoV-2sind als “Mittelwerte”den
Angaben eines Faktenchecks bei CORRECTIV entnommen. Die Prävalenz hingegen ist nur
ein grober Mittelwert zwischen den in einem Bericht zur Heinsbergstudie angegebenen
“Extremwerten”15,5%und2,2%.


---


<!-- Page 445 of 584 -->


Musterlösung: 02-EntwurfimÜberblick 436
1 Diagnose;Test;Prävalenz;Sensitivität;Spezifizität
2 Brustkrebs;Mammographie;0,01;0,8;0,904
3 SARS-CoV-2 Infektion;PCR-Test;0,08;0,98;0,97
Die Erkenntnis, dass es um read-only Zugriffe auf eine simple Liste geht,
und die Entscheidung für eine Persistenz mittels CSV-Datei reicht für den
Lösungsansatz.
Lösungsansatz für die Domänenlogik
Die Herausforderung dieser Aufgabe steckt also im verbleibenden Aspekt,
in der Domäne. Wie kannst du das Vorgehen bei der Berechnung als
Lösungsansatz beschreiben, gar visualisieren?
Wenn du gegooglet hast, bist du sicher auf Wikipedia²¹⁹ gestoßen. Dort
wird dir eine Formel präsentiert:
BerechnungeinerBedingtenWahrscheinlichkeit
Das bedeutet:
Die Wahrscheinlichkeit, dass Ereignis A eingetreten war,
wenn man Ereignis B beobachtet, entspricht der Wahrschein-
lichkeit, dass A und dann B eintreten geteilt durch die Wahr-
scheinlichkeit, dass man überhaupt ein B beobachtet.
Das Ereignis A vorliegt, kannst du auch als Hypothese oder “A wie
Annahme”betrachten-z.B.“DieFrauhatBrustkrebs.”DasEreignisBoder
“B wie Beobachtung” ist das Testergebnis für diese Hypothese - z.B. “Die
Mammographie der Frau hat ein positives Ergebnis.”
Und etwas weiter unten bei Wikipedia findest du noch eine detailliertere
Formel, den Satz von Bayes:
²¹⁹https://de.wikipedia.org/wiki/Bedingte_Wahrscheinlichkeit


---


<!-- Page 446 of 584 -->


Musterlösung: 02-EntwurfimÜberblick 437
SatzvonBayes
Als Start ist das nicht schlecht - nur wo ist darin der Bezug zu den
Größen aus der Datenbank, den Berechnungsgrundlagen? Da kommt der
Entscheidungsbaum ins Spiel, der beim Multiplikationsansatz gezeigt ist.
Allerdings finde ich die deutsche Erklärung nicht so gut, besser wird
es auf der englischsprachigen Wikipedia-Seite zum Bayes Theorem²²⁰
dargestellt.
EntscheidungsbaumfürdasBayesTheorem
Mit so einem Baum lassen sich die relevanten Fälle plastisch und nach-
vollziehbar machen, zumindest in einem so einfachen Beispiel wie dem
vorliegenden. Darin kannst du nämlich alle Angaben platzieren. Etwas
ausführlichererklärtdasz.B.dieseSeitezumThemaBedingteWahrschein-
lichkeiten²²¹.
Für Lösungsansätze versuche ich oft zunächst konkret zu sein und dann
die Lösung durch Verallgemeinerung/Abstraktion zu finden. Also zuerst
konkret das Beispiel Mammographie:
• 10.000Frauen,diesicheinerMammographieunterziehen,bildenim
Entscheidungsbaum die Wurzel als Grundgesamtheit.
• Von diesen 10.000 Frauen, die sich untersuchen lassen, leiden 1%
an Brustkrebs. Das ist ein Faktum, das unabhängig vom Test fest-
²²⁰https://en.wikipedia.org/wiki/Bayes%27_theorem
²²¹https://www.mathebibel.de/bedingte-wahrscheinlichkeit


---


<!-- Page 447 of 584 -->


Musterlösung: 02-EntwurfimÜberblick 438
gestellt wird. Im obigen Entscheidungsbaum ist das die Wahr-
scheinlichkeit P(A)=0,01. Daraus ergeben sich zwei Knoten unter
der Wurzel: Die Menge der Frauen, die Brustkrebst haben (10.000
x 0,01=100) und die, die gesund sind (10.000 x (1-0,01)=10.000 x
0,99=9.900 oder 10.000 - 100 = 9.900).
• Jetzt wird der Test auf beide Untermengen angewandt. Natürlich
weiß man dabei nicht, welche getestet wird. De facto ergeben sich
dennoch für jeden der beiden Unterknoten wiederum zwei Knoten:
eine Untermenge, bei der der Test korrekt ist und eine, bei der er
inkorrekt ist.
– Auf der Seite der tatsächlich Kranken ist die Sensitivität
des Tests relevant. Krank und als solche auch erkannt (true
positive) sind 100 x 0,8 = 80 Frauen; krank, aber als solche
nicht erkannt (false negative) sind 100 - 80 = 20 Frauen. Der
Sensitivität entspricht im EntscheidungsbaumP(B|A)=0,8. Die
beiden ganz linken Äste zusammen entsprechen der Multipli-
kation P(B|A) x P(A) im Zähler beim Satz von Bayes.
– Auf der Seite der Gesunden ist die Spezifizität des Tests
relevant. Gesund und als solche auch erkannt (true negative)
sind 9.900 x 0,904 = 8.950 Frauen; gesund, aber als krank
gemeldet (false positive) werden 9.900 - 8.950 = 950 Frauen.
Die Spezifizität des hiesigen Szenarios hat im Bayes Theorem
keinen Namen. Sie versteckt sich in P(B), worin die rechte
Seite des Baumes eingeht.


---


<!-- Page 448 of 584 -->


Musterlösung: 02-EntwurfimÜberblick 439
EntscheidungsbaumfürdasMammographie-Szenario
Auf dieser Basis die finale Berechnung der gesuchten Aussage: Wie
hoch ist die Wahrscheinlichkeit, dass ein positiver Test tatsächlich eine
Erkrankung bedeutet?
• DazubrauchtesnochdieWahrscheinlichkeitP(B) bzw.dieZahlder
Beobachtungen positiver Tests überhaupt. Die lässt sich aus dem
Baum ganz leicht ablesen: es gibt true positives und false positives.
Die Zahl der Frauen mit beiden Ergebnissen sind zu addieren: 80 +
950 = 1.030.
• Die gesuchte Aussage ist das Verhältnis der zurecht als krank
erkannten zu den insgesamt positiv getesteten Frauen: 80 / 1.030
= 0,0776 = 7,8%.
Nur in 7,8% aller Fälle ist also ein positiver Mammographie-Test auch eine
wahre Aussage über den Gesundheitszustand einer Frau.²²²
²²²Hättest du das gedacht? Obwohl der Test doch recht gut ist - immerhin werden 80%
der Erkrankungen erkannt - ist seine Aussagekraft gering. Aber so ist das mit Bedingten
Wahrscheinlichkeiten: sie leiten uns schnell in die Irre. Selbst Profis haben das nicht im
Kopf (oder im Gefühl), wie die angeführte Studie zeigt. Wir lassen uns zu schnell von einer
Testgüte im Sinne der Sensitivität beeindrucken und haben die Prävalenz nicht im Blick.
Wenndiesehrgeringist,dannkommtesnämlichaufdieSpezifizitätan.Istdienichtnahezu
perfekt, kommt es zu hohen false positive Meldungen, die das gute Ergebnis durch hohe
Sensitivitätnachuntenziehen.


---


<!-- Page 449 of 584 -->


Musterlösung: 02-EntwurfimÜberblick 440
Damit ist der wesentliche Teil des Lösungsansatzes fertig. Alles hat seinen
Platz, was gegeben war; alles steht im Zusammenhang.
• Durch die Angabe der Diagnose oder des Tests auf der Kommando-
zeile werden aus der Datenbank die relevanten Werte geladen. Das
ist außerhalb der Domänenlogik.
• EbenfallswirddurcheinenKommandozeilenparameterderrelevan-
te Ast im Baumdiagramm gewählt. Wird nach der Wahrscheinlich-
keit eines positives Ergebnisses gefragt, geht es um die gezeigten
Blatt-Knoten. Bei Frage nach der Wahrscheinlichkeit für ein negati-
vesErgebnis,würdendieKnotenfüreinnegativesErgebnisgewählt.
Hier ergäbe sich eine Wahrscheinlichkeit von 8.950 / (20 + 8.950) =
0,997 = 99,7%.
• Die aus der Datenbank geladenen Zahlen gehen alle in die Berech-
nung ein. Wenn in einem ersten Schritt immer der gesamte Baum
berechnet wird, kann in einem zweiten die Glaubwürdigkeit als
Ergebnis aus den Blättern “gepflückt” werden.


---


<!-- Page 450 of 584 -->


Musterlösung: 02-EntwurfimÜberblick 441
DerumdieGlaubwürdigkeitsberechnungerweiterteEntscheidungsbaum
Das ist eine problemspezifische informelle Darstellung, die es mir sehr
leicht gemacht hat, eine Lösung zu finden. Es gibt noch andere visu-
elle/zweidimensionale Darstellungen für Bedingte Wahrscheinlichkeiten,
doch diese hat mir unmittelbar eingeleuchtet.
Von ihr ausgehend kann ich auch leicht einen Schritt weitergehen in
Richtung Formalisierung und Modell. Mit Excel lässt sich der Berech-
nungsfluss durch den Baum ohne Hochspracheneinsatz interaktiv gestal-
ten. Das ist ein trivialer Prototyp, den ich einem Auftraggeber vorlegen
könnte. Sogar ein Modell kann ich mir damit sparen, bevor ich Feedback


---


<!-- Page 451 of 584 -->


Musterlösung: 02-EntwurfimÜberblick 442
bekomme.
PrototypderLösungmitExcel
Und die dahinter stehenden Berechnungen lassen sich vielleicht sogar in
die Implementation übernehmen, für die ein Modell den Rahmen vorgibt:
Reflexion
Zweierlei scheint mir hervorhebenswert an dieser Aufgabe:
1. DerLösungsansatzumfasstnichtdasgesamteProblem.MancheAs-
pekte sind so naheliegend/einfach, dass sie nicht betrachtet werden
müssen. Auch sie müssen später im Modell natürlich repräsentiert
sein; doch eine nähere Auseinandersetzung ist (zunächst) nicht
nötig. Wirklich spannend, herausfordernd, problematisch ist nur
ein Teil der Gesamtaufgabe. Diesen Teil zu finden, sollte dein erstes
Bemühen sein. Mach dir die Problemlösung einfacher, indem du so
viel wie möglich ausblendest. Konzentriere dich auf das Wichtigste
bzw. Schwierigste. Denn wenn du das nicht in den Griff bekommst,
ist der Rest auch egal.


---


<!-- Page 452 of 584 -->


Musterlösung: 02-EntwurfimÜberblick 443
2. Der Lösungsansatz hat eine sehr individuelle Form. Vielleicht er-
findest du die, vielleicht kannst du aber auch etwas nutzen, was
andere schon erfunden haben. Der Entscheidungsbaum in meiner
Lösung “ist nicht auf meinem Mist gewachsen”. Dein Job ist die
Problemlösung inklusive Implementation. Als Entwickler gewinnst
du keinen Blumentopf für die Erfindung einer besonders kreativen
Darstellung für den Lösungsansatz. Er muss einfach nur tauglich
sein, um dir im Lösungsprozess zu helfen und am Ende die Lösung
zu kommunizieren bzw. in ein Modell zu übersetzen.²²³
²²³Ich hätte das P(B) im Satz von Bayes weiter aufschlüsseln können, um mir die Rech-
nung mit einer angenommenen und willkürlichen Grundgesamtheit zu sparen. Sensitivität
und Spezifizität wären darin aufgetaucht und die Lösung wäre schlicht eine lange Formel.
Dashabeichhiernichtgetan,umderVisualitäteinenVorzugzugeben.Abereskönnteein
OptimierungsschrittinderModellierungoderspäterderImplementierungsein.


---


<!-- Page 453 of 584 -->


Musterlösung: 03 - Radikale
Objektorientierung
Wieist es dir gegangenbei der Übersetzungdeines Lösungsansatzes? Hast
du eine Differenz bemerkt zwischen dem, wie du normalerweise codiert
hättest und wie PoMO/IOSP es nun von dir verlangt haben? Wie differen-
ziert hast du die Klassen/Objekte und die Funktionen gestaltet? Hast du
zuerst an Klassen und dann an Methoden gedacht oder umgekehrt? Gibt
es bei dir Klassen, die als Nachrichten fließen oder sind das nur primitive
Datentypen?
Eine “richtige” Lösung gibt es hier nicht in Bezug auf die inhaltliche
Strukturierung. Unter welchem Dach du Logik angesiedelt hast, ist nicht
wichtig. Aber in Bezug auf die Form habe ich jetzt schon eine Erwar-
tung. “Richtig” ist deine Lösung nur, wenn deine Methoden entweder
nur integrieren oder nur operieren. Sie enthalten entweder keine Logik
oder nur Logik. Ist das der Fall? Wieviele Integrationsmethoden hast du
“gefunden”?
Aufgabe - Mit PoMO/IOSP
implementieren
Der Lösungsansatz in der Musterlösung für Kapitel 2 hat sich vor allem
auf die Berechnung der Glaubwürdigkeiten bezogen. Die Schwierigkeit
der Aufgabe steckte in der Domänenlogik.²²⁴ Der Rest drumherum ist
technisches Handwerk. Daraus ergab sich für mich bei der Erarbeitung
der Musterlösung leicht eine Modellskizze.
²²⁴EinHinweisaufdasKernproblemistfürmichdieSprache.Wasisteseigentlich,wasda
berechnetwerdensoll.MathematischbetrachtetgehtesumeineWahrscheinlichkeit.Dasist
für Anwender aber abstrakt. Wie kann die Wahrscheinlichkeit verständlicher, relevanter,
greifbarer gemacht werden? Mit einem guten Be-Griff. Den hatte ich für mich in der
Musterlösungmit“Glaubwürdigkeit”gefunden.Anschließendwaralleseinfacher.Woklare
Begriffe fehlen, versteckt sich also oft das Kernproblem, d.h. das Problem, das noch am
kniffligstenist.


---


<!-- Page 454 of 584 -->


Musterlösung: 03-RadikaleObjektorientierung 445
Modellskizze
Die “großen” Verantwortungsbereiche in Verfeinerung des Lösungsansat-
zes sind:
• Analyse der Kommandozeile. Die Parameter müssen ausgelesen
und der weiteren Verarbeitung zur Verfügung gestellt werden.
• Ermittlung des relevanten Tests aus der Datenbank aufgrund der
Angabe auf der Kommandozeile.
• Die Auswertung des Tests in Bezug auf die Glaubwürdigkeit. Das
ist die Domäne, der Kern der Anwendung. Darauf bezieht sich der
Lösungsansatz vor allem.
• Die Ausgabe einer Beschreibung der Glaubwürdigkeit.
Dabei könnte es bleiben. Doch mein Gefühl sagt mir, dass eine Auswer-
tung noch nicht gleich eine verständliche Beschreibung der Glaubwürdig-
keit ist. Davon lebt das Programm ja aber, dass am Ende ein Text steht,
der auch für einen Laien eine Bedeutung hat. Deshalb sehe ich noch eine
weitere Verantwortlichkeit:
• Deutung der Glaubwürdigkeit. Die Wahrscheinlichkeiten der Aus-
wertung laut Lösungsansatz werden verständlich formuliert. Die
Ausgabe am Ende ist damit trivial und aufs Technische reduziert.
Dies ist nur eine Modellskizze, weil der Lösungsansatz zwar verfeinert ist,
aber konkrete Funktionen mit Signaturen und Beziehungen nicht explizit
sind. Mit meiner Erfahrung in der Codierung mit PoMO und IOSP traue
ich mir zu, von hier aus direkt in den Code zu springen. Ein etwas feineres
BilddesModellshabeichimKopf.Ichüberblicke,dassdieHerstellungdes
Verhaltens geradlinig sein wird. Aber: Don’t try this at home! Oder hast
du es in deiner Lösung schon genau so gemacht?
Codierung der Integration
Um von dieser Modellskizze in den Code zu kommen, gehe ich top-
down vor. Ich beginne beim Groben: den Objekten und den dazwischen
aufgespannten“Nachrichtenkanälen”.IchbeginnealsomitDefinitionvon
Klassen, von denen ich Objekte instanziiere.


---


<!-- Page 455 of 584 -->


Musterlösung: 03-RadikaleObjektorientierung 446
1 var db = new Testdatenbank();
2 var exp = new Experte();
3 var über = new Übersetzer();
4 var con = new Console();
5 var kom = new Kommandozeile(args);
Diese Objekte repräsentieren die Verantwortlichkeiten in meiner Spiegel-
strichliste der Modellskizze. Ich bin halt der Meinung, dass diese “Rollen”
mit ihren unterschiedlichen Aufgabengebieten im “Zusammenspiel” eine
Gesamtlösung “darstellen” können.
Lediglich das Objekt für die Kommandozeile{} ist hier hervorhebens-
wert, weil es mit der Kommandozeile (args) initialisiert wird. Es ist für
mich ein Datenobjekt, also ein Objekt, das für eine Datenstruktur steht.
In diesem Fall strukturiert Kommandozeile{} ein string-Feld gemäß
der Syntax für den Kommandozeilenaufbau der Anwendung. Damit wird
ein nicht weiter syntaktisch und semantisch strukturiertes Feld zu etwas
für die weitere Verarbeitung Bedeutsamem. Ich freue mich, dass mir die
mainstream Objektorientierung diese Möglichkeit zur Kapselung gibt.
Mit den Objekten in der Hand überlege ich, wie zwischen ihnen Nachrich-
ten fließen sollen. In einer Integration stöpsle ich sie zu einem “Netzwerk”
zusammen, wie Bauteile auf einer elektronischen Platine.
1 var test = db.Heraussuchen(kom.Bezeichnung);
2 var auswertung = exp.Auswerten(test);
3 var übersetzung = über.Deuten(test, auswertung, kom.Ergebnis);
4 con.Display(übersetzung);
Die Hilfsvariablen sind streng genommen nicht nötig. Es könnten alle
Funktionsaufrufe auch geschachtelt stattfinden:
1 con.Display(
2 über.Deuten(
3 db.Heraussuchen(kom.Bezeichnung),
4 exp.Auswerten(
5 db.Heraussuchen(kom.Bezeichnung)),
6 kom.Ergebnis));
Ist das allerdings besser verständlich? Ich glaube nicht. Du kannst das
lesen, wenn du dich anstrengst; ein natürlicher Lesefluss verläuft jedoch
anders. Und db.Heraussuchen() muss sogar zweimal aufgerufen wer-
den; das widerspricht deiner “Performanceästhetik” sicherlich.


---


<!-- Page 456 of 584 -->


Musterlösung: 03-RadikaleObjektorientierung 447
Lesefluss verläuft für mich von oben nach unten und von links nach
rechts.DemlaufengeschachtelteFunktionsaufrufeimwahrstenSinnedes
Wortes zuwider. Deshalb plädiere ich für die Nutzung von Hilfsvariablen.
Mit ihnen kann ich den Lesefluss natürlich halten. Außerdem vermeide
ich damit den mehrfachen Aufruf von Methoden; doch das ist für mich
sekundär.
ImSinnederradikalenObjektorientierungstellendieHilfsvariablenNach-
richten dar, z.B. ist test die Nachricht, die db “absondert” und dann zu
expundüberfließt.Oder genauer:testistnichtdie Nachricht,sondern
die payload für die Nachrichten, die bei den Empfängern Auswerten()
und Deuten() lauten.
Die Integration reichert hier also Daten an, indem sie sie in Nachrichten
verpackt. Aus test wird exp.Auswerten(test).
Wenn du sehr kritisch hinschaust, könntest du das als zweierlei Verant-
wortlichkeiten ansehen. Sollte Integration nicht nur auf “Verdrahtung”
konzentriert sein, d.h. die Verbindung von Objekten zu einem Ganzen wie
eine Leiterplatte?
Ich denke, da ist etwas dran. In anderen Zusammenhängen würde ich da
auch mehr differenzieren wollen. Ein erster Schritt wäre es z.B., wieder
zurückzugenerischenMethodenzugehenundalleNachrichtenalseigene
Typen auszudrücken.
1 var test = db.Handle(kom.Bezeichnung);
2 var auswertung = exp.Handle(test);
3 ...
Dabei musst du aber aufpassen, dass sich Quellobjekte (z.B. db) nicht mit
ihren Nachrichten logisch an Senkenobjekte ( exp) binden. Die Quelle
darf immer noch nichts über die Senke wissen. Indem sie nur einen Test
“absondert”, sind viele Objekte frei, damit etwas anzufangen. Allerdings
kommt es auf den Kontext an; den spannt eine Integration auf. Insofern
finde ich es nicht so schlimm, wie in der ersten Integrationsvariante
gezeigt, die aus test ein exp.Auswerten() macht.
Dennoch haben konkrete Nachrichtentypen ihren Platz in der radikalen
Objektorientierung, wie du später sehen wirst.
Eine noch extremere Form der Integration “ohne Eingriff” wäre, Nach-
richten auf einen Bus zu legen, an den sich jeder Interessierte anschließen
kann. Hier eine ganz knappe Skizze:


---


<!-- Page 457 of 584 -->


Musterlösung: 03-RadikaleObjektorientierung 448
1 var bus = new MessageBus();
2
3 var db = new Testdatenbank();
4 var exp = new Experte();
5 ...
6
7 bus.Abonnieren += db.Publizieren;
8 bus.Abonnieren += exp.Publizieren;
9 ...
10
11 db.Abonnieren += bus.Publizieren;
12 exp.Abonnieren += bus.Publizieren;
13
14 bus.Send(new Start());
DerNachrichtenbuswärehiernureinMedium,dasNachrichtenvonallen
Quellen an alle Senken weiterleitet. Jede Senke entscheidet dann, ob sie
darauf reagieren will. Das ist total generisch und könnte im Grunde auch
automatisiert werden, wenn Quellen und Senken formal erkennbar wären
(z.B. über ein Interface). Um Senken nicht zu überlasten mit irrelevanten
Nachrichten,könntenAbonnementsauchtypisiertsein;jedeSenkekönnte
beim Abonnieren angeben, an welchen Nachrichten sie interessiert ist.
Dieser Ansatz hat einen gewissen Charme, insbesondere in technischer
Hinsicht.DochschondieseSkizzesolltedirklarmachen,worineingroßer
Nachteil liegt: eine Integration mittels Bus ist informationsarm. Ihr geht
jedeKlarheitab,wasdenngenaudieVerbindungensindzwischenQuellen
und Senken. Es ist kein Nachrichtenfluss erkennbar, auch wenn garantiert
ist, dass alle Nachrichten zuständige Empfänger erreichen.
Deshalb ziehe ich, wo ich kann, vor, Quell- und Senkenobjekt in der Inte-
grationexplizitzuverbindenwieindererstenIntegrationzusehen.Dasist
in einem linearen, eindimensionalen Programmtext etwas umständlicher
als in einem Diagramm, aber mit etwas Disziplin geht es schon. Wenn
du erstmal genügend viele Modelle in Code übersetzt hast und dabei
Formulierungsmuster befolgst, wird es dir leicht fallen, aus PoMO/IOSP
CodeeinvisuellesModellabzuleiten.Ichmachedasinzwischenreflexhaft.
Und wenn es nicht gelingt, dann weiß ich, dass im Code etwas quer sitzt.
Aber zurück zur Codierung des Lösungsansatzes für die Bestimmung
der Glaubwürdigkeit von Testergebnissen. Die Integration zeigt mir den
Prozess, wie das Ergebnis schrittweise durch die Zusammenarbeit der
Objekte hergestellt wird. Mit diesem Code kann sich jeder schnell einen
Überblick über die Verhaltenserzeugung verschaffen. Dieser Code lässt
sich auch leicht erklären. Viele gute Eigenschaften kommen hier zusam-
men: Übersichtlichkeit (alles liegt auf einem Blick vor), Lesbarkeit (alles
kann von oben nach unten lesend verstanden werden), Konformität mit
SLA (Single Level of Abstraction Prinzip). Was willst du mehr?


---


<!-- Page 458 of 584 -->


Musterlösung: 03-RadikaleObjektorientierung 449
1 var test = db.Heraussuchen(kom.Bezeichnung);
2 var auswertung = exp.Auswerten(test);
3 var übersetzung = über.Deuten(test, auswertung, kom.Ergebnis);
4 con.Display(übersetzung);
db stellt einen test her, der zu exp fließt und dort vom Auswerten()-
“Rezeptor” “empfangen” wird. Daraufhin erzeugt exp eine auswertung,
die zusammen mit dem test und dem auf der Kommandozeile angegebe-
nen Ergebnis kom.Ergebnis zu Objekt über fließt, das Tupel aus allen
dreieinem“Rezeptor”fürDeutsch()-Nachrichten“empfangen”wirdzur
Verarbeitung. Und die liefert dann eine übersetzung, die zu Objekt con
fließt, wo sie von Display() akzeptiert und verarbeitet wird, was zu
einem Seiteneffekt auf der Konsole führt, der Anzeige für den Benutzer.
Eigentlich alles ganz einfach, oder?
Soweit zumindest die Theorie. Denn mehr ist der Code bisher nicht. Es
gibt weder die Klassen zur Erzeugung der Objekte, noch die “Rezeptor-
Methoden”darauf.AbermeineIDERider vonJetBrainsfürC#unterstützt
mich bei diesem Vorgehen: Klassen, die es nicht gibt, kann ich mit einem
Tastendruck anlegen; Methoden, die es nicht gibt, kann ich mit einem
Tastendruck in den zugehörigen Klassen anlegen. Das folgende Bild zeigt
diese Schritte, die ich für alle Klassen und Methoden in der Integration
durchlaufen bin.


---


<!-- Page 459 of 584 -->


Musterlösung: 03-RadikaleObjektorientierung 450
Zuerst habe ich alle Objekte instanziiert und dabei die zugehörigen Klas-
sen angelegt. Dann habe ich die Objekte im Sinne des Nachrichtenflusses
verbunden mit Hilfsvariablen und dabei die Funktionen angelegt.
Codierung der Operationen
NachdemichmitderIntegrationdasbigpicturederLösungimplementiert
habe, kann ich nun bei den Teilen weitermachen. Die Implementation ist
also ein rekursiver top-down Prozess: Ich nehme mir eine Funktion vor
undfleischesieaus.EntwederfülleichLogikein(Operation)oderichrufe
andere Funktionen auf (Integration). Am Anfang steht nur eine Funktion
zur Diskussion: Main(). Jetzt allerdings habe ich die Qual der Wahl
zwischen vier Methoden. Wo also beginnen, beim Einfachen oder beim
Komplizierten, oben oder unten in Liste, außen (Benutzerschnittstelle,
Persistenz) oder innen (Domäne)?
Da alle Objekte unabhängig voneinander sind (PoMO), ist es im Grunde
egal, wo ich beginne. Deshalb beginne ich da, wo ich am meisten Klarheit
habe: beim Objekt für die Kommandozeileninterpretation.
1 class Kommandozeile
2 {
3 public Kommandozeile(string[] args) {
4 Bezeichnung = args[0];
5 Ergebnis = args[1] == "positiv" || args[1] == "positive" || args[1] == "1";
6 }
7
8 public string Bezeichnung { get; }
9 public bool Ergebnis { get; }
10 }
Die Logik ist trivial, wenn ich keine Variationen und keine Fehlerbe-
handlung annehme. Das will ich auch nicht, weil nichts davon in den
Anforderungen steht und es für den Zweck hier unwesentlich ist. Deshalb
kann auch die gesamte Logik im Konstruktor stehen. Ein Datenobjekt wie
die Kommandozeile{} kann nur “leben”, wenn die Analyse des string-
Feldes erfolgreich war; ansonsten stürzt das Programm womöglich ab.
Weiter am anderen Ende der Integration, bei der Ausgabe. Damit bleibe
ich bei der Benutzerinteraktion, also einem peripheren Objekt, das dem
Benutzer zugewandt ist.
Hier ist die Logik noch einfacher. Ich beschränke die Verantwortlichkeit
des Objektes darauf, eine Nachricht aufzugeben, die schon formuliert


---


<!-- Page 460 of 584 -->


Musterlösung: 03-RadikaleObjektorientierung 451
ist. Das vom System.Console-API abhängige Objekt soll nicht mit
Entscheidungen in Bezug auf die Domäne befasst sein. Das würde seine
Testbarkeit reduzieren.
1 class Console
2 {
3 public void Display(string übersetzung)
4 => System.Console.WriteLine(übersetzung);
5 }
Ichhabeüberlegt,obichdieseeineZeilewirklichineinObjektkapsle.Die
Integration könnte doch so aussehen:
1 var test = db.Heraussuchen(kom.Bezeichnung);
2 var auswertung = exp.Auswerten(test);
3 var übersetzung = über.Deuten(test, auswertung, kom.Ergebnis);
4 System.Console.WriteLine(übersetzung)
Aber damit wäre Main() eben keine Integration mehr, weil darin Logik
stünde: der Aufruf von System.Console(). Es wären Abstraktions-
niveaus vermischt, was der Verständlichkeit abträglich ist. Es wäre die
Testbarkeit geschmälert.
Und überhaupt hätte das ekelig ausgesehen. Ja, das meine ich so: unschön,
unsauber,garekelig.Soetwasgehörtsichnicht.Damitwillichausdrücken,
dass Clean Code Development für mich eine Sache der Ästhetik ist. Ich
möchte dir also ein ästhetisches Empfinden vermitteln, dass dich reflex-
haft das Richtige tun lässt. Du sollst rauskommen aus einer immer wieder
anstrengenden bewussten Beurteilung von Code in Bezug auf Testbarkeit
und Ordnung. Solange dein Bewusstsein noch eingeschaltet ist, stehst
du schnell in Zielkonflikten - die du oft zuungunsten von Testbarkeit
und Ordnung entscheidest. Wenn aber diese Werte in ein ästhetisches
Empfinden “codiert” werden können, dann stehen sie im Grunde nicht
mehrzurDisposition.Dannfolgtduihnenreflexhaft.NurinExtremfällen
hältst du inne, um zu überlegen, ob du wirklich dem ästhetischen Reflex
folgen sollst.
Programming with Ease soll dir also wirklich unter die Haut gehen. Ich
möchte bei dir eine gewisse Alternativlosigkeit installieren, die robust ist
gegen Anfeindungen des Tagesgeschäftes. Gewisse Prinzipien sollst du
einfach einhalten no matter what. Oder zumindest aller-, allermeistens.
So wie du allermeistens die Verkehrsregeln einfach einhältst oder nicht


---


<!-- Page 461 of 584 -->


Musterlösung: 03-RadikaleObjektorientierung 452
stiehlst oder die Wahrheit sagst oder den Müll trennst. Nicht immer, aber
allermeistens. Weil es “sich richtig anfühlt”.
Für mich fühlt sich System.Console() in der Integration nicht richtig
an. Wenn ich solchen Code sehe, schüttle ich mich.
Klar, in diesem Beispiel ist das alles nicht so schlimm. Doch ich möchte
dich von Anfang an mit “schönen Bildern” trainieren und habe deshalb
selbst diese eine Zeile in ein eigenes Objekt verpackt. Das hat nicht weh
getan, das frisst kein Brot, das bläht den Code nicht wirklich auf.
Jetzt ist die Hälfte der Peripherie implementiert. Die andere Hälfte besteht
aus dem Datenbankzugriff. Er stellt sozusagen die dunkle Seite des Pro-
gramms dar, weil er dem Betrachter abgewandt ist, aber Interaktion mit
der Umwelt darstellt.
Der Datenbankzugriff ist schon etwas umfangreicher. Hier fühle ich mich
nicht mehr wohl, die gesamte Logik in die öffentliche Methode zu stecken.
Deshalb wird die zu einer Integration. Du kannst in ihr leicht überblicken,
wie das Heraussuchen funktioniert: zuerst werden die Daten geladen,
dann fließen die geladenen Daten weiter zur eigentlichen Filterung.
1 class Test
2 {
3 public string Testbezeichnung;
4 public string Diagnose;
5 public double Prävalenz;
6 public double Sensitivität;
7 public double Spezifizität;
8 }
9
10
11 class Testdatenbank
12 {
13 public Test Heraussuchen(string bezeichnung) {
14 var tests = Laden();
15 return Heraussuchen(tests, bezeichnung);
16 }
17
18 private IEnumerable<Test> Laden()
19 => File.ReadAllLines("testdatenbank.csv")
20 .Select(x => x.Split(';'))
21 .Skip(1)
22 .Select(Map);
23
24 private Test Map(string[] roherDatensatz) {
25 var deDE = CultureInfo.CreateSpecificCulture("de-DE");
26
27 return new Test {
28 Diagnose = roherDatensatz[0],
29 Testbezeichnung = roherDatensatz[1],
30 Prävalenz = double.Parse(roherDatensatz[2],deDE),
31 Sensitivität = double.Parse(roherDatensatz[3],deDE),
32 Spezifizität = double.Parse(roherDatensatz[4],deDE)
33 };
34 }
35
36 private Test Heraussuchen(IEnumerable<Test> tests, string bezeichnung)
37 => tests.First(x => x.Testbezeichnung.IndexOf(bezeichnung) >= 0 ||


---


<!-- Page 462 of 584 -->


Musterlösung: 03-RadikaleObjektorientierung 453
38 x.Diagnose.IndexOf(bezeichnung) >= 0);
39 }
VonaußenbetrachtetfindetdasHeraussuchenalsoaufpersistentenDaten
statt. Intern hingegen ist es geteilt in einen persistenten Anteil (Laden())
und einen nicht persistenten, der das tatsächliche Heraussuchen über-
nimmt. Das äußere Heraussuchen() könntest du als eine Form von
decorator²²⁵ ansehen.
Wie du vielleicht erspürst, hat mit C# mit seinen Sprachfeatures die
Implementation sehr erleichtert. Linq zur Verarbeitung von Mengen mit
seinen Funktionen Select() oder First() ist ein Segen! Ein schönes
Beispiel auf für radikale Objektorientierung: von ReadAllLines() bis
Select(Map) (Zeile 19ff) fließen Daten durch einen Verarbeitungspro-
zess.
Der Test ist für mich ein reine Nachrichtenobjekt. Deshalb haftet ihm
keine Funktionalität an. Darüber lässt sich streiten; im Sinne des Prinzips
Separation of Concerns (SoC) und auch des IOSP glaube ich jedoch, dass
das so richtig ist. Später mehr dazu.
Für mich ist das Testdatenbank{}-Objekt immer noch eine Operation,
die in Main() integriert wird. Dem widerspricht nicht, dass darin selbst
wiedereineIntegrationsmethodesteckt.EsgehtumdenGesamtzweckdes
Objektes; der ist, etwas zu tun; es ist ein Arbeitspferd, keine “Führungs-
kraft”.
Nach der Peripherie kann ich nun nicht mehr anders, als mich dem Kern,
der Domäne zuzuwenden. Am klarsten laut Lösungsansatz ist mir darin
das Objekt, das ich Experte{} genannt habe:
²²⁵https://en.wikipedia.org/wiki/Decorator_pattern


---


<!-- Page 463 of 584 -->


Musterlösung: 03-RadikaleObjektorientierung 454
1 class Auswertung
2 {
3 public double GlaubwürdigkeitPositivesErgebnis;
4 public double GlaubwürdigkeitNegativesErgebnis;
5
6 public double Ergebnisglaubwürdigkeit(bool ergebnis)
7 => ergebnis ? GlaubwürdigkeitPositivesErgebnis
8 : GlaubwürdigkeitNegativesErgebnis;
9 }
10
11 class Experte
12 {
13 public Auswertung Auswerten(Test test) {
14 const double GRUNDGESAMTHEIT = 1000000.0;
15
16 var tatsächlichPositiv = GRUNDGESAMTHEIT * test.Prävalenz;
17 var truePositive = tatsächlichPositiv * test.Sensitivität;
18 var falseNegative = tatsächlichPositiv - truePositive;
19
20 var tatsächlichNegativ = GRUNDGESAMTHEIT - tatsächlichPositiv;
21 var trueNegative = tatsächlichNegativ * test.Spezifizität;
22 var falsePositive = tatsächlichNegativ - trueNegative;
23
24 return new Auswertung {
25 GlaubwürdigkeitPositivesErgebnis = truePositive /
26 (truePositive + falsePositive),
27 GlaubwürdigkeitNegativesErgebnis = trueNegative /
28 (trueNegative + falseNegative)
29 };
30 }
31 }
Die Logik entspricht dem, was im Lösungsansatz als Baum ausgeführt ist.
Ich habe mich den einfach von oben nach unten durchgehangelt und auf
das Excel-Kalkulationsblatt geschielt.
Den Lösungsansatz selbst habe ich dabei nicht in Frage gestellt. Sicher
könnte der optimiert werden, indem ich auf die Rechnung mit einer ima-
ginierten Grundgesamtheit zurückgreife. Die Berechnung könnte auch
rein mit Wahrscheinlichkeiten laufen. Doch dagegen habe ich mich im
Entwurf entschieden und werde es nicht ad hoc in der Codierung umsto-
ßen.²²⁶
Und zum Schluss die ominöse Deutung. Im Lösungsansatz taucht sie gar
nicht auf. Die Skizze der Benutzerschnittstelle in der Aufgabenstellung
macht allerdings deutlich, dass es nicht mit der Ausgabe einer Glaubwür-
digkeit getan ist. Der Benutzer will einen Text sehen und auch noch einen,
den er halbwegs verstehen kann.
DieAuswertungmussalsogedeutetundinetwasVerständlichesübersetzt
werden. Das macht das Übersetzer{}-Objekt. Dort fließen alle bisher
²²⁶Sollte ich aber mal ein Rappel bekommen und diesen Teil optimieren wol-
len, dann wüsste ich, wo genau ich dafür ansetzen müsste: nur bei der Nachricht
Experte.Auswerten(). Die Verantwortlichkeit für die Domäne ist klar und völlig ent-
koppeltvonanderenObjekten.


---


<!-- Page 464 of 584 -->


Musterlösung: 03-RadikaleObjektorientierung 455
gewonnenen Daten zusammen und werden in einen zweizeiligen Text
übersetzt.
Dass es ein Text mit zwei Zeilen ist, deutet darauf hin, dass die Überset-
zung etwas mit der Benutzerschnittstelle zu tun hat. Wäre die grafischer,
gar bildlicher, würde die Deutung nicht in einem Text resultieren.
Andererseits beschäftigt sich der Übersetzer mit Domänendaten wie Test
und Auswertung. Er gehört also nicht direkt zur Peripherie.
Für mich steht das Übersetzer{}-Objekt zwischen Domäne und Peri-
pherie, ist aber peripherienah. Es ist ein typischer Mapper, der etwas aus
dem Inneren der Software für die Außenwelt verständlich macht, ohne
dabei von einem API abhängig zu sein.
1 class Übersetzer
2 {
3 public string Deuten(Test test, Auswertung auswertung, bool ergebnis) {
4 var deutung = new StringBuilder();
5
6 deutung.AppendFormat(
7 "Die Wahrscheinlichkeit für eine korrekte {0} Diagnose von '{1}' ist: {2:0.000}",
8 ergebnis ? "positive" : "negative",
9 test.Diagnose,
10 auswertung.Ergebnisglaubwürdigkeit(ergebnis));
11
12 var glaubwürdigkeitAlsText = auswertung.Ergebnisglaubwürdigkeit(ergebnis)
13 .ToString()
14 .Replace(".", "");
15 var führendeNullen = 0;
16 for(var i=0;i<glaubwürdigkeitAlsText.Length;i++)
17 if (glaubwürdigkeitAlsText[i] == '0')
18 führendeNullen++;
19 else
20 break;
21 var getestete = Math.Pow(10, führendeNullen);
22 var erkrankte = auswertung.Ergebnisglaubwürdigkeit(ergebnis) * getestete;
23
24 deutung.AppendFormat(
25 "\nBei ca. {0:0} von {1} getesteten Personen ist die Aussage des Tests korrekt.",
26 erkrankte,
27 getestete
28 );
29
30 return deutung.ToString();
31 }
32 }
Wie du siehst, ist die gesamte Logik zur Deutung in nur einer Methode
versammelt.Dasistnichtschön-aberinsofernsauber,alsdassesauchhier
keine funktionalen Abhängigkeiten gibt. Deuten() ist eine waschechte
Operation.²²⁷
²²⁷Ja, die Methode ist eine Operation auch wenn sie auf der Auswertung
Ergebnisglaubwürdigkeit() aufruft. Warum das für mich kein Widerspruch
zum IOSP ist, erkläre ich dir später. An dieser Stelle bemerkst du hoffentlich, dass
dieser scheinbare Widerspruch dir keine Verständnisschwierigkeiten macht und auch die
Testbarkeitnichteinschränkt.


---


<!-- Page 465 of 584 -->


Musterlösung: 03-RadikaleObjektorientierung 456
Warum habe ich Deuten() aber nicht weiter “gesäubert”? Weil den Prin-
zipien Genüge getan war; die Aufgabe war erledigt. Das letzte fehlende
Stück Logik war implementiert, das Programm lief - und so habe ich mich
entschlossen, es so stehen zu lassen, bis ich wieder dran muss. Dann ist es
leicht zu refaktorisieren. Deuten() hat eine klare Struktur, die ich durch
Auslagerung zweier Funktionen explizit machen könnte.
So viel auch aus didaktischen Gründen mal als Beispiel, dass nicht immer
alles perfekt sein muss. Dreck bleibt zurück, das ist ganz natürlich. Nur
sollte der ein gewisses Maß nicht überschreiten. Und du solltest jederzeit
in der Lage sein, die Regeln der Kunst darauf anzuwenden.
Deshalb bis auf Weiteres auch hier: Don’t try this at home!
Reflexion
Es war etwas ungewohnt, den Code nur nach dem Lösungsansatz zu
schreiben. Ohne zu einem Stift zu greifen und zuerst ein Modell zu
zeichnen, musste ich mich schon sehr konzentrieren. Ich weiß nicht, wie
du es gemacht hast, aber für mich war es ein kleiner Ehrgeiz, ohne ein
Modell zu arbeiten, weil die Lösung der Aufgabe zu Kapitel 2 keines
geliefert hatte.
Klar, ich hätte “nachmodellieren” können und habe das auch im Kopf
getan. Die Modellskizze am Anfang ist das Ergebnis. Ein “richtiges”
Modell hingegen gab es trotzdem nicht. Das hat die Implementation doch
etwas herausfordernder gemacht als üblich.
Einerseits. Denn andererseits ist mir dadurch noch bewusster geworden,
welchen Halt PoMO und IOSP mir während der Codierung geben. Der
Code kann strukturell gar nicht so schlimm werden, wenn ich mich nur
tapfer an die Prinzipien halte. Insbesondere IOSP hält mich ständig an der
Hand. Wenn mir wieder ein Aspekt einfällt, den ich noch in den Code
einbringen muss, dann setzt mir als erstes IOSP dafür klare Grenzen. Das
erleichtert mich enorm.
Ebenso ist es im Vorgehen einfach, mich durch die Unterscheiden zwi-
schen Integration und Operation führen zu lassen. Meistens beginne ich
aufeinerEbenemitderIntegrationundhabedannschonallesNotwendige
vor mir liegen. Aber es kann auch mal sein, dass ich an einer Operation


---


<!-- Page 466 of 584 -->


Musterlösung: 03-RadikaleObjektorientierung 457
sehr interessiert bin; dann realisiere ich die und weiß, dass sie später in
einer Integration ihren Kontext finden wird. Gerade bei solchem bottom-
up Vorgehen ist mir das PoMO hilfreich, weil es mich daran erinnert, das
Objekt, auf das ich mich gerade konzentriere, nicht von anderen abhängig
zu machen.


---


<!-- Page 467 of 584 -->


Musterlösung: 04 -
Flow-Design mit
1-dimensionalen
Datenflüssen
Aufgabe 1 - Modellieren und
implementieren
Als Lösungsansatz wähle ich den ersten in Kapitel 2 skizzierten:
Darin wird zwar noch mehrfach einem Namen gefragt, aber das kann ich
ja im Modell weglassen.


---


<!-- Page 468 of 584 -->


Musterlösung: 04-Flow-Designmit1-dimensionalenDatenflüssen 459
Lösungsansatz verfeinern: Prä-Modell
Ich könnte jetzt versuchen, den Lösungsansatz gleich in ein Flow-Design
Modell zu überführen. Doch auch wenn es einfach ist, Modelle zu verwer-
fen,willichnichtzufrühanfangen.CodeistschwierigeralseinDiagramm
zu ändern. Ein Diagramm ist aber immer noch schwieriger als eine Liste
zu ändern.
Datenflüsse sind Sequenzen von Funktionseinheiten. Damit sind sie im
Grunde Listen. Und Listen kann man noch leichter anfertigen als Da-
tenflüsse. Umso leichter, je weniger ich auf eine Reihenfolge der Listen-
einträge achten muss. Also verfeinere ich den Lösungsansatz zunächst
rein textuell, um mir mehr Überblick zu verschaffen; das ist mein Prä-
Modell. Die Stationen im Datenfluss müssen für mich darin im Kopf Sinn
ergeben. Wenn ich sie mir wie eine Geschichte erzählen kann, dann bin
ich zufrieden.
Was muss also passieren, um das gewünschte Verhalten herzustellen?
Wie sieht der Gesamtprozess aus? Ich kann meine Überlegung beim
Wichtigsten beginnen oder auch am Ende des Prozesses.
• DasWichtigste,dieDomäneistdieErmittlungeinerBegrüßung(O)
für einen Namen (I) mit einer gewissen Anzahl Besuche (I).
Woher kommen die Inputs (I) für diesen Schritt, wohin geht der Output
(O)?
• Die Begrüßung (I) muss einfach nur ausgegeben werden auf der
Console.
• Der Name (O) ist eine Ausgabe der Nachfrage beim Anwender über
die Console.
• Die Anzahl der Besuche (O) kommt aus der Datenbank. Dort steht
ja zu jedem Namen (I), wie oft der schon auf einer Party war. Laut
LösungsansatzwerdeninderDatenbankTupelgespeichert:(Name,
Besuchsanzahl).
EigentlichsindjetztalleInputsdurchOutputsbefriedigt.Dochesfehltein
Schritt:


---


<!-- Page 469 of 584 -->


Musterlösung: 04-Flow-Designmit1-dimensionalenDatenflüssen 460
• Der Name ist zu registrieren. Die Besuchsanzahl muss in der Daten-
bank für den Namen (I) aktualisiert werden. Das ist so wichtig wie
die Domäne.²²⁸
Das Prä-Modell halte ich für vollständig. Ich glaube, alles Nötige wird
darin irgendwie getan. Jetzt sollte ich seine Schritte noch in die richti-
ge Reihenfolge bringen. Bisher waren die Prozessschritte in beliebiger
Reihenfolge, so wie sie mir eingefallen sind oder gerne auch mal von
hinten nach vorne entwickelt. Vom Output her denken, hilft oft beim
Datenflussentwurf, also upstream.
Für das Modell ist eine downstream Orientierung aber natürlich besser.
1. Namen erfragen (NErf)
2. Namen registrieren (NReg)
3. Besuchsanzahl zum Namen ermitteln (BErm)
4. Begrüßung bestimmen (BBest)
5. Begrüßung ausgeben (BAusg)
Dannach kann ich einen Datenfluss einfach aufzeichnen.
Modell
Die Schritte im Entwurf sind für mich:
1. Free-form Lösungsansatz finden
2. Liste: Prozessschritte sammeln
3. Liste: Prozessschritte ordnen
4. Diagramm: Prozess als Datenfluss visualisieren
Das ist ein kleiner Wasserfall - den du aber natürlich wie ein Lachs
auch mal entgegen den Strom wieder hoch schwimmen kannst. Bei der
Visualisierung kann dir z.B. auffallen, dass ein Prozessschritt fehlt oder
sogar der Lösungsansatz eine Lücke hat.
²²⁸WennessowichtigwiedieDomäneist,könnteichüberlegen,dieseVerantwortlichkeit
in die Domäne zu ziehen, also von der Datenbank unabhängig zu machen. Aber der
Einfachheithalberlasseichesjetztso,wieesistmitdemLösungsansatzunddemPrä-Modell.
AmVorgehenwürdedieser“Twist”nichtsändern.UmsVorgehengehteshierabervorallem.


---


<!-- Page 470 of 584 -->


Musterlösung: 04-Flow-Designmit1-dimensionalenDatenflüssen 461
Je nach Problemschwierigkeitsgrad durchlaufe ich diese Schritte mehr
oder weniger explizit mit mehr oder weniger Iterationen.
Jetzt aber zum Modell. Das zeichne ich nach der geordneten Liste der Pro-
zessschritte mit deren Abkürzungen. Dadurch kann meine Visualisierung
etwas knapper werden.
Das war einfach. Dabei hat es keine Überraschungen gegeben. Der Daten-
fluss ist nach der Liste keine so große Erleuchtung, würde ich sagen. Den-
noch finde ich ihn wichtig, damit du dich an die Darstellung gewöhnst.
Implementation
DasInteressanteanderImplementationist“dieVerdrahtunginReihe”der
Funktionseinheiten:
1 static void Main(string[] args) {
2 var name = NamenErfragen();
3 NamenRegistrieren(name);
4 var n = BesuchsanzahlErmitteln(name);
5 var begrüßung = BegrüßungBestimmen(name, n);
6 BegrüßungAusgeben(begrüßung);
7 }
Main() ist die Funktion, die die Implementation des Datenflusses inte-
griert. Irgendwo muss das ja geschehen. Erst ab C# 9.0 ist dafür keine
Funktion an der Wurzel mehr nötig. Andererseits macht Main() kein
Problem. Die Funktion ist nur wie ein bisschen altbekanntes Rauschen.
Immerhin gibt es sie seit knapp 50 Jahren - zuerst in C, dann C++, Java,
C#.
Dass jeder Schritt im Prozess, den der Datenfluss des Modells darstellt,
zu einer Funktion geworden ist, sollte dich nicht überraschen. Die Namen
habe ich der geordneten Liste entnommen, also nicht die Abkürzungen
benutzt. Das macht sich im Code besser; der hat länger Bestand als das
Modell, das nur als Zwischenschritt gedacht ist.


---


<!-- Page 471 of 584 -->


Musterlösung: 04-Flow-Designmit1-dimensionalenDatenflüssen 462
Die Implementationen der einzelnen Funktionen zu zeigen, ist unspan-
nend. Es sind kurze Operationen. Nur eine möchte ich exemplarisch
herausgreifen:
1 private static string NamenErfragen() {
2 while (true) {
3 Console.Write("Name: ");
4 var name = Console.ReadLine();
5 if (string.IsNullOrWhiteSpace(name) is false)
6 return name;
7 }
8 }
Erstens ist hier eine Schleife zu finden. Das soll dich ein wenig beruhigen:
Schleifen bleiben dir erhalten, auch wenn ich oben gegen Schleifen gewet-
terthabe.SiehabenimDatenflussnichtszusuchen;inderimperativenLo-
gik sind sie aber natürlich ein nützliches Konstrukt. NamenErfragen()
kapselt das Detail, dass solange nach einem Namen befragt wird, bis ein
nicht leerer eingegeben wird. Solange bleibt die Kontrolle in der Funktion.
Danach gibt sie sie mittels return ab; sie ist fertig. In anderen Szenarien
könnte sie aber auch die Kontrolle behalten wollen, z.B. wenn mehrere
Namen erfragt werden sollen. Das geht auch - aber dazu erst später mehr.
ZweitensistdieFunktion-horribiledictu-einestatischeFunktion.Sowas
sehen viele mainstream OO-Entwickler nicht gern. Manche wettern sogar
massiv dagegen und sagen, das ginge gar nicht. Das sei ganz und gar nicht
objektorientiert und gehöre im Grunde verboten. Pfui, static!
Aber ich sehe das anders. Widerspricht die statische Definition der Funk-
tion den Prinzipien PoMO oder IOSP? Nein. Widerspricht sie anderen
Prinzipien wie SRP oder SLA? Nein. Wo sollte also ein Problem mit
static sein?
Radikale Objektorientierung verortet die Verarbeitung von Daten aka
Messages in Funktionen. Die enthalten Logik zur Transformation von Ein-
gabeninAusgaben.SolangedieseFunktionennichtaufZustandzugreifen
müssen, gibt es kein Problem mit statischen Funktionen. Daten, Variablen
“global” zu machen, also weithin sichtbar, widerspricht natürlich dem
Gedanken der Kapselung. Lokalität lässt sich gut mit Klassen herstellen,
die ihre Daten nicht veröffentlichen, also private halten. Doch hier
geht es gar nicht um solchen schützenswerten Zustand. Deshalb ist eine
allergische Reaktion gegen static unangebracht.
Im Gegenteil! Ich meine, dass jede statische Funktion begrüßt werden
sollte. Du solltest dich förmlich strecken nach statischen Funktionen.


---


<!-- Page 472 of 584 -->


Musterlösung: 04-Flow-Designmit1-dimensionalenDatenflüssen 463
Denn die sind erstens leichter testbar. Und zweitens - unter der Prämisse,
dasssienichtaufDatenaußerhalbihrerzugreifen-sindsieverständlicher.
Warum solltest du darauf verzichten wollen, nur weil ein paar Leute
eine gewisse Vorstellung von Objektorientierung entwickelt haben, die
massenweise auch ohne statische Methoden zu schwer evolvierbaren
Codebasen führen?
Die anderen Operationen in meiner Implementation des Modells sind
natürlich ebenfalls statische Funktionen. Der verwaltete Zustand - die
Gästeliste - ist persistent auf der Festplatte und insofern ohnehin “global”.
Da würde eine Kapselung in ein “echtes” Objekt nicht helfen. Davon
abgesehen sind wir noch nicht bei der Modularisierung. Lass uns einen
Schritt nach dem anderen machen.
Aufgabe 2 - Reverse modeling
Die Integration in der Musterlösung zum Problem der Bedingten Wahr-
scheinlichkeiten sah so aus:
1 var test = db.Heraussuchen(kom.Bezeichnung);
2 var auswertung = exp.Auswerten(test);
3 var übersetzung = über.Deuten(test, auswertung, kom.Ergebnis);
4 con.Display(übersetzung);
Was du im Programmtext von oben nach unten liest und verstehst, das
visualisierst du im Datenfluss-Modell gewöhnlich von links nach rechts.
Jeder Funktionsaufruf in der Integration wird dabei zu einem “Kringel”.
Es wäre schön, wenn du das auch textuell so ausdrücken könntest. In F#
könnte das z.B. ungefähr so aussehen:
kom.Bezeichnung |> db.Heraussuchen |> exp.Auswerten |>
über.Deuten |> con.Display
Nur ungefähr wäre das eine Übersetzung, weil darin einige Details nicht
beachtet sind:
• test fließt nicht aus Auswerten() heraus, aber in Deuten()
hinein.
• Deuten() hat mehr als einen Input.


---


<!-- Page 473 of 584 -->


Musterlösung: 04-Flow-Designmit1-dimensionalenDatenflüssen 464
• kom.Ergebnis ist ein Zwitter: einerseits steht kom für eine Daten-
struktur, andererseits muss ein Ergebnis als bool-Wert fließen.
Wie können diese Details in einem visuellen Fluss als Modell unterge-
bracht werden?
Ein Teil des Geheimnisses steckt in einem fehlenden Funktionsaufruf in
der obigen Integration. Der ist unscheinbar in der Musterlösung und ist
dort der Konstruktion der Objekte zugeschlagen: der Konstruktor von
Kommandozeile{}. Vollständig sieht die Integration nämlich so aus:
1 var kom = new Kommandozeile(args);
2 var test = db.Heraussuchen(kom.Bezeichnung);
3 var auswertung = exp.Auswerten(test);
4 var übersetzung = über.Deuten(test, auswertung, kom.Ergebnis);
5 con.Display(übersetzung);
Der erste Schritt ist nicht das Heraussuchen eines Tests, sondern die Ana-
lyse der Kommandozeile. Denn woher sollen sonst plötzlich Bezeichnung
und Ergebnis kommen? Main() als Integrationsmethode bekommt die
Kommandozeile lediglich als string[] args geliefert.
Im Modell nenne ich die Analyse aus Gewohnheit zunächst Parse, weil
es um die Übersetzung eines Textes in eine bedeutungsvolle Struktur
geht wie bei einem Compiler. Die Zerlegung in “Symbole” (tokenization)
hat allerdings die Infrastruktur schon übernommen durch Zerlegung der
Kommandozeile in nicht leere Teilzeichenketten. Im Programm bleibt
deshalb lediglich das Parsing übrig, d.h. die Erkennung bzw. syntaktische
Einordnung dieser “Symbol”: aus zwei Zeichenketten werden eine Testbe-
zeichnung und ein Testergebnis.


---


<!-- Page 474 of 584 -->


Musterlösung: 04-Flow-Designmit1-dimensionalenDatenflüssen 465
Parsing ist das, was passiert. Das könnte ja auch explizit geschehen, z.B.
1 var (bezeichnung, ergebnis) = Kommandozeile.Parse(args);
2 var test = db.Heraussuchen(kom.Bezeichnung);
3 ...
In der radikal objektorientierten Lösung hatte ich mich jedoch dafür
entschieden, die Kommandozeile als Datenstruktur zu verstehen. Auf
einer inhaltlich niedrigen Abstraktionsstufe war ihr Typ string[]. Mit
Kommandozeile{}hatteichsieaufeinehöhereStufegehoben.args[0]
ist technisch, kom.Bezeichnung ist domänenspezifisch. Nach der Kon-
struktion von kom stehen im Code Bezeichnung und Ergebnis über das
Objekt zur Verfügung wie nach der Generierung des Tupels durch Par-
se().
Dem Code treuer wäre allerdings ein Modell wie folgt:


---


<!-- Page 475 of 584 -->


Musterlösung: 04-Flow-Designmit1-dimensionalenDatenflüssen 466
Du siehst, ich habe mir hier gleich eine Freiheit genommen: aus einem
Konstruktor als Funktionseinheit - benannt mit ctor und dem Datenty-
pen Kommandozeile{} - fließt etwas heraus, das “technische” Objekt.
Indem ich es mit kom benenne, stehen mir seine Daten downstream zur
Verfügung.
Gräme dich nicht, wenn du an dieser Stelle unsicher warst. Diese klei-
ne Herausforderung sollte dich dazu bringen, etwas mehr zu grübeln
und kreativ zu werden. Denn auch wenn ich dir ein Denkmodell und
eine Notation dafür vorstelle, heißt das nicht, dass das vollständig oder
allein seligmachend wäre. Du solltest dir die Offenheit bewahren, von
der “offiziellen” Flow-Design Notation abzuweichen, um dein Modell
ausdrucksstark zu formulieren, wenn dir etwas fehlen sollte. So hat sich ja
auchdieFlow-DesignNotationselbst,wiedusiehiersiehst,überdieJahre
entwickelt: Wenn wir etwas nicht ausdrücken konnten, dann haben wir
einen Weg gesucht, es zu tun - der konsistent war mit dem, was schon
existierte. Das Einfachste waren am Anfang also “Kringel” und Pfeil -
des Rest musste sich dem anpassen, weil schon ein Rahmen vorgegeben


---


<!-- Page 476 of 584 -->


Musterlösung: 04-Flow-Designmit1-dimensionalenDatenflüssen 467
war.²²⁹
In diesem Entwurf sind alle Problempunkte von oben adressiert:
• test wird mit | wieder aufgegriffen
• Deuten() kann natürlich ein Tupel als Input bekommen, das
nach einem | aus dem, was upstream an verschiedenen Stellen
entstanden ist, zusammengesetzt ist
• kom ist ein Datum im Fluss mit einer eigenen Struktur und wird im
Fluss über seinen Konstruktor erzeugt
Der letzte Punkt ist technisch trivial, war für’s reverse modeling aber
etwas knifflig. Nun siehst du, wie auch das abgebildet werden kann.
Damit ist auch ein Beispiel geschaffen für weitere Modelle. In denen kann
es sein, dass du an einer Stelle zunächst eine Funktionseinheit platzierst
wie Parse() und sie später ersetzt durch einen Konstruktor. Im Kapitel
über die Modularisierung werden wir das sicher wiedersehen.
Trotz der kleinen Herausforderung war für dich bei dieser Aufgabe
deutlichzuspüren,wieleichtsichPoMO/IOSP-CodezurückineinModell
übersetzen lässt. Mit ein wenig Übung wirst du für ein Modell schon den
Code vor deinem geistigen Auge sehen und umgekehrt, für Code einen
Datenflussfühlenundimaginieren.Dasgehörtfürmichzur“ästhetischen
Erziehung”mitFlow-Design:IchmöchtedireinCodeidealvermitteln,das
du reflexartig anstrebst und bei dessen Abwesenheit durch schauderst.
Ideal ist es deshalb, weil es dir den Wechsel vom Denken zum Codieren
so leicht macht. Du kannst vom Konzeptionellen zum Praktischen ganz
einfach wechseln. Das ist nützlich bei der Neuentwicklung, weil du von
der modellierten Lösung schnell zu Code kommst; die Codierung wird
dadurch für dich sogar hoffentlich bisweilen langweilig. Das ist aber auch
nützlich bei der Konfrontation mit ancient code, wo die Dokumentation
dünn ist und du niemanden mehr “von den Altvorderen” mehr fragen
²²⁹Nureinessolltestduehernicht“hinterfragen”:dasParadigmadesDatenflusses.Dazu
gehört auch der freiwillige Verzicht auf Rückflüsse (Schleifen). Das ist die Grundlage von
Flow-Design, das auf der radikalen Objektorientierung ruht. Notationelle Anpassungen
sollten sich innerhalb des Paradigmas bewegen. Wenn du aus dem Paradigma aussteigst,
dann verlässt du Flow-Design. Natürlich darfst du auch das tun; jederzeit kannst du einen
ganzanderenModellierungsansatzverwenden,z.B.Zustandsautomaten,nuristesdanneben
keinFlow-Designmehr.Aberversuchedoch,dicherstmalaufFlow-Designeinzulassen.Der
Ansatzistrechtmächtig;damitkannstduvieleModellierungsszenarienbefriedigen.


---


<!-- Page 477 of 584 -->


Musterlösung: 04-Flow-Designmit1-dimensionalenDatenflüssen 468
kannst, die ihn geschrieben haben. Wenn solcher Code (auch noch mit
automatisierten Testsgestützt) PoMO und IOSP folgt, dann hast du es viel,
viel leichter, ihn zurück in ein Konzept zu übersetzen, dort zu verstehen
und dann an neue Anforderungen anzupassen.
Aufgabe 3 - Lösen, modellieren,
implementieren
Für diese Aufgabe gibt es kein Modell und keinen PoMO/IOSP-Code als
Ausgangspunkt.DumusstselbsteinenLösungspflockindenBodenhauen,
aus dem du ein Datenfluss-Modell ableitest. Die Implementation ist dann
“nur Formsache”. Ich hoffe, es hat dir Spaß gemacht, diesen ganzen Bogen
zu spannen.
Die Anforderungen sind wieder einmal trivial. Da gibt es nicht viel zu
beachten. Es geht ja auch darum, den Prozess zu üben. Dennoch und
gerade dabei ist natürlich Sorgfalt angebracht.
Lösungsansatz
Was lässt sich bei diesem Problem an Lösungsansatz formulieren? Liegt
dernichtschonaufderHandunddukannstsofortineinModellspringen?
Ich bin anderer Meinung. Es lohnt sich, über den Lösungsansatz nachzu-
denken und ihn zumindest kurz zu formulieren.
Diese Aufgabe findest du abgespeckt im Internet unter dem Stichwort
codekata mitdemNamen“wordwrap”.MeinerEinschätzungnachleiden
viele der vorgestellten Lösungen jedoch darunter, dass sie eben keinen
Lösungsansatzformulierthaben.SiestürzensichmitTest-DrivenDevelop-
ment einfach ins Getümmel. Da kommt dann lauffähiger und auch noch
getesteter Code heraus - nur finde ich den nicht sehr verständlich. Als
Beispiel eine Java-Lösung von Robert C. Martin²³⁰:
²³⁰https://thecleancoder.blogspot.com/2010/10/craftsman-62-dark-path.html


---


<!-- Page 478 of 584 -->


Musterlösung: 04-Flow-Designmit1-dimensionalenDatenflüssen 469
1 public class Wrapper {
2 public static String wrap(String s, int col) {
3 return new Wrapper(col).wrap(s);
4 }
5
6 private int col;
7
8 private Wrapper(int col) {
9 this.col = col;
10 }
11
12 private String wrap(String s) {
13 if (s.length() <= col)
14 return s;
15 int space = (s.substring(0, col).lastIndexOf(' '));
16 if (space != -1)
17 return breakLine(s, space, 1);
18 else if (s.charAt(col) == ' ')
19 return breakLine(s, col, 1);
20 else
21 return breakLine(s, col, 0);
22 }
23
24 private String breakLine(String s, int pos, int gap) {
25 return s.substring(0, pos) + "\n" + wrap(s.substring(pos + gap), col);
26 }
27 }
Verstehst du das? Siehst du den Lösungsansatz? Was könnte den charak-
terisieren?
Für mich besteht der Lösungsansatz aus zwei Aspekten:
• Der umzubrechende Text - der hier nur aus einer Zeile bestehen
darf - wird bei Bedarf zerbrochen. Bedarf liegt vor, wenn die Zeile,
die gerade erzeugt wird, zu lang wird.
• Die Lösung geht rekursiv vor.
Diesen Lösungsansatz habe ich reverse designed aus dem Code. Ich habe
interpretiert, was ich sehe. Interessant ist dabei, dass der Begriff Wort aus
den Anforderungen - die Kata heißt “word wrap” - nicht vorkommt. Ich
kanndasKonzeptWort imCodenichtfinden.InsofernsolltedieKataeher
“line break” heißen; dazu würde die Implementation passen.
Je weniger du den Code verstehst, je weniger dir ein Lösungsansatz
klar ist, desto weniger kannst du überblicken, ob der Code das Problem
vollständig korrekt löst. Zum Beispiel hat der Code ein Problem mit
dem Text “ab c d”, wenn die maximale Zeilenlänge 4 ist. Die erste Zeile
des umgebrochenen Textes sollte dann lauten “ab c” - doch sie lautet
nur “ab”. Wer hätte das gedacht? Wo liegt dafür das Problem im Code?
Hilft dir meine Formulierung des Lösungsansatzes bei der Fehlersuche?


---


<!-- Page 479 of 584 -->


Musterlösung: 04-Flow-Designmit1-dimensionalenDatenflüssen 470
Wahrscheinlich nicht. Besser wäre ein Lösungsansatz vom Autor des
Codes - oder verständlicherer Code.
Aber einerlei. Ich wolltedir ja erstmal nur einen Eindruck davon verschaf-
fen, was ich bei solch einer Aufgabe unter Lösungsansatz verstehe: eine
skizzenhafte Beschreibung des Vorgehens.
Für die Aufgabe, wie ich sie formuliert habe, könnte das so aussehen:
• Textdatei als Abfolge von Worten verstehen. Dabei geht vorhande-
ner Whitespace verloren.
• Worte, länger als die max. Zeilenlänge, können verstanden werden
als Abfolgen von Worten maximaler Zeilenlänge.
• Worte zu Zeilen passender Länge zusammenfassen. Dabei werden
sie durch einfache Leerzeichen getrennt.
• Worte rekursiv verarbeiten.
Dass zunächst die Kommandozeile analysiert werden muss und der Text
zu laden ist und am Ende die Zeilen ausgegeben werden, ist Kleinkram,
der hier nicht der Erwähnung lohnt. Der Lösungsansatz “springt in die
Mitte der Handlung”, die Domäne. Motto: Cut to the chase.
DieanderenVerantwortlichkeitendrumherumbildeneinensimplenFluss.
Wie der Prozess für den konkreten Textumbruch aussieht, ist hingegen
nicht so klar. Deshalb mache ich mir grundsätzliche Gedanken dazu, die
sehr deklarativ sind. Ich beschreibe noch nicht mal einen Fluss, sondern
nur Aspekte.
Diese Aspekte sollten später im Modell natürlich auftauchen. Begriffe, die
imLösungsansatzvorkommen,solltendarinzufindensein,z.B.Wort oder
Zeile.
An diesen Begriffen siehst du auch schon, dass mein Lösungsansatz ein
anderer ist als der von Robert C. Martin. Bei mir stehen Worte im Kern,
bei ihm Zeilen.
Modell
Für das Modell muss ich konkreter werden. Jetzt gilt es, auch das Drum-
herum zu präzisieren. Zunächst mal eine grobe Liste dessen, was getan
werden muss:


---


<!-- Page 480 of 584 -->


Musterlösung: 04-Flow-Designmit1-dimensionalenDatenflüssen 471
• Worte zu neuen Zeilen zusammensetzen
• Zeilen ausgeben
• Text in Worte zerlegen
• Text aus Datei laden
• Kommandozeile analysieren
• Lange Worte zerlegen
In der Reihenfolge sind mir die Verantwortlichkeiten eingefallen. Jetzt gilt
es sie zu ordnen und mit Ein-/Ausgaben zu versehen. Indem ich das Punkt
für Punkt tue, achte ich auf das PoMO. Jede Funktionseinheit soll für sich
Sinn machen.
1. Kommandozeile analysieren(args): (dateiname, max. Zeilenlänge)
2. Text aus Datei laden(dateiname): text
3. Text in Worte zerlegen(text): wort*
4. Lange Worte zerschneiden(wort*, max. Zeilenlänge): wort’*
5. Worte zu neuen Zeilen zusammensetzen(wort’*, max. Zeilenlänge):
zeile*
6. Zeilen ausgeben(zeile*)
Das passt alles zusammen, würde ich sagen: Daten, die downstream als
Input gebraucht werden, werden upstream als Output erzeugt; es fehlt
nichts und es ist auch nichts übrig.
Ein paar Worte aber noch zu Details dieser Datenfluss-Skizze:
- Die “Pascal Syntax”, bei der der Resultatstyp am Ende einer Funktions-
signatur steht, habe ich benutzt, weil auf diese Weise der Input vor dem
Output steht. Das finde ich besser lesbar.
• DasSternchen*fürMengenhabeichhierauchimTextgeschrieben,
weil es mir erspart, mich für einen Mengentyp zu entscheiden. Ich
weiß einfach, dass z.B. nicht nur ein Wort, sondern viele aus Text
in Worte zerlegen() herausfließen sollen.
• In Lange Worte zerlegen() fließen Worte hinein und wieder
heraus. Das sind teilweise dieselben Worte, manche sind aber erst
durch Zerlegung von langen Worten entstanden. Um anzuzeigen,
dass es nicht dieselben Worte sind, habe ich die Ausgabe mit einem
Strich versehen: wort'*. Sie ist ähnlich, basiert auf der Eingabe, ist
aber nicht 1:1 die Eingabe.


---


<!-- Page 481 of 584 -->


Musterlösung: 04-Flow-Designmit1-dimensionalenDatenflüssen 472
• Die kursiven Verben in den Beschreibungen der Schritte will ich im
Modell benutzen. Sie sind kurz und knapp und sprechend zugleich.
Damit spare ich mir etwas Platz und Aufwand.
Bevor ich das Modell zeichne, noch ein kurze Überlegung: Was ist mit der
Rekursion? Der Lösungsansatz spricht davon, aber in der Lösungsskizze
taucht sie nicht auf. Wie kommt das? Die Rekursion ist unterhalb des
Radars eines Datenfluss-Diagramms. Sie ist ein algorithmisches Detail
einer Funktionseinheit. Relevant ist es für Worte zu Zeilen zusam-
mensetzen(). Irgendwie wird die Implementation dafür wohl rekursiv
sein-dochwederupstreamnochdownstreammerkenFunktionseinheiten
davon etwas.²³¹
Ohne Not, die Rekursion darzustellen, sollte ist das Modell keine Überra-
schung:
In der Notation habe ich mir eine kleine Freiheit genommen, indem ich
den senkrechen Strich zur Trennung von Output und Input durch man-
chen Pfeil gezogen habe (z.B. zwischen analysieren() und laden()).
²³¹EsgibteinespezielleNotationfürRekursionimFlow-Design,dochdiefindeichnicht
so wichtig. Später gehe ich aber nochmal darauf ein, wie du Rekursionen und auch andere
FormenvonWiederholungenimModellsichtbarmachenkannst.


---


<!-- Page 482 of 584 -->


Musterlösung: 04-Flow-Designmit1-dimensionalenDatenflüssen 473
Das soll wieder ein Beispiel dafür sein, dass Kreativität erlaubt und
gewünscht ist. Im konkreten Fall habe ich zu diesem Mittel gegriffen, um
mir das Zeichnen auf dem iPad etwas einfacher zu machen. Die Stiftdicke
im Verhältnis zur Blattbreite ist so, dass ich den Datenfluss nicht so gut in
die Breite ziehen kann. Deshalb ist er auch umgebrochen und mäandriert
von oben nach unten.
AndererseitshabeichdieNotzurTugendgemachtunddieFlussabschnitte
bewusst gewählt. Die Domäne ist konzentriert auf die mittleren beiden
Abschnitte; drumherum ist “Infrastruktur”. Das vertiefen wir später bei
der Modularisierung aber nochmal.
Mit dem Modell steht mir die Lösung visuell, greifbar, übersichtlich vor
Augen. Kommt sie mir immer noch plausibel vor? Ich habe mich jetzt in
vier Schritten angenähert. Ja, ich denke, das passt so. Ich bin bereit für die
Codierung.
Codierung
Jede Funktionseinheit im Modell wird wieder zu einer Funktion. Lang-
weilig, oder? Und wieder kann ich mich guten Gewissens für statische
Funktionen entscheiden. Keine kapselt einen Zustand.
Die Integration übernimmt wie gewohnt Main():
1 static void Main(string[] args) {
2 var (dateiname, maxZeilenlänge) = Analysieren(args);
3 var text = Laden(dateiname);
4 var worte = Zerlegen(text);
5 worte = Zerschneiden(worte, maxZeilenlänge);
6 var zeilen = Zusammensetzen(worte, maxZeilenlänge);
7 Ausgeben(zeilen);
8 }
Dieses Mal geschieht die Analyse der Kommandozeile nicht über ein
“echtes” Objekt. Das hat keinen tieferen Sinn. Oder wenn, dann hat es
damit zu tun, dass wir die Modularisierung noch nicht besprochen haben.
Die worte überschreibt die Integration mit dem Zerschneiden(). Die
erste Zerlegung wird nicht mehr gebraucht. Eine spezielle Variable für
wort'* habe ich mir also gespart.
Ansonsten keine Überraschungen in der Integration, würde ich sagen.


---


<!-- Page 483 of 584 -->


Musterlösung: 04-Flow-Designmit1-dimensionalenDatenflüssen 474
Und die Implementationen der Funktionseinheiten? Das sind alles Opera-
tionen.DerenLogikistweniginteressant.InC#sindesvieleEinzeiler,weil
die Sprache gute Abstraktionen bietet. Nur das Zusammensetzen lohnt
vielleicht herausgehogen zu werden, weil dort die Rekursion steckt:
1 private static IEnumerable<string> Zusammensetzen(IEnumerable<string> worte,
2 int maxZeilenlänge) {
3 return Zusammensetzen(new List<string>(worte), new List<string>());
4
5
6 IEnumerable<string> Zusammensetzen(List<string> verbleibendeWorte,
7 List<string> zeilen) {
8 if (verbleibendeWorte.Count == 0) return zeilen;
9
10 var zeile = "";
11 while (verbleibendeWorte.Count > 0) {
12 var tempZeile = zeile + (zeile.Length > 0 ? " " : "")
13 + verbleibendeWorte[0];
14 if (tempZeile.Length > maxZeilenlänge)
15 break;
16
17 zeile = tempZeile;
18 verbleibendeWorte.RemoveAt(0);
19 }
20 zeilen.Add(zeile);
21
22 return Zusammensetzen(verbleibendeWorte, zeilen);
23 }
24 }
Das ich mir hier lokale Funktionen zunutze gemacht habe, ist ein Imple-
mentationsdetail. Die innere, sich wirklich rekursiv aufrufende Funktion
hätte auch neben der äußeren stehen können. Aber mit der Schachtelung
verberge ich das Implementationsdetail Rekursion und spare mir die ma-
xZeilenlänge als Parameter innen, weil sie über eine closure verfügbar
ist.
Die äußere Funktion Zusammensetzen() stößt die Rekursion mit ei-
nem zusätzlichen Parameter für die zu sammelnden Zeilen. Das ist ein
Implementationdetail und soll nicht nach außen sichtbar sein; deshalb
gibt es zwei Funktionen. Damit ist die äußere Funktion selbst auch eine
Integration; sie enthält keine Logik.
Die innere Funktion leistet rekursiv das Zusammensetzen der Zeilen. Sie
isteineOperation;darinfindetsichdieganzeLogik.Allerdings…amEnde
ruft sie sich selbst auf. Ist das nicht ein Widerspruch zum IOSP? Ganz,
ganz streng genommen ist es das. Aber das ist eine “lässliche Sünde”. Dem
Charakter als Operation wird kein Abbruch getan. Die Verständlichkeit
und Testbarkeit sinken dadurch nicht. Das ist das Wichtigste! Der Effekt
steht immer über dem Prinzip. Wenn der Effekt einer Gebotsübertretung
nicht gravierend ist, dann ist das ok. Im nächsten Kapitel wirst du dafür


---


<!-- Page 484 of 584 -->


Musterlösung: 04-Flow-Designmit1-dimensionalenDatenflüssen 475
noch ein Beispiel sehen; wieder wird es mit der Wiederholung von Logik
zu tun haben.
Wenn dich solche Unsauberkeit durch die Rekursion aber stört, kannst du
sie natürlich vermeiden und immer durch eine Schleife ersetzen. Ich fand
die Rekursion aber naheliegend(er): Eine Zeile wird aus den verbliebenen
Worten zusammengesetzt, die dadurch Wort für Wort reduziert werden.
Wenn eine Zeile voll ist, wird sie registriert - und der Prozess beginnt von
vorne mit dem nun verbliebenen Worten. Das ist für mich ein typisches
Rekursionsszenario.
Die Logik meiner Lösung erfüllt die Akzeptanztestfälle des Auftraggebers
und auch den Sonderfall, der dem obigen Java-Code durch die Lappen
geht. Dafür braucht der vergleichbare Codeanteil ca. 38 Zeilen statt
der 27 des Java-Codes. Das sind ca. 40% mehr, doch ich finde die gut
aufgewandt. Die Verständlichkeit ist deutlich besser durch Einhaltung
von PoMO und IOSP. Und auch die Testbarkeit finde ich höher, selbst
wenn der Java-Code mit TDD vorangetrieben wurde. Doch dazu mehr
in meinem Buch Test-first Codierung. Die höhere Testbarkeit steckt für
mich in der stärkeren Isolation von Logik nach Verantwortlichkeiten von
vornherein durch den Entwurf. Beim Java-Code ist Logik einzig durch
spätere Refaktorisierungsschritte entstanden. Darauf zu vertrauen, finde
ich aber risikoreich. Ordnung lässt sich nur bedingt nachträglich in Code
hineinrefaktorisieren. Ich bin ein Freund davon, den Code von Anfang an
durch Entwurf “grundsauber” zu schreiben. Dafür hat das Modell gesorgt.
Reflexion
Die Herausforderung bei dieser Aufgabe war, dass das “Produkt” vor der
Codierung wirklich komplett “vorausgedacht” werden sollte. Ich habe
dich zu einem Wasserfall verführt. Weil du den ja aber in 60-90 Minuten
durchschwimmenkonntest,halteichdasfürkeinProblem.Tage-oderwo-
chenlange Wasserfälle sind gar keine gute Idee. Aber mal für 1-2 Stunden
Schritten sequenziell zu folgen, ist kein Ding, sondern eben vorteilhaft.
Der Ordnung im Code ist das zuträglich. Zu früh mit der Codierung zu
beginnen führt zu Unordnung oder belastenden Refaktorisierungen. Das
kostet am Ende mehr Zeit als du meinst, sparen zu können.
Aber wahrscheinlich war es ungewohnt, ein solches Problem so formal
anzugehen. Es fühlt sich algorithmisch an und ist es auch im Kern.


---


<!-- Page 485 of 584 -->


Musterlösung: 04-Flow-Designmit1-dimensionalenDatenflüssen 476
Dennoch ließen sich hier sequenzielle Teile identifizieren und in einen
Fluss bringen. Dadurch steigt die Übersichtlichkeit und die Codierung
wird einfacher. Lass dich also nicht zu schnell durch “Algorithmen” erden.
Die sind in diesem Beispiel in zwei Funktion(seinheit)en gekapselt: Zer-
schneiden() und Zusammensetzen() enthalten den Löwenanteil Lo-
gik. Die richtig hinzubekommen ist vielleicht auch nicht ganz einfach.
Besser jedoch, dass du dich genau darauf konzentrieren kannst, indem du
diese Funktionen in der Hand hast und automatisierte Tests daran gezielt
anlegen kannst, also dass die Logik “irgendwo herumschwirrt”.
Den Gesamtalgorithmus der Domänenlogik in eine Sequenz zu bringen,
sollte dich bei dieser Aufgabe also etwas anspannen. Es galt, eine Balance
zu finden zwischen Datenfluss und gekapseltem Kontrollfluss.


---


<!-- Page 486 of 584 -->


Musterlösung: 05 -
Flow-Design mit
2-dimensionalen
Datenflüssen
Aufgabe 1 - Implementation eines
Modells
Für dich ist es vielleicht etwas schwieriger als für mich, dass Modell für
das Diamantenwachstum zu implementieren, weil es nicht dein Modell
ist. Du musst dich erst eindenken in meinen Entwurf. Würde ich neben
dir sitzen und dich nochmal durch das Modell leiten oder du könntest mir
kurz Fragen stellen, wäre das kaum der Rede wert. Doch allein gelassen
mit einem Modell zu sein, macht die Sache etwas zäher.
Das ist hier nicht schlimm, denke ich. Die Sache ist ja trivial, das Modell
sehr überschaubar. Dennoch diese kurze Anmerkung, um dich zu sensi-
bilisieren: Glaub nicht, dass nur, weil du jetzt anfängst zu modellieren,
Lösungen anderen “über den Zaun geschmissen werden können”. Eine
Übergabe sollte immer im Dialog stattfinden; noch besser, die Entwick-
lung fand schon zusammen statt. Implementierer sollten an der Modellie-
rung beteiligt sein. Wenn du beides in einer Person bist - Designer und
Codierer -, ist das ohnehin kein Problem. Wenn du hingegen im Team
arbeitest, versuch aktiv, die anderen mit einzubeziehen. Collective design
ownership ist das Motto.
Aber jetzt ans Werk der Codierung!
Für mich ist das wie Abschreiben. Ich gehe die Datenflusshierarchie von
oben nach unten breadth-first durch. Das heißt, bei einer Integration
verbinde ich zuerst alle Funktionseinheiten, so dass ich im Code schon
den Fluss sehe.


---


<!-- Page 487 of 584 -->


Musterlösung: 05-Flow-Designmit2-dimensionalenDatenflüssen 478
1 public static void Main(string[] args) {
2 var größe = Finden(args);
3 var diamant = Wachsen(größe);
4 Präsentieren(diamant);
5 }
Dann erst mache ich einen drill-down entlang des Flusses und erzeuge
die Methoden. Zunächst alle ohne Inhalt, um die Signaturen zügig zu
bekommen. Dann fülle ich nur die Integrationen in gleicher Weise aus.²³²
Zunächst bleiben also z.B. Finden() und Präsentieren() leer; Wach-
sen() bekommt aber seinen Fluss.
1 private static char Finden(string[] args)
2 => args[0][0];
3
4 private static string Wachsen(in char größe) {
5 var schichten = Generieren(größe);
6 return Pressen(schichten);
7 }
8
9 private static void Präsentieren(string diamant) {
10 Console.WriteLine(diamant);
11 }
Als nächstes sind also die Methoden in Wachsen() dran. Pressen() als
Operationbleibtungefüllt,aberGenerieren()spanntseinenDatenfluss
auf:
1 private static IEnumerable<string> Generieren(in char größe) {
2 var schichtendefinitionen = Aufspannen(größe).ToArray();
3 return Aufschichten(schichtendefinitionen);
4 }
5
6 private static string Pressen(IEnumerable<string> schichten)
7 => string.Join("\n", schichten);
Damit sind alle Integrationen des Modells am Start. Der gesamte Daten-
fluss existiert in Form von Funktionsrümpfen und ist schon vollständig
“verdrahtet”.
Jetzt erst gehe ich durch die Operationen. Meistens fange ich mit dem
Einfachen/Kurzenan.DassinddieFunktionen,dieschonmitLogikgefüllt
oben siehst. Solche “Einzeiler” müssten auch nicht getestet werden.
²³²WennduhierschonLogikindenOperationensiehst,dannistdasnurmeinerBequem-
lichkeitgeschuldetundsolldenTextetwaskürzerhalten.DieseLogiklasseichzunächstwirk-
lich aus. Es steht in den Operationen lediglich so viel drin, dass der Compiler keinen Fehler
meldet.InC#erreicheichdasz.B.mitthrows new NotImplementedException().


---


<!-- Page 488 of 584 -->


Musterlösung: 05-Flow-Designmit2-dimensionalenDatenflüssen 479
Aber die sind in der Realität wohl eher selten. Früher oder später sind also
Mehr- und Vielzeiler dran.
Das Aufspannen() wollte ich als erstes hinter mich bringen. Nach den
ganz einfachen Funktionen habe ich also für das Herzstück entschieden.
Die Logik dafür war nicht wirklich schwierig, aber doch etwas aufwendi-
ger als gedacht.
1 private static IEnumerable<Schichtendef> Aufspannen(char größe) {
2 var anzahlObereSchichten = (int) char.ToUpper(größe) - (int) 'A';
3
4 var schichtenindizes = new List<int>(Enumerable.Range(1, anzahlObereSchichten));
5 schichtenindizes.Add(anzahlObereSchichten+1);
6 schichtenindizes.AddRange(Enumerable.Range(1, anzahlObereSchichten).Reverse());
7
8 foreach (var index in schichtenindizes)
9 yield return new Schichtendef {
10 Breite = index*2-1,
11 Kennung = (char)((int)'A'-1+index)
12 };
13 }
Während der Modellierung hatte ich vor meinem geistigen Aufge nur
die Schleife (Zeilen 8..12). Bei gegebenen Schichtenindizes schien mir die
trivial. Doch in der Codierung stellte sich heraus, dass ich unsicher war,
wieichinC#ambestendieBuchstabenreihenfolgeerzeuge.Sollteichüber
Buchstaben iterieren und die Indizes daraus ableiten? Oder sollte ich über
Indizes iterieren und die Buchstaben/Kennungen daraus ableiten? Für die
Zeilen 2 bis 6 haben ist deshalb einen kleinen Moment länger gebraucht.
Das Aufschichten hingegen war ganz leicht, auch wenn es etwas mehr
Zeilen umfasst.
1 private static IEnumerable<string> Aufschichten(Schichtendef[] schichtendefinitionen) {
2 var maxBreite = schichtendefinitionen.Max(x => x.Breite);
3 foreach (var def in schichtendefinitionen)
4 yield return Schicht_generieren(maxBreite, def);
5 }
6
7 private static string Schicht_generieren(int maxBreite, Schichtendef def) {
8 var einzugsTiefe = (maxBreite - def.Breite) / 2;
9 var einzug = "".PadLeft(einzugsTiefe, ' ');
10
11 if (def.Breite == 1)
12 return $"{einzug}{def.Kennung}";
13 else
14 return $"{einzug}{def.Kennung}{"".PadLeft(def.Breite - 2, ' ')}{def.Kennung}";
15 }
Hier nun siehst du das Beispiel für “unsaubere” Integration in konkreter
Ausprägung: Aufschichten() enthält eine Schleife, was ja eigentlich
nicht sein darf. Doch die ist trivial und die Hauptarbeit wird pro Schicht
in Schicht_generieren() geleistet.


---


<!-- Page 489 of 584 -->


Musterlösung: 05-Flow-Designmit2-dimensionalenDatenflüssen 480
Reflexion
Bei gegebenem Modell ist die Codierung wirklich ein no-brainer. Je-
denfalls über weite Strecken. Falls ich dann aber doch mal das Hirn
anschalten muss, dann in einem sehr überschaubaren Kontext, meist nur
eine Operation. In dem Moment kann ich mich darauf verlassen, dass
der Rest schon versorgt ist. Ich kann mich ganz darauf konzentrieren, die
Logik in einer Funktion hinzubekommen. Wenn ich dafür Tests brauche,
dann kann ich die punktgenau anlegen.²³³
InnerhalbdesModellswardieVorberechnungderSchichtendef-Daten
wirklich eine gute Entscheidung zur Entzerrung der Domäne.
Aufgabe 2 - Die Dimensionalität eines
Modells erhöhen
Aus dem gewundenen Datenfluss mache ich mir zunächst einen etwas
übersichtlicheren geraden. Die Bezeichnungen der Funktionseinheiten
kürze ich darin ab:
In diesem 1-dimensionalen Datenfluss kann ich jetzt leicht Gruppen
bilden.NichtsanderessindIntegrationenja:GruppierungenvonOperatio-
nenoderauchanderenGruppierungen.NatürlichsindIntegrationenspezi-
elle Gruppierungen, sie komponieren aus den Gruppenmitgliedern etwas
wunderbar Nützliches durch Zusammenschaltung in einem Datenfluss.
Integrationen sind nicht nur “Säcke” mit einer Anzahl Funktionseinheiten
darin.
Nicht nur, denn andererseits sind sie genau das. Auch und erstmal. Und
so ziehe ich denn um das, was ich in dem 1-dimensionalen Datenfluss für
²³³EigentlichistdasVorgehennatürlichtest-first.Daraufverzichteichhiernur,weildas
Thema ein anderes ist und Tests in Bezug darauf Rauschen darstellen würden. Funktionen
wie Aufspannen() und Schicht_generieren() würde ich bei Produktionscode test-
first entwickeln.


---


<!-- Page 490 of 584 -->


Musterlösung: 05-Flow-Designmit2-dimensionalenDatenflüssen 481
näher zusammengehörig halte, schlicht eine Grenze. Sie zeigt an, dass das,
was innen liegt, untereinander eine höhere Kohäsion hat als mit etwas,
das außen liegt.
In einer ersten Variante finde ich, das Heraussuchen und Auswerten
und Deuten irgendwie eine Einheit bilden (1). Da passiert etwas sehr
anderes als bei Parsen oder Display. Die beiden äußeren Funktionsein-
heiten sind mit der Interaktion mit der Umwelt beschäftigt. Die inneren
Funktionseinheiten sind davon unabhängig; deshalb die Grenze (1).
Innerhalb dieser Gemeinschaft in (1) gehören vielleicht Auswerten und
Deuten nochmal enger zusammen. Sie verbindet - zusammen mit der
Datenstruktur Test - die Domäne. Heraussuchen hingegen ist mit der
Persistenz beschäftigt; das ist auch eine Form der Interaktion mit der
Umwelt.
Ja, so könnten weitere Integrationen aussehen. Das wäre nicht ganz
schlecht. Aber vielleicht geht es noch besser?
Als zweite Variante könnte ich mir vorstellen, dass doch Deuten und
Displayengerzusammengehören.In(4)sindnundieFunktionseinheiten
eingeschlossen, die sich mit der Präsentation dessen, was in (3) ermittelt
wird,beschäftigen.DasDeutenistjaeinklaresZugeständnisanBenutzer;
diewollenesbequemhabenundnichtselbsteineWahrscheinlichkeitdeu-
ten. Ändern sich die Benutzeransprüche, dann wird Deuten womöglich
überflüssig oder ändert sich stark. Das hat ja aber keinen Einfluss auf die
Domäne, in deren Kern Auswerten steht.


---


<!-- Page 491 of 584 -->


Musterlösung: 05-Flow-Designmit2-dimensionalenDatenflüssen 482
Und nicht nur Auswerten gehört zur Domäne. Der Test tut es auch.
Und der wird von Heraussuchen beschafft. Beide Funktionseinheiten
können also als zusammengehörig betrachtet werden innerhalb von (3).
Ja, vielleicht ist das wirklich ein guter Gedanke. (3) zieht einen Kreis um
einen Kern, der aus Testdatenbank und Auswertung besteht. Die Deutung
liegt da schon weiter weg; sie gehört weniger zu Auswertenals das
Heraussuchen. Das drücke ich in der dritten Variante aus, wo (6) erhält,
was (3) schon dargestellt hat, aber (5) den Gedanken von (1) aufgreift.
Die Deutung wird damit wieder enger an die Domäne gerückt. Oder
umgekehrt: Die konkrete Anzeige wird davon abgerückt, weil es dort um
harte Technologie geht.
(5) trennt die UI-Technologie vom Rest. Was in (5) zusammengefasst ist,


---


<!-- Page 492 of 584 -->


Musterlösung: 05-Flow-Designmit2-dimensionalenDatenflüssen 483
kann hinter ganz verschiedenen Frontends zum Einsatz kommen.²³⁴
Ja, ich denke mit der dritten Variante bin ich zufrieden. Die transformie-
re ich in einen 2-dimensionalen Datenfluss. Dabei muss ich allerdings
Namen für die Gruppierungen finden, die ich bisher mit (5) und (6)
bezeichnet habe. Das ist nochmal eine kleine Qualitätsprüfung. Sollte ich
keine guten Namen finden können, fehlt noch etwas.
Mit Beurteilen für (5) und Berechnen für (6) bin ich ganz zufrieden.
Der Benutzer wünscht sich vermittels seiner Benutzerschnittstelle eine
Beurteilung des Testergebnisses. Und innerhalb der Beurteilung findet
zunächst eine Berechnung statt. Die Glaubwürdigkeit wird aufgrund der
Testdaten bestimmt. Dass die persistent vorliegen, ist nur ein Detail.
²³⁴Noch deutlicher wäre das, wenn Deuten aus zwei Teilen bestünde. Erstens einem
Berechnungsteil, der die Zahlen ermittelt, die im erklärenden Text stehen. Zweitens aus
einem Formulierungsteil, der die Zahlen in einen erklärenden Text verpackt. Der Berech-
nungsteil würde dann innerhalb von (5) stehen, der Formulierungsteil außerhalb und nahe
an Display. Das Berechnungsergebnis der Deutung wäre universeller einsetzbar; damit
ließe sich auch vielleicht ein Diagramm zeichnen. Die konkrete Formulierun in Form
einerZeichenkettehingegenistschonsehraufeineUI-Technologie(hier:Konsolenausgabe)
zugeschnitten.


---


<!-- Page 493 of 584 -->


Musterlösung: 05-Flow-Designmit2-dimensionalenDatenflüssen 484
Reflexion
Du siehst, ich habe mich für die Aufgabe von der Datenflussnotation
befreit. Statt alle Varianten mittels 2-dimensionaler Datenflüsse zu eva-
luieren, habe ich einfach nur ein paar “Kreise gezogen”. Das hat es mir
leichter gemacht, zu einem Urteil zu kommen. Ich habe mich nicht mit
einer Notation belasten müssen.
Als ich dann mein Urteil gefällt hatte, habe ich das Ergebnis in die
Flow-Design Notation gebracht. Diese Transformation hat mir nochmal
Gelegenheit zum Review beschert, weil ich ja Namen finden musste.
Mach dich also locker, was die Notation angeht. Erkenne vielmehr das
Muster dahinter: Es gibt immer wieder Tätigkeiten, die monotlithisch aus-
sehen,aberinWirklichkeitausmehrerenTeilen/Phasenzusammengesetzt
sind.GeradeinderEntwicklungvonetwassinddaseineKreativitätsphase
und dann eine Konkretisierungsphase. In Ersterer geht es um Weitung des
Blicks,umExploration;inLetzterergehtesumEinengung,Konzentration.
Während der Kreativität willst du wenig durch Regeln oder Notationen
eingeschränkt sein; die Konzentration hingegen läuft auf konkrete Formu-
lierung in einer Notation hinaus. Von dort kann dann wieder etwas Neues
beginnen.
Außerdem erkenne, dass auch Modellierung innerhalb des Entwurfs ein
Entwicklungsprozess ist. Der ist nicht geradlinig. Du kommst nicht (im-
mer) sofort auf das endgültige (und schon gar nicht beste) Modell. Du
versuchst es vielmehr zuerst mit dem einen, siehst (!), dass es irgendwie
noch nicht stimmig ist, und probierst etwas anderes. Das Sehen, d.h. dass
du eine Idee vor dir auf dem Papier (oder iPad) hast, ist dabei wichtig.
Dadurch kannst du zwei Varianten nämlich vergleichen: eine sichtbare,
konkreteundeineunsichtbare,schwammigeindeinemKopf.Sokannstdu
einen Dialog mit dir selbst führen und dich über die durch Visualisierung
entstehenden Kontraste voranziehen.
Dass du Kontrast spürst und wie fein oder grob die sind, ist allerdings
Übungssache. Damit ein solches Vorgehen seinen Nutzen entfaltet, musst
du dran bleiben. Austausch mit anderen hilft auch, deinen Kontrastdetek-
tor zu sensibilisieren.


---


<!-- Page 494 of 584 -->


Musterlösung: 05-Flow-Designmit2-dimensionalenDatenflüssen 485
Aufgabe 3 - Anforderungen umsetzen
mit 2-dimensionalem Modell
Jetzt wieder alles zusammen: von den Anforderungen bis zum Code
müssen alle Phasen durchlaufen werden. Aber zum Glück sind die An-
forderungen einfach und die Interaktion mit dem Benutzer ist wieder aus
eine Funktion an der Spitze einer Datenflusshierarchie beschränkt.
Der Trick bei dieser Aufgabe ist, dass du dich wirklich schrittweise
voranarbeitest. Letztlich folgst du dabei auch einem Datenfluss. Jeder
Schritt im Prozess hat einen Input, den er in einen Output transformiert,
der der Input für den nächsten ist. Die fließenden Daten (Substantive)
sind:
• Anforderungen
• Lösungsansatz
• Modell
• Code
Die Prozessschritte (Verben) sind:
• Lösen
• Modellieren
• Codieren
Oder mit etwas mehr Integration und Differenzierung:
• Entwerfen
– Lösen
– Modellieren
* Zerlegen
* Verdrahten
• Codieren


---


<!-- Page 495 of 584 -->


Musterlösung: 05-Flow-Designmit2-dimensionalenDatenflüssen 486
Du arbeitest in einem Datenfluss und stellst Datenflüsse her. Das zu
erkennen, war während der Entwicklung von Flow-Design für mich
ein Beleg für die Tauglichkeit der Methode. Wir Menschen arbeiten in
(Produktions)Prozessen, die nichts anderes sind als “Produktflüsse”.²³⁵
Warum sollte Software nicht genauso organisiert sein? Sie stellt ja auch
etwas her.
Verstehen
Als Aufschlag zunächst eine Vergewisserung, dass ich die Anforderungen
verstanden habe. Es geht um die Analyse von Quellcodedateien. Die
stehen in einem Verzeichnisbaum in beliebiger Tiefe, z.B.
1 src/
2 frontend/
3 main.java
4 validation.java
5 validinput.txt
6 backend/
7 domain/
8 process.java
9 data.java
10 rules.json
11 persistence/
12 repository.java
Zu finden wären z.B. alle .java-Dateien (hier: 5 Dateien), nicht aber
.txt- oder .json-Dateien.
Und in diesen Quellcodedateien sollen nur ganz bestimmte Zeilen gezählt
werden. Das Programm kann die Dateien zwar zeilenweise lesen, nur
sind dann nicht alle Zeilen relevant für das Ergebnis. Leerzeilen und
Kommentarzeilen sind auszuschließen. In den Anforderungen ist ein
Beispiel dafür.
Pro Aufruf analysiert das Programm einen Verzeichnisbaum und gibt nur
summarische Information aus.
²³⁵Oder nenn es auch workflow oder value chain oder value stream, wenn dir das
passenderfürdieArbeitswelterscheint.


---


<!-- Page 496 of 584 -->


Musterlösung: 05-Flow-Designmit2-dimensionalenDatenflüssen 487
Ich sehe zwei Probleme:²³⁶
• Ein technisches: die Sammlung der Dateien im Verzeichnisbaum.
• Ein inhaltliches: die Erkennung mehrzeiliger Kommentare.
DaichdasalsProblemeidentifiziere,mussdieLösungdafürFunktionsein-
heiten aufweisen, die die Verantwortlichkeit haben, genau diese Probleme
zu lösen. Das SRP lauert überall!
Lösen
Die Anforderungsanalyse hat schon zwei funktionale Strukturelemente
herausgearbeitet:
• Sammeln aller relevanten Dateien
• Analysieren der Dateien auf Relevantes hin. Und sogar noch genau-
er: die Nichtbeachtung von mehrzeiligen Kommentaren.
Im Lösungsansatz möchte ich nur in Bezug auf die Domäne darüber
hinausgehen. Mir scheint es sinnvoll zu überlegen, wie ich die “Nichtbe-
achtung” des Irrelevanten bewerkstelligen kann.
²³⁶Ich bin immer wieder versucht, Herausforderung statt Problem zu schreiben. Das
klänge irgendwie zeitgemäßer, weniger bedrohlich. Meistens muss ich mich jedoch zur
Räson rufen. Herausforderung passt schlicht nicht. Herausforderungen und Probleme sind
beide Hürden. Die Begriffe sind für mich deshalb allerdings nicht austauschbar. Man
sollte nicht Herausforderung sagen, weil das modern ist. Der Unterschied zwischen den
Hürden ist für mich ganz klar:Herausforderungen sind Hürden, die kann ich umgehen. Ich
muss Herausforderungen nicht annehmen; sie sind lediglich Einladungen, sich mit etwas
intensiver zu beschäftigen, eben eine Hürde zu nehmen. Es geht bei Herausforderungen
aberauchohne.Einfachignorieren,drumherumgehen.ProblemehingegensindHürden,die
müssen genommen werden. Um Probleme kann man nicht herum gehen. Probleme stellen
Forderungen; sie müssen gelöst werden. Ein triviales Beispiel: Meine Schuhe zu schließen,
isteinProblem.(Zumindest,wennichmitSchuhenrausgehenundnichtandauerndstolpern
will.)MeineSchuhenurmiteinerHandzuschließen,isthingegennureineHerausforderung.
Insofern sind auch die Probleme hier wirklich Probleme und keine Herausforderungen:
Die Dateien müssen gesammelt und mehrzeilige Kommentaren müssen erkannt werden.
(Zumindest, wenn du das Programm schreiben willst. Das zu tun, ist für dich allerdings
nureineHerausforderung;dumusstdieÜbungsaufgabenichtlösen.)


---


<!-- Page 497 of 584 -->


Musterlösung: 05-Flow-Designmit2-dimensionalenDatenflüssen 488
• Zunächstscheintesmirsinnvoll,dieunterschiedlichenIrrelevanten
nicht “auf einem Haufen” beurteilen zu wollen. Das könnte alles in
einer Schleife über die Zeilen einer Datei untersucht werden. Doch
dann wäre die Schleife sehr umfangreich. Ich bin dafür, dass Leer-
zeichen getrennt von 1- und mehrzeiligen Kommentaren behandelt
werden. Das Ergebnis wäre eine Filter-Pipeline. Der könnte man
jederzeit weitere Filter hinzufügen oder einen Filter durch einen
verbesserten ersetzen.
• Und den Filter verstehe ich als Sieb, in dem etwas hängenbleibt.
Er filtert etwas heraus. Das bedeutet, wenn Quellcode durch den
Leerzeilenfilter gelaufen ist, dann enthält er keine Leerzeilen mehr.
DitofüralleanderenFilter.MitjedemFilterschrumpftderQuellzei-
lenumfang einer Datei. Sie wird durch die Filter-Pipeline auf ihre
Nettozeilen reduziert. Deren Anzahl muss am Ende nur abgelesen
werden.
Ein Lösungsansatz ist dadurch gekennzeichnet, dass er Entscheidungen
enthält. Er fokussiert auf eine Option unter Vernachlässigung anderer
Optionen. Die Pipeline-Idee entscheidet sich gegen den monolithischen,
mehr algorithmischen Ansatz. Die Sieb-Idee entscheidet sich gegen den
Fokus auf das Relevante; Filter konzentrieren sich auf das Irrelevante, das
sie zurückhalten/löschen.
Modellieren
Der Lösungsansatz ist grob. Für ein konkretes Modell muss ich ihn zuerst
verfeinern. Die Idee muss in einer Struktur manifestiert werden.
Zerlegen
Bei der Zerlegung finde ich die Verantwortlichkeitsbereiche. Was ist von
was zu trennen? Welche Entscheidungen gilt es zu repräsentieren?
In den Anforderungen stecken Entscheidungen zu den Aspekten…
• Benutzerschnittstelle: Wie kommen Parameter ins Programm und
wie kommen Ergebnisse hinaus?


---


<!-- Page 498 of 584 -->


Musterlösung: 05-Flow-Designmit2-dimensionalenDatenflüssen 489
• Datenherkunft: Woher kommen die Daten, die zu analysieren sind,
und wie werden sie beschafft?
• Analysekriterien: Welche Daten sind zu berücksichtigen bzw. wel-
che nicht?
Wenn ich das ein wenig ordne, komme ich z.B. auf diesen Verantwortlich-
keitsbaum:
• Auf der obersten Ebene sind genannten Aspekte repräsentiert.
• Aufgrund meiner Plattformerfahrung entscheide ich, dass alle As-
pekte außer der Analyse trivial zu implementieren sind. Eine Ver-
feinerung lohnt nicht. Hervorhebenswert ist hier nur Sammeln: Je
nach Programmiersprache bzw. Standardbibliothek kann es sich
lohnen, diesen Aspekt weiter zu zerlegen. In C# jedoch ist sowohl
dieBestimmungderrelevantenDateienwiedasLadenihrerInhalte
ein Einzeiler. Ein rekursiver Abstieg durch den Verzeichnisbaum
muss nicht von Hand implementiert werden.
• DieAnalysezerfälltfürmichnochmalinFilter-Anteil(Bereinigen)
und die Ergebnisbestimmung.
• Und im Filter-Anteil liste ich die auf der Hand liegenden Filter.


---


<!-- Page 499 of 584 -->


Musterlösung: 05-Flow-Designmit2-dimensionalenDatenflüssen 490
Verdrahten
Mit dem Lösungsansatz habe ich die Lösung grob visualisiert. Was mir
im Kopf herumgewabert ist, hat jetzt eine konkrete Form. Darauf kann
ich aufbauen und die Funktionseinheiten “in Reihe schalten” in einem
Datenfluss-Modell:
Wie du siehst, unterscheidet sich das Modell überraschend vom Zerle-
gungsbaum. Dass es plötzlich Datenflüsse gibt, ist natürlich nicht über-
raschend. Auch nicht, dass ich einen eigenen Datentypen Datei heraus-
gezogen habe.
• Überraschend ist zum einen, dass es eine weitere Integration gibt.
Verarbeiten habe ich eingezogen, weil mir im Fluss zu viel auf
der ersten Integrationsebene passiert ist. Dort mag ich einen drei-
schrittigen Progess: Eingabe lesen (Parsen), Eingabe verarbei-
ten,Ausgabeanzeigen.DiesesMusterkannichdirauchansHerz
legen. Wenn du danach Ausschau hältst, kannst du es oft finden/an-
wenden und damit einen Datenfluss schneller begreifbar machen.
Parsen und Anzeigen sind wie Klammern um Verarbeiten.
Das gibt es auch bei anderen Aspekten wie z.B. (De)Serialisierung,
Ver-/Entschlüsselung, Laden/Speichern.


---


<!-- Page 500 of 584 -->


Musterlösung: 05-Flow-Designmit2-dimensionalenDatenflüssen 491
• Überraschend ist auch, dass ich nun doch das Sammeln weiter zer-
legt habe. Selbst wenn die Codierung für das Finden und Laden der
Dateien simpel ist, stecken darin doch Entscheidungen, die anders
ausfallen könnten. Beispielsweise könnten sich die Kriterien für
relevanteDateienändern(z.B.mehrereDateitypen,Ausschlussliste)
oderweitereDatenjeDateigeladenwerden(z.B.Dateiname,letztes
Änderungsdatum). Das hört sich zunächst vielleicht weit hergeholt
an… Ja, vielleicht und ich möchte dir auch keine vorzeitige Opti-
mierung in Richtung “beliebiger” Erweiterbarkeit empfehlen. Was
für mich aber dafür spricht, diese Funktionseinheiten zu extrahie-
ren, das sind die deutlich sichtbaren Entscheidungen, die dahinter
stehen. Die zu erkennen, ist kein Glaskugel nötig, sondern nur
ein gutes Auge. Die Definition relevanter Dateien ist eine klare
Entscheidung, die etwas einschließt und anderes ausschließt. Die
Einführung des Datentyps Datei steht für die Entscheidung, was
genau geladen werden soll und dass dafür ein Container sinnvoll
erscheint, der Raum für Wachstum bietet.²³⁷
Codieren
Die Codierung des Modells ist weitgehend geradlinig. Die Operationen
sindweniginteressantweilplattformspezifisch-miteinerAusnahme,wie
du unten sehen wirst.
Immer wieder sehenswert finde ich ja aber die Integrationen. Dafür ist
das IOSP gemacht: Code übersichtlich machen ohne die “Verknotungen”
durch Logik.
²³⁷Hier denke ich allerdings vor allem an Datenwachstum. Dass Funktionalität wie die
Filterungdorthinwandert,seheichnicht.DassähevielleichtObjektorientiertaus,wäreaber
nurschwerzuerweiternbeineuenFiltern.Nein,dieFiltermüssendabeigetrenntbleiben.


---


<!-- Page 501 of 584 -->


Musterlösung: 05-Flow-Designmit2-dimensionalenDatenflüssen 492
1 static void Main(string[] args) {
2 var pfad = Parsen(args);
3 var (dateienzahl, nettozeilenzahl) = Verarbeiten(pfad, "java");
4 Anzeigen(dateienzahl, nettozeilenzahl);
5 }
6
7 private static (int dateienzahl, int nettozeilenzahl) Verarbeiten(string pfad,
8 string dateityp) {
9 var dateien = Sammeln(pfad, dateityp);
10 return Analysieren(dateien);
11 }
12
13 private static IEnumerable<Datei> Sammeln(string pfad, string dateityp) {
14 var dateinamen = Finden(pfad, dateityp);
15 return Laden(dateinamen);
16 }
17
18 private static (int dateienzahl, int nettozeilenzahl) Analysieren(IEnumerable<Datei> da\
19 teien) {
20 dateien = Bereinigen(dateien).ToArray();
21 return Zählen(dateien);
22 }
23
24 private static IEnumerable<Datei> Bereinigen(IEnumerable<Datei> dateien)
25 => dateien.LeerzeilenLöschen()
26 .EinzeiligeKommentareLöschen()
27 .MehrzeiligeKommentareLöschen();
Hervorhebenswert ist hier nur zweierlei:
• Ich habe mich entschlossen, das Kriterium für relevante Dateien -
den Dateityp, z.B. java- als Parameter hin die Verarbeitung hinein-
zureichen. Das geschieht in Main() und macht Verarbeiten()
“wiederverwendbar” für Programmiersprachen, die dieselben Kom-
mentarkonventionen teilen. Ich hätte das im Modell ausdrücken
können durch eine Konstante, die in Verarbeiten hineinfließt
- doch zu dem Zeitpunkt war ich dafür noch nicht sensibilisiert.
Als ich dann aber mit dem Dateisystem-API gearbeitet habe, hatte
ich die Idee. Eigentlich wird der Dateityp dann erst bei Finden()
gebraucht; also muss er über einige Ebenen durchgereicht werden.
• Die Filter-Pipeline in Bereinigen() habe ich mit einem fluent
interface implementiert. Das ist eine valide Übersetzung eines Da-
tenflusses, kommt ohne temporäre Variablen aus und ist hübsch zu
lesen (Zeilen 24-26). Das kommt einer Notation mit einem pipeline
operator wie | bzw. |> (F#, Kotlin) schon sehr nahe.
Allerdings hat so einfluent interface seinen Preis. Die Funktionen müssen
dafürineineeigeneKlasseausgelagertwerden.Dasistsinddieinteressan-
tenOperationen,aufdieichobenangespielthabe.HiereinBeispielfürdie
Implementation:


---


<!-- Page 502 of 584 -->


Musterlösung: 05-Flow-Designmit2-dimensionalenDatenflüssen 493
1 static class Bereinigung
2 {
3 public static IEnumerable<Datei> LeerzeilenLöschen(this IEnumerable<Datei> dateien)\
4 {
5 return dateien.Select(x => new Datei {Zeilen = LeerzeilenLöschen(x.Zeilen)});
6
7 IEnumerable<string> LeerzeilenLöschen(IEnumerable<string> zeilen)
8 => zeilen.Where(x => string.IsNullOrWhiteSpace(x) is false);
9 }
10 ...
11 }
Ich habe wieder die Arbeit für alle Listenelemente getrennt von der
Arbeit auf einem Listenelement (lokale Funktion). Die Magie der so
genannten extension methods liegt in der Definition der Klasse und der
Methode als static und dann der Kennzeichnung des ersten Parame-
ters mit this. Dadurch kann die Methode LeerzeilenLöschen() in
dot notation, also mit einem Punkt, auf alle Werte vom Typ IEnu-
merable<Datei> angewendet werden. Wenn im Code steht datei-
en.LeerzeilenLöschen() dann macht der Compiler daraus Berei-
nigen.LeerzeilenLöschen(dateien).
Ein wunderbares Sprachfeature, um fluent interfaces zu definieren! So
profitiert die Übersetzung von Flow-Design Modellen von modernen
Sprachen.
Die Filterung von Leerzeilen und 1-zeiligen Kommentaren unterscheidet
sich von der für mehrzeilige Kommentare. Die braucht nämlich Zustand.
Beim Durchlaufen der Zeilen hängt ihre Klassifizierung davon ab, ob
ein Kommentarzeichen gefunden wurde oder nicht. Das merkt sich der
Algorithmus in imKommentar.
1 public static IEnumerable<Datei> MehrzeiligeKommentareLöschen(
2 this IEnumerable<Datei> dateien) {
3 return dateien.Select(x => new Datei {Zeilen =
4 MehrzeiligeKommentareLöschen(x.Zeilen)});
5
6 IEnumerable<string> MehrzeiligeKommentareLöschen(IEnumerable<string> zeilen) {
7 var imKommentar = false;
8 foreach (var z in zeilen) {
9 if (imKommentar) {
10 var iKommentarende = z.IndexOf("*/");
11 if (iKommentarende >= 0) {
12 // ein Kommentar endet in der Zeile;
13 // Folgezeilen sind keine Kommentarzeilen mehr
14 imKommentar = false;
15 if (z.Trim().EndsWith("*/") is false)
16 // Kommentarzeile ist schon eine Nettozeile, weil nach dem
17 // Kommentarende nicht nur Whitespace steht
18 yield return z;
19 }
20 }
21 else {
22 var iKommentaranfang = z.IndexOf("/*");
23 if (iKommentaranfang >= 0) {


---


<!-- Page 503 of 584 -->


Musterlösung: 05-Flow-Designmit2-dimensionalenDatenflüssen 494
24 // ein Kommentar beginnt in der Zeile;
25 // Folgezeilen sind Kommentarzeilen
26 imKommentar = true;
27 if (z.Trim().StartsWith("/*") is false)
28 // Kommentarzeile ist noch eine Nettozeile, weil vor dem
29 // Kommentaranfang nicht nur Whitespace steht
30 yield return z;
31 }
32 else
33 yield return z;
34 }
35 }
36 }
37 }
Die Funktion ist schon etwas länger, aber 25 Zeilen Logik sind noch nicht
zu viel, finde ich. Außerdem ziehen die Kommentare, die ich hier für
hilfreich halte, die Logik in die Länge. Netto sind es sogar weniger als
20 Zeilen Logik.
Für diesen Teil des Programms hätte ich im Entwurf auch ein Modell
machen können - allerdings kein Datenfluss-Modell, sondern ein Zu-
standsdiagramm. Für zwei Zustände ist das allerdings nicht ganz lohnend.
Und dann hätte sich die Frage nach der Übersetzungsregel gestellt. Denn
Modelle sollen ja geradlinig in Code transformiert werden können. Ich
habe zwar so eine Übersetzungsregel - doch da es hier um Datenfluss-
Modellierung geht, wollte ich nicht zu weit abschweifen. Deshalb schlicht
monolithischeLogikfürdieOperationMehrzeilige Kommentare lö-
schen.
Reflexion
Insgesamt war das eine gute Erfahrung, finde ich. Vom Problem zur
lauffähigen Lösung in wenigen klaren Schritten. Tatsächlich habe ich bei
der Implementation keinen Fehler gemacht. Alles war klar ausgearbeitet;
die jeweilige Logik in den Operationen war überschaubar. (Nur die
mehrzeiligenKommentarehabenmichetwasmehrNachdenkengekostet.)
TrotzdemliefdasProgrammnicht.Esstürztenichtab,aberzeigtean,keine
Nettozeilen gefunden zu gaben in einer Datei. Es gab tatsächlich nur eine
relevante Datei in einem Unterverzeichnis mit zwei Dateien. Soweit war
das Ergebnis noch korrekt. Doch warum keine Nettozeilen?
DaraufhinhabeichmitdemDebuggingangefangen:Ichwolltefeststellen,
ab wo fehlerhafte Daten in der Verarbeitung sind. Wie sich herausstellte,


---


<!-- Page 504 of 584 -->


Musterlösung: 05-Flow-Designmit2-dimensionalenDatenflüssen 495
wurden aus der Datei keine Zeilen geladen. Hatte ich den API falsch
eingesetzt? Das konnte eigentlich nicht sein.
Es hat mich einige Minuten gekostet, um das Problem aufzuspüren: Die
Testdatei war tatsächlich leer. Das Ergebnis war korrekt. Ich hatte ver-
gessen, den Beispielcode aus der Aufgabe aus dem Clipboard einzusetzen,
nachdem ich die Datei angelegt hatte. Wie das geschehen konnte, weiß
ich nicht. Aber so war’s.
Schön, dass das der Fehler außerhalb des Code war. Die schrittweise
Annäherung an den Code hatte sichergestellt, dass die Lösung korrekt ist.
Doch korrekt ist am Ende nicht genug. Bei dieser Größenordnung spürst
du sicher auch ein gewisses Unbehagen, alle Funktionseinheiten in der-
selben Klasse zu codieren. Auch wenn sie im Fluss zusammengehören,
so passen sie nicht alle unter das Dach einer Klasse. Umso stärker wirst
du dieses Gefühl haben, je umfangreicher Datenflüsse werden. Oder
manchmal wirst du dich auch schon bei kleinen winden; Domänenlogik
undDatenbankzugriffsindsoverschieden,warumsolltendieinderselben
Klasse untergebracht sein? Das scheint ein Widerspruch selbst gegen
mainstream Objektorientierung.
Deshalb dreht sich das nächste Kapitel um die Modularisierung. Wach-
sende Datenflüsse müssen über Integrationen hinausgehend organisiert
werden. In dieser Implementation hat mich die Idee der fluent interface
vor einer zu großen Überladung von Program gerettet; für die extension
methods musste ich eine eigene Klasse definieren. Glück gehabt. In Zu-
kunft möchte ich mich jedoch nicht mehr aufs Glück verlassen.


---


<!-- Page 505 of 584 -->


Musterlösung: 06 -
Flow-Design mit
modularisierten
Datenflüssen
Ich hoffe, bei diesen Übungsaufgaben kommt allmählich Spaß an der
Sache mit dem Entwurf bei dir auf. Mit Modulen im Entwurfsbild,
genauer: Klassen, sind ja nun endlich alle Bestandteile der mainstream
Objektorientierung wieder beisammen. Du musst dir nicht mehr den
Kopf darüber zerbrechen, wie du nur mit Datenflüssen große Programme
beschreiben sollst.
Aufgabe 1 - Datenfluss modularisieren
Als erste Aufgabe dieses Mal die Modularisierung eines schon existieren-
den Datenflusses für die Nettozeilenzählung. Den hast du nicht selbst
entworfen und auch ich muss mich wieder ein wenig hineindenken in
die Problematik. Das ist ein gutes Beispiel dafür, wie es dir immer wieder
gehen kann: Du wirst das Modell nicht flüssig von “vorne nach hinten”
einfach “durchlesen” können, sondern musst es dir erarbeiten. Dabei
gehst du vor und zurück. Du musst deuten, beurteilen, für gut befinden
oder auch etwas verbessern nach deinem Wissensstand. Ordnung und
Sauberkeit von Code sind relativ und subjektiv.
Schrittweise Modularisierung
Bei der Modularisierung gehe ich auch hier wieder vor allem bottom-up
vor. Links im Bild kannst du das ein bisschen verfolgen:


---


<!-- Page 506 of 584 -->


Musterlösung: 06-Flow-DesignmitmodularisiertenDatenflüssen 497
• Ich könnte sagen, dass ich mit irgendeiner Operation anfange, aber
so ist es dann doch nicht. Ich habe so meine Pappenheimer, die ich
gerne aus dem Weg haben will und wo ich mir sehr sicher bin, in
welches Modul sie gehören: das sind die Operationen, die zur Peri-
pheriegehören,alsoAPI-Zugriffekapseln.Dasweißichganzsicher
vonRelevante Dateien finden.FürdieOperationeröffneich
die Klasse Filesystem{}.
• Gibt es weitere Operationen, die in diese Klasse passen? Ja: Laden.
EinmalgehteszwarummehrereDateienundeinmalumdenInhalt
einer Datei, doch das ist für mich in diesem Beispiel ähnlich genug.
Auf jeden Fall gehört Laden aber nicht zur Datenklasse Datei{}
dieschondefiniertist.DasistjaeinereineDatenklasseundverträgt
deshalb eher keine Logik und schon gar keine API-Aufrufe.
• Sammeln als Integration nehme ich gleich mit ins Filesystem{},
weil die Funktionseinheit zwei Operationen aus derselben Klasse
integriert.
• Als nächstes fasse ich in einem Rutsch Parsen und Anzeigen in
der Klasse UI{} zusammen. Das ist auch noch sehr naheliegend.
• Dann die Operationen zur Filterung. Ich denke, die gehören alle
zusammenineineKlasseFilter{}.UndweildanndieIntegration
Bereinigen wieder nur aus einer Klasse integriert, kommt sie
ebenfalls in die Klasse. Damit ist die Oberfläche/der Kontrakt für
dieFilterungreduziertaufeineFunktion.DetailsderFilterungmuss
man außerhalb der Klasse nicht sehen.
• Es bleibt noch Zählen als Operation. Die Verantwortlichkeit ist
trivial. Dafür lohnt sich keine eigene Klasse. Aber auch Filter{}


---


<!-- Page 507 of 584 -->


Musterlösung: 06-Flow-DesignmitmodularisiertenDatenflüssen 498
mag ich sie nicht zuschlagen. Deshalb fasse ich sie mit der Integra-
tion Analysieren zusammen.
• Überhaupt stecke ich alle darüber liegenden Integrationen in diesel-
be Klasse: Program{} wird zu meiner zentralen Integrationsklasse
in diesem kleinen Szenario.
Klassendiagramm
Das Klassendiagramm kann ich leicht ableiten. Was ich da sehe, gefällt
mir von den Verantwortlichkeiten her:
• EsgibteineKlassefürdieAufgabederIntegration:Program{}.Sie
bildet das oberste Stratum.
• Es gibt mehrere Klassen, die auf die Operation, d.h. die Verhal-
tensherstellung konzentriert sind und das Ganze auf einem zweiten
Stratum repräsentieren: UI{}, Filesystem{} und Filter{}.
• Und schließlich ist da sogar eine Datenklasse, die die Module teilen.
Sogar Program{} ist davon abhängig, weil in der Integration beim
Zählen mit Dateien gearbeitet wird.
Beim Herausarbeiten des Klassendiagramms fällt mir nun die Abhängig-
keit von Filter{} zu Datei{} auf. Die Domäne ist abhängig von eine
Klasse, deren Instanzen die Persistenz beschafft. Das kann schon so sein
- doch in diesem Fall finde ich das irgendwie unnötig. Muss die Filterung
wirklich Dateien kennen?


---


<!-- Page 508 of 584 -->


Musterlösung: 06-Flow-DesignmitmodularisiertenDatenflüssen 499
Nein, die Filterung muss nur auf Mengen von Zeilen arbeiten. Der
Kontrakt der Filterung kann weiter verkleinert werden, indem ich die
Datei{}ausihmstreicheunddieOperationenunabhängigdavonmache.
Die Datenklasse Datei{} eingeführt zu haben, bereue ich nicht. Nur
weil es sie aber gibt, bedeutet das nicht, dass jeder sie kennen muss.
Datenklassen können dich also aus der primitive obsession befreien - und
andererseits kann es manchmal eine Tugend sein, primitivere Datentypen
an Modulschnittstellen zu benutzen, um die Verantwortlichkeit klarer
herauszustellen. Filter{} muss keine Kenntnis davon haben, dass zu
filternde Zeilen irgendetwas mit Dateien zu tun haben.
Bibibliotheken
Im Strukturdiagramm der Bibliotheken findest du die Abhängigkeit nun
also nicht mehr:


---


<!-- Page 509 of 584 -->


Musterlösung: 06-Flow-DesignmitmodularisiertenDatenflüssen 500
Ich muss sagen, das sieht gut so aus. Durch die Auflösung der Abhängig-
keit muss nun die Domänenbibliothek Filter das Filesystem nicht
kennen. Warum sollte auch der Kern eines Programms abhängig sein von
der Peripherie?
• Die Domänenklasse Filter{} allein in einer Bibliothek finde ich
sehr angemessen. Die Domäne verdient eine Black Box, mit der sie
sogar wiederverwendet werden könnte.²³⁸
• Dasselbe gilt für den Zugriff auf das Dateisystem. Die Sammlung
von Dateien eines Typs hat auch Potenzial für die Wiederverwen-
dung.
• Die Benutzerschnittstelle ist in diesem Szenario so dünn und im
Grunde nebensächlich, dass ich sie in der Bibliothek unterbringe,
die die Integrationen enthält und die Anwendung repräsentiert.
Man muss die Zahl der Module auch nicht zwanghaft vergrößern.
Sie sollen entkoppeln, aber sie sollen eben auch zusammenfassen.
DieWahrscheinlichkeit,dassKlasseninanderenZusammenhängen
²³⁸Ich führe hier mal die Wiederverwendung an, weil sie ein so beliebter Begriff der
mainstream Objektorientierung ist. Zwar halte ich sie für stark überbewertet, weil längst
nicht in dem Maße wiederverwendet wird, wie es sich ihre Befürworter wünschen. Au-
ßerdem sind sich die meisten Befürworter nicht bewusst, welche Verantwortung mit der
Wiederverwendungeinhergeht:Waswiederverwendetwerdenwillundwird,mussnämlich
sehr stabil sein. Und schließlich steht die Effizienz, die eine Wiederverwendung verspricht,
dem entgegen, was meistens viel wichtiger ist: Flexibilität. Dennoch hält sich der “Mythos”
Wiederverwendbarkeit.Warumalsonicht,ihneinmalbedienen-dannallerdingsrichtig,d.h.
auf der Modul-Hierarchieebene der Bibliotheken. Wiederverwendbarkeit braucht die Black
Box.Undichwürdesogarsagen,dassesdamiteinerBibliothek,gareinemPaketnichtgetan
ist, sondern eine Komponente her müsste. Doch in diesem Beispiel will ich da mal nicht so
weithinaufreichen.


---


<!-- Page 510 of 584 -->


Musterlösung: 06-Flow-DesignmitmodularisiertenDatenflüssen 501
nochmal gebraucht werden könnten - z.B. hinter einem anderen
Frontend - ist dafür ein Treiber. Deshalb Domäne und Dateisystem-
zugriff in eigenen Bibliotheken.
Aufgabe 2 - Game of Life
Beim Game of Life ist die Aufgabe wieder mal größer. Auf der grünen
WiesesolleinganzesProgrammentworfenwerden.Daistzunächstetwas
Anforderungsanalyse nötig und daraus folgend ein Lösungsansatz, bevor
es mit den Datenflüssen losgehen kann.
Lösungsansatz
Daten werden aus Dateien gelesen und in Dateien geschrieben. Das ist
nichtsospannend.DerLösungsansatzkonzentriertsichdaheraufdas,was
dazwischen passiert: die Domäne.
Hier scheinen mir zwei Entscheidungen zu treffen: eine zur Datenstruktur
und eine zum Vorgehen bei der Transformation einer Welt mit ihrer
Lebensgeneration in die nächste.
Die Welt, in der sich das “Drama des Lebens” abspielt, ist hier so zentral,
dass es sich lohnt, dafür eine eigene Datenstruktur aufzusetzen. Ich denke,
es sollte eine Klasse geben, die den Dateiinhalt in Form einer boolschen
Matrix repräsentiert. Darauf kann sich auch etwas Logik ansammeln, was
hilfreich zur Bekämpfung einer primitive obsession sein mag.
Bei gegebener Welt-Matrix stellt sich die Frage, wie die Evolution stattfin-
densollte.DieRegelnsindklarfüreineZelle.AberwiesolldieGesamtheit
allerZellenbehandeltwerden?IchfindedadenBegriffderNachbarschaft
hilfreich: Das Leben und Sterben einer Zelle hängt davon ab, wieviele
Zellen in ihrer Nachbarschaft leben bzw. tot sind. Bei der Berechnung
der nächsten Generation einer Welt werden daher die Zellen in beliebiger
Reihenfolge durchlaufen und für jede die Nachbarschaft ermittelt. Mit der
geht es dann zur Bestimmung “des Schicksals” der Zelle, das sich in einer
neuen Welt niederschlägt.


---


<!-- Page 511 of 584 -->


Musterlösung: 06-Flow-DesignmitmodularisiertenDatenflüssen 502
Die Nachbarschaftsermittlung sehe ich als Verantwortlichkeit der Daten-
strukturklasse; sie fällt in die Kategorie Zugriff.
Modellierung
MitdiesergrobenVorstellungvonderArbeitsweisedesProgrammsmache
ichmirzuerstGedankenüberdienotwendigen“Bauteile”.Welchewerden
überhaupt gebraucht? Welche sind größer, welche sind kleiner? Erst
danach bringe ich sie in einem Datenfluss zusammen.
Zerlegungsbaum
Das Programm wird nicht ganz klein werden. Da muss ich etwas tun, um
den Überblick über den Datenfluss zu behalten. Deshalb benenne ich die
Funktionseinheiten im Zerlegungsbaum schon mit Kürzeln; dann fällt der
Datenfluss knapper aus.
DaessichumeinKonsolenprogrammhandelt,gibtesnureineInteraktion
und also nur einen Fluss, der von Main() später integriert wird. Alles
Folgende hängt also unter dieser Wurzel:


---


<!-- Page 512 of 584 -->


Musterlösung: 06-Flow-DesignmitmodularisiertenDatenflüssen 503
• Kommandozeile analysieren (KANA) - trivial²³⁹
• Evolutionsfortschritt melden (EMEL) - trivial. Hier stellt sich aller-
dings die Frage, wann/wo die Meldung stattfindet. Ich habe diese
Verantwortlichkeit nur vorbehaltlich so weit oben im Zerlegungs-
baum angesiedelt.
• Initiale Welt laden (WLAD)
– Datei laden (DLAD) - trivial
– Deserialisieren (WDSE) - trivial bis einfach. Die textuellen
Daten werden in die Welt-Datenstruktur überführt.
• Evolvierte Welt speichern (WSPE)
– Serialisieren (WSER) - trivial
– DateinamenfürdieseEvolutionsgenerationbestimmen(DATN)
- trivial
– Datei speichern (DSPE) - trivial
• Evolution spielen (EVOL) - Ausgehend von der initialen Welt wer-
den neue Generationen erzeugt. Die nächste ersetzt dabei jeweils
die vorhergehende.
– Welt evolvieren (WEVOL) - Eine neue Welt Zelle für Zelle
berechnen.
* Lebewesen in ihrer Umgebung aufspüren (LSAM) - ein-
fach. Alle Lebewesen werden gesammelt und mit ihren
Nachbarnversehen.HiererwarteichdiezentralenSchlei-
fen der Verarbeitung.
* ÜberdasSchicksaljedesLebewesensentscheiden(LENT)
- einfach. Es wird eine Zelle im Kontext ihrer Nachbarn
betrachtet. Das Ergebnis ist dann aber nur die Informati-
on, ob sie zukünftig mit Leben gefüllt ist oder nicht.
* Neue Welt aus den Entscheidungen zu den einzelnen
Lebewesen zusammensetzen (WZUS) - trivial.
• Evolvierte Welten zurücksetzen (WZUR) - einfach. Bevor es mit
der Generierung neuer Welten für die initiale losgehen kann, soll-
ten eventuell vorhandene gelöscht werden. Denn wenn die Welt
block.txt nun sich über 3 Generationen entwickeln soll, früher
jedoch eine gleichnamige Welt schon 4 Generationen bekommen
hat,dannwürdesonsteinealte,überhängigenochaufderFestplatte
stehen.
²³⁹Ich kennzeichne die Teilprobleme mit einem Schwierigkeitsgrad, wie ich ihn in Test-
first Codierung eingeführt habe. Damit gebe ich mir einen Hinweis für das Vorgehen in
einerspäterenImplementation.DieseAngabeistnurfürBlätter/Operationennötig;darüber
liegendeKnotenimZerlegungsbaumsindperdefinitionemkompliziert,dennsiewurdenja
weiterzerlegt.


---


<!-- Page 513 of 584 -->


Musterlösung: 06-Flow-DesignmitmodularisiertenDatenflüssen 504
Die Matrix der Welt ist ebenfalls mit (einfacher) Logik für den Zugriff
ausgestattet:
• Abfrage der Matrix-Dimensionen (Breite, Höhe) - trivial
• Setzen des neuen Lebenszustands einer Matrix-Zelle - trivial
• Auslesen des Lebenszustands einer Zelle inklusive ihrer Nachbar-
zellen - einfach. Ob ich die Nachbarzellen einzeln mit ihren Lebens-
zuständen liefere oder nur die Anzahl der lebenden, weil die für
das Regelwerk ausschlaggebend ist, überlege ich wohl erst bei der
Codierung.
Datenfluss
Ich habe durch den Zerlegungsbaum einen Eindruck vom Umfang des
Datenflusses, d.h. seiner Breite und Tiefe. Da kommt ein bisschen zu-
sammen, doch mit den Abkürzungen für die Funktionseinheiten wird das
Diagramm hoffentlich nicht ausufern.
Die Reihenfolge der Verarbeitung für viele Funktionseinheiten ist kein
Problem. In der Evolution muss ich aber noch genau hinschauen. Und
auch die Verquickung mit der Matrix muss stimmen. Und ich die Fort-
schrittsausgabe platzieren: Die soll eigentlich mit ihrer API-Abhängigkeit
nicht so tief im Baum stehen, doch nur dort ist bekannt, wann eine
weitereGenerationerzeugtwurde;wennichwährendderEvolutionschon
darüber informieren will, muss nah dran protokolliert werden.


---


<!-- Page 514 of 584 -->


Musterlösung: 06-Flow-DesignmitmodularisiertenDatenflüssen 505
Im Datenfluss siehst du Nummern, die anzeigen in welcher Reihenfolge
ich ihn habe wachsen lassen.
1. Zuerst die Wurzel, ist ja klar.
2. Dann die Integration, die die Wurzel vornimmt. Bisher gibt es nur
Funktionseinheiten und Datenflusspfeile. Ich habe mir noch keine
Gedanken über die konkret fließenden Daten gemacht. Das kommt
erst weiter unten.
3. Ich verfeinere das Laden der initialen Welt: Dateiinhalt lesen und
deserialisieren.
4. Integration der Speicherung aller berechneten Generationen. Auch
wenn ich noch keine Daten notiert habe, ist mir soviel klar, dass
am Ende alle neuen Welten auf einmal angeliefert und gespeichert
werden.DasistfürmicheinedeutlichereTrennungderVerantwort-
lichkeiten: das Eine ist fertig - Evolution -, das andere ist dran -
Speicherung.
5. Die Evolution insgesamt, die aus einer initialen Welt viele zukünf-
tige Welten macht, breche ich runter auf die Entwicklung nur einer
neuen Welt aus einer vorherigen. In EVOL wird es also dark logic
geben,d.h.Logik,dieeinenEffekthat,ohnedassdusiesiehst.Denn
“sichtbar” ist per definition nur Logik in Operationen. In WEVOL
kann ich mich nun ganz auf eine Welt konzentrieren.


---


<!-- Page 515 of 584 -->


Musterlösung: 06-Flow-DesignmitmodularisiertenDatenflüssen 506
6. Deren Datenfluss ist der nächste: Hier wird die Welt nun in eine
Folge von Zellen mit ihren Nachbarn zerlegt, auf die die Regeln
angewendet werden. Aus dem Ergebnis wird die neue Welt zusam-
mengesetzt. Das ist die zentrale Domänenlogik.
7. Am Ende des Zerlegungsbaums angekommen merke ich, dass ich
mit dem Zurücksetzen des Dateisystems eine bestehende Integra-
tion erweitern muss. Ich verberge WZUR im Datenfluss von WSPE.
Bevor die neuen Welten gespeichert werden, bereinige ich even-
tuelle alte Versionen gleichen Namens. Daran hatte ich bei der
Verfeinerung in Schritt (4) nicht gedacht. Ich bin zu sehr nach
der Zerlegungshierarchie vorgegangen, in der WZUR noch nicht
zugeordnet war; es war ein Anhängsel am Ende, weil ich daran
erst zum Schluss gedacht hatte. Doch genau dafür sind ja die
verschiedenen Phasen da: dass ich reflektiere und “geradeziehe”.
8. Da die Zusammenhänge zwischen den Funktionseinheiten nun
klar sind, mache ich mich daran, die Daten zu bestimmen, die
dazwischen fließen. Dabei gehe ich von links nach rechts und von
oben nach unten vor.
9. DazugehörtauchdieFestlegungderDatenstrukturen.Weltkannte
ich schon als Matrix aus der Zerlegung. Nun ist aber noch dazu
gehörig die Zelle gekommen. Ich denke, die Welt in Zellen aufzu-
lösen, um die einzeln den Regeln zu unterwerfen, ist eine gute Idee
für den Datenfluss in WEVOL.
10. Und nun ist es doch passiert: Ich habe eine Funktionseinheit verges-
sen. Kein Wunder, denn die Fortschrittsanzeige EMEL lag mir oben
schon im Magen. Jetzt ist sie übriggeblieben und ich muss einen
Platz für sie finden. Wenn ich während der Evolution melden will,
dass wieder eine Generation berechnet wurde, dann geht das nur
innerhalb von WEVOL, am besten am Ende.
Du siehst, einerseits ist die Übersetzung einer Zerlegungshierarchie in ei-
nenDatenflussgeradlinig-andererseitsmussmanschonetwasaufpassen,
damitnichtsvergessenwird.UnddieGelegenheitzurReflexionsolltestdu
auch nutzen. Wenn der Fluss konkret sichtbar wird, stellen sich manche
Dinge aus der Zerlegungsphase nochmal anders dar.
Modularisierung
Bis auf die Datenstrukturklassen für die Welt sind noch keine Klassen
im Datenfluss festgelegt. Das folgt wie immer in einem nachgelagerten


---


<!-- Page 516 of 584 -->


Musterlösung: 06-Flow-DesignmitmodularisiertenDatenflüssen 507
Schritt:
Auf hier halte ich für dich die Reihenfolge meines Vorgehens fest:
1. Wie sollte es anders sein: Die Datenklassen stehen am Anfang. Ich
färbe ihr Vorkommen im ganzen Datenfluss ein. Damit ist es später
für mich leichter, auch die Abhängigkeiten zu ihnen auszulesen.
2. Weil ich gerade bei den Datenstrukturen bin, mache ich mit den
Operationen für ihre Umwandlung weiter. Wo wird eine Welt
hergestellt bzw. “zerlegt”. Das ist im Zusammenhang mit der Per-
sistenz der Fall. Die Funktionseinheiten dafür bewegen sich in einer
“Zwischenwelt”: sie gehören nicht wirklich zur Persistenz und auch
nicht wirklich zur Domäne. Also bekommen sie eine eigene Klasse,
das Mapping{}.
3. Als nächstes mache ich mir klar, welche Operationen zur Persistenz
gehören. Die sind einfach zu identifizieren, allerdings stößt mir
dabei auf, dass sie unter WSPE nicht in einem Block stehen. Die
Farbgebung und Einfassung durch die Klasse macht mir deutlich,
dass die Persistenzverantwortlichkeit in dem Datenfluss auseinan-
der gerissen ist. Darüber muss ich nochmal nachdenken… Doch
das ist ein anderer Modus; erstmal bin ich zufrieden, überhaupt
die Funktionseinheiten des Filesystem{} identifiziert zu haben.
Deshalb weiter mit der Modularisierung.


---


<!-- Page 517 of 584 -->


Musterlösung: 06-Flow-DesignmitmodularisiertenDatenflüssen 508
4. Ich entscheide mich endgültig, die Zellenbeschaffung inklusive
NachbarschaftssammlungderWelt{}zuzuschlagen.DieWeltkann
sich selbst zerlegen in ihre Bestandteile. Das finde ich für eine
Datenstruktur konsequent.
5. Und wenn sie sich zerlegen kann, dann kann sie sich auf wieder
zusammensetzen. Deshalb gehört auch der Aufbau einer neuen
Welt aus evolvierten Zellen zur Welt{}.
6. Die eigentliche Regelanwendung gehört natürlich zur Evoluti-
on{}, der zentralen Domänenklassen. Und weil ich schon dabei
bin, schlage ich der gleich die Integrationsebenen darüber zu. Da
ist ja ohnehin eine unsaubere Funktionseinheiten mitdark logic
dabei. Die Domäne besteht damit aus Logik in einer Serviceklasse
und einer Datenklasse. Das ist nicht ungewöhnlich. Verhalten und
Daten gehören gerade in der Domäne zusammen.
7. Und weil ich nun schon Integration modularisiert habe, mache ich
darüber weiter. In Program{} fasse ich die Integrationen auf den
oberen Ebenen des Datenflusses zusammen und aggregiere auch
noch das Bisschen Logik für die Kommandozeilenanalyse.
8. Wenn die Kommandozeilenanalyse, die zur Benutzerinteraktion
gehört,inProgram{}liegt,dannisteskonsequent,dieFortschritts-
meldung dort auch anzusiedeln. Aber ganz wohl ist mir dabei nicht.
Ich sehe, dass Program{} damit über die Datenflusshierarchie
auseinander gerissen ist.
Meine Erfahrung in der Modularisierung sagt mir, dass es keine gute
Idee ist, unten im Datenfluss eine Funktionseinheit in einer Klasse zu
haben,dieauchobenvorkommt.DennDatenflusshierarchiensindjaauch
Abhängigkeitsbäume, was bedeutet, dass nun Evolution{} von Pro-
gram{} abhängig ist, weil WEVOL auch EMEL integriert. Und umgekehrt
ist natürlich Program{} von Evolution{} abhängig, weil die Aufgabe
von Program{} die Integration in den oberen Strata ist. Damit ist eine
zirkuläre Abhängigkeit entstanden. Das geht gar nicht. Nie!
Also muss ich einen Weg finden, sie aufzulösen. Den sehe ich nur in
konsequenter Auslagerung der Benutzerinteraktion in eine eigene Klasse
UI{}, von der sowohl Program{} wie Evolution{} dann abhängig
sind.


---


<!-- Page 518 of 584 -->


Musterlösung: 06-Flow-DesignmitmodularisiertenDatenflüssen 509
Siehst du die UI{}-Klasse links oben und rechts unten? Schön ist das
immer noch nicht, aber im Moment weiß ich keinen anderen Ausweg
unter der Prämisse, dass die Fortschrittsanzeige bei jeder neuen Welt
sofort erfolgen soll.
AberwennichschonbeimVerändernderModularisierungbin,dannkann
ich auch nochmal einen Blick auf die auseinander gerissene Persistenz
werfen. Jetzt bin ich raus aus dem ersten “Flow” der Modularisierung und
kann mich dem widmen, was mir in Schritt (3) aufgefallen ist.
Nein, das ist wirklich nicht schön. Die rot klassifizierten Funktionseinhei-
ten sollten zusammenstehen, wenn irgend möglich. Das sagt mir mein
ästhetisches Empfinden. Schön, dass es das gibt und auch anschlagen
kann. Visualisierte Datenflüsse machen es möglich. Die Strukturierung
wird besser, ohne dass ich nachdenken muss. Ein Reflex gibt mir die
Verbesserung ein. Hier die alte und die neue Version des Persistenz-
Datenflusses inklusive Modularisierung:


---


<!-- Page 519 of 584 -->


Musterlösung: 06-Flow-DesignmitmodularisiertenDatenflüssen 510
Alle Funktionseinheiten für die Persistenz aller Welten stehen nun zu-
sammen. Sie arbeiten rein auf serialisierten Daten. Das Zurücksetzen des
Dateisystems macht wie bisher den Anfang. Und die neu eingezogene
Integration Speichern reduziert die Oberfläche von Filesystem{};
dort werden nur noch zwei Funktionen angeboten, eine zum Laden einer
Welt und eine zum Speichern vieler. Das gefällt mir.
Klassendiagramm
Im Datenflussdiagramm ist jetzt viel zusammengekommen. Darin die
Klassen jedoch eingezeichnet zu haben, war sehr sinnvoll, weil ich da-
durch nochmal über den Prozess nachgedacht habe. Erst Verhalten, dann
Struktur; erst Verben, dann Substantive. Die Funktionseinheiten der Da-
tenflusshierarchie waren eine gute Masse, um daraus Aggregationen zu
abstrahieren.
Die möchte ich nun aber einmal herausarbeiten, um deren Abhängigkei-
ten zu überprüfen:


---


<!-- Page 520 of 584 -->


Musterlösung: 06-Flow-DesignmitmodularisiertenDatenflüssen 511
Das sieht gut aus. Es gibt ein Stratum der Integration und eines der
Operation. Darunter die Datenstrukturen.
Nur an einer Stelle stutze ich wieder: Auch die Abhängigkeit zwischen
Evolution{} und UI{} taugt mir nicht. Warum sollte die Domäne von
der Peripherie abhängen? Wenn die Domäne mit der Peripheri integriert
wird, ist das ok; doch eine Abhängigkeit suggeriert unterschiedliche
Abstraktionsniveaus. Die gibt es jedoch nicht zwischen Domäne und
Peripherie; beide gehören dem selben Stratum an.
Aber ich lasse das mal so stehen für den Moment. Eine Lösung kann sich
entweder nur ergeben durch Neuplatzierung der Fortschrittsanzeige, so
dass nicht mehr kontinuierlich angezeigt wird, wenn eine neue Welt be-
rechnet wurde; dann ist es aber auch keine Fortschrittsanzeige mehr. Oder
eine Lösung braucht ein weiteres Konzept, das ich dir im nächsten Kapitel
vorstellen will. Für den Moment lebe ich also mit dieser Unsauberkeit.
Bibliotheksdiagramm
Als nächste Ebene der Modularisierung wieder die Aggregation der Klas-
sen zu Bibliotheken. Welche Black Boxes könnte/sollte es hier geben?


---


<!-- Page 521 of 584 -->


Musterlösung: 06-Flow-DesignmitmodularisiertenDatenflüssen 512
Ich denke, mit drei Bibliotheken kommt das Programm aus. Program
ist die Repräsentanz des Programms; dort startet die Ausführung. Die
Domäne steht ganz natürlich für sich mit der Serviceklasse und den
Datenklassen.UnddiePersistenzist-wieimmer-ebenfallsausgelagert.²⁴⁰
Gut, dass die nicht noch von den Datenklassen abhängig ist.
DassallerdingsdieDomänenbibliothekGame of Lifefüreinezirkuläre
Abhängigkeit zu Program sorgt, geht gar nicht. Die wird natürlich durch
die beim Klassendiagramm erwähnte Abhängigkeit der Evolution von der
Benutzerinteraktion verursacht. Ich wusste ja, dass dadurch nichts Gutes
entstehen kann…
Im Moment lasse ich aber auch das stehen. Im nächsten Kapitel löst sich
das in Wohlgefallen auf. Der Aufwand, eine Bibliothek für die Benutzer-
interaktion herauszuziehen, ist mir im Moment zu groß. Da ohnehin noch
keine Implementation nötig ist, gibt es keine technischen Schwierigkeiten.
Reflexion
So sieht realistische Modellierung aus. Hier war nichts geschönt, nichts
kaschiert, wie es so oft in Lehrbuchbeispielen passiert.²⁴¹ Was geradlinig
lieg, lief tatsächlich so; wo es nicht so gut lief, lief es tatsächlich nicht
so gut. Das zu dokumentieren hat mir die Bezifferung der Schritte leicht
²⁴⁰SiehstdudasMuster?DieBibliotheksstrukturdervorherigenLösungsiehtgenausoaus:
Eine integrierende Bibliothek fasst Peripherie und Domäne zusammen. Das ist kein Zufall!
DieBeweggründedahintererkläreichdirimKapitelzurIODAArchitektur.
²⁴¹Ok, ich habe mir die Aufgabe nur in sofern einfacher gemacht, als dass ich den
Zerlegungsbaum aus dem Band Test-first Codierung abgeschrieben habe. Doch dort hatte
ichihneigensfürdiedortigeAufgabeentwickelt.Ehrlich.Kannstdumirglauben.Wieglatt
dasgegangenist,kannstdudortnachlesen.Auchdasistnichtgeschönt.


---


<!-- Page 522 of 584 -->


Musterlösung: 06-Flow-DesignmitmodularisiertenDatenflüssen 513
gemacht.Undichwarnatürlichfroh,dassichdieDiagrammeaufmeinem
iPad gezeichnet habe, so dass ich die Nachträge ohne große Probleme
einarbeiten konnte.
Entwurf ist die zentrale kreative Tätigkeit in der Softwareentwicklung -
abgesehen vom Gesamtprozess. Softwareentwicklung als Ganzes ist eben
Entwicklung, also ein Prozess, der nicht immer geplant und geradlinig
voranschreitenkann.DeshalbdasinkrementelleVorgehen.Undinnerhalb
jedes Inkrements kann es Iterationen geben: Es geht vor und dann wieder
zurück.
Winston Royce hat das iterative Vorgehen 1970 in seinem Paper “Mana-
ging the Development of Large Software Systems²⁴²” für die folgenden
Programmierergenerationen prägend visualisiert:
Auch wenn das Ganze wie ein Wasserfall aussieht, gibt es darin doch
Schleifen. Diese Rückschritte sind Iterationen: Es wird etwas nochmal
getan, wovon man dachte, dass es schon abgeschlossen sei. Jeder Pfeil, der
zurück zeigt, stellt eine Nachbesserung dar. Ob der Pfeil dann nur zum
unmittelbaren Vorläuferprozessschritt zeigt oder noch weiter nach oben,
ist unerhelblich.²⁴³
²⁴²http://www-scf.usc.edu/~csci201/lectures/Lecture11/royce1970.pdf
²⁴³NatürlichistderGesamtaufwandderNachbesserungumsogrößer,jeweiteroben/vor-
ne sie ansetzen muss. Deshalb untertitelt Royce das Diagramm mit“Hopefully, the iterative
interactionbetweenthevariousphasesisconfinedtosuccessivesteps.”


---


<!-- Page 523 of 584 -->


Musterlösung: 06-Flow-DesignmitmodularisiertenDatenflüssen 514
Und so ist es auch mir gegangen. Zwar bin ich nicht so weit zurückge-
gangen, aber auch ich habe mich im Nachbesserungskreis gedreht. Das ist
normal. Und wenn du in der Literatur Beispiele siehst, wo geradlinig vom
Ausgangspunkt auf das Ziel zugegangen wird, dann ist das genauso irreal
wie der das ewige Lächeln und die wohlgeformten Körper der Instagram-
Influencer.
Auch aus diesem Grunde habe ich einen so umgangssprachlichen Ton
für die Programming with Ease-Bände gewählt: mit ihm kann ich mir
Realismus erlauben. Würde ich dich offizieller, distanzierter, lehrbuchhaf-
ter ansprechen, würden Umwege eine Dissonanz bei dir erzeugen. Und
würde ich sie angesichts eines solchen Tons nicht gehen, sondern alles
glatt erscheinen lassen, wie es sich für ein Lehrbuch geziemt, dann wäre
das eben irreal und würde bei dir falsche Vorstellungen wecken.
Nicht nur habe ich mich aber hier ein wenig im Kreis gedreht bei der
Entwicklung des Modells, ich bin mir auch sicher, dass weitere Anpassun-
gen während der Codierung notwendig sein werden.²⁴⁴ Ein Entwurf ist
immer nur eine Therorie! Funktioniert der Entwurf, löst er das Problem
wirklich? Nur lauffähiger Code, der in implementiert kann den Beweis
führen. Bubbles don’t crash.
Was aber natürlich nicht heißt, dass ein Entwurf überflüssig wäre, weil er
ja eh nicht läuft. Das anderes fokussierte Mindset während des Entwurfs
ist entscheidend. Indem du Entwurf und Codierung trennst, wendest du
auf deine Arbeit das SRP an: in beiden Phasen werden schlicht sehr
unterschiedliche Entscheidungen getroffen.
²⁴⁴Allemal wird sich dann auch herausstellen, ob meine Einschätzungen der Schwierig-
keitsgrade bei der Zerlegung realistisch waren. Erfahrungsgemäß ist am Ende doch nicht
allessotrivialundeinfach,wiemanessichvorstellt.


---


<!-- Page 524 of 584 -->


Musterlösung: 07 -
Flow-Design mit
3-dimensionalen
Datenflüssen
Ich hoffe, mit dieser Aufgabe “ein ganzes Spiel” zu programmieren, rückt
Flow-Design für dich auf der Skala der Praxisrelevanz ein weiteres Stück
nach oben. Ich jedenfalls finde die Aufgabe vergleichsweise herausfor-
dernd. Sie ist so groß, dass ich nicht sehe, dass die Implementation “in
einem Rutsch” für mich machbar sein wird, selbst wenn ich ein Modell
erarbeitet habe.
Das Spiel ist ganz einfach. In den Spielregeln und in der Bedienung
steckt hier kein Geheimnis. Andererseits ist die Aufgabe groß genug, um
typische Aspekte einer Anwendung zu beleuchten. Der Teufel steckt im
Detail…
Technologisch gibt es hier allerdings wieder keine Herausforderung. Das
ist ja auch gewollt. Ich möchte dich nicht ablenken mit Infrastruktur. Am
Ende ist es kein Unterschied, ob du Flow-Design im Zusammenhang mit
einemlokalenRDBMSodereinerMongoDB-InstanzinderCloudodermit
RabbitMQ einsetzt. Die Prinzipien bleiben dieselben; die technologischen
Abhängigkeiten werden weggekapselt. Sie sind Sache eines tief liegenden
Stratums.
Aber genug der Vorrede. Game on!
Aufgabe 1 - Tic-Tac-Toe
Auch wenn das Spiel ganz einfach ist, will ich sauber vorgehen, um am
Ende sauberen Code zu haben. Selbst wenn es mir in den Fingern juckt,
einfach drauflos zu programmieren… Ich weiß, dass ich damit schnell an


---


<!-- Page 525 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 516
eine Grenze stoßen werden. Und dann stecke ich mittendrin, habe eine
Menge Code angehäuft, weiß nicht ein und aus und wünsche mir, dass
ich systematischer begonnen hätte.
Lösungsansatz
Systematisch ist es, zuerst ganz die Lösung zu skizzieren und sie mit
Schlaglichtern grob auszuleuchten. In welcher Hinsicht kann auf der
Ebene des Lösungsansatzes schon eine Entscheidung treffen, die einen
Rahmen aufspannt, in dem sich dann das Modell bewegt? Zumindest bie-
tet sich hier die Gelegenheit, zentrale Begriffe zu finden und in Beziehung
zu setzen, d.h. eine Domänensprache zu etablieren.
Als UI-Technologie akzeptiere ich die Konsole. Weitere Technologien gibt
es nicht zu bedenken. Keine Persistenz, keine Kommunikation sind nötig.
Die Darstellung eines Spielstands ist auf der Konsole eine Fleißarbeit,
etwas nervig, aber ansonsten kein Problem.
Die Musik spielt bei dieser Aufgabe in der Domäne, im Kern der Anwen-
dung.Spielsteine aufSpielfeldern desSpielbretts zuplatzieren,solltedabei
auch nicht das Problem sein.
Nach jedem Zug eines Spielers müssen jedoch Regeln beachtet werden,
auch wenn es nur wenige sind:
• Welcher Spieler ist als nächstes dran bzw. wer ist der aktuelle
Spieler?
• Ist durch einen Zug das Spiel beendet worden? Es kann unentschie-
den enden oder mit einem Spieler als Gewinner.
Spielerwechsel
Die Spieler wechseln sich bei erfolgreichen Zügen ab. Es beginnt immer
Spieler X, darauf folgt Spieler O, dann wieder X usw. bis zum Spielende.
Der aktuelle Spieler kann mithin aus der Anzahl der getätigten Züge
bestimmt werden: 1. Zug: X, 2. Zug: O, 3. Zug: X usw. X ist dran, wenn
ein ungerader Zug zu tätigen ist bzw. wenn die Zahl der schon getätigten
Züge gerade ist.


---


<!-- Page 526 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 517
Spielende
Unentschieden ist das Spiel, wenn alle Spielfelder besetzt sind, ohne dass
eine Gewinnsituation für einen Spieler eingetreten ist. Es könnte schon
vorher als unentschieden deklariert werden, wenn nämlich keine Gewinn-
konstellation mehr durch verbleibende Züge erreicht werden kann; das
scheint mir jedoch recht kompliziert und für diese Aufgabe nicht nötig.
Das verschiebe ich lieber auf einen sehr, sehr langen Winterabend ohne
sonstige Kurzweil.
Gewonnen ist das Spiel, sobald alle Felder in einer Reihe des Spielbretts -
vertikal, horizontal oder diagonal - von Steinen eines Spielers belegt sind.
Das Spielbrett ist eine Matrix bestehend aus Spielfeldern, die über ein Ko-
ordinatensystem mit Spalten und Zeilen adressiert werden: das Spielfeld
links oben hat die Koordinate A1, das in der Mitte ist B2 usw.
Ich denke, das die Spieler ihre Steine durch Angabe einer Spielfeldkoordi-
nate setzen sollten.


---


<!-- Page 527 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 518
Das Domänenmodell
Aus der kurzen Reflexion über die Spielregeln nehme ich mit, dass die
Domäne zweigeteilt ist:
• Es gibt ein Domänendatenmodell, das das Spielbrett repräsentiert.
Das Spielbrett kann als Datenstruktur mit bestimmten Eigenschaf-
tenaufgefasstwerden(Stichwort:ADT).HierkannZugriffgewährt
und Konsistenz gesichert werden.
• Es gibt Domänenregeln, die es durchzusetzen gilt. Zu einem Teil
geschieht das mit der Datenstruktur. Doch die Datenstruktur ist
eben nur eine Struktur. Sie kann melden, dass kein Platz mehr ist
für einen weiteren Zug. Doch ihre Aufgabe ist nicht, das zu deuten
imSinneeinesSpielendes.Dafürsollteeinseparater“Regelwächter”
zuständig sein, ein Schiedsrichter. Der sagt an, ob das Spiel beendet
ist oder noch weitergeht und wer der aktuelle Spieler ist.
Das Domänendatenmodell
Die Benutzer sehen ein zweidimensionales Spielbrett. Das bedeutet nicht,
dass eine zweidimensionale Datenstruktur in der Domäne zum Einsatz
kommen muss. Eine naive mainstream Objektorientierung mag das na-
helegen - doch es gibt keinen Grund, die sichtbare Welt 1:1 im Code
zwangsläufig abzubilden.
WelcheDatenstrukturauchimmerinternzumEinsatzkommenmag,muss
am Ende in etwas für die Spieler verständliches übersetzt werden. Das ist
klar. Das UI generiert eine Projektion in Form einer Matrix.
Sollte deshalb jedoch intern auch eine Matrix das Domänendatenmodell
der Wahl sein? Ich entscheide mich aus zwei Gründen für ein Nein.
1. Da ich gar nicht so genau weiß, wie meine Implementation ausse-
hen wird und was womöglich noch für Anforderungen kommen
mögen, ziehe ich eine Datenstruktur vor, die flexibel und offen ist
für viele Entwicklungswege.
2. Eine Matrix mag oberflächlich passend erscheinen - doch sie wird
dem Grundcharakter des Spiels gar nicht gerecht. Der ist nämlich
der einer Entfaltung. Das Spiel entfaltet sich in der Zeit in Form


---


<!-- Page 528 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 519
einer Sequenz von Zügen. Die Spieler sehen auf dem Spielbrett
davon zwar immer nur den aktuellen Zustand - warum sollte das
aber den Code limitieren? Wenn du Profischachspieler beobachtest,
wirst du feststellen, dass die nicht zufrieden sind mit einem aktuel-
len Zustand: Sie notieren vielmehr die Züge in ihrer Chronologie,
um später das Spiel in seiner Dynamik nachvollziehen zu können.
Für mich ist das Domänendatenmodell also keine Matrix, sondern eine
ListevonZügen.²⁴⁵DiewerdeninderReihenfolge,wieSpielersiemachen,
aufgezeichnet mit ihren Spielfeldkoordinaten. Das ist alles. Daraus sollte
sich jederzeit alles “berechnen lassen”, z.B. der aktuelle Spieler oder ein
Gewinn oder die Spielbrettkonfiguration.
Die Zugliste
1 (0,0)
2 (1,1)
3 (1,0)
entspricht z.B. dieser Spielbrettkonfiguration:
²⁴⁵Wenn du hier einen Anklang an das Konzept event store heraushörst, dann zurecht.
Ich bin ein großer Freund davon und halte es für unterbewertet. Aber hier werde ich nicht
weiterdaraufeingehen.“ListevonZügen”ohneweitereEreignissesollreichen.


---


<!-- Page 529 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 520
Interessanterweise tut das aber auch diese Liste:
1 (1,0)
2 (1,1)
3 (0,0)
Du siehst also, dass eine Zugliste mehr Informationen enthält als eine
Matrix. Und wer bin ich, dass ich mehr Informationen so früh in einem
Projekt ausschlagen würde? Wer weiß, wohin sich das alles noch entwi-
ckeln wird…
Modell
Es handelt sich um eine Konsolenanwendung. Ich könnte daher wie
üblich einen Datenfluss bei main starten lassen. Die Gliederung ist doch
naheliegend:


---


<!-- Page 530 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 521
• Spiel starten
– Datenstruktur/Brett initialisieren
– Noch leeres Brett anzeigen
• Die Spieler spielen lassen
– Spielzug vom aktuellen Spieler erfragen. Das passiert immer
wieder. Wahrscheinlich wird hier ein Stream nötig sein.
– Spielzug ausführen unter Anwendung aller Regeln.
– Aktualisierts Brett anzeigen - oder einen Fehler, falls etwas
nicht mit dem Zug gestimmt haben sollte.
IchkönntedenZerlegungsbaumnochtiefertreiben,docherstmalhalteich
an,ummireinenÜberblickzuverschaffen.Istdasplausibel?Lässtsichdas
gut darstellen? Das Gefühl ist bei größeren Szenarien normal: Du willst
die nicht “in einem Rutsch durchentwerfen” von einer Datenflusswurzel
bis zu allen Operationen. Du arbeitest dich besser schrittweise heran. Das
kann von oben nach unten sein, vom Groben zum Feinen. Manchmal sind
dir aber auch Abschnitte irgendwo im Baum schon klar als eigenständige
Verantwortlichkeiten.
High-level Datenfluss
Mein erstes grobes Modell für den Zerlegungsbaum sieht so aus:
Da ich es vor mir habe, gefällt es mir aber nicht. Irgendwie passt es nicht
zur Natur der Anwendung. Ich habe im Lösungsansatz ja einen großen
Bereichidentifiziert,denichimModellnichtsehe:dieDomäne.Dakönnte
ich noch nachschärfen mit Modulkästen um die Funktionseinheiten, doch


---


<!-- Page 531 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 522
das kommt nicht stringend vor. Umgekehrt müsste ich anfangen mit den
großen identifizierten Bereichen.
Ich versuche es nochmal und benutze mal EBCs auf dieser hohen Abstrak-
tionsebene. Viel Datenfluss gibt es ja gar nicht, der in seinen Feinheiten
zu verfolgen wäre.
Ja, das gefällt mir besser. Große Blöcke für grobe Verantwortlichkeiten.
Dass es zwischen denen nun “Rückflüsse” gibt, ist nicht schlimm; so ist
das halt beim Wechsel von Verben auf Substantive, von Verhalten auf
Dinge. Wie gesagt: Es gibt auch keine ausgefeilten Datenflüsse sondern
im Grunde nur einen der beim UI seinen Ausgang nimmt als Produzent
von Zügen, über die Domänenlogik fließt und dann wieder ins UI, wo das
Ergebnis angezeigt wird.
Um die Schleife zu vermeiden, kannst du dir das UI auch zweigeteilt
vorstellen bestehend aus:
• Editor/Collector: Sammelt die Eingaben vom Benutzer, lässt den
Benutzer Eingabedaten bearbeiten.
• Projektor: Zeigt Ausgaben der Verarbeitung der Eingaben in einer
Form an, die dem Benutzer nutzt.
Wenn Anwendungen größer werden, mag es angezeigt sein, diese zwei
Seiten eines UI strukturell zu trennen. Hier sehe ich das aber nicht als
nötig an. Eine Klasse für beides wird reichen.


---


<!-- Page 532 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 523
Allerdings hängt der Spielstart noch etwas in der Luft. Den ordne ich am
besten auch visuell konsequent auf dieser Ebene dem Spiel unter:
Das Programm startet beim Spiel, lässt Daten zum UI fließen, dessen
Output wiederum ans Spiel gehen, das einen neuen Spielstand generiert,
den das UI anzeigt usw. usf. bis zum Spielende und damit Programmende.
An dieser Stelle mache ich mir auch schon Gedanken dazu, wie denn
der Spielstand dem UI kommuniziert wird. Das interne Datenmodell der
Domäne hat hier nichts zu suchen. Das UI soll von solchen Details unab-
hängig sein und sich keine große Mühe machen müssen, den Spielstand
anzuzeigen.ImmerhinistUI-Logiknotorischschwierigzutesten;siesollte
deshalb so dünn wie möglich sein.
Im Spielstand{} als Teil des Kontrakts zwischen UI und Spiel-Domäne


---


<!-- Page 533 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 524
findestdudeshalbendlichauchmaleinSpielbrettals3x3-Matrix.²⁴⁶Deren
Elemente können drei Zustände annehmen: entweder ist ein Spielfeld leer
oder es ist mit einem X-Spielstein besetzt oder mit einem O-Spielstein.
Das UI soll natürlich nicht ins Rätseln kommen, was eine Spielbrettkon-
figuration bedeutet. Deshalb enthält der Spielstand auch noch die Meta-
Information ob bzw. wie das Spiel beendet ist oder welcher Spieler dran
ist. Dafür soll ebenfalls eine Enumeration zum Einsatz kommen.
Port-Datenflüsse
Soweit das Modell auf einem hohen Abstraktionsniveau. Bei der Größe
dieses Projektes gehe ich anders vor als sonst. Oder zumindest dokumen-
tiere ich es für dich anders. Bisher habe ich dir komplette Modelle gezeigt
und dann vielleicht erklärt, wie ich dahin gekommen bin. Jetzt wäre es
mir zu groß, um das auch zu tun. Also nehme ich dich mit auf die Reise
der schrittweisen Verfeinerung.
Was liegt unterhalb der EBCs? Wie sind die intern aufgebaut? Mit Flow-
Design können wir und müssen wir ganz leicht zwischen Außenansicht
und Innenansicht wechseln. Eine Integrierten Schaltenkreis (engl. inte-
grated circuit (IC)) machst du nicht auf; du bist froh, dass du dich mit
den Details nicht beschäftigen musst. Den hast du ja aber auch nicht
gebaut, sondern gekauft. Das Modell hingegen musst du selbst bauen und
sozusagen selbst ICs definieren; UI{} und Spiel{} sind solche ICs.
Datenfluss-Wurzeln innerhalb von EBCs
Zuerst zoome ich den Projektionsaspekt der Benutzerschnittstelle hinein:
²⁴⁶Spielstanddrücktsehrpassendaus,worumesgeht:Umetwas,dassteht,sichalsonicht
bewegt.DerSpielstandisteinSchnappschussvoneinemSpielinBewegung.


---


<!-- Page 534 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 525
Das Spiel produziert Nachrichten aufgrund zweier Reize: bei Spielstart
und für jeden Zug. Beides aktualisiert den Spielstand, der angezeigt
werden muss. Oder der Zug kann nicht ausgeführt werden; dann wird
ein Fehler gemeldet.
Aus den Ports der EBCs sind jetzt Funktionseinheiten geworden. Die las-
sen sich im Weiteren verfeinern; sie sind die Wurzeln für die Datenflüsse
der EBCs.
Der Spielstart ist der Beginn. Aber woher kommt der Zug? Das UI{}
verdient hier eine weitere Detaillierung:


---


<!-- Page 535 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 526
Ein Zug wird immer vom Benutzer erfragt, wenn eine Anzeige erfolgt ist.
Oder genauer: Eigentlich muss Zug erfragen nur einmal angestoßen
werden nach der ersten Anzeige und produziert fortan einen Strom von
Zügen.²⁴⁷
Damit ist die genauere Zusammenarbeit zwischen UI und Spiel geklärt.
Ich bin ein Stratum tiefer gegangen unterhalb die EBCs. Die Wurzeln für
non-EBC Datenflüsse sind jetzt beieinander.²⁴⁸
Intergrationen verfeinern
Das Modellieren ist im Grunde eine Fleißarbeit. Wenn du erstmal einen
Einstieg hast, dann leitet der dich weiter und weiter in die Tiefe - bis du
genügend Klarheit gewonnen hast. Der Lösungsansatz das Stratum mit
den EBCs war im Grunde das Schwierigste. Von da an folge ich nur dem,
was darin an “offenen Punkten” gelistet ist; das sind zunächst die Ports,
nun sind es die Wurzel-Funktionseinheiten und so wird es weitergehen.
Am Ende muss ich nur an allem einen Haken haben, der anzeigt “Ich habe
das betrachtet und verfeinert oder für fein genug erachtet.” Alles muss
entweder als Integration oder Operation gekennzeichnet sein.
In den vorherigen Diagrammen zeigen das schon die Farben an. Rot steht
wie früher schon für Operation; da bin ich mit der Verfeinerung am Ende.
Grün steht für Integration und ich muss noch tiefer bohren.
Da fange ich doch am besten am Anfang an beim Starten:
²⁴⁷Ob du einen Stream von Zügen erzeugst, die Kontrolle also inZug erfragen bleibt,
oder ob du pro Signal von Anzeigen nur einen Zug erfragst, ist für das Modell nicht so
wichtig;imModellistbeidesverständlich.InderImplementationjedoch,wenndusynchron
programmierst,wäreesnichtsoschön,nureinenZugzuerfragen;irgendwiemüsstedasja
mehrfach geschehen. Also ist entweder eine Schleife nötig, die das Modell nicht zeigt (dark
logic)odereineRekursion.DeshalbbinicheherfüreinenStreamimModell.Duwirstunten
sehen,wieichesimDetailimplementierthabe.
²⁴⁸DusiehstdasMuster,wieichdieseVerfeinerungderEBCsvorgenommenhabe,oder?
IchbinandenPortsentlanggegangenundhabefürjedeneineFunktionseinheitherausgezo-
gen.ManchmalverbindeteineFunktionseinheitInput-PortundOutput-PorteinerEBC,z.B.
Starten;manchmalgehörenInput-undOutput-PortaberauchzuzweiFunktionseinheiten,
dieeinentop-levelFlussimEBCbilden,z.B.Anzeigen+Zug erfragen.Aufderobersten
Ebene sind EBCs eigentlich nicht komplizierter. Wenn sie viele Ports haben, gehören dazu
zwar auch viele Funktionseinheiten, doch die liegen im Grunde meist mehr oder weniger
unverbundennebeneinander.Dasistdannnichtschwierigzuverstehen.


---


<!-- Page 536 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 527
Wie ich auf die einzelnen Stationen im Datenfluss komme, kann verschie-
dene Wege gehen:
• Ich schaue mir an, ob der Input zum Output passt. Meistens nicht,
also frage ich mich, welchen ersten Schritt ich tun kann, um dem
Output näher zu kommen. Ich treibe den Datenfluss von links nach
rechts, d.h. downstream voran. Schrittweise nähere ich mich der
Ausgabe an.
• Ich schaue mir an, ob der Output zum Input passt. Meistens nicht,
also frage ich mich, was ein guter Input wäre, um den Output
herzustellen. Ich treibe den Datenfluss von rechts nach links, d.h.
upstream voran. Schrittweise nähere ich mich der Eingabe an.
• Manchmal springe ich auch mitten hinein und “weiß einfach”, dass
einbestimmterProzessschrittnötig istoderwünschenswert.Dasist
z.B. bei der Verarbeitung von Listen oft der Fall, wo ich sofort sehe,
das es eigentlich um die Transformation einzelner Elemente geht.
Oder es ist der Fall, wenn mir ins Auge springt, dass eine Transfor-
mation einen Kern hat (Domäne), der von Infrastrukturbelangen
eingefasst wird (Peripherie, z.B. Benutzerschnittstelle, Persistenz,
Kommunikation). Dann konzentriere ich mich darauf, zuerst die
ArbeitsweisedesKernsnäherzubeschreiben-derRestdrumherum


---


<!-- Page 537 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 528
wird dann dazu passend gestaltet.²⁴⁹
Im vorliegenden Fall ist mir sofort klar, dass eine interne Datenstruktur -
das Domänendatenmodell - initialisiert werden muss. Das ist die Zugliste
aus dem Lösungsansatz. Die Initialisierung zeigt mit der “kleinen Tonne”
an, dass dahinter ein Zustand steht; den werde ich woanders sicher
wiedersehen.
Und woher kommt der Spielstand{} als Output von Starten? Der
wird sicherlich aus dem Domänendatenmodell generiert. Aber soll dafür
die Spielstandermittlung auch von den Domänendaten abhängig sein? Ich
entscheide mich dagegen. Ich möchte den fan-in des Domänendatenmo-
dells so klein wie möglich halten; jede Abhängigkeit mehr fordert ja auch
ein Mehr an Stabilität ein. Also geht an die Spielstandermittlung nur die
Liste der Züge; das mag ein kleiner Unabhängigkeitsgewinn sein, aber ich
glaube, es ist einer.
Starten ist jetzt verfeinert. Dabei ist eine Integration entstanden. Soll
ich jetzt schon in die eintauchen? Nein, ich entscheide mich dafür, in der
Breitevorzugehen.ImStratum,zudemStartengehört,gibtesnocheine
weitere Integration, die ich mir zuerst anschauen will.
²⁴⁹IndemFallentstehtmanchmalauchsoforteinganzerDatenflussalsMuster.Oderich
versuche, das konkrete Problem passend zum Muster zu denken/formulieren. Ein typisches
Musterist:lesen+verarbeiten+schreiben.


---


<!-- Page 538 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 529
Einen Zug aufzuführen bedeutet, den Spielstein auf dem Brett zu plat-
zieren - bzw. ihn im Domänenmodell, wo es kein Brett als Matrix gibt,
sondern nur eine Liste von Zügen, zu registrieren - und dann den sich
ergebenden Spielstand zu ermitteln.
Hier siehst du schon wieder die “kleine Tonne” für den Zustand. Über sie
sindZug registrierenundZüge initialisierenverbunden;des-
halb gehören beide Funktionseinheiten ganz natürlich zur selben Klasse:
Zugliste{}.
Damit ist die nächste Ebene der Verfeinerung abgeschlossen. Alle vor-
herigen Integrationen sind jetzt aufgeschlüsselt. Dabei sind allerdings
weitere Integrationen entstanden. Denen muss ich mich nun widmen.
Weil die Zugliste als Datenstruktur so konkret ist, will ich dort als erste
hinuntersteigen.Ichglaube,dakommeichamehestenaufdenBodeneines
Datenflusses, die Operationen.
Für mich besteht die Registrierung aus zwei Aspekten: der Validierung
und der tatsächlichen Eintragung in die Zugliste. Letztere ist trivial; der
Zug muss “physisch” an die Liste angehängt werden. Die Valdierung


---


<!-- Page 539 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 530
vorher soll feststellen, ob das aber den Regeln entspricht, die das Domä-
nendatenmodellrepräsentiert.EsstehtfüreinBrett,aufdemnichtbeliebig
Steine platziert werden können. Die Validation passt zumindest auf, dass
nicht zwei Steine auf demselben Feld landen.
Wieviel Logik das am Ende ausmacht, weiß ich nicht. Für beide Aspekte
nehme ich zumindest an, dass sich eine weitere Verfeinerung nicht lohnt.
Eventuell bin ich sogar schon zu tief gegangen und es im Code gar keine
zwei Funktionen dafür geben. Zumindest habe ich mir aber die Aspekte
klar gemacht; so vergesse ich sie nicht.
Die andere bis jetzt verbliebene Integration ist die Ermittlung des Spiel-
standes. Sie taucht mehrfach auf. Ich habe sie bis jetzt vor mir herge-
schoben, weil sich darunter der Löwenanteil der Domänenlogik aufhalten
wird.
Aber ich vertage die Verfeinerung der Domäne noch etwas, indem ich
sie erstmal trenne vom Aufbau der Spielstand{}-Datenstruktur. Ich
denke upstream und frage mich, woher der Spielstand{} kommt: In
ihm steckt einerseits die Zugliste, die zum Brett wird. Andererseits steckt
darin der Status, d.h. ob das Spiel schon beendet ist oder welcher Spieler
dran ist. Beide strukturellen Bestandteile des Output lasse ich erstmal


---


<!-- Page 540 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 531
einfach generieren und dann zusammenfügen.
Die Transformation der Züge in einer Spielbrett ist eine Formalität, denke
ich; das kann ich mit einer Operation abhandeln. Aber die Statusermitt-
lung ist nun wirklich, wirklich der Kern der Domänenlogik.
Letztere siedle ich deshalb gleich im Schiedsrichter{} an. Erstere
gehört für mich zum Mapping{}. Damit bezeichne ich eine Datenstruk-
turtransformation ohne Domänenlogik. Solches Mapping findet immer
an Schnittstellen statt: Hier ist das die Schnittstelle zwischen Domäne
(Spiel{}) und Peripherie (UI{}). Das Mapping muss dafür Datenstruk-
turen aus beiden Welten kennen.
Einerseitsistdasmisslich,weilesdamitstarkabhängigist.Andererseitsist
genau das sein Zweck. Das Mapping ist abhängig, damit andere Aspekte
unabhängig sein können. Das Mapping zieht eine Trennwand ein. Es
isoliert zwei Programmbereiche von einander. Das Domänendatenmodell
kannsichjetztändernundjenseitsdesMappinghatdaskeinenEffekt;um-
gekehrt kann sich der Spielstand{} ändern und die Domäne bekommt
davon nichts mit.
Ja, ich weiß, Mapping ist nervig. Mapping scheint auch oft unnütz, wo es
doch tolle Frameworks gibt, die es dir erlauben, Daten von der Persistenz
durchdieDomänenlogikbiszumUIeinfachdurchzureichen.O/R-Mapper
und data binding im Frontend sind technologische Meisterleistungen.
Aber ich rate zur Vorsicht. Ich war davon auch mal begeistert und habe
es gern auf Entwicklerkonferenzen vorgestellt. Welche Produktivität sich
damit erzielen lässt! Kurzfristig. Denn ich glaube inzwischen, dass es sich
dabei langfristig um sehr problematische Vereinfachungen handelt. Die
Effizienz, die du damit bekommst, bezahlst du teuer mit Inflexibilität.
Deshalb habe ich mich für dieses Beispiel auch ganz bewusst für so unter-
schiedliche Datenstrukturen im Kern und an der Peripherie entschieden.
Langfristigfahreichdamitbesser;dabinichmirsicher.Undgenaudarum
geht es ja bei Flow-Design: langfristig höhere Produktivität.
Abschließend die Verfeinerung der Spielstandermittlung. Damit komme
ich hoffentlich am Boden der Datenflusshierarchien an:


---


<!-- Page 541 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 532
Den Spielstand zu ermitteln bedeutet, festzustellen, ob ein Spielende
vorliegt oder - falls nicht -, den aktuellen Spieler zu ermittteln. Und ein
Spielende liegt vor, wenn das Spiel entweder unentschieden ist oder ein
Spieler gewonnen hat.
Das ist doch alles naheliegend, oder?
Alles zusammen gehört zum Verhaltensaspekt der Domäne. Ich subsum-
miere es komplett unter dem Schiedsrichter{}. Solange nicht z.B. die
Spielendebestimmung zu großen Mengen Domänenlogik führt, kann es in
derselben Klasse implementiert werden.
Tatsächlich bin ich damit bei Operationen über die ganze Ausdehnung
aller Datenflüsse angekommen. Die Zerlegung ist abgeschlossen. 100%
sicher muss ich dabei ja auch nicht sein. Es kann passieren, dass ich in
der Codierung merke, dass ich irgendwo zu weit zerlegt habe. Oder ich
stelle fest, dass weitere Zerlegung nötig ist. Vorstellen könnte ich mir das
bei der Gewinnfeststellung. Für den Moment fühle ich mich ganz wohl.
Wenn ich die Modellschnippsel zusammenfüge, kommt ein Gesamtbild
heraus. Auch wenn ich gewiss war, dass ich nichts vergessen hatte, ist
es gut, das nochmal im Überblick zu sehen: alle Integrationen haben


---


<!-- Page 542 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 533
eine Verfeinerung erfahren. Die Linie verbinden sie über die Ausschnitte
hinweg.
Wenn in einem Datenfluss auf einer Ebene eine Integration die unterste
Ebene darstellt, dann erfordert das eine Verfeinerung an anderer Stelle.
Dort ist die Integration dann die Wurzel. Deshalb wiederholen sich die
Integrationen in den Ausschnitten. Die Linien stellen nur die Beziehung
zwischen den potenziell mehreren “Nutzungsorten” und der Verfeinerung
her.
Keine Integration ist ohne solche Beziehung oder ist direkt in einem
Ausschnitt verfeinert. Damit bin ich zufrieden.
DieModularisierunghabeichnebenbeigemacht.Siewarnaheliegendbzw.
hat sich aus dem Lösungsansatz natürlich ergeben. Hier und da gibt es
vielleichtnochUnschärfe,dochdasistegal.Ichbinzuversichtlich,dassich
in der Codierung nachschärfen kann; die Abweichung zum Modell wird
nicht gravierend sein. Am Ende liegt die Wahrheit selbstverständlich im
Code.


---


<!-- Page 543 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 534
Implementation
Das Modell liegt in all seiner Schönheit nun vor mir. Es zu entwerfen
warschonetwasumfangreicheralsbeidenvorhergehendenBeispielen.Es
zu implementieren wird deshalb auch mehr Aufwand sein - selbst wenn
ich es in Bezug auf die Module und Kontrakte nur “runtercodieren” muss.
Die Logik hier und da erfordert doch noch etwas nachdenken oder sogar
weitere Verfeinerung der Datenflusshierarchie.
Ich könnte jetzt von oben nach unten oder von unten nach oben oder von
links nach rechts codieren. Am Ende muss ohnehin alles erledigt werden.
Doch wenn ich in dieser Weise codiere, bekomme ich auch erst am Ende
Feedback dazu, ob das Modell zu etwas Lauffähigem, Nützlichem führt.
Selbst wenn ich die Phasen wasserfallartig durchfließe von der Anforde-
rungsanalyse über den Entwurf zur Codierung, weil jede für sich nicht
vielZeitinAnspruchnimmt,stockeichjetztbeiderImplementierung.Die
“in einem Schwung” ohne Stopp, ohne Feedback durchzuziehen, schmeckt
mir nicht. Da fühle ich mich unsicher.
Ich entscheide mich deshalb dafür, das Gesamtmodell inkrementell in
den Gesamtcode zu überführen. Die Inkremente schneide ich so, dass
schrittweise etwas wächst, mit dem ich mehr und mehr anfangen kann.
Das Spiel wird immer vollständiger, leistungsfähiger.
Die komplette Realisierung der Anforderungen mit Entwurf und Co-
dierung ist für sich genommen ein großes Inkrement. Innerhalb dieses
Inkrements gehe ich nun wieder und feiner inkrementell nur in der Codie-
rung vor. Analyse und Entwurf sind für die kompletten Anforderungen
abgeschlossen;dieCodierungerfolgtaberscheibchenweise.Warumnicht?
Inkrementelles Vorgehen ist kein Selbstzweck. Es verzögert die Fertigstel-
lung. Das ist natürlich gewollt, wenn man inkrementell vorgeht. Dadurch
entsteht Feedback zwischendurch und es besteht die Möglichkeit für
Kurskorrekturen. Wenn das jedoch nicht nötig oder möglich ist, dann
lohnt auch inkrementelles Vorgehen nicht.
IchsehedenBedarfjetzterstbeiderImplementation.Allemaljaauch,weil
kein Kunde da ist, dem ich schon früher hätte Ergebnisse zum Feedback
hätte vorlegen können. Inkrementelle Anforderungsanalyse oder Model-
lierung hätten keinen Sparringpartner gehabt. Doch bei der Implemen-
tierung bin ich mir selbst der Sparringpartner und Feedbackgeber. Mein


---


<!-- Page 544 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 535
ModellistderPlan,vondemichnichtsichersagenkann,dassersichauch
so umsetzen lässt. Inkrementelle Codierung bekommt also durch den von
mir selbst erstellten Plan Feedback. Ich als Planersteller merke, ob ich mit
dem Plan auf dem gelben Ziegelsteinweg in die Smaragdstadt bin - oder
auf dem Holzweg.
Als Inkremente nehme ich mir vor:
1. Initialisierug und Darstellung des Spielbretts. Damit setze ich zu-
mindest die grobe Struktur im obersten Stratum auf. Spiel{} und
UI{} müssen verdrahtet werden.
2. Zug erfragen und Spielstein immer platzieren; kein Spielerwechsel,
keine Spielendeerkernnung. Damit bekomme ich grundsätzliche
Interaktivitätundsehe,VeränderungenaufdemSpielbrett.DieZug-
Koordinatemussichwohlhierauchschonvalidierenundungültige
Koordinaten abweisen, z.B. X1 oder A7.
3. Nach jedem Zug wechselt der Spieler. Die gesetzten Spielsteine
wechseln jetzt systematisch und das Prompt für die Zugeingabe
fordert den aktuellen Spieler auf.
4. Zug validieren. Jetzt wird geprüft, ob ein Zug noch auf dem Spiel-
brett platziert werden darf; das ist ja nur der Fall, wenn das Feld
nicht belegt ist. Das ist eine Sache der Domäne.²⁵⁰ Wenn der Zug
invalide ist, wird dem Benutzer eine Meldung gezeigt.
5. Unentschieden feststellen. Da jetzt spielerspezifische Züge möglich
sind, kann ich jetzt ein Unentschieden leicht feststellen: alle Felder
auf dem Spielbrett sind belegt.
6. Gewinn feststellen. Die Gewinnfeststellung erfordert einige Logik.
Die spare ich mir bis zum Schluss auf, wenn ich schon sichtbar
einige Codierungserfolgs eingefahren habe.
²⁵⁰DieKoordinatenüberprüfungwareineSachederBenutzerschnittstelle,damitderKon-
traktzwischenUI{}undSpiel{}eingehaltenwird.DazugehörtdersyntaktischeAspekt,
dass die Spielfeldkoordinaten des Zugs als int-Tupel übergeben werden. Dazu gehört aber
auch der semantische Aspekt, dass diese Zahlenwerte für Spalte und Zeile in bestimmten
Wertebereichenliegen(jeweils0..2).IndemichdenKontraktmiteinemint-Tupelgestaltet
habe, brauche ich diese semantische Validation. Hätte ich stattdessen eine Enumeration
definiert, die nur valide Koordinaten enthält - z.B. enum Spielfeldkoordinaten{A1,
A2, A3, …, C3} -, dann hätte ich das semantische Problem eliminiert. Diese Festlegung
schien mir jedoch zu hart; lieber lebe ich mit einem flexibleren Kontrakt und etwas mehr
LogikimUI{}.


---


<!-- Page 545 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 536
Bei der Planung der Inkremene fällt mir auf, dass das Modell in einer
Hinsicht falsch ist:
Es ist inkorrekt, die Unentschieden-Prüfung upstream von einer Gewinn-
Prüfung stattfinden zu lassen. Wenn der 9. Spielzug zu einem Gewinn
führt,würdezuerstunentschiedenfestgestelltunddasSpieldamitbeendet.
Stattdessen muss zuerst auf Gewinn geprüft werden - und nur, wenn der
nicht vorliegt, kann es sein, dass dennoch das Spiel beendet ist, weil der 9.
Zug gemacht wurde.
Darauf muss ich bei der Codierung spätestens in Inkrement 6 achten.


---


<!-- Page 546 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 537
Inkrementelle Implementierung
LeiderkannichdieinkrementelleCodierunghiernichtmitdirgemeinsam
durchlaufen. Aber einen Eindruck vom zeitlichen Ablauf will ich dir mit
einem Auszug aus meinem Git Commit-Log geben:
Auffällig daran ist einerseits der zeitliche Abstand der Commits.
• “Inkrement 6” hat mit der hauptsächlichen Domänenlogik nur 15
Minuten gedauert? Nein. Ich habe die Gewinnfeststellung stark
abgekürzt und prüfe nur darauf, ob das Feld B2 besetzt ist. Den
größten Teil des Inkrements hat eine Refaktorisierung im Zusam-
menhang mit der Unentschieden-Prüfung eingenommen.
• Für “Inkrement 2 u 4” habe ich nicht wirklich so lange gebraucht.
Zwischen 11:06 und 13:56 habe ich eine ausgiebige Mittagspause
mit Einkauf gemacht.
• “Inkrement 3” ist mit knapp 60 Minuten Dauer gelistet. Das ist auch
deutlich mehr, als ich gebraucht habe - glaube ich.
• Inkremente 2 und 4 haben gar keinen Abstand. Habe ich vergessen,
nach Inkrement 2 ein Commit zu machen? Nein, ich glaube, ich
habe vielmehr beide Inkremente so miteinander verbunden, dass
ich nicht erst eines abgeschlossen und dann das andere begonnen
habe.
Andererseits bin ich bei der Implementierung nicht streng nach Plan
vorgegangen. Bei der Implementierung von Inkrement 2 war ich schon
beim Domänendatenmodell zugange, da habe ich die Validierung von In-
krement4gleichmiteingebaut.ImmernochhätteichdieInkrementevom
Commit her trennen können, dass ich jedoch die Reihenfolge verändert
habe, finde ich nicht schlimm.
Eine Planung ist nur eine Planung, d.h. eine Idee davon, wie der Ablauf
sein könnte. Die Planungsschritte sind schon ernsthaft gewählt und


---


<!-- Page 547 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 538
priorisiert. Doch das ist nur eine Hilfe für die Abarbeitung, um während
derer nicht ständig den mentalen Modus zu wechseln. Abwechselnd
Entscheiden und Abarbeiten hat auch einen Multitasking-Overhead. Den
versucht man mit Planung zu vermeiden oder zumindest zu vermindern.
In diesem Fall hatte ich den Plan komplett im Überblick und es kam auch
nicht zwingenddarauf an, das eine nach dem anderenzu tun. Es gab nicht
zwischen allen Inkrementen Abhängigkeiten. Wie du siehst, konnte ich
Inkrement 4 nach vorne vor 3 ziehen. Die weiteren Inkremente waren
allerdings abhängig von Inkrement 3.
Schlaglichter auf den Code
Statt einer chronologischen Entwicklung des Code zeige ich dir Aus-
schnitte aus dem finalen Zustand. Zuerst ein Überblick der Klassen, die
entstanden sind. Keine Überraschungen, denke ich:


---


<!-- Page 548 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 539
Außer: Den Spielstatus{} gibt es zweimal: einmal als Domänendaten-
typen wie hier zu sehen; so hat er weite Gültigkeit. Und einmal als lokalen
Datentypen innerhalb von Spielstand{}:
1 class Spielstand
2 {
3 public enum Spieldfeldbelegungen {
4 _,
5 X,
6 O
7 }
8
9 public enum Spielstatus {
10 XamZug,
11 OamZug,
12 XhatGewonnen,
13 OhatGewonnen,
14 Unentschieden
15 }
16
17 public Spieldfeldbelegungen[,] Brett = new Spieldfeldbelegungen[3, 3];
18 public Spielstatus Status;
19
20 public bool SpielBeendet => Status == Spielstatus.XhatGewonnen ||


---


<!-- Page 549 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 540
21 Status == Spielstatus.OhatGewonnen ||
22 Status == Spielstatus.Unentschieden;
23 }
Warum die Dopplung? Widerspruch gegen DRY? Auch wenn die Form
dieselbeist,habeichmichfürzweiTypenentschieden,weilesebeneinmal
um die Domäne geht - und ein anderes Mal geht es um einen Datentypen
an der Schnittstelle zwischen Domäne und Peripherie. Letzterer soll
entkoppeln. Deshalb darf nicht nur das Spielbrett in zwei Strukturen
vorliegen, sondern auch der Spielstatus. Die Domäne weiß nichts davon,
dass es Spielstand.Spielstatus gibt und umgekehrt. So können
sich beide Seiten unabhängig entwickeln. Ich könnte z.B. entscheiden,
dass ich die Information, wer am Zug ist und den Spielendestatus im
Spielstand{} trenne. Oder umgekehrt. Die jeweils andere Partei muss
sich dann nicht anpassen, sondern nur das Mapping diese Änderung
kaschieren.
Wie du siehst, habe ich auch in den Spielstand{} etwas Logik gelegt,
der es dem UI{} leichter macht, Entscheidungen zu treffen.
Überhaupt die Benutzerschnittstelle… Wie das Modell zeigt, hat die zwei
Seiten: Projektion und Sammlung.
Interessant an der Projektion ist nicht, wie das Spielbrett gezeichnet wird;
vielmehr möchte ich dir zeigen, wie ich pragmatisch mit der Verbindung
zwischen Projektion und Sammlung umgegangen bin: Innerhalb von
Anzeigen() wird zuerst das Spielbrett gezeichnet - und dann wird an
die Erfragung des Zuges weitergeleitet. Ich habe sozusagen kurzerhand
aus Anzeigen() eine Integration gemacht. Das schien mir pragmatisch,
weil letztlich nur einmal der Übergang von dort zur Sammlung relevant
ist.
1 class UI
2 {
3 private bool _geöffnet;
4 private Spielstand _spielstand;
5
6 public void Anzeigen(Spielstand spielstand) {
7 SpielbrettZeichnen();
8 ZugErfragen();
9
10
11 void SpielbrettZeichnen() {
12 ...
13 if (spielstand.SpielBeendet) {
14 Console.WriteLine($"{Spielendemeldung()}");
15 Environment.Exit(0);
16 }
17 _spielstand = spielstand;
18 ...


---


<!-- Page 550 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 541
19
20 string Spielendemeldung()
21 => spielstand.Status switch {
22 Spielstand.Spielstatus.XhatGewonnen => "X hat gewonnen!",
23 ...
24 };
25 }
26 }
27 ...
28 }
Außerdem habe ich das UI{} aufgeladen mit der Verantwortung, das
Programm zu beenden. Wenn das Spielende erreicht ist, schießt das UI{}
sich und alles andere ab. Quasi Apoptose der Softwarezelle.²⁵¹ Auch das
war eine pragmatische Entscheidung. Ordentlicher wäre es natürlich, die
Erkennung dieses Falles nach außen zu melden, so dass außerhalb das
Programm beendet werden kann.
BeiderSammlungsiehstdu,wieichdafürsorge,dassdaswiederkehrende
Signal(nach)derAnzeigenichtdazuführt,dassZugErfragen()indirekt
rekursiv aufgerufen wird: Es gibt ein Flag, das geprüft, ob die Sammlung
schon läuft. Wenn ja, dann wird sie nicht erneut gestartet.
1 class UI
2 {
3 ...
4
5 private bool _running;
6
7 public void ZugErfragen() {
8 if (_running) return;
9 _running = true;
10
11 while (true) {
12 var text = Zugeingabe();
13 if (ZugValidieren(text, out var zug))
14 OnZug(zug);
15 }
16 ...
17 }
18
19 public event Action<(int spalte, int zeile)> OnZug;
20 }
Ansonsten ist die Sammlung zwar eigentlich eine Operation wie die
Projektion, doch ich habe sie zu einem Hybriden gemacht, indem ich in
der Schleife lokale Funktionen aufrufe. So ist der Code verständlich - aber
testwürdig finde ich ihn nicht.
Achte drauf, wie ich die Entscheidung, ob der Zug valide ist, nicht
mittels Continuation übersetzt habe, sondern über das Muster mit bool-
Rückgabewert und out-Parameter.
²⁵¹WaseineSoftwarezelleist,erkläreichdirimnächstenKapitel.


---


<!-- Page 551 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 542
Das Spielals EBC, andas derZug fließt,hält keineÜberraschungenbereit.
Seine Aufgabe ist die Integration und die Haltung des Domänenzustands
in Form des Spielbretts:²⁵²
1 class Spiel
2 {
3 private Spielbrett _spielbrett;
4
5 public void Starten() {
6 _spielbrett = new Spielbrett();
7 var spielstand = SpielstandErmitteln();
8 OnNeuerSpielstand(spielstand);
9 }
10
11
12 public void ZugAusführen((int spalte, int zeile) zug) {
13 if (_spielbrett.Platzieren(zug)) {
14 var spielstand = SpielstandErmitteln();
15 OnNeuerSpielstand(spielstand);
16 }
17 else
18 OnUngültigerZug();
19 }
20
21
22 private Spielstand SpielstandErmitteln() {
23 var spielstatus = Schiedsrichter.SpielstatusErmitteln(_spielbrett.Züge.ToArray(\
24 ));
25 return Mapping.Map(_spielbrett, spielstatus);
26 }
27
28
29 public event Action<Spielstand> OnNeuerSpielstand;
30 public event Action OnUngültigerZug;
31 }
Nur in Zeile 13 kannst du sehen, dass ich schon wieder eine Kontroll-
struktur benutzt habe, um zwischen erfolgreicher Platzierung des Zugs
und Invalidität zu unterscheiden. Wie schon gesagt: Continuations sind
kein Selbstzweck und Prinzipien auch nicht. Behalte dein Augenmaß!
Außerdem gibt es schon genügend Continuations in Form der Events der
EBC-Klassen.
²⁵²ImModellwardasSpielbrettnichtexplizitalsZustandzusehen.ImSpielbrett(bzw.der
Zugliste die zu Spielbrett{} geworden ist) gibt es die Tonne. Die soll helfen, Funktions-
einheitenzufinden,diezusammengehören,weilsiealleaufdiesenZustandzugreifen.Doch
das Spielbrett selbst als Zustand von Spiel{} ist nicht mit ebensoeiner Tonne angezeigt
bei Starten und Zug ausführen. Wie kommt das? Ist das inkonsistent? Nein, das ist
Erfahrung.Esgibtkeine“PflichtzurTonne”.DassIntegrationenohnehinabhängigsindvon
dem,wassieintegrieren,dassistjaklar.InsofernistdasSpielabhängigvoneinemSpielbrett
undz.B.auchdemSchiedsrichter.NuristderSchiedsrichteralsstatischeKlasserealisiert;er
braucht keinen Zustand; also taucht er nicht als Member-Variable von Spiel{} auf. Beim
Spielbrett{} ist das anders. Das ist als Datenstruktur als Instanzklasse realisiert, dafür
gibteseinObjekt,dasbrauchtdannaucheineMember-Variable.EineAnzeigealsTonneist
angesichts dieser Natürlichkeit nicht nötig. Aber darauf folgt z.B., dass auchSpiel{} eine
Instanzklasseseinmuss.


---


<!-- Page 552 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 543
DasMappingfindetamAusgangdesSpielsstatt,wieimModellentworfen.
Wenn ich das hier aber so sehe, dann kommt mir der Gedanke, ob es
Teil des Spiels sein sollte. Das Mapping als Puffer zwischen Domäne
und Peripherie könnte im Datenfluss auch im darüber liegenden Stratum
tatsächlich zwischen ihnen angesiedelt sein. Alternativ könnte es auch
einen Decorator²⁵³ geben, der das eigentliche Spiel mit dem Mapping
umwickelt.
Aber für den Moment bin ich zufrieden. Das passt schon so. Und wenn es
nicht mehr passt… dann ändere ich es. Immer schön locker bleiben…
Wie du dir vorstellen kannst, ist das Spielbrett selbst ganz simpel:
1 class Spielbrett {
2 private List<(int spalte, int zeile)> _züge = ...
3
4 public bool Platzieren((int spalte, int zeile) zug) {
5 if (_züge.Contains(zug)) return false;
6
7 _züge.Add(zug);
8 return true;
9 }
10
11 public IEnumerable<(int spalte, int zeile)> Züge => _züge;
12 }
Es stellt als ADT eine Liste dar, an die nur am Ende angefügt werden
darf mit Platzieren(). Und als weitere Bedingung gilt, dass jeder Zug
in Form einer Spalte/Zeile-Kombination nur einmal in der List stehen
darf. Größenmäßig ist das Spielbrett selbst nicht: beliebig viele Züge mit
beliebigen Koordinaten können eingetragen werden. Mehr Restriktionen
als die vorhandenen wäre Overengineering gewesen. DasSpielbrett{}
existiertfürmichalsonichtimluftleerenRaumundmussgegenalleEven-
tualitäten abgesichert werden. Es ist vielmehr für einen genau bekannten
Kontext gebaut. Dafür leistet es genug.
Und schließlich noch der Schiedsrichter.²⁵⁴ Darin sind die Operationen
nicht so wichtig; wie ein Unentschieden oder ein Gewinn genau festge-
stellt wird, ist Fleißarbeit für die Codierung der Logik. Aber die Integra-
tion mag dich interessieren. Da ist z.B. die Spielstatusermittlung gleich
am Anfang: die hat einen Ausgang, es wird immer ein Spielstatus der
Domäne geliefert, doch intern gibt es zwei Flussarme. Einmal ist das Spiel
²⁵³https://en.wikipedia.org/wiki/Decorator_pattern
²⁵⁴Der Schiedsrichter gehört der Domäne an. Ich habe ihn schon im Modell bewusst
zustandsfreigehalten.EristdeshalbalsstatischeKlassenachdemfunctionalcore,imperative
shell Patternimplementiert.


---


<!-- Page 553 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 544
zuende und damit auch der Status klar; das andere mal ist es noch nicht
zuende und der aktuelle Spieler muss noch ermittelt werden. Mittels einer
Closure²⁵⁵ lasse ich die Continuations den status setzen (Zeilen 6 und
7), der am Ende zurückgeliefert wird. Das ist nötig, weil Continuations ja
stets Funktionen sein sollen, die keinen Rückgabewert haben. Sonst wäre
das PoMO nicht eingehalten.
1 class Schiedsrichter {
2 public static Spielstatus SpielstatusErmitteln((int spalte, int zeile)[] züge) {
3 var status = Spielstatus.Unentschieden;
4
5 SpielendeFeststellen(züge,
6 _ => status = _,
7 () => status = AktuellenSpielerErmitteln(züge)
8 );
9
10 return status;
11 }
12
13
14 static void SpielendeFeststellen((int spalte, int zeile)[] züge,
15 Action<Spielstatus> onSpielende,
16 Action onKeinSpielende) {
17 GewinnFeststellen(züge,
18 onSpielende,
19 () => UnentschiedenFeststellen(züge,
20 onSpielende,
21 onKeinSpielende)
22 );
23 }
24
25
26 static void UnentschiedenFeststellen((int spalte, int zeile)[] züge,
27 Action<Spielstatus> onUnentschieden,
28 Action onKeinUnentschieden) {
29 ...
30 }
31
32
33 static void GewinnFeststellen((int spalte, int zeile)[] züge,
34 Action<Spielstatus> onGewinn,
35 Action onKeinGewinn) {
36 ...
37 }
38 ...
39 }
Anders ist es bei der eingeschachtelten Spielendeermittlung. Sie hat zwei
AusgängewieauchdievonihrintegriertenFunktionenfürdieUnentschieden-
und Gewinn-Prüfung. Deshalb ist dort kein Closure-Klimmzug nötig.
So ist es recht nach der “reinen Lehre”!
Aber - wie wiederholt gesagt - am Ende zählt nicht die eine Regel, das
eine Prinzip, sondern der Zweck und das Gesamtergebnis. Deshalb habe
ich mir erlaubt, von der “reinen Lehre” abzuweichen. Schau hier:
²⁵⁵https://en.wikipedia.org/wiki/Closure_(computer_programming)


---


<!-- Page 554 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 545
1 class Schiedsrichter { // Nicht PoMO-konforme Variante!
2 public static Spielstatus SpielstatusErmitteln((int spalte, int zeile)[] züge) {
3 return SpielendeFeststellen(züge,
4 () => AktuellenSpielerErmitteln(züge)
5 );
6 }
7
8
9 static Spielstatus SpielendeFeststellen((int spalte, int zeile)[] züge,
10 Func<Spielstatus> onKeinSpielende) {
11 return GewinnFeststellen(züge,
12 () => UnentschiedenFeststellen(züge,
13 onKeinSpielende)
14 );
15 }
16
17
18 static Spielstatus UnentschiedenFeststellen((int spalte, int zeile)[] züge,
19 Func<Spielstatus> onKeinUnentschieden) {
20 ...
21 }
22
23
24 static Spielstatus GewinnFeststellen((int spalte, int zeile)[] züge,
25 Func<Spielstatus> onKeinGewinn) {
26 ...
27 }
28 ...
29 }
In dieser Version liefern alle Funktionen immer einen Status als Ergebnis.
Entweder bestimmen sie ihn selbst, z.B. stellt UnentschiedenFest-
stellen() selbst fest, ob ein Unentschieden vorliegt. Oder - und das ist
hierderTrick!-sieerfragendownstreameinenStatus,wennsiesichselbst
nicht zuständig fühlen. Deshalb gibt es nur noch einen Funktionszeiger
und der ist eine Funktion (Func<T>), statt eine Prozedur (Action<T>).
Das PoMo ist jetzt natürlich verletzt. OMG! Jede Funktion weiß, dass von
downstream ein Status zurückfließen muss, dass “dort unten” also etwas
Bestimmtes passiert. Aber ich denke, das ist in diesem Fall ok. Der Code
ist knapper, übersichtlicher geworden, ohne Verständlichkeit einzubüßen,
würde ich sagen. Und hat die Testbarkeit gelitten? Nein. Die Operationen
sind immer noch testbar, denn die Logik, die sie da downstream aufrufen,
wirdjainjiziertundkannimTestdurcheinSurrogatleichtersetztwerden.
Reflexion
Die Aufgabe war nicht ganz klein. Das will ich zugeben. Aber mit
etwasSystematikwarsiedennochgutzulösen.DieFlow-Design-Register
musste ich aber schon ziehen. Und ein bisschen schmutzig ist es auch
geworden.
Genau das will ich dir ja aber vermitteln. So ist das Programmiererleben.
Wir versuchen, uns an Prinzipien zu halten. Wir stehen dafür ein. Wir


---


<!-- Page 555 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 546
geben unser Bestes. Doch hier und da bringt uns etwas Pragmatismus
weiter.
SRP, SLA, IOSP/PoMo, Messaging… all das ist “menschengemacht”. Es
sind gute Ideen in Bezug auf einen hehren Zweck. Es lohnt sich, darauf
zu achten. Auf jeden Fall! Doch am Ende sind es eben unvollständige
und grobe Mittel, die das Denken nicht ersetzen können und sollen.
Du bist weiterhin gefragt mit deinem Urteilsvermögen. Wenn ich auf
IOSP/PoMo so bestehe, dann will ich dir nur für viele Situationen eine
Stütze bieten. In vielen Situation sollst du dein Urteilsvermögen nicht
verschwenden, sondern tatsächlich einer best practice folgen. So sparst
du Kraft für die wirklich kritischen Momente. IOSP/PoMo, Flow-Design,
die ganze radikale Objektorientierung, das schrittweise Vorgehen von
Programming with Ease ist eine Sache der Ökonomie, der persönlichen
Aufmerksamkeits- und Energie-Ökonomie.
DashabeichbeidieserAufgabesehrdeutlichgemerkt.InjederPhasehabe
ich mich unbelastet gefühlt. Ich war nicht überfordert, fühlte mich nicht
im Chaos von so vielen Dingen, die es zu bedenken gilt, sondern war stets
fokussiert.
Abstraktionen habe ich als das genommen was sie sind: Karten. Das
heißt als Pläne, die die Navigation in der Situation erleichtern sollen,
indem sie etwas Vorausschau/Überblick bieten. Doch letztlich sind die
Abstraktionen, die Pläne eben nicht die Realität und müssen sich ihr auch
mal beugen. Ich habe das Modell bei der Codierung angepasst; ich bin
im Code von ehernen Richtlinien abgewichen. Und ich habe die Gangart
gewechselt während der Modellierung und auch für die Codierung.
Das alles diente dem Fortschritt ohne Eingehen von (zu großen) Kom-
promissen. Ich war mir also stets des Spannungsfeldes bewusst zwischen
kurzfristiger Optimierung und Nachhaltigkeit.
Fehlerfrei ist das Ergebnis sicherlich nicht. Das geht nicht bei der Kom-
plexität von Softwareentwicklung. Aber deshalb entwickeln wir ja schon
lange iterativ: weil wir wissen, dass die gute Idee von gestern, spätestens
morgen keine so gute Idee mehr sein wird. Ordnung, Sauberkeit, Nachhal-
tigkeitimCodeistnichts,wasdugeradlinig“fürimmer”herstellenkannst.
Da gibt es immer etwas nachzubessern.
Und insofern musst du auch nicht danach streben, Perfektion beim ersten
Mal zu erreichen. Redliches Bemühen, wirklich redliches Bemühen um


---


<!-- Page 556 of 584 -->


Musterlösung: 07-Flow-Designmit3-dimensionalenDatenflüssen 547
Verhaltenund Testbarkeitund Verständlichkeitund Ordnung,dasistalles,
was du schaffen kannst.
Dass du dieserhalb ein Gefühl für Balance entwickelst, das wünsche ich
dir.


---


<!-- Page 557 of 584 -->


Musterlösung: 08 - Die IODA
Architektur
Eigentlich ist die IODA Architektur kein großes Ding, finde ich. Sie ergibt
sichganznatürlichauchIOSPundPoMo.WenndueinpaarmalmitFlow-
Design Anwendungen entworfen hast, kommst du von selbst auf IODA,
glaube ich.
Dennoch ist es nützlich, diese Brille zu haben. Wenn du durch sie blickst,
kannst du nach Erwartbarem in Code suchen; was du findest, kannst du
kategorisieren. Du siehst, was da ist und was fehlt. Du bemerkst, was gut
separiert ist und wo Aspekte verwachsen sind. Für neue Anwendungen
bekommst du quasi eine Checkliste, woran du denken solltest, wenn nicht
sogar eine Form von Bauanleitung.
1. Software hat eine Benutzerschnittstelle, die Portale. Immer. Sonst
könnte sie nicht benutzt werden.
2. Das Wichtigste einer Software ist aber nicht die Benutzerschnitt-
stelle, sondern die Domäne. Dort werden die Ergebnisse hergestellt,
dieBenutzersehenwollen.DieDomänebestehteinerseitsausLogik
für die Produktion der Resultate, andererseits aus Daten für die
Resultate.
3. Eskannsein,dassdieDomäneHilfebraucht.Danngreiftsiemittels
Providern auf Ressourcen zu, die wiederum für eine Domäne mit
eigener Logik und eigenen Daten stehen.
4. Die Ergebnisproduktion durch Domäne und Provider wird mittels
Processors integriert.
5. Die Anbindung der Ergebnisproduktion an die Portale übernehmen
Interactors.
6. Und das ganze ruht auf einem Fundament aus APIs, die von
Portalen und Provider für den Ressourcenzugriff gebraucht werden,
und ganz allgemein die Funktionen der Logik darstellen.


---


<!-- Page 558 of 584 -->


Musterlösung: 08-DieIODAArchitektur 549
Aufgabe 1 - Umbau nach IODA
Der bisherige Datenfluss und die Modularisierung für Game of Life ist
schon nicht ganz schlecht. Daran müsste ich nicht herumschrauben. Er
folgt dem IOSP mit einer sinnigen Modularisierung.


---


<!-- Page 559 of 584 -->


Musterlösung: 08-DieIODAArchitektur 550
Dass das UI{} hier noch “unten hängt” ist nicht so schlimm; das kann ich
währenddesIODA-UmbausnochkorrigierennachdenErkenntnissenaus
Kapitel 7:
Dafür als erstes eine Bestandsaufnahme: Was ist denn gemäß IODA
Architektur schon da?


---


<!-- Page 560 of 584 -->


Musterlösung: 08-DieIODAArchitektur 551
• Portal(e): UI{}
• Provider: Filesystem{}
• Domäne
– Logik: Evolution{}
– Daten: Welt{}, Zelle{}
Und was ist mit Program{} und Mapping{}?
Program{} ist mit Aufgaben überladen: Dort findet Konstruktion und
Integration statt; die Klasse ist Interactor und Processor zugleich. Das
muss ich entzerren.
Das Mapping{} gehört zur Ressourcenkommunikation. Hier ist zu über-
legen, ob es direkt vom Processor integriert werden sollte oder ob ein
MappingFilesystem{} als Provider auf höherem Abstraktionsniveau
um Filesystem{} und Mapping{} gewickelt werden sollte. Ich denke,
ich versuche es erstmal ohne weiteres Modul. Wenn erstmal ein Processor
eingeführt ist, sind die Abhängigkeiten besser verteilt.
Hier zunächst die Funktionseinheiten der operationalen Klassen in einem
Fluss. Sie sind öffentlich und zu integrieren:
Ob ich bei der Integration von unten nach oben bzw. innen nach außen
vorgehen oder umgekehrt,entscheide ich situativ. Manchmal liegt mir das
eine näher, dann wieder das andere. In jedem Fall bietet mir IODA eine
Ziellinie. Ich muss Interactor und Processor über den Fluss legen.
Ich fange mal unten an, weil ich damit die Frage, ob der Interactor eine
Application oder ein Controller ist, noch etwas hinausschieben kann.
Als erstes trennt der Processor{} das UI{} vom “Rest”. Oder um-
gekehrt, der zentralen Bearbeitungsprozess wird getrennt vom UI{}.
Dadurch reduziert sich das oberste Stratum auf drei simple Schritte: EVA.


---


<!-- Page 561 of 584 -->


Musterlösung: 08-DieIODAArchitektur 552
Dass darunter allerding fünf integriert werden, finde ich etwas viel. Alle-
mal, da der Zusammenhalt zwischen ihnen nicht gleich ist; z.B. hängen
DLAD und WDSE enger zusammen als WDSE und EVOL. Das sollte durch
weitere Integrationen ausgedrückt werden:
Wie oben angekündigt übernimmt der Processor auch diese Integrationen.
Die Zahl der Module muss ja auch nicht mit Macht in die Höhe getrieben
werden. IODA ist mit Processor{} gedient; dem höheren Zusammen-
halt wird mit integrierenden Funktionseinheiten Ausdruck verliehen. Das
reicht an Struktur erstmal.
Jetzt der Interactor: Ist es ein Controller oder eine Application. Es wird
auf keine Benutzereingabe gewartet, deshalb liegt wohl ein Controller
nahe. Andererseits fände ich handle hier nicht als Bezeichnung für die
Integration passend. Da läuft ein Programm einmal ab pro Aufruf. Der
Controllerwirdnichtlängergehostet.Deshalbnenneichdieintegrierende
Funktionseinheit run:


---


<!-- Page 562 of 584 -->


Musterlösung: 08-DieIODAArchitektur 553
Alles, was passiert, wird jetzt durch run repräsentiert. Und das, was
passiert, besteht aus nur drei Prozessschritten. Und davon der wesentli-
che besteht wiederum aus nur drei Prozessschritten. Das finde ich sehr
überschaubar.
Darüber liegt der Vollständigkeit halber noch main im notorischen Pro-
gram{}. Dass hier nur eine Funktionseinheit integriert wird, ist der Rolle
von main geschuldet; es gibt für eine Konstruktion ja im Grunde gar
nichts zu integrieren. Sie Integration bezieht sich also nur auf den Anstoß
der ganzen Verarbeitung über deren Wurzel. Deshalb lässt du main im
Entwurfsalltag auch weg.


---


<!-- Page 563 of 584 -->


Musterlösung: 08-DieIODAArchitektur 554
Was dort konstruiert wird, ist naheliegend:
• Provider und Portale solltest du als instanziierbare Klassen imple-
mentieren. Sie sollten mindestens konfigurierbar, wenn nicht sogar
ersetzbar durch Surrogate sein. Für Ersteres ist ein Konstruktor
nützlich, der einmal die Konfiguration ermöglicht, die dann aus
dem Weg ist. Für Letzteres ist ein Interface nützlich, das nur
Instanzklassen haben können.
• Interactors und Processors werden instanziierbar, weil sie mit den
Instanzen von Providern und Portalen konfiguriert werden.
Die Domäne hingegen ist für mich erstmal nicht unbedingt zu konstru-
ieren. Da sie nichts mit Providern und Portalen zu tun hat, wüsste ich
nicht, warum sie konfigurierbar über einen Konstruktor sein sollte. Eine
Injektion von Abhängigkeiten ist nicht nötig. Im Einzelfall mag ich mich
anders entscheiden, doch das ist erstmal mein Ausgangspunkt.
Wenn Softwarezellen wachsen, ist anzunehmen, dass es weitere integrie-
rende Klassen unterhalb des Processors geben wird. Die können dann in-


---


<!-- Page 564 of 584 -->


Musterlösung: 08-DieIODAArchitektur 555
haltlich näher am Processor sein, also allgemeiner; oder sie sind spezifisch
wie z.B. ein MappingFilesystem{}, das ich oben angedacht hatte.
Das Strukturdiagramm nach dem Umbau sieht nun so aus:
Ich finde das wunderbar ordentlich und gut testbar.
Abhängigkeiten zeigen den
Abstraktionsgradienten hinab
Aber wahrscheinlich brauchst du ein wenig, um dich daran zu gewöhnen.
Am Ende hat mir geholfen, konsequent zu fragen, was Abhängigkeiten
im Allgemeinen und funktionale im Besonderen bedeuten. Lass mich
das nun doch noch einmal am Schichtenmodell der Architektur erklären;
es ist so grundlegend, dass mir das hier angesichts des resultierenden
Strukturdiagramms ein Bedürfnis ist.
Hier eine Darstellung der Schichtenarchitektur²⁵⁶, die Ende der 1990er/-
Anfang der 2000er sehr populär war in der Microsoft-Welt:
²⁵⁶https://stackoverflow.com/questions/573201/whats-the-best-way-to-structure-a-
project


---


<!-- Page 565 of 584 -->


Musterlösung: 08-DieIODAArchitektur 556
DusiehstdarinzwarsogarPfeilefürDatenflüsse,aberdiesindnebensäch-
lich und betreffen nur die Umwelt. Wesentlich ist, was du nicht siehst:
die funktionalen Abhängigkeiten, die von oben nach unten verlaufen.
Jeder farbige Kasten ist vom darunter liegenden als funktional abhängig
gedacht.²⁵⁷ UI Components braucht UI Process Components, Business
Components braucht Data Access Logic Components usw.
Das klang für mich damals alles total logisch. Das war so sauber und klar.
Doch das war es nicht, jedenfalls nicht absolut. Es war nur relativ zu dem,
was vorher war, sauberer und klarer.
²⁵⁷Die grauen Kästen an der Seite mit den cross-cutting concerns lasse ich hier außen
vor. Von ihnen sind alle Schichten abhängig. Dass sie “horizontal gestapelt” sind, ist auch
unerheblichundwarnieimSinneeinerSchichtunggemeint.


---


<!-- Page 566 of 584 -->


Musterlösung: 08-DieIODAArchitektur 557
Zuerst habe ich die Ungereimtheit nicht bemerkt. Dann war es nur ein
dumpfes Unwohlsein. Erst nach Jahren habe ich mir erlaubt, diese Lehre
offeninFragezustellen.Dennwasjagänzlichunverständlichist-aberim
Grunde nicht in Zweifel gezogen wurde -, das ist die Abhängigkeit “des
Business” von der Datenhaltung überhaupt. Warum sollte die Geschäfts-
logik von der Datenzugriffslogik funktional abhängig sein? Warum sollte
das Business wissen, dass es eine Datenhaltung gibt und auch noch, wie
diese Datenhaltung zu benutzen ist?
EinKolbenimMotorweißnichtsvoneinemZylinderundnichtsvoneiner
Zündkerze usw. Alle Bauteile in einem Motor passen einfach zusammen.
Von außen betrachtet sind sie komplementär; sie ergänzen sich. Doch
das ist nicht Sache der Bauteile, sondern von etwas anderem. Das ist
Komposition.
Was ist also die Aufgabe von funktionalen Abhängigkeiten? Sie haben
zwei Aufgaben: Sie transportieren Daten und sie integrieren. Funktionale
Abhängigkeiten widersprechen fundamental dem SRP. In ihnen sind zwei
Entscheidungen repräsentiert - und das ist eine zuviel. Sie stehen für die
Entscheidung, was fließt, und für die Entscheidung wozwischen etwas
fließt.
Ob du nun dieses Schichtenmodell nimmst oder ein konzentrisches wie
die Hexagonal Architecture, es ist immer dasselbe. Und es wird damit
etwas suggeriert, was nicht wahr ist: dass oben bzw. außen einer höheren
Abstraktionsebene angehört, als unten bzw. innen.
Dieser Gedanke der geschichteten Abstraktionen stammt nach meinem
Empfinden vom OSI 7-Schichten Modell²⁵⁸:
²⁵⁸https://www.webopedia.com/quick_ref/OSI_Layers.asp


---


<!-- Page 567 of 584 -->


Musterlösung: 08-DieIODAArchitektur 558
Dort ist ein Layer i stets abstrakter als das Layer i-1. Schicht für Schicht
wird hier in Bezug auf die Kommunikation von der Hardware abstrahiert.
Eine abstraktere Schicht ist dabei abhängig von einer weniger abstrakten.
Das ist ganz natürlich. So sieht stratified design aus.
Das OSI 7-Schichten Modell hat wunderbare Dienste geleistet für die
Hard- und Softwareentwicklung. Doch es wäre ein großes Missverständ-
nis, das, was du dort siehst, auf die Schichten oder Schalen der Archi-
tekturmuster zu übertragen. Das passiert jedoch intuitiv. Schichten sind
Schichten, oder?
Nein, sind sie nicht. Das Missverständnis in Bezug auf das Schichtenmo-


---


<!-- Page 568 of 584 -->


Musterlösung: 08-DieIODAArchitektur 559
dell liegt in der Benutzung des Begriffs “Schicht”. Ich denke, man kann
sagen: Da ist etwas schief gelaufen.
Das OSI 7-Schichten Modell “funktioniert” nachweislich und hat großen
Wert. Also erlaube ich mir, daraus zu entnehmen, was der Zweck von
Abhängigkeiten ist: Sie verbinden Abstraktionsebenen miteinander. Ab-
hängigkeiten weisen von hoher zu niedriger Abstraktion, wenn es um die
Herstellung von Verhalten geht.
In jeder Schicht des OSI 7-Schichten Modells geschieht dasselbe: Es wird
kommuniziert. Nur geschieht das eben auf unterschiedlichen Abstrakti-
onsebenen.
Im Schichtenmodell der Architektur hingegen geschieht in den Schichten
nicht dasselbe! Die Businesslogik-Schicht hat eine ganz andere Aufgabe
als die Datenzugrifsslogikschicht usw. Und weil das so ist, ist es grund-
sätzlich falsch, diese Funktionsbereiche übereinander zu legen und zu
suggerieren, sie würden Abstraktionsebenen darstellen.
SchichtenimArchitekturmustertunganzUnterschiedliches;siesindkom-
plementär. Sie gehören derselben Abstraktionsebene an. Deshalb sollten
sie nicht übereinander, sondern nebeneinander dargestellt werden.²⁵⁹
Und da sie eben nicht dasselbe tun und zwischen ihnen keine Abstrakti-
onshierarchie besteht, sollten sie auch nicht voneinander abhängig sein.
Genau diese ist nun in der IODA Architektur endlich der Fall wie du oben
im Strukturdiagramm siehst. Filesystem{} und UI{} und Evoluti-
on{} sind komplementär. Sie gehören derselben Abstraktionsebene an.
Deshalb sind sie nicht voneinander abhängig.
Darüber jedoch sind die Integrationen, deren Zweck es ist, Abstraktions-
ebenen zu schaffen. Deshalb sind sie übereinander geschichtet wie im OSI
7-Schichten Modell und Abhängigkeiten verlaufen von oben nach unten.
Was übereinander liegt und abhängig ist, das abstrahiert. Was nebenein-
ander liegt und unabhängig ist, das operiert.
Wenn du zwei Funktionen oder Klassen oder Module im Allgemeinen
in deinem Code betrachtest, dann frage dich also stets, ob sie dasselbe
²⁵⁹DamitstehensieineinerLiniemitdencross-cuttingconcernsindengrauenKästen.Al-
lesindFunktionsbereiche,diekomplementärsind.AllegehörenzurEbenederOperationen
inIODA.


---


<!-- Page 569 of 584 -->


Musterlösung: 08-DieIODAArchitektur 560
tun,nurebenaufunterschiedlichenAbstraktionsniveaus,oderobsieeben
nicht dasselbe tun, sondern sich ergänzen. Ist Ersteres der Fall, dann ist
eine Abhängigkeit zwischen ihnen natürlich; ist Letzteres der Fall, sollte
es keine Abhängigkeit zwischen ihnen geben.
Das halte ich für einen sauberen, konsequenten, theoretisch fundierten
Umgang mit Abhängigkeiten.
Aufgabe 2 - Enturf nach IODA inkl.
Implementation
Bei der zweiten Aufgabe geht es wieder mal - langweilig, oder? - um eine
Konsolenanwendung. Langweilig, oder? Dafür ist es die letzte Aufgabe.
Und die Erklärung für diese langweilige Technologie ist immer noch
dieselbe: Ich benutze sie in den Übungsaufgaben, eben weil sie langweilig,
trivial und jedem zur Verfügung steht.²⁶⁰
Anforderungsanalyse
Also: Auf der Konsole soll ein Ratespiel gespielt werden. Es findet ein
kleiner Dialog statt. Es gibt zwei Interaktionen:
• Das Spiel wird gestartet, indem das Programm gestartet wird. Es
läuft dann bis die dabei bestimmte Zielzahl erraten ist.
• Der Benutzer versucht wiederholt die Zielzahl durch Angabe einer
Ratezahl zu erraten. Das Programm vergleicht die Ratezahlen mit
der Zielzahl und gibt Hinweise in Bezug auf das Verhältnis von
Zielzahl und Ratezahl.
²⁶⁰Ok, fast allen. Es gibt einige Programmiersprachen, die so sehr in Entwicklungsumge-
bungenundeineLaufzeitumgebungeingebundensind,dassdarinkeineKonsolenötigist,mit
denenestatsächlichschwierigbisunmöglichist,Konsolenanwendungenzuschreiben.SAP
ABAP-Entwickler rollen regelmäßig die Augen, wenn sie eine Aufgabe “auf der Konsole”
lösen sollen. Das tut mir leid; da heißt es dann kreativ sein. Denn bei den Aufgaben geht
es ja nicht um Konsole, sondern um einfache Benutzerschnittstellentechnologie. Wie etwas
anderesalsdieKonsoleeinfachist,dannkannmanhaltdieeinfachereTechnologiebenutzen.
Abernunistesjagleichgeschafft.


---


<!-- Page 570 of 584 -->


Musterlösung: 08-DieIODAArchitektur 561
Bei der Anforderungsanalyse kann ich schon auf meine Vorstellung von
der Architektur zurückgreifen. Ich weiß, dass die eigentliche Arbeit von
einem Processor geleistet wird. Der ist unabhängig von der konkreten
Benutzerschnittstelle.
Nachrichten an den Processor
Indemich“dieAugenzusammenkneife”undvonderBenutzerschnittstelle
abstrahiere, die eine Application als Interactor um den Processor herum
klammern wird, kann ich in der Anforderungsanalyse also schon überle-
gen, wie die Schnittstelle des Processors aussehen wird.
Den beiden Interaktionen entsprechen zwei Nachrichten, die der Proces-
sor zu verarbeiten hat:
• (Raterahmen) Starten(): Der Processor startet das Spiel und
liefert als Ergebnis den Wertebereich, in dem sich die Zielzahl
befindet; das ist der Raterahmen.
• (Rateergebnis) Beurteilen(int ratezahl): Der Proces-
sor vergleicht die Ratezahl mit der Zielzahl und teilt im Rateer-
gebnis mit, ob die Zahl erraten wurde oder wie ihr Verhältnis zur
Zielzahl ist.
Ich könnte jetzt noch klarer in den Anforderungen werden, indem ich
Akzeptanztests für den Processor definieren. Eigentlich ist das nötig und
muss auch möglich sein, wie ich ausführlich in Test-first Codierung
darstelle. Doch in diesem Band geht es fokussiert um den Entwurf;
deshalb überspringe ich diesen Schritt. Aber: Don’t try this at home! Oder
zumindest nicht in deinem Produktionscode.
Diese beiden Interaktionsfunktionen oder message handler sind wunder-
bare Ausgangspunkt für die Datenflüsse der Modellierung. Du erinnerst
dich an die “Kleiderbügelarchitektur”? Starten() und Beurteilen()
dienen als Aufhänger für die unabhängig von einander “im Schrank hän-
genden” Datenflüsse. Ich beginne durch die Art der Anforderungsanalyse
also gleich den Entwurf mit einem Vorsprung. Diese Art der Anforde-
rungsanalyse nenne ich Slicing; ich erläutere sie näher im gleichnamigen
Band meiner Reihe Programming with Ease.


---


<!-- Page 571 of 584 -->


Musterlösung: 08-DieIODAArchitektur 562
Lösungsansatz
DieAnforderungsanalyseistnunschonsehrkonkretgewordenmitFunkti-
onssignaturen.DennochwillicheinenMomentinnehaltenundüberlegen,
was einen Lösungsansatz darüber hinaus ausmachen könnte. Diemessage
handler beschreiben ja auch nur eine Oberfläche, die des Processors. Wie
sieht es aber grob darunter aus?
• Im Processor wird es irgendwo Zustand geben. Die Zielzahl ist zu
halten und auch die Ratezahlen müssen erinnert werden. Ich sehe
hier vor allem Domänendaten in der Domäne, die mit etwas Logik
angereichert sind.
• Die Zielzahl wird unter Verwendung eines Zufallszahlengenerators
bestimmt. Das ist eine Ressource, für die es einen Provider geben
muss.
Die Softwarezelle für das Programm ergibt sich daraus wie folgt:
Damit sind ohne nähere Modellierung schon einige Module klar:
• Portal für die Konsole-Benutzerschnittstelle
• Provider für den Zufallszahlengenerator
• Domänendatenstruktur für das Ratespiel
• Nachrichtendatentypen für Raterahmen und Rateergebnis
• Application
• Processor


---


<!-- Page 572 of 584 -->


Musterlösung: 08-DieIODAArchitektur 563
Modell
Das Modell entwickle ich gewöhnlich Interaktion für Interaktion. Da-
durch bekomme ich einen guten Fokus und gehe inkrementell vor. Jede
Interaktion hat ja Wert für den Nutzer. Wenn Interaktionen umfangreich
sind, kann ich auch innerhalb der Interaktionen nochmal Inkremente
definieren. Das scheint mir hier jedoch nicht nötig.
Spiel starten
Wenn das Spiel gestartet wird, ist zunächst der Raterahmen und die
Zielzahl zu bestimmen:
Pro Spiel nennt das Programm [dem Benutzer] einen Zah-
lenbereich n..m, in dem die zu ratende Zahl liegt. n wird
zufällig aus dem Bereich 1..50 gewählt, m wird zufällig aus
dem Bereich 10..100 gewählt. Es gilt je Spiel: n<=m-10.
Hier kommt der Provider zum Einsatz, der im Kern nur den Zufallszah-
lengenerator meiner Programmiersprache kapseln soll. Diesen Provider
für den API call möchte ich aber nicht mit der Logik aufladen, wie genau
die Zielzahl zu bestimmen ist. Die müsste auf einer höheren Ebene liegen:


---


<!-- Page 573 of 584 -->


Musterlösung: 08-DieIODAArchitektur 564
Der Zielenzahlengenerator{} enthält hier ein bisschen dark logik.
Dasfindeichabernichtschlimm.ImWesentlichenintegrierterdenrohen
API-Provider. Dass etwas mehr passiert ist daran zu erkennen, dass die
Integration dreier Funktionseinheiten desselben Moduls nicht zu einer
integrierenden Funktionseinheit im selben Modul führt.
Das Ratespiel{} wird über den Konstruktor gestartet - und anschlie-
ßend als Zustand im Processor gehalten.
DasStratumoberhalbvonstartenhabeichbewusstnichteingezeichnet.
Ich blende die Benutzerschnittstelle erstmal aus und konzentriere mich
darauf, was “hinter den Kulissen” passiert. Das ist nämlich gut testbar.
Rateversuch beurteilen
Die Beurteilung einer Ratezahl kann zu verschiedenen Ergebnissen füh-
ren:
• Die Zielzahl wurde gefunden.
• Oder: Die Zielzahl wurde nicht gefunden, dann ist zu bestimmen…


---


<!-- Page 574 of 584 -->


Musterlösung: 08-DieIODAArchitektur 565
– ob sich die Ratezahl näher zur Zielzahl bewegt hat…
– und ob sie schon einmal angegeben worden war.
Diese Überprüfung soll das Ratespiel{} durchführen. Im Lösungsan-
satz habe ich noch kühn gesagt, dass es sich dabei um Domänendaten mit
etwas Logik handelt. Doch bei genauerem Hinsehen sollte Domänenlogik
herausgezogen werden:
• Die Domänendaten bestehen nur aus der Zielzahl und der Liste
der Ratezahlen. Ihre Logik beschränkt sich darauf, eine Ratezahl
zu registrieren und dabei zu melden, ob es sich dabei um eine Wie-
derholung handelt. Außerdem können die Domänendaten befragt
werden, ob die Zielzahl gefunden wurde. Ist das der Fall, müssen
weitere Ratezahlen gar nicht registriert werden. Das ist die ganze
Domänendatenlogik.
• Ob sich allerdings die aktuelle Ratezahl näher an der Zielzahl
befindet als die vorherige, das zu bestimmen ist keine Sache einer
Datenstruktur. Sie muss lediglich den Zugriff auf ihre Daten geben,
um diese Frage mit Domänenlogik beantworten zu können.
Ichahne,dassichdieBifurkationimDatenflussmitetwasdarklogic über-
setzenwerde;aberdasmachtjanichts,weilesnureineFallunterscheidung
seinwird.DieModellierungmitStreamsmachtmirdanichts;sieerlauben
vielmehr größere Entscheidungsfreiheit.


---


<!-- Page 575 of 584 -->


Musterlösung: 08-DieIODAArchitektur 566
Mit einer Klasse für Domänenlogik zur Beurteilung der “Temperatur-
entwicklung” bin ich nicht ganz zufrieden. Sie scheint mir etwas zu
viel. Andererseits… Wenn ich die Funktionseinheit dem Processor{}
zuschlagenwürde,wäredessenFokusIntegrationverwässert;andererseits
gehörtdieseLogiknunwirklichnichtineineDatenstrukturhinein;siehat
nichts mit Zugriff oder Validation/Konsistenz zu tun.
Aber die Domänenlogik darf natürlich auf die Domänendaten, das Rate-
spiel{} zugreifen. Das wird allerdings nicht als Zustand gehalten wie
im Processor{}, sondern ließt nur hinein.
Application
Da die message handler des Processors vorhanden sind, steige ich ein
Stratum höher. Wie können sie vom Interactor integriert werden?
Wie eigentlich nicht anders zu erwarten, ist das sehr einfach. Ein handler
wird nur einmal durchlaufen, der andere immer wieder in einem Strom
von Ratezahlen.
Die Rateschleife und Ergebnis anzeigen gehören beide zum UI.
Sie können also leicht Zustand teilen. Das könnte hilfreich sein, um die
Rateschleife zu beenden bei Spielende. Das modelliere ich aber nicht spe-
ziell.IneinersynchronenImplementationistestrivial,dassdasProgramm
aufhört, wenn die Schleife in Rateschleife verlassen wird.
Ich denke, alle Funktionseinheiten und Module sind jetzt am Start.


---


<!-- Page 576 of 584 -->


Musterlösung: 08-DieIODAArchitektur 567
Implementation
Die Implementation des Modells gehe ich wieder inkrementell an. Ich
möchte schnell ein erstes Feedback haben. Außerdem sind es für mich
zweimentaleModi,amRahmenundimRahmenzuarbeiten.AmRahmen
bedeutet für mich, den Strukturrahmen bestehend aus den Modulen
aufzusetzen. Im Rahmen ist dann die Codierung von Funktionen, um
die Datenflüsse zu spannen. Am Rahmen zu arbeiten, finde ich relativ
langweilig, denn es entsteht ja kein Verhalten. Im Rahmen stelle ich Wert
her und da ist es dann auch wieder knifflig wegen der Logik.
Als Inkremente kann ich mir diese Schritte vorstellen:
1. Bei Programmstart wird ein Raterahmen mit n=1, m=10 aufge-
spannt und ohne Zielzahl gespielt. Ratezahlen entsprechen nie der
Zielzahl und es wird immer kälter; nur wenn als Ratezahl 42
eingegeben wird, wird Spielende gemeldet. Hier gibt es noch keine
Domänenlogik, aber schon einen Processor. Vor allem läuft aber die
Benutzerschnittstelle in einer Schleife. Module: Application{},
Processor{}, UI{}, Raterahmen{}, Rateergebnis{}.
2. Der Raterahmen bleibt und 7 wird als Zielzahl festgesetzt. Jetzt gibt
es eine Domäne. Die prüft für jede Ratezahl aber nur, ob sie der


---


<!-- Page 577 of 584 -->


Musterlösung: 08-DieIODAArchitektur 568
Zielzahl entspricht. Neue Module: Ratespiel{}, Zielzahlen-
generator{}.
3. Der Raterahmen und die Zielzahl werden zufällig bestimmt. Neues
Modul: Zufallszahlen{}.
4. Eine wiederholte Ratezahl wird erkannt.
5. Die Temperaturentwicklung wird bestimmt. Neues Modul: Ther-
mostat{}.
6. Bonus: Validation der Eingabe einer Ratezahl. Wenn sie außerhalb
des Rahmens liegt, wird erneut gefragt. Dieses Feature fällt mir
gerade ein; es ist nicht gefordert, aber wäre doch nett. Die Logik
dafür beschränkt sich auf die Rateschleife.
Wie immer ist das nur ein Plan, also eine Theorie. Bei der Codierung wird
sich zeigen, ob dieses Vorgehen eine gute Idee war.
Schlaglichter auf den Code
Ungefähr 75 Minuten später²⁶¹ kann ich sagen: Ja, das war eine gute
Idee. Die Inkremente haben gut aufeinenader aufgebaut. Das heißt nicht,
dass ich nicht zwischendurch noch etwas geradeziehen musste, doch im
Grunde hat alles so geklappt.
Wie schon bei der vorherigen Musterlösung will ich dich aber nun
nicht mit dem kompletten Code langweilen, sondern picke nur einige
Sehenswürdigkeiten heraus. Ein Blick zurück hat auch den Vorteil, dass
nun die ganze Struktur vor mir liegt.
²⁶¹Dazu kommen noch ca. 20 Minuten für den Entwurf. Die muss ich jedoch schätzen,
während mir die Implementationsdauer vom Git-Repository genannt wird. Insgesamt hat
die Aufgabe also ca. 2 Stunden von Anfang bis Fertigstellung inklusive Bonus gebraucht.
Das finde ich ok. Und ich denke, die Codierung hat sehr davon profitiert, dass ich dabei
entlangeinemModellvorgegangenbin.Sieverliefsehrgeradlinig.


---


<!-- Page 578 of 584 -->


Musterlösung: 08-DieIODAArchitektur 569
Die zeige ich dir auch, weil du daran siehst, dass die IODA-Ebenen sich
darinspiegelnkönnenundsollen.FürmichwirdderCodeinsgesamtüber-
sichtlicher, wenn ich nicht nur die Klassen des Entwurfs implementiere,
sondern auch die Kategorien des Architekturmodells manifestiere.
Lass mich nun anhand der IODA Architektur von oben nach unten
vorgehen, von den Abstraktionen zu den Details. Am Anfang deshalb die
Konstruktion. Schon hier zeigt sich durch den Fokus große Übersichtlich-
keit:


---


<!-- Page 579 of 584 -->


Musterlösung: 08-DieIODAArchitektur 570
1 static void Main(string[] args) {
2 var ui = new UI();
3 var zzg = new Zielzahlengenerator(new Random().Next);
4 var proc = new Processor(zzg);
5 var app = new Application(ui, proc);
6
7 app.Run();
8 }
Hier kannst du sehen, bei welchen Klassen ich mich für eine Instanziie-
rung entschieden habe. Nur der Thermostat{} ist ausgenommen als
Domänenlogik-Klasse. Processor{} wird wie die Provider instanziiert,
weil auch hier einer injiziert wird.
Hervorhebenswert ist auch die Konfiguration von Zielzahlengenera-
tor{}: Ich habe mich spontan gegen eine Provider-Klasse Zufallszah-
len{} entschieden, weil es nur um eine Funktion geht und die auch noch
von der Signatur her 1:1 von der C#-Plattform bereitgestellt wird. Statt
also über Klasse und Interface zu gehen zu müssen, um in einem Test den
ZufallszahlengeneratordurcheinSurrogatzuersetzen,reichtdieInjektion
einer Funktion. Im Produktionscode ist das hier die Standardfunktion von
C#: Next() auf der Klasse Random{}.
Die Integration im Interactor entspricht vollständig dem Modell. Ich habe
den Stream mit einer Continuation implementiert:
1 class Application
2 {
3 private readonly UI _ui;
4 private readonly Processor _proc;
5
6 public Application(UI ui, Processor proc) {
7 _ui = ui;
8 _proc = proc;
9 }
10
11 public void Run() {
12 var raterahmen = _proc.Starten();
13 _ui.Rateschleife(raterahmen,
14 r => {
15 var e = _proc.Beurteilen(r);
16 _ui.ErgebnisAnzeigen(e);
17 });
18 }
19 }
Der Processor bietet auch keine Überraschungen. Beide integrierenden
Methoden sehen aus wie im Entwurf. Hier kommt dann auch die statische
Klasse Thermostat{} zum Einsatz - die für Tests ja aber unkrisitsch
ist, falls ich auf dem Processor Akzeptanztests ansetzen wollte. Selbst die
Instanz von Zielzahlengenerator{} ist in dem Fall vernachlässigbar,


---


<!-- Page 580 of 584 -->


Musterlösung: 08-DieIODAArchitektur 571
weil sie wiederum ja konfiguriert wurde mit der eigentlich störenden API-
Abhängigkeit. Die könnte ich in einem Test nach Willen gestalten und
weiterhin einen Zielzahlengenerator{} injizieren.
1 class Processor
2 {
3 private readonly Zielzahlengenerator _zzg;
4 private Ratespiel _spiel;
5
6 public Processor(Zielzahlengenerator _zzg) {
7 this._zzg = _zzg;
8 }
9
10
11 public Raterahmen Starten() {
12 var (zielzahl, n, m) = _zzg.Generieren();
13 _spiel = new Ratespiel(zielzahl);
14 return new Raterahmen(n, m);
15 }
16
17
18 public Rateergebnis Beurteilen(int ratezahl) {
19 var wiederholung = _spiel.Registrieren(ratezahl);
20 var erfolg = _spiel.Geraten();
21 var temperaturveränderung = Thermostat.TemperaturentwicklungBeurteilen(_spiel);
22
23 return new Rateergebnis(
24 erfolg,
25 Map(temperaturveränderung),
26 wiederholung);
27
28
29 Rateergebnis.Temperaturveränderungen Map(Thermostat.Temperaturveränderungen tv)
30 => tv switch {
31 Thermostat.Temperaturveränderungen.Keine
32 => Rateergebnis.Temperaturveränderungen.Keine,
33 ...
34 };
35 }
36 }
Mich selbst überrascht hat am Ende die Notwendigkeit des Mapping. Im
Modell war mir noch nicht 100%ig klar, das die Beurteilung der Tempera-
turentwicklung ein Ergebnis liefert, das 1:1 in der Message-Datenstruktur
Rateergebnis{} auftaucht. Um an dieser Stelle kein “Domänenleck”
entstehen zu lassen, entkopple ich den Ergebnistyp vom Domänentyp mit
einem Map().
DadasMappingsoüberschaubarist,habeicheskurzerhandnuralslokale
MethodeinderProcessor-Methodeangelegt.Sollteeswachsen,würdeich
es dort herausziehen.
Weil ich bei der Zufallszahlengenerierung vom Modell abgewichen bin,
hier ein Blick auf die Nutzung der injizierten Funktion:


---


<!-- Page 581 of 584 -->


Musterlösung: 08-DieIODAArchitektur 572
1 class Zielzahlengenerator
2 {
3 private readonly Func<int, int, int> _zufallszahl;
4
5 public Zielzahlengenerator(Func<int,int,int> zufallszahl) {
6 _zufallszahl = zufallszahl;
7 }
8
9 public (int zielzahl, int n, int m) Generieren() {
10 var n = _zufallszahl(1, 50);
11 var m = _zufallszahl(n + 10, 100);
12 var z = _zufallszahl(n, m);
13 return (z, n, m);
14 }
15 }
Die angekündigte dark logic in Generieren() ist wirklich minimal. Sie
besteht lediglich aus dem n+10für die untere Grenze von m. Das finde ich
sehr verschmerzbar.
Insgesamt ist die Methode mit dem Aufruf der injizierten Funktion sehr
aufgeräumt. Durch die Benennung des Funktionszeigers ist das, was
dort passiert, quasi frei von Rauschen: Es werden drei Zahlen abhängig
voneinander zufällig generiert.
Die Logik des UI{} ist unspektakulär. Allerdings möchte ich dir einen
Blick darauf geben, wie ich mich nun entschieden habe, das Programm
abzubrechen:
1 class UI
2 {
3 private bool _running = true;
4
5 public void Rateschleife(Raterahmen raterahmen, Action<int> onRatezahl) {
6 ...
7 while (_running) {
8 ...
9 onRatezahl(ratezahl);
10 }
11 }
12
13
14 public void ErgebnisAnzeigen(Rateergebnis rateergebnis) {
15 if (rateergebnis.Erfolg) {
16 ...
17 _running = false;
18 return;
19 }
20 ...
21 }
22 }
Wennein Rateerfolg angezeigtwird, setzt dasUI{} die gemeinsameVaria-
ble_runningauf false.AufderenZustandprüftdieRateschleife()
- und wenn das Spiel nicht mehr läuft, bricht sie ab. Damit fällt die
Funktion zurück - Zeile 13 in Application{} oben - und das Programm
endet sauber.


---


<!-- Page 582 of 584 -->


Musterlösung: 08-DieIODAArchitektur 573
Und zum Schluss noch eine kleine Erweiterung, die ich dem Rate-
spiel{} als Domänendatenstruktur zugegeben habe:
1 class Ratespiel
2 {
3 private readonly int _zielzahl;
4 private readonly List<int> _ratezahlen = new();
5
6 public Ratespiel(int zielzahl) {
7 _zielzahl = zielzahl;
8 }
9
10 ...
11
12 public int Zielzahl => _zielzahl;
13 public IEnumerable<int> Ratezahlen => _ratezahlen;
14 }
Neben den beiden Methoden, die das Modell vorsieht, ist die Klasse
nun noch mit zwei Zugriffsmethoden ausgestattet. Darüber kann der
Thermostat{} auf die Daten zugreifen: Der muss Ratezahlen mit der
Zielzahl vergleichen. Zwar sind es genau genommen nur die beiden
letzten Ratezahlen, die ihn interessieren, doch ich reiche pauschal alle
registrierten heraus, um Ratespiel{} nutzender Domänenlogik mehr
Freiheit zu gewähren. Vielleicht kommen weitere Auswertungen hinzu;
dannmüssteichnichtsoschnelldieDatenstrukturanfassen.UnddieListe
der Ratezahlen insgesamt herauszugeben, scheint mir sehr naheliegend.
Reflexion
Dieser Entwurf mit Implementation auf der Basis von IODA hat mir mehr
Spaß gemacht als die Musterlösung von Kapitel 7. Durch das IODA Archi-
tekturmuster habe ich mich mehr geführt gefühlt. Bestimmte Logik hatte
sofort ihren Platz. Umgekehrt konnte ich durch die IODA-Brille schauen
und mich fragen, welche Logik ich noch brauchen könnte. Insbesondere
hat mir das bei der Modularisierung rund um die Zufallszahlen geholfen.
Dort konnte ich die Logik sofort einem Provider zuschlagen.
Auch das Modellieren entlang der Processor-Funktionseinheiten als Wur-
zeln von Datenflüssen, hat mir geholfen, mich zu konzentrieren. Ich
musste immer nur einen Datenfluss-“Kleiderbügel” im Blick behalten.
Eine saubere Anforderungsanalyse, die genau nach diesen Punkten der
Interaktion sucht, ist dafür natürlich die Voraussetzung. Wenn die aber
stattfindet, dann bietet die Processor-Integration eine schönen Ansatz-
punkt für den Entwurf und auch für eine test-first Codierung. Dort


---


<!-- Page 583 of 584 -->


Musterlösung: 08-DieIODAArchitektur 574
können Akzeptanztests ansetzen, die sich um keine Benutzerschnittstelle
kümmern müssen und eventuelle Provider-Abhängigkeiten durch Surro-
gate ersetzen können.
An einer Stelle habe ich mich bei der Codierung allerdings vertan: Wäh-
rend Inkrement 2 entsteht der Zielzahlengenerator{}. Den hatte ich
zunächst als statische Klasse angelegt. Das hat ausgereicht für Inkrement
2. Das passte dann aber nicht mehr für Inkrement 3. Der Zufallszahlen-
generator als Ressource kann nicht einfach genutzt werden; dann wäre
Zielzahlengenerator{} untestbar. Vielmehr muss der Zufallszahlen-
generator injiziert werden - und das erfordert, dass Zielzahlengene-
rator{} ebenfalls eine Instanzklasse ist. Daran hatte ich nicht gedacht.
Eigentlich hätte mir das laut Modell klar sein müssen; doch so kann es
eben gehen. Gräme dich also nicht, wenn dir das auch einmal passiert.
Was kann ich daraus lernen? Bei der Modularisierung könnte ich Klassen
sofort als statisch bzw. instanziierbar kennzeichnen. Da habe ich für diese
Entscheidung mehr Muße und Überblick. Während der Codierung muss
das dann nur noch “abschreiben”.
Wenn ich bei der Kennzeichnung der instanziierbaren Klassen von unten
nach oben vorgehe, dann kann ich bei jedem neuen Level überleben, ob
die Instanzierbarkeit darunter das Level darüber “ansteckt”.
• Daten wie Raterahmen{} sind zwar instanziierbar, aber nicht


---


<!-- Page 584 of 584 -->


Musterlösung: 08-DieIODAArchitektur 575
ansteckend.
• Dazu gehört auch Ratespiel{} als Domänendatenklasse.
• Doch Zufallszahlen{} als vom Namen her “halbe Datenklasse”
stecktZielzahlengenerator{}an-unddassetztsichdannfort
nach oben.
• Lediglich Thermostat{} als Domänenlogik-Klasse kann statisch
bleiben.
Wenn du das Klassendiagramm jetzt nach Ansicht des Codes nochmal
betrachtest, magst du dich fragen, wie es sein kann, dass eine operierende
Klasse wie Zielzahlengenerator{} abhängig sein kann. Entweder ist
sie integrierend und liegt höher in der Hierarchie oder sie operiert und
dann sollte sie nicht mehr abhängig sein. Oder?
Nicht ganz, denn letztlich sind nur Funktion(seinheit)en streng getrennt
in Integration und Operation. Klassen können hybrid sein. Klassen - oder
Module im Allgemeinen - haben nur einen vorherrschenden Charakter.
Der ist bei Zielzahlengenerator{} die Operation. Processor{}
hingegen hat den eindeutigen Zweck, zu integrieren. Deshalb darf es auch
innerhalb der Ebene O von IODA weitere Abhängigkeiten geben.
Außerdem tut Zielzahlengenerator{} dasselbe wie Zufallszah-
len{} - nur auf einer höheren Abstraktionsebene. Die Abhängigkeit
weist wie beim OSI 7-Schichten Modell korrekt von hoher zu niedriger
Abstraktion.