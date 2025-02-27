from Word import Word
from dataGenerator import dataGenerator
import random

class Model:
    def __init__(self, Word):
        self.currentWord = Word
        #print("currentWord is", self.currentWord) (Test)

    def checkTranslation(mp3Path):
        pass

    def getRandomWord(self):
        randomWord = random.choice(list(dataGenerator.precompiledDict.keys()))
        return Word(randomWord, dataGenerator.precompiledDict[randomWord][0],
                    dataGenerator.precompiledDict[randomWord][1],
                    dataGenerator.precompiledDict[randomWord][2])
    

#test = Model(Word("hello","bonjour","hello/path.mp3","bonjour/path.mp3"))
#testWord = test.getRandomWord()
#print(testWord.getEnglishWord(),
#      testWord.getTranslatedWord(),
#      testWord.getEnglishAudio(),
#      testWord.getTranslatedAudio())