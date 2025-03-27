import glob
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

def buscar_arquivos(diretorio_raiz, extensao=".wav"):
    """
    Busca recursivamente arquivos com a extensão especificada a partir do diretório raiz.
    
    Parâmetros:
    - diretorio_raiz (str): Caminho para o diretório inicial da busca.
    - extensao (str): Extensão dos arquivos a buscar (ex: ".wav", ".phn", etc).

    Retorno:
    - lista_arquivos (list): Lista com os caminhos completos dos arquivos encontrados.
    """
    padrao_busca = os.path.join(diretorio_raiz, '**', f'*{extensao}')
    lista_arquivos = glob.glob(padrao_busca, recursive=True)
    return lista_arquivos

def processing_batch(caminho_arquivo, N=100):
    print(f"Processando arquivo: {caminho_arquivo}")

    taxa_amostragem, sinal = wavfile.read(caminho_arquivo)

    # Garante que o sinal é mono (canal único)
    if len(sinal.shape) > 1:
        sinal = sinal[:, 0] # considera apenas o primeiro canal

    num_segmentos = len(sinal) // N
    energias = []

    for i in range(num_segmentos):
        inicio = i * N
        fim = inicio + N 
        segmento = sinal[inicio:fim]

        energia = np.sum(segmento.astype(float) ** 2)
        energias.append(energia)
        #print(f"Segmento {i}: Energia = {energia:}")

    # Plotar formar de onde e curva de energia
    plt.figure(figsize=(10, 6))

    #subplot 1: forma de onda
    plt.subplot(211)
    tempo = np.arange(len(sinal)) / taxa_amostragem
    plt.plot(tempo, sinal)
    plt.xlabel("Tempo [s]")
    plt.ylabel("Amplitude")

    #subplot 2: curva de energia
    plt.subplot(212)
    plt.plot(energias, marker='o')
    plt.title('Energia por Segmento (janelas de 100 amostras)')
    plt.xlabel('Segmento')
    plt.ylabel('Energia')

    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    diretorio_timit = "./timit"  # caminho do dataset 
    arquivos_wav = buscar_arquivos(diretorio_timit, extensao=".wav")

    print(f"Total de arquivos encontrados: {len(arquivos_wav)}")
    print("Primeiros 5 arquivos:")
    for caminho in arquivos_wav[:5]:
        print(caminho)
        processing_batch(caminho)
