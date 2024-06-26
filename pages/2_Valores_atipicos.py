# Importamos librerias necesarias
import streamlit as st
import streamlit.components.v1 as components


# Configuración de página
st.set_page_config(page_title='Proyecto 2: Barcelona', layout='wide', page_icon='🇪🇸')





# Mostramos los apartados que queremos en nuestra presentación
st.title('VALORES ATIPICOS')
st.markdown('##### <span style="color:orange;">En esta sección analizamos los valores atípicos.</span>', unsafe_allow_html=True)
st.write('Para ser más específicos con nuestra explicación, a continuación, mostraremos 2 graficos en los que se puede de manera objetiva la diferencia entre los valores atípicos y la gran cantidad de datos.')
col1, col2 = st.columns(2)
with col1:
    with open('/Users/juliobrionesmorales/Documents/GitHub/Airbnb_Barcelona/HTML/1_outliers_price.html', 'r') as file:
        html_content = file.read()
    components.html(html_content,height=700)

with col2:
    with open('/Users/juliobrionesmorales/Documents/GitHub/Airbnb_Barcelona/HTML/2_outliers_nights.html', 'r') as file:
        html_content = file.read()
    components.html(html_content, height=700) 
st.markdown('##### <span style="color:orange;">Función genérica utilizada para arreglar outliers</span>', unsafe_allow_html=True)
st.write('El objetivo principal de esta función es arreglar los valores atípicos o outliers. Identificamos los valores a atípicos como aquellos que son mayores que los bigotes (máximos y mínimos) del diagrama de caja y bigotes. Para ello, este función sustituye, estos valores atípicos por los valores de máximo o mínimo del diagrama de caja y bigotes.')
st.image('img/3_funcion_outliers.png',width=1000)

st.markdown('##### <span style="color:orange;">Esta sección volvemos a analizar los valores atípicos</span>', unsafe_allow_html=True)
st.write('Para comprobar que la función utilizada en el apartado anterior ha sido útil con respecto a la modificación u ajuste de los valores atípicos, vamos a volver a mostrar las gráficas de caja y bigotes pero con los datos arreglados.')
col1, col2 = st.columns(2)
with col1:
    with open('/Users/juliobrionesmorales/Documents/GitHub/Airbnb_Barcelona/HTML/3_sinoutliers_price.html', 'r') as file:
        html_content = file.read()
    components.html(html_content,height=700)

with col2:
    with open('/Users/juliobrionesmorales/Documents/GitHub/Airbnb_Barcelona/HTML/4_sinoutliers_nights.html', 'r') as file:
        html_content = file.read()
    components.html(html_content, height=700)



