
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Mapping Demo", page_icon="🌍")

st.title("Mapping Demo")
st.write("This demo displays random points on a map.")

map_data = pd.DataFrame(
    {
        "lat": np.random.uniform(-37.9, -37.7, 100),
        "lon": np.random.uniform(144.8, 145.1, 100),
    }
)

st.map(map_data)
