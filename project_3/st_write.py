import streamlit as st

import pandas as pd

# Displaying data on the screen
# 1. st.wrtie()
# 2. magic

st.write('Hello World')
st.write(1234)
st.write(
        pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )
)

'Display using magic :smile:'