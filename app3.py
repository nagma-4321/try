
print("hello")

import streamlit as st

# Initialize session state to store conversation history
if "conversation" not in st.session_state:
    st.session_state.conversation = []  # Stores tuples of (question, response)
if "current_question_index" not in st.session_state:
    st.session_state.current_question_index = 0

# Define chatbot questions
questions = [
    "What's your name?",
    "How are you feeling today?",
    "Let's talk about this year 2024.",
    "How was your year?",
    "What is the most amazing memory of this year of yours?",
    "What is the one learning you got from this year?",
    "What is the one thing you liked the most about yourself this year?",
    "Have you captured the best memories of your life with you? If yes, I can give a suggestion to you.",
    "If you get a chance to write a book regarding the philosophy of living life, what would be the title?",
    "Do you pay gratitude to the higher for all the opportunities in your life?",
    "What one advice do you want to give yourself to be happier in life?"
]

# Suggestion for Question 7
suggestion = "Please convert them to physical copies; otherwise, you might lose them due to storage issues."

# Define chatbot layout
st.set_page_config(page_title="DATE TO MEMORIES (2024 Edition)", layout="centered")

# Header design
st.markdown(
    """
    <div style="background-color:orange; padding:20px; border-radius:10px;">
        <h1 style="color:white; text-align:center;">DATE TO MEMORIES (2024 Edition)</h1>
        <h3 style="color:white; text-align:center;">Reliving Moments, Creating Memories</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

# Chat area
st.write("### Chat")
chat_area = st.container()

def display_chat():
    """Function to display the chat in a styled format."""
    for question, response in st.session_state.conversation:
        st.markdown(
            f"""
            <div style="display:flex; align-items:baseline; justify-content:space-between; margin:10px 0;">
                <div style="background-color:#FFC7C7; padding:10px; border-radius:10px; max-width:60%; text-align:left;">
                    <b>Bot:</b> {question}
                </div>
                <div style="flex-grow:1;"></div>
                <div style="background-color:#E1FFC7; padding:10px; border-radius:10px; max-width:60%; text-align:right;">
                    <b>You:</b> {response}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Display chat history
with chat_area:
    display_chat()

# Handle the current question and response
if st.session_state.current_question_index < len(questions):
    question = questions[st.session_state.current_question_index]

    # Display the current question
    st.markdown(
        f"""
        <div style="background-color:#FFC7C7; padding:10px; border-radius:10px; margin-top:10px;">
            <b>Bot:</b> {question}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # User response input
    user_input = st.text_input("Your Response:")

    # Handle submission
    if st.button("Send"):
        if user_input.strip():
            # Store the conversation
            st.session_state.conversation.append((question, user_input))
            st.session_state.current_question_index += 1

            # Add suggestion after question 7
            if st.session_state.current_question_index == 8:
                st.session_state.conversation.append(("Bot Suggestion", suggestion))
        else:
            st.warning("Please provide a response to proceed!")

# Display thank-you message after all questions
if st.session_state.current_question_index >= len(questions):
    user_name = next(
        (response for question, response in st.session_state.conversation if "name" in question.lower()), "Friend"
    )
    st.success(
        f"Thank you for your responses, {user_name}! I appreciate your thoughtful answers and wish you the best for the future."
    )

    # Display all the responses for review
    with st.expander("Review Your Responses"):
        for question, response in st.session_state.conversation:
            st.write(f"**{question}**: {response}")




        