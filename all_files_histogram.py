from simple_batch_processing import buscar_arquivos
from scipy.io import wavfile
import numpy as np
import multiprocessing as mp
import matplotlib.pyplot as plt
import os

def compute_energy(file, N: int =100 # window size
                   ):
    _, signal = wavfile.read(file)
    if signal.ndim > 1:
        signal = signal[:, 0]
    n_seg = len(signal) // N
    return [np.sum(np.square(signal[i * N : (i + 1) * N], dtype=float)) for i in range(n_seg)]

diretorio_timit = "./timit"
extension = ".wav"
files = buscar_arquivos(diretorio_timit, extensao=extension)
window_size = 100
max_cpu_threads = max(1, os.cpu_count() - 1)  # dummy way of getting maximum available CPU threads
assert len(files) > 0, "must have at least one file, obviously."

'''
Ok, this is a bit of a hack, but it works xD. The idea is to use the multiprocessing library to
do it in parallel. The function compute_energy will be called for each file in the list.
The results will be collected in a list and then concatenated into a single array.
This *starmap* is an autonomous function, in such a way that if the first thread
finishes before the others, it will start processing the next file in the list.
'''
with mp.Pool(max_cpu_threads) as pool:
    results = pool.starmap(compute_energy, [(file, window_size) for file in files])

energies = np.concatenate(results)
plt.hist(energies, bins=50, color='blue', alpha=0.7)
plt.xlabel('Energy')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75, linestyle=':')
plt.savefig("histogram.png", dpi=300, bbox_inches='tight')
