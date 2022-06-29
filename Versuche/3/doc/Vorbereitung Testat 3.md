# Vorbereitung Testat 3

------

### Lernziele:

- Umgang mit Mikrofonen und Lautsprechern
- Praktisches Verständnis der Fourierreihe und der Fourieranalyse
- Messung des Frequenzgangs von Lautsprechern

### **Vorbereitung:**

* Arbeiten Sie Kap. 8-10 der Vorlesung durch und lesen Sie ggf. die noch zu klärenden Fragen in der in den Vorlesungsunterlagen angegebenen Literatur nach.
* Gehen Sie die unten bereitgestellten Testatfragen durch und beantworten Sie sie. Falls Sie die Antwort nicht wissen, lesen Sie sie in den Unterlagen nach. Getestet werden alle Bestandteile der Vorbereitung, d.h. Kap. 8-10 aus der Vorlesung.
* Lesen Sie die Versuchsanleitung durch. Schauen Sie ggf. in den Unterlagen nach, falls etwas inhaltlich nicht klar sein sollte.

```
Fragenkatalog zu Testat 3
==========================


1. Wie verändert sich das Spektrums einer Rechteckschwingung mit fester Impulsdauer, bei der die Periode immer weiter erhöht wird?
* Wird die Periodendauer T bei gleichbleibender Impulsdauer größer, wird der Abstand der Linien 1/T im Frequenzbereich immer kleiner bis die einzelnen Linien zu einem kontinuierlichem Spektrum verschmelzen.
* ![[Pasted image 20220507203823.png]]

2. Was ist ein fastperiodisches Signal?
* Fastperiodische Signale sind Signale, die grundsätzlich nichtperiodisch sind, jedoch in einzelnen Abschnitten periodisch verlaufen.

3. Sie beobachten ein Spektrum aus mehreren Linien bei 100 Hz, 200 Hz, 270 Hz, 400 Hz und 800 Hz. Um was für einen Signaltyp handelt es sich?
* Mehrere Linien  (also ein diskretes Linienspektrum) deuten in der Regel zwar auf eine periodisches Signal, allerdings sind die Frequenzen nicht ausschließlich ganzzahlige Vielfache der Grundfrequenz. Es handelt sich daher um ein quasiperiodisches Signal.

4. Welche Signale lassen sich als Fourierreihe darstellen?
* Alle praktischen Signale bzw. alle realen periodischen Signale.

5. Wie sieht das Spektrum eines einzelnen Rechteckimpulses aus?
* Aus einer Linie, die durch eine Sinc-Funktion beschrieben werden kann:
  sinc x = (sin x)/x

6. Wie sieht die Fouriertransformierte des mit 2 skalierten Einheitsimpulses aus?
* 1*2 = 2 ???

7. Wie kann man am Besten die wechselnde Tonhöhe in der Aufnahme eines Solo-Musikstückes
bestimmen?
* Mit Hilfe von Windowing. Man teilt das lang andauernde Signal in aufeinanderfolgende, überlappende Fenster auf und führt dort eine lokale Fourieranalyse aus, nachdem man den Abschnitt mit einer möglichst glatten Fensterfunktion (z.B. Gaußfunktion) multipliziert hat.

8. Sie zerlegen ein relativ glattes, periodisches Signal in mehrere Abschnitte und 
bestimmen in jedem Abschnitt die lokale Fouriertransformation. Wie unterscheiden sich die lokalen Spektra vom Gesamtspektrum und warum?
* Die lokalen Spektra besitzen deutlich höhere Frequenzen, da durch das Ausschneiden steile Übergänge entstehen und diese viele hohe Frequenzen im Spektrum erzeugen.

9. Was bedeutet die Komplementarität von Frequenz und Zeit?
* Dass das Frequenzband und die Zeitdauer eines Signals nicht unabhängig voneinander gemessen werden können. Je eingeschränkter das Frequenzband eines Signals ist, desto größer muss zwangsläufig die Zeitdauer sein und umgekehrt.

10. Wie berechnet man die Frequenzunschärfe eines Signals?
* Es gilt die Frequenz-Zeit-Unschärferelation Δt * Δf >= 0.88.

11. Was besagt die Frequenz-Zeit-Unschärferelation?
* Man kann niemals gleichzeitig Zeitdauer und Frequenz genauer als σ_t * σ_ω = 1 angeben.

12. Bei welchem Signal ist das Produkt aus Zeit- und Frequenzunschärfe genau gleich 1?
* Bei Gabor-Wavelets.

13. Was ist der Unterschied zwischen der Fourierreihe und dem Spektrum eines periodischen Signals?
* Bei einem periodischen Signal sind Fourierreihe und Spektrum identisch (außer an evtl. Unstetigkeiten).

14. Was ist die Ausblendeigenschaft des Dirac-Impulses?
* Da der Dirac-Impuls d(t) an d(0) unendlich hoch ist und für alle anderen t gegen 0 konvergiert, ergibt sich für das Integral d(t) * f(t) dt = f(0).

15. Bei dem Spektrum eines Signals ist der Realteil gerade und der Imaginärteil ungerade. Um was für einen Signaltyp handelt es sich?
* Es handelt sich um ein reelles Signal.

16. Die Fouriertransformierte von f_1(t) sei F_1(ω), die Fouriertransformierte von f_2(t) sei F_2(ω). Wie sieht die Fouriertransformierte von 
f(t) = 3 * f_1(ω) - 0.7 * f_2(ω) aus, und welche Eigenschaft macht man sich dabei zunutze?
* Aufgrund von der Linearitätseigenschaft gilt F(t) = 3 * F_1(t) - 0.7 * F_2(t).

17. Was passiert mit dem Spektrum eines Signals, wenn man es in zeitlicher Richtung 
verschiebt?
* Der Betrag des Spektrums bleibt unverändert, nur die Phase ändert sich (wird mit gleichem Faktor multipliziert).

18. Wie sieht das Spektrum eines Signals aus, das um den Faktor 2 im Zeitbereich gestreckt wird?
* Das Spektrum wird um den Faktor 2 gestaucht.

19. Was passiert mit dem Spektrum eines Signals, wenn man es mit einem konstanten
Phasenfaktor mit dem Phasenwinkel a multipliziert?
* ???

20. Was ist das Gibbs-Phänomen?
* Bei unstetigen Signalen konvergiert der maximale Abstand zwischen endlichen Fourierreihen und Zielsignal nicht. An Unstetigkeitsstellen entstehen Gibbsche Über- und Unterschwinger.

```

