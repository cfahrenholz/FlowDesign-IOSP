<!-- Page 1 of 9 -->


PLANUNG Slicing
ANFORDERUNGSANALYSE FÜR ENTWICKLER, TEIL 6
Inkremente innerhalb von
Interaktionen f inden
Die Anforderungsanalyse muss grob beginnen. Wie aber gelangen Sie zu den kurzen Ite-
rationen, die für schnelle Rückmeldungen im Rahmen agilen Vorgehens unerlässlich sind?
Dieser Abschluss der Serie zur Anforderungsanaly-
se für Entwickler ([1] bis [5]) zeigt Ihnen, wie Sie
die Inkremente, in die Sie Anforderungen beim Slicing
schneiden, so fein machen können, dass Sie innerhalb
weniger Stunden Feedback zu Ihrer Umsetzung erhalten.
Bei der Zerlegung der Anforderungen mit Slicing geht
es zunächst um das „Ob oder ob nicht?“: Soll es ein Inkre-
ment überhaupt geben oder nicht? Und: Ist ein Inkrement
schon erkannt oder nicht?
Wo zum Beispiel zwei Kontexte in einem Softwaresystem
identifiziert wurden, kann die Frage gestellt werden, welcher
davon zuerst begonnen werden soll. Ob es noch einen drit-
ten Kontext gibt, ist vielleicht noch unklar. Wo dann vielleicht
zehn Dialoge innerhalb einer Perspektive identifiziert wur-
den, stellt sich die Frage, welche davon in welcher Reihen-
folge umgesetzt werden sollen. Sobald über diese zehn Dia-
loge hinweg zum Beispiel insgesamt 75 Interaktionen he-
rausgearbeitet worden sind, kann überlegt werden, welche
davon überhaupt und wann umgesetzt werden.
Und „ganz unten“ geht es darum, welche Funktionen auf
der CQS-Ebene implementiert werden sollen. Die sind natür-
lich niemals für ein komplettes Softwaresystem mit seinen Depth-first ist so aufwendig, dass diese Phase nicht voll-
Applikationen, Workern und Dialogen durch eine initiale ständig in der Breite durchlaufen werden kann; nur für eine
Analyse erkennbar. Sie ergeben sich vielmehr über die Zeit. gewisse Zeit ist eine Beschränkung auf breadth-first möglich.
Immer wieder gehen Sie zurück in die Anforderungsanalyse In der Breite bleiben daher über kurz oder lang Lücken. In-
und fragen: „Was noch? Was fehlt?“ Als Antwort schälen sich kremente werden nicht weiter verfolgt; darunter hängende
im Dialog mit dem Kunden weitere Entry Points heraus. Inkremente werden nicht einmal entdeckt.
Das meine ich mit „Ob oder ob nicht?“: Es kann eben nicht
Existenzielle Inkremente
alles in der Tiefe realisiert werden; auf einmal sowieso nicht.
In Bild 1 sehen Sie, wie eine Erkundung des Anforderungs- Es kann jedoch noch nicht einmal alles in der Tiefe erkannt
raums – oder konkreter: des Anforderungsbaums – sowohl in werden.
der Breite als auch in der Tiefe verläuft. Sie beginnt mit einer Die Natur der Softwareentwicklung ist also nicht nur inkre-
Breadth-first-Phase, die einen Überblick verschafft: Welche mentell: ein Inkrement nach dem anderen realisieren. Sie ist
größeren Brocken müssen eigentlich bewältigt werden? Wo auch notwendig iterativ: Die Analyse muss mehrfach durch-
liegen architektonische Herausforderungen? Dazu gehören laufen werden, um ein Softwaresystem immer näher an einen
die Ebenen System, Context, App und Worker. Zielzustand heranzubringen. (Natürlich ist dieser Zustand
Ab einem bestimmten Punkt jedoch ist es interessant, sich auch noch ein bewegliches Ziel, was die Notwendigkeit zur
zu konzentrieren und einen Ast in die Tiefe zu verfolgen bis Iteration verdoppelt.)
zur konkreten Funktion mit Signatur und Testfällen. Inner- Die bisherigen Inkremente könnte ich existenziell nennen.
halb von Workern geht es dabei depth-first vorwärts über Sie existieren entweder oder eben nicht. Der Entry Point
Perspektiven, Dialoge, Interaktionen, Entry Points und CQS- ep(x:string):number wird entweder realisiert oder nicht. Da-
Funktionen. für muss es die Interaktion i im Dialog d in der Perspektive p
32 9.2024 www.dotnetpro.de
003322--004400__SSlliicciinngg__eeaa__ffss__eeaa..iinndddd 3322 3300..0077..2244 1111::3300


---


<!-- Page 2 of 9 -->


