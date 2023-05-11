# Vorbereitung Testat 4

------

### Lernziele:

- Praktisches Verständnis der Fourierreihe und der Fourieranalyse
- Methoden der Frequenzmessung, insbesondere Windowing
- Mustererkennung mit Prototypen-Klassifikatoren

### **Vorbereitung:**

* Arbeiten Sie Kap. 11-14 der Vorlesung durch und lesen Sie ggf. die noch zu klärenden Fragen in der in den Vorlesungsunterlagen angegebenen Literatur nach.
* Gehen Sie die unten bereitgestellten Testatfragen durch und beantworten Sie sie. Falls Sie die Antwort nicht wissen, lesen Sie sie in den Unterlagen nach. Getestet werden alle Bestandteile der Vorbereitung, d.h. Kap. 11-14 aus der Vorlesung.
* Lesen Sie die Versuchsanleitung durch. Schauen Sie ggf. in den Unterlagen nach, falls etwas inhaltlich nicht klar sein sollte.

```
Fragenkatalog zu Testat 4
==========================


1. Wie wirkt die Differentiation auf das Spektrum eines Signals?
* Die Frequenz bleibt gleich, nur ihr Betrag ändert sich um w und die Phase verschiebt sich um -pi/2.

2. Wie funktioniert die Faltung, um das Ausgangssignal eines Systems zur Zeit t zu 
berechnen?
* Das Eingangssignal wird mit der Impulsantwort multipliziert.
Interpretieren lässt sich diese folgendermaßen:
Die Impulsantwort h(t) wird um t nach links verschoben und an der y-Achse gespiegelt.
Dann wird sie punktweise mit dem Signal f(T) multipliziert und das Integral ergibt nun den Ausgangswert y(t).

3. Wie sieht der Amplitudengang eines Differenzierers aus?
* Der Amplitudengang ist eine Gerade mit der Steigung 1.

4. Wie wirkt ein lineares System auf das Spektrum eines Signals?
* Ein lineares System verändert die Frequenzen des Signals nicht.

5. Was ist ein Bode-Diagramm?
* Ein Bode-Diagramm zeigt zwei Funktionsgraphen:
Ein Graph zeigt den Betrag (Amplitudenverstärkung), der andere zeigt das Argument (Phasenverschiebung) einer komplexwertigen Funktion in Abhängigkeit der Frequenz.

6. Wie verändert der Phasengang eines linearen Systems die Phase des Eingangssignals?
* Der Phasengang verschiebt das Eingangssignal. Meistens ist der Phasengang negativ, d.h. der Ausgang folgt verzögert dem Eingang.

7. Wievielen Dezibel entspricht ein Verstärkungsfaktor von 100?
* 40 dB.

8. Was ist Filterung?
* Die Veränderung oder Ausschaltung einzelner Frequenzkomponenten eines Signals.

9. Welche Eigenschaften haben ideale frequenzselektive Filter im Zeitbereich?
* Ideale Filter sind extrem scharf im Frequenzbereich lokalisiert. Nach der Unschärferelation führt dies zu einer weiträumigen ”Verschmierung” im Zeitbereich. (kap. 14.17)
* Nichtkausal
* Unendlich große Impulsantwort (Sinc-Funktion)
* Überschwingen
* Oszillierendes Einschwingen (kap. 14.18)

10. Wie muss man den Frequenzgang eines Filters im Spektralraum verändern, damit sich die Impulsantwort in der Zeitdomäne verschiebt?
* Man multipliziert den Frequenzgang mit einem Phasenfaktor e^(-iwa)

11. Was ist das Faltungsintegral?
* Das Faltungsintegral gibt an, wie für ein beliebiges Eingangssignal das zugehörige Ausgangssignal mit Hilfe der Impulsantwort berechnet werden kann.

12. Wie kann man ein Vokal in einem Sprachsignal erkennen?
* Vokale sind fastperiodische Signalabschnitte. Sie werden durch eine lokale Form der Fourieranalyse erkennbar.

13. Was ist ein Phonem?
* Phoneme sind Lauteinheiten, welche in einer Sprache die gleiche bedeutungsunterscheidende Funktion haben (z.B. gerolltes R und Rachen-R).

14. Wie funktioniert die Kurzzeit-Fouriertransformation?
* Das Signal wird in eine Folge überlappender Zeitfenster zerlegt, die mit einer geeigneten Fensterfunktion multipliziert werden. In jedem Fenster wird eine lokale Fourieranalyse durchgeführt.

15. Was muss man bei der Wahl des Fensters bei der Kurzzeit-Fouriertransformation 
beachten?
* Wird ein kurzes Zeitfenster gewählt, lässt sich relativ genau zeitlich lokalisieren, wann ein relativ breites Band benachbarter Frequenzen wahrnehmbar ist.

16. Wie funktioniert ein Nächste-Nachbar-Klassifikator?
* Das zu klassifizierende Signal wird mit den jeweiligen Prototypen der Klassen verglichen. Der Klassifikator entscheidet sich für die Klasse, zu deren Prototyp das Signal am ähnlichsten ist.

17. Wie unterscheiden sich Korrelation und Kovarianz als Ähnlichkeitsmaß?
* Die Korrelation hat den Nachteil, dass Signale mit hohem Mittelwert automatisch "ähnlicher" zu einander sind bzw. stärker korrelieren. Bei der Kovarianz wird dies ausgeglichen, in dem vorher der Mittelwert/das Integral bei beiden Signalen abgezogen wird.

18. Warum verwendet man meist nichtideale Filter mit welligen Durchlass- und 
Sperrbereichen und einem Übergangsbereich statt idealen frequenzselektiven Filtern?
* Man verwendet sie, um Überschwinger und Oszillationen zu vermeiden und um eine endliche kausale Impulsantwort zu erhalten.

19. Was sind Formanten?
* Der Hohlraumresonator des Mund- und Rachenraumes verstärkt Frequenzen, bei denen sich in seinem Inneren stehende Wellen bilden können. Die Frequenzbereiche, bei denen die relative Verstärkung am höchsten ist, nennt man Formanten.

20. Wie wird die momentane Frequenz eines akustischen Eingangssignals in der 
Basilarmembran des Innenohrs codiert?
* Die Basilarmembran hat ein Erregungsmaximum, dessen Ort von der Frequenz abhängt. Also wird die Frequenz durch den Ort codiert.

21. Was ist eine Schwebung?
* Eine periodische Verstärkung und Abschwächung einer Sinusschwingung.

22. Ein System liefert für eine Sinusschwingung als Eingangssignal eine doppelt so große Sinusschwingung gleicher Frequenz als Ausgangssignal, das um 10 ms verzögert ist. 
Um welche Art von System handelt es sich?
* Um ein lineares und kausales System mit Speicher.

Zusätze:

Welches System hat einen Speicher?
* Das Verzögerungsglied.

Warum muss man zur Messung der Systemantwort warten, bis das System einen stationären Zustand erreicht hat?
* Weil die durch den Einschaltvorgang angeregten Eigenschwingungen des Systems erst abklingen müssen.

Welches System hat eine Impulsantwort, die nicht aus einem Dirac-Impuls entsteht?
* Der Integrierer.
```

