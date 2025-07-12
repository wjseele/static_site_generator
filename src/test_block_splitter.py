import unittest
from block_splitter import markdown_to_blocks


class TestBlockSplitter(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_links(self):
        md = """
            This is a [link](https://link.com).

            And this is an ![image](https://image.com)
        """
        expected = [
            "This is a [link](https://link.com).",
            "And this is an ![image](https://image.com)",
        ]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_empty(self):
        md = ""
        self.assertRaises(ValueError, markdown_to_blocks, md)

    def test_multiple_empty_lines(self):
        """Test blocks separated by more than two newlines"""
        md = "Block 1\n\n\n\nBlock 2"
        result = markdown_to_blocks(md)
        self.assertEqual(result, ["Block 1", "Block 2"])

    def test_trailing_whitespace_blocks(self):
        """Test blocks with only whitespace"""
        md = "Real block\n\n   \n\nAnother block"
        result = markdown_to_blocks(md)
        self.assertEqual(result, ["Real block", "Another block"])

    def test_mixed_indentation(self):
        """Test blocks with tabs and spaces"""
        md = "\tTab indented\n\n    Space indented"
        result = markdown_to_blocks(md)
        self.assertEqual(result, ["Tab indented", "Space indented"])

    def test_single_block(self):
        """Test markdown with no block separators"""
        md = "Just one block\nwith multiple lines"
        result = markdown_to_blocks(md)
        self.assertEqual(result, ["Just one block\nwith multiple lines"])


if __name__ == "__main__":
    unittest.main()
