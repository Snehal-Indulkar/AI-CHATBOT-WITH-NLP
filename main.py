import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import google.generativeai as genai
import tkinter as tk
from tkinter import scrolledtext
from dotenv import load_dotenv
import os

# === NLTK Setup ===
nltk.download('punkt')
nltk.download('vader_lexicon')
from nltk.tokenize import word_tokenize
sia = SentimentIntensityAnalyzer()

# --- LOAD ENV VARIABLES ---
load_dotenv()
API_KEY = os.getenv('API_KEY')

# === Configure Gemini API ===
genai.configure(api_key=API_KEY)

# === Initialize Chat Session ===
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
chat_session = model.start_chat(history=[
    {
        "role": "user",
        "parts": [
            "You are ChatMate, a helpful and friendly assistant. "
            "Reply briefly, naturally, and like a real human. "
            "Avoid giving long explanations unless asked."
        ]
    }
])

# === Chat Function ===
def chat():
    prompt = user_input.get().strip()
    if not prompt:
        return

    chat_area.insert(tk.END, "You: " + prompt + "\n")
    user_input.delete(0, tk.END)

    if prompt.lower() == "bye":
        chat_area.insert(tk.END, "ChatMate: Goodbye! 👋\n")
        window.after(1500, window.destroy)
        return

    # --- NLTK Sentiment Analysis ---
    try:
        tokens = word_tokenize(prompt)  # ✅ Safe tokenization
        sentiment = sia.polarity_scores(prompt)
        compound = sentiment['compound']

        if compound >= 0.5:
            mood_emoji = "😊"
        elif compound <= -0.5:
            mood_emoji = "😔"
        else:
            mood_emoji = "😐"
    except Exception as e:
        mood_emoji = ""
        print(f"Sentiment Analysis Error: {e}")

    # --- Gemini Response ---
    try:
        response = chat_session.send_message(prompt)
        reply = response.text.strip() or "(No response received)"
    except Exception as e:
        reply = f"ChatMate Error: {str(e)}"

    chat_area.insert(tk.END, f"ChatMate: {reply} {mood_emoji}\n\n")
    chat_area.see(tk.END)

# === GUI Setup ===
window = tk.Tk()
window.title("ChatMate")
window.geometry("500x600")
window.configure(bg="#F0F2F5")

chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Segoe UI", 12), bg="white", fg="black")
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

user_input = tk.Entry(window, font=("Segoe UI", 14))
user_input.pack(padx=10, pady=(0, 10), fill=tk.X)
user_input.focus()

send_button = tk.Button(window, text="Send", command=chat, bg="#0084FF", fg="white", font=("Segoe UI", 12, "bold"))
send_button.pack(pady=(0, 10))

window.bind("<Return>", lambda event: chat())

chat_area.insert(tk.END, "ChatMate: Hello! I'm ChatMate. Type 'bye' to exit.\n\n")

# === Start GUI Loop ===
window.mainloop()