PLANUNG Slicing
im Worker w in der App a im Kontext k im Softwaresystem Zerlegungshierarchie, das heißt eines ihrer Blätter, kann noch
geben. Falls irgendetwas davon nicht aufgesetzt ist, braucht höchst umfangreich sein.
es keine Funktion ep(). Es wäre deshalb wünschenswert, weiter zerlegen zu kön-
Oder genauer: Mindestens muss es die Hierarchiebenen nen. Sie wollen einem PO nicht sagen, „Gut, dass wir im En-
konzeptionell darüber geben, weil ihre Herausarbeitung zur try Point noch das Command update() und die Query load()
Erkenntnis geführt hat, dass ep() nötig ist. Sie müssen nicht gefunden haben. Du kannst in sechs Wochen mit der Umset-
unbedingt implementiert werden, um ep() zu realisieren und zung von update() rechnen.“ Das wäre gänzlich unagil. In-
gegen Akzeptanztests laufen zu lassen. Dasselbe gilt, wenn kremente dürfen nicht Wochen für die Realisierung brau-
ep() eventuell in die CQS-Funktionen update(x:string):void chen. Eine Rückmeldung vom PO muss in viel, viel kürzeren
und load():number zerlegt wurde. Zeitabständen eingeholt werden können.
Bis hierhin dreht sich Slicing um die Zerlegung in existen- Leider sehe ich jedoch keine simple weitere formale Zer-
zielle Inkremente. Und die ganze Zerlegung hat das Ziel, die legbarkeit von Inkrementen wie vom System bis zur CQS-
Entry-Point-Funktionen als Inkremente zu identifizieren, Funktion. Funktionen sind etwas anderes als Dialoge; die
Anforderungsanalyse mit Slicing in zwei
grundsätzlichen Phasen: zuerst in der Breite,
dann in der Tiefe (Bild 1)
weil diese für Sie konkrete Einstiegspunkte in die Umsetzung wiederum sind etwas anderes als Worker (Betriebssystem-
mit Entwurf und Codierung sind. Erreicht ist dieser Level erst, prozesse); diese unterscheiden sich schließlich von Kontexten
wenn Sie sich über die Existenz der Funktionen im Klaren als durch Kontrakte definierte Sprachgrenzen.
sind, Sie deren Signaturen klar herausgearbeitet haben und Unterhalb von (CQS-)Funktionen jedoch … Was soll da
der PO/Kunde sich klar über Testfälle ist. Vorher sollten Sie noch kommen? Es können nur weitere Funktionen sein. En-
nicht mit der Arbeit an Produktionscode beginnen. Das Risi- try Points sind Wurzeln von Funktionsbäumen, die zur Lauf-
ko für Änderungen, die seine Sauberkeit belasten, ist einfach zeit das Verhalten herstellen, das Benutzer von einer Interak-
zu groß. Unentschiedenes Hin und Her auf Produktionscode tion erwarten.
ist Gift für die Langlebigkeit einer Codebasis. Für mich ist jedoch weniger klar, welche Funktionen es in
diesem Funktionsbaum geben sollte. Eine weitere Zerle-
Qualitative Inkremente
gungshierarchie in Form einer Checkliste wie die der Slicing-
Auch wenn die Zahl solcher existenziellen Inkremente in ei- Ebenen bis hierher sehe ich nicht. Jetzt wird es schwieriger.
nem Softwaresystem sehr, sehr groß ist, bedeutet das nicht, Das Ziel ist nun nicht mehr so deutlich vor Augen wie mit En-
dass deshalb der Scope dieser Inkremente auf der untersten try Points und ihren Verfeinerungen, den Commands und
Ebene klein ist. Selbst wenn Sie schließlich innerhalb eines Queries.
Entry Points einer Interaktion innerhalb eines Dialogs inner- Deshalb würde ich nicht mehr von existenziellen Inkre-
halb eines Perspektive innerhalb eines Workers innerhalb menten sprechen, sondern von qualitativen Inkrementen.
einer App in einem Kontext eines Softwaresystems auf ein Durch eine weitere Verfeinerung der Anforderungen in-
Kommando gestoßen sind, stehen Sie nicht wegen all der har- nerhalb und unterhalb eines Entry Points geht es um dessen
ten Zerlegungsarbeit vor sehr feinen Anforderungen, die im qualitative Ausprägung. Ein Beispiel mag verdeutlichen, was
Nu umgesetzt sind. Nein, auch das Inkrement am Ende der ich meine. ▶
www.dotnetpro.de 9.2024 33
003322--004400__SSlliicciinngg__eeaa__ffss__eeaa..iinndddd 3333 3300..0077..2244 1111::3300


|  | Anforderungsanalyse mit Slicing in zwei
grundsätzlichen Phasen: zuerst in der Breite,
dann in der Tiefe (Bild 1) |
| --- | --- |



---


<!-- Page 3 of 9 -->


PLANUNG Slicing
Nehmen Sie eine Aufgabenverwaltung als zu realisieren- könnten vom PO Sie können Ihre Umsetzungs-
des Softwaresystem an. Das ist sehr übersichtlich und lässt überprüft werden, geschwindigkeit beeinflussen,
sich naheliegend wie folgt zerlegen: ohne dass der Auf- indem Sie die Anzahl sowie die
Das ganze System steht für die Aufgabenverwaltung. wand für Persistenz äußere und die innere Qualität
Darin gibt es eine Desktop-App. getrieben werden der Inkremente einstellen
Die App hat einen Dialog für die Erfassung der müsste. (Bild 2)
Details zu einer Aufgabe. Woran würde der
Vor allem hat sie aber einen Dialog für die Übersicht PO merken, dass
über alle Aufgaben mit folgenden Interaktionen: diese Qualität fehlt?
Hinzufügen einer neuen Aufgabe Wenn er die App
Bearbeiten einer Aufgabe schließt und wieder
Abhaken einer Aufgabe öffnet, sind vorher
Löschen einer Aufgabe erfasste Aufgaben
Wahl zwischen Anzeige unerledigter und verschwunden.
erledigter Aufgaben Wie könnten Sie die
Öffnen des Dialogs mit Anzeige aller Aufgaben Qualität der App ein wenig
Der Entry Point sieht dafür so aus: steigern und dem PO schon einen
loadAll():Task[]. Das ist eine Query; Eindruck von ihrer Arbeitsweise mit
Verfeinerung auf CQS-Ebene ist nicht nötig. Persistenz verschaffen? Sie könnten die in-
terne Liste mit den Aufgaben einfach pauschal beim
Für den letzten, explizit genannten Entry Point kann ein Test Schließen der App zum Beispiel im JSON-Format in einer
formuliert werden; Sie können mit der Umsetzung beginnen. Textdatei speichern und beim Start von dort wieder laden.
Dasselbe ist aber auch leicht für die Entry Points der anderen Woran würde der PO merken, dass immer noch Qualität
Interaktionen möglich, die ich hier der Einfachheit halber fehlt? Er könnte nicht in zwei Instanzen der Anwendung auf
ausgelassen habe. So weit dreht sich alles um existenzielle demselben Rechner oder auf verschiedenen Rechnern gleich-
Inkremente. zeitig an den Aufgaben arbeiten. Die letzte geschlossene In-
Wann könnten Sie nun dem PO eine Umsetzung für eine stanz würde mit ihren Daten „gewinnen“.
Rückmeldung vorlegen? Wovon hängt der Umsetzungsauf- Das meine ich mit qualitativen Inkrementen. Sie beschrei-
wand ab? Zunächst hängt Ihr Aufwand davon ab, wie viele ben verschiedene „Ausbaustufen“ des Verhaltens, das durch
der existenziellen Inkremente Sie bis zu einer Rückmeldung einen Entry Point repräsentiert wird.
umsetzen wollen/sollen. Ist der PO nur mit allen Entry Points
Die Dimensionen der Qualität
zufrieden? Oder kann er sich auf eine Untermenge einlassen,
gar nur einen Entry Point? Je weniger es sind, desto schnel- Genau genommen gibt es sogar zwei Qualitätsdimensionen
ler sind Sie, oder? (Bild 2): Die eine steht für fühlbare Qualität wie im Beispiel;
Die Menge der existenziellen Inkremente ist die eine Di- es geht um Softwareverhalten. Die andere steht für nicht
mension, in der Sie einen Regler bewegen können, um die fühlbare Qualität; PO oder Kunde oder Anwender können
Zeit bis zu einer Rückmeldung zu keine Aussage im Moment der Be-
verändern. nutzung darüber machen. Nur über
Eine zweite Dimension ist die eine längere Projektlaufzeit wür-
Qualität, in der die existenziellen den sie bemerken können, dass es
Inkremente umgesetzt werden. Da- an einer gewissen Qualität man-
mit meine ich zunächst die für den gelt, obwohl äußerlich alles läuft,
PO fühlbare Qualität. Wie ließe sich Die Qualität von wie es soll. Mit dieser anderen
die im Beispiel unterschiedlich ge- Inkrementen schritt- Qualität meine ich die innere, das
stalten? Zum Beispiel könnte eine weise erhöhen (Bild 3) heißt die, um die es auch beim
erste Umsetzung ohne Persistenz Clean Code Development geht. Sie
auskommen. Alle geforderten Entry ist gekennzeichnet durch Testbar-
Points wären vorhanden, die App keit und Wandelbarkeit.
könnte bedient werden – allerdings Auch die innere Qualität können
würden die Daten lediglich in-me- Sie bei Ihrer Umsetzung einstellen;
mory gehalten. Das könnte Ihren Sie können sich für mehr oder für
Implementationsaufwand drastisch weniger entscheiden. Ausdruck
senken. dafür sind zum Beispiel die Testab-
Die Qualität wäre geringer als deckung oder der Grad der Modu-
die gewünschte, doch es wäre ein larisierung oder ob Sie Prinzipien
Schritt in die richtige Richtung. Vie- sauberer Codierung eingehalten
le Aspekte des Softwaresystems haben.
34 9.2024 www.dotnetpro.de
003322--004400__SSlliicciinngg__eeaa__ffss__eeaa..iinndddd 3344 3300..0077..2244 1111::3300


