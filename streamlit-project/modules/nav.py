import streamlit as st

def Navbar():
    with st.sidebar:
        st.page_link('main.py', label='Car Sales Dataset', icon=None)
        st.page_link('pages/1_EDA.py', label='Exploratory data analysis', icon=None)
        st.page_link('pages/2_VIS.py', label='Visualization', icon=None)
        st.page_link('pages/3_MOD.py', label='Machine Learning Model', icon=None)