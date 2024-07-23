import streamlit as st
import pandas as pd
import numpy as np

df = st.file_uploader("Choose a file")

chart_data = pd.DataFrame(df, columns=df.columns)