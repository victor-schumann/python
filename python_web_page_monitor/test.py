import requests
import hashlib
import time
from playsound import playsound

# URL of the website to monitor
url = "https://finalfour.2ticket.pt/"

# Path to the sound file to play when a change is detected
sound_file = "sound.wav"  # Ensure this file exists in the same directory

# Function to fetch the content of the website
def fetch_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None

# Function to compute the SHA-256 hash of the content
def compute_hash(content):
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

# Fetch the initial content and compute its hash
initial_content = fetch_website_content(url)
if initial_content is None:
    print("Failed to fetch the initial content. Exiting.")
    exit(1)

previous_hash = compute_hash(initial_content)

print("Monitoring website for changes...")

try:
    while True:
        time.sleep(10)  # Wait for 10 seconds before the next check
        current_content = fetch_website_content(url)
        if current_content is None:
            print("Error fetching the website. Skipping this check.")
            continue
        current_hash = compute_hash(current_content)
        if current_hash != previous_hash:
            print("Website content has changed!")
            playsound(sound_file)
            previous_hash = current_hash
        else:
            print("No change detected.")
except KeyboardInterrupt:
    print("Monitoring stopped by user.")
