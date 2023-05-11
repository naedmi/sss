# Vorbereitung Testat 1

------

### Lernziele:

- Verständnis der Kalibrierung eines Sensors mit nichtlinearer Kennlinie
- Messen von Kennlinien
- Lineare Regression
- Fehlerrechnung
- Dokumentation der Experimente und deren Auswertung (Versuchsbericht)

### **Vorbereitung:**

*  Arbeiten Sie Kap. 2-4 der Vorlesung durch und lesen Sie ggf. die noch zu klärenden Fragen in der in den Vorlesungsunterlagen angegebenen Literatur nach.
* Eignen Sie sich die Grundlagen der Programmiersprache Python an (Kontrollstrukturen, Tupel, Listen, Dictionaries), z.B. anhand der unten aufgeführten Links.
* Lesen Sie die Versuchsanleitung durch. Schauen Sie ggf. in den Unterlagen nach, falls etwas inhaltlich nicht klar sein sollte.

* Gehen Sie die unten bereitgestellten Testatfragen durch und beantworten Sie sie. Falls Sie die Antwort nicht wissen, lesen Sie sie in den Unterlagen nach. Getestet werden alle Bestandteile der Vorbereitung, d.h. Kap. 2-4 aus der Vorlesung, Versuchsanleitung und Numpy.

```
Fragenkatalog Testat 1
======================

1. Welche elektrische Größe misst ein Drehspul-Messwerk?
* Die Stromstärke (I) in Ampere (A).

2. Wie funktioniert ein Drehspulinstrument?
* Eine Spule ist beweglich im Magnetfeld eines Dauermagneten positioniert. Durch die mit Draht umwickelte Spule wird Strom geleitet und dadurch entsteht ein eigenes Magnetfeld und die Spule wird je nach Stärke des Stroms mehr oder weniger vom Dauermagneten angestoßen und abgestoßen. An der Spule ist ein Zeiger befestigt, der die Stromstärke auf einer Skala anzeigt. Endet der Stromfluss, wird die Spule durch eine Spirale/Feder? in die Ausgangsposition gebracht.

3. Eine indirekte Messgröße A berechnet sich als Differenz zweier direkt gemessener 
 Eingangsgrößen B und C mit absolutem Messfehler ΔB bzw. ΔC, d.h. A = B - C. Wie groß 
schätzen Sie den absoluten Messfehler ΔA?
* ΔB + ΔC

4. Sie haben eine indirekt gemessene Größe A, die von mehreren Eingangsgrößen B, C, D, ... 
abhängt, die alle den gleichen Messfehler haben. Welche der Eingangsgrößen hat den größten 
Einfluss auf den Messfehler von A?
* Kp?

5. Was leistet die lineare Regression?
* Bei vielen Messungen kann man die lineare Regression anwenden, um die Ausgleichsgerade zu bestimmen (vorausgesetzt, es besteht eine lineare Abhängigkeit zwischen den Werten).

6. Kann man die lineare Regression auch bei Kennlinien anwenden, die einem Gesetz der Form
y = x ^ a folgen?
* Nein, da es keine lineare Abbildung ist. Dafür gibt es eine nicht-lineare Regression.

7. Sie haben in Python eine 5 x 5 - Matrix a angelegt. Wie greifen Sie auf das zweite 
Element der dritten Zeile zu?
* a[2][1]

8. Ein Messintrument hat einen Anzeigefehler von 1% und einen Skalenendwert von 5A. Im 
Moment zeigt das Instrument einen Strom von 2A an. In welchem Bereich liegt der wahre 
Wert des Stroms?
* 0.01 * 5A = 0.05A
Der wahre Wert liegt zwischen 1.95A und 2.05A.

9. Auf der Anzeige Ihres analogen Messinstrumentes steht "KL 1.5". Was bedeutet das?
* Dass das Messinstrument in die Fehlerklasse 1.5 eingeteilt ist. Also sind Anzeigefehler mit Abweichungen von 1.5% des Skalenendwertes möglich.

10. Wie schätzt man den wahren Wert einer Messgröße, wenn mehrere fehlerbehaftete 
Messungen vorliegen?
* Als Schätzwert für den wahren Wert wird das arithmetische Mittel (Durchschnitt) aus den einzelnen Messwerten verwendet. 

11. Sie haben 20 Einzelmessungen mit einer Standardabweichung des Mittelwertes von s. Wie groß ist das Vertrauensintervall, in das der wahre Wert der Messgröße mit einer 
Wahrscheinlichkeit von 95,5% fällt?
* Von -2s bis 2s.

12. Warum muss man jede Messung mit dem größten Messbereich beginnen?
* Um sicherzustellen, dass das Messgerät auch bei größeren Werten voll funktionsfähig ist (und nicht durch sie zerstört wird).

13. Warum kann ein Drehspulinstrument nicht beliebig schnell veränderliche Ströme oder 
Spannungen anzeigen?
* Weil der Zeiger sich durch ein Gleichgewicht zwischen Magnet- und Rückstellkraft positioniert und Zeit zum Einschwingen benötigt.

14. Was ist der Parallaxenfehler?
* Wenn es einen Abstand zwischen Zeiger und Skala gibt, sodass der abgelesene Wert je nach Blickwinkel variieren kann.

15. Welches Messprinzip liegt dem im Praktikum eingesetzten Abstandssensor zugrunde?
* Es wird durch eine Infrarot-LED ein Lichtstrahl ausgesendet, vom Objekt reflektiert und durch eine zweite Linse auf einen optischen Positionssensor gelenkt. Ein Signalprozessor leitet eine Spannung zum Ausgang des Sensors. (Infrarotmessprinzip?)

16. Zu was benützt man ein Oszilloskop?
* Um Spannungen zu messen. Um Signale und Schwingungen zu visualisieren. 

17. Wie funktioniert ein analoges Oszilloskop?
* Es wird ein Elektronenstrahl so abgelenkt (vertikal und horizontal), dass man eine Schwingung auf einem Monitor erkennen kann.

18. Was ist der Unterschied zwischen einem Sensor und einem Messgerät?
* Der Sensor ist ein Teil vom Messgerät. Er nimmt physikalische Eigenschaften oder die stoffliche Beschaffenheit seiner Umgebung auf und wandelt sie in der Regel in elektromagnetische Signale um. Das Messgerät wandelt die vom Sensor aufgenommene Messgröße in einen angezeigten Messwert um.

19. Was für ein Sensortyp ist der im Praktikum eingesetzte Abstandssensor?
* Ein extrinsischer Sensor. Ein aktiver Sensor?

20. Wie funktioniert die Triggerung beim Oszilloskop?
* Es wird bei jedem Durchlauf die Ablenkung so lang angehalten, bis das zu messende Signal einen bestimmten Spannungswert erreicht hat. Dadurch werden die Perioden eines periodischen Signals genau übereinander gezeichnet. ?
```

