
import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.title("Plotting Demo")
st.write("This demo shows a simple line chart using random data.")

chart_data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=["Series 1", "Series 2", "Series 3"],
)

st.line_chart(chart_data)

if st.button("Re-run"):
    st.rerun()
