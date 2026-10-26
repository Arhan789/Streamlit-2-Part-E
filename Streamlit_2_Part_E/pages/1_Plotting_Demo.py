import streamlit as st
import numpy as np
import time

st.set_page_config(
    page_title="Plotting Demo",
    page_icon="📈"
)

st.title("Plotting Demo")
st.sidebar.header("Plotting Demo")

st.write("This demo shows how Streamlit can create animated charts.")

if st.button("Generate animated chart"):
    progress_bar = st.progress(0)
    status_text = st.empty()
    chart = st.empty()

    data = np.random.randn(1, 1)

    for i in range(1, 101):
        new_rows = data[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        data = np.concatenate([data, new_rows])

        chart.line_chart(data)
        progress_bar.progress(i)
        status_text.text(f"{i}% Complete")
        time.sleep(0.05)

    progress_bar.empty()
    status_text.success("Animation completed!")
