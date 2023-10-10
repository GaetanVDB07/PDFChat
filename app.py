import streamlit as st
from dotenv import load_dotenv


def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDF files", page_icon=":books:")

    st.header("Chat with multiple PDF files :books:")
    st.text_input("Ask a question about your documents.")

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your PDF files", accept_multiple_files=True, type="pdf")
        st.button("Process")




if __name__ == '__main__':
    main()