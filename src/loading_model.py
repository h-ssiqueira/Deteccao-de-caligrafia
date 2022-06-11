# -*- coding: utf-8 -*-
"""Loading_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19uxyJwCkC4SKA-C5puz4jTff1_DZxCGx

# Equipe:
# Ana Cláudia Akemi Matsuki de Faria
# Danielle Bezerra Moreira
# Derek Freire Quaresma
# Henrique Sartori Siqueira
# Rafael Silva Barbon

** Configurar a janela do paint 400px x 400px e o tamanho do pincel para maior espessura **

# Transformando uma IMG em CSV

Transformar a imagem para 28x28 px
Inverter a cor da imagem
Transformar em escala de cinza
Salvar em um arquivo formatado com cabeçalho e pixels separados por ','
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from keras.models import load_model
from PIL import Image, ImageOps
from sklearn.preprocessing import MinMaxScaler



"""Redimensiona (28x28) e inverte as cores da imagem e salvando-a em tons de cinza"""

img = Image.open('../letras/A.png')

img = img.resize((28, 28), Image.ANTIALIAS)
img = ImageOps.invert(img.convert("L"))

"""Transforma a matriz representando a imagem em um vetor com 784 posições"""

data = np.squeeze(np.asarray(img)).flatten()
#print(data.flatten())
print(data)
print(type(data))
print(data.shape)

"""Transforma o vetor em um arquivo csv com o cabeçalho e os dados necessários para se adequar a entrada do modelo"""

f = open("entrada.csv","w")
i = 0
while(i != data.size):
    string = "0."
    if i == data.size-1:
        string = string + str(i+1)
    else:
        string = string + str(i+1) + ','
    f.write(string)
    i = i+1
f.write('\n')
i = 0
while(i != data.size):
    if i == data.size-1:
        string = data[i].astype(str)
    else:
        string = data[i].astype(str) + ','
    f.write(string)
    i = i+1
f.close()

"""# Utilizando o modelo

https://machinelearningmastery.com/save-load-keras-deep-learning-models/#:~:text=How%20to%20Load%20a%20Keras%20Model.%20Your%20saved,the%20model%20with%20the%20same%20architecture%20and%20weights.
https://towardsdatascience.com/multi-output-model-with-tensorflow-keras-functional-api-875dd89aa7c6

Carregando o modelo e sua descrição
"""

# PADRÃO
#model = load_model('../modelos/padrao.h5')

# MODIFICADO1
model = load_model('../modelos/modificado1.h5')

# MODIFICADO2
#model = load_model('../modelos/modificado2.h5')

model.summary()

"""# Tratando dados para fazer previsão """

#https://machinelearningmastery.com/standardscaler-and-minmaxscaler-transforms-in-python/

train = pd.read_csv("A_Z Handwritten Data.csv").astype('float32')

train.rename(columns={'0':'label'}, inplace=True)
train = train.drop('label',axis = 1)
standard_scaler = MinMaxScaler()
standard_scaler.fit(train)

"""# Carregar imagem (em csv) que será classificada e tratá-la

Transformar a imagem em csv para user no modelo
https://newbedev.com/converting-images-to-csv-file-in-python
"""

predict = pd.read_csv("entrada.csv").astype('float32')
predict.head()

to_predict = standard_scaler.transform(predict)

plt.figure(figsize = (12,10))
row, colums = 4, 4
for i in range(1):
    plt.subplot(colums, row, i+1)
    plt.imshow(to_predict.reshape(28,28),interpolation='nearest', cmap='Greys')
plt.show()

"""Modelo prevê qual letra corresponde e exibe as probabilidades das letras"""

#https://github.com/christianversloot/machine-learning-articles/blob/main/how-to-predict-new-samples-with-your-keras-model.md
to_predict= to_predict.reshape(to_predict.shape[0], 28, 28, 1).astype('float32')
predictions = model.predict(to_predict)
print(predictions)

"""Trata a previsão e exibe o resultado"""

# Generate arg maxes for predictions
classes = np.argmax(predictions, axis = 1)
print(classes)
alphabets_mapper = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z'}
classes = pd.DataFrame(classes)
Letter=classes[0].map(alphabets_mapper)
print("Letra prevista: ", Letter[0])