import streamlit as st
import pandas as pd
from pages import create, all_skills, delete, update

# Konfigurasi Halaman
st.set_page_config(page_title="Skill Manager", page_icon="🤖")

# --- SIDEBAR SIMPEL ---
with st.sidebar:
    st.title("🤖 Agent Skill")
    
    # Navigasi Utama
    menu = st.selectbox(
        "Pilih Menu:",
        ["All Skills", "Create Skill", "Update Skill", "Delete Skill"]
    )

# --- KONTEN UTAMA ---
if menu == "All Skills":
    st.header("🚀 All Skills")
    st.write("All your current AI skills")
    all_skills.show_page()

elif menu == "Create Skill":
    st.header("➕ Create New Skill")
    create.show_page()
    
elif menu == "Update Skill":
    st.header("🗘 Update Skill")
    st.write("Update Your Skill AI")
    update.show_page()

elif menu == "Delete Skill":
    st.header("❌ Delete Skill")
    st.write("Delete your skill")
    delete.show_page()