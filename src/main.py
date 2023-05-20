import streamlit as st
import pickle,json
import pandas as pd
from utils.utils import *

st.title("Product Similarity Search")
# Get the input text
text = st.text_input("Enter a description of a clothing item:")

# Get the top 5 similar items
similar_items = get_similar_items(text, 10)

# Display the results
st.table(similar_items)
