import pandas as pd

test = pd.read_csv("EnglishToFrenchNouns.csv")
testDict = dict()
for i in range(len(test)):
    testDict.setdefault(test["EnglishWord"][i],
                    [test["TranslatedWord"][i],
                    test["Prompt"][i],
                    test["Response"][i]])
        
class dataGenerator:

    precompiledDict = testDict

    def __init__():
        print("classes dictionary is set to 'testDict'")

    @staticmethod
    def getEnglishWord(key):
        return key
    
    @staticmethod
    def getTranslatedWord(key):
        return dataGenerator.precompiledDict[key][0]
    
    @staticmethod
    def getEnglishAudio(key):
        return dataGenerator.precompiledDict[key][1]
    
    @staticmethod
    def getTranslatedAudio(key):
        return dataGenerator.precompiledDict[key][2]
    

#print("This is the test csv dataframe: \n", test, "\n",
#      "This is the dictionary test: \n", testDict, "\n",
#      dataGenerator.getEnglishWord("Hello"), "\n",
#      dataGenerator.getTranslatedWord("Apple"), "\n",
#      dataGenerator.getEnglishAudio("House"), "\n",
#      dataGenerator.getTranslatedAudio("Hello"), "\n",
#      )