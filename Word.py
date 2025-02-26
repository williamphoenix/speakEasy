class Word:
    def __init__(self, englishWord, translatedWord,
                 englishAudio, translatedAudio):
        self.englishWord = englishWord
        self.translatedWord = translatedWord
        self.englishAudio = englishAudio
        self.translatedAudio = translatedAudio
    
    def getEnglishWord(self):
        return self.englishWord
    
    def getTranslatedWord(self):
        return self.translatedWord
    
    def getEnglishAudio(self):
        return self.englishAudio
    
    def getTranslatedAudio(self):
        return self.translatedAudio
    
#test= Word("hi","marhaba","path1","path2")
#word1 = test.getEnglishWord()
#word2 = test.getEnglishAudio()
#print(word1, word2)