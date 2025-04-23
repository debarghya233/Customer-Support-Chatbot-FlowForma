import streamlit as st
from chatbot import get_response
from kb_loader import load_kb
from analytics import log_query, get_logs

st.title("FlowForma Support Assistant")

if "db" not in st.session_state:
    st.session_state.db = load_kb()

query = st.text_input("Enter your question:")
if query:
    answer = get_response(query, st.session_state.db)
    st.write("Answer:", answer)
    log_query(query, answer)

with st.expander("View Conversation Log"):
    st.dataframe(get_logs())
