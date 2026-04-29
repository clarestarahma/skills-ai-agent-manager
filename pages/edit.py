import pugsql
from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from utils.list_to_string import format_list_to_string
from utils.embedding import getEmbeddingOpenAI
import time

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
    name = st.text_input("Name", value=skill.get("name"))
    desc = st.text_area("Description", value=skill.get("description"))
    when = st.text_area("When to use", value=skill.get("when_to_use"))
    queries = st.text_area("Add More example queries", help="Gunakan Enter 2x untuk memisahkan antar tag", placeholder=format_list_to_string(skill.get("example_queries")))
    tags = st.text_area("Add More Tags", help="Gunakan Enter 2x untuk memisahkan antar tag", placeholder=format_list_to_string(skill.get('tags')))
    tools = st.text_area("Add More Tools", help="Gunakan Enter 2x untuk memisahkan antar tool", placeholder=format_list_to_string(skill.get("tools")))
    instr = st.text_area("Instructions", value=skill.get("instructions"))

    if st.button("Update"):
        try:
            changes = []

            #  name
            if name and name != skill["name"]:
                db.update_skills_name(id=skill['id'], name=name.strip())
                changes.append("name")

            #  description
            if desc and desc != skill["description"]:
                db.update_skills_description(id=skill['id'], description=desc.strip())
                changes.append("desc")

            #  when to use
            if when and when != skill["when_to_use"]:
                db.update_skills_when_to_use(id=skill['id'], when_to_use=when.strip())
                changes.append()

            # example queries
            if queries.strip():
                db.update_skills_example_queries(id=skill['id'], example_queries=queries.strip())
                changes.append("example_queries")

            # tags
            if tags.strip():
                db.update_skills_tags(id=skill['id'], tags=tags.strip())
                changes.append("tags")

            # tools
            if tools.strip():
                db.update_skills_tools(id=skill['id'], tools=tools.strip())
                changes.append("tools")

            #  Instruction and embedding
            if instr and instr != skill["instructions"]:
                clean_instr = instr.strip()
                db.update_skills_instructions(id=skill['id'], instructions=clean_instr)
                vector_data = getEmbeddingOpenAI(clean_instr)
                if vector_data:
                    db.update_skills_embedding(id=skill['id'], embedding=vector_data)
                changes.append("instructions")
            
            if changes:
                st.cache_data.clear()
                detail_changes = ", ".join(changes)
                st.success(f"Skill updated successfully: {detail_changes}")
                time.sleep(2)
                st.rerun()
            else:
                st.info("No changes detected")
        except Exception as e:
            st.error(f"Failed to update skill. Error: {e}")