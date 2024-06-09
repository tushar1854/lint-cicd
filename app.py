import streamlit as st
import pandas as pd
import numpy as np
import requests
import time
from api_conf import subfeddits_api, comments_api
from utils import process_comments, convert_dict2list

st.set_page_config(page_title="Feddit-All About Everything")
st.title("feddit insights")

with st.form("input_form"):
    col1, col2, col3 = st.columns([3,3,1])

    with col1:
        subfeddit_name = st.text_input("SubFeddit Name", placeholder = "f/games")

    with col2:
        limit = st.number_input("No. of Comments", value = 25, step = 1)

    with col3:

        st.markdown("""
        <style>
        .big-font {
            font-size:0.0000001px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<p class="big-font">Hello World !!</p>', unsafe_allow_html=True)
        submit_button =  st.form_submit_button(label="Submit")
        
if submit_button:
    progress_bar = st.progress(25, 'Fetching subfeddit data')
    time.sleep(0.5)
    response = requests.get(url=subfeddits_api)
    response = response.json()
    subfeddit_id = None
    for subfeddit in response['subfeddits']:
        if subfeddit['title'] == subfeddit_name:
            subfeddit_id = subfeddit['id']
            break
    if not subfeddit_id:
        st.error("sufeddit not found")
        progress_bar.empty()
    else:
        progress_bar.progress(50, 'Fetching comments')
        time.sleep(0.5)
        params = {'subfeddit_id': subfeddit_id, 'limit': limit}
        response = requests.get(comments_api, params)
        response = response.json()
        comments = response['comments']
        progress_bar.progress(75, 'Analyzing comments')
        comments_list = process_comments(comments)
        df = convert_dict2list(comments_list)
        progress_bar.progress(100, 'Analysis done')
        progress_bar.empty()
        st.dataframe(df, width=1000)