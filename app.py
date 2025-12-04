import streamlit as st

home_page = st.Page("home.py", title="About", url_path="home")
design2_page = st.Page("design2.py", title="Design 2", url_path="design2")


pages = [home_page, design2_page]

current_page = st.navigation(pages=pages, position="hidden")

st.set_page_config(layout="wide")
st.title("🏡 House & Browse")
num_cols = len(pages) + 1

columns = st.columns(num_cols, vertical_alignment="bottom")

for col, page in zip(columns[1:], pages):
    col.page_link(page)

current_page.run()