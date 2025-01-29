import streamlit as st
from function.utils import read_txt, read_columns_descriptions


def subheader_main():
    overview_path = 'static/overview.txt'
    overview = read_txt(overview_path)
    st.subheader(overview)

def header_main():
    st.header("Neo Bank Churn Kaggle Competition")
    subheader_main()

def display_first_n_rows(df, n=10):
    st.title("10 first rows of raw dataframe")
    st.dataframe(df.limit(n))

def display_columns_descriptions():
    columns = read_columns_descriptions()
    st.write(columns)
