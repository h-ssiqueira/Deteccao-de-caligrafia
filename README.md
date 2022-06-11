# Detecção de Caligrafia
![GitHub Repository Size](https://img.shields.io/github/repo-size/h-ssiqueira/Deteccao-de-caligrafia?label=Repository%20Size&style=for-the-badge)

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![MAC](https://img.shields.io/badge/MAC-000000?style=for-the-badge&logo=macos&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

![Google Colab](https://img.shields.io/badge/Googlecolab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)

![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)

## Descrição

Detecção de letras utilizando CNN, baseado neste [dataset](https://www.kaggle.com/datasets/sachinpatel21/az-handwritten-alphabets-in-csv-format). Para mais informações, acesse a [apresentação do projeto](Detec%C3%A7%C3%A3o%20de%20Caligrafia.pdf).

## Arquivos

* [modificado.py](src/modificado.py) | [modificado.ipynb](src/modificado.ipynb) é referente ao treinamento do modelo.
* [loading_model.py](src/loading_model.py) | [loading_model.ipynb](src/Loading_model.ipynb) é referente à utlização do modelo para classificar uma imagem em formato PNG.

### Modelos:
* [padrao.h5](modelos/padrao.h5) é referente ao modelo original treinado com 200 imagens em cada época com 18 épocas (99,33% de acurácia)
* [modificado1.h5](modelos/modificado1.h5) é referente ao modelo modificado, utilizando 2000 imagens por época e um total de 30 épocas (99,24% de acurácia)
* [modificado2.h5](modelos/modificado2.h5) é referente ao modelo modificado, utilizando 1200 imagens por época e um total de 30 épocas (99,39% de acurácia)

## Executando
* Instalar as dependências necessárias do Python para cada arquivo.
* Extrair o [dataset](src/A_Z%20Handwritten%20Data.zip)
* Verificar se os caminhos nos arquivos correspondem ao nome:

    * [modificado.py](src/modificado.py) | [modificado.ipynb](src/modificado.ipynb):
        * [46](src/modificado.py#L46) - local onde se encontra o dataset para treino (segunda célula).
        * [170](src/modificado.py#L170) - local a ser salvo o modelo gerado (última célula).

    * [loading_model.py](src/loading_model.py) | [loading_model.ipynb](src/Loading_model.ipynb):
        * [37](src/loading_model.py#L37) - Imagem PNG a ser classificada (segunda célula), este deve ser modificado para classificar outras imagens.
        * [52](src/loading_model.py#L52) - CSV da imagem em PNG formatado para o modelo (quarta célula).
        * [85](src/loading_model.py#L85) - Modelo em si (quinta célula).
        * [96](src/loading_model.py#L96) - Dataset (sexta célula).
        * [109](src/loading_model.py#L109) - Entrada do arquivo csv gerado anteriormente (sétima célula).

* Para uma imagem PNG, utilizar o software Paint com uma resolução de 400 px x 400 px e a maior espessura possível do pincel para desenhar uma letra de fôrma maiúscula.
## Autores
* Ana Cláudia Akemi Matsuki de Faria
* Danielle Bezerra Moreira
* [Derek Freire Quaresma](https://github.com/derekfq)

* [Henrique Sartori Siqueira](https://github.com/h-ssiqueira)

* [Rafael Silva Barbon](https://github.com/RafaelBarbon)