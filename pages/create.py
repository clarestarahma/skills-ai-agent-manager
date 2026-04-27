import streamlit as st
import pugsql
import os
from dotenv import load_dotenv

load_dotenv()

queries = pugsql.module('queries/')
queries.connect(os.getenv('DATABASE_URL'))

st.title("Create Skill")

name = st.text_input("Name (required)")
desc = st.text_area("Description (required)")
meta = st.text_area("Metadata (required)")
when = st.text_area("When to use (required)")
instr = st.text_area("Instructions (required)")
tag = st.text_area("Tags")
tool = st.text_area("Tool")
query = st.text_area("Query")

if st.button("Create"):
    queries.create_skill(
        name=name,
        description=desc,
        metadata=meta,
        when_to_use=when,
        instructions=instr,
        embedding=None
    )

    if tag:
        queries.create_skill_tags(
            tag=tag
        )

    if tool:
        queries.create_skill_tools(
            tool=tool
        )

    if query:
        queries.create_skill_example_queries(
            query=query
        )

    st.success("Skill Created!")
    st.rerun()