# Suzzany 🦆🐓

###
<br>

Suzzany é um sistema inteligente para monitoramento de galinheiros, utilizando **Visão Computacional** e **Redes Neurais** para detectar codornas, identificar a postura de ovos e alertar sobre intrusos no local.
O projeto foi inicialmente desenvolvido para reconhecer codornas em tempo real com base em um modelo YOLOv3 customizado e está em contínuo desenvolvimento.

A ideia deste projeto surgiu após a perda de algumas codornas devido à presença de intrusos no galinheiro, o que tornou necessária uma solução para evitar maiores prejuízos.
<br><br>

## Funcionalidades

<p>A detecção e reconhecimento inicial das codornas está em fase de treinamento, com melhorias futuras planejadas para integrar as demais funcionalidades:</p>

- 🎥 **Monitoramento em Tempo Real**: Detecta codornas e postura de ovos no galinheiro usando visão computacional.
- 🐀 **Detecção de Intrusos**: Detectar a presença de outros animais, como ratos, no galinheiro (em desenvolvimento).
- 🔔 **Alertas Automáticos**: Receber alertas automáticos quando ovos forem detectados ou quando um intruso aparecer (em desenvolvimento).
<br>

## Pré-requisitos

Para rodar o projeto localmente, você precisará das dependencias listadas no `requirements.txt`:

- **Python 3.10+**
- **OpenCV**: Para manipulação e processamento de vídeo e imagem.
- **NumPy**: Biblioteca essencial para operações numéricas em Python.
- **Python-dotenv**: Para carregar variáveis de ambiente do arquivo `.env`.
- **Scikit-learn**: Ferramenta de machine learning e manipulação de dados.
- **Darknet**: Framework open-source para redes neurais, usado para treinar e executar o YOLO.
<br>

## Instalação

Clonando o repositório:

```bash
$ git clone git@github.com:rafittu/quail-detector.git
$ cd quail-detector
```

Crie um ambiente virtual e ative-o:

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
```

Instale as dependências:

```bash
$ pip install -r requirements.txt
```

<br>

## Iniciando o app

Os arquivos de **datasets de treinamento** e **pesos pré-treinados** são necessários para rodar a detecção no projeto, mas **não estão incluídos diretamente neste repositório** devido ao tamanho e restrições de armazenamento.
Para obter os arquivos necessários, entre em contato diretamente comigo <a href="https://www.linkedin.com/in/rafittu/">aqui</a>.

De posse do dataset e dos pesos pré-treinados, inclua-os na seguinte pasta:
```
QUAIL-DETECTOR/
├── .venv/
├── src/
├── utils/
├── yolo/
│   ├── dataset/            #Arquivos do dataset aqui
│   │   ├── annotations/
│   │   ├── images/
│   │   └── labels
│   ├── weights/             #Arquivos de peso aqui
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

Crie um arquivo `.env` na raiz do projeto e preencha as informações de acordo com o arquivo `.env.example` disponível.

Para iniciar o monitoramento do galinheiro com a detecção de codornas, execute o arquivo `main.py`:

```bash
$ python3 src/main.py
```
<br>

##

<p align="right">
  <a href="https://www.linkedin.com/in/rafittu/">Rafael Ribeiro 🚀</a>
</p>
