from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
import time

load_dotenv()  # Loading all the environment variables

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Function to print initial messages
def print_initial_messages():
    initial_messages = [
        "DR.PANDA: Hi there! I'm here to chat with you. Feel free to share your thoughts or concerns. If you'd like, you can mention any mental health-related experiences.",
        "DR.PANDA: Type 'bye' when you're ready to end the conversation."
    ]
    for message in initial_messages:
        st.session_state['chat_history'].append(("Bot", message))

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
    print_initial_messages()  # Print initial messages when the session starts

# Create a vertical container for chat history and input area
chat_container = st.container()

# Input message and send button at the bottom
with chat_container:
    # Display chat history
    st.subheader("Chat History:")
    
    for role, text in st.session_state['chat_history']:
        if role == "You":
            st.markdown(f"<div style='text-align: right;'><b>{role}:</b> {text}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='text-align: left;'><b>{role}:</b> {text}</div>", unsafe_allow_html=True)

    # Input field for user to type their question
    input_text = st.text_input("Type your message here:", key="input")
    
    # Submit button to send the message
    submit = st.button("Send")

    if submit and input_text:
        # Check for "bye" to end the conversation
        if input_text.lower() == "bye":
            goodbye_message = "DR.PANDA: Thank you for sharing. Take care and goodbye!"
            st.session_state['chat_history'].append(("Bot", goodbye_message))
            
            # Save the conversation to a text file
            with open("chat_history.txt", "w") as f:
                for role, text in st.session_state['chat_history']:
                    f.write(f"{role}: {text}\n")

            st.session_state['chat_history'].append(("Bot", "Chat saved to 'chat_history.txt'."))

        else:
            # Show loading spinner
            with st.spinner('Thinking...'):
                time.sleep(2)  # Simulate processing time
                response = get_gemini_response(input_text)
            
            # Add user query and response to session state chat history
            st.session_state['chat_history'].append(("You", input_text))
            st.subheader("The Response is")
            
            # Display response and add to chat history
            for chunk in response:
                st.write(chunk.text)
                st.session_state['chat_history'].append(("Bot", chunk.text))

