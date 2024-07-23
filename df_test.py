import streamlit as st
import pandas as pd
import numpy as np

file = pd.read_csv("./for_decomp_example.csv")

st.write('файл загружен')