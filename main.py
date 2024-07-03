from io import BytesIO
import streamlit as st
import pandas as pd


delimiter = st.radio("**Delimiter**", [",", ";"], horizontal=True)

uploaded_file = st.file_uploader("**Upload csv file**", type="csv")

if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file, delimiter=delimiter)

    st.write("**Preview data**", dataframe)

    output = BytesIO()

    dataframe.to_excel(output, index=False)

    st.download_button(
        label="**Download xlsx file**",
        data=output,
        file_name=f"{uploaded_file.name}.xlsx",
    )