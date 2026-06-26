import streamlit as st
import pymongo

conn=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2v")
mydb=conn["STUDENTS"]
my=mydb["user_info"]

st.success("User Profile")

if "username" not in st.session_state:
    st.error("Please Signin First")
    st.stop()

str1=st.session_state["username"]

res=my.find({"username":str1})

for data in res:

    st.success(f"Username : {data['username']}")
    st.success(f"Password : {data['password']}")
    st.success(f"Email : {data['email']}")
    st.success(f"Phone Number : {data['phone']}")
    st.success(f"Gender : {data['gender']}")
    st.success(f"Address : {data['address']}")
    st.success(f"Dob : {data['dob']}")
    
# Logout
if st.button("Logout"):
    st.session_state.clear()
    st.switch_page("main.py")
