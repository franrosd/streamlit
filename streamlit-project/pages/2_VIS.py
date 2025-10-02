#Library
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title Page
st.header("Visualization")

# Load Data
df = pd.read_csv('data.csv')

# Bar Chart 2
st.markdown('Model & Year of Manufacture by Manufacturer')
st.bar_chart(data=df, 
             x='Manufacturer', 
             y='Year of manufacture', 
             x_label=None, 
             y_label=None, 
             color='Model', 
             horizontal=True, 
             sort=True, 
             stack=None, 
             width=None, 
             height=None, 
             use_container_width=True)

# Bar Chart 1
st.markdown('Price distribution by Fuel Type')
st.bar_chart(data=df, 
             x='Fuel type', 
             y='Price', 
             x_label=None, 
             y_label=None, 
             color='Fuel type', 
             horizontal=None, 
             sort=True, 
             stack=None, 
             width=None, 
             height=None, 
             use_container_width=True)

# Correlation Matrix
st.subheader("Correlation Matrix (Heatmap)")

corr = df[["Engine size","Year of manufacture","Mileage","Price"]].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap='mako', fmt=".2f", linewidths=.5, ax=ax)
# Display the plot in Streamlit
st.pyplot(fig) 

st.markdown('-0.81 = Mileage x Year')
st.markdown('0.71 = Year x Price')
st.markdown('-0.63 = Mileage x Price')

# Bar Chart 3
st.subheader('Price distribution by Year of Manufacture')
st.bar_chart(data=df, 
             x='Year of manufacture', 
             y='Price', 
             x_label=None, 
             y_label=None, 
             color=None, 
             horizontal=False, 
             sort=True, 
             stack=None, 
             width=None, 
             height=None, 
             use_container_width=True)

# Bar Chart 4
st.subheader('Price distribution by Mileage')
st.bar_chart(data=df, 
             x='Mileage', 
             y='Price', 
             x_label=None, 
             y_label=None, 
             color=None, 
             horizontal=False, 
             sort=True, 
             stack=None, 
             width=None, 
             height=None, 
             use_container_width=True)