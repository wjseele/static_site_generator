import unittest

from delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestDelimiter(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is a text with a **bold** word.", TextType.TEXT)
        expected = [
            TextNode("This is a text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word.", TextType.TEXT),
        ]
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), expected)

    def test_italic(self):
        node = TextNode("This is a text with a _italic_ word.", TextType.TEXT)
        expected = [
            TextNode("This is a text with a ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word.", TextType.TEXT),
        ]
        self.assertEqual(split_nodes_delimiter([node], "_", TextType.ITALIC), expected)

    def test_code(self):
        node = TextNode("This is a text with a `code` word.", TextType.TEXT)
        expected = [
            TextNode("This is a text with a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" word.", TextType.TEXT),
        ]
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE), expected)

    def test_double_bold(self):
        node = TextNode("This is a **text** with a **bold** word.", TextType.TEXT)
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word.", TextType.TEXT),
        ]
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), expected)

    def test_list_of_nodes(self):
        node = TextNode("This is a text with a **bold** word.", TextType.TEXT)
        expected = [
            TextNode("This is a text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word.", TextType.TEXT),
        ]
        expected.extend(expected * 2)
        self.assertEqual(
            split_nodes_delimiter([node, node, node], "**", TextType.BOLD),
            expected,
        )

    def test_at_start(self):
        node = TextNode("_Italic text_ right at the start.", TextType.TEXT)
        expected = [
            TextNode("", TextType.TEXT),
            TextNode("Italic text", TextType.ITALIC),
            TextNode(" right at the start.", TextType.TEXT),
        ]
        self.assertEqual(split_nodes_delimiter([node], "_", TextType.ITALIC), expected)

    def test_entire_string_delimited(self):
        node = TextNode("**Full bold text**", TextType.TEXT)
        expected = [
            TextNode("", TextType.TEXT),  # The part before the first delimiter
            TextNode("Full bold text", TextType.BOLD),
            TextNode("", TextType.TEXT),  # The part after the last delimiter
        ]
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), expected)

    def test_no_delimiter_present(self):
        node = TextNode("This is just plain text", TextType.TEXT)
        expected = [TextNode("This is just plain text", TextType.TEXT)]
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), expected)

    def test_empty_delimited_content(self):
        node = TextNode("Text with ****empty bold", TextType.TEXT)
        expected = [
            TextNode("Text with ", TextType.TEXT),
            TextNode("", TextType.BOLD),  # Empty content inside the delimiters
            TextNode("empty bold", TextType.TEXT),
        ]
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), expected)

    def test_missing_delimited(self):
        node = TextNode("This is not **correct bold.", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [node], "**", TextType.BOLD)
        bad_node = TextNode("This is missing a delimiter", TextType.TEXT)
        self.assertRaises(
            Exception, split_nodes_delimiter, [bad_node], "", TextType.BOLD
        )
        self.assertRaises(
            Exception, split_nodes_delimiter, [bad_node], "**", TextType.TEXT
        )

    def test_text_return(self):
        node = TextNode("Just normal text", TextType.BOLD)
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), [node])


if __name__ == "__main__":
    unittest.main()
