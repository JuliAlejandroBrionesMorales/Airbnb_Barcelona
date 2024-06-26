# Importamos librerias necesarias
import streamlit as st
import pandas as pd
import pandas as pd
import folium
from folium.plugins import FastMarkerCluster
from streamlit_folium import folium_static
import streamlit.components.v1 as components


# Configuración de la página de trabajo
st.set_page_config(page_title='Proyecto 2: Barcelona', layout='wide', page_icon='🇪🇸')



# CONFIGURACIÓN DE LA PRESENTACIÓN
st.title('TOP200')
st.write('El objetivo de sección es mostraros la comparación de las mejores y peores viviendas en cuanto acupación (200 mejores y peores viviendas). Se mostrarán las principales diferencias que hemos encontrado entre las mismas, así como conclusiones que hemos obtenido de la comparación dde hipótesis.')
st.markdown('#### <span style="color:orange;">Creación Dataframes</span>', unsafe_allow_html=True)
st.write('Para la creación de los dataframes hemos analizado la correlación de las variables numéricas con respecto a "price" y "availability_365". Posteriormente hacemos una selección de las variables con más correlación para poder hacer el calculo del puntuaje ponderado. Este puntuaje ponderado indica el ranking de las propiedades en cuanto alquiler. Cuanto más alto sea este puntuaje ponderado, mejor posición tendrá la propieddad.')


st.markdown('#### <span style="color:orange;">Mapas por zonas de las mejores y peores viviendas</span>', unsafe_allow_html=True)
st.write('Los siguiente mapas muestran la distribución de las 200 mejores y peores viviendas en Barcelona de acuerdo a nuestro análisis. Se puede ver ligeras diferencias entre las zonas de población de los 2 dataframes.')

# Cargamos los dataframes de top200
top_200 = pd.read_csv(r'/Users/juliobrionesmorales/Documents/GitHub/Airbnb_Barcelona/data/1. top200/top_200.csv')
bottom_200 = pd.read_csv(r'/Users/juliobrionesmorales/Documents/GitHub/Airbnb_Barcelona/data/1. top200/bottom_200.csv')
col1, col2 = st.columns(2)
# En la primera columna, mostrar el mapa para el top_200
with col1:
    st.markdown("#### Top 200")
    map_top = folium.Map(location=[41.3851, 2.1734], zoom_start=11.5)
    locations_top = top_200[['latitude', 'longitude']].values.tolist()
    FastMarkerCluster(data=locations_top).add_to(map_top)
    folium_static(map_top)

# En la segunda columna, mostrar el mapa para el bottom_200
with col2:
    st.markdown("#### Bottom 200")
    map_bottom = folium.Map(location=[41.3851, 2.1734], zoom_start=11.5)
    locations_bottom = bottom_200[['latitude', 'longitude']].values.tolist()
    FastMarkerCluster(data=locations_bottom).add_to(map_bottom)
    folium_static(map_bottom)

# Graficas interesantes de acuerdo a nuestro analisis.
st.markdown('##### <span style="color:orange;">Gráficas comparativas y Contraste de Hipótesis</span>', unsafe_allow_html=True)
st.write('En esta primera gráfica se pretende mostrar las diferencias gráficas que hemos encontrado al comparar las 200 mejores y peores viviendas en nuestro análisis. También, se han llevado a cabo contraste de hipótesis comparando estas viviendas para poder conseguir consejos de mejora en el  alquiler.')  
st.markdown('#### GRAFICAS COMPARATIVAS')
# GRAFICA 1
st.markdown('**1. Número de Tipo de Propiedades**')
st.write('Estas gráficas muestran como las mejores y peores propiedades siguen una tendencia distinta en cuanto al alquiler de las tipo de propiedades.')
with open('HTML/9_comparacion_propiedades.html', 'r') as file:
    html_content = file.read()
components.html(html_content, height=500) 


# GRAFICA 2
st.markdown('**2. Número de Tipo de Habitaciones**')
st.write('En esta segunda gráfica confirma como las mejores propiedades siguen una tendencia de alquiler hacia casas enteras, mientrás que las peores tienen una tendencia hacia el alquiler habitaciones privadas.')
with open('HTML/10_comparacion_habitaciones.html', 'r') as file:
    html_content = file.read()
components.html(html_content, height=500) 

# GRAFICA 3
st.markdown('**3. Número Promedio de Noches Mínimas**')
st.write('En esta tercera gráfica podemos ver como las mejores propiedades tienen un número de noches promedio mucho más alto que las propiedades con peor valoración de acuerdo a nuestro analisis.')
with open('HTML/11_comparacion_noches_minimas.html', 'r') as file:
    html_content = file.read()
components.html(html_content, height=500) 

# GRAFICA 4
st.markdown('**4. Comparación de Puntuaje de Limpieza**')
st.write('En esta última gráfica, también se puede observar como las comparaciones de los puntuajes de limpieza por grupos vecinales es mucho mayor que las peores viviendas.')
with open('HTML/12_comparacion_limpieza.html', 'r') as file:
    html_content = file.read()
components.html(html_content, height=500) 

st.write('Es imporatante resaltar la gran diferencia que existe entre los tipos de propiedades alquiladas para los 200 mejores y 200 peores viviendas de acuerdo a nuestro análisis. Mientras la primera tiene una tendencia por el alquiler de viviendas o apartamentos entero, y la segunda tiene una tendencia por alquilar habitaciones por pocos días.')
st.write('Es importante resaltar la gran diferencia que existe entre el alquiler de los tipos de propiedades entre los 200 mejores y peores viviendas.')

