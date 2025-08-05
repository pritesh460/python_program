import joblib
import sys
import streamlit as st

model = joblib.load('G:/Python/cyberSecurity_project/Email_phishing/Phishing_model.pkl')
vectorizer = joblib.load('G:/Python/cyberSecurity_project/Email_phishing/vectorizer.pkl')

st.title('Phishing Email Detecter')

st.write("Choose how to provide the email content: ")

input_method = st.radio(
    "Select input method:",
    ('Paste Email Text', 'Uplode .tex File')
)

email_text = ''

if input_method == 'Paste Email Text':
    email_text = st.text_area("Past the email conten below: ")
elif input_method == 'Uplode .tex File':
    uploaded_file = st.file_uploader('Choose a .tex file',type='txt')
    if uploaded_file is not None:
        email_text = uploded_file.read().decode('utf-8')

if st.button('Check Email'):
    if email_text.strip()=='':
        st.warning("Please provide email content")
    else: 
        vectorizer_input = vectorizer.transform([email_text])
        prediction = model.predict(vectorizer_input)
        if prediction [0]==1:
            st.error("This is a Phishing email")
        else:
            st.success("This email is safe")
