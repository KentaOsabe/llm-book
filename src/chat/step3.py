import streamlit as st
# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# セッション状態を初期化
if "history" not in st.session_state:
    st.session_state.history = []
    # st.session_state.llm = ChatOpenAI()
    st.session_state.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")

st.title("マルチモーダルRAGチャットボット")

# アップローダを追加
uploaded_file = st.file_uploader("画像を選択してください", type=["jpg", "jpeg", "png"])

# アップロードされた画像を表示
if uploaded_file is not None:
    st.image(uploaded_file, caption="画像", width=300)


# ユーザ入力を受け取る
user_input = st.text_input("メッセージを入力してください:")

# ボタンを追加し、クリックされたらアクションを起こす
if st.button("送信"):
    st.session_state.history.append(HumanMessage(user_input))
    response = st.session_state.llm.invoke(st.session_state.history)
    st.session_state.history.append(response)

    # 会話を表示
    for message in reversed(st.session_state.history):
        st.write(f"{message.type}: {message.content}")
