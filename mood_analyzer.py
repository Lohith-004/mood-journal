from textblob import TextBlob
from datetime import datetime
import json
import os

def get_sentiment_emoji(score):
    if score > 0.5:
        return "😄"
    elif score > 0.1:
        return "🙂"
    elif score > -0.1:
        return "😐"
    elif score > -0.5:
        return "😞"
    else:
        return "😡"

def main():
    entry = input("How are you feeling today? 📝\n> ")
    blob = TextBlob(entry)
    score = blob.sentiment.polarity
    emoji = get_sentiment_emoji(score)

    log_entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "entry": entry,
        "sentiment_score": score,
        "mood": emoji
    }

    if os.path.exists("mood-log.json"):
        with open("mood-log.json", "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(log_entry)

    with open("mood-log.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"\nMood detected: {emoji} (score: {score:.2f})")
    print("Your entry has been saved to mood-log.json 📁")

if __name__ == "__main__":
    main()
