# Importamos librerias necesarias
import streamlit as st
import streamlit.components.v1 as components



# Configuramos las página de inicio
st.set_page_config(page_title='Proyecto 2: Barcelona', layout='wide', page_icon='🇪🇸')




# Configuración de la presentación
st.title('ANALISISIS DESCRIPTIVO')
st.markdown('##### <span style="color:orange;">Las siguientes gráficas muestran el reflejo de lo que nos pueden decir los datos al representarlos.</span>', unsafe_allow_html=True)
col1, col2 = st.columns (2)
with col1:
    st.write('Esta gráfica muestra la diferencia de precio que nos podemos encontrar entre los diferentes grupos vecinales de Barcelona. Recalcar, que aunque los precios parezcan similares entre los grupos de vecinos, estos cambian muchos de unos a otros.')
    with open('/Users/juliobrionesmorales/Documents/GitHub/Airbnb_Barcelona/HTML/5_precio_grupovecinos.html', 'r') as file:
        html_content = file.read()
    components.html(html_content,height=700)

with col2:
    st.write('En este gráfico vemos el número de camas por tipo de habitación. Podemos hacer hincapié en la gran diferencia de número de habitaciones entre los apartamentos y las habitaciones de los hoteles.')
    with open('/Users/juliobrionesmorales/Documents/GitHub/Airbnb_Barcelona/HTML/6_camas_tipohabitacion.html', 'r') as file:
        html_content = file.read()
    components.html(html_content, height=700) 
st.write('')
col1, col2 = st.columns(2)
with col1:
    st.write('En esta gráfica, se muestra la evolución del los precio por el tipo de habitación, teniendo en cuenta el número de noches mínimas. Podemos hacer hincapié en como los apartamentos tienen una tendencia bajista respecto al precio, cuanto más noches más barato.')
    with open('/Users/juliobrionesmorales/Documents/GitHub/Airbnb_Barcelona/HTML/7_evolucion_preciohabitacion.html', 'r') as file:
        html_content = file.read()
    components.html(html_content,height=700, width=800)
with col2:
    st.write('En esta gráficase muestra las distribución porcentual de los grupos vecinales. Se obseva como Eixample tiene el mayor porcentaje de ocupación, con una gran diferencia sobre los demás grupos vecinales.')
    with open('/Users/juliobrionesmorales/Documents/GitHub/Airbnb_Barcelona/HTML/8_grupos_vecinos.html', 'r') as file:
        html_content = file.read()
    components.html(html_content,height=700,width=600)