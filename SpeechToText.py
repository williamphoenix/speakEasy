import os
from openai import OpenAI

class SpeechToText:

    @staticmethod
    def audioToString(audioFilePath):
        try:
            if not os.path.exists(".apikey"):
                    raise FileNotFoundError("API key file '.apikey' not found.")
            with open(".apikey", "r") as keyFile:
                apiKey = keyFile.read().strip()

            if not apiKey:
                 raise ValueError("API key file is empty.")
            
            client = OpenAI(api_key=apiKey)

            if not os.path.exists(audioFilePath):
                 raise FileNotFoundError(f"Audio file '{audioFilePath}' not found.")

            try: 
                audioFile = open(audioFilePath, "rb")
                transcription = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audioFile
                )
            except IOError as e:
                 raise IOError(f"Error opening file '{audioFilePath}': {e}")

            return transcription.text
        
        except FileNotFoundError as fnf_error:
            print(f"File error: {fnf_error}")
        except ValueError as ve:
            print(f"Value error: {ve}")
        except IOError as io_error:
            print(f"I/O error: {io_error}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return None

print(SpeechToText.audioToString("TranslatedAudio/Bonjour.mp3"))