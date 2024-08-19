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
st.markdown("**use this Penguins App to make your own Penguins scatterplot** ")

#select box for choosing species
#selected_species = st.selectbox("What specie would you like to Visualize? ",
                                #['Adelie', 'Gentoo', 'Chinstrap'])

#select box for X and  Y axes
selected_x_var = st.selectbox('What do you want the x variable to be?',
                              ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
                              

selected_y_var = st.selectbox('What about the y?',
                              ['bill_depth_mm', 'bill_length_mm', 'flipper_length_mm'])

#Extracting the table
#df = df[df['species'] == selected_species]

#Visualization
alt_chart = (
    alt.Chart(df)
    .mark_circle()
    .encode(
    x=selected_x_var,
    y=selected_y_var,
    color = "Species"
    )
    .interactive()

)
st.altair_chart(alt_chart, use_container_width=True)