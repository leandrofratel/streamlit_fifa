import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide",
    page_title="FIFA23 Teams"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club_sidebar = st.sidebar.selectbox("Clube", clubes)

df_filtered = df_data[df_data["Club"] == club_sidebar].set_index("Name")

st.image(df_filtered.iloc[0] ["Club Logo"])
st.markdown(f"## {club_sidebar}")

columns = [
    "Age", "Photo", "Flag", "Overall",
    "Value(£)", "Wage(£)", "Joined",
    "Height(cm.)", "Weight(lbs.)", "Contract Valid Until",
    "Release Clause(£)"
]


st.dataframe(
    df_filtered[columns],
    column_config={
        "Overall": st.column_config.ProgressColumn("Overall", min_value=0, max_value=100, format="%d"),
        "Photo": st.column_config.ImageColumn("Photo"),
        "Flag": st.column_config.ImageColumn("Country"),
        "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f",min_value=0, max_value=df_filtered["Wage(£)"].max())
    }
)