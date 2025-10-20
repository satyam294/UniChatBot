# chatbot.py  (Recommended - uses nltk + fuzzywuzzy)
import json
import re
import sys
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
except Exception:
    nltk = None

# Load FAQ
with open("data/faq.json", "r", encoding="utf-8") as f:
    faq = json.load(f)

# Build a flat list of candidate phrases mapped to intent keys
candidates = []
intent_map = {}  # candidate phrase -> intent_key
for intent_key, info in faq.items():
    # include both the canonical intent_key and provided examples
    candidates.append(intent_key.replace("_", " "))
    intent_map[intent_key.replace("_", " ")] = intent_key
    for ex in info.get("examples", []):
        candidates.append(ex)
        intent_map[ex] = intent_key

# Preprocessing helpers
STOPWORDS = set()
if nltk:
    try:
        STOPWORDS = set(stopwords.words("english"))
    except Exception:
        # stopwords may not be downloaded; fallback empty set
        STOPWORDS = set()

def normalize(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s]", " ", text)  # remove punctuation
    tokens = text.split()
    if STOPWORDS:
        tokens = [t for t in tokens if t not in STOPWORDS]
    return " ".join(tokens)

# Prepare normalized candidate list for faster matching
normalized_candidates = [normalize(c) for c in candidates]

def find_best_intent(user_text, threshold=60):
    user_norm = normalize(user_text)
    # Use process.extractOne for fuzzy match against normalized_candidates
    match, score = process.extractOne(user_norm, normalized_candidates, scorer=fuzz.token_set_ratio)
    if score >= threshold:
        matched_phrase = match
        intent_key = intent_map.get(candidates[normalized_candidates.index(matched_phrase)])
        return intent_key, score
    # fallback: also try matching the raw user input against keys directly
    for key in faq.keys():
        if key in user_text.lower() or key.replace("_", " ") in user_text.lower():
            return key, 100
    return None, 0

def get_response(user_text):
    intent, score = find_best_intent(user_text)
    if intent:
        return faq[intent]["response"]
    # final fallback
    return "Sorry, I don't know the answer to that yet. Try asking about admissions, courses, fees, or contact."

def repl():
    print("University Chatbot (type 'exit' or 'bye' to quit)")
    while True:
        try:
            user = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBye!")
            break
        if not user:
            continue
        if user.lower() in ("exit", "quit", "bye", "goodbye"):
            print("Bot:", faq.get("bye", {}).get("response", "Goodbye!"))
            break
        reply = get_response(user)
        print("Bot:", reply)

if __name__ == "__main__":
    repl()
