# Importamos librerias necesarias
import streamlit as st
import pandas as pd




# Configuramos las página de inicio
st.set_page_config(page_title='Proyecto 2: Barcelona', layout='wide', page_icon='🇪🇸')




# Configuración de la presentación
st.title('ANALISISIS DESCRIPTIVO')
st.markdown('##### <span style="color:orange;">Las siguientes gráficas muestran el reflejo de lo que nos pueden decir los datos al representarlos.</span>', unsafe_allow_html=True)
col1, col2 = st.columns (2)
with col1:
    st.write('Esta gráfica muestra la diferencia de precio que nos podemos encontrar entre los diferentes grupos vecinales de Barcelona. Recalcar, que aunque los precios parezcan similares entre los grupos de vecinos, estos cambian muchos de unos a otros.')
    st.image('img/19_precio_grupovecinos.png')
with col2:
    st.write('En este gráfico vemos el número de camas por tipo de habitación. Podemos hacer hincapié en la gran diferencia de número de habitaciones entre los apartamentos y las habitaciones de los hoteles.')
    st.image('img/20_camas_tipohabitacion.png')
st.write('')
st.write('')
col1, col2 = st.columns(2)
with col1:
    st.write('En esta gráfica, se muestra la evolución del los precio por el tipo de habitación, teniendo en cuenta el número de noches mínimas. Podemos hacer hincapié en como los apartamentos tienen una tendencia bajista respecto al precio, cuanto más noches más barato.')
    st.image('img/21_evolucion_preciohabitacion.png')
with col2:
    st.write('En esta gráficase muestra las distribución porcentual de los grupos vecinales. Se obseva como Eixample tiene el mayor porcentaje de ocupación, con una gran diferencia sobre los demás grupos vecinales.')
    st.image('img/22_grupos_vecinales.png')