import streamlit as st
import requests


st.title("Handwritten Digit Recognition (0-9)")
st.write("Upload a handwritten digit image and get prediction.")

uploaded_file = st.file_uploader("Choose an image", type=["png"])

predict = st.button("Predict")

if uploaded_file is not None:

    if predict:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            files={
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }
        )

        result = response.json()

        st.subheader(f"Predicted Digit: {result['predicted_digit']}")

