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


if __name__ == "__main__":
    unittest.main()
