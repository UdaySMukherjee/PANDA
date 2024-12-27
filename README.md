# PANDA: Psychological Abnormality Detection Application

PANDA (Psychological Abnormality Detection Application) is an innovative AI-powered chatbot designed to assist users in understanding and addressing mental health concerns. By leveraging advanced natural language processing, PANDA provides personalized support, symptom detection, and insights based on user interactions.

---

## Features

- **AI-Powered Chatbot**: Engages in meaningful conversations to provide mental health insights.
- **Symptom Classification**: Detects a wide range of psychological symptoms from user interactions.
- **Knowledge Base Integration**: Utilizes a dynamic SQLite database for accurate and relevant responses.
- **PDF Report Generation**: Provides a detailed summary of user interactions and detected symptoms in a downloadable report.
- **Customizable and Extendable**: Easily adaptable for various use cases and mental health domains.

---

## Prerequisites

- Python 3.8+
- Required libraries: `flask`, `sqlite3`, `dotenv`, `google-generativeai`, `fpdf`
- Google API Key for Generative AI

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/UdaySMukherjee/pandagpt--backend.git
   cd panda-ai
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the project root.
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_google_api_key
     ```

4. Initialize the SQLite database:
   ```bash
   sqlite3 knowledge_base.db < schema.sql
   ```

---

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Access the application at `http://localhost:5000`.

3. Use the `/chat` endpoint to interact with the chatbot.
   - Example:
     ```bash
     curl -X POST http://localhost:5000/chat -H "Content-Type: application/json" -d '{"message": "I feel anxious lately."}'
     ```

4. End the conversation with `bye` to generate a PDF report.

---

## Project Structure

```
.
├── app.py                # Main application file
├── schema.sql            # SQLite database schema
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── .env                  # Environment variables
└── knowledge_base.db     # SQLite database
```

---

## Acknowledgments

- Inspired by advancements in AI and mental health care.
- Powered by Google Generative AI.

---

## Disclaimer

PANDA is not a substitute for professional medical advice, diagnosis, or treatment. Please consult a qualified healthcare provider for any mental health concerns.
