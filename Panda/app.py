# from flask import Flask, request, jsonify
# from dotenv import load_dotenv
# import os
# import google.generativeai as genai
# import time
# from datetime import datetime

# load_dotenv()

# # Configure Google Generative AI
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# model = genai.GenerativeModel('gemini-pro')
# chat = model.start_chat(history=[])
# app = Flask(__name__)

# # Function to send user input to the Gemini model and get the response
# def get_gemini_response(question):
#     try:
#         response = chat.send_message(question, stream=True)
#         response_text = ""
#         for chunk in response:
#             response_text += chunk.text  
#         print("Gemini Response:", response_text)
#         return response_text
#     except Exception as e:
#         print(f"Error while fetching Gemini response: {str(e)}")
#         return f"Error: {str(e)}"

# # Define a route to handle POST requests from the Android app
# @app.route('/chat', methods=['POST'])
# def chat_response():
#     try:
#         user_message = request.json.get("message")
#         if not user_message or not isinstance(user_message, str) or user_message.strip() == "":
#             return jsonify({"error": "Invalid message provided. Please enter a valid question."}), 400
#         print("Received message:", user_message)
#         gemini_response = get_gemini_response(user_message)
#         chat_id = str(int(time.time() * 1000)) 
#         current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         response_data = {
#             "id": chat_id,
#             "message": gemini_response,
#             "sender": "gemini",
#             "date": current_date
#         }
#         return jsonify(response_data)
    
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import google.generativeai as genai
import time
from datetime import datetime
from report import generate_report  # Import the report generation function

load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
app = Flask(__name__)

# Initialize the passage variable to store the conversation
passage = ""

# Function to send user input to the Gemini model and get the response
def get_gemini_response(question):
    try:
        response = chat.send_message(question, stream=True)
        response_text = ""
        for chunk in response:
            response_text += chunk.text  
        print("Gemini Response:", response_text)
        return response_text
    except Exception as e:
        print(f"Error while fetching Gemini response: {str(e)}")
        return f"Error: {str(e)}"

# Define a route to handle POST requests from the Android app
@app.route('/chat', methods=['POST'])
def chat_response():
    global passage  # Ensure we can modify the global passage variable
    try:
        user_message = request.json.get("message")
        if not user_message or not isinstance(user_message, str) or user_message.strip() == "":
            return jsonify({"error": "Invalid message provided. Please enter a valid question."}), 400

        print("Received message:", user_message)

        # Append user message to passage
        passage += f"User: {user_message}\n"
        
        # If user says 'bye', generate report, print the passage, and end conversation
        if user_message.strip().lower() == 'bye':
            # Print the full conversation
            print("Full Conversation Passage:\n", passage)
            
            # Include passage in the report generation
            generate_report(passage)  # Pass the full passage to the report generation function
            return jsonify({"message": "Thank you! Your conversation report is generated and sent to you as a PDF."})
            # return jsonify({"message": passage})
        
        gemini_response = get_gemini_response(user_message)
        passage += f"DR.PANDA: {gemini_response}\n"  # Append Gemini response to passage
        chat_id = str(int(time.time() * 1000)) 
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        response_data = {
            "id": chat_id,
            "message": gemini_response,
            "sender": "gemini",
            "date": current_date
        }
        return jsonify(response_data)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