st.markdown('#### CONTRASTE DE HIPOTESIS')
col1, col2 = st.columns(2)
with col1:
    with st.expander("CONTRASTE 1"):
        st.markdown('- **Hipotesis nula (Ho)**: el tipo de propiedad no tiene un impacto significativo en el precio de la vivienda.')
        st.markdown('- **Hipotesis alternativa (H1)**: el tipo de propiedad tiene un impacto significativo en el precio de la vivienda.')
        st.markdown('<p style="color:green; text-align:center; font-style:italic">Tras analizar los datos(top_200 y bottom_200) se rechaza la hipótesis nula (H0) en ambos casos.</p>', unsafe_allow_html=True)
with col2:
    with st.expander("CONTRASTE 2"):
        st.markdown('- **Hipotesis nula (Ho)**: no hay diferencia significativa en la aceptación del alquiler entre propiedades con diferentes capacidades de acomodación.')
        st.markdown('- **Hipotesis alternativa (H1)**: existen una diferencia significativa en la aceptación del alquiler entre propiedades con diferentes capacidades de acomodación.')
        st.markdown('<p style="color:green; text-align:center; font-style:italic">Tras analizar los datos (top_200 y bottom_200) se rechaza la hipótesis nula (H0) en ambos casos. Es por ello que, se recomienda máximizar la acomodación en la medida de lo posible.</p>', unsafe_allow_html=True)
st.write('')
col1, col2 = st.columns(2)
with col1:
    with st.expander("CONTRASTE 3"):
        st.markdown('- **Hipotesis nula (Ho)**: no hay diferencia significativa en la aceptación del alquiler y el número mínimo de noches.')
        st.markdown('- **Hipotesis alternativa (H1)**: existe una diferencia significativa en la aceptación del alquiler y el número mínimo de noches.')
        st.markdown('<p style="color:green; text-align:center; font-style:italic">Tras analizar los datos (top_200 y bottom_200) se rechaza la hipótesis nula (H0) en ambos casos. Es por ello que, se recomienda fijar bien el número de noches mínimas en función de su tipo de propiedad, ya que este factor es crucial a la hora de alquier su propiedad.</p>', unsafe_allow_html=True)
with col2:
    with st.expander("CONTRASTE 4"):
        st.markdown('- **Hipotesis nula (Ho)**: no existe una correlación entre el número de camas y el availability_365.')
        st.markdown('- **Hipotesis alternativa (H1)**: existe una correlación entre el número de camas y el availability_365.')
        st.markdown('<p style="color:green; text-align:center; font-style:italic">Tras analizar los datos, en el top_200 vivienda se rechaza la hipótesis nula (H0), mientras que en bottom_200 viviendas se acepta la hipótesis nula (H0). Esto es un dato a tener en cuenta para poder identificar que tipo de propiedadad disponemos y como podemos actuar.</p>', unsafe_allow_html=True)
st.write('')
col1, col2 = st.columns(2)
with col1:
    with st.expander("CONTRASTE 5"):
        st.markdown('- **Hipotesis nula (Ho)**: no existe una diferencia significativa entre la aceptación del alquiler de acuerdo al precio.')
        st.markdown('- **Hipotesis alternativa (H1)**: existe una diferencia significativa entre la aceptación del alquiler de acuerdo al precio.')
        st.markdown('<p style="color:green; text-align:center; font-style:italic">Tras analizar los datos (top_200 y bottom_200) se rechaza la hipotesis nula (H0) en ambos casos.</p>', unsafe_allow_html=True)
with col2:
    with st.expander("CONTRASTE 6"):
        st.markdown('- **Hipotesis nula (Ho)**: no existe una correlación entre la ocupación y las reseñas de limpieza.')
        st.markdown('- **Hipotesis alternativa (H1)**: existe una correlación entre la ocupación y las reseñas de limpieza.')
        st.markdown('<p style="color:green; text-align:center; font-style:italic">Tras analizar los datos, en el top_200 vivienda se acepta la hipótesis nula (H0) y en el bottom_200 viviendas se rechaza la hipótesis nula (H0). Por lo tanto, en caso de alquilar habitaciones, se recomienda tenerlas lo más limpia posible.</p>', unsafe_allow_html=True)
st.write('')
col1, col2 = st.columns(2)
with col1:
    with st.expander("CONTRASTE 7"):
        st.markdown('- **Hipotesis nula (Ho)**: no existe una correlación entre la ocupación y las reseñas de comunicación.')
        st.markdown('- **Hipotesis alternativa (H1)**: existe una correlación entre la ocupación y las reseñas de comunicación.')
        st.markdown('<p style="color:green; text-align:center; font-style:italic">Tras analizar los datos (top_200 y bottom_200) se rechaza la hipotesis nula (H0) en ambos casos. Se recomienda establecer la comunicación más fluida posible con los posibles candidatos a alquilar su propiedad.</p>', unsafe_allow_html=True)
with col2:
    with st.expander("CONTRASTE 8"):
        st.markdown('- **Hipotesis nula (Ho)**: no existe una diferencia significativa entre la aceptación del alquiler de acuerdo al precio.')
        st.markdown('- **Hipotesis alternativa (H1)**: existe una diferencia significativa entre la aceptación del alquiler de acuerdo al precio.')
        st.markdown('<p style="color:green; text-align:center; font-style:italic">Tras analizar los datos (top_200 y bottom_200) rechazamos la hipotesis nula (H0) en ambos casos. Es importante fijar bien el precio de acuerdo a la propiedad que se tenga.</p>', unsafe_allow_html=True)

st.write('Tras la realizar los contrastes de hipótesis y analizar los datos, consideramos que es fundamental establecer un precio competitivo y semejante a la propiedad ofrecida. Por ello, en la siguiente página se ha creado una calculadora de precio para poder solucionar este problema.')
