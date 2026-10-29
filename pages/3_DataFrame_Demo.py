
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

st.title("DataFrame Demo")
st.write("This demo shows how to display a pandas DataFrame.")

df = pd.DataFrame(
    {
        "Country": ["Australia", "India", "United States", "Japan"],
        "Population (millions)": [27, 1460, 347, 123],
        "Example Value": np.random.randint(10, 100, 4),
    }
)

st.subheader("Example data")
st.dataframe(df, use_container_width=True)

st.subheader("Example bar chart")
st.bar_chart(df, x="Country", y="Example Value")
