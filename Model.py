from Word import Word
from dataGenerator import dataGenerator
import random
from SpeechToText import SpeechToText

class Model:

    def __init__(self):
        self.DG = dataGenerator()

    def checkTranslation(self, audioFilePath, correctAnswer):
        print("THE AUDIO FILE PATH IS", audioFilePath)
        userAnswer = SpeechToText.audioToString(audioFilePath)
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
                    dictionary[randomWord][2])
    

#test = Model(Word("hello","bonjour","hello/path.mp3","bonjour/path.mp3"))
#testWord = test.getRandomWord()
#print(testWord.getEnglishWord(),
#      testWord.getTranslatedWord(),
#      testWord.getEnglishAudio(),
#      testWord.getTranslatedAudio())

# m = Model()
# print(m.checkTranslation("TranslatedAudio/Bonjour.mp3", "Bonjour"))
