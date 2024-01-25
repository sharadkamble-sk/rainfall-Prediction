import streamlit as st
import pickle
import os

# Function to load the model
@st.cache(allow_output_mutation=True)
def load_model():
    model_path = 'rain_pred_final.pkl'
    if os.path.exists(model_path):
        with open(model_path, 'rb') as model_file:
            return pickle.load(model_file)
    else:
        st.error(f"Model file '{model_path}' not found.")
        return None

# Main function
def main():
    st.title("Rainfall Prediction App")

    # Load the model
    model = load_model()

    if model is not None:
        # Collect user input
        rainfall = st.number_input("Rainfall:", value=0.0)
        sunshine = st.number_input("Sunshine:", value=0.0)
        windGustSpeed = st.number_input("Wind Gust Speed:", value=0.0)
        humidity3pm = st.number_input("Humidity 3pm:", value=0.0)
        pressure3pm = st.number_input("Pressure 3pm:", value=0.0)
        cloud9am = st.number_input("Cloud 9am:", value=0.0)
        cloud3pm = st.number_input("Cloud 3pm:", value=0.0)
        rainToday = st.number_input("Rain Today:", value=0.0)

        # Make prediction
        prediction = model.predict([[rainfall, sunshine, windGustSpeed, humidity3pm, pressure3pm, cloud9am, cloud3pm, rainToday]])
        output = int(prediction[0])

        # Render templates based on the prediction
        if output == 1:
            st.success("Prediction: Rainfall")
        else:
            st.success("Prediction: Sunny")

if __name__ == "__main__":
    main()
