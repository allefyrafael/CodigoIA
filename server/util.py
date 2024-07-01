import pickle
import json
import numpy as np
import joblib

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    global __model
    if __model is None:
        load_saved_artifacts()  # Certifique-se de que o modelo esteja carregado

    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def load_saved_artifacts():
    global __data_columns, __locations, __model
    print("Loading saved artifacts...")

    # Carregar colunas de dados
    with open("artifacts/columns.json", "r", encoding='utf-8') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # primeiras 3 colunas são sqft, bath, bhk

    # Carregar modelo usando joblib
    if __model is None:
        try:
            __model = joblib.load('artifacts/banglore_home_prices_model.joblib')
        except FileNotFoundError:
            print("Arquivo do modelo não encontrado. Certifique-se de que o modelo tenha sido criado corretamente.")
            return None
        except Exception as e:
            print("Erro ao carregar o modelo:", str(e))
            return None

    print("Loading saved artifacts...done")
    return __model

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '_main_':
    load_saved_artifacts()
    if __model:
        print("Modelo carregado com sucesso.")
        print(get_location_names())
        print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
        print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
        print(get_estimated_price('Kalhalli', 1000, 2, 2))  # outra localização
        print(get_estimated_price('Ejipura', 1000, 2, 2))   # outra localização
    else:
        print("Falha ao carregar o modelo. Verifique os logs para mais detalhes.")