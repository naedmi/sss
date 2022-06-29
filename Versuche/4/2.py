import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import os


def create_references():
    for s in ('hoch', 'tief', 'links', 'rechts'):
        spectrum_all = []
        for i in range(1, 6):
            data = np.load(f'data/recording_{s}_{i}.npy')  # read all .npy files for each word
            spectrum_all.append(eins.windowing(data))

        reference = np.abs(np.mean(spectrum_all, 0))  # mean of all recordings
        np.save(f'data/reference_{s}', reference)

        plt.plot(reference)
        plt.xlim(0, 1600)
        plt.ylabel('amplitude')
        plt.xlabel('frequency [Hz]')
        plt.title(f'reference amplitude spectrum \"{s}\"')
        plt.savefig(f'plots/reference_{s}_spectrum.png')
        plt.show()


def test(testfile_path):
    data = eins.windowing(np.load(testfile_path))

    print('hoch ' + str(stats.pearsonr(data, np.load('data/refs/reference_hoch.npy'))))
    print('tief ' + str(stats.pearsonr(data, np.load('data/refs/reference_tief.npy'))))
    print('rechts ' + str(stats.pearsonr(data, np.load('data/refs/reference_rechts.npy'))))
    print('links ' + str(stats.pearsonr(data, np.load('data/refs/reference_links.npy'))))


def print_correlation():
    print('--------------------------------')
    print('testing hoch')
    print('--------------------------------')
    test('data/test/recording_hoch_2.npy')
    print('--------------------------------')

    print('\n\n--------------------------------')
    print('testing rechts')
    print('--------------------------------')
    test('data/test/recording_rechts_2.npy')
    print('--------------------------------')

    print('\n\n--------------------------------')
    print('CONTROL testing rechts reference')
    print('--------------------------------')
    data = np.load('data/refs/reference_rechts.npy')
    print('hoch ' + str(stats.pearsonr(data, np.load('data/refs/reference_hoch.npy'))))
    print('tief ' + str(stats.pearsonr(data, np.load('data/refs/reference_tief.npy'))))
    print('rechts ' + str(stats.pearsonr(data, np.load('data/refs/reference_rechts.npy'))))
    print('links ' + str(stats.pearsonr(data, np.load('data/refs/reference_links.npy'))))
    print('--------------------------------')


def voice_recog():
    hit = 0
    miss = 0
    data_nad = [0, 0]  # hit, miss
    data_mav = [0, 0]
    for f in [f for f in os.listdir('data/test')]:
        if 'flo' not in f:  # sry flo
            val = eins.windowing(np.load(f'data/test/{f}'))
            fn = ''
            max_coef = 0
            for filename in os.listdir('data/refs'):
                file = np.load(f'data/refs/{filename}')
                coef = stats.pearsonr(val, file)
                if max_coef < coef[0]:  # get highest coefficient
                    max_coef = coef[0]
                    fn = filename
            if fn[9:-4] in f:  # is result correct?
                hit = hit + 1
                if 'mav' in f:
                    data_mav[0] = data_mav[0] + 1
                else:
                    data_nad[0] = data_nad[1] + 1
            else:
                miss = miss + 1
                if 'mav' in f:
                    data_mav[1] = data_mav[1] + 1
                else:
                    data_nad[1] = data_nad[1] + 1

    # person 1
    print('nada stats:')
    print('1 hit:\t\t' + str(data_nad[0]))
    print('1 miss:\t\t' + str(data_nad[1]))
    print('1 hit-rate:\t' +
          str(round((data_nad[0] / (data_nad[0] + data_nad[1])) * 100, 3)) + '%\n')

    # person 2
    print('mav stats:')
    print('2 hit:\t\t' + str(data_mav[0]))
    print('2 miss:\t\t' + str(data_mav[1]))
    print('2 hit-rate:\t\t' +
          str(round((data_mav[0] / (data_mav[0] + data_mav[1])) * 100, 3)) + '%\n')

    # total
    print('hit:\t\t\t' + str(hit))
    print('miss:\t\t\t' + str(miss))
    print('hit-rate:\t\t' + str(round((hit / (hit + miss) * 100), 3)) + '%')


if __name__ == '__main__':
    eins = __import__('1')
    # create_references()
    # print_correlation()
    voice_recog()
