import numpy as np
import matplotlib.pyplot as plt


def std(messfehler):
    n = len(messfehler)
    return np.sqrt(1 / (n - 1) * np.sum(messfehler ** 2))


if __name__ == '__main__':
    u_min = -10
    u_max = 10
    n_bits = 11

    delta_u = (u_max - u_min) / 2 ** n_bits

    print("theoretischer Quantisierungsfehler: " + str(delta_u * 1000) + "mV")

    data = np.genfromtxt("data/2.csv", delimiter=";", skip_header=1)

    voltage = data[:, 0]
    feinmessgeraet = data[:, 4]
    multimeter = data[:, 1]
    picoscope = data[:, 2]
    adwandler = data[:, 3]

    messfehler_multimeter = feinmessgeraet - multimeter
    messfehler_picoscope = feinmessgeraet - picoscope
    messfehler_adwandler = feinmessgeraet - adwandler


    std_multimeter = std(messfehler_multimeter)
    std_picoscope = std(messfehler_picoscope)
    std_adwandler = std(messfehler_adwandler)

    print("std multimeter: " + str(std_multimeter * 1000) + " mV")
    print("std a/d-wandler: " + str(std_adwandler * 1000) + " mV")
    print("std picoscope: " + str(std_picoscope * 1000) + " mV")

    plt.plot(voltage, messfehler_adwandler, label="A/D-Wandler")
    plt.plot(voltage, messfehler_multimeter, label="Multimeter")
    plt.plot(voltage, messfehler_picoscope, label="Picoscope")
    plt.xlabel("Spannung in V")
    plt.ylabel("Abweichung in V")
    plt.legend()
    # plt.savefig("plots/2_messfehler.png")
    # splt.show()