---


<!-- Page 4 of 9 -->


PLANUNG Slicing
Sie können hohe äußere Qualität (zum Beispiel alle Entry dass Wert für Geld steht. Und damit stehen Inkremente für
Points laufen mehrbenutzerfähig persistent) und geringe in- Geld. Denn Inkremente sollen Wert liefern. Ein PO ist aufge-
nere Qualität (zum Beispiel sie weisen eine geringe Testab- rufen, die Wertsteigerung durch geschicktes Schneiden und
deckung auf) haben; Sie können aber auch niedrige äußere Priorisieren von Inkrementen zu optimieren.
Qualität (zum Beispiel alle Entry Points laufen nur mit In-Me- Bei den sprichwörtlichen Wasserfallprojekten entsteht
mory-Datenhaltung) und hohe innere Qualität (zum Beispiel Wert erst ganz am Schluss mit einem großen Sprung (oder
Sie haben hohe Testabdeckung und saubere Modularisie- vielleicht auch bei Erreichen gewisser Meilensteine). Bis da-
rung) kombinieren. hin vergeht viel Zeit, in der das Softwareprojekt nur Geld kos-
Ganz grob empfehle ich jedoch das Vorgehen wie in Bild 3 tet; währenddessen ist unsicher, ob und wie viel Wert wirk-
skizziert: lich dermaleinst entstehen wird.
Wählen Sie nur eine kleine Zahl existenzieller Inkremente, Dem stellt die Agilität eine Vorgehensweise entgegen, die
implementieren Sie diese zuerst mit einer geringeren äuße- viel häufiger Wert liefert. Wird nach Scrum gearbeitet, könn-
ren Qualität te das zum Beispiel alle vier oder alle zwei Wochen sein. Wer
und auch nur mit suboptimaler innerer Qualität (v1). nach Kanban arbeitet, liefert mit jedem Inkrement, das auf
Dann addieren Sie äußere Qualität in mehreren Schritten, „Done“ gestellt wird, Wert; das kann jeden Tag passieren.
bis alle (bekannten) Wünsche erfüllt sind (v2, v3). Hier ein Beispiel: Ein PO hat vier Inkremente identifiziert,
Zum Schluss ziehen Sie die innere Qualität „gerade“. Sie die ab Release jeden Monat einen bestimmten Mehrgewinn
refaktorisieren und runden Ihre Testsuite ab (v4). generieren. Jedes Inkrement braucht natürlich auch eine ge-
wisse Umsetzungszeit. In welcher Reihenfolge sollten die In-
Bei gegebener Zahl der existenziellen Inkremente – idealer- kremente angegangen werden, um eine möglichst große
weise konzentrieren Sie sich stets nur auf einen Entry Point Wertsteigerung zu erzielen? Bild 5 stellt zwei mögliche Priori-
zur gleichen Zeit –, sieht die Kurve der Qualitätsentwicklung sierungen gegenüber. Eine erzielt nach zwölf Monaten 14 400
sogar eher wie in Bild 4 aus: Sie starten mit suboptimaler in- Euro Mehrgewinn, die andere 15 500 Euro.
nerer Qualität, diese sinkt im Verlauf der Iterationen, durch
die Sie für das existenzielle Inkrement laufen, und erst am En-
de erhöhen Sie sie auf den eigentlich notwendigen Level.
Realistisches Clean Code Development erkennt an, dass
äußere und innere Qualität nicht gleichzeitig gesteigert wer-
den können. Ja, innere Qualität kann nicht einmal stets ge-
halten werden, während an der äußeren Qualität gearbeitet
wird. Deshalb braucht es immer wieder „Sprünge“ nach oben
für die innere Qualität, während derer sich die äußere nicht Realistischer
verändert; das sind Refaktorisierungen. Verlauf der Qua-
Bitte beachten Sie, dass auch die Steigerung der inneren litätsentwick-
Qualität ein Inkrement darstellt. Selbst wenn PO, Kunde und lung in Bezug auf
Anwender davon nichts (unmittelbar) bemerken, wird der ein existenzielles
Wert der Software dadurch gesteigert. Und um nichts ande- Inkrement (Bild 4)
res geht es bei der inkrementellen Entwicklung von Software:
die Steigerung ihres Wertes in kleinen Schritten.
Wert versus Erkenntnis
Wenn ich von Wert schreibe, denken Sie sicherlich an Wert
für den Kunden. Der drückt sich letztlich in Mehrgewinn aus:
Wenn Software ein bestimmtes Verhalten zeigt, das für Be-
nutzer nützlich ist, mehrt das den Gewinn des Unternehmens Während der Kunde für den Wert eines ganzen Soft-
auf die eine oder andere Weise mehr oder weniger unmittel- waresystems sicher eine Vorstellung hat, weil er es ja bewil-
bar. Nützliches Verhalten senkt die Kosten und/oder steigert ligen muss und also die Kosten gegen Alternativen abwägt,
den Umsatz. Aus anderen Gründen sind Unternehmen nicht sieht es für feinere Inkremente schon anders aus. Kontext
gewillt, Geld für Software auszugeben. oder Apps, also „dicke Scheiben“ des Slicings, mögen auch
Dass sie für diese Nützlichkeit Geld ausgeben müssen, ist noch einen bezifferbaren Wert haben, Dialoge oder Interak-
selbstverständlich. Diese Kosten werden mit dem Mehrge- tionen hingegen kaum.
winn verrechnet. Wenn Aussicht besteht, dass etwas übrig Dass ein PO wüsste, welchen Mehrgewinn die Umsetzung
bleibt, könnte sich das Softwareprojekt lohnen, wenn nicht dieses oder jenes Entry Points generieren würde, ist kaum
ein besserer ROI eines anderen Projekts oder geringere Op- anzunehmen. Geschweige denn, dass ein PO das für ein-
portunitätskosten woanders dem entgegenstehen. zelne Qualitätsaspekte innerhalb eines solchen Inkrements
Aber wir wollen uns nicht in Details der Wirtschaftlichkeits- sagen könnte. Dennoch wird ein PO irgendeinen Eindruck
betrachtung verlieren. Es geht mir nur darum, klarzumachen, davon haben, in welchem Verhältnis die Werte mehrerer ▶
www.dotnetpro.de 9.2024 35
003322--004400__SSlliicciinngg__eeaa__ffss__eeaa..iinndddd 3355 3300..0077..2244 1111::3300


