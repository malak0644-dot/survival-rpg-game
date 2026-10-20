import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة وعنوان المنصة
st.set_page_config(page_title="Nexus AI - منصة الذكاء الاصطناعي", page_icon="⚡", layout="wide")

# قراءة واستدعاء ملف HTML الخاص بالتطبيق المعروض
with open("game.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# عرض التطبيق داخل منصة Streamlit
components.html(html_code, height=900, scrolling=True)
