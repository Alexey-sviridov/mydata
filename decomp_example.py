import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_excel("./for_decomp_example.xlsx")

chart_data = pd.DataFrame(df, columns=df.columns)