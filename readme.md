# 🎓 CampusConnect DITU — AI-Powered University Chatbot

**CampusConnect DITU** is a simple AI-powered **terminal-based chatbot** designed to answer university-related queries such as admissions, fees, courses, campus facilities, and more.  
It uses **Natural Language Processing (NLP)** concepts like **text normalization**, **stopword removal**, and **fuzzy string matching (via FuzzyWuzzy)** to understand user input and respond accurately based on a predefined FAQ dataset.

---

## 🚀 Features
- 💬 Interactive chatbot that responds to student queries about DIT University.  
- 🧠 Uses **FuzzyWuzzy’s token-based matching** for intent recognition.  
- 🗂️ Reads data from an easily editable `faq.json` file.  
- ⚙️ Includes **text preprocessing** (punctuation removal, stopword filtering, normalization).  
- 💻 Works entirely in the **terminal** — no web integration required (yet!).  
- 🔐 Clean, modular code design for easy extension and future improvements.

---

## 🧩 Project Structure

```
CampusConnect-DITU/
│
├── data/
│   └── faq.json              # Frequently Asked Questions dataset
│
├── chatbot.py                # Main chatbot code (terminal-based)
├── requirements.txt          # Required Python dependencies
├── README.md                 # Project overview and instructions
└── config.py (optional)      # For storing API keys (for future web version)
```

---

## 🛠️ Installation and Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/CampusConnect-DITU.git
cd CampusConnect-DITU
```

### 2️⃣ Create and Activate Virtual Environment
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Chatbot
```bash
python chatbot.py
```

---

## 📘 Example Conversation

```
University Chatbot (type 'exit' or 'bye' to quit)

You: What is the admission process?
Bot: To apply for admission at DITU, visit the official university admission portal and fill out the online application form...

You: What is the B.Tech fee?
Bot: The fee structure varies by course. For example: B.Tech – approx ₹1,70,000 per year, MBA – ₹2,00,000 per year...

You: Does DITU have hostels?
Bot: Yes, DITU provides separate hostels for boys and girls with comfortable rooms, Wi-Fi, and mess facilities.

You: bye
Bot: Goodbye! It was nice talking to you. Have a great day ahead!
```

---

## 🧠 How It Works

1. **User Input:** The chatbot takes text input from the user in the terminal.  
2. **Text Normalization:** Converts input to lowercase, removes punctuation, and filters out stopwords.  
3. **Fuzzy Matching:** Compares processed input with stored FAQs using `fuzz.token_set_ratio` to find the closest match.  
4. **Intent Recognition:** Identifies which intent (e.g., “admission_process”, “fees_structure”) the question relates to.  
5. **Response Generation:** Returns the pre-defined answer from `faq.json`.  

---

## 🧰 Technologies Used

- **Python 3.11**
- **FuzzyWuzzy** → for string similarity matching  
- **NLTK** → for tokenization and stopword removal  
- **JSON** → for storing FAQ dataset  
- **re (regex)** → for text cleaning and normalization  

---

## 📚 Future Improvements

- 🌐 Add a **web-based or GUI interface** (using Flask or Streamlit).  
- 🤖 Integrate **real-time data** from university APIs.  
- 💡 Add **contextual understanding** (multi-turn conversations).  
- 🗣️ Enable **voice input/output** for accessibility.  
- 🌏 Add **multi-language support** (e.g., English and Hindi).  

---

## 👩‍💻 Team Members
- **Member 1:** Satyam Chand  
- **Member 2:** [Add Name Here]  
- **Member 3:** [Add Name Here]  
- **Member 4:** [Add Name Here]  

---

## 🏁 Conclusion

CampusConnect DITU demonstrates how an **AI-powered chatbot** can simplify university communication by instantly answering student queries.  
It combines **NLP preprocessing** with **fuzzy matching** to achieve reliable performance — even without large language models — making it an ideal project for beginners exploring AI and Python.

---

## 📝 License
This project is developed for academic and educational purposes.  
You’re free to use, modify, and extend it with proper attribution.
