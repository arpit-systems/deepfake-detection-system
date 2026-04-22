import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

st.title("Deepfake Detection System")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("Data Preview", df.head())

    # Check if target column exists
    if "is_deepfake" in df.columns:

        y = df["is_deepfake"]
        X = df.select_dtypes(include=['number']).drop(columns=["is_deepfake"])

        model = LogisticRegression()
        model.fit(X, y)

        predictions = model.predict(X)

        df["Prediction"] = predictions

        st.write("Predictions", df.head())

    else:
        st.warning("No 'is_deepfake' column found. Only preview is shown.")