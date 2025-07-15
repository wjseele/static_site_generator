import unittest

from generator import extract_title


class TestTextNode(unittest.TestCase):
    def test_basic_title(self):
        title = extract_title("# Title")
        self.assertEqual(title, "Title")

    def test_missing_title(self):
        self.assertRaises(Exception, extract_title, "Title")

    def test_wrong_header(self):
        self.assertRaises(Exception, extract_title, "## Title\n### More title")

    def test_bigger_test(self):
        test_text = """
            # Title
            
            A bunch of text

            ## a subheading
        """
        title = extract_title(test_text)
        self.assertEqual(title, "Title")


if __name__ == "__main__":
    unittest.main()
