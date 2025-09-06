import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name = st.text_input("Enter your name: ")

age = st.slider("Select your age: ", 0, 100, 25)
st.write(f"Your age is {age}.")

option = ["Python", "Java", "C++", "Javascript"]
choice = st.selectbox("Choose your favourite language: ", option)
st.write(f"You favourite language is {choice}.")


if name:
    st.write(f"Hello, {name}")

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file",type = "csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)