#-------------------------------------------------------------------------------------#
# File: Chat.py
# Description: Main application entry point and process manager
# Author: @hams_ollo
# Version: 0.0.3
# Last Updated: [2024-11-21]
#-------------------------------------------------------------------------------------#
# SETUP GUIDE:  streamlit run .\frontend\Chat.py 
#
# Initial Setup:
# 1. Create virtual environment  -> python -m venv venv
# 2. Activate virtual environment:
#    - Windows                   -> .\venv\Scripts\activate
#    - Unix/MacOS               -> source venv/bin/activate
# 3. Install requirements       -> pip install -r requirements.txt
# 4. Copy environment file      -> cp .env.example .env
# 5. Add your Groq API key to .env
#
# Running the Application:
# 1. Start the application      -> python main.py     /     streamlit run main.py
# 2. Access the web interface   -> http://localhost:8501
# 3. Stop the application      -> Ctrl+C
# 4. Deactivate virtual env    -> deactivate
#
# Development Commands:
# 1. Update dependencies       -> pip freeze > requirements.txt
# 2. Run with debug logging   -> python main.py --log-level=debug
# 3. Clear Streamlit cache    -> streamlit cache clear
#
# Git Quick Reference:
# 1. Initialize repository    -> git init
# 2. Add files to staging    -> git add .
# 3. Commit changes         -> git commit -m "your message"
# 4. Create new branch      -> git checkout -b branch-name
# 5. Switch branches        -> git checkout branch-name
# 6. Push to remote         -> git push -u origin branch-name
# 7. Pull latest changes    -> git pull origin branch-name
# 8. Check status          -> git status
# 9. View commit history   -> git log
#
#-------------------------------------------------------------------------------------#

"""
Main entry point for Streamlit Cloud deployment
"""
import os
import sys
from pathlib import Path
import logging

import streamlit as st

# Configure logging
logging.basicConfig(level=logging.INFO)

# Set page configuration at the very beginning
st.set_page_config(
    page_title="Dynamic AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

# Import after st.set_page_config
from app.core.sqlite_setup import setup_sqlite
from frontend.Chat import display_chat_interface

def init_session_state():
    """Initialize session state variables."""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

def main():
    """Main function to run the Streamlit application."""
    # Initialize SQLite for ChromaDB
    setup_sqlite()
    
    # Initialize session state
    init_session_state()
    
    # Set the app title in sidebar
    st.sidebar.markdown("# 💬 AI Chat Assistant")

    # Display the chat interface
    display_chat_interface()

if __name__ == "__main__":
    main()
