import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from simple_batch_processing import buscar_arquivos
import os

def display_histograms(caminho_arquivo, caminho_base, output_base):
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

    # Criação do caminho relativo para manter a estrutura
    caminho_relativo = os.path.relpath(caminho_arquivo, caminho_base)
    caminho_saida = os.path.join(output_base, os.path.dirname(caminho_relativo))

    # Cria os diretórios necessários se não existirem
    os.makedirs(caminho_saida, exist_ok=True)

    # Nome do arquivo de saída
    nome_base = os.path.splitext(os.path.basename(caminho_arquivo))[0]
    caminho_histograma = os.path.join(caminho_saida, f"{nome_base}_histograma.png")

    # Plot e salva o histograma
    plt.figure(figsize=(8, 4))
    plt.hist(sinal, bins=100, color='gray', edgecolor='black')
    plt.title("Histograma da Amplitude")
    plt.xlabel("Amplitude")
    plt.ylabel("Frequência")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(caminho_histograma)
    plt.close()

if __name__ == "__main__":
    base_timit = "./timit"
    output_dir = "./output"

    caminhos = buscar_arquivos(base_timit, extensao=".wav")

    for caminho in caminhos[:]:
        display_histograms(caminho, caminho_base=base_timit, output_base=output_dir)
        print("\n")