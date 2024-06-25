import streamlit as st
import pandas as pd
import pickle
from pycaret.regression import load_model, predict_model

# Establecemos configuración de página
st.set_page_config(page_title='Proyecto 2: Barcelona', layout='wide', page_icon='🇪🇸')

# Cargamos el modelo predictor de precio
model_path = r'/Users/juliobrionesmorales/Documents/GitHub/Airbnb_Barcelona/airbnb_barcelona_predictor'
model = load_model(model_path)

st.title('PREDICTOR DE PRECIO AIRBNB')

col1, col2 = st.columns (2)
with col2:
    st.write('')
with col1:
    # Campos de entrada (al modelo tenemos que pasarle exactamente las mismas variables con las que fue entrenado)
    neighbourhood = st.selectbox('neighbourhood_cleansed', ['la Barceloneta', "la Dreta de l'Eixample", 'la Sagrada Família',
        "el Camp d'en Grassot i Gràcia Nova", 'el Raval',
        'el Besòs i el Maresme', 'Sant Antoni', 'el Barri Gòtic', 'Sants',
        'el Poblenou', "la Nova Esquerra de l'Eixample",
        'la Vila Olímpica del Poblenou',
        'Sant Pere, Santa Caterina i la Ribera', 'Pedralbes',
        'el Guinardó', "l'Antiga Esquerra de l'Eixample",
        "el Camp de l'Arpa del Clot", 'el Coll', 'el Clot',
        'Vallcarca i els Penitents',
        'Diagonal Mar i el Front Marítim del Poblenou',
        'la Vila de Gràcia', 'el Poble Sec', 'el Fort Pienc',
        'Sant Gervasi - Galvany', 'Navas', 'Sant Martí de Provençals',
        'el Putxet i el Farró', 'la Bordeta', 'Sarrià',
        'el Parc i la Llacuna del Poblenou', 'Sants - Badal',
        'la Font de la Guatlla', 'la Maternitat i Sant Ramon',
        'el Baix Guinardó', 'la Prosperitat', 'el Turó de la Peira',
        'el Congrés i els Indians', 'Provençals del Poblenou',
        "la Font d'en Fargues", 'les Corts', 'Hostafrancs', 'el Carmel',
        'la Salut', 'Sant Gervasi - la Bonanova', 'les Tres Torres',
        'Vallvidrera, el Tibidabo i les Planes', 'la Teixonera',
        'la Marina del Prat Vermell', 'Can Baró', 'Porta',
        'la Verneda i la Pau', 'Vilapicina i la Torre Llobeta',
        'la Marina de Port', 'la Sagrera', 'Sant Andreu', 'el Bon Pastor',
        'Verdun', 'la Guineueta', 'Horta', 'Sant Genís dels Agudells',
        "la Vall d'Hebron", 'les Roquetes', 'la Trinitat Vella',
        'la Trinitat Nova', 'Torre Baró', 'Montbau', 'la Clota',
        'Can Peguera'])

    room_type = st.selectbox('room_type', ['Private room', 'Entire home/apt', 'Hotel room', 'Shared room'])
    minimum_nights = st.number_input('minimum_nights', min_value=1, max_value=100)
    bedrooms = st.number_input('bedrooms', min_value=1, max_value=10)
    beds = st.number_input('beds', min_value=1, max_value=10)
    bathrooms = st.number_input('bathrooms', min_value=1, max_value=10)

# df_pread_new = df[['neighbourhood_cleansed','room_type','minimum_nights','bedrooms','beds','bathrooms', 'price']]

# Crear un DataFrame con los inputs
input_data = pd.DataFrame({
    'neighbourhood_cleansed': [neighbourhood],
    'room_type': [room_type],
    'minimum_nights': [minimum_nights],
    'bedrooms': [bedrooms],
    'beds': [beds],
    'bathrooms': [bathrooms]
})


# Hacer la predicción
if st.button('Predict Price'):
    prediction = predict_model(model, data=input_data)
    st.write('The predicted price is ', prediction['prediction_label'][0].round(2), '€')