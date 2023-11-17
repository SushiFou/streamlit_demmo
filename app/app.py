import pandas as pd
import streamlit as st
from homepage import *
from machine_learning import *
from visualization import *

st.title('DEMO APP ESILV')


display_page = st.sidebar.selectbox('Quelle page souhaitez-vous visiter ?',('HOMEPAGE', 'VISUALISATIONS', 'MACHINE LEARNING'))
if display_page == 'HOMEPAGE':
    homepage()
elif display_page == 'VISUALISATIONS':
    visualization()
elif display_page == 'MACHINE LEARNING':
    ml()