---


<!-- Page 5 of 9 -->


PLANUNG Slicing
Inkremente stehen. Wenn ein genauer Geldbetrag nicht be- das schneller geradegezogen werden, als wenn er erst später
zifferbar ist, ist das nicht so schlimm. Auch ohne exakte Zahl höherqualitative Inkremente in die Hand bekommen hätte.
ist aber klar, dass Wert sich um Geld dreht. Damit möglichst schnell Wert hergestellt wird, ist möglichst
Wie passt nun dazu, dass ich oben Qualitätsinkremente schnell festzustellen, was überhaupt wertvoll ist. Das weiß ein
vorgeschlagen habe, die offensichtlich keinen Wert für den PO nicht immer a priori. In solchem Fall zu versuchen, ein
Kunden haben. Wenn Sie eine Aufgabenverwaltung zu- Wertinkrement herzustellen, das notwendig zu kurz springen
nächst mit geringer äußerer Qualität realisieren, indem Sie muss, ist Verschwendung. Besser ist es, bei der Qualität ab-
Die Priorisierung macht den Unterschied bei der Generierung von Wert. Blaue Balken: Am Anfang eines Monats geliefertert Wert; grü-
ne Balken: Wert, der pro Monat durch alle bisherigen Lieferungen entsteht; rote Kurve: kumulierter Wert. Unterschiedliche Priorisierun-
gen führen zu unterschiedlichem Anstieg der Wert-Kurve (Bild 5)
Daten nur in-memory halten, können Anwender damit nichts zuspecken und vor allem das zu liefern, was viel Licht ins An-
anfangen. Sie haben ein Inkrement geliefert und keinen Wert forderungsdunkel bringt, sprich Erkenntnis. Ist die Erkennt-
hergestellt? nis gewonnen, kann mehr Qualität in einer nächsten Itera tion
Ich bin der Meinung, das passt. Inkremente sollen mög- geliefert werden – bis schließlich sogar Wert entsteht.
lichst häufig möglichst viel Wert mit wenig Aufwand liefern – „Nur“ ein Erkenntnis-Inkrement zu liefern und noch kein
doch mit diesem Anspruch kann es lange dauern, bis Sie et- Wert-Inkrement, ist mithin ökonomisch. Ein Mangel wird
was zur Rückmeldung vorlegen. Deshalb unterscheide ich möglichst schnell ausgeglichen, teure Umwege werden ver-
zwischen Wert-Inkrementen und Erkenntnis-Inkrementen. mieden.
Wert-Inkremente können ausgeliefert werden und erzeu- Und woher weiß der PO, ob er noch nicht genau weiß, was
gen Mehrgewinn für den Kunden. für den Kunden welchen Wert darstellt? Er weiß es oft eben
Erkenntnis-Inkremente sind nicht auslieferungsfähig, son- nicht, höchstens ahnt er es. Auch Sie wissen es nicht. Deshalb
dern nützen vor allem dem internen Erkenntnisgewinn. Sie lautet meine Empfehlung, Inkremente so klein wie möglich
beziehungsweise der PO haben davon einen Vorteil. zu schneiden und Erkenntnis-Inkremente strategisch an den
Anfang zu stellen. Suchen Sie offensiv nach Wegen, zuerst
Ein Erkenntnis-Inkrement dient zur Orientierung: „Sind wir Erkenntnis zu gewinnen und nicht sofort dem Wert hinterher-
auf dem richtigen Weg zum Wert?“ zuhecheln. Der Wert wird sich einstellen, wenn die Erkennt-
Bei reduzierter äußerer Qualität bekommt ein PO aller- nis solide gewonnen ist.
dings immer noch etwas in die Hand, woran er feststellen
Maximal 16 Stunden bis zur Erkenntnis
kann, ob seine Idee von Anforderungen beziehungsweise Ihr
Verständnis und Ihre Umsetzung wirklich den Nutzen für den Der Zweck hinter Slicing ist nicht nur, auf kristallklar defi-
Kunden erhöhen würden. nierte Ausgangspunkte für Entwurf und Codierung inklusive
Beispiel Aufgabenverwaltung mit In-Memory-Datenhal- automatisierte Tests zu kommen: Entry Points. Er besteht
tung: Darin steckt kein Wert, dennoch erlaubt sie dem PO ei- auch darin, Anforderungen so fein zu schneiden, dass zügig
nen Umgang mit der App, der ihm Erkenntnis darüber ver- Feedback gewonnen werden kann.
schaffen kann, ob die Darstellung so ist, wie er sie sich Was ist zügig? Meine Definition ist sehr einfach: maximal
wünscht, und die Interaktionen so erreichbar und granular 16 Stunden Arbeitszeit.
sind, wie sie für bequeme Nutzung sein sollen. Er bekommt Vom Beginn der Umsetzung eines Inkrements bis zu einer
ein End-to-End-Benutzererlebnis – nur ohne Persistenz. Falls Lieferung zwecks Rückmeldung vom PO sollten nicht mehr
ihm dabei etwas auffällt, das verändert werden sollte, kann als 16 Arbeitsstunden vergehen. Wenn Sie heute um 9:00 Uhr
36 9.2024 www.dotnetpro.de
003322--004400__SSlliicciinngg__eeaa__ffss__eeaa..iinndddd 3366 3300..0077..2244 1111::3300


