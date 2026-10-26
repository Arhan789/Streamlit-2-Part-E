import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋"
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown("""
Streamlit is an open-source app framework built for
Machine Learning and Data Science projects.

**Select a demo from the sidebar** to explore the app.

### Available demonstrations
- Plotting Demo
- Mapping Demo
- DataFrame Demo

### Learn more
Visit the [Streamlit documentation](https://docs.streamlit.io).
""")
