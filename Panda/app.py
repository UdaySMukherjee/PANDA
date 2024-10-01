
# from flask import Flask, request, jsonify
# from dotenv import load_dotenv
# import os
# import google.generativeai as genai
# import time

# # Load environment variables from .env file
# load_dotenv()

# # Configure Google Generative AI
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Initialize the Gemini Pro model
# model = genai.GenerativeModel('gemini-pro')

# # Start a new chat session (with an empty history)
# chat = model.start_chat(history=[])

# # Initialize the Flask app
# app = Flask(__name__)

# # Function to send user input to the Gemini model and get the response
# def get_gemini_response(question):
#     try:
#         # Send the message to Gemini and stream the response
#         response = chat.send_message(question, stream=True)
        
#         # Concatenate the streamed chunks into a full response
#         response_text = ""
#         for chunk in response:
#             response_text += chunk.text  # Append the text chunks
        
#         # Print the response in the console (for debugging purposes)
#         print("Gemini Response:", response_text)
        
#         return response_text
#     except Exception as e:
#         print(f"Error while fetching Gemini response: {str(e)}")
#         return f"Error: {str(e)}"

# # Define a route to handle POST requests from the Android app
# @app.route('/chat', methods=['POST'])
# def chat_response():
#     try:
#         # Get the user message from the POST request (in JSON format)
#         user_message = request.json.get("message")
        
#         # Validate if the message is a non-empty string
#         if not user_message or not isinstance(user_message, str) or user_message.strip() == "":
#             return jsonify({"error": "Invalid message provided. Please enter a valid question."}), 400

#         # Print the received message
#         print("Received message:", user_message)
        
#         # Get the response from Gemini Pro model
#         gemini_response = get_gemini_response(user_message)
        
#         # Send the response back to the Android app
#         return jsonify({"response": gemini_response})
    
#     except Exception as e:
#         # Handle any unexpected errors
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     # Run the Flask app on all available IP addresses (port 5000)
#     app.run(host='0.0.0.0',  port=5000)





from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import google.generativeai as genai
import time
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini Pro model
model = genai.GenerativeModel('gemini-pro')

# Start a new chat session (with an empty history)
chat = model.start_chat(history=[])

# Initialize the Flask app
app = Flask(__name__)

# Function to send user input to the Gemini model and get the response
def get_gemini_response(question):
    try:
        # Send the message to Gemini and stream the response
        response = chat.send_message(question, stream=True)
        
        # Concatenate the streamed chunks into a full response
        response_text = ""
        for chunk in response:
            response_text += chunk.text  # Append the text chunks
        
        # Print the response in the console (for debugging purposes)
        print("Gemini Response:", response_text)
        
        return response_text
    except Exception as e:
        print(f"Error while fetching Gemini response: {str(e)}")
        return f"Error: {str(e)}"

# Define a route to handle POST requests from the Android app
@app.route('/chat', methods=['POST'])
def chat_response():
    try:
        # Get the user message from the POST request (in JSON format)
        user_message = request.json.get("message")
        
        # Validate if the message is a non-empty string
        if not user_message or not isinstance(user_message, str) or user_message.strip() == "":
            return jsonify({"error": "Invalid message provided. Please enter a valid question."}), 400

        # Print the received message
        print("Received message:", user_message)
        
        # Get the response from Gemini Pro model
        gemini_response = get_gemini_response(user_message)
        
        # Generate a unique chat ID
        chat_id = str(int(time.time() * 1000))  # Use the current timestamp as a unique ID
        
        # Get the current timestamp as the date
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Construct the response in the format expected by the Android app
        response_data = {
            "id": chat_id,
            "message": gemini_response,
            "sender": "gemini",  # Indicating the response is from the AI
            "date": current_date
        }
        
        # Send the response back to the Android app
        return jsonify(response_data)
    
    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app on all available IP addresses (port 5000)
    app.run(host='0.0.0.0', port=5000)
