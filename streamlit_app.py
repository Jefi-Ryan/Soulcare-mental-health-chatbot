
import streamlit as st
import requests
import json

_, title, _ = st.columns(3, gap = "large")

with title:
    st.header("Soul Care")
    st.text("")


# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"], unsafe_allow_html=True)

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)


# Generate a new response if last message is not from assistant

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # response = generate_llama2_response(prompt)
            placeholder = st.empty()
            payload = {"query": prompt}
            server_url = "localhost"
            server_port = 8000
            ans = requests.get(f'http://{server_url}:{server_port}/chatbot/', params=payload)
            ans = json.loads(ans.text)

            output = ans['response'].split("### Response:")[-1].split("<eos>")[0].lstrip("\\n").strip().rstrip("]").replace('\\n', '<br>')
            print(ans["response"])

            # full_response = ''
            # for item in response:
            #     full_response += item
            #     placeholder.markdown(full_response)
            placeholder.markdown(output, unsafe_allow_html=True)


    message = {"role": "assistant", "content": f"{output}"}
    st.session_state.messages.append(message)




