import streamlit as st
from function.data_prep import get_churn_train_df
from function.frontend import display_first_n_rows, display_columns_descriptions, display_df_summary


st.header('EDA')
df = get_churn_train_df()

left, right = st.columns(2)

with left:
    display_first_n_rows(df, 10)
    display_df_summary(df)

with right:
    display_columns_descriptions()