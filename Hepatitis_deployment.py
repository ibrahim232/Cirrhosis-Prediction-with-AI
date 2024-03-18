
import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
import warnings

def run():
    st.set_page_config(page_title="Cirrhosis Prediction", page_icon="🩺", layout="wide")
    warnings.simplefilter(action='ignore', category=FutureWarning)

    select_page = st.sidebar.radio('Select page', ['Analysis', 'Model Prediction', 'About'])

    if select_page == 'Analysis':
        cleaned_data = pd.read_csv('Hepatitis_Cleaned.csv')
        st.image('https://th.bing.com/th/id/OIP.nCkh1m-FQ0zwXAv0-9HY6QHaFi?rs=1&pid=ImgDetMain', width=700)
        st.write('### Dataset Overview')
        st.dataframe(cleaned_data.head())

        # Univariate Analysis for Categorical Features
        st.write('### Univariate Analysis for Categorical Features')
        categorical_cols = ['Sex']  
        for col in categorical_cols:
            fig = px.histogram(cleaned_data, x=col, color=col)
            st.plotly_chart(fig, use_container_width=True)

        # Bivariate Analysis for Numerical Features
        st.write('### Bivariate Analysis for Numerical Features')
        numerical_cols = ['Age', 'ALB', 'ALP', 'ALT', 'AST', 'BIL', 'CHE', 'CHOL', 'CREA', 'GGT', 'PROT']  
        for col in numerical_cols:
            fig = px.box(cleaned_data, x='Category', y=col, color='Category')
            st.plotly_chart(fig, use_container_width=True)

        # Correlation Heatmap for Numerical Features
        st.write('### Correlation Heatmap for Numerical Features')
        corr_matrix = cleaned_data[numerical_cols].corr()
        fig = px.imshow(corr_matrix, text_auto=True, color_continuous_scale='RdBu_r')
        st.plotly_chart(fig, use_container_width=True)

    elif select_page == 'Model Prediction':
        st.title('Cirrhosis Prediction Model')
        st.image('Cirrhosis-cover.jpg', width=700)
        model = joblib.load('Hepatitis_Model.pkl')
        inputs = collect_user_input()
        if st.button('Predict'):
            df = pd.DataFrame([inputs])
            result = model.predict(df)[0]
            display_prediction(result)

    elif select_page == 'About':
        display_about_info()

    display_footer()

def collect_user_input():
    st.sidebar.header('Enter Your Health Details:')
    # Updated input fields based on the cirrhosis dataset
    inputs = {
        'Sex': st.sidebar.selectbox('Sex', ['m', 'f']),
        'Age': st.sidebar.slider('Age', 20, 80, 50),
        'ALB': st.sidebar.slider('ALB (Albumin)', 31.4, 54.4, 42.06),
        'ALP': st.sidebar.slider('ALP (Alkaline Phosphatase)', 22.9, 115.4, 65.53),
        'ALT': st.sidebar.slider('ALT (Alanine Aminotransferase)', 3.8, 51.4, 22.83),
        'AST': st.sidebar.slider('AST (Aspartate Aminotransferase)', 12.0, 43.4, 24.52),
        'BIL': st.sidebar.slider('BIL (Bilirubin)', 1.8, 15.6, 7.22),
        'CHE': st.sidebar.slider('CHE (Cholinesterase)', 3.9, 12.86, 8.23),
        'CHOL': st.sidebar.slider('CHOL (Cholesterol)', 2.86, 7.8, 5.43),
        'CREA': st.sidebar.slider('CREA (Creatinine)', 41.0, 114.0, 77.89),
        'GGT': st.sidebar.slider('GGT (Gamma-Glutamyl Transferase)', 4.5, 44.6, 21.09),
        'PROT': st.sidebar.slider('PROT (Protein)', 62.1, 82.4, 72.18)
    }
    return inputs

def display_prediction(result):
    if result == 1:
        st.error("Prediction: High risk of cirrhosis.")
        st.markdown(health_advice(True))
    else:
        st.success("Prediction: Low risk of cirrhosis.")
        st.markdown(health_advice(False))

def health_advice(high_risk):
    if high_risk:
        return """
        ### Health Advice for High-Risk Individuals
        If you're at high risk of cirrhosis, it's crucial to consult with a healthcare provider for a detailed assessment and personalized advice. Consider adopting a liver-healthy lifestyle:
        - Maintain a balanced diet low in alcohol and fatty foods.
        - Engage in regular physical activity.
        - Monitor and manage your liver health regularly.
        """
    else:
        return """
        ### Health Advice for Low-Risk Individuals
        To maintain a low risk of cirrhosis, continue practicing a liver-healthy lifestyle:
        - Eat a diet rich in fruits, vegetables, and whole grains.
        - Stay active with regular exercise.
        - Avoid excessive alcohol consumption.
        - Keep up with regular health check-ups.
        """

def display_about_info():
    st.title('About Cirrhosis Prediction')
    st.markdown("""
        ## Background and Problem Statement

        Cirrhosis is a late stage of scarring (fibrosis) of the liver caused by many forms of liver diseases and conditions, such as hepatitis and chronic alcoholism. Early detection and management can greatly improve outcomes for individuals at risk. This app aims to leverage machine learning to predict cirrhosis risk based on health and lifestyle factors, facilitating early intervention and awareness.
    """)

def display_footer():
    st.markdown("Developed for educational and informational purposes.")
    st.markdown("[GitHub](https://github.com/ibrahim232) | [LinkedIn](https://www.linkedin.com/in/ibrahim-abdelnasar/)")

if __name__ == '__main__':
    run()
