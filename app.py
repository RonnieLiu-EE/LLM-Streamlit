import streamlit as st

img_path = 'assets/images/'
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

#st.set_page_config(layout='wide')

# sidebar menu
with st.sidebar:
    col_a1, col_a2, col_a3 = st.columns(3)

    st.divider()

    selected_format = st.selectbox("Upload Document Format", ('HTML', 'PDF', 'DOCX', 'XLSX', 'PPTX', 'CSV', 'Email', 'Video'))

    with col_a2:
        st.image(dict_format_code[selected_format])

    uploaded_files = st.file_uploader("Choose one of more file(s)", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)

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