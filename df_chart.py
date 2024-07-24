import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("for_decomp_example.csv", sep=';',encoding="windows-1251")

st.dataframe(df)