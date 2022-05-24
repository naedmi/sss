import matplotlib.pyplot as plt
import numpy as np
import data.measurements as data

if __name__ == '__main__':
    # _amplitudeLarge = [20 * np.log10(1 / data.amplitude_big[x])
    _amplitudeLarge = [20 * np.log10(0.001 * data.amplitude_big[x]/data.peak_b_big[x])
                       for x in range(0, len(data.amplitude_big))]

    # _amplitudeSmall = [20 * np.log10(1 / data.amplitude_small[x])
    _amplitudeSmall = [20 * np.log10(0.001 * data.amplitude_small[x]/data.peak_b_small[x])
                       for x in range(0, len(data.amplitude_small))]

    # −∆t * f * 360
    _phaseShiftLarge = [(data.phase_shift_big[x] * -1) * data.freq[x] * 360
                        for x in range(0, len(data.phase_shift_big))]

    _phaseShiftSmall = [(data.phase_shift_small[x] * -1) * data.freq[x] * 360
                        for x in range(0, len(data.phase_shift_small))]

    plt.plot(data.freq, _amplitudeSmall, 'b', label='small speaker')
    plt.plot(data.freq, _amplitudeLarge, 'y', label='big speaker')
    plt.title('Bode Amplitude')
    plt.ylabel('amplitude in dB')
    plt.xlabel('frequency in Hz')
    plt.grid(True)
    plt.semilogx()
    plt.legend()
    plt.savefig('plots/bode_amplitude-frequency.png')
    plt.show()

    plt.plot(data.freq, _phaseShiftSmall, 'b', label='small speaker')
    plt.plot(data.freq, _phaseShiftLarge, 'y', label='big speaker')
    plt.title('Bode Phase-Shift')
    plt.ylabel('phase shift in µsec')
    plt.xlabel('frequency in Hz')
    plt.grid(True)
    plt.semilogx()
    plt.legend()
    plt.savefig('plots/bode_phase-frequency.png')
    plt.show()
