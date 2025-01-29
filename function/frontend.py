import streamlit as st
from function.utils import read_txt, read_columns_descriptions
from function.data_prep import get_df_summary

def subheader_main():
    overview_path = 'static/overview.txt'
    overview = read_txt(overview_path)
    st.subheader(overview)

def header_main():
    st.header("Neo Bank Churn Kaggle Competition")
    subheader_main()

def display_first_n_rows(df, n=10):
    st.subheader("10 first rows of raw dataframe")
    st.dataframe(df.limit(n))

def display_columns_descriptions():
    columns = read_columns_descriptions()
    st.subheader("Columns description")
    st.write(columns)

def display_df_summary(df):
    summary = get_df_summary(df)
    st.subheader('Dataframe summary')
    st.dataframe(summary)