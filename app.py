import streamlit as st
from geolocalizador import *
from streamlit_folium import folium_static
from pprint import pprint

st.title('Mapzer App')
st.sidebar.title('Menu')

origem = st.sidebar.selectbox('Endereço de origem', ['Selecione um endereço',
                                                     'Av. Cezar Hilal, 700, Vitória - ES'])
data = st.sidebar.date_input('Data')
equipes = st.sidebar.selectbox('Número de equipes', [1, 2, 3, 4, 5, 6, 7])

if __name__ == '__main__':
    try:
        bd = acessa_bd(data)

    except AttributeError:
        st.write('Conexão com banco de dados não realizada.')

    else:
        df = gera_dataframe(bd)
        df = agrupa_visitas(df, equipes)

        st.write(df)
        # df = agrupa_visitas(df, equipes)
