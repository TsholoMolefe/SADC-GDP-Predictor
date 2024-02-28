import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the best model
loaded_model = joblib.load("best_model.pkl")

# Set the title
st.title("SADC GDP Predictor")

# Create a new data frame with the same columns as used during training
new_data_columns = ['Year', 'GDP Growth%', 'GDP Government pp', 'GDP Private pp', 'Investment', 'Inflation',
                    'Unemployment', 'Employment', 'Imports', 'Exports', 'FDI', 'Government Debt',
                    'Real Interest Rate', 'Gini Index', 'Population', 'Population Growth', 'Life Expectancy',
                    'Literacy', 'Net Exports', 'Country Name']

new_data = pd.DataFrame(columns=new_data_columns)

# Fill in the new_data DataFrame with user input
for column in new_data_columns:
    if column == 'Country Name':
        country_mapping = {
            0: 'Angola', 1: 'Botswana', 2: 'Democratic Republic of the Congo', 3: 'Eswatini',
            4: 'Lesotho', 5: 'Madagascar', 6: 'Malawi', 7: 'Mauritius', 8: 'Mozambique', 9: 'Namibia',
            10: 'Seychelles', 11: 'South Africa', 12: 'Tanzania', 13: 'Zambia', 14: 'Zimbabwe'
        }
        country_input = st.selectbox("Select Country:", list(country_mapping.keys()), key='country_input')
        new_data[column] = [country_mapping[country_input]]
    elif column == 'Year':
        new_data[column] = [int(st.number_input(f'Enter {column}: ', value=0, step=1, key=f'{column}_input'))]
    elif column == 'Population':
        new_data[column] = [int(st.text_input(f'Enter {column}: ', value='0', key=f'{column}_input'))]
    else:
        new_data[column] = [st.number_input(f'Enter {column}: ', value=0.0, step=0.01, key=f'{column}_input')]

# Encoding 'Country Name' using LabelEncoder
label_encoder = LabelEncoder()
new_data['Country Name'] = label_encoder.fit_transform(new_data['Country Name'])

# Make predictions using the loaded model
prediction = loaded_model.predict(new_data)

# Display the prediction
st.write(f'Predicted GDP: {prediction[0]}')

