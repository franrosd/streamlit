# Import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

##Step 1
# Load Data
df = pd.read_csv('data.csv')

# Get column names
column_names = df[["Engine size","Year of manufacture","Mileage","Price"]].columns

## Step 2
# Sidebar for user input selection
st.sidebar.markdown('<h2 style="color: white;">Select One output and at least one input Variable</h1>', unsafe_allow_html=True)
# Select output variable
output_variable_model = st.sidebar.selectbox('Select One output Variable', column_names)

# Select input variables to predict the target variable (output)
input_variables_model = st.sidebar.multiselect('Select at least one input Variable', column_names)

if not output_variable_model or not input_variables_model:
    st.warning('Select One output and at least one input Variable to start.')

# User option for setting the rate of test data
test_data_rate = st.sidebar.slider('Select the rate of test data', 1000, 25000, 1000, 1000)

## Step 3
# Define input features (X) and target variable (y) for model training
X_model = df[input_variables_model]
y_model = df[output_variable_model]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_model, y_model,  test_size=test_data_rate, random_state=42)

# Train Random Forest model
model = RandomForestRegressor()
model.fit(X_train, y_train)

## Step 4
# Streamlit application
# Model Training and Validation

st.title('Machine Learning Model: Training, Validation and Prediction using Random Forest Algorithm')

# Display information about the trained model
st.header('Model Information')
st.write(f'Output Variable (Target): {output_variable_model}')
st.write(f'Input Variables: {", ".join(input_variables_model)}')
st.write(f'Training Data Shape: {X_train.shape}')
st.write(f'Test Data Shape: {X_test.shape}')

# Display scatter plot chart of predicted vs observed values for test data
st.subheader('Scatter Plot: Predicted vs Observed (Test Data)')

test_predictions = model.predict(X_test)
scatter_df = pd.DataFrame({'Observed': y_test, 'Predicted': test_predictions})
fig, ax = plt.subplots(figsize=(8, 5))

# Create a scatter plot with a regression line
fig, ax = plt.subplots(figsize=(8, 5))
scatter_plot = sns.regplot(x='Observed', y='Predicted', data=scatter_df, ax=ax)

# Calculate R-squared value
r_squared = r2_score(y_test, test_predictions)

# Calculate Root Mean Squared Error (RMSE)
rmse = np.sqrt(mean_squared_error(y_test, test_predictions))

# Customize title and labels
scatter_plot.set_title(f'Predicted vs Observed {output_variable_model}', color='black')
scatter_plot.set_xlabel('Observed', color='blue')
scatter_plot.set_ylabel('Predicted', color='blue')

# Show the plot
st.pyplot(fig)

# Add R-squared and RMSE result
st.write('r_squared = ', r_squared)
st.write('Root Mean Square Error (RMSE) =', rmse)

#ax.text(0.05, 0.9, text, transform=ax.transAxes2), color='blue', fontsize=1
# Display feature importance chart
st.subheader('Feature Importance Chart')
feature_importance_model = pd.Series(model.feature_importances_, index=input_variables_model).sort_values(ascending=False)
fig, ax=plt.subplots(figsize=(10, 6))
sns.barplot(x=feature_importance_model, y=feature_importance_model.index, palette='viridis')
ax.set_title('Random Forest Feature Importance')
st.pyplot(fig)