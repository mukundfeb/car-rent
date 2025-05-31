Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # app.py
... 
... import streamlit as st
... 
... # Title of the app
... st.title("👋 Welcome to Streamlit!")
... 
... # Simple text
... st.write("This is your first Streamlit app.")
... 
... # Text input
... name = st.text_input("What's your name?")
... 
... # Button to display greeting
... if st.button("Say Hello"):
...     if name:
...         st.success(f"Hello, {name}! 👋")
...     else:
...         st.warning("Please enter your name first.")
