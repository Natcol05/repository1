
import streamlit as st 
import pandas as pd 
import plotly_express as px 

ruta = 'vehicles_us.csv'
car_data = pd.read_csv(ruta)
car_data

st.header('información de vehiculos')
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    fig = px.histogram(car_data, x="odometer")
    
    st.plotly_chart(fig, use_container_width=True)
    
   

import streamlit as st 
import pandas as pd 
import plotly_express as px 

ruta = 'vehicles_us.csv'
car_data = pd.read_csv(ruta)
car_data

st.header('información de vehiculos')
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    fig = px.histogram(car_data, x="odometer")
    
    st.plotly_chart(fig, use_container_width=True)


