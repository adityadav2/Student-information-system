import streamlit as st
import pymongo
import random

st.title("SignIn")

t1 = st.text_input("Username")
t2 = st.text_input("Password", type="password")

if "captcha" not in st.session_state:
    st.session_state["captcha"] = random.randint(1000, 9999)

st.write("CAPTCHA:", st.session_state["captcha"])
captcha_input = st.text_input("Enter CAPTCHA")

if st.button("SIGNIN"):

    if captcha_input != str(st.session_state["captcha"]):
        st.error("Invalid CAPTCHA")

    else:
        conn = pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2v")

        mydb = conn["STUDENTS"]
        my = mydb["user_info"]

        res = my.find({"username": t1, "password": t2})

        v = 0

        for data in res:
            v += 1
            st.session_state["username"] = t1
            st.switch_page("pages/profile.py")

        if v == 0:
            st.error("Invalid Login")

st.write("If you want to change your password then click change password")

if st.button("Change Password"):
    st.switch_page("pages/change password.py")

st.write("If you forget your password then contact me")

if st.button("contact me"):
   st.switch_page("pages/Contact Us.py")

