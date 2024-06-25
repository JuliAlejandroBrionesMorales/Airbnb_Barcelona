# Importamos librerias necesarias
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


st.set_page_config(page_title='Proyecto 2: Barcelona', layout='wide', page_icon='🇪🇸')



st.title('VALORES NULOS')
st.markdown('##### <span style="color:orange;">Esta sección muestra de manera sencilla los pasos a seguidos para reparar los valores nulos:</span>', unsafe_allow_html=True)
    
col1, col2= st.columns(2)
with col1:
     # Valores nulos Calendar
    with st.expander("DF_CALENDAR"):
        st.image('/img/12_nulos_calendar.png')
        st.write('Reparamos los valores nulos de dataframe calendar, eliminando la columna **ajusted_price** debido a que tiene un gran porcentaje de valores nulos.')
with col2:
    st.write('')

st.write('')     
col1, col2= st.columns(2)
with col1:
    with st.expander("DF_REVIEWS"):
        st.image('img/13_nulos_reviews.png')
        st.write('Reparamos los valores nulos del dataframe reviews, eliminando las filas con valores nulos (solo en columna comments).')
with col2:   
    st.write('')

st.write('')   
col1, col2 = st.columns(2)
with col1:
    with st.expander("DF_LISTINGS"):
        st.image('img/14_nulos_listings.png')
        st.markdown('##### Reparacion valores nulos')
        st.markdown('1. Utilizamos función genérica para codificar variables categóricas mediante label encode.')
        st.markdown('2. Aplicamos función genérica para encontrar el mejor valor de k.')
        st.markdown('3. Aplicamos una función genérica que imputa los valores faltantes en nuestro dataframe tilizando el algoritmo K-Nearest Neighbors (KNN).')
