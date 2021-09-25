import unittest

from translator.py import englishToFrench, frenchToEnglish


class TestenglishToFrench (unittest.TestCase):
    def test1 (self):
        self.assertEqual(englistToFrench('Hello'),'Bonjour')
        self.assertEqual(englistToFrench(None),None)
        self.assertEqual(englistToFrench('This is my house'),'Cette maison est la mienne')
        self.assertEqual(englistToFrench('Nice to meet you'),'Ravi de vous rencontrer')

class TestfrenchToEnglish (unittest.TestCase):
    def test1 (self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        self.assertEqual(frenchToEnglish(None),None)
        self.assertEqual(frenchToEnglish('Cette maison est la mienne'),'This is my house')
        self.assertEqual(frenchToEnglish('Ravi de vous rencontrer'),'Nice to meet you')
     

unittest.main()