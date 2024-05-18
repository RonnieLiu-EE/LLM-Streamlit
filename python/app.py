import streamlit as st
import os

from io import BytesIO
from microservices.utilities import Utils
from microservices.svc_preprocessor import PreprocessorFactory


utils = Utils()

img_path = '../resources/images/'
upload_path = '../resources/tmp/uploaded_files/'

dict_format_code = {
    'HTML': f'{img_path}icon_html.png', 
    'PDF': f'{img_path}icon_pdf.png', 
    'DOCX': f'{img_path}icon_docx.png',
    'XLSX': f'{img_path}icon_xlsx.png', 
    'PPTX': f'{img_path}icon_pptx.png', 
    'CSV': f'{img_path}icon_csv.png', 
    'Email': f'{img_path}icon_email.png',
    'Video': f'{img_path}icon_video.png'
}

EMBEDDING = 'openai'
VECTOR_STORE = 'faiss'
MODEL_LIST = ['gpt-4o', 'gpt-4', 'gpt-3.5-turbo']

st.set_page_config(layout='wide')

# sidebar menu
with st.sidebar:

    st.markdown(
        "## How to use\n"
        "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"  # noqa: E501
        "2. Upload a file of supported format📄\n"
        "3. Ask a question about the document💬\n"
    )
    with st.expander("See currently supported formats"):
        col_a1, col_a2, col_a3, col_a4, col_a5, col_a6, col_a7, col_a8 = st.columns(8)
        with col_a1:
            st.image(dict_format_code['PDF'])

    st.divider()

    api_key_input = st.text_input(
        "OpenAI API Key",
        type="password",
        placeholder="Paste your OpenAI API key here (sk-...)",
        help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501
        value=os.environ.get("OPENAI_API_KEY", None)
        or st.session_state.get("OPENAI_API_KEY", ""),
    )

    st.session_state["OPENAI_API_KEY"] = api_key_input
    openai_api_key = st.session_state.get("OPENAI_API_KEY")
    if not openai_api_key:
        st.warning(
            "Enter your OpenAI API key in the sidebar. You can get a key at"
            " https://platform.openai.com/account/api-keys."
        )

    # model selector
    model: str = st.selectbox("Model", options=MODEL_LIST)  # type: ignore
    with st.expander("Advanced Options"):
        return_all_chunks = st.checkbox("Show all chunks retrieved from vector search")
        show_full_doc = st.checkbox("Show parsed contents of the document")

    #st.divider()

    # file uploader
    uploaded_files = st.file_uploader(
        "Choose one of more file(s)", 
        accept_multiple_files=True,
        type=['pdf'],
        help="Scanned documents are not supported yet!"
    )

    if not uploaded_files or len(uploaded_files) == 0:
        st.stop()

    for uploaded_file in uploaded_files:
        # stage file for processing
        file_name = uploaded_file.name
        file_ext = utils.get_file_extension(file_name)
        save_directory = f'{upload_path}{file_ext.lower()}'
        save_path = os.path.join(save_directory, file_name)

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        preprocessor = PreprocessorFactory.create_preprocessor(file_ext)
        preprocessor.run(save_path)

        st.write("Files uploaded:", file_name)

    st.divider()

    col_b1, col_b2, col_b3 = st.columns([1, 5, 1])
    with col_b2:
        st.button("Build Knowledge Base")



# main panel
st.title("Knowledge Bot")

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# react to user input
prompt = st.chat_input("Ask any questions about the uploaded documents")
if prompt:
    # display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    ###############################################################################
    # TODO: replace response with below code once backend is built
    #
    #with st.spinner("Searching for an answer..."):
    #    response = requests.post(CHATBOT_URL, json=data)
    #
    #    if response.status_code == 200:
    #        output_text = response.json()["output"]
    #        explanation = response.json()["intermediate_steps"]
    #
    #    else:
    #        output_text = """An error occurred while processing your message.
    #        Please try again or rephrase your message."""
    #        explanation = output_text
    ################################################################################
    
    
    response = f"Echo: {prompt}"
    # display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})