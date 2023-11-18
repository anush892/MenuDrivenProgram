import os
import webbrowser
import pyttsx3
import tweepy
import wikipedia
from bs4 import BeautifulSoup
import requests

def open_notepad():
    os.system("notepad.exe")

def open_chrome():
    webbrowser.get("chrome").open()

def open_whatsapp():
    webbrowser.open("https://web.whatsapp.com/")

def send_email():
    # Implement email functionality here

def send_sms():
    # Implement SMS functionality here

def chat_with_gpt():
    # Implement chat with GPT functionality here

def get_geolocation():
    # Implement geolocation functionality here

def get_twitter_trends():
    consumer_key = "your_consumer_key"
    consumer_secret = "your_consumer_secret"
    access_token = "your_access_token"
    access_token_secret = "your_access_token_secret"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    trends = api.trends_place(1)  # Worldwide trends
    print("Current Twitter Trends:")
    for trend in trends[0]["trends"]:
        print("- " + trend["name"])

def get_hashtag_posts():
    hashtag = input("Enter a hashtag: ")
    # Implement getting top 10 posts for the hashtag here

def get_wikipedia_data():
    topic = input("Enter a topic: ")
    url = f"https://en.wikipedia.org/wiki/{topic}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")

    print(f"Wikipedia data for {topic}:")
    for paragraph in paragraphs:
        print(paragraph.get_text())

def play_audio():
    # Implement simple audio player functionality here

def play_video():
    # Implement basic video player functionality here

def control_speaker():
    text_to_speak = input("Enter text to speak: ")
    engine = pyttsx3.init()
    engine.say(text_to_speak)
    engine.runAndWait()

# Menu
while True:
    print("\nMenu:")
    print("1. Notepad")
    print("2. Chrome")
    print("3. WhatsApp")
    print("4. Email")
    print("5. SMS")
    print("6. Chat with GPT")
    print("7. Geolocation")
    print("8. Twitter Trends")
    print("9. Hashtag Posts")
    print("10. Wikipedia Data")
    print("11. Audio Player")
    print("12. Video Player")
    print("13. Control Speaker")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "0":
        break
    elif choice == "1":
        open_notepad()
    elif choice == "2":
        open_chrome()
    elif choice == "3":
        open_whatsapp()
    elif choice == "4":
        send_email()
    elif choice == "5":
        send_sms()
    elif choice == "6":
        chat_with_gpt()
    elif choice == "7":
        get_geolocation()
    elif choice == "8":
        get_twitter_trends()
    elif choice == "9":
        get_hashtag_posts()
    elif choice == "10":
        get_wikipedia_data()
    elif choice == "11":
        play_audio()
    elif choice == "12":
        play_video()
    elif choice == "13":
        control_speaker()
    else:
        print("Invalid choice. Please enter a valid option.")
