#Imports
import pickle
import numpy as np
import os

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Configurações 
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_models = os.path.join(base_dir, 'models')
maxlen = 20

# Carregar Artefatos (Isso roda quando importa o arquivo)
try:
    model = load_model(os.path.join(path_models, 'chatbotIA.keras'))
    
    with open(os.path.join(path_models, 'tokenizer.pkl'), 'rb') as f:
        tokenizer = pickle.load(f)
        
    with open(os.path.join(path_models, 'label_encoder.pkl'), 'rb') as f:
        label_encoder = pickle.load(f)
    print("Sistema Carregado!")
except Exception as e:
    print(f"Erro ao carregar modelos: {e}")
    model = None

def resposta(mensagem):
    if model is None:
        return "Erro: O cérebro do bot não foi carregado."

    #Tokenizar 
    seq = tokenizer.texts_to_sequences([mensagem])
    
    if not seq or not seq[0]:
        return "Desculpe, não entendi. Tente usar outras palavras."

    #Padding
    padded = pad_sequences(seq, maxlen=maxlen, padding='post')

    #Prever
    predicao = model.predict(padded, verbose=0)
    index = np.argmax(predicao)
    confianca = predicao[0][index]
    
    # Traduzir
    resposta = label_encoder.inverse_transform([index])[0]

    #Filtro de Confiança
    if confianca < 0.65:
        return "INDECISO" # Retorno especial para facilitar o teste
    
    return resposta