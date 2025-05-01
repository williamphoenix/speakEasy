import pandas as pd

class dataGenerator:
    
    def __init__(self):
        self.FrenchDict = self.compileDict("EnglishToFrenchNouns.csv")
        self.SpanishDict = self.compileDict("EnglishToSpanishNouns.csv")
        self.EnglishDict = self.compileDict("EnglishToEnglishNouns.csv")

    @staticmethod
    def compileDict(path):
        current = pd.read_csv(path)
        currentDict = dict()
        for i in range(len(current)):
            currentDict.setdefault(current["EnglishWord"][i],
                        [current["TranslatedWord"][i],
                            current["Prompt"][i],
                            current["Response_Correct"][i],
                            current["Response_Incorrect"][i]])
        return currentDict

    def getDict(self, lang):
        if(lang == "French"):
            return self.FrenchDict
        elif(lang == "Spanish"):
            return self.SpanishDict
        elif(lang == "English"):
            return self.EnglishDict
        else:
            raise("did not find language to access")
    
    def getEnglishWord(self, key):
        return key
    
    def getTranslatedWord(self, key):
        return dataGenerator.precompiledDict[key][0]
    
    def getPrompt(self, key):
        return dataGenerator.precompiledDict[key][1]
    

    def getResponse_Correct(self, key):
        return dataGenerator.precompiledDict[key][2]
    
    def getResponse_Incorrect(self, key):
        return dataGenerator.precompiledDict[key][3]