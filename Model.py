from Word import Word
from dataGenerator import dataGenerator
import random
from SpeechToText import SpeechToText

class Model:
    def __init__(self):
        pass
        #print("currentWord is", self.currentWord) (Test)

    def checkTranslation(self, audioFilePath, correctAnswer):
        print("THE AUDIO FILE PATH IS", audioFilePath)
        userAnswer = SpeechToText.audioToString(audioFilePath)
        print("THE TRANSCRIBED STRING IS:", userAnswer)
        if correctAnswer.strip().lower() in userAnswer.strip().lower():
            return 100
        else:
            return 0
       

    def getRandomWord(self, language):
        randomWord = random.choice(list(dataGenerator.precompiledDict[language].keys()))
        return Word(randomWord, dataGenerator.precompiledDict[language][randomWord][0],
                    dataGenerator.precompiledDict[language][randomWord][1],
                    dataGenerator.precompiledDict[language][randomWord][2])
    

#test = Model(Word("hello","bonjour","hello/path.mp3","bonjour/path.mp3"))
#testWord = test.getRandomWord()
#print(testWord.getEnglishWord(),
#      testWord.getTranslatedWord(),
#      testWord.getEnglishAudio(),
#      testWord.getTranslatedAudio())

# m = Model()
# print(m.checkTranslation("TranslatedAudio/Bonjour.mp3", "Bonjour"))
