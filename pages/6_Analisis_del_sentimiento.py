import streamlit as st

st.set_page_config(page_title='Proyecto 2: Barcelona', layout='wide', page_icon='🇪🇸')


st.title('NATURAL LANGUAGE PROCESSING (NLP)')
st.write('El Procesamiento del Lenguaje Natural (NLP) es una disciplina que combina la informática, la linguistica y el aprendizaje automático. Este caso, hemos utilizado técnicas de NLP para analizar el sentimineto asociado con las palabras de nuestros dataframes de estudio (top_200 y bottom_200.')
st.write('Para analizar el sentimiento asociado con las palabras en cada dataframe, fusionamos los dataframes de estudio con df_reviews. Este último dataframe contiene opiniones de las personas sobre cada una de las propiedades.')

st.markdown('#### <span style="color:orange;">Estudio de idiomas - reviews</span>', unsafe_allow_html=True)
st.write('Como podemos observar en la siguientes 2 gráficas, existe una clara tendencia a escribir comentarios en inglés.')
col1, col2 = st.columns(2)
with col1:
    st.markdown('##### TOP_200')
    st.image('img/8_numero%20_comentario_top200.png')
with col2:
    st.markdown('##### BOTTOM_200')
    st.image('img/9_numero_comentario_bottom_200.png')


st.markdown('#### <span style="color:orange;"> Utilización de **CountVectorizer** - reviews</span>', unsafe_allow_html=True)
st.write('CountVectorizer es una clase de en scikit-learn que transforma una colección de documentos de texto en una matriz númerica de recuentos de palabras. En nuestro caso, los hemos utilizado para calcular la frecuencia de cada palabra única en el conjunto de textos de las opiniones.')
col1, col2 = st.columns(2)
with col1:
    st.markdown('##### TOP_200')
    st.write('Las palabras con más frecuencia en top_200 son: "apartment"-"great"-"very"-"stay"-"location"-"perfect"- "great"...')
    st.image('img/wordcloud1.png')
with col2:
    st.markdown('##### BOTTOM_200')
    st.write('Mientras que las palabras más frecuentes en bottom_200 son: "great"-"place"-"host"-"but"-"had"-"todo"...')
    st.image('img/wordcloud2.png')


st.markdown('#### <span style="color:orange;">Estudio de idiomas - description</span>', unsafe_allow_html=True)
st.write('Como podemos observar en la siguientes 2 gráficas, existe una tendencia aplastante a establecer descripciones en inglés. Esta clara tendencia puede deberse a que Barcelona es una ciudad turística.')
col1, col2 = st.columns(2)
with col1:
    st.markdown('##### TOP_200')
    st.image('img/10_lenguage_description_top200.png')
with col2:
    st.markdown('##### BOTTOM_200')
    st.image('img/11_language_description_bottom200.png')


st.markdown('#### <span style="color:orange;">Utilización de **CountVectorizer** - description</span>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown('##### TOP_200')
    st.write('Se puede ver como en el dataframe top_200 existe una clara tendencia hacia descripciones orientadas al alquiler de apartamentos, por palabras como "apartments"-"home"...')
    st.image('img/wordcloud3.png')
with col2:
    st.markdown('##### BOTTOM_200')
    st.write('Mientras que en dataframe bottom_200 existe una clara tendencia hacia al alquiler de habitaciones por palabra como "room".')
    st.image('img/wordcloud4.png')
st.write('Es conveniente establecer una descripción acorde al tipo de propiedad que se pretende alquilar. Antes de establecer una descripción se recomienda hacer una estudio de propiedades similares a la suya para poder sacar conclusiones respecto a tipo de descripción que se tiene que establecer.')
