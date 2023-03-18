from Chatbot import main
import streamlit as st

st.set_page_config(page_title = "My Chatbot App", page_icon = ":tada:", layout = "wide")
st.title("My Chatbot App")

with st.container():
    st.sidebar.title("Sidebar")
    st.sidebar.subheader("Pages")
    app_mode = st.sidebar.selectbox("select a page",("Home","Chatbot"))

    if app_mode == "Home":
        st.markdown("Chat with me if you feel bored")
        st.video('https://www.youtube.com/watch?v=pX6zqaEHAdw')
    elif app_mode == "Chatbot":
        st.text("Please talk to me")
        text = st.text_input("You:")
        if text != "":
            st.write("Chatbot:")
            with st.spinner("Loading..."):
                st.write(main(text))