|  |  |  |
| --- | --- | --- |



---


<!-- Page 6 of 9 -->


PLANUNG Slicing
mit der Umsetzung beginnen, sollten Sie morgen um 17:00
Uhr damit fertig sein. Natürlich darf es auch schneller gehen, Spätestens alle 16 Arbeitsstunden
nur länger sollte es nicht dauern. ein Ergebnis liefern, um Rückmel-
Kürzer, schneller ist sehr schwierig. Schon 16 Arbeitsstun- dung zu bekommen, ob der einge-
den werden Ihnen für viele Inkremente unrealistisch erschei- schlagene Weg noch stimmt (Bild 7)
nen. Zu recht, wenn Sie nur an Wert-Inkremente denken.
Aber um die geht es ja nicht mehr ausschließlich. Erkenntnis-
gewinn sollte in 16 Arbeitsstunden möglich sein.
Und wenn nicht, sagt das auch etwas über den Stand der
Kenntnis bei PO und/oder bei Ihnen aus: Sie bewegen sich in
großer Unsicherheit. Umwege, also Verschwendung drohen;
Frustration, Unzuverlässigkeit, Qualitätsmängel, Konflikte
liegen vor Ihnen – es sei denn, Sie packen diese Unsicherheit
bei den Hörnern. Prototypen und Spikes mögen dann besse-
re Mittel sein als Inkremente, die Produktionscode verändern.
Länger als 16 Arbeitsstunden ist natürlich sehr einfach. Nur
droht dann erstens „Stochern im Nebel“ angesichts fehlen-
der Rückmeldung, zweitens steigt das Risiko von Multitas-
king. Man wird Sie kaum zehn Tage lang ungestört an einem
Wert-Inkrement werkeln lassen – dessen Wert am Ende trotz
aller Mühe ungewiss ist. Vielmehr wird man Ihnen immer
wieder andere Aufgaben/Inkremente dazwischenschieben; morgen andere Aufgaben abzulehnen. Über ein oder zwei
ja, auch und gerade bei agilem Vorgehen. Auf diese Weise Tage ist es möglich, sich echt zu konzentrieren, um verläss-
dehnt sich das 10-Tage-Inkrement schnell auf 12, 15, 20 Tage lich zu liefern. Ist das geschafft, kann erst mal wieder etwas
aus. Die Rückmeldungen entschwinden in unbekannte Zu- anderes dran sein. Aber zweimal acht Arbeitsstunden können
kunft. Das macht dann auch irgendwann keinen Spaß mehr. Sie unter Kontrolle haben, wenn Sie es ernst meinen mit der
Verlässlichkeit. Mehr scheint mir in einem normalen Projekt-
betrieb sehr unwahrscheinlich.
Wie gesagt, damit meine ich keine Wert-Inkremente, son-
dern vor allem Erkenntnis-Inkremente. Verabreden Sie die
explizit mit Ihrem PO. Suchen Sie im Rahmen eines Entry
Points nach weiteren Inkrementen, die einen schrittweisen
Aufbau seines Gesamtverhaltens und damit Gesamtnutzens
und Wertes erlauben.
In Bild 6 sehen Sie, wie ich mir die Entwicklung eines Wert-
Inkrements vorstelle: Es ist der Schlussstein eines Weges, der
bis dahin mit Erkenntnis-Inkrementen gepflastert ist. Um die-
sen Wert jedoch langfristig zu erhalten, müssen sie darauf
achten, die innere Qualität anschließend ebenfalls wieder auf
einen hohen Wert zu bringen.
Denn gelieferter Wert heute im Sinne von Nützlichkeit in-
teressiert den Kunden eigentlich nur, wenn dadurch zukünf-
tige weitere Nützlichkeitssteigerungen nicht kompromittiert
werden. Nützlichkeit braucht Nachhaltigkeit. (Wenn Kunden
scheinbar so nicht denken, ist das vor allem ihrem Unver-
ständnis anzurechnen, was die Möglichkeiten des Raubbaus
Arbeiten Sie sich schrittweise an Wert heran – und denken an der Ressource Code angeht. Wüssten sie darum, würden
Sie zum Abschluss an die Nachhaltigkeit (Bild 6) sie offensiver hohe innere Qualität fordern.)
Die x-Achse in Bild 6 können Sie übrigens auch zeitlich ver-
stehen: Mit fortschreitender Zeit erhöhen Sie zunächst die äu-
Nein, Sie wollen so schnell wie möglich Klarheit. Eine ßere Qualität – und addieren am Ende nochmal Aufwand für
Rückmeldung – selbst wenn Sie negativ sein sollte – ist auch die innere. In Bild 7 sind die Entwicklungen von innerer und
wichtig für Ihren „sense of purpose“: Wenn Sie merken, dass äußerer Qualität je Inkrement parallel notiert.
da jemand ist, der sich für Ihr Ergebnisse interessiert, sind Sie
Single Responsibilities für schnelle Erkenntnis
mit mehr Engagement bei der Sache.
Ich glaube, dass eine Lieferung „spätestens morgen“ ho- Was erzeugt Wert? Die Summe der in Code umgesetzten Ent-
hen Fokus fördert. Zur Not schaffen Sie es nämlich sogar, bis scheidungen des Kunden. ▶
www.dotnetpro.de 9.2024 37
003322--004400__SSlliicciinngg__eeaa__ffss__eeaa..iinndddd 3377 3300..0077..2244 1111::3300


