import pandas as pd
import numpy as np
import streamlit as st


def report_config():
    st.set_page_config(layout='wide')

def read_txt(path):
    with open(path, 'r') as f:
        return f.read()

def read_columns_descriptions():
    path = 'static/df_columns_description.txt'
    columns = read_txt(path)
    return columns
