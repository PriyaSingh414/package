import streamlit as st
import joblib

# Load the pre-trained model
model = joblib.load('placement.pkl')

def main():
    st.title("Placement Prediction Based on CGPA")
    st.write("Enter your CGPA to predict the likelihood of placement.")

    # Input: CGPA
    cgpa = st.slider("Select your CGPA", min_value=0.0, max_value=10.0, step=0.1)
    st.write(f"Your CGPA: {cgpa}")

    # Button to trigger prediction
    if st.button('Predict Placement'):
        # Validate CGPA
        if cgpa < 0.0 or cgpa > 10.0:
            st.error("Please enter a CGPA between 0.0 and 10.0.")
        else:
            # Make prediction
            result = model.predict([[cgpa]])
            st.success(f"Prediction: {'Placed' if result[0] == 1 else 'Not Placed'}")
            st.balloons()

if __name__ == '__main__':
    main()
