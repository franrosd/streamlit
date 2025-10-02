#Library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title Page
st.header("Exploratory Data Analysis")
st.subheader('Dataframe of Car Sales')
# Load Data
df = pd.read_csv('data.csv')
st.dataframe(df)

# Descriptive Statistic
st.subheader("Descriptive Statistics:")
st.dataframe(df.describe(include='all'))

# Manufacturer Distribution
st.subheader("Ditribution of each Column")
st.markdown('Distribution of Manufacturer')
        
fig5, ax = plt.subplots()
ax.hist(df['Manufacturer'])
st.pyplot(fig=fig5, 
          clear_figure=None, 
          width="content", 
          use_container_width=None)

# Engine Size Distribution
st.markdown('Distribution of Engine Size')
        
fig6, ax = plt.subplots()
ax.hist(df['Engine size'])
st.pyplot(fig=fig6, 
          clear_figure=None, 
          width="content", 
          use_container_width=None)

# Fuel Type Distribution
st.markdown('Fuel Type Distribution')
          
fig3, ax = plt.subplots()
ax.hist(df['Fuel type'])
st.pyplot(fig=fig3, 
          clear_figure=None, 
          width="content", 
          use_container_width=None)

# Year of manufacture Distribution
st.markdown('Distribution of Year of Manufacture')
         
fig4, ax = plt.subplots()
ax.hist(df['Year of manufacture'])
st.pyplot(fig=fig4, 
          clear_figure=None, 
          width="content", 
          use_container_width=None)

# Mileage Distribution
st.markdown('Distribution of Mileage')
         
fig2, ax = plt.subplots()
ax.hist(df['Mileage'])
st.pyplot(fig=fig2, 
          clear_figure=None, 
          width="content", 
          use_container_width=None)

# Price Distribution
st.markdown('Distribution of Price')

fig1, ax = plt.subplots()
ax.hist(df['Price'])
st.pyplot(fig=fig1, 
          clear_figure=None, 
          width="content", 
          use_container_width=None)