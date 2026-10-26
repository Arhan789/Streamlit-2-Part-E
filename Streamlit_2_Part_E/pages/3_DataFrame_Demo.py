import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="DataFrame Demo",
    page_icon="📊"
)

st.title("DataFrame Demo")
st.sidebar.header("DataFrame Demo")

st.write("Explore tabular data and interactive visualisations.")

df = pd.DataFrame({
    "Year": [2021, 2022, 2023, 2024, 2025],
    "Sydney": [120, 135, 150, 165, 180],
    "Melbourne": [110, 125, 145, 160, 175],
    "Brisbane": [80, 95, 110, 130, 150]
})

cities = st.multiselect(
    "Choose cities",
    ["Sydney", "Melbourne", "Brisbane"],
    default=["Sydney", "Melbourne"]
)

st.dataframe(df[["Year"] + cities], hide_index=True)

if cities:
    chart_data = df.melt(
        id_vars="Year",
        value_vars=cities,
        var_name="City",
        value_name="Value"
    )

    chart = alt.Chart(chart_data).mark_line(point=True).encode(
        x=alt.X("Year:O"),
        y=alt.Y("Value:Q"),
        color="City:N",
        tooltip=["Year", "City", "Value"]
    )

    st.altair_chart(chart, use_container_width=True)
else:
    st.warning("Select at least one city.")
