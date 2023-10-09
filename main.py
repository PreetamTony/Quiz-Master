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
        category_dict[item['name']] = item['id']
    return category_dict

def get_question(amount,category,difficulty):
    questions = rq.get("https://opentdb.com/api.php?amount="+str(amount)+"&category="+str(category)+"&difficulty="+str(difficulty)).json()
    return questions


st.markdown("<style>description {color: Green;}</style>",unsafe_allow_html = True)
st.title(":orange[Welcome to the] :violet[QuizMaster!]")
st.subheader("_Engage, Entertain, and Educate with QuizMaster - Where Knowledge Meets Fun!_", divider= 'rainbow')
# st.markdown("---")
st.sidebar.title("Tune the Options to Play the Game")
st.sidebar.markdown("---")
categories_option = get_category()
category = st.sidebar.selectbox("Category: ", list(categories_option.keys()), index= None, placeholder= "Select one: ")
if category is None:
    st.warning('Please select one category to start the game', icon="⚠️")
else:
    levels = st.sidebar.selectbox("Difficulty Level: ", ['Easy', 'Medium', 'Hard'])
    QuestionCount = st.sidebar.slider("Number of Question Per Game:", 1, 10, 1)
    # TypeOption = st.sidebar.selectbox("Type of Questions", ['Any','True/False', "MCQ"])
    # if TypeOption == 'True/False':
    #     TypeOption = 'boolean'
    # else:
    #     TypeOption = 'multiple'
    QuestionList = get_question(QuestionCount,categories_option[category], levels.lower())
    st.write(QuestionList)

