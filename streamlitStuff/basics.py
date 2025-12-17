import time

import numpy as np
import streamlit as st
import pandas as pd

# https://docs.streamlit.io/get-started/fundamentals/main-concepts

left_column, right_column = st.columns(2)

with left_column:

    df = pd.DataFrame({
      'first column': [1, 2, 3, 4],
      'second column': [10, 23, 14, 45]
    })

    st.write("Hello World! A basic Streamlit app.")
    st.write(df)

    st.write("st.table() is not interactive")
    st.table(df)

    st.write("st.dataframe() is interactive and stylable")
    st.dataframe(df.style.highlight_max(axis=0))

    st.write("Line Chart, every columne of df a line!")
    st.line_chart(df)

    option = st.selectbox(
        "Which number do you like best?",
        df['first column']
    )

with right_column:

    st.write("Area Chart, with lat/lon")
    map_points = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])
    st.map(map_points)

    x = st.slider("x")
    st.write(x, "squared is", x * x)

    if st.checkbox("Show dataframe"):
        chart_data = pd.DataFrame(
            np.random.randn(5, 3),
            columns=['a', 'b', 'c'])

        st.write(chart_data)


    st.write("You selected:", option)

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

st.write('Starting a long computation...')

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

st.write('...and now we\'re done!')