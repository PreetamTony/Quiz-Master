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
import random

def get_category():
    category_dict = dict()
    category_json_list = rq.get("https://opentdb.com/api_category.php").json()
    for item in category_json_list['trivia_categories']:
        category_dict[item['name']] = item['id']
    return category_dict

@st.cache_data
def get_question(category,difficulty):
    questions = rq.get("https://opentdb.com/api.php?amount=10"+"&category="+str(category)+"&difficulty="+str(difficulty)).json()["results"]
    return questions

def initialize_session_state():
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'player_score' not in st.session_state:
        st.session_state.player_score = 0

def update_score(player_choice, correct_answer):
    if str(player_choice) == str(correct_answer):
        st.session_state.player_score += 1

if "submit_key" in st.session_state and st.session_state.submit_key == True:
    st.session_state.running = True
else:
    st.session_state.running = False


st.markdown("<style>description {color: Green;}</style>",unsafe_allow_html = True)
st.title(":orange[Welcome to the] :violet[QuizMaster!]")
st.subheader("_Engage, Entertain, and Educate with QuizMaster - Where Knowledge Meets Fun!_", divider= 'rainbow')
st.sidebar.title("Tune the Options to Play the Game")
st.sidebar.markdown("---")
initialize_session_state()

def calculate_score(player_choice):
    correct_answer = quiz_questions[st.session_state.current_question]["answer"]
    # st.write("inside calculate_score" + str(correct_answer))
    update_score(player_choice, correct_answer)
    st.session_state.current_question += 1

categories_option = get_category()
category = st.sidebar.selectbox("Category: ", list(categories_option.keys()), index= None, placeholder= "Select one: ")
if category is None:
    st.warning('Please select one category to start the game', icon="⚠️")
else:
    levels = st.sidebar.selectbox("Difficulty Level: ", ['Easy', 'Medium', 'Hard'])
    QuestionList = get_question(categories_option[category], levels.lower())
    # st.write(QuestionList)
    len_response = len(QuestionList)
    quiz_questions = []
    for item in range(len_response):
        temp_dict = dict()
        temp_dict['text'] = QuestionList[item].get("question")
        temp_dict['options'] = tuple(QuestionList[item].get("incorrect_answers") + [QuestionList[item].get("correct_answer")])
        temp_dict['answer'] = QuestionList[item].get("correct_answer")
        quiz_questions.append(temp_dict)

    ind = st.session_state.current_question
    # st.write(quiz_questions[st.session_state.current_question]["answer"])
    current_question = quiz_questions[ind]
    st.subheader(quiz_questions[ind]["text"])
    player_choice = st.radio("Select your answer:",
                                 options=current_question["options"],
                                 key=f"question_{ind}")
    if st.button("Submit", key="submit_key", disabled=(st.session_state.running)):
        calculate_score(player_choice)
        st.write(st.session_state.player_score)
        if st.session_state.current_question < len(quiz_questions):
            st.rerun()  
        if st.session_state.current_question >= len(quiz_questions):
            st.success("Quiz Finished!")
            st.write(f"Your Score: {st.session_state.player_score}")
