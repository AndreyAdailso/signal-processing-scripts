# 2025-PDS

Este diretório é dedicado à análise do dataset TIMIT. O TIMIT foi desenvolvido para suportar pesquisas em reconhecimento automático de fala e conhecimento acústico-fonético.

## Sobre o TIMIT

O TIMIT é um conjunto de dados amplamente utilizado em estudos de processamento de sinais de fala, aprendizado de máquina e linguística. Ele contém gravações de fala anotadas com transcrições fonéticas e ortográficas, sendo uma ferramenta essencial para o avanço em tecnologias de reconhecimento de fala.
## Processamento em Lote de Arquivos: simple_batch_processing.py

O script `simple_batch_processing.py` realiza o processamento em lote de arquivos de áudio de forma eficiente. Ele executa as seguintes etapas:

1. **Busca Recursiva de Arquivos**: Pesquisa recursivamente todos os arquivos com uma extensão específica dentro de uma pasta e armazena os caminhos em uma lista.
2. **Processamento de Arquivos**:
    - Lê o conteúdo de cada arquivo (forma de onda do sinal).
    - Divide o sinal em segmentos (janelas) de N=100 amostras e processa cada segmento:
      - Calcula a energia \( e_i \) do i-ésimo segmento e armazena em um array.
      - Exibe no terminal a energia de cada segmento.
    - Plota a forma de onda do sinal e a energia segmentada (curva de energia por segmento) em dois gráficos organizados com `subplot(211)`.

Este script é útil para análise de sinais de fala e extração de características acústicas.

## Parte II – Cálculo de Histogramas de Amplitudes e Durações: display_histograms.py

O script `display_histograms.py` realiza o cálculo de histogramas de amplitudes e durações para arquivos de áudio. Ele executa as seguintes etapas:

1. **Identificação do Intervalo de Amostragem**:
    - Determina o intervalo de amostragem \( T_s \) (em segundos) de cada arquivo de áudio.
    - Calcula a duração total da forma de onda com base no intervalo de amostragem e no número de amostras.

2. **Cálculo de Estatísticas**:
    - Para cada arquivo, calcula:
        - **Duração**: mínima, máxima e média.
        - **Amplitude**: mínima, máxima e média.

3. **Geração de Histogramas**:
    - Em um laço, calcula e exibe o histograma da amplitude de cada forma de onda.
    - Os histogramas fornecem uma visão detalhada da distribuição das amplitudes nos arquivos processados.

Este script é útil para análise estatística de sinais de fala e visualização de características acústicas.