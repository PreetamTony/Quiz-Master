import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import json as js
import requests as rq
import time
from datetime import datetime, timedelta
import altair as alt

def get_category():
    category_dict = dict()
    category_json_list = rq.get("https://opentdb.com/api_category.php").json()
    for item in category_json_list['trivia_categories']:
        category_dict[item['id']] = item['name']
    return category_dict



st.markdown("<style>description {color: Green;}</style>",unsafe_allow_html = True)
st.title(":orange[Welcome to the] :violet[QuizMaster!]")
st.subheader("_Engage, Entertain, and Educate with QuizMaster - Where Knowledge Meets Fun!_", divider= 'rainbow')
# st.markdown("---")
st.sidebar.title("Tune the Options to Play the Game")
st.sidebar.markdown("---")
categories_option = get_category()
category = st.sidebar.selectbox("Category: ", list(categories_option.values()), index= None, placeholder= "Select one: ")
if category is None:
    st.warning('Please select one category to start the game', icon="⚠️")
else:
    levels = st.sidebar.selectbox("Difficulty Level: ", ['Easy', 'Medium', 'Hard'])
    QuestionCount = st.sidebar.slider("Number of Question Per Game:", 1, 50, 1)
    TypeOption = st.sidebar.selectbox("Type of Questions", ['True/False', "MCQ"])
    if TypeOption == 'True/False':
        TypeOption = 'boolean'
    else:
        TypeOption = 'multiple'
    

