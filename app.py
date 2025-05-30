Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import streamlit as st
... 
... st.title("👋 Hello Streamlit!")
... st.write("This is your first Streamlit app.")
... 
... # Input from user
... name = st.text_input("Enter your name")
... 
... # Button to display greeting
... if st.button("Greet Me"):
