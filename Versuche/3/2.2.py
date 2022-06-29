import matplotlib.pyplot as plt
import numpy as np
import data.measurements as data

if __name__ == '__main__':
    _amplitude_big = [20 * np.log10(1 / data.amplitude_big[x])
                      for x in range(0, len(data.amplitude_big))]

    _amplitude_small = [20 * np.log10(1 / data.amplitude_small[x])
                        for x in range(0, len(data.amplitude_small))]

    # −∆t * f * 360
    _phase_shift_big = [(data.phase_shift_big[x] / 1000000 * -1) * data.freq[x] * 360
                        for x in range(0, len(data.phase_shift_big))]

    _phase_shift_small = [(data.phase_shift_small[x] / 1000000 * -1) * data.freq[x] * 360
                          for x in range(0, len(data.phase_shift_small))]

    plt.plot(data.freq, _amplitude_small, 'b', label='small speaker')
    plt.plot(data.freq, _amplitude_big, 'y', label='big speaker')
    plt.title('Bode Amplitude')
    plt.ylabel('amplitude in dB')
    plt.xlabel('frequency in Hz')
    plt.grid(True)
    plt.semilogx()
    plt.legend()
    plt.savefig('plots/bode_amplitude-frequency.png')
    plt.show()

    plt.plot(data.freq, _phase_shift_small, 'b', label='small speaker')
    plt.plot(data.freq, _phase_shift_big, 'y', label='big speaker')
    plt.title('Bode Phase-Shift')
    plt.ylabel('phase shift in °')
    plt.xlabel('frequency in Hz')
    plt.grid(True)
    plt.semilogx()
    plt.legend()
    plt.savefig('plots/bode_phase-frequency.png')
    plt.show()
