import unittest
from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    """English to French tests"""
    def test1(self):
        # Test Hello returns Bonjour
        self.assertEqual(english_to_french('Hello')["translations"][0]["translation"], 'Bonjour')
        # Test Hello does not return Hello
        self.assertNotEqual(english_to_french('Hello')["translations"][0]["translation"], 'Hello')
        # Test None returns empty string
        self.assertNotEqual(english_to_french("None")["translations"][0]["translation"], '')
        # Test empty string returns empty string
        self.assertNotEqual(english_to_french(0)["translations"][0]["translation"], 0)

class TestF2E(unittest.TestCase):
    """French to English tests"""
    def test1(self):
        # Test Bonjour returns Hello
        self.assertEqual(french_to_english('Bonjour')["translations"][0]["translation"], 'Hello')
        # Test Bonjour does not return Bonjour
        self.assertNotEqual(french_to_english('Bonjour')["translations"][0]["translation"], 'Bonjour')
        # Test None returns empty string
        self.assertNotEqual(french_to_english("None")["translations"][0]["translation"], '')
        # Test empty string returns empty string
        self.assertNotEqual(french_to_english(0)["translations"][0]["translation"],0)

if __name__ == "__main__":
    unittest.main()
