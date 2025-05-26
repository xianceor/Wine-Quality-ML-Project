# Wine Quality Predictor

## Overview
This is an interactive web application built using Streamlit that predicts the quality of wine based on physicochemical properties. The model was trained on a wine quality dataset, and the app allows users to input various wine characteristics to obtain a predicted quality score.

## Features
- User-friendly interface with sliders for 10 key wine features:
  - Fixed Acidity
  - Volatile Acidity
  - Citric Acid
  - Residual Sugar
  - Chlorides
  - Free Sulfur Dioxide
  - Total Sulfur Dioxide
  - Density
  - pH
  - Sulphates
- Real-time prediction of wine quality on a scale of 0 to 10
- Informative descriptions for each input feature to assist users
- Responsive layout optimized for both desktop and mobile devices

## Technologies Used
- Python 3.x
- Streamlit
- scikit-learn / joblib (for loading the pre-trained model)
- pandas
- numpy

## Installation and Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/wine-quality-predictor.git
   cd wine-quality-predictor

## Model
The predictive model is pre-trained and saved as best_wine_quality_model.pkl. It uses physicochemical features to estimate wine quality on a numeric scale.

## Dataset
The model was trained on the Wine Quality Dataset from the UCI Machine Learning Repository.
