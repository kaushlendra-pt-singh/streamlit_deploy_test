import streamlit as st

st.title("Profile")

# Splitting into 2 columns instead of 3. 
# The [1, 2] means the text column is twice as wide as the image column.
col1, col2 = st.columns([1, 2])

with col1:
    # use_container_width ensures the image fits nicely inside its column
    st.image('https://i.pinimg.com/1200x/cd/4b/d9/cd4bd9b0ea2807611ba3a67c331bff0b.jpg', use_container_width=True)

with col2:
    st.subheader("About Me")
    st.write("I am a passionate developer focusing on Artificial Intelligence, Machine Learning, and NLP.")
    st.write("I love building interactive applications and exploring agentic workflows.")

st.divider()

st.subheader("Experience & Education")
st.write("- **B.Tech in Computer Science** (2022 - 2026)")
st.write("- **Projects:** Sentiment Analysis APIs, Portfolio Websites, and Data Pipelines.")