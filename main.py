import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("hello world")

st.title("simple data dashboard")

upload_file = st.file_uploader("Upload Your file", "csv")


if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.subheader("data preview")
    st.write(df.head())

    if st.button("view summary of data"):
        st.write(df.describe())

    number_of_rows = st.number_input("how many row you want to see?", min_value= 1, max_value= len(df))
    if st.button("view add data"):
        st.write(df.head(number_of_rows))

    st.subheader("Filer the data")
    column = df.columns.tolist()
    select_columns = st.selectbox("select columns filter by", column)
    unique_value = df[select_columns].unique()
    st.subheader(f"Total Values are: {unique_value.size}" )
    selected_value = st.selectbox("Selected value", unique_value)
    # "=========================================================="
    # st.write(unique_value)

    filtered_df = df[df[select_columns] == selected_value]
    st.subheader(f"Total Values are: {filtered_df.size}" )
    st.write(filtered_df)


    st.subheader("Plot Data")
    x_columns = st.selectbox("Select Column for x axis", column)
    y_columns = st.selectbox("Select Column for y axis", column)

    if st.button("Plot Graph"):
        st.line_chart(filtered_df.set_index(x_columns)[y_columns])
else:
    st.write("waiting for the file upload")