import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

global a, b

# distance values
x = [10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70]

# mean values of voltage (protocol)
y = [1.362, 1.193, 1.011, 0.9611, 0.8398, 0.8209, 0.7439, 0.6581, 0.618, 0.580, 0.5417, 0.5226,
     0.4473, 0.4474, 0.403, 0.403, 0.3817, 0.3398, 0.300, 0.320, 0.3002]


def conv(_):
    return _.replace(',', '.').encode()


def read(path):
    return np.genfromtxt((conv(_) for _ in open(path)), delimiter=';',
                         dtype=np.double, skip_header=300, skip_footer=50, usecols=1)


# umkehrung
def f(v):
    return np.e ** b * v ** a


if __name__ == '__main__':
    # read data
    z = []
    std = []
    for num in range(10, 73, 3):
        values = read(f'data/{num}.csv')
        z.append(np.mean(values))
        std.append(np.std(values))

    # calculate logarithms
    log_volt, log_dist = np.log(y), np.log(x)

    # calculate linear regression
    result = stats.linregress(log_volt, log_dist)
    x1 = np.linspace(np.min(log_volt), np.max(log_volt), 21)
    a = result.slope
    b = result.intercept
    y1 = result.slope * x1 + result.intercept  # slope -> gradient

    # 1st plot - characteristic curve
    plt.title('Kennlinie')
    plt.xlabel('Abstand [cm]')
    plt.ylabel('Spannung [V]')
    plt.plot(x, y, label="protocol", linewidth=1)
    plt.plot(x, z, label="data", linewidth=1)
    plt.legend()
    plt.savefig('plots/characteristic.png')
    plt.show()

    # # 2nd plot - standard deviation
    # plt.title('Standardabweichung')
    # plt.xlabel('Abstand [cm]')
    # plt.ylabel('Spannung [V]')
    # plt.plot(x, std)
    # plt.axis([7, 73, 0, 0.1])
    # plt.savefig('plots/std.png')
    # plt.show()

    # 3rd plot - logarithm
    plt.title('Logarithmierte Werte')
    plt.xlabel('(logarithmierter) Abstand [cm]')
    plt.ylabel('(logarithmierte) Spannung [V]')
    plt.plot(log_volt, log_dist)
    plt.savefig('plots/log.png')
    plt.show()

    # 4th plot - linear regression
    plt.title('Lineare Regression - Ausgleichsgerade')
    plt.ylabel('(logarithmierter) Abstand [cm]')
    plt.xlabel('(logarithmierte) Spannung [V]')
    plt.plot(log_volt, log_dist, 'ob')
    plt.plot(x1, y1, '-r')
    plt.savefig('plots/linear-regression.png')
    plt.show()

    print("Nichtlineare Kennlinie: y = e^%.3f * x^%.3f\n" % (result.intercept, result.slope))

    a4_length = read(f'data/a4-lang.csv')
    a4_length_mean = np.mean(a4_length)
    a4_width = read(f'data/a4-breit.csv')
    a4_width_mean = np.mean(a4_width)

    std = np.std(a4_length) / math.sqrt(len(a4_length))  # Standardabweichung / Wurzel(n)
    print(f'std = {std}\n')
    print(f'68.26%: result is between {a4_length_mean - std} V and {a4_length_mean + std} V')
    print(f'95%: result is between {a4_length_mean - 1.96 * std} V and {a4_length_mean + 1.96 * std} V\n')

    length_err = result.slope * np.e ** result.intercept * a4_length_mean ** (result.slope - 1) * std
    print(f'err = {-length_err}\ndist = {f(a4_length_mean)}cm\n')

    print('---------------------------------------------------------------------------------------')

    std = np.std(a4_width) / math.sqrt(len(a4_width))  # Standardabweichung / Wurzel(n)
    print(f'std = {std}\n')
    print(f'68.26%: result is between {a4_width_mean - std} V and {a4_width_mean + std} V')
    print(f'95%: result is between {a4_width_mean - 1.96 * std} V and {a4_width_mean + 1.96 * std} V\n')

    width_err = result.slope * np.e ** result.intercept * a4_width_mean ** (result.slope - 1) * std
    print(f'err = {-width_err}\ndist = {f(a4_width_mean)}cm\n')

    print('---------------------------------------------------------------------------------------')

    length_dist = f(a4_length_mean)
    width_dist = f(a4_width_mean)
    print("Fläche: x = %f +- %f [cm^2]" % (length_dist * width_dist, math.sqrt((width_dist * length_err) ** 2
                                                                               + (length_dist * width_err) ** 2)))
