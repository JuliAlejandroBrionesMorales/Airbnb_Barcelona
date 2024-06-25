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
    st.image('img/15_outliers_price.png')
with col2:
    st.image('img/16_outliers_minimumnights.png')
    
st.markdown('##### <span style="color:orange;">Función genérica utilizada para arreglar outliers</span>', unsafe_allow_html=True)
st.write('El objetivo principal de esta función es arreglar los valores atípicos o outliers. Identificamos los valores a atípicos como aquellos que son mayores que los bigotes (máximos y mínimos) del diagrama de caja y bigotes. Para ello, este función sustituye, estos valores atípicos por los valores de máximo o mínimo del diagrama de caja y bigotes.')
st.image('img/3_funcion_outliers.png',width=1000)

st.write('')

st.markdown('##### <span style="color:orange;">Esta sección volvemos a analizar los valores atípicos</span>', unsafe_allow_html=True)
st.write('Para comprobar que la función utilizada en el apartado anterior ha sido útil con respecto a la modificación u ajuste de los valores atípicos, vamos a volver a mostrar las gráficas de caja y bigotes pero con los datos arreglados.')
col1, col2 = st.columns(2)
with col1:
    st.image('img/17_sin_outliers_price.png')
with col2:
    st.image('img/18_sin_outliers_minnights.png')



