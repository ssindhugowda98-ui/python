# =========================================
# Company Management App
# company_app.py
# =========================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from datetime import date, datetime
import random

# -----------------------------------------
# Page Config
# -----------------------------------------

st.set_page_config(
    page_title="NexaCorp | Company Portal",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------
# Custom CSS
# -----------------------------------------

st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background: #0f172a;…
