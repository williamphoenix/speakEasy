class Word:
    def __init__(self, englishWord, translatedWord, prompt, responce_correct, response_incorrect):
        self.englishWord = englishWord
        self.translatedWord = translatedWord
        self.prompt = prompt
        self.response_correct = responce_correct
        self.response_incorrect = response_incorrect
    
    def getEnglishWord(self):
        return self.englishWord
    
    def getTranslatedWord(self):
        return self.translatedWord
    
    def getPrompt(self):
        return self.prompt
    
    def getResponse_Correct(self):
        return self.response_correct
    
    def getResponse_Incorrect(self):
        return self.response_incorrect
    
#test= Word("hi","marhaba","path1","path2")
#word1 = test.getEnglishWord()
#word2 = test.getEnglishAudio()
#print(word1, word2)