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

    def test_heading(self):
        text = "# Title"
        self.assertEqual(block_to_block_type(text), BlockType.HEADING)

    def test_sub_heading(self):
        text = "### Subheading"
        self.assertEqual(block_to_block_type(text), BlockType.HEADING)

    def test_code(self):
        text = "```delete everything```"
        self.assertEqual(block_to_block_type(text), BlockType.CODE)

    def test_bad_code(self):
        text = "`delete everything`"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)

    def test_quotes(self):
        text = ">To be\n>Or not\n>To be"
        self.assertEqual(block_to_block_type(text), BlockType.QUOTE)

    def test_unordered_list(self):
        text = "- list1\n- list2\n- list3"
        self.assertEqual(block_to_block_type(text), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        text = "1. list1\n2. list2\n3. list3"
        self.assertEqual(block_to_block_type(text), BlockType.ORDERED_LIST)


if __name__ == "__main__":
    unittest.main()
