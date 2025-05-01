import os
import csv
import subprocess

from pathlib import Path
from openai import OpenAI

#Go through Translation CSV, save speech to text audio files to directories, write path to cvs file
#Please don't run the functions in this file without asking 🥺

try:
    if not os.path.exists(".apikey"):
            raise FileNotFoundError("API key file '.apikey' not found.")
    with open(".apikey", "r") as keyFile:
        apiKey = keyFile.read().strip()

    if not apiKey:
            raise ValueError("API key file is empty.")

    client = OpenAI(api_key=apiKey)

except FileNotFoundError as fnf_error:
    print(f"File error: {fnf_error}")
except ValueError as ve:
    print(f"Value error: {ve}")
except IOError as io_error:
    print(f"I/O error: {io_error}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

def generateAudio():
    with open("EnglishToEnglishNouns.csv", mode="r", ) as file:
        csvFile = csv.DictReader(file)
        for lines in csvFile:
            speech_file_path = Path(__file__).parent/"EnglishResponse"/"Incorrect" / f"{lines["EnglishWord"]}_incorrect.mp3"
            print(speech_file_path)

            response = client.audio.speech.create(
                model="gpt-4o-mini-tts",
                voice="sage",
                input=f"Incorrect. The word was \"{lines["TranslatedWord"]}\"",
                instructions=f"You are a helpful teacher asking your student to translate a word into another language.",
            )
            response.stream_to_file(speech_file_path)
generateAudio()

def writeAudioPaths():
    with open("EnglishToFrenchNouns.csv", mode="r", newline="", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)

    for row in rows:
        english_word = row["English"] 
        audio_filename = f"{english_word}.mp3"
        relative_path = f"EnglishAudio/{audio_filename}"

        row["EnglishAudio"] = relative_path

    fieldnames = rows[0].keys()

    with open("EnglishToFrenchNouns.csv", mode="w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def trimAudio(pathToFiles):
    for filename in os.listdir(pathToFiles):
        if filename.endswith((".mp3", ".wav", ".m4a")):
            file_path = os.path.join(pathToFiles, filename)

            temp_file_path = os.path.join(pathToFiles, f"temp_{filename}")

            trim_cmd = [
                "ffmpeg", "-i", file_path,
                "-af", "silenceremove=stop_periods=-1:stop_duration=0.2:stop_threshold=-50dB", 
                "-c:a", "libmp3lame",  
                "-b:a", "128k",  
                "-y", temp_file_path  
            ]
            
            subprocess.run(trim_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"Trimmed audio saved as temporary file: {temp_file_path}")

            overwrite_cmd = [
                "mv", temp_file_path, file_path  
            ]
            subprocess.run(overwrite_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"Replaced original file with trimmed audio: {filename}")

            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)
                print(f"Deleted temporary file: {temp_file_path}")

    print("All files processed and overwritten.")

if __name__ == "__main__":
    folder_to_trim = "SpanishPrompt"  # Change this to the folder you want to process