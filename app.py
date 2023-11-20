import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

st.header('Streamlit Homework lkona')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)


x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(0, x_limit,1)

# Create a random array of data that we will use for our y values
y_data = [random.random() for value in x_axis]

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)



st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)


scatter = alt.Chart(df).mark_point().encode(
    x='x',
    y='y'
)

st.altair_chart(scatter, use_container_width=True)


st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)
st.markdown("\n \n")
st.markdown("The five changes I made were.....")
st.markdown("""
The 5 changes I made were:
- Change 1 : Tooltip added
- Change 2 : X and Y axis labels
- Change 3 : Chart Title, theme
- Change 4 : circle size, opacity, fill, color
- Change 5 : Background
""")
st.markdown("\n \n")
st.markdown("\n \n")
st.markdown("\n \n")
st.markdown("\n \n")

scatter = alt.Chart(df).mark_point(size=150, opacity=0.8, fill='magenta', color='yellow').encode(
    alt.X('x', title = "New X-axis title"),
    alt.Y('y', title = "New Y-axis title"),
    tooltip = ['x','y']
).properties(title="New Chart Title",background='#D9E9F0')

st.altair_chart(scatter, theme="streamlit", use_container_width=True)

st.markdown("\n \n")
st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)

st.markdown("""
The 2 changes I made were:
- Change 1: Chart title, Background
- Change 2: X and Y labels
"""
)

st.markdown("\n \n")
st.markdown("\n \n")

# Generating Data
source = pd.DataFrame({
    'Trial A': np.random.normal(0, 0.8, 1000),
    'Trial B': np.random.normal(-2, 1, 1000),
    'Trial C': np.random.normal(3, 2, 1000)
})

bar = alt.Chart(source).transform_fold(
    ['Trial A', 'Trial B', 'Trial C'],
    as_=['Experiment', 'Measurement']
).mark_bar(
    opacity=0.3,
    binSpacing=0
).encode(
    alt.X('Measurement:Q', title ="Measurement").bin(maxbins=100),
    alt.Y('count()', title ="Records").stack(None),
    alt.Color('Experiment:N')
).properties(title="Layered Histogram",background='#D9E9F0')

st.altair_chart(bar, use_container_width=True)
