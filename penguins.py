# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 09:51:05 2024

@author: SAIL
"""

import pandas as pd
import streamlit as st
import altair as alt
import seaborn as sns


st.title("Palmer's Penguins")

#Read the csv file using pandas library
df = pd.read_csv("penguins.csv")

#Have a glimpse of the dataset
st.write(df.head(10))