import streamlit as st
import google.generativeai as genai

# Set up the Gemini API key
genai.configure(api_key="AIzaSyArdQA4hsN0rlUJLBT09bDbR0UPaaYryhY")  # Replace with your Gemini API Key

# Function to get a response from Gemini with improved precision
def get_gemini_response(user_input):
    """Generate a structured, precise response using Gemini API with advanced prompting."""
    
    # *Enhanced Prompt for Accurate, Clear, and Direct Answers*
    prompt = f"""
    You are an expert career counselor assisting students with their education and job queries. 
    Provide *accurate, structured, and to-the-point responses* in a *step-by-step manner*.

    *Guidelines for Response:*
    - Keep answers *precise and structured* (no generic responses).
    - Use *bullet points or step-by-step breakdowns*.
    - *If the question is about higher education*, suggest courses based on eligibility, entrance exams, and future job scope.
    - *If the question is about career paths*, provide job roles, industries, salaries, and required skills.
    - *If the question is about entrance exams*, list eligibility, syllabus, and exam dates.
    - *If the question is about a confused student, give **motivational and clear* guidance.
    - *If the user asks about multiple fields*, compare them with advantages and disadvantages.
    
    *Example Response Structure:*
    1️⃣ *Available Courses:* List top courses based on the student’s stream.  
    2️⃣ *Entrance Exams:* Mention exams required for admission.  
    3️⃣ *Job Opportunities:* List job roles, industries, salary trends.  
    4️⃣ *Future Scope:* Explain growth trends and industry demand.  

    *Student's Question:* {user_input}
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text if response.text else "Sorry, I couldn't generate a precise response."

# Streamlit UI
st.title("🎓 Career Guidance Chatbot")
st.write("Get precise answers about courses, job opportunities, and career choices!")

# User Input
user_input = st.text_input("Type your question here:")

if user_input:
    response = get_gemini_response(user_input)
    st.write("*Bot:*", response)