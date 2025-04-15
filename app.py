import streamlit as st
from chatpersona import processed_haji_query
# ✅ Step 1: Define your function
def process_input(user_input):
    return f"You said: {user_input}"  # Just echoes the input

# ✅ Step 2: Set up the UI
st.title("🧪 Simple Hitesh Choudhary Input/Output App")

user_query = st.text_input("Enter your message")

if st.button("Submit"):
    if user_query.strip():
        result = processed_haji_query(user_query)  # Pass input to function
        st.success(result)  # Show the result
    else:
        st.warning("Please enter something.")
