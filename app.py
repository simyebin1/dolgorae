import streamlit as st

st.markdown("""
<style>
.stApp {
    background-color: #F8F4EC;
}
</style>
""", unsafe_allow_html=True)

st.title("오늘의 말차다")
st.write("오늘의 말차를 만들어 보세요.")
st.button("시작하기")
