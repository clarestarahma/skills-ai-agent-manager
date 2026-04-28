import streamlit as st
import pugsql
import os

st.title("All Skills")

queries = pugsql.module('queries/')
queries.connect(os.getenv('DATABASE_URL'))

skills = queries.get_all_skills_data().mappings().all()
st.dataframe(skills, width="stretch")