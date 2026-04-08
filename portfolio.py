import streamlit as st

# 1. Page Configuration (Sets the tab title and icon)
st.set_page_config(page_title="Kaush's Portfolio", page_icon=":rocket:", layout="centered")

# --- TOP SECTION: Image (Left) & Contact Info (Right) ---
# We split the page into two columns. The [1, 2] means the right column is twice as wide as the left.
col1, col2 = st.columns([1, 2])

with col1:
    # Placeholder image. Replace the URL with your local file path like "my_photo.jpg" later.
    st.image("https://i.pinimg.com/1200x/cd/4b/d9/cd4bd9b0ea2807611ba3a67c331bff0b.jpg", width=180)

with col2:
    st.title("Kaush")
    st.subheader("AI, ML & NLP Developer")
    # Using Streamlit's built-in markdown icons
    st.write(":email: kaush@example.com")
    st.write(":telephone_receiver: +91 9876543210")
    st.write(":link: [GitHub](https://github.com) | [LinkedIn](https://linkedin.com)")

st.divider() # Creates a clean horizontal line

# --- MIDDLE SECTION: Career Objective & Education ---
st.header(":dart: Career Objective")
st.write("""
To leverage my passion for Artificial Intelligence, Natural Language Processing, and Machine Learning to build innovative, 
research-oriented solutions. I am eager to contribute to open-source projects and explore the frontiers of Agentic AI and IoT.
""")

st.header(":mortar_board: Education")
st.write("**Bachelor of Technology in Computer Science**")
st.write("*Your University Name | 2022 - 2026*")
st.write("- **Core Focus:** Machine Learning, NLP, Data Structures, Algorithms.")
st.write("- **Key Projects:** Vibe_Check (High-level sentiment analysis using LLM APIs).")

st.divider()

# --- FOOTER ---
# Using HTML alignment combined with Streamlit icons for a clean centered footer
st.markdown(
    f"""
    <div style="text-align: center; color: gray;">
        <p>Built with ❤️ using Streamlit</p>
        <p>{':globe_with_meridians::computer::robot_face:'}</p>
    </div>
    """,
    unsafe_allow_html=True
)