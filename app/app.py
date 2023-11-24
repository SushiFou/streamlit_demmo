import pandas as pd
import streamlit as st
from homepage import *
from machine_learning import *
from visualization import *

st.title('DEMO APP ESILV')


display_page = st.sidebar.selectbox('Quelle page souhaitez-vous visiter ?',('HOMEPAGE', 'VISUALISATIONS', 'MACHINE LEARNING'))
# HOMEPAGE STUFF
if display_page == 'HOMEPAGE':
    homepage()
    if st.button('Load Data'):
        df_train = pd.read_csv('./data/Data_Train.csv')
        st.write("Data Successfully loaded")
        st.dataframe(data=df_train)
        st.line_chart(data=df_train, x='Airline', y ='Price')
# VISUALIZATION STUFF
elif display_page == 'VISUALISATIONS':
    visualization()
# MACHINE LEARNING STUFF
elif display_page == 'MACHINE LEARNING':
    ml()



