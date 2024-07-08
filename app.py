import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('graduate_admission_model.pkl', 'rb'))


# Function to make predictions
def predict_admission(gre_score, toefl_score, university_rating, sop, lor, cgpa, research):
    features = np.array([[gre_score, toefl_score, university_rating, sop, lor, cgpa, research]])
    prediction = model.predict(features)
    return prediction[0]


# Streamlit app
def main():
    st.set_page_config(page_title="Graduate Admission Predictor", page_icon="🎓", layout="centered")

    # App title and description
    st.title("Graduate Admission Predictor")
    st.markdown("""
        <div style="background-color:#2E8B57;padding:10px;border-radius:10px;">
        <h2 style="color:white;text-align:center;">Predict Your Chances of Graduate School Admission</h2>
        </div>
    """, unsafe_allow_html=True)

    st.image("https://example.com/admission_image.jpg", use_column_width=True)

    st.markdown("### Enter the following details:")

    # Input fields
    gre_score = st.number_input("GRE Score", min_value=0, max_value=340, value=320)
    toefl_score = st.number_input("TOEFL Score", min_value=0, max_value=120, value=100)
    university_rating = st.slider("University Rating", min_value=1, max_value=5, value=3)
    sop = st.slider("Statement of Purpose (SOP) Rating", min_value=1.0, max_value=5.0, step=0.1, value=3.5)
    lor = st.slider("Letter of Recommendation (LOR) Rating", min_value=1.0, max_value=5.0, step=0.1, value=3.5)
    cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.01, value=8.0)
    research = st.selectbox("Research Experience", options=[0, 1])

    if st.button("Predict"):
        prediction = predict_admission(gre_score, toefl_score, university_rating, sop, lor, cgpa, research)
        st.success(f'Your predicted chance of admission is {prediction * 100:.2f}%')

    st.markdown("""
        <style>
        .stButton button {
            background-color: #2E8B57;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)


if __name__ == '__main__':
    main()
