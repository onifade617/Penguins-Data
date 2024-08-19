# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 09:51:05 2024

@author: SAIL
"""

import pandas as pd
import streamlit as st
import altair as alt


st.title("Palmer's Penguins")

#Read the csv file using pandas library
df = pd.read_csv("penguins.csv")

#Have a glimpse of the dataset
st.write(df.head(10))

#This is an heading
st.markdown("use this Penguins App to make your own Penguins scatterplot ")

#select box
selected_species = st.selectbox("What specie would you like to Visualize? ",
                                ['Adelie', 'Gentoo', 'Chinstrap'])