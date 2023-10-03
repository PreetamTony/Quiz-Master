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

st.markdown("<style>description {color: Green;}</style>",unsafe_allow_html = True)
st.title("Welcome to the Quiz Master!")
st.markdown("---")
st.sidebar.title("Choose one of the following category of Quiz:")