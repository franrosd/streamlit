#Library
import streamlit as st
import pandas as pd

# add text
st.title("Car Sales Dataset")
st.header("Comprehensive dataset of 50k car listings with technical specifications, mileage")
st.markdown("This dataset contains detailed information on car sales, covering multiple manufacturers and models. It is suitable for data analysis, price prediction, market trend analysis, machine learning, and exploratory data analysis (EDA).\nThe dataset includes information about manufacturers, car models, engine specifications, fuel type, year of manufacture, mileage, and final sale price\n\nResearchers, data scientists, and machine learning practitioners can use this dataset for:\n\n    Price prediction models (e.g., regression, XGBoost, deep learning)\n    Car valuation analysis for resale markets\n    Market trend analysis across manufacturers and fuel types\n    Data visualization projects\n\nThe dataset is clean, structured, and well-suited for both beginners and advanced projects.")

# add image
st.image("images/car-main.jpg")