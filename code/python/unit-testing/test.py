import unittest
from name import formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        result = formatted_name("ashish", "panigrahi")
        self.assertEqual(result, "Ashish Panigrahi")
