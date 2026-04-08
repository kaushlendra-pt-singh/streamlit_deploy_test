import streamlit as st

# Optional: Set global page settings
st.set_page_config(page_title="My Portfolio", page_icon=":rocket:")

# Define the pages
home_page = st.Page("views/home.py", title="Home", icon=":material/home:")
profile_page = st.Page("views/profile.py", title="Profile", icon=":material/person:")
contact_page = st.Page("views/contact.py", title="Contact", icon=":material/mail:")

# Setup the navigation
# Note: I removed default=True from contact so the Home page loads first
pg = st.navigation([home_page, profile_page, contact_page])

# Optional Logo (Uncomment and add a valid URL/Path if you want one in the sidebar)
# st.logo('https://via.placeholder.com/150x50.png?text=Logo')

# You MUST run the navigation block to make the pages render
pg.run()