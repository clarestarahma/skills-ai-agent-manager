import pugsql
from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from utils.list_to_string import format_list_to_string

load_dotenv()

db = pugsql.module('queries/')
db.connect(os.getenv('DATABASE_URL'))

st.title("Edit Skills")

data = db.get_all_skills_data().mappings().all()
df = pd.DataFrame(data)

# ======================
# 1. DATAFRAME VIEW ONLY
# ======================
st.subheader("All Skills")

st.dataframe(df, width="stretch")

# ======================
# 2. SELECTBOX (SOURCE OF TRUTH)
# ======================
if not df.empty:
    skill_names = df["name"].tolist()

    selected_name = st.selectbox("Pilih Skill", skill_names)

    skill = df[df["name"] == selected_name].iloc[0]

    # ======================
    # 3. EDIT FORM
    # ======================
    st.subheader("Edit Skill")
    name = st.text_input("Name", placeholder=skill.get("name"))
    desc = st.text_area("Description", placeholder=skill.get("description"))
    when = st.text_area("When to use", placeholder=skill.get("when_to_use"))
    queries = st.text_area("Example to queries", placeholder=format_list_to_string(skill.get("example_queries")))
    tags = st.text_area("Tags", placeholder=format_list_to_string(skill.get('tags')))
    tools = st.text_area("Tools", placeholder=format_list_to_string(skill.get("tools")))
    instr = st.text_area("Instructions", placeholder=skill.get("instructions"))
    embedding = st.text_area("Embedding", placeholder=skill.get("embedding"))

    if st.button("Update"):

        if name != skill["name"]:
            db.update_skills_name(id=skill['id'], name=name)

        if desc != skill["description"]:
            db.update_skills_description(id=skill['id'], description=desc)

        if when != skill["when_to_use"]:
            db.update_skills_when_to_use(id=skill['id'], when_to_use=when)

        if queries != format_list_to_string(skill['example_queries']):
            db.update_skills_example_queries(id=skill['id'], example_queries=queries)

        if tags != format_list_to_string(skill["tags"]):
            db.update_skills_tags(id=skill['id'], tags=tags)

        if tags != format_list_to_string(skill["tools"]):
            queries.update_skills_tools(id=skill['id'], tools=tools)

        if instr != skill["instructions"]:
            db.update_skills_instructions(id=skill['id'], instructions=instr)

        if embedding != skill["embedding"]:
            db.update_skills_instructions(id=skill['id'], embedding=embedding)

        st.cache_data.clear()
        st.success("Updated!")
        st.rerun()