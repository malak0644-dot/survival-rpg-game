import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="لعبة البقاء والقرار المصيري", page_icon="🎮", layout="wide")

with open("game.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=850, scrolling=True)
