# C:/Python311/python.exe -m pip install python-telegram-bot pygame pyaudio requests playsound pyautogui pyperclip
import requests
import hashlib
import time
import pygame
from datetime import datetime
import telegram

url = "https://finalfour.2ticket.pt/"
sound_file = "sound.wav"
bot_token = 'token_str_goes_here'
bot = telegram.Bot(token=bot_token) # setup with botfather on Telegram, send a message to it
chat_id = 123456 # get from https://api.telegram.org/botBOT_KEY_HERE/getUpdates, your ID is the one right above your name

pygame.mixer.init()

def play_sound(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

def fetch_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None

def compute_hash(content):
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def send_telegram_message(message):
    try:
        bot.send_message(chat_id=chat_id, text=message)
        print("Notification sent via Telegram.")
    except telegram.TelegramError as e:
        print(f"Error sending message: {e}")

initial_content = fetch_website_content(url)
if initial_content is None:
    print("Failed to fetch the initial content. Exiting.")
    exit(1)

previous_hash = compute_hash(initial_content)
print("Monitoring website for changes...")

iteration = 0

try:
    while True:
        time.sleep(3)
        iteration += 1
        print()
        print(f"Iteration: {iteration}")

        current_content = fetch_website_content(url)
        if current_content is None:
            print("Error fetching the website. Skipping this check.")
            continue

        current_hash = compute_hash(current_content)

        if iteration == 1:
            print("Simulating a change for testing...")
            change_detected = True
        else:
            change_detected = current_hash != previous_hash

        if change_detected:
            print("Website content has changed!")
            previous_hash = current_hash
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            custom_message = f"Website content changed at {current_datetime}. Link: {url}"
            
            send_telegram_message(custom_message)
            play_sound(sound_file)
            
        else:
            print("No change detected.")

except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")
