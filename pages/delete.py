import streamlit as st
import pugsql
import os
import pandas as pd
import time
from dotenv import load_dotenv


def show_page():
    load_dotenv()

    queries = pugsql.module('queries/')
    queries.connect(os.getenv('DATABASE_URL'))

    # st.title("Delete Skills")

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

    confirm = st.checkbox("I am sure I want to delete these skills", key="confirm_delete")

    if st.button("Delete Selected"):
        if confirm:
            if not selected:
                st.warning("Please select at least one skill to delete.")
            else:
                try:
                    deleted_names = []
                    for name in selected:
                        skill_id = skill_map[name]["id"]
                        queries.delete_skill(id=skill_id)
                        deleted_names.append(name)
                    st.cache_data.clear()

                    names_str = ", ".join(deleted_names)
                    st.success(f"Successfully deleted: {names_str}")
                    time.sleep(2)
                    st.rerun()
                except Exception as e:
                    st.error(f"Failed to delete skills. Error: {e}")
        else:
            st.warning("You must confirm by checking the box before deleting")