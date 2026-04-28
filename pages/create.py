import streamlit as st
import pugsql
import os
from dotenv import load_dotenv
from utils.embedding import getEmbedding

load_dotenv()

db = pugsql.module('queries/')
db.connect(os.getenv('DATABASE_URL'))

st.title("Create Skill")
name = st.text_input("Name (required)")
desc = st.text_area("Description (required)")
when = st.text_area("When to use (required)")
queries = st.text_area("Example to queries")
tags = st.text_area("Tags")
tools = st.text_area("Tools")
instr = st.text_area("Instructions")
embedding = st.text_area("Embedding")

if st.button("Create"):
    db.create_skill(
        name=name,
        description=desc,
        when_to_use=when,
        example_queries=queries,
        tags=tags,
        tools=tools,
        instructions=instr,
        embedding=None
    );

    st.success("Skill Created!")
    st.rerun()