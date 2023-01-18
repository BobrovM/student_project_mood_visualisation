import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import glob
from datetime import datetime
import plotly.express as px


paths = glob.glob("fake_diary/*.txt")

pos_scores, neg_scores = [], []
dates = []
for path in paths:
    with open(path, "r") as file:
        text = file.read()
        analyzer = SentimentIntensityAnalyzer()
        scores = analyzer.polarity_scores(text)
    path = path.strip(".txt")
    path = path.strip("fake_diary\\")
    date = datetime.strptime(path, "%Y-%m-%d").date()
    dates.append(date.strftime("%b %d %Y"))
    pos_scores.append(scores["pos"])
    neg_scores.append(scores["neg"])

st.set_page_config(layout="wide")

st.title("Diary Tone")

st.header("Positivity")
figure = px.line(x=dates, y=pos_scores, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure)

st.header("Negativity")
figure = px.line(x=dates, y=neg_scores, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure)