import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


def windowing(data):
    size = 512
    step = 256

    sub = [data[i: i + size] for i in range(0, len(data), step)]  # divide
    gaus = signal.windows.gaussian(512, 512 / 4)  # gaussian window func

    windows10 = [np.concatenate((np.zeros(i * 256), np.array(gaus * sub[i]),
                                 np.zeros((len(sub) - 1 - i) * 256))) for i in range(0, len(sub) - 2)]

    ffts = [np.fft.rfft(i) for i in windows10]  # local fourier transform
    fft = np.abs(np.array(ffts).mean(0))
    return fft


def main(file_name, word):
    data = np.load(f'data/{file_name}.npy')
    fft = windowing(data)
    plt.plot(fft)
    plt.xlim(0, 1600)
    plt.ylabel('amplitude')
    plt.xlabel('frequency [Hz]')
    plt.title(f'amplitude spectrum \"{word}\"')
    plt.savefig(f'plots/{file_name}_spectrum.png')
    plt.show()


if __name__ == '__main__':
    main('reference_hoch', 'hoch')
