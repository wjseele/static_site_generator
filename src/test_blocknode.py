import unittest

from blocknode import BlockType, block_to_block_type


class TestTextNode(unittest.TestCase):
    def test_paragraph(self):
        text = "Just some text."
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)

    def test_empty(self):
        self.assertRaises(ValueError, block_to_block_type, "")

    def test_wrong(self):
        self.assertRaises(ValueError, block_to_block_type, ["string1", "string2"])


if __name__ == "__main__":
    unittest.main()
