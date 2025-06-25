# AI-CHATBOT-WITH-NLP

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: SNEHAL NAMDEV INDULKAR

*INTERN ID*: CT4MXIT

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 16 WEEKS

*MENTOR*: NEELA SANTOSH


# 🤖 ChatMate — AI-Powered Sentiment Chatbot

ChatMate is an intelligent, friendly chatbot built using **Python**, combining **natural language understanding** (NLTK) with **Google Gemini AI** for real-time, sentiment-aware conversations. It features a simple **Tkinter GUI** that responds with emojis based on your mood. It's fun, lightweight, and great for learning AI integration in desktop apps.

---

## 🖥️ Preview

You: I’m having a great day!

ChatMate: That’s wonderful to hear! 😊

You: I'm feeling a bit down.

ChatMate: I'm here for you. 😔


---

## 📌 Features

- 🌐 **Gemini 1.5 Flash API** for fast, human-like replies.
- 🧠 **Sentiment Detection** using NLTK (VADER lexicon).
- 🖼️ **GUI Interface** with Tkinter (includes scrollable chat and emoji feedback).
- 🛡️ **Secure API Handling** using `.env` file.
- 👋 Type `"bye"` to gracefully exit the app.

---

## 🛠️ Tech Stack

| Function           | Tool / Library                |
|--------------------|-------------------------------|
| Language           | Python                        |
| GUI Framework      | Tkinter                       |
| NLP Toolkit        | NLTK (`vader_lexicon`)        |
| AI Model           | Google Gemini 1.5 Flash       |
| Env Management     | python-dotenv                 |
| Development IDE    | Visual Studio Code            |

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.8 or newer
- API key from [Google Generative AI](https://ai.google.dev/)
- Git or download access to the project

### 📦 Install Required Packages

```bash
   pip install nltk python-dotenv google-generativeai
```

Then run this once in Python to download NLTK data:

```python
import nltk
nltk.download('punkt')
nltk.download('vader_lexicon')
```

🧪 Run the App
1. Create a .env file in the root folder:
```ini
API_KEY=your_api_key_here
```

2. Run the script:
```bash
python main.py
```

## 🧠 How It Works

- **Sentiment Analysis**
  - Uses `SentimentIntensityAnalyzer` to calculate polarity scores.
  - Displays:
    - 😊 for positive sentiment
    - 😐 for neutral sentiment
    - 😔 for negative sentiment

- **AI Response**
  - Sends user input to Gemini AI using `GenerativeModel`.
  - Returns a smart, concise reply.

- **GUI Behavior**
  - Chat appears in a scrollable text box.
  - Input is typed below with a "Send" button or by pressing Enter.
  - Typing `"bye"` exits the program.


---

💡 Where It Can Be Used
- 🧑‍🏫 Educational Bots

- 💬 Emotional Support Tools

- 🛍️ Customer Support Chat Interfaces

- 📚 Interactive Learning Platforms

- 💻 AI Desktop App Projects







