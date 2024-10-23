import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide",
    page_title="FIFA23 Players"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club_sidebar = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[ (df_data["Club"] == club_sidebar) ]

players = df_players["Name"].value_counts().index
player_sidebar = st.sidebar.selectbox("Jogador", players)

player_stats = df_data[df_data["Name"] == player_sidebar].iloc[0]

st.image(player_stats["Photo"])
st.title(player_stats["Name"])

st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posiçao:** {player_stats['Position']}")

left, middle, right = st.columns(3)
left.markdown(f"**Idade:** {player_stats['Age']}")
middle.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")
right.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}")
st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

# Métricas
left, middle, right = st.columns(3)
left.metric(label="Valor de Mercado", value=f"£ {player_stats['Value(£)']:,}")
middle.metric(label="Remuneração Semanal", value=f"£ {player_stats['Wage(£)']:,}")
right.metric(label="Cláusula de Rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")