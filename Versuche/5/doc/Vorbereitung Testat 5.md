# Vorbereitung Testat 5

------

### Lernziele:

- Umgang mit Analog-zu-Digital- und Digital-zu-Analog-Wandlern
- Messung der Genauigkeit der AD- und DA-Wandlung
- Untersuchung des Zeitverhaltens der DA-Wandlung
- Praktische Erfahrungen mit dem Abtasttheorem

### **Vorbereitung:**

* Arbeiten Sie Kap. 15-17 der Vorlesung durch und lesen Sie ggf. die noch zu klärenden Fragen in der in den Vorlesungsunterlagen angegebenen Literatur nach.
* Gehen Sie die unten bereitgestellten Testatfragen durch und beantworten Sie sie. Falls Sie die Antwort nicht wissen, lesen Sie sie in den Unterlagen nach. Getestet werden alle Bestandteile der Vorbereitung, d.h. Kap.15-17 aus der Vorlesung.
* Lesen Sie die Versuchsanleitung durch. Schauen Sie ggf. in den Unterlagen nach, falls etwas inhaltlich nicht klar sein sollte.

```
Fragenkatalog Testat 5
======================

1. Wie beschreibt man mathematisch die Abtastung eines Signals g(t) zum Zeitpunkt t1?
* Durch die Multiplikation mit einer verschobenen Deltafunktion d(t - t1).

2. Wie sieht das Spektrum einer mit Abtastintervall 1 abgetasteten Funktion mit Spektrum G(omega) aus?
* Das ursprüngliche Spektrum des Signals wird unendlich oft im Abstand 1 wiederholt.

3. Wie verändert sich das Spektrum einer Kammfunktion, wenn man das Abtastintervall 
verdreifacht?
* Die Impulse des Spektrums rücken um das Dreifache zusammen.

4. Unter welchen Bedingungen entsteht Aliasing?
* Abstastfrequenz < 2 * Maximalfrequenz

5. Wie funktioniert das Sägezahnverfahren bei der A/D-Wandlung?
* Das Sägezahnverfahren ist ein Zählverfahren: Man zählt solange die Anzahl der regelmäßig getakteten Impulse ab, bis eine Sägezahnspannung den Sample-and-Hold-Wert überschreitet. Die Zahl der gezählten Impulse ist das quantisierte Ergebnis.


6. Welche scheinbare Frequenz hat ein Sinussignal der Frequenz f0, wobei f0 größer als die Nyquistfrequenz, aber kleiner als die Abtastfrequenz f1 ist?
* Die Frequenz erscheint kleiner als die Nyquistfrequenz, und zwar f1 - f0.

7. Was ist Aliasing?
* Aliasing tritt auf, wenn ein Signal mit mehr als der doppelten Nyquistfrequenz abgetastet wird. Aliasing bedeutet Überlappung der Kopien des Spektrums.

8. Wie schafft man es, die Fouriertransformierte eines diskreten Signals im Computer zu berechnen, obwohl seine Fouriertransformierte kontinuierlich ist?
* Das Eingangssignal wird periodisch fortgesetzt. Im Rechner wird das resultierende periodische Spektrum nur durch eine Periode repräsentiert.

9. Ist die diskrete Fouriertransformation und die Fouriertransformation bei zeitdiskreten Signalen das Gleiche?
* Nein. 
  Diskrete Fouriertransformation -> endliches Spektrum
  Fouriertransformierte eines zeitdiskreten Signals -> unendliches Spektrum

10. Was ist ein FIR-Filter?
* Finite Impulse Response: Aus einer Serie von Verzögerungsgliedern werden die letzten Eingangswerte mit dem Filterkoeffizienten multipliziert und dann aufsummiert. Die Werte der Koeffizienten sind die Impulsantwort.

11. Was ist ein FFT-Filter?
* Ein Filter, bei dem das Einganssignal zuerst in den Frequenzbereich fouriertransformiert wird, dann mit dem Frequenzgang multipliziert und über IFFT wieder in den Zeitbereich rücktransformiert wird. So werden nicht erwünschte Frequenzbereiche auf Null gesetzt.

12. Wieviele Fourierkoeffizienten hat die Fourierreihe eines diskreten Signals, das aus 8 Abtastpunkten besteht?
* Sie hat 8 Fourierkoeffizienten.

13. Warum braucht man bei diskreten periodischen Signalen nur endliche Fourierreihen zu ihrer Darstellung?
* Weil es nur endlich viele harmonisch verwandte diskrete Sinus-Signale gibt.

14. Was sind die Unterschiede zwischen den Analysegleichungen der diskreten und 
kontinuierlichen Fourierreihe?
* Das Integral ist durch eine Summe ersetzt, der Normierungsfaktor ist unterschiedlich.

15. Warum reicht bei diskreten linearen Systemen die Antwort auf einen Einheitsimpuls zum Zeitpunkt 0, um es vollständig zu charakterisieren?
* 

16. Wie berechnet man die Systemantwort eines diskreten linearen Systems?
* Die Impulsantwort wird an der y-Achse gespiegelt, punktweise mit dem Signal multipliziert und alles aufsummiert.

17. Was ist der Hauptunterschied zwischen dem Spektrum eines aperiodischen 
kontinuierlichen Signals und dem eines aperiodischen diskreten Signals?
* Das Spektrum des diskreten Signals ist periodisch, das des kontinuierlichen Signals nicht.

18. Wie sieht ein idealer zeitdiskreter Tiefpass im Spektralraum aus?
* Eine achsensymmetrische Sinc-Funktion.

19. Ein zeitdiskreter Filter besteht aus der Differenz des momentanen Inputwertes und des Inputwertes des vergangenen Zeitschritts. Um was für eine Art von Filter handelt es sich?
* Differenz -> Hochpass
  Durchschnitt -> Tiefpass

20. Ist eine zeitdiskrete Sinusschwingung immer periodisch?
* Nein, nur wenn die Periode oder ganzzahlige Vielfache der Periode ein ganzzahliges Vielfaches des Abtastintervalls darstellen.

```

