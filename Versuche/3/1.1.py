# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import helper

if __name__ == '__main__':
    # data
    data_offset = 4996  # 5000
    data_length = 1287  # 1287

    # read measurements
    data = np.genfromtxt('data/ton.csv', delimiter=';', converters=helper.decconv(2), skip_header=7)

    # calculate interval
    time = data[:2, 0]  # to timestamps
    interval = np.abs(time[1] - time[0])  # length of time slice
    interval_ms = round(interval, 3)
    interval_us = round(interval * 1000, 3)
    interval_s = round(interval / 1000, 6)

    x_line = np.zeros(data_length)
    y_line = np.zeros(data_length)
    zero_crossing = np.zeros(data_length)

    i = 0
    while i < data_length:
        x_line[i] = data[data_offset + i, 0]
        y_line[i] = data[data_offset + i, 1]
        i += 1

    # Grundperiode und Grundfrequenz
    zero_crossing = helper.find_zero_crossing(y_line, data_length)  # Ermittelt die Nulldurchgänge

    period = 246
    basic_period = period * interval_ms  # Grundperiode in ms
    basic_frequency = 1 / (period * interval_s)  # Grundfrequenz

    # plot
    plt.figure(dpi=250)
    plt.plot(x_line, y_line)
    plt.ylabel('voltage in mV')
    plt.xlabel('time in ms')
    plt.grid(True)
    plt.savefig('plots/voltage_harmonica.png')
    plt.show()

    # ----------------------------------------------------------------

    print()
    print(f'Grundperiode: {basic_period} ms')
    print(f'Grundfrequenz: {round(basic_frequency, 3)} Hz')
    print(f'Signaldauer: {round(interval_s * len(data), 3)} s')
    print(f'Abtastfrequenz: {round(1 / interval_s, 3)} Hz')  # f = 1/T [T in s]
    print(f'Signallänge M: {len(data)}')  # Anzahl Datenpunkte
    print(f'Abtastintervall ∆t: {interval_s} s')  # Zeitdauer zwischen zwei Abtastpunkten
    print()
