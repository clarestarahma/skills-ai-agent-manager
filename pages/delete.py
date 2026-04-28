import streamlit as st
import pugsql
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

queries = pugsql.module('queries/')
queries.connect(os.getenv('DATABASE_URL'))

st.title("Delete Skills")

skills = queries.get_all_skills_data().mappings().all()
df = pd.DataFrame(skills)

# ======================
# 1. DATAFRAME VIEW ONLY
# ======================
st.subheader("All Skills")

st.dataframe(df, width="stretch")

skill_map = {s["name"]: s for s in skills}
names = list(skill_map.keys())

selected = st.multiselect("Pilih skill yang mau dihapus", names)

if selected:
    st.write("Akan dihapus:")
    for name in selected:
        st.write("•", name)

if st.button("Delete Selected"):
    for name in selected:
        skill_id = skill_map[name]["id"]
        queries.delete_skill(id=skill_id)

    st.success("Deleted!")
    st.rerun()