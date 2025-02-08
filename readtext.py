import os
import time

def install(package):
    os.system(f"python -m pip install {package}")

# Try to import pyttsx3, and install it if not found
try:
    import pyttsx3
except ImportError:
    print("pyttsx3 not found. Installing...")
    install('pyttsx3')
    import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)

# Function to calculate progress percentage
def calculate_progress(current_position, total_length):
    return (current_position / total_length) * 100

# Function to save the current position to a bookmark file
def save_bookmark(position, bookmark_file="bookmark.txt"):
    with open(bookmark_file, 'w') as file:
        file.write(str(position))

# Function to load the current position from a bookmark file
def load_bookmark(bookmark_file="bookmark.txt"):
    if os.path.exists(bookmark_file):
        with open(bookmark_file, 'r') as file:
            return int(file.read().strip())
    return 0  # Start from the beginning if no bookmark exists

# Function to add pauses for punctuation, display progress, and handle bookmarks
def speak_with_pauses(text, bookmark_file="bookmark.txt"):
    total_length = len(text)  # Total length of the text
    start_position = load_bookmark(bookmark_file)  # Load the saved position
    processed_length = start_position  # Start from the saved position

    # Skip the text that has already been processed
    if total_length < start_position:
        remaining_text = text[0:]
        with open(bookmark_file, 'w') as file:
            file.write("0")  # Reset the bookmark
        
        return print("Book is finished. To read again, please run the program again.")
    else:
        remaining_text = text[start_position:]
        print(start_position)
        print(total_length)

    for sentence in remaining_text.split('.'):  # Split text by periods
        print(sentence)  # Display the sentence----------------------------------------------------------------------------------------
        if sentence.strip():  # Ignore empty strings
            for clause in sentence.split(','):  # Split by commas
                if clause.strip():
                    engine.say(clause.strip())  # Speak the clause
                    engine.runAndWait()  # Wait for speech to finish
                    processed_length += len(clause) + 1  # +1 for the comma
                    # Calculate and display progress
                    progress = calculate_progress(processed_length, total_length)
                    print(f"Progress: {progress:.2f}% ")
                    time.sleep(0.3)  # Pause after a comma
            processed_length += 1  # +1 for the period
            time.sleep(0.5)  # Pause after a period
        else:
            processed_length += 1  # +1 for empty sentences (e.g., multiple periods)
            time.sleep(0.5)  # Pause for empty sentences

        # Save the current position to the bookmark file
        save_bookmark(processed_length, bookmark_file)

# Example text
text = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""

# Speak the text with pauses, progress, and bookmarking
speak_with_pauses(text)