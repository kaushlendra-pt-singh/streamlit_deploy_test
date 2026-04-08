import streamlit as st

st.title("Get in Touch :email:")

st.write("Feel free to reach out if you'd like to collaborate, discuss tech, or just say hi!")

st.write("**Email:** kaush@example.com")
st.write("**LinkedIn:** [linkedin.com/in/yourprofile](https://linkedin.com)")
st.write("**GitHub:** [github.com/yourusername](https://github.com)")

st.divider()

st.subheader("Send a Message")

# A sleek form for users to contact you
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    
    # The submit button
    submitted = st.form_submit_button("Send Message")
    
    if submitted:
        if name and email and message:
            st.success(f"Thanks for reaching out, {name}! I'll get back to you soon.")
        else:
            st.error("Please fill out all fields before submitting.")