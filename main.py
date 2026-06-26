import streamlit as st
import time
with st.spinner("Loading....."):
       time.sleep(2)
st.title("XYZ SCHOOL")
st.write("Welcome to ours school page")
st.write("1.It's for class Nursery to Tenth")
st.write("2.We give best education to your childern")
st.write("3.We have best teacher and staff for your childern")
st.write("thank you")
st.write("For more detalis go to about us")
if st.button("About Us"):
       st.switch_page("pages/About Us.py")
