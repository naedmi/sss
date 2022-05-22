# -*- coding: utf-8 -*-

# Useful links
# https://data36.com/linear-regression-in-python-numpy-polyfit/

import numpy as np
import matplotlib.pyplot as plt
import helper

if __name__ == '__main__':
    # data
    DataOffset = 4996  # 5000
    DataLength = 1287  # 1287
    # Periodenlänge 429

    # read data
    data = np.genfromtxt('data/ton.csv', delimiter=';', converters=helper.decconv(2), skip_header=7)

    # calculate interval
    time = data[:2, 0]  # get to timestamps
    interval = np.abs(time[1] - time[0])  # length of time slice
    interval_ms = round(interval, 3)
    interval_us = round(interval * 1000, 3)
    interval_s = round(interval / 1000, 6)

    x_line = np.zeros(DataLength)
    y_line = np.zeros(DataLength)
    zeroCrossing = np.zeros(DataLength)

    i = 0
    while i < DataLength:
        x_line[i] = data[DataOffset + i, 0]
        y_line[i] = data[DataOffset + i, 1]
        i += 1

    # Grundperiode und Grundfrequenz
    zeroCrossing = helper.find_zero_crossing(y_line, DataLength)  # Ermittelt die Nulldurchgänge

    period = 429
    basicPeriod = period * interval_ms  # Grundperiodenlänge in ms
    basicFrequenz = 1 / (period * interval_s)  # Grundfrequenz

    # plot
    # fig, ax = plt.subplots()
    plt.figure(dpi=250)
    plt.plot(x_line, y_line)

    plt.ylabel('voltage in mV')
    plt.xlabel('time in ms')
    plt.grid(True)
    plt.savefig('plots/voltage_harmonica.png')
    plt.show()

    # ----------------------------------------------------------------

    print()
    print(f'Grundperiode: {basicPeriod} ms')
    print(f'Grundfrequenz: {round(basicFrequenz, 3)} Hz')
    print(f'Signaldauer: {round(interval_s * len(data), 3)} s')
    print(f'Abtastfrequenz: {round(1 / interval_s, 3)} Hz')  # f = 1/T [T in s]
    print(f'Signallänge M: {len(data)}')  # Anzahl Datenpunkte
    print(f'Abtastintervall ∆t: {interval_s} s')  # Zeitdauer zwischen zwei Abtastpunkten
    print()
