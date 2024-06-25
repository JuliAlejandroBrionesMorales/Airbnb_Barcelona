# Importamos librerias necesarias
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go




# Configuramos las página de inicio
st.set_page_config(page_title='Proyecto 2: Barcelona', layout='wide', page_icon='🇪🇸')






# Cargamos base de datos

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

# Cargar los DataFrames usando las funciones cacheadas para evitar retrasos al cargar nuestra presentación.
df_calendar = load_df_calendar()
df_listings = load_df_listings()
df_reviews = load_df_reviews()

@st.cache_data
def load_df_calendar():
    return pd.read_feather(r'/Users/juliobrionesmorales/Documents/GitHub/Airbnb_Barcelona/data/3. data_sin_outliers/df_calendar.feather')

@st.cache_data
def load_df_listings():
    return pd.read_feather(r'/Users/juliobrionesmorales/Documents/GitHub/Airbnb_Barcelona/data/3. data_sin_outliers/df_listings.feather')

@st.cache_data
def load_df_reviews():
    return pd.read_feather(r'/Users/juliobrionesmorales/Documents/GitHub/Airbnb_Barcelona/data/3. data_sin_outliers/df_reviews.feather')

# Cargar los DataFrames usando las funciones cacheadas
df_calendar2 = load_df_calendar()
df_listings2 = load_df_listings()
df_reviews2 = load_df_reviews()






# Configuración de la presentación
st.title('ANALISISIS DESCRIPTIVO')
st.markdown('##### <span style="color:orange;">Las siguientes gráficas muestran el reflejo de lo que nos pueden decir los datos al representarlos.</span>', unsafe_allow_html=True)
col1, col2 = st.columns (2)
with col1:
    st.write('Esta gráfica muestra la diferencia de precio que nos podemos encontrar entre los diferentes grupos vecinales de Barcelona. Recalcar, que aunque los precios parezcan similares entre los grupos de vecinos, estos cambian muchos de unos a otros.')
    fig = px.box(df_listings, x='neighbourhood_group_cleansed', y='price', template='plotly', title='1. Precio en función del grupo de vecinos', width=800,height=700)
    st.plotly_chart(fig)  
with col2:
    st.write('En este gráfico vemos el número de camas por tipo de habitación. Podemos hacer hincapié en la gran diferencia de número de habitaciones entre los apartamentos y las habitaciones de los hoteles.')
    grouped_type = df_listings.groupby('room_type')['beds'].sum().reset_index()
     # Crear el gráfico de barras
    fig = px.bar(grouped_type, x='room_type', y='beds', title='2. Número de camas por tipo de habitación')
    fig.update_layout(yaxis=dict(tickformat='d')) # Actualizar el layout para quitar los decimales
    st.plotly_chart(fig)  
st.write('')
st.write('')
col1, col2 = st.columns(2)
with col1:
    st.write('En esta gráfica, se muestra la evolución del los precio por el tipo de habitación, teniendo en cuenta el número de noches mínimas. Podemos hacer hincapié en como los apartamentos tienen una tendencia bajista respecto al precio, cuanto más noches más barato.')
    # Agrupamos por mínimo de noches y tipo de habitación, y calculamos el precio promedio
    grouped_data = df_listings2.groupby(['minimum_nights','room_type'])['price'].mean().reset_index()

    # Configurar el formato del eje y para mostrar los precios reales
    fig = make_subplots(rows=2, cols=2, subplot_titles=grouped_data['room_type'].unique())

    for i, room_type in enumerate(grouped_data['room_type'].unique(), 1):
        filtered_data = grouped_data[grouped_data['room_type'] == room_type]
        fig.add_trace(go.Scatter(x=filtered_data['minimum_nights'], y=filtered_data['price'], mode='lines', name=room_type),
                    row=(i + 1) // 2, col=(i % 2) + 1)

    fig.update_layout(title_text='3. Evolución de precios por tipo de habitación', showlegend=False)
    fig.update_yaxes(title_text='Precio promedio', tickformat='€,.2f')  
    fig.update_xaxes(title_text='Mínimo de noches', tickformat='format_xaxis')
    st.plotly_chart(fig) 
with col2:
    st.write('En esta gráficase muestra las distribución porcentual de los grupos vecinales. Se obseva como Eixample tiene el mayor porcentaje de ocupación, con una gran diferencia sobre los demás grupos vecinales.')
    # Calcular la cantidad de listados por 'neighbourhood_group_cleansed'
    neighbourhood_counts = df_listings2['neighbourhood_group_cleansed'].value_counts().reset_index()
    neighbourhood_counts.columns = ['neighbourhood_group_cleansed', 'count']

    # Crear un gráfico circular
    fig = px.pie(neighbourhood_counts, values='count', names='neighbourhood_group_cleansed', 
                    title='4. Distribución de Listados por Grupo de Vecindarios',
                    labels={'neighbourhood_group_cleansed': 'Grupo de Vecindarios', 'count': 'Cantidad'},
                    template='plotly')
    st.plotly_chart(fig) 