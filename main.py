import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Result Analysis")
uploaded_file=st.file_uploader("Upload an Excel file",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.write(df)

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter data")
    columns=df.columns.tolist()
    selected_column=st.selectbox("Select column to filter by",columns)
    unique_values=df[selected_column].unique()
    selected_value=st.selectbox("Select a value",unique_values)
    filtered_df=df[df[selected_column]==selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column=st.selectbox("Select your x-axis column",columns)
    y_column=st.selectbox("Select your y-axis column",columns)

    if st.button("Generate plot"):
        st.line_chart(filtered_df.set_index(x_column) [y_column])
else:
    st.write("Waiting for file upload....")
