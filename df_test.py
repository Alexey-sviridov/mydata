import streamlit as st
import pandas as pd
import numpy as np

file = pd.read_excel("./for_decomp_example.xlsx")

st.write('файл загружен')