---


<!-- Page 7 of 9 -->


PLANUNG Slicing
Der Kunde hat sich entschieden, die Realisierung einer Und das Single Responsibility Principle (SRP) trägt Ihnen
Aufgabenverwaltung zu beauftragen. Das ist ihm zum Bei- dazu auf, den Code, der die Verantwortung für die Umset-
spiel 5000 Euro wert; er erhofft sich dadurch einen Mehrge- zung einer Entscheidung trägt, mit einem Bezeichner zu ver-
winn von 250 Euro pro Monat. Die Lieferung des Codes für sehen [6].
die Aufgabenverwaltung startet die Produktion des Mehrge- Entscheidungen ziehen Verantwortlichkeiten im Code
winns. nach sich. Welche Codeabschnitte für welche Entscheidun-
Auf dieser Abstraktionsebene steht einer Entscheidung ein gen verantwortlich sind, ist glasklar zu machen. Nur so kann
Inkrement gegenüber. Code gezielt angepasst werden, wenn sich die Entscheidun-
Diese eine große Entscheidung besteht jedoch aus ande- gen ändern; nur so kann Code verlässlich getestet werden, ob
ren, dieser Entscheidung müssen weitere folgen. Wenn eine er überhaupt seiner Verantwortlichkeit gerecht wird.
Aufgabenverwaltung entwickelt werden soll, stellen sich Das SRP ist also analyseleitend und gleichzeitig auch ent-
zum Beispiel diese Fragen: wurfsinspirierend. Größere Entscheidungen werden durch
Soll es eine Desktop-, Web- oder Mobile-App sein? Oder gröbere Strukturelemente repräsentiert (zum Beispiel Pro-
sollen womöglich mehrere Endgeräte bedient werden? zess, Bibliothek, Klasse). Kleinere Entscheidungen, Detail-
Soll sie mehrbenutzerfähig sein? entscheidungen werden durch Funktionen repräsentiert.
Soll sie für 5, 25, 100, 1000 oder mehr Benutzer ausgelegt Noch feinere durch einzelne Ausdrücke.
sein? Wenn Sie auf der Suche nach Inkrementen sind, folgen Sie
Sollen andere Softwaresysteme integriert werden schon intuitiv einem Entscheidungsbaum in die Tiefe. Jeder
(zum Beispiel Google Kalender)? Kontext, jede App, jeder Worker, jeder Dialog und jede Inter-
Für welches Datenaufkommen pro Benutzer soll das Soft- aktion stehen für eine Entscheidung. Dass zum Beispiel Auf-
waresystem ausgelegt sein? gaben gelöscht werden können sollen, ist eine Entscheidung,
Soll es eine Authentifizierung für Benutzer geben? für die es eine Interaktion mit einem Entry Point gibt.
Soll es eine Autorisierung mit unterschiedlichen Rechten Doch da endet der Entscheidungsbaum gewöhnlich nicht.
für Benutzer geben? Er setzt sich in die Tiefe fort. Weitere Entscheidungen machen
Soll es Benutzerrollen geben? in Summe die aus, für die eine Interaktion steht.
Welche Funktionalität soll das Softwaresystem haben? Aufgaben sollen gelöscht werden können? Wie steht es
Sollen Aufgaben in Listen zusammengefasst werden dann zum Beispiel mit den folgenden Fragen:
können? Wie soll unbeabsichtigtes Löschen verhindert oder im Ef-
Sollen Aufgaben (listenübergreifend) getaggt werden fekt gemildert werden? Soll vor dem endgültigen Löschen
können? eine Bestätigung eingeholt werden? Oder soll die Aufgabe
Sollen Tags zentral umbenannt werden können? nur als gelöscht gekennzeichnet werden, um sie gegebe-
Soll eine Erinnerung an Aufgaben erfolgen? Wenn ja, nenfalls über eine Rückgängig-Interaktion wieder herzu-
wie? stellen?
Soll der Fortschritt bei der Erledigung von Aufgaben Soll eine Aufgabe gelöscht werden können, wenn andere
festgehalten werden können? von ihr abhängig sind?
Sollen Aufgaben aufeinander Bezug nehmen können, Wenn eine gelöschte Aufgabe die letzte mit einem Hashtag
sodass Abhängigkeitsbeziehungen entstehen ist, soll dann das Tag aus der Liste aller Hashtags ver-
(Vorgänger, Nachfolger …)? schwinden oder dennoch darinbleiben?
und so weiter und so fort. Soll das Löschen durch einen Soundeffekt begleitet wer-
den?
Sie sehen, es gibt viele, viele, viele Entscheidungen zu tref- Soll das Löschen durch eine Animation begleitet werden?
fen. Kunden müssen sich darüber klar werden, was sie wol- Braucht ein Benutzer für das Löschen ein bestimmtes Recht?
len. POs sollen ihnen helfen, diese Klarheit zu erlangen. Klar- Kann er eigene Aufgaben immer löschen und nur
heit besteht darin, Entscheidungen erstens zu benennen und fremde mit einem bestimmten Recht?
zweitens explizit zu entscheiden.
Entscheidungen, die nicht herausgearbeitet sind und nicht Diese und weitere Entscheidungen sind herauszuarbeiten
explizit entschieden sind, werden ansonsten von Ihnen als und nach dem SRP klar mit einem Bezeichner identifiziert zu
Entwickler mehr oder weniger bewusst entschieden. Sie ma- implementieren. Softwareentwicklung, ja, schon Anforde-
chen Annahmen – deren Umsetzung am Ende dem Kunden rungsanalyse ist wahrlich kein leichtes Unterfangen.
vorgelegt wird. Ob der mit Ihren Annahmen übereinstimmt, Doch diese Sichtweise auf die Analyse hat auch einen Vor-
ist fraglich. Änderungsaufwand droht. teil: Jede Entscheidung ist potenziell eine, die auch erst mal
Ihre vornehmste Aufgabe während der Anforderungsana- vernachlässigt werden kann. Es kann für den Zweck des Er-
lyse besteht mithin darin, alle Entscheidungen des Kunden kenntnisgewinns nur die einfachstmögliche Entscheidung
herauszuarbeiten, explizit zu machen und die vom Kunden getroffen werden. Sie fällt immer so aus, dass Sie weniger
getroffenen Entscheidungen festzuhalten. Ihre Verantwort- Umsetzungsaufwand haben. Flüssige agile, also im Kern in-
lichkeit ist es anschließend, Code zu schreiben, der diese Ent- krementell-iterative Arbeit basiert auf der Kunst des Loslas-
scheidungen umsetzt. sens. Loslassen von „lieb gewonnenen“ Ideen, was eine Soft-
38 9.2024 www.dotnetpro.de
003322--004400__SSlliicciinngg__eeaa__ffss__eeaa..iinndddd 3388 3300..0077..2244 1111::3300


