import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

st.set_page_config(
    layout="wide",
    page_title="FIFA23 Streamlit"
)

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets\CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[ df_data["Contract Valid Until"] >= datetime.today().year ]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data


st.markdown("# FIFA23 OFFICIAL DATASET")
st.sidebar.markdown("Desenvolvido por [Leandro Fratel](https://www.linkedin.com/in/leandrofratel/)")

btn = st.button("Acesse os dados do Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database")

st.markdown(
    """
    O conjunto de dados da FIFA no Kaggle contém informações detalhadas sobre jogadores de futebol, como nome, idade, nacionalidade, 
    clube e posição. Além disso, traz estatísticas de desempenho, como habilidades de passe, chute e defesa, além de características físicas.

    Esses dados são amplamente usados em projetos de análise e machine learning, permitindo criar visualizações, 
    fazer previsões e descobrir padrões sobre o desempenho dos jogadores em campo.
    """
)