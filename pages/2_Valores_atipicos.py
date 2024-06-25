# Importamos librerias necesarias
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import feather

# Configuración de página
st.set_page_config(page_title='Proyecto 2: Barcelona', layout='wide', page_icon='🇪🇸')





# Mostramos los apartados que queremos en nuestra presentación
st.title('VALORES ATIPICOS')
st.markdown('##### <span style="color:orange;">En esta sección analizamos los valores atípicos.</span>', unsafe_allow_html=True)
st.write('Para ser más específicos con nuestra explicación, a continuación, mostraremos 2 graficos en los que se puede de manera objetiva la diferencia entre los valores atípicos y la gran cantidad de datos.')
col1, col2 = st.columns(2)
with col1:
    # Leemos dataframe sin valores nulos
    df_listings1 = pd.read_feather(r'/Users/juliobrionesmorales/Documents/GitHub/Airbnb_Barcelona/data/2. data_sin_nulos/df_listings.feather')
    fig = px.box(df_listings1, y='price', template='plotly', title='Diagrama de caja y bigotes de price')
    st.plotly_chart(fig)
with col2:
    fig = px.box(df_listings1, y='maximum_nights', template='plotly', title='Diagrama de caja y bigotes de maximum_nights')
    st.plotly_chart(fig)
    
st.markdown('##### <span style="color:orange;">Función genérica utilizada para arreglar outliers</span>', unsafe_allow_html=True)
st.write('El objetivo principal de esta función es arreglar los valores atípicos o outliers. Identificamos los valores a atípicos como aquellos que son mayores que los bigotes (máximos y mínimos) del diagrama de caja y bigotes. Para ello, este función sustituye, estos valores atípicos por los valores de máximo o mínimo del diagrama de caja y bigotes.')
st.image('/Users/juliobrionesmorales/Documents/1. FORMACION/3. DATA ANALYTICS /PROYECTOS_BOOTCAMP/PROYECTO FINAL 2/img/3_funcion_outliers.png',width=1000)

st.write('')

st.markdown('##### <span style="color:orange;">Esta sección volvemos a analizar los valores atípicos</span>', unsafe_allow_html=True)
st.write('Para comprobar que la función utilizada en el apartado anterior ha sido útil con respecto a la modificación u ajuste de los valores atípicos, vamos a volver a mostrar las gráficas de caja y bigotes pero con los datos arreglados.')
col1, col2 = st.columns(2)
with col1:
    # Leemos dataframe sin valores nulos
    df_listings2 = pd.read_feather(r'/Users/juliobrionesmorales/Documents/GitHub/Airbnb_Barcelona/data/3. data_sin_outliers/df_listings.feather')
    fig = px.box(df_listings2, y='price', template='plotly', title='Diagrama de caja y bigotes de price')
    st.plotly_chart(fig)
with col2:
    fig = px.box(df_listings2, y='maximum_nights', template='plotly', title='Diagrama de caja y bigotes de maximum_nights')
    st.plotly_chart(fig)