---


<!-- Page 8 of 9 -->


PLANUNG Slicing
ware alle können soll. Nicht für immer, aber doch für einen Feature Y sollte nun endlich umgesetzt werden …“ sind Aus-
gewissen Zeitraum. sagen, die Sie sicher auch schon getätigt haben. Doch was ist
Ein paar Beispiele fürs Loslassen: mit „Feature“ gemeint? In meiner Wahrnehmung geht es al-
Unbeabsichtigtes Löschen verhindern? Nein. lermeistens um eine funktionale Anforderung. Und ich wür-
Darauf achten, ob es Abhängigkeiten gibt? Nein. de sogar sagen: Eine funktionale Anforderungen im Rahmen
Hashtags anpassen? Nein. einer Interaktion.
Soundeffekt? Nein. Deshalb möchte ich den Begriff wie folgt formalisieren: Ein
Animation? Nein. Feature ist ein Inkrement innerhalb des Inkrements, für das
Rechte für das Löschen? Nein. ein Entry Point (beziehungsweise eine seiner CQS-Funktio-
nen) steht. Realisierte Features sind umgesetzte Entschei-
Wer bei der Benutzung die Interaktion „Aufgabe löschen“ dungen im Rahmen des Scopes. Der Scope sind die Anforde-
triggert, der löscht einfach die Aufgabe. Fertig. Und wenn die rungen an einen Entry Point.
Datenhaltung nur in-memory ist, verringert sich der Umset- In der Umsetzung bekommt jedes Feature einen Bezeich-
zungsaufwand dafür noch weiter. (Das ist der Fall, wenn die ner, am besten durch Kapselung in einer Funktion. Bei grö-
Entscheidung für Persistenz zunächst und temporär verneint ßeren Features kann dafür aber auch eine Klasse oder ein
wird.) Auf diese Weise kann der PO in kürzester Zeit Rück- noch höheres Modul stehen. Features sind also implementier-
meldung geben, ob ihm der allgemeine Fluss der Bedienung te Verantwortlichkeiten des SRP.
passt. Nochmal als Beispiel die Aufgabenverwaltung: Dass eine
Der PO kann sogar bestimmen: All die anderen Entschei- Aufgabe gelöscht werden kann, würde ich nicht als Feature
dungen, die zunächst negativ/minimal getroffen wurden, bezeichnen. Das ist eine Anforderung, die durch eine Inter-
bleiben so. Anderes ist wichtiger, als nach einem ersten Er- aktion in einem Dialog beantwortet wird.
kenntnis-Inkrement noch eine Löschbestätigung zu imple- Innerhalb der Interaktion „Aufgabe löschen“ jedoch gibt
mentieren oder auf die Tags aufzupassen und so fort. Er kann es Features, zum Beispiel:
bestimmen, dass das, was nur ein Erkenntnis-Inkrement hat- Bestätigungsabfrage
te sein sollen, doch ein Wert-Inkrement ist. Nicht 100 Prozent Verweigerung des Löschens, wenn es noch abhängige Auf-
des ursprünglichen Wertes wurde erreicht, aber zum Beispiel gaben gibt
80 Prozent. Das ist gut genug für eine Auslieferung, die schon Löschen eines Tags, das die Aufgabe als einzige enthält
Nutzen stiftet. (Wenn zumindest die Entscheidung für Persis- Soundeffekt abspielen
tenz nun bejaht und der In-Memory-Provider
durch einen persistenten ausgetauscht wird.)
„Gut genug“ denken zu können ist auch ein Er-
gebnis von Loslassen.
Das SRP kommt als Prinzip für die Strukturie-
rung daher. Es ist eines der fünf Clean-Code-
SOLID-Prinzipien. Doch woher kommen die Ver-
antwortlichkeiten, die nach dem SRP sauber „ver-
packt“ werden sollen? Es sind Aspekte der Anfor-
derungen. Deshalb beginnt der Einsatz des SRP
schon während der Anforderungsanalyse. Es lei-
tet Ihre Fragen. Es fordert Sie auf, tiefer und tie-
fer zu bohren und noch genauer hinzuschauen, ob
nicht noch eine Entscheidung unentdeckt und/
oder nicht explizit entschieden ist. Sobald Sie be-
merken, eine Annahme zu treffen, halten Sie in-
ne! Nehmen Sie nicht an, sondern legen Sie die
Entscheidung dem PO vor. Alle Features sind gekapselt in Funktionen (Bild 8)
Damit meine ich natürlich Entscheidungen
rund um die Ausprägung von Verhalten der Soft-
ware. Technische Detailentscheidungen – „Sollte hier LINQ Bild 8 zeigt mit einer Code-Skizze, wie Features in Funktionen
benutzt werden?“ oder „Benutzen wir class, struct oder re- gekapselt sein könnten. Präfixe für Funktionsnamen deuten
cord?“ – sind nicht für den PO relevant. Auf sie bezieht sich eine Modularisierung an. Auf diese Weise könnten sogar
das SRP zwar auch, doch die Entscheidung müssen Sie bezie- schon alle Features repräsentiert sein – ohne sie implemen-
hungsweise Ihr Entwicklerteam treffen. tieren zu müssen. Außer der Funktion provider.DeleteTask()
könnten alle nur minimale Rümpfe sein. Auf diese Weise wür-
Die Features einer Software
den Sie Anforderungen im Code dokumentieren, ohne schon
Der Begriff „Feature“ ist Ihnen für Anforderungen geläufig. Implementationsaufwand treiben zu müssen. (Aber natürlich
„Das Feature X der Anwendung ist gut gelungen“ oder „Das gilt auch hier: Vorsicht vor Premature Optimization!) ▶
www.dotnetpro.de 9.2024 39
003322--004400__SSlliicciinngg__eeaa__ffss__eeaa..iinndddd 3399 3300..0077..2244 1111::3300


