import streamlit as st
from function.data_prep import get_churn_train_df
from function.utils import read_txt


def subheader():
    overview_path = '../static/overview.txt'
    overview = read_txt(overview_path)
    st.subheader(overview)

def header():
    st.header("Neo Bank Churn Kaggle Competition")
    subheader()

def train_df():
    train_df = get_churn_train_df()
    st.dataframe(train_df.show(10))
