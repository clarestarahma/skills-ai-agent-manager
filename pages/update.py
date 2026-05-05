from dotenv import load_dotenv
from utils.list_to_string import format_list_for_forms
from utils.embedding import getEmbeddingOpenAI
from models.skills import Skill
from utils.list import get_list

import time
import pugsql
import os
import streamlit as st
import pandas as pd


def show_page():
    load_dotenv()

    db = pugsql.module('queries/')
    db.connect(os.getenv('DATABASE_URL'))

    # st.title("Edit Skills")

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
        queries = st.text_area("Add More example queries", help="use two enter to separate between query", value=format_list_for_forms(skill.get("example_queries")))
        tags = st.text_area("Add More Tags", help="use two enter to separate between tag", value=format_list_for_forms(skill.get('tags')))
        tools = st.text_area("Add More Tools", help="use two enter to separate between tool", value=format_list_for_forms(skill.get("tools")))

        if st.button("Update"):
            try:
                changes = []
                #  name
                if name and name.strip() != skill["name"]:
                    db.update_skills_name(id=skill['id'], name=name.strip())
                    changes.append("name")

                #  description
                if desc and desc.strip() != skill["description"]:
                    db.update_skills_description(id=skill['id'], description=desc.strip())
                    changes.append("desc")

                #  when to use
                if when and when.strip() != skill["when_to_use"]:
                    # db.update_skills_when_to_use(id=skill['id'], when_to_use=when.strip())
                    changes.append("when to use")

                # example queries
                db_queries = skill.get("example_queries") or []
                queries_list = get_list(queries.strip())
                if queries.strip() and set(queries_list) != set(db_queries):
                    db.update_skills_example_queries(id=skill['id'], example_queries=queries.strip())
                    changes.append("example_queries")

                # tags
                db_tags = skill.get("tags") or []
                tags_list = get_list(tags.strip())
                if tags.strip() and set(tags_list) != set(db_tags):
                    db.update_skills_tags(id=skill['id'], tags=tags.strip())
                    changes.append("tags")

                # tools
                db_tools = skill.get("tools") or []
                tools_list = get_list(tools.strip())
                if queries.strip() and set(tools_list) != set(db_tools):
                    db.update_skills_tools(id=skill['id'], tools=tools.strip())
                    changes.append("tools")

                #  embedding
                if changes:
                    skill_obj = Skill(
                        name=name.strip(),
                        description=desc.strip(),
                        when_to_use=get_list(when.strip()),
                        example_queries=get_list(queries.strip()),
                        tags=get_list(tags)
                    )
                    vector_data = getEmbeddingOpenAI(skill_obj.summary)
                    if vector_data:
                        db.update_skills_embedding(id=skill['id'], embedding=vector_data)
                    changes.append("embedding")
                
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