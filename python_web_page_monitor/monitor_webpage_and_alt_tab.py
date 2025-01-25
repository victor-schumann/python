# C:/Python311/python.exe -m pip install python-telegram-bot pygame pyaudio requests playsound pyautogui pyperclip
import requests
import hashlib
import time
import pyautogui
import pyperclip
import pygame
from datetime import datetime
import telegram

url = "https://finalfour.2ticket.pt/"
sound_file = "sound.wav"
bot_chat_id = 554710663
bot_token = '7819099231:AAHn6ZGr1mSMtYu8qkk_Semp2U7p8Jo5ufI'
bot = telegram.Bot(token=bot_token)

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

initial_content = fetch_website_content(url)
if initial_content is None:
    print("Failed to fetch the initial content. Exiting.")
    exit(1)

previous_hash = compute_hash(initial_content)
print("Monitoring website for changes...")

iteration = 0

try:
    while True:
        time.sleep(60)
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
            
            play_sound(sound_file)
            
            pyautogui.hotkey("alt", "tab")
            time.sleep(0.5)
            pyperclip.copy(custom_message)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(0.2)
            pyautogui.press("enter")
            pyautogui.hotkey("alt", "tab")

        else:
            print("No change detected.")

except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")
