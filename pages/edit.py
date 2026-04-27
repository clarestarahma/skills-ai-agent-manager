import pugsql
from dotenv import load_dotenv
import os
import streamlit as st
import uuid
import pandas as pd

load_dotenv()

queries = pugsql.module('queries/')
queries.connect(os.getenv('DATABASE_URL'))

st.title("Edit Skills")

data = queries.get_all_skills_data().mappings().all()
df = pd.DataFrame(data)

# ======================
# 1. DATAFRAME VIEW ONLY
# ======================
st.divider()
st.subheader("All Skills")

st.dataframe(df, width="stretch")

# ======================
# 2. SELECTBOX (SOURCE OF TRUTH)
# ======================
skill_names = df["name"].tolist()

selected_name = st.selectbox("Pilih Skill", skill_names)

skill = df[df["name"] == selected_name].iloc[0]

# ======================
# 3. EDIT FORM
# ======================
st.subheader("Edit Skill")
name = st.text_input("Name", value=skill["name"])
desc = st.text_area("Description", value=skill["description"])
when = st.text_area("When to use", value=skill["when_to_use"])
instr = st.text_area("Instructions", value=skill["instructions"])
tag = st.text_area("Tag", value=skill.get('tag'))
tool = st.text_area("Tool", value=skill.get("tool"))
query = st.text_area("Query", value=skill.get("query"))

if st.button("Update"):

    if name != skill["name"]:
        queries.update_skill_name(id=skill['id'], name=name)

    if desc != skill["description"]:
        queries.update_skill_description(id=skill['id'], description=desc)

    if when != skill["when_to_use"]:
        queries.update_skill_when_to_use(id=skill['id'], when_to_use=when)

    if instr != skill["instructions"]:
        queries.update_skill_instructions(id=skill['id'], instructions=instr)

    if tag != skill.get("tag"):
        if skill.get("tag") is None or skill.get("tag") == "":
            queries.create_skill_tags(skill_id=skill['id'], tag=tag)
            st.write(f"Mencoba insert tag : {tag} untuk ID: {skill['id']}")
        else:
            queries.update_skill_tags_tag(skill_id=skill['id'], tag=tag)
            st.write(f"Mencoba update tag jadi: {tag} untuk ID: {skill['id']}")

    if tool != skill.get("tool"):
        if skill.get("tool") is None or skill.get("tool") == "":
            queries.create_skill_tools(skill_id=skill['id'], tool=tool)
            st.write(f"Mencoba insert tool : {tool} untuk ID: {skill['id']}")
        else:
            queries.update_skill_tools_tool(skill_id=skill['id'], tool=tool)
            st.write(f"Mencoba update tool jadi: {tool} untuk ID: {skill['id']}")

    if query != skill.get("query"):
        if skill.get("query") is None or skill.get("query") == "":
            st.write(f"Mencoba insert query : {query} untuk ID: {skill['id']}")
            queries.create_skill_example_queries(skill_id=skill['id'], query=query)
        else:
            queries.update_skill_example_queries_query(skill_id=skill['id'], query=query)
            st.write(f"Mencoba update query jadi: {query} untuk ID: {skill['id']}")

    st.cache_data.clear()
    st.success("Updated!")
    st.rerun()