import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(10, 2) / [50, 50] + [18.844184, -97.1286527],
    columns=['lat', 'lon'])

st.map(map_data)

st.dataframe(map_data)