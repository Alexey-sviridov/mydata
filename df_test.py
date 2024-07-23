import streamlit as st
import pandas as pd
import numpy as np

uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")

st.image("./for_decomp_example.xlsx")