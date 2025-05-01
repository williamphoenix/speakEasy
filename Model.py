import random

from Word import Word
from dataGenerator import dataGenerator
from SpeechToText import SpeechToText

class Model:

    def __init__(self):
        self.DG = dataGenerator()

    def checkTranslation(self, audioFilePath, correctAnswer, targetLanguage):
        print("THE AUDIO FILE PATH IS", audioFilePath)
        userAnswer = SpeechToText.audioToString(audioFilePath, targetLanguage)
        print("THE TRANSCRIBED STRING IS:", userAnswer)
        if correctAnswer.strip().lower() in userAnswer.strip().lower():
            return 100
        else:
            return 0
       
    def getRandomWord(self, language):
        dictionary = self.DG.getDict(language)
        randomWord = random.choice(list(dictionary.keys()))
        return Word(randomWord, dictionary[randomWord][0],
                    dictionary[randomWord][1],
                    dictionary[randomWord][2],
                    dictionary[randomWord][3])