import os
import csv
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
    with open("EnglishToSpanishNouns.csv", mode="r", ) as file:
        csvFile = csv.DictReader(file)
        count = 0
        for lines in csvFile:
            if count < 1000:
                #print(lines["French"])
                speech_file_path = Path(__file__).parent/"SpanishPrompt" / f"{lines["EnglishWord"]}.mp3"
                print(speech_file_path)

                response = client.audio.speech.create(
                    model="gpt-4o-mini-tts",
                    voice="sage",
                    input=f"How do you say {lines["EnglishWord"]} in Spanish?",
                    instructions=f"You are a helpful teacher asking your student to translate a word into another language.",
                )
                response.stream_to_file(speech_file_path)
                count += 1

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