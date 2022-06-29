import numpy as np


def std(messfehler):
    n = len(messfehler)
    return np.sqrt(1 / (n - 1) * np.sum(messfehler ** 2))


if __name__ == '__main__':
    u_min = 0
    u_max = 5
    n_bits = 10

    delta_u = (u_max - u_min) / 2 ** n_bits

    print("theoretischer Quantisierungsfehler: " + str(delta_u * 1000) + "mV")

    data = np.genfromtxt("data/3.csv", delimiter=";", skip_header=1)

    voltage = data[:, 0]
    feinmessgeraet = data[:, 1]
    multimeter = data[:, 2]
    picoscope = data[:, 3]

    messfehler = voltage - feinmessgeraet
    messfehler_multimeter = voltage - multimeter
    messfehler_picoscope = voltage - picoscope

    std_feinmessgeraet = std(messfehler)
    std_multimeter = std(messfehler_multimeter)
    std_picoscope = std(messfehler_picoscope)

    print("Messfehler Feinmessgerät zu Eingabe: " + str(std_feinmessgeraet * 1000) + " mV")
    print("Messfehler Multimeter zu Eingabe: " + str(std_multimeter * 1000) + " mV")
    print("Messfehler Picoscope zu Eingabe: " + str(std_picoscope * 1000) + " mV")
    # print("Verhältnis Messfehler zu theor. QF: " + str(std_feinmessgeraet / delta_u))
