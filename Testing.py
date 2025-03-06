import unittest
from Word import Word

class Testing(unittest.TestCase):


    def test_word(self):
        test= Word("hi","marhaba","path1","path2")

        self.assertEqual(test.getEnglishWord(), 'hi',
            f"Message should be hi")
        self.assertEqual(test.getTranslatedWord(), 'marhaba',
            f"Message should be hi")
        self.assertEqual(test.getEnglishAudio(), 'path1',
            f"Message should be hi")
        self.assertEqual(test.getTranslatedAudio(), 'path2',
            f"Message should be hi")

    


if __name__ == '__main__':
    unittest.main()


    #test= Word("hi","marhaba","path1","path2")
#word1 = test.getEnglishWord()
#word2 = test.getEnglishAudio()
#print(word1, word2)