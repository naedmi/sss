import numpy as np


def decconv(col_num):
    conv = dict((col, lambda valstr:
                float(valstr.decode('utf-8').replace(',', '.'))) for col in range(col_num))
    return conv


# Ermittelt die Nulldurchgänge eines Signal
# return: Array mit Nulldurchgängen, wobei höherer Wert = näher am Nulldurchgang
def find_zero_crossing(src, length):
    arr = np.zeros(length)  # Erstelle neues leeres Array
    faktor = [1, 2, 4, 8, 16, 16, 8, 4, 2, 1]

    # Iteriert über src und schaut hierbei von der aktuellen Stelle 5 vor
    # und 5 zurück. Umso mehr nullen um den aktuellen Index umso höher wird
    # dessen "Nullwert". Durch den Faktor wird die Entfernung zur derzeitigen
    # Position gewichtet
    for i in range(5, length - 5):

        jmin = i - 5
        jmax = i + 5
        j = np.linspace(jmin, jmax, 11, dtype=int)

        for x in j:
            if src[x] == 0:
                arr[i] = arr[i] + faktor[x - i]

    return arr


def smooth(src, length):
    maxVal = max(src)
    for i in range(0, length):
        if src[i] < (maxVal * 0.5):
            src[i] = 0

    return src
