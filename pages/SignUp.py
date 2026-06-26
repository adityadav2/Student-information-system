import streamlit as st
import pymongo
from datetime import date

st.header("Sign Up")

name = st.text_input("User Name")
Password = st.text_input("Password", type="password")
email = st.text_input("Email")
phone = st.text_input("Phone Number")

c = st.selectbox("Course", ["BCA", "IT", "CS", "AI & ML"])
g = st.radio("Gender", ["M", "F"])

address = st.text_area("Address")
dob = st.date_input("DOB",min_value=date(1990,1,1),max_value=date.today())

b1 = st.button("SAVE")


def get_data():

    conn = pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2v")

    mydb = conn["STUDENTS"]
    my = mydb["user_info"]

    my.insert_one({
        "username": name,
        "password": Password,
        "email": email,
        "phone": phone,
        "course": c,
        "gender": g,
        "address": address,
        "dob": str(dob)
    })

    st.success("You are registered successfully !!")


if b1:
    get_data()
