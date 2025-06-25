###############################################
# Gabriel NAVENNEC - 06/05/2025               #
# SYMBHI - FRANCE DIGUE - IUGA                #
#                                             #
# Version 1.0                                 #
###############################################

# python -m streamlit run "C:\Users\Gabriel.NAVENNEC\Symbhi\Site Pôle Ouvrage - Documents\SIRS\Stages\2025_04_Gabriel_NAVENNEC\projet_alpha\application\streamlit_app.py"

import utils.read_files as rf
import streamlit as st

from st_pages import add_page_title, get_nav_from_toml

st.set_page_config(
    page_title="Home page",
    page_icon="👋",
    layout="wide")
