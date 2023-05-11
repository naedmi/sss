# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import helper

if __name__ == '__main__':
    # read data
    data = np.genfromtxt('data/ton.csv', delimiter=';', converters=helper.decconv(2), skip_header=7, skip_footer=0)

    # calculate interval
    time = data[:2, 0]
    interval = np.abs(time[1] - time[0])  # length of time slice
    interval_ms = round(interval, 3)
    interval_us = round(interval * 1000, 3)
    interval_s = round(interval / 1000, 6)

    fourier = np.fft.fft(data[:, 1])  # Fouriertransformation
    spectrum = np.abs(fourier)  # Fouriertransformierte Frequenz absolutieren -> keine negativen Werte
    freq = range(0, len(spectrum), 1) / (len(data) * interval_s)  # Anzahl der Schwingungen
    # in die Frequenz umzurechnen: f = n / (M * Δt)

    x_line = np.zeros(1000)
    y_line = np.zeros(1000)
    zeroCrossing = helper.find_zero_crossing(y_line, 1000)  # Nulldurchgänge

    # Grundperiode und Grundfrequenz
    period = 246
    basic_period = period * interval_ms  # Grundperiodenlänge in ms
    basic_frequency = 1 / (period * interval_s)  # Grundfrequenz

    # Darstellung des Amplitudenspektrums
    plt.plot(freq / 1e3, spectrum)
    plt.ylabel('amplitude in V')
    plt.xlabel('frequency in kHz')
    plt.grid(True)
    plt.savefig('plots/spectrum_harmonica.png')
    plt.show()

    # Teil 2
    plt.plot((freq / 1e3)[0:400], spectrum[0:400], 'r')
    plt.ylabel('amplitude in V')
    plt.xlabel('frequency in kHz')
    plt.grid(True)
    plt.savefig('plots/spectrum_harmonica_zoom.png')
    plt.show()

    print()
    print(f'Grundperiode: {basic_period} ms')
    print(f'Grundfrequenz: {round(basic_frequency, 3)} Hz')
    print(f'Signaldauer: {round(interval_s * len(data), 3)} s')
    print(f'Abtastfrequenz: {round(1 / interval_s, 3)} Hz')  # f = 1/T [T in s]
    print(f'Signallänge M: {len(data)}')  # Anzahl Datenpunkte
    print(f'Abtastintervall ∆t: {interval_s} s')  # Zeitdauer zwischen zwei Abtastpunkten
    print()

    # -------------------------------------------------------------------------- Part 2
    print("Frequenz mit der größten Amplitude", np.max(spectrum))
    print()