import streamlit as st
import numpy as np
import pandas as pd

df = pd.read_csv("top_500.csv")
doc_sim_df = pd.read_csv("similarity.csv")

games_list = df['Title'].values


def game_recommender(game_title, games=games_list, doc_sims=doc_sim_df):
    # find game id
    game_idx = np.where(games == game_title)[0][0]
    # get game similarities
    game_similarities = doc_sims.iloc[game_idx].values
    # get top 5 similar game IDs
    similar_game_idxs = np.argsort(-game_similarities)[1:6]
    # get top 5 games
    similar_games = games[similar_game_idxs]
    # return the top 5 games
    return similar_games



st.title('Sistem Rekomendasi Video Game 🎮')
st.header("Menggunakan Algoritma TF-IDF dan Cosine Similarity", divider = "blue")

user_input = st.text_input(
    "Judul Video Game",
    placeholder = 'Masukkan Judul Video Game yang diinginkan'
    )
#user_input = user_input.lower()

if 'output' not in st.session_state:
    st.session_state.output = ''

def btn_action(): 
    try:
        st.session_state.output = game_recommender(user_input.lower(),games_list, doc_sim_df)
    except:
        st.session_state.output = "Video Game tidak dapat ditemukan"


st.button('Submit',on_click=btn_action)
st.write(st.session_state.output)
