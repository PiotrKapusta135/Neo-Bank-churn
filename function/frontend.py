import streamlit as st
from function.data_prep import get_churn_train_df

def header():
    st.header("Neo Bank Churn Kaggle Competition")

def train_df():
    train_df = get_churn_train_df()
    st.dataframe(train_df)
