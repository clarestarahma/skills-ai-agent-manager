import streamlit as st
import pugsql
import os
from dotenv import load_dotenv
from utils.embedding import getEmbeddingOpenAI
from utils.clean_list import clean_for_display
from utils.list import get_list
import time
from models.skills import Skill

def show_page():
    load_dotenv()

    db = pugsql.module('queries/')
    db.connect(os.getenv('DATABASE_URL'))

    # st.title("Create Skill")
    name = st.text_input("Name")
    desc = st.text_area("Description")
    when = st.text_area("When to use")
    queries = st.text_area("Example to queries")
    tags = st.text_area("Tags")
    tools = st.text_area("Tools")

    all_fields = [name, desc, when, queries, tags, tools]

    message_placeholder = st.empty()

    if st.button("Create"):
        if all(f.strip() for f in all_fields):
            try:
                skill = Skill(
                    name=name.strip(),
                    description=desc.strip(),
                    when_to_use=when.strip(),
                    example_queries=get_list(queries.strip()),
                    tags=get_list(tags.strip())
                )
                db.create_skill(
                    **skill.dump(),
                    tools=tools.strip(),
                    embedding=getEmbeddingOpenAI(skill.summary)
                );

                message_placeholder.success(f"""
                    Skill Created Successfully!
                    
                    \tDetails:\n
                    \t -> Name: {name.strip()}
                    \t -> Description: {desc.strip()[:50]}...
                    \t -> When to use: {when.strip()[:50]}...
                    \t -> Example Queries: {clean_for_display(queries.strip())}
                    \t -> Tags: {clean_for_display(tags.strip())}
                    \t -> Tools: {clean_for_display(tools.strip())}
                """)

                time.sleep(5)
                st.rerun()
            except Exception as e:
                message_placeholder.error(f"An error occured: {e}")
        else:
            message_placeholder.warning("All fields are required! Please ensure no boxes are left empty.")