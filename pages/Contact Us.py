import streamlit as st
st.title("Contact Us")
st.subheader("Adderess")
st.write("Kantatoli,Ranchi")
st.write("You can contact me at any time(24*7) I am available my contact details are")
st.subheader("Phone number")
st.write("9504292872")
st.subheader("Email ID")
st.write("adityadav0095@gmail.com")
if st.button("Signup"):
    st.switch_page("pages/SignUp.py")
