import streamlit as st
import numpy as np
import pandas as pd

df = pd.read_csv("top_500.csv")
doc_sim_df = pd.read_csv("similarity.csv")

games_list = df['Title'].values
description_list = df['Game Description'].values


def game_recommender(game_title, games=games_list, descriptions=description_list, doc_sims=doc_sim_df):
    # find game id
    game_idx = np.where(games == game_title)[0][0]
    # get game similarities
    game_similarities = doc_sims.iloc[game_idx].values
    # get top 5 similar game IDs
    similar_game_idxs = np.argsort(-game_similarities)[1:6]
    # get top 5 games
    similar_games = games[similar_game_idxs]
    # get top 5 games description
    similar_description = descriptions[similar_game_idxs]
    # Create a DataFrame with game titles and descriptions
    similar_games_df = pd.DataFrame({
        'Title': similar_games,
        'Description': similar_description
    })

    return similar_games_df


st.set_page_config(page_title = 'Rekomendasi Video Game - Ilham Triza Kurniawan', layout = 'wide')

st.title('Sistem Rekomendasi Video Game 🎮')
st.header("Menggunakan Algoritma TF-IDF dan Cosine Similarity", divider = "violet")
margin_left, col_left, margin_mid, col_right, margin_right = st.columns([0.2,5,1,5,0.2])

user_input = col_left.text_input(
    "Judul Video Game",
    placeholder = 'Masukkan Judul Video Game yang diinginkan'
    )
#user_input = user_input.lower()

if 'output' not in st.session_state:
    st.session_state.output = ''

def btn_action(): 
    try:
        st.session_state.output = game_recommender(user_input.lower(),games_list,description_list, doc_sim_df)
    except:
        st.session_state.output = "Video Game tidak dapat ditemukan"


col_left.button('Submit',on_click=btn_action)
col_right.write(st.session_state.output)
