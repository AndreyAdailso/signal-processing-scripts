import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from simple_batch_processing import buscar_arquivos

def display_histograms(caminho_arquivo):
    print(f"Processando arquivo: {caminho_arquivo}")

    taxa_amostragem, sinal = wavfile.read(caminho_arquivo)

    if len(sinal.shape) > 1:
        sinal = sinal[:, 0]

    sinal = sinal.astype(float)

    Ts = 1.0 / taxa_amostragem

    duracao = len(sinal) * Ts

    amp_min = np.min(sinal)
    amp_max = np.max(sinal)
    amp_media = np.mean(sinal)

    print(f"Taxa de amostragem: {taxa_amostragem} Hz")
    print(f"Intervalo de amostragem: {Ts} s")
    print(f"Duração do sinal: {duracao} s")
    print(f"Amplitude: mínima: {amp_min}, máxima: {amp_max}, média: {amp_media}")

    
    plt.figure(figsize=(8, 4))
    plt.hist(sinal, bins=100, color='gray', edgecolor='black')
    plt.title("Histograma da Amplitude")
    plt.xlabel("Amplitude")
    plt.ylabel("Frequência")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    caminhos = buscar_arquivos("./timit", extensao=".wav")
    for caminho in caminhos[:5]:
        display_histograms(caminho)
        print("\n")