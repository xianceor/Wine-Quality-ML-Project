import streamlit as st
import pandas as pd
import joblib
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animations from URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load your model
model = joblib.load("best_wine_quality_model.pkl")

# Page config with a wine emoji icon
st.set_page_config(page_title="🍷 Wine Quality Predictor", layout="wide", page_icon="🍷")

# Load Lottie animations
waifu_animation = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jcikwtux.json")  # cute anime girl
wine_animation = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_g6qzauqj.json")  # wine pouring

# Header section with Lottie animation + title
col1, col2 = st.columns([3,1])
with col1:
    st.markdown("<h1 style='color: purple; font-weight: bold;'>🍷 Wine Quality Prediction App</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:20px;'>Predict the quality of wine based on physicochemical attributes.</p>", unsafe_allow_html=True)
    st.markdown("---")

with col2:
    if wine_animation:
        st_lottie(wine_animation, speed=1, height=150, key="wine_anim")

# Sidebar for inputs
with st.sidebar:
    st.header("🍇 Input Features")
    fixed_acidity = st.slider("Fixed Acidity", 4.0, 16.0, 7.0, help="Amount of fixed acids in wine.")
    volatile_acidity = st.slider("Volatile Acidity", 0.10, 1.50, 0.5, help="Amount of volatile acids affecting sharpness.")
    citric_acid = st.slider("Citric Acid", 0.0, 1.0, 0.3, help="Contributes to freshness and flavor.")
    residual_sugar = st.slider("Residual Sugar", 0.5, 16.0, 2.5, help="Sugar remaining after fermentation.")
    chlorides = st.slider("Chlorides", 0.01, 0.2, 0.05, help="Salt content affecting taste.")
    free_sulfur_dioxide = st.slider("Free Sulfur Dioxide", 1.0, 72.0, 15.0, help="Preservative levels.")
    total_sulfur_dioxide = st.slider("Total Sulfur Dioxide", 6.0, 300.0, 46.0, help="Total sulfur dioxide present.")
    density = st.slider("Density", 0.9900, 1.0050, 0.9965, help="Mass per unit volume.")
    pH = st.slider("pH", 2.5, 4.5, 3.3, help="Acidity level of wine.")
    sulphates = st.slider("Sulphates", 0.2, 2.0, 0.6, help="Contributes to wine's stability and flavor.")
    st.markdown("---")
    if st.button("Predict Wine Quality"):
        input_data = pd.DataFrame([{
            'fixed acidity': fixed_acidity,
            'volatile acidity': volatile_acidity,
            'citric acid': citric_acid,
            'residual sugar': residual_sugar,
            'chlorides': chlorides,
            'free sulfur dioxide': free_sulfur_dioxide,
            'total sulfur dioxide': total_sulfur_dioxide,
            'density': density,
            'pH': pH,
            'sulphates': sulphates
        }])
        with st.spinner('Predicting...'):
            prediction = model.predict(input_data)[0]
        st.success(f"Predicted Wine Quality: **{int(round(prediction))}** (out of 10)")

# Main content layout with 2 columns
left_col, right_col = st.columns([2, 1])

with left_col:
    st.markdown("### 🍷 A Little History about Wine")
    st.markdown(
        """
        Wine is one of the oldest alcoholic beverages, dating back thousands of years.
        It is believed that wine production began around 6000 BC in what is now Georgia.
        The ancient Egyptians, Greeks, and Romans all valued wine for both its taste and cultural significance.
        
        Wine quality depends on many factors including grape type, fermentation process, and chemical composition.
        This app helps predict wine quality based on some of these physicochemical attributes.
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.markdown("### ✨ “Savor the Spirit of Adventure — Quality Wine, Inspired by the Straw Hat Crew!” 🍷🏴‍☠️")
    st.markdown(
        """
        <div style="text-align:center;">
            <img src="https://i.pinimg.com/originals/34/92/0a/34920a32bfef7237f77b6181b6da6191.gif" alt="Anime Waifu Drinking Wine" width="500" />
        </div>
        """,
        unsafe_allow_html=True,
    )

with right_col:
    st.markdown("### 🍇 Feature Guide")
    st.info(
        """
        - **Fixed Acidity:** Amount of fixed acids.
        - **Volatile Acidity:** Amount of volatile acids.
        - **Citric Acid:** Adds freshness.
        - **Residual Sugar:** Sugar left after fermentation.
        - **Chlorides:** Salt content.
        - **Free Sulfur Dioxide:** Preservatives.
        - **Total Sulfur Dioxide:** Total sulfur compounds.
        - **Density:** Mass per unit volume.
        - **pH:** Acidity level.
        - **Sulphates:** Flavor and stability.
        """
    )


#C:\Users\lenovo\OneDrive\Documents\Bootcamp Project 1> streamlit run wine_quality_app.py