import pandas as pd

test = pd.read_csv("EnglishToFrenchNouns.csv")
testDict = dict()
for i in range(len(test)):
    testDict.setdefault(test["EnglishWord"][i],
                    [test["TranslatedWord"][i],
                    test["EnglishAudio"][i],
                    test["TranslatedAudio"][i]])

frenchDict = testDict
        
arabic = pd.read_csv("arabicTest.csv")
arabicDict = dict()
for i in range(len(arabic)):
    arabicDict.setdefault(arabic["EnglishWord"][i],
                    [arabic["TranslatedWord"][i],
                    arabic["EnglishAudio"][i],
                    test["TranslatedAudio"][i]])

class dataGenerator:

    precompiledDict = dict()
    precompiledDict.setdefault("arabic",arabicDict)
    precompiledDict.setdefault("french",frenchDict)
    precompiledDict.setdefault("test",testDict)


    def __init__():
        print("classes dictionary is set to 'testDict'")
    

#print("This is the test csv dataframe: \n", test, "\n",
#      "This is the dictionary test: \n", testDict, "\n",
#      dataGenerator.getEnglishWord("Hello"), "\n",
#      dataGenerator.getTranslatedWord("Apple"), "\n",
#      dataGenerator.getEnglishAudio("House"), "\n",
#      dataGenerator.getTranslatedAudio("Hello"), "\n",
#      )