---


<!-- Page 9 of 9 -->


PLANUNG Slicing
Skizze der
Mengenverhältnisse
zwischen den Ebenen der
Slicing-Hierarchie (Bild 9)
Fazit
sondern auch kleine, schwer erkennbare Entscheidungen
Meine klare Empfehlung zur Abrundung Ihrer Anforde- aufdecken. So viel wird impliziert, vorausgesetzt …)
rungsanalyse mit Slicing: Entwickeln Sie einen Spürsinn für
Features. Seien Sie nicht mit Entry Points als Endpunkten der Also: Augen und Ohren auf bei der Anforderungsanalyse!
Anforderungszerlegung zufrieden. Schauen Sie unter die Lassen Sie sich nicht mit User Stories und Use Cases „abspei-
Haube der Entry Points beziehungsweise CQS-Funktionen. sen“. Fordern Sie viel konkretere Entscheidungen des PO,
Dort finden Sie immer zahlreiche Features, die Sie mehr oder die Ihnen zunächst präzise spezifizierte Entry Points und
weniger unabhängig voneinander implementieren können. dann einen Fächer an Features je Entry Point liefern, mit dem
Das SRP leitet Sie bei der Codierung, indem es Ihnen nahe- Sie das inkrementelle Vorgehen für schnelle Rückmeldungen
legt, jedes Feature mit einem Bezeichner zu identifizieren – fein justieren können. Das ist pragmatische Agilität. ◾
am besten ist das mindestens eine Funktion.
Und gegenüber dem PO können Sie den Aufwand bis zur [1] Ralf Westphal, Strukturiert zerlegen, dotnetpro 4/2024,
Lieferung des nächsten Inkrements mittels Features fein steu- Seite 42 ff., www.dotnetpro.de/A2404Slicing
ern. Peilen Sie als Iterationsdauer maximal 16 Stunden an. In [2] Ralf Westphal, Den Stier bei den Hörnern packen,
dieser Zeit konzentrieren Sie sich auf Inkremente gebündelt dotnetpro 5/2024, Seite 26 ff.,
aus einem oder mehreren Features einer Interaktion. www.dotnetpro.de/A2405Slicing
Lassen Sie sich nicht wild machen durch Bettelei des PO [3] Ralf Westphal, Das Messer richtig ansetzen, dotnetpro
nach Wert. Konzentrieren Sie sich auf den Mangel, den Sie 6/2024, Seite 34 ff., www.dotnetpro.de/A2406Slicing
spüren. Wenn für Wert noch zu wenige Informationen vorlie- [4] Ralf Westphal, Die Benutzerschnittstelle treibt das
gen, liefern Sie Inkremente für den Erkenntnisgewinn. Wert Slicing, dotnetpro 7/2024, Seite 44 ff.,
wird sich zur rechten Zeit schon einstellen. Keine Sorge. www.dotnetpro.de/A2407Slicing
Features machen den Zerlegungsbaum des Slicing natür- [5] Ralf Westphal, Grobe Schnitte durch die Anforderungen,
lich sehr „blattlastig“. Ich versuche in Bild 9 einmal eine ganz dotnetpro 8/2024, Seite 30 ff.,
überschlägige Rechnung: www.dotnetpro.de/A2408Slicing
Überschaubar ist noch die Menge der Worker innerhalb [6] Ralf Westphal, The Single Responsibility Principle,
eines Softwaresystems. Bis dahin mag eine Breadth-first- www.dotnetpro.de/SL2409Slicing1
Zerlegung möglich sein.
Anschließend wird es schon sehr detailliert, und der Fokus
sollte auf eine App in einem Kontext gehen. Ralf Westphal
Innerhalb einer App lohnt sich wiederum die Priorisierung ist Trainer, Berater und Mitgründer der Clean
einer Perspektive mit wenigen Dialogen und ihren Interak- Code Developer Initiative (https://clean-code-
tionen. developer.de). Seine Schwerpunkte sind dauer-
Denn auf der untersten Ebene ist die Zahl der Features min- haft hohe Produktivität für die Softwareent-
destens zwei Zehnerpotenzen größer als die Zahl der Dia- wicklung und zukunftsfähige Teamorganisation.
loge. (Wahrscheinlich ist diese Abschätzung sogar noch un- https://ralfw.de
tertrieben: Die Zahl der Features „geht durch die Decke“,
dnpCode A2409Slicing
wenn Sie wirklich genau hinhören und nicht nur größere,
40 9.2024 www.dotnetpro.de
003322--004400__SSlliicciinngg__eeaa__ffss__eeaa..iinndddd 4400 3300..0077..2244 1111::3300