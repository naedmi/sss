# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import helper

if __name__ == '__main__':
    dataKlein = np.genfromtxt('data/versuch_2/little_speaker.csv', delimiter=';', skip_header=3,
                              converters=helper.decconv(3))
    dataGross = np.genfromtxt('data/versuch_2/big_speaker.csv', delimiter=';', skip_header=3,
                              converters=helper.decconv(3))

    # Amplituden der Lautsprecher
    grossAmp = dataGross[:, 1]
    kleinAmp = dataKlein[:, 1]
    grossPhase = dataGross[:, 2]
    kleinPhase = dataKlein[:, 2]
    freq = dataGross[:, 0]

    # Plot Amplitude
    plt.figure(1)
    plt.plot(freq, grossAmp, 'r', label='big speaker')
    plt.plot(freq, kleinAmp, 'b', label='little speaker')
    plt.title("Amplitude")
    plt.xlabel("Frequenz in Hz")
    plt.ylabel("Amplitude in mV")
    plt.grid(True)
    plt.show()

    # Plot Phasengang
    plt.figure(2)
    plt.plot(freq, kleinPhase, 'r', label='big speaker')
    plt.plot(freq, grossPhase, 'b', label='little speaker')
    plt.title("Phasengang")
    plt.xlabel("Frequenz in Hz")
    plt.ylabel("Phasenverschiebung in µs ")
    plt.grid(True)
    plt.show()

    # 20 log10 zur Berechung des Bode-Diagramms kleiner Lautsprecher
    kleinAmp = 1 / kleinAmp
    kleinAmp = 20 * np.log10(kleinAmp)

    # 20 log10 zur Berechung des Bode-Diagramms grosser Lautsprecher
    grossAmp = 1 / grossAmp
    grossAmp = 20 * np.log10(grossAmp)

    # Phasenwinkel mit −∆t * f * 360 für den kleinen Lautsprecher
    kleinPhase = (kleinPhase * -1) * freq * 360

    # Phasenweinkel mit −∆t * f * 360 für den großen Lautsprecher
    grossPhase = (grossPhase * -1) * freq * 360

    # Plot Amplitude Bodediagramm großer Lautsprecher
    plt.figure(3)
    # plt.plot(freq, grossAmp, 'y', label = 'big speaker')
    # plt.plot(freq, kleinAmp, 'r', label = 'little speaker')
    plt.semilogx(freq, grossAmp, 'b')
    plt.semilogx(freq, kleinAmp, 'r')
    plt.title("Bode-Amplitude")
    plt.xlabel("Frequenz in Hz")
    plt.ylabel("Amplitude in dB")
    plt.grid(True)
    plt.show()

    # Plot Phasengang Bodediagramm kleiner Lautsprecher
    plt.figure(4)
    # plt.plot(freq, grossPhase, 'y', label = 'big speaker')
    # plt.plot(freq, kleinPhase, 'r', label = 'little speaker')
    plt.semilogx(freq, grossPhase, 'b')
    plt.semilogx(freq, kleinPhase, 'r')
    plt.title("Bode-Phasengang")
    plt.xlabel("Frequenz in Hz")
    plt.ylabel("Phasenverschiebung in ° ")
    plt.grid(True)
    plt.show()
