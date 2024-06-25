# Importamos librerias necesarias
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


st.set_page_config(page_title='Proyecto 2: Barcelona', layout='wide', page_icon='🇪🇸')

# ----------- CARAGAMOS DATAFRAMES --------------------
# Para poder abrir los archivos con la url
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Funciones para cargar los DataFrames y almacenarlos en caché
@st.cache_data
def load_df_calendar():
    return pd.read_csv(r'https://data.insideairbnb.com/spain/catalonia/barcelona/2024-03-20/data/calendar.csv.gz')

@st.cache_data
def load_df_listings():
    return pd.read_csv('https://data.insideairbnb.com/spain/catalonia/barcelona/2024-03-20/data/listings.csv.gz')

@st.cache_data
def load_df_reviews():
    return pd.read_csv (r'https://data.insideairbnb.com/spain/catalonia/barcelona/2024-03-20/data/reviews.csv.gz')


# Cargar los DataFrames usando las funciones cacheadas
df_calendar = load_df_calendar()
df_listings = load_df_listings()
df_reviews = load_df_reviews()



st.title('VALORES NULOS')
st.markdown('##### <span style="color:orange;">Esta sección muestra de manera sencilla los pasos a seguidos para reparar los valores nulos:</span>', unsafe_allow_html=True)
    
col1, col2= st.columns(2)
with col1:
     # Valores nulos Calendar
    with st.expander("DF_CALENDAR"):
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(df_calendar.isnull(), cbar=False, cmap='viridis', ax=ax)
        # Configura las etiquetas y tamaño de la fuente
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        st.pyplot(fig)
        st.write('Reparamos los valores nulos de dataframe calendar, eliminando la columna **ajusted_price** debido a que tiene un gran porcentaje de valores nulos.')
with col2:
    st.write('')

st.write('')     
col1, col2= st.columns(2)
with col1:
    with st.expander("DF_REVIEWS"):
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(df_reviews.isnull(), cbar=False, cmap='viridis', ax=ax)
        # Configura las etiquetas y tamaño de la fuente
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        st.pyplot(fig)
        st.write('Reparamos los valores nulos del dataframe reviews, eliminando las filas con valores nulos (solo en columna comments).')
with col2:   
    st.write('')

st.write('')   
col1, col2 = st.columns(2)
with col1:
    with st.expander("DF_LISTINGS"):
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(df_listings.isnull(), cbar=False, cmap='viridis', ax=ax)
        # Configura las etiquetas y tamaño de la fuente
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        st.pyplot(fig)
        st.markdown('##### Reparacion valores nulos')
        st.markdown('1. Utilizamos función genérica para codificar variables categóricas mediante label encode.')
        st.markdown('2. Aplicamos función genérica para encontrar el mejor valor de k.')
        st.markdown('3. Aplicamos una función genérica que imputa los valores faltantes en nuestro dataframe tilizando el algoritmo K-Nearest Neighbors (KNN).')
