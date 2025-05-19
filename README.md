# Project - 1 AI-Powered Chatbot

An intelligent chatbot built using Natural Language Processing (NLP) technologies to handle customer support queries and frequently asked questions (FAQs). This chatbot uses transformer-based models for generating contextual responses and logs all user interactions into a database.

---

## 🧠 Features

- Understands and responds to user queries contextually
- Uses transformer-based NLP model for better accuracy
- Simple web interface for interaction
- Stores chat logs in a database
- Easy deployment using Flask or FastAPI

---

## 🔧 Technologies Used

- **Python**
- **Flask** or **FastAPI**
- **Transformers (HuggingFace)**
- **NLTK**
- **SQLite**

---

## 📁 Project Structure

```
AI-Powered-Chatbot/
├── app/
│   ├── chatbot.py           # Core chatbot logic
│   ├── database.py          # Interaction logging logic (SQLite)
│   └── routes.py            # Flask/FastAPI routes
├── static/
│   └── style.css            # Optional frontend styles
├── templates/
│   └── index.html           # Chat interface
├── main.py                  # Entry point of the app
├── requirements.txt         # Dependencies
├── README.md                # Project documentation
```

---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/suriyaasuri/ai-powered-chatbot.git
   cd ai-powered-chatbot
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Running the Chatbot

```bash
python main.py
```

Then open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📋 Example Conversation

**User:** How can I reset my password?  
**Chatbot:** You can reset your password by clicking on "Forgot Password" at the login page. A reset link will be sent to your email.

---

## 🛠️ Customization Tips

- Modify `chatbot.py` to change the underlying logic or model.
- Use a more powerful model like GPT-2 or DistilGPT2 from HuggingFace Transformers.
- Extend the frontend for a better UX using JavaScript or React.

---

## 💾 Logging

All chat interactions are stored in a SQLite database (`chat_logs.db`) including:
- Timestamps
- User queries
- Bot responses

---

## 📜 License

This project is licensed under the MIT License. Feel free to use and modify it.

---

## 👨‍💻 Author

Made by D Suriyaa
