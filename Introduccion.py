# --------------------LIBRERÍAS----------------------------#
# Solo importamos las necesarias para poder trabajar con la página de inicio
import streamlit as st
import pandas as pd
import feather 





# Configurar la página de Streamlit
st.set_page_config(page_title='Proyecto 2: Barcelona', layout='wide', page_icon='🇪🇸')




# -------------------- CONFIGURACION MULTIPAGINA ------------#
st.title('AIRBNB -BARCELONA')
col1, col2 = st.columns(2)
with col1:
    st.image('img/1_barcelona.jpeg', use_column_width=True)
with col2:
    st.write('')
    st.write('')
    st.write('Este proyecto se centra en el análisis de datos de usuarios que utilizaron Airbnb en Barcelona, basándose en datos extraídos de Inside Airbnb (https://insideairbnb.com/). El objetivo principal es explorar descubrimientos a través del análisis de datos mediante diversas técnicas analíticas. El proceso incluyó la limpieza exhaustiva de los datos para garantizar su calidad y coherencia, seguido de un análisis descriptivo detallado para comprender las características clave de las viviendas y los usuarios.')
    st.write('')
    st.write('Además, se llevó a cabo una comparación entre las 200 mejores y peores viviendas según varios criterios, con el fin de identificar los factores determinantes de su desempeño. Se aplicó un análisis de sentimiento a las reseñas de los usuarios para profundizar en la experiencia del cliente y se desarrolló una calculadora de precios para ayudar a los propietarios a establecer tarifas competitivas.')
    st.write('')
    st.write('Este proyecto no solo proporciona valiosas percepciones sobre el mercado de alquileres a corto plazo en Barcelona, sino que también demuestra cómo el análisis de datos puede facilitar decisiones estratégicas informadas en el sector de la hospitalidad y el turismo.')
   



# -------------------- CARGAMOS BBDD ------------#
# Para poder abrir los archivos con la url
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

@st.cache_data
def load_df_calendar():
    return pd.read_csv(r'https://data.insideairbnb.com/spain/catalonia/barcelona/2024-03-20/data/calendar.csv.gz')

@st.cache_data
def load_df_listings():
    return pd.read_csv('https://data.insideairbnb.com/spain/catalonia/barcelona/2024-03-20/data/listings.csv.gz')

@st.cache_data
def load_df_reviews():
    return pd.read_csv (r'https://data.insideairbnb.com/spain/catalonia/barcelona/2024-03-20/data/reviews.csv.gz')

# Cargar los DataFrames usando las funciones cacheadas para hacer menos pesadas cargar los dataframes
df_calendar = load_df_calendar()
df_listings = load_df_listings()
df_reviews = load_df_reviews()





# -------------------- MOSTRAMOS DATAFRAME ------------#
st.title('BASE DE DATOS')
st.write('Los siguiente botones muestran los dataframes utilizados para el análisis de este proyecto.')
# Inyectar CSS con st.markdown
st.markdown(""" <style>div.stButton > button:first-child {background-color: #6699FF;color: white;}</style>""",unsafe_allow_html=True,)
# Crear botones y contenedor para mostrar los dataframes
col1, col2, col3 = st.columns(3)
with col1:
    show_calendar = st.button("DF_CALENDAR")
with col2:
    show_listings = st.button("DF_LISTINGS")
with col3:
    show_reviews = st.button("DF_REVIEWS")

# Variable para almacenar el DataFrame a mostrar
display_df = "DF_CALENDAR"  # Valor por defecto

# Actualizar el DataFrame a mostrar según el botón presionado
if show_calendar:
    display_df = "DF_CALENDAR"
elif show_listings:
    display_df = "DF_LISTINGS"
elif show_reviews:
    display_df = "DF_REVIEWS"

# Usar un contenedor para mostrar el dataframe seleccionado en todo el ancho
with st.container():
    if display_df == "DF_CALENDAR":
        st.dataframe(df_calendar.head(100))
        st.write(df_calendar.shape)
    elif display_df == "DF_LISTINGS":
        st.dataframe(df_listings.head(100))
        st.write(df_listings.shape)
    elif display_df == "DF_REVIEWS":
        st.dataframe(df_reviews.head(100))
        st.write(df_reviews.shape)









