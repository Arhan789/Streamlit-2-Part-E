import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(
    page_title="Mapping Demo",
    page_icon="🌍"
)

st.title("Mapping Demo")
st.sidebar.header("Mapping Demo")

st.write("Explore geographic locations using an interactive map.")

data = pd.DataFrame({
    "name": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "lat": [-33.8688, -37.8136, -27.4698, -31.9505],
    "lon": [151.2093, 144.9631, 153.0251, 115.8605]
})

cities = st.sidebar.multiselect(
    "Select cities",
    data["name"].tolist(),
    default=data["name"].tolist()
)

filtered = data[data["name"].isin(cities)]

if filtered.empty:
    st.warning("Please select at least one city.")
else:
    st.map(filtered, latitude="lat", longitude="lon")
    st.dataframe(filtered, hide_index=